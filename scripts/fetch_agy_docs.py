#!/usr/bin/env python3
"""Fetch Antigravity (agy) CLI markdown docs.

antigravity.google now publishes docs as an Astro site with:

- an LLM index at `/llms.txt` (sectioned Documentation links),
- optional completeness via `/sitemap.xml`,
- raw Markdown at `/docs/<slug>.md` (`Content-Type: text/markdown`).

This fetcher:

  1. loads `/llms.txt` and extracts Documentation entries + sections,
  2. optionally merges `/docs/*` URLs from the sitemap that are missing there,
  3. downloads each `/docs/<slug>.md`,
  4. mirrors them under docs/<output_subdir>/<slug>.md and writes a manifest.

Some responses are gzip-encoded; bodies are decompressed from the
Content-Encoding header or gzip magic bytes.
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
from typing import Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree

import certifi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "sources.json"
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "docs_manifest.json"

USER_AGENT = "agy-cli-docs-mirror/1.0"

# `- [label](https://antigravity.google/docs/...): description`
LLMS_DOC_LINK_REGEX = re.compile(
    r"^- \[([^\]]+)\]\((https?://[^)]+/docs/[^)]+)\):\s*(.*)$"
)
LLMS_SECTION_REGEX = re.compile(r"^###\s+(.+)$")

REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRIES = 4
BASE_BACKOFF_SECONDS = 1.5
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
UNLISTED_SECTION = "Unlisted"


@dataclass(frozen=True)
class Source:
    source_id: str
    site_root: str
    llms_path: str
    sitemap_path: str
    docs_path_prefix: str
    include_sitemap_docs: bool
    output_subdir: str


@dataclass(frozen=True)
class DocPage:
    section: str
    slug: str
    url: str
    rel_path: str
    label: str


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
        sitemap_path = raw.get("sitemap_path", "/sitemap.xml")
        docs_path_prefix = raw.get("docs_path_prefix", "/docs/")
        include_sitemap_docs = bool(raw.get("include_sitemap_docs", True))
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
                sitemap_path=sitemap_path,
                docs_path_prefix="/" + docs_path_prefix.strip("/") + "/",
                include_sitemap_docs=include_sitemap_docs,
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
    elif encoding and encoding not in {"identity", "gzip"}:
        raise RuntimeError(f"Unsupported content-encoding: {encoding}")
    return raw.decode("utf-8")


def fetch_bytes(url: str) -> Tuple[bytes, str | None, str | None]:
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/markdown,text/plain,application/xml,text/xml,text/html,*/*",
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
    parsed = urlparse(url)
    path = parsed.path or ""
    prefix = source.docs_path_prefix
    if not path.startswith(prefix):
        return None
    slug = path[len(prefix) :].strip("/")
    if not slug or slug.endswith(".md"):
        return None
    return slug


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
        if not slug:
            continue

        pages[slug] = DocPage(
            section=section or UNLISTED_SECTION,
            slug=slug,
            url=markdown_url_for_slug(source, slug),
            rel_path=safe_rel_path(slug),
            label=label,
        )

    return pages


def parse_sitemap_doc_slugs(sitemap_text: str, source: Source) -> List[str]:
    # ElementTree tolerates default namespaces via local-name matching below.
    try:
        root = ElementTree.fromstring(sitemap_text)
    except ElementTree.ParseError as exc:
        raise RuntimeError(f"Failed to parse sitemap XML: {exc}") from exc

    slugs: List[str] = []
    seen: set[str] = set()
    for node in root.iter():
        if not node.tag.endswith("loc") or node.text is None:
            continue
        loc = node.text.strip().rstrip("/")
        slug = docs_slug_from_url(loc, source)
        if not slug or slug in seen:
            continue
        seen.add(slug)
        slugs.append(slug)
    return sorted(slugs)


def discover_doc_pages(source: Source) -> List[DocPage]:
    llms_url = urljoin(source.site_root + "/", source.llms_path.lstrip("/"))
    llms_text, _ = fetch_text(llms_url)
    pages = parse_llms_doc_pages(llms_text, source)
    if not pages:
        raise RuntimeError(f"No Documentation entries found in {llms_url}")

    sitemap_added = 0
    if source.include_sitemap_docs:
        sitemap_url = urljoin(source.site_root + "/", source.sitemap_path.lstrip("/"))
        sitemap_text, _ = fetch_text(sitemap_url)
        for slug in parse_sitemap_doc_slugs(sitemap_text, source):
            if slug in pages:
                continue
            pages[slug] = DocPage(
                section=UNLISTED_SECTION,
                slug=slug,
                url=markdown_url_for_slug(source, slug),
                rel_path=safe_rel_path(slug),
                label=slug,
            )
            sitemap_added += 1

    print(
        f"[INFO] Source={source.source_id} llms_pages={len(pages) - sitemap_added} "
        f"sitemap_added={sitemap_added}"
    )
    return [pages[slug] for slug in sorted(pages.keys())]


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


def main() -> int:
    strict_fetch = os.environ.get("STRICT_FETCH", "0") == "1"

    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    sources = load_sources(CONFIG_PATH)
    existing_manifest = load_existing_manifest(MANIFEST_PATH)
    existing_files = existing_manifest.get("files", {})

    new_files: Dict[str, Dict] = {}

    fetch_started_at = now_iso()
    total_pages = 0
    successful_pages = 0
    failed_pages: List[Tuple[str, str]] = []

    for source in sources:
        print(f"[INFO] Source={source.source_id} site={source.site_root}")
        pages = discover_doc_pages(source)
        print(f"[INFO] Source={source.source_id} discovered={len(pages)}")
        total_pages += len(pages)

        source_root = DOCS_ROOT / source.output_subdir
        source_root.mkdir(parents=True, exist_ok=True)

        for page in pages:
            manifest_key = f"{source.output_subdir}/{page.rel_path}"
            try:
                dest = source_root / page.rel_path
                dest.parent.mkdir(parents=True, exist_ok=True)

                content, content_type = fetch_text(page.url)
                if not looks_like_markdown(content, content_type):
                    raise RuntimeError(
                        f"Expected markdown from {page.url}, got content-type={content_type!r}"
                    )

                digest = sha256_text(content)

                existing = existing_files.get(manifest_key, {})
                if existing.get("sha256") != digest or not dest.exists():
                    dest.write_text(content, encoding="utf-8")

                new_files[manifest_key] = {
                    "source": source.source_id,
                    "section": page.section,
                    "slug": page.slug,
                    "label": page.label,
                    "url": page.url,
                    "sha256": digest,
                    "bytes": len(content.encode("utf-8")),
                    "fetched_at": fetch_started_at,
                }
                successful_pages += 1
                print(f"[OK] {manifest_key}")
            except Exception as exc:  # noqa: BLE001
                print(f"[WARN] failed url={page.url} err={exc}")
                failed_pages.append((page.url, str(exc)))

    previous_paths = set(existing_files.keys())
    current_paths = set(new_files.keys())
    removed_paths = sorted(previous_paths - current_paths)

    for removed in removed_paths:
        file_path = DOCS_ROOT / removed
        if file_path.exists():
            file_path.unlink()
            remove_empty_dirs(file_path.parent, DOCS_ROOT)

    manifest = {
        "generated_at": now_iso(),
        "tool": "scripts/fetch_agy_docs.py",
        "strict_fetch": strict_fetch,
        "sources": [
            {
                "id": s.source_id,
                "site_root": s.site_root,
                "llms_path": s.llms_path,
                "sitemap_path": s.sitemap_path,
                "docs_path_prefix": s.docs_path_prefix,
                "include_sitemap_docs": s.include_sitemap_docs,
                "output_subdir": s.output_subdir,
            }
            for s in sources
        ],
        "stats": {
            "total_pages": total_pages,
            "successful_pages": successful_pages,
            "failed_pages": len(failed_pages),
            "removed_files": len(removed_paths),
        },
        "failed": [{"url": url, "error": err} for url, err in failed_pages],
        "files": {k: new_files[k] for k in sorted(new_files.keys())},
    }

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print("\n[SUMMARY]")
    print(f"total_pages={total_pages}")
    print(f"successful_pages={successful_pages}")
    print(f"failed_pages={len(failed_pages)}")
    print(f"removed_files={len(removed_paths)}")

    if failed_pages and strict_fetch:
        print("[ERROR] STRICT_FETCH=1 and failures detected")
        return 1

    if successful_pages == 0:
        print("[ERROR] No documents fetched successfully")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
