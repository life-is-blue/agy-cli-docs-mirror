#!/usr/bin/env python3
"""Fetch Agy CLI markdown docs listed in llms.txt indexes."""

from __future__ import annotations

import hashlib
import json
import os
import re
import ssl
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

import certifi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "sources.json"
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "docs_manifest.json"

USER_AGENT = "agy-cli-docs-mirror/1.0"

# Capture markdown links and bare URLs from llms.txt.
MARKDOWN_LINK_REGEX = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
BARE_URL_REGEX = re.compile(r"(?<!\()https?://[^\s<>()\"'`]+")

REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRIES = 4
BASE_BACKOFF_SECONDS = 1.5
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


@dataclass(frozen=True)
class Source:
    source_id: str
    llms_txt: str
    allowed_host: str
    docs_path_prefix: str
    root_docs_path: str
    output_subdir: str


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
        llms_txt = raw.get("llms_txt")
        allowed_host = raw.get("allowed_host")
        docs_path_prefix = raw.get("docs_path_prefix")
        root_docs_path = raw.get("root_docs_path")
        output_subdir = raw.get("output_subdir")

        if (
            not source_id
            or not llms_txt
            or not allowed_host
            or not docs_path_prefix
            or not root_docs_path
            or not output_subdir
        ):
            raise RuntimeError(f"Invalid source entry: {raw}")

        if not docs_path_prefix.startswith("/") or not docs_path_prefix.endswith("/"):
            raise RuntimeError(f"docs_path_prefix must look like '/docs/': {docs_path_prefix}")

        if not root_docs_path.startswith("/"):
            raise RuntimeError(f"root_docs_path must start with '/': {root_docs_path}")

        result.append(
            Source(
                source_id=source_id,
                llms_txt=llms_txt,
                allowed_host=allowed_host,
                docs_path_prefix=docs_path_prefix,
                root_docs_path=root_docs_path,
                output_subdir=output_subdir,
            )
        )
    return result


def fetch_text(url: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/markdown,text/plain,*/*"})
        try:
            with urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS, context=SSL_CONTEXT) as response:
                raw = response.read()
            return raw.decode("utf-8")
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt == MAX_RETRIES:
                break
            sleep_seconds = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            time.sleep(sleep_seconds)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def canonicalize_candidate_url(raw_url: str, source: Source) -> str | None:
    # Trim common punctuation around copied markdown links.
    candidate = raw_url.strip().lstrip("(<").rstrip(".,;:!?)]}>\"'`")

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"}:
        return None

    if parsed.netloc != source.allowed_host:
        return None

    path = parsed.path
    if not (path == source.root_docs_path or path.startswith(source.docs_path_prefix)):
        return None

    if not path.endswith(".md"):
        return None

    # Normalize to https and strip query/fragment for stable manifest keys.
    normalized = parsed._replace(scheme="https", query="", fragment="")
    return normalized.geturl()


def parse_markdown_urls(llms_text: str, source: Source) -> List[str]:
    candidates = set(MARKDOWN_LINK_REGEX.findall(llms_text))
    candidates.update(BARE_URL_REGEX.findall(llms_text))

    urls: Set[str] = set()
    for raw in candidates:
        normalized = canonicalize_candidate_url(raw, source)
        if normalized:
            urls.add(normalized)

    return sorted(urls)


def normalized_relative_path(url: str, source: Source) -> Path:
    parsed_url = urlparse(url)

    if parsed_url.netloc != source.allowed_host:
        raise RuntimeError(f"Disallowed host for url={url}")

    if parsed_url.path == source.root_docs_path:
        return Path("index.md")

    if not parsed_url.path.startswith(source.docs_path_prefix):
        raise RuntimeError(
            f"URL path does not match allowed docs prefix: url={url} prefix={source.docs_path_prefix}"
        )

    relative = unquote(parsed_url.path[len(source.docs_path_prefix) :]).lstrip("/")
    if not relative:
        relative = "index.md"

    rel_path = Path(relative)
    if any(part in {"", ".", ".."} for part in rel_path.parts):
        raise RuntimeError(f"Unsafe relative path derived from {url}: {relative}")

    if rel_path.suffix != ".md":
        raise RuntimeError(f"Expected .md path, got {relative}")

    return rel_path


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
    total_urls = 0
    successful_urls = 0
    failed_urls: List[Tuple[str, str]] = []

    for source in sources:
        print(f"[INFO] Source={source.source_id} index={source.llms_txt}")
        llms_text = fetch_text(source.llms_txt)
        urls = parse_markdown_urls(llms_text, source)
        if not urls:
            raise RuntimeError(f"No markdown URLs discovered from {source.llms_txt}")

        print(f"[INFO] Source={source.source_id} discovered={len(urls)}")
        total_urls += len(urls)

        source_root = DOCS_ROOT / source.output_subdir
        source_root.mkdir(parents=True, exist_ok=True)

        for url in urls:
            try:
                rel = normalized_relative_path(url, source)
                dest = source_root / rel
                dest.parent.mkdir(parents=True, exist_ok=True)

                content = fetch_text(url)
                digest = sha256_text(content)

                manifest_key = f"{source.output_subdir}/{rel.as_posix()}"
                existing = existing_files.get(manifest_key, {})
                existing_digest = existing.get("sha256")
                if existing_digest != digest or not dest.exists():
                    dest.write_text(content, encoding="utf-8")

                new_files[manifest_key] = {
                    "source": source.source_id,
                    "url": url,
                    "sha256": digest,
                    "bytes": len(content.encode("utf-8")),
                    "fetched_at": fetch_started_at,
                }
                successful_urls += 1
                print(f"[OK] {manifest_key}")
            except Exception as exc:  # noqa: BLE001
                print(f"[WARN] failed url={url} err={exc}")
                failed_urls.append((url, str(exc)))

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
                "llms_txt": s.llms_txt,
                "allowed_host": s.allowed_host,
                "docs_path_prefix": s.docs_path_prefix,
                "root_docs_path": s.root_docs_path,
                "output_subdir": s.output_subdir,
            }
            for s in sources
        ],
        "stats": {
            "total_urls": total_urls,
            "successful_urls": successful_urls,
            "failed_urls": len(failed_urls),
            "removed_files": len(removed_paths),
        },
        "failed": [{"url": url, "error": err} for url, err in failed_urls],
        "files": {k: new_files[k] for k in sorted(new_files.keys())},
    }

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print("\n[SUMMARY]")
    print(f"total_urls={total_urls}")
    print(f"successful_urls={successful_urls}")
    print(f"failed_urls={len(failed_urls)}")
    print(f"removed_files={len(removed_paths)}")

    if failed_urls and strict_fetch:
        print("[ERROR] STRICT_FETCH=1 and failures detected")
        return 1

    if successful_urls == 0:
        print("[ERROR] No documents fetched successfully")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
