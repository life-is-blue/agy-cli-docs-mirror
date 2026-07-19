#!/usr/bin/env python3
"""Fetch Antigravity (agy) CLI markdown docs.

Unlike a plain llms.txt mirror, antigravity.google is a single-page app:
- `/docs/<slug>` routes all return the same JS shell (content is rendered client-side).
- The real markdown lives at `/assets/docs/<path>/<filename>.md`.
- The slug -> (path, filename) mapping only exists inside the hashed `main-*.js` bundle.

So this fetcher:
  1. loads the index HTML and discovers the current `main-*.js` bundle,
  2. extracts the doc page table ({section, path, slug, filename}) from the bundle,
  3. downloads each `/assets/docs/<path>/<filename>.md`,
  4. mirrors them under docs/<output_subdir>/<slug>.md and writes a manifest.

The site serves every asset gzip-encoded regardless of Accept-Encoding, so responses
are decompressed explicitly.
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
from typing import Dict, List, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import certifi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "sources.json"
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "docs_manifest.json"

USER_AGENT = "agy-cli-docs-mirror/1.0"

# `main-THARYY64.js` style bundle reference in index.html.
BUNDLE_REGEX = re.compile(r"main-[A-Za-z0-9]+\.js")
# Minified page table entries: {section:"...",path:"...",slug:"...",filename:"..."}
PAGE_ENTRY_REGEX = re.compile(
    r'\{section:"(?P<section>[^"]*)",path:"(?P<path>[^"]*)",'
    r'slug:"(?P<slug>[^"]*)",filename:"(?P<filename>[^"]*)"\}'
)

REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRIES = 4
BASE_BACKOFF_SECONDS = 1.5
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


@dataclass(frozen=True)
class Source:
    source_id: str
    site_root: str
    index_path: str
    docs_asset_prefix: str
    output_subdir: str


@dataclass(frozen=True)
class DocPage:
    section: str
    slug: str
    url: str
    rel_path: str


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
        index_path = raw.get("index_path", "/")
        docs_asset_prefix = raw.get("docs_asset_prefix")
        output_subdir = raw.get("output_subdir")

        if not source_id or not site_root or not docs_asset_prefix or not output_subdir:
            raise RuntimeError(f"Invalid source entry: {raw}")

        if not docs_asset_prefix.startswith("/"):
            raise RuntimeError(f"docs_asset_prefix must start with '/': {docs_asset_prefix}")

        result.append(
            Source(
                source_id=source_id,
                site_root=site_root.rstrip("/"),
                index_path=index_path,
                docs_asset_prefix="/" + docs_asset_prefix.strip("/"),
                output_subdir=output_subdir,
            )
        )
    return result


def _decode_body(raw: bytes, content_encoding: str | None) -> str:
    encoding = (content_encoding or "").lower()
    if encoding == "gzip":
        raw = gzip.decompress(raw)
    elif encoding == "deflate":
        raw = zlib.decompress(raw)
    elif encoding and encoding != "identity":
        raise RuntimeError(f"Unsupported content-encoding: {encoding}")
    return raw.decode("utf-8")


def fetch_text(url: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/markdown,text/html,text/plain,*/*",
                "Accept-Encoding": "gzip",
            },
        )
        try:
            with urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS, context=SSL_CONTEXT) as response:
                raw = response.read()
                content_encoding = response.headers.get("Content-Encoding")
            return _decode_body(raw, content_encoding)
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt == MAX_RETRIES:
                break
            sleep_seconds = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            time.sleep(sleep_seconds)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def discover_bundle_url(source: Source) -> str:
    index_url = urljoin(source.site_root + "/", source.index_path.lstrip("/"))
    html = fetch_text(index_url)
    match = BUNDLE_REGEX.search(html)
    if not match:
        raise RuntimeError(f"Could not find main-*.js bundle in {index_url}")
    return urljoin(source.site_root + "/", match.group(0))


def safe_rel_path(slug: str) -> str:
    slug = slug.strip().strip("/")
    if not slug:
        raise RuntimeError("Empty slug")
    parts = slug.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise RuntimeError(f"Unsafe slug: {slug}")
    return "/".join(parts) + ".md"


def extract_doc_pages(bundle_js: str, source: Source) -> List[DocPage]:
    pages: Dict[str, DocPage] = {}
    for match in PAGE_ENTRY_REGEX.finditer(bundle_js):
        section = match.group("section")
        path = match.group("path").strip("/")
        slug = match.group("slug")
        filename = match.group("filename")
        if not path or not slug or not filename:
            continue

        url = f"{source.site_root}{source.docs_asset_prefix}/{path}/{filename}.md"
        rel_path = safe_rel_path(slug)

        # Same slug may appear under multiple sections (e.g. shared "mcp" page);
        # keep the first occurrence for a stable, deduplicated set.
        if slug not in pages:
            pages[slug] = DocPage(section=section, slug=slug, url=url, rel_path=rel_path)

    return [pages[slug] for slug in sorted(pages.keys())]


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
        bundle_url = discover_bundle_url(source)
        print(f"[INFO] Source={source.source_id} bundle={bundle_url}")
        bundle_js = fetch_text(bundle_url)

        pages = extract_doc_pages(bundle_js, source)
        if not pages:
            raise RuntimeError(f"No doc pages discovered in bundle {bundle_url}")

        print(f"[INFO] Source={source.source_id} discovered={len(pages)}")
        total_pages += len(pages)

        source_root = DOCS_ROOT / source.output_subdir
        source_root.mkdir(parents=True, exist_ok=True)

        for page in pages:
            manifest_key = f"{source.output_subdir}/{page.rel_path}"
            try:
                dest = source_root / page.rel_path
                dest.parent.mkdir(parents=True, exist_ok=True)

                content = fetch_text(page.url)
                digest = sha256_text(content)

                existing = existing_files.get(manifest_key, {})
                if existing.get("sha256") != digest or not dest.exists():
                    dest.write_text(content, encoding="utf-8")

                new_files[manifest_key] = {
                    "source": source.source_id,
                    "section": page.section,
                    "slug": page.slug,
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
                "index_path": s.index_path,
                "docs_asset_prefix": s.docs_asset_prefix,
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
