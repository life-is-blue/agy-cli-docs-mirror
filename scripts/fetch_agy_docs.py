#!/usr/bin/env python3
"""Fetch Antigravity (agy) CLI markdown docs with Starlight sidebar alignment.

antigravity.google publishes docs as an Astro Starlight site:
- Raw Markdown is available at `/docs/<slug>.md` (`Content-Type: text/markdown`),
- The site sidebar DOM in HTML exposes the complete multi-level navigation tree,
- `/llms.txt` provides an LLM resource directory.

This fetcher:
  1. Parses the official Astro Starlight sidebar navigation tree from HTML,
  2. Integrates any additional pages listed in `/llms.txt` into the navigation tree,
  3. Provides a fallback navigation generator if HTML discovery is unavailable,
  4. Disables file deletions on degraded discovery to protect against accidental data loss,
  5. Uses staged downloading and verifies invariants BEFORE committing any changes to disk,
  6. Preserves existing fetched_at timestamps on unchanged files for clean Git diffs,
  7. Enforces strict invariant verification in all modes: Manifest Files == Sidebar Leaves == SUMMARY Links.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import re
import ssl
import time
import zlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import certifi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "sources.json"
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "docs_manifest.json"
STARLIGHT_SIDEBAR_PATH = DOCS_ROOT / "starlight_sidebar.json"
SUMMARY_PATH = DOCS_ROOT / "SUMMARY.md"

USER_AGENT = "agy-cli-docs-mirror/1.0"

# `- [label](https://antigravity.google/docs/...): description`
LLMS_DOC_LINK_REGEX = re.compile(
    r"^- \[([^\]]+)\]\((https?://[^)]+/docs/[^)]+)\):"
)
LLMS_SECTION_REGEX = re.compile(r"^###\s+(.+)$")

REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRIES = 4
BASE_BACKOFF_SECONDS = 1.5
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


@dataclass(frozen=True)
class Source:
    source_id: str
    site_root: str
    llms_path: str
    docs_path_prefix: str
    output_subdir: str


@dataclass(frozen=True)
class DocPage:
    section: str
    slug: str
    url: str
    rel_path: str
    label: str
    category_path: Tuple[str, ...] = ()
    sidebar_label: Optional[str] = None
    badge: Optional[Dict[str, str]] = None


@dataclass(frozen=True)
class DiscoveryResult:
    sidebar_tree: List[Dict[str, Any]]
    pages: List[DocPage]
    is_degraded: bool  # True if HTML sidebar failed and llms.txt fallback was used


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_sources(config_path: Path) -> List[Source]:
    payload = json.loads(config_path.read_text(encoding="utf-8"))
    raw_sources = payload.get("sources", [])
    if not raw_sources:
        raise RuntimeError("No sources configured in config/sources.json")

    result: List[Source] = []
    for raw in raw_sources:
        source_id = raw.get("id")
        site_root = raw.get("site_root")
        llms_path = raw.get("llms_path", "/llms.txt")
        docs_path_prefix = raw.get("docs_path_prefix", "/docs/")
        output_subdir = raw.get("output_subdir")

        if not source_id or not site_root or not output_subdir:
            raise RuntimeError(f"Invalid source entry: {raw}")

        if not docs_path_prefix.startswith("/"):
            raise RuntimeError(f"docs_path_prefix must start with '/': {docs_path_prefix}")

        result.append(
            Source(
                source_id=source_id,
                site_root=site_root.rstrip("/"),
                llms_path=llms_path,
                docs_path_prefix="/" + docs_path_prefix.strip("/") + "/",
                output_subdir=output_subdir,
            )
        )
    return result


def _decode_body(raw: bytes, content_encoding: str | None) -> str:
    encoding = (content_encoding or "").lower()
    if encoding == "gzip" or (not encoding and raw[:2] == b"\x1f\x8b"):
        raw = gzip.decompress(raw)
    elif encoding == "deflate":
        raw = zlib.decompress(raw)
    elif encoding and encoding != "identity":
        raise RuntimeError(f"Unsupported content-encoding: {encoding}")
    return raw.decode("utf-8")


def fetch_bytes(url: str) -> Tuple[bytes, str | None, str | None]:
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,text/markdown,text/plain,*/*",
                "Accept-Encoding": "gzip",
            },
        )
        try:
            with urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS, context=SSL_CONTEXT) as response:
                raw = response.read()
                content_encoding = response.headers.get("Content-Encoding")
                content_type = response.headers.get("Content-Type")
            return raw, content_encoding, content_type
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt == MAX_RETRIES:
                break
            sleep_seconds = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            time.sleep(sleep_seconds)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def fetch_text(url: str) -> Tuple[str, str | None]:
    raw, content_encoding, content_type = fetch_bytes(url)
    return _decode_body(raw, content_encoding), content_type


def docs_slug_from_url(url: str, source: Source) -> Optional[str]:
    if not url:
        return None

    full_url = urljoin(source.site_root + "/", url)
    parsed = urlparse(full_url)
    expected_host = urlparse(source.site_root).netloc
    if parsed.netloc and parsed.netloc != expected_host:
        return None

    path = parsed.path or ""
    prefix = source.docs_path_prefix

    if path.rstrip("/") == prefix.rstrip("/"):
        return "home"

    if not path.startswith(prefix):
        return None

    slug = path[len(prefix) :].strip("/")
    if slug.endswith(".md"):
        slug = slug[:-3]

    if not slug:
        return "home"

    parts = slug.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        return None

    return "/".join(parts)


def markdown_url_for_slug(source: Source, slug: str) -> str:
    return f"{source.site_root}{source.docs_path_prefix}{slug}.md"


def safe_rel_path(slug: str) -> str:
    slug = slug.strip().strip("/")
    if not slug:
        raise RuntimeError("Empty slug")
    parts = slug.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise RuntimeError(f"Unsafe slug: {slug}")
    return "/".join(parts) + ".md"


def parse_badge(el: Any) -> Optional[Dict[str, str]]:
    badge_el = el.find("span", class_=lambda c: c and "sl-badge" in c)
    if not badge_el:
        return None
    badge_text = badge_el.get_text(strip=True)
    classes = badge_el.get("class", [])
    variant = "default"
    for v in ["note", "tip", "danger", "caution", "success"]:
        if v in classes:
            variant = v
            break
    return {"text": badge_text, "variant": variant}


def extract_label_without_badge(container: Any) -> str:
    label_spans = [
        s for s in container.find_all("span", recursive=False)
        if "sl-badge" not in s.get("class", [])
    ]
    if label_spans:
        return label_spans[0].get_text(strip=True)
    return container.get_text(strip=True)


def parse_starlight_sidebar_dom(
    ul_el: Any,
    source: Source,
    parent_categories: Tuple[str, ...] = (),
) -> Tuple[List[Dict[str, Any]], Dict[str, DocPage]]:
    sidebar_items: List[Dict[str, Any]] = []
    doc_pages: Dict[str, DocPage] = {}

    for li in ul_el.find_all("li", recursive=False):
        details = li.find("details", recursive=False)
        if details:
            summary = details.find("summary", recursive=False)
            group_label_span = summary.find("span", class_="group-label") if summary else None
            badge = parse_badge(group_label_span or summary) if summary else None

            if group_label_span:
                group_label = extract_label_without_badge(group_label_span)
            elif summary:
                group_label = summary.get_text(" ", strip=True)
            else:
                group_label = "Group"

            sub_ul = details.find("ul", recursive=False)
            sub_items: List[Dict[str, Any]] = []
            if sub_ul:
                current_categories = parent_categories + (group_label,)
                sub_items, sub_pages = parse_starlight_sidebar_dom(
                    sub_ul, source, current_categories
                )
                doc_pages.update(sub_pages)

            group_obj: Dict[str, Any] = {
                "label": group_label,
                "collapsed": True,
                "items": sub_items,
            }
            if badge:
                group_obj["badge"] = badge
            sidebar_items.append(group_obj)
            continue

        link = li.find("a", recursive=False)
        if link:
            href = link.get("href", "")
            slug = docs_slug_from_url(href, source)
            if not slug:
                continue

            label = extract_label_without_badge(link)
            badge = parse_badge(link)

            starlight_slug = f"{source.output_subdir}/{slug}" if source.output_subdir else slug
            item_obj: Dict[str, Any] = {
                "label": label,
                "slug": starlight_slug,
            }
            if badge:
                item_obj["badge"] = badge
            sidebar_items.append(item_obj)

            top_section = parent_categories[0] if parent_categories else "Documentation"
            doc_pages[slug] = DocPage(
                section=top_section,
                slug=slug,
                url=markdown_url_for_slug(source, slug),
                rel_path=safe_rel_path(slug),
                label=label,
                category_path=parent_categories,
                sidebar_label=label,
                badge=badge,
            )

    return sidebar_items, doc_pages


def discover_sidebar_from_html(
    source: Source,
    fetch_text_fn: Callable[[str], Tuple[str, str | None]] = fetch_text,
) -> Tuple[List[Dict[str, Any]], Dict[str, DocPage]]:
    candidate_urls = [
        f"{source.site_root}{source.docs_path_prefix}overview",
        f"{source.site_root}{source.docs_path_prefix}home",
        f"{source.site_root}{source.docs_path_prefix}cli/overview",
    ]

    for page_url in candidate_urls:
        try:
            html_text, _ = fetch_text_fn(page_url)
            soup = BeautifulSoup(html_text, "html.parser")
            sidebar_nav = soup.find("nav", {"aria-label": "Main"}) or soup.find(
                "nav", class_=lambda c: c and "sidebar" in c
            )
            if not sidebar_nav:
                continue
            top_ul = sidebar_nav.find("ul", class_="top-level")
            if not top_ul:
                continue

            sidebar_items, doc_pages = parse_starlight_sidebar_dom(top_ul, source)
            if sidebar_items and doc_pages:
                return sidebar_items, doc_pages
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] Failed to inspect sidebar from {page_url}: {exc}")

    return [], {}


def parse_llms_doc_pages(llms_text: str, source: Source) -> Dict[str, DocPage]:
    pages: Dict[str, DocPage] = {}
    in_documentation = False
    section: Optional[str] = None

    for raw_line in llms_text.splitlines():
        line = raw_line.rstrip()
        if line.strip() == "## Documentation":
            in_documentation = True
            section = None
            continue

        if in_documentation and line.startswith("## ") and not line.startswith("###"):
            break

        if not in_documentation:
            continue

        section_match = LLMS_SECTION_REGEX.match(line)
        if section_match:
            section = section_match.group(1).strip()
            continue

        link_match = LLMS_DOC_LINK_REGEX.match(line)
        if not link_match:
            continue

        label = link_match.group(1).strip()
        url = link_match.group(2).strip().rstrip("/")
        slug = docs_slug_from_url(url, source)
        if not slug or not section:
            continue

        pages[slug] = DocPage(
            section=section,
            slug=slug,
            url=markdown_url_for_slug(source, slug),
            rel_path=safe_rel_path(slug),
            label=label,
            category_path=(section,),
            sidebar_label=label,
        )

    return pages


def build_fallback_sidebar_from_llms(
    llms_pages: Dict[str, DocPage],
    source: Source,
) -> List[Dict[str, Any]]:
    """Build a valid Starlight sidebar tree when HTML DOM discovery is unavailable."""
    sections: Dict[str, List[Dict[str, Any]]] = {}
    for slug in sorted(llms_pages.keys()):
        page = llms_pages[slug]
        starlight_slug = f"{source.output_subdir}/{slug}" if source.output_subdir else slug
        item_obj: Dict[str, Any] = {
            "label": page.label,
            "slug": starlight_slug,
        }
        sections.setdefault(page.section, []).append(item_obj)

    fallback_tree: List[Dict[str, Any]] = []
    for section_name, items in sections.items():
        if section_name.lower() == "home" and len(items) == 1:
            fallback_tree.append(items[0])
        else:
            fallback_tree.append({
                "label": section_name,
                "collapsed": True,
                "items": items,
            })
    return fallback_tree


def merge_supplemental_pages_into_sidebar_tree(
    sidebar_tree: List[Dict[str, Any]],
    extra_pages: List[DocPage],
    source: Source,
) -> List[Dict[str, Any]]:
    """Ensure any pages discovered only in llms.txt are integrated into the sidebar tree."""
    if not extra_pages:
        return sidebar_tree

    extra_by_section: Dict[str, List[DocPage]] = {}
    for page in extra_pages:
        extra_by_section.setdefault(page.section, []).append(page)

    for section_name, pages in extra_by_section.items():
        matched_group: Optional[Dict[str, Any]] = None
        for group in sidebar_tree:
            if group.get("label", "").lower() == section_name.lower() and "items" in group:
                matched_group = group
                break

        new_items = []
        for page in pages:
            starlight_slug = f"{source.output_subdir}/{page.slug}" if source.output_subdir else page.slug
            new_items.append({"label": page.label, "slug": starlight_slug})

        if matched_group:
            matched_group["items"].extend(new_items)
        else:
            sidebar_tree.append({
                "label": section_name,
                "collapsed": True,
                "items": new_items,
            })

    return sidebar_tree


def discover_all_doc_pages(
    source: Source,
    fetch_text_fn: Callable[[str], Tuple[str, str | None]] = fetch_text,
) -> DiscoveryResult:
    sidebar_tree, sidebar_pages = discover_sidebar_from_html(source, fetch_text_fn)
    is_degraded = False

    if sidebar_tree:
        print(f"[INFO] Discovered {len(sidebar_pages)} pages from Starlight sidebar DOM")
    else:
        print("[WARN] HTML sidebar discovery returned no items; checking llms.txt fallback")

    llms_pages: Dict[str, DocPage] = {}
    try:
        llms_url = urljoin(source.site_root + "/", source.llms_path.lstrip("/"))
        llms_text, _ = fetch_text_fn(llms_url)
        llms_pages = parse_llms_doc_pages(llms_text, source)
        print(f"[INFO] Discovered {len(llms_pages)} pages from {llms_url}")
    except Exception as exc:  # noqa: BLE001
        print(f"[WARN] Failed to fetch llms.txt ({exc})")

    if not sidebar_tree:
        if llms_pages:
            print("[WARN] HTML sidebar discovery failed; generating fallback tree from llms.txt (DELETIONS DISABLED)")
            is_degraded = True
            sidebar_tree = build_fallback_sidebar_from_llms(llms_pages, source)
            sidebar_pages = llms_pages
        else:
            raise RuntimeError(f"No documentation pages discovered for source {source.source_id}")

    merged_pages: Dict[str, DocPage] = dict(sidebar_pages)
    extra_from_llms: List[DocPage] = []
    for slug, page in llms_pages.items():
        if slug not in merged_pages:
            merged_pages[slug] = page
            extra_from_llms.append(page)

    if extra_from_llms:
        print(f"[INFO] Merging {len(extra_from_llms)} supplemental llms.txt pages into sidebar tree")
        sidebar_tree = merge_supplemental_pages_into_sidebar_tree(
            sidebar_tree, extra_from_llms, source
        )

    return DiscoveryResult(
        sidebar_tree=sidebar_tree,
        pages=[merged_pages[slug] for slug in sorted(merged_pages.keys())],
        is_degraded=is_degraded,
    )


def generate_summary_md(sidebar_tree: List[Dict[str, Any]]) -> str:
    lines = ["# Antigravity Documentation\n"]

    def walk(items: List[Dict[str, Any]], depth: int = 0) -> None:
        indent = "  " * depth
        for item in items:
            label = item.get("label", "")
            badge = item.get("badge")
            badge_str = f" `{badge['text']}`" if badge and "text" in badge else ""
            if "items" in item:
                lines.append(f"{indent}- {label}{badge_str}")
                walk(item["items"], depth + 1)
            elif "slug" in item:
                slug = item["slug"]
                rel_file = f"{slug}.md"
                lines.append(f"{indent}- [{label}]({rel_file}){badge_str}")

    walk(sidebar_tree)
    return "\n".join(lines) + "\n"


def extract_sidebar_leaf_slugs(tree: List[Dict[str, Any]]) -> List[str]:
    slugs: List[str] = []

    def walk(items: List[Dict[str, Any]]) -> None:
        for it in items:
            if "items" in it:
                walk(it["items"])
            elif "slug" in it:
                slugs.append(it["slug"])

    walk(tree)
    return sorted(slugs)


def extract_summary_links(summary_text: str) -> List[str]:
    matches = re.findall(r"\]\(([^)]+\.md)\)", summary_text)
    return sorted([m[:-3] for m in matches])


def looks_like_markdown(content: str, content_type: str | None) -> bool:
    ct = (content_type or "").lower()
    if "html" in ct:
        return False
    stripped = content.lstrip()
    if stripped.startswith("<!DOCTYPE") or stripped.lower().startswith("<html"):
        return False
    if "markdown" in ct or "text/plain" in ct:
        return True
    return stripped.startswith("#") or stripped.startswith("---")


def sha256_text(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_existing_manifest(path: Path) -> Dict:
    if not path.exists():
        return {"files": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def remove_empty_dirs(start: Path, stop: Path) -> None:
    current = start
    while current != stop and current.exists():
        if any(current.iterdir()):
            break
        current.rmdir()
        current = current.parent


def check_deletion_integrity(
    discovered_keys: Set[str],
    existing_files: Dict[str, Any],
    is_degraded: bool,
    max_drop_ratio: float = 0.2,
) -> Tuple[bool, Optional[str]]:
    """Verify if the discovery result has sufficient completeness proof to authorize deletions."""
    if is_degraded:
        return False, "Discovery degraded (HTML sidebar unavailable)"

    previous_keys = set(existing_files.keys())
    if not previous_keys:
        return True, None

    previous_count = len(previous_keys)
    discovered_count = len(discovered_keys)

    # For established repos with >= 5 files, an unannounced loss of > 20% files indicates incomplete discovery
    if previous_count >= 5 and discovered_count < int(previous_count * (1.0 - max_drop_ratio)):
        return False, (
            f"Discovery integrity check failed: discovered {discovered_count} pages vs "
            f"{previous_count} previously tracked pages (drop exceeds {int(max_drop_ratio * 100)}% threshold). "
            "Deletions blocked to protect against partial discovery/upstream layout truncation."
        )

    return True, None


def sync_docs(
    config_path: Path = CONFIG_PATH,
    docs_root: Path = DOCS_ROOT,
    manifest_path: Path = MANIFEST_PATH,
    sidebar_path: Path = STARLIGHT_SIDEBAR_PATH,
    summary_path: Path = SUMMARY_PATH,
    strict_fetch: bool = False,
    fetch_text_fn: Callable[[str], Tuple[str, str | None]] = fetch_text,
) -> Tuple[int, Dict[str, Any]]:
    """Execute complete doc synchronization with atomic staging and strict validation."""
    docs_root.mkdir(parents=True, exist_ok=True)
    sources = load_sources(config_path)
    existing_manifest = load_existing_manifest(manifest_path)
    existing_files = existing_manifest.get("files", {})

    fetch_started_at = now_iso()
    staged_files: Dict[str, Dict[str, Any]] = {}
    staged_writes: Dict[Path, str] = {}  # dest_path -> content
    combined_sidebar_tree: List[Dict[str, Any]] = []
    discovered_target_keys: Set[str] = set()

    any_source_degraded = False
    total_pages = 0
    successful_pages = 0
    failed_pages: List[Tuple[str, str]] = []

    for source in sources:
        print(f"[INFO] Source={source.source_id} site={source.site_root}")
        discovery = discover_all_doc_pages(source, fetch_text_fn)
        if discovery.is_degraded:
            any_source_degraded = True
        combined_sidebar_tree.extend(discovery.sidebar_tree)
        print(f"[INFO] Source={source.source_id} total_target_pages={len(discovery.pages)}")
        total_pages += len(discovery.pages)

        source_root = docs_root / source.output_subdir

        for page in discovery.pages:
            manifest_key = f"{source.output_subdir}/{page.rel_path}"
            discovered_target_keys.add(manifest_key)
            dest = source_root / page.rel_path

            try:
                content, content_type = fetch_text_fn(page.url)
                if not looks_like_markdown(content, content_type):
                    raise RuntimeError(
                        f"Expected markdown from {page.url}, got content-type={content_type!r}"
                    )

                digest = sha256_text(content)
                existing = existing_files.get(manifest_key, {})
                content_changed = existing.get("sha256") != digest or not dest.exists()

                if content_changed:
                    staged_writes[dest] = content
                    fetched_at = fetch_started_at
                else:
                    fetched_at = existing.get("fetched_at", fetch_started_at)

                entry: Dict[str, Any] = {
                    "source": source.source_id,
                    "section": page.section,
                    "category_path": list(page.category_path),
                    "slug": page.slug,
                    "label": page.label,
                    "url": page.url,
                    "sha256": digest,
                    "bytes": len(content.encode("utf-8")),
                    "fetched_at": fetched_at,
                }
                if page.sidebar_label:
                    entry["sidebar_label"] = page.sidebar_label
                if page.badge:
                    entry["badge"] = page.badge

                staged_files[manifest_key] = entry
                successful_pages += 1
                print(f"[OK] {manifest_key}")
            except Exception as exc:  # noqa: BLE001
                print(f"[WARN] failed url={page.url} err={exc}")
                failed_pages.append((page.url, str(exc)))

                # Defensive preservation: If existing file is already on disk, preserve it
                if manifest_key in existing_files and dest.exists():
                    print(f"[INFO] Retaining existing local copy for failed page: {manifest_key}")
                    preserved_entry = dict(existing_files[manifest_key])
                    preserved_entry["last_fetch_status"] = "failed"
                    preserved_entry["last_fetch_error"] = str(exc)
                    staged_files[manifest_key] = preserved_entry

    summary_content = generate_summary_md(combined_sidebar_tree) if combined_sidebar_tree else ""

    # Invariant Verification (Hard Contract across ALL modes)
    sidebar_slugs = extract_sidebar_leaf_slugs(combined_sidebar_tree)
    summary_slugs = extract_summary_links(summary_content)
    staged_slugs = sorted([k[:-3] for k in staged_files.keys()])

    invariant_errors: List[str] = []
    if sidebar_slugs != staged_slugs:
        diff_sm = set(sidebar_slugs) ^ set(staged_slugs)
        invariant_errors.append(f"Sidebar slugs mismatch with Staged files: diff={diff_sm}")
    if summary_slugs != staged_slugs:
        diff_sum = set(summary_slugs) ^ set(staged_slugs)
        invariant_errors.append(f"SUMMARY.md links mismatch with Staged files: diff={diff_sum}")

    # Determine if this sync can be committed
    if failed_pages and strict_fetch:
        print(f"[ERROR] STRICT_FETCH=1 and {len(failed_pages)} failures detected; aborting without disk mutations.")
        return 1, {"error": "strict_fetch_failures", "failed": failed_pages}

    if invariant_errors:
        for err in invariant_errors:
            print(f"[ERROR] Invariant violated: {err}")
        print("[ERROR] Aborting sync to prevent committing inconsistent artifacts.")
        return 1, {"error": "invariant_violation", "details": invariant_errors}

    if successful_pages == 0 and total_pages > 0:
        print("[ERROR] Zero documents fetched successfully; aborting sync.")
        return 1, {"error": "zero_successful_pages"}

    # Deletion Integrity Check
    allow_deletions, deletion_ineligibility_reason = check_deletion_integrity(
        discovered_target_keys, existing_files, any_source_degraded
    )

    if not allow_deletions and strict_fetch and (set(existing_files.keys()) - discovered_target_keys):
        print(f"[ERROR] STRICT_FETCH=1 and deletion integrity verification failed: {deletion_ineligibility_reason}")
        return 1, {"error": "deletion_integrity_failed", "reason": deletion_ineligibility_reason}

    # --- ATOMIC COMMIT PHASE (All validations passed) ---

    # 1. Write updated markdown files to disk
    for dest_path, content in staged_writes.items():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(content, encoding="utf-8")

    # 2. Deletion handling protected by integrity verification
    previous_paths = set(existing_files.keys())
    if not allow_deletions:
        print(f"[WARN] {deletion_ineligibility_reason}; skipping file deletions to protect data.")
        removed_paths: List[str] = []
        # Preserve previous files in manifest that were not in discovered_target_keys
        for prev_key in sorted(previous_paths - discovered_target_keys):
            if prev_key in existing_files:
                staged_files[prev_key] = existing_files[prev_key]
    else:
        removed_paths = sorted(previous_paths - discovered_target_keys)

    for removed in removed_paths:
        file_path = docs_root / removed
        if file_path.exists():
            print(f"[INFO] Removing deleted upstream document: {removed}")
            file_path.unlink()
            remove_empty_dirs(file_path.parent, docs_root)


    # 3. Write Starlight sidebar configuration and SUMMARY.md
    if combined_sidebar_tree:
        sidebar_path.write_text(
            json.dumps(combined_sidebar_tree, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"[INFO] Wrote Starlight sidebar configuration to {sidebar_path}")

        summary_path.write_text(summary_content, encoding="utf-8")
        print(f"[INFO] Wrote SUMMARY.md index to {summary_path}")

    # 4. Write manifest
    manifest = {
        "generated_at": now_iso(),
        "tool": "scripts/fetch_agy_docs.py",
        "strict_fetch": strict_fetch,
        "is_degraded": any_source_degraded,
        "sources": [
            {
                "id": s.source_id,
                "site_root": s.site_root,
                "llms_path": s.llms_path,
                "docs_path_prefix": s.docs_path_prefix,
                "output_subdir": s.output_subdir,
            }
            for s in sources
        ],
        "sidebar_file": str(sidebar_path.relative_to(docs_root.parent) if sidebar_path.is_relative_to(docs_root.parent) else sidebar_path.name),
        "summary_file": str(summary_path.relative_to(docs_root.parent) if summary_path.is_relative_to(docs_root.parent) else summary_path.name),
        "stats": {
            "total_pages": total_pages,
            "successful_pages": successful_pages,
            "failed_pages": len(failed_pages),
            "removed_files": len(removed_paths),
            "invariants_passed": True,
        },
        "failed": [{"url": url, "error": err} for url, err in failed_pages],
        "files": {k: staged_files[k] for k in sorted(staged_files.keys())},
    }

    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print("\n[SUMMARY]")
    print(f"total_pages={total_pages}")
    print(f"successful_pages={successful_pages}")
    print(f"failed_pages={len(failed_pages)}")
    print(f"removed_files={len(removed_paths)}")
    print(f"is_degraded={any_source_degraded}")
    print("invariants_passed=True")

    return 0, manifest


def main() -> int:
    strict_fetch = os.environ.get("STRICT_FETCH", "0") == "1"
    code, _ = sync_docs(strict_fetch=strict_fetch)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
