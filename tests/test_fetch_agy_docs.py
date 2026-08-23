#!/usr/bin/env python3
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from fetch_agy_docs import (
    Source,
    DocPage,
    docs_slug_from_url,
    safe_rel_path,
    parse_starlight_sidebar_dom,
    parse_llms_doc_pages,
    build_fallback_sidebar_from_llms,
    merge_supplemental_pages_into_sidebar_tree,
    generate_summary_md,
    extract_sidebar_leaf_slugs,
    extract_summary_links,
    sha256_text,
    sync_docs,
)
from bs4 import BeautifulSoup


class TestFetchAgyDocsPure(unittest.TestCase):
    def setUp(self):
        self.source = Source(
            source_id="antigravity",
            site_root="https://antigravity.google",
            llms_path="/llms.txt",
            docs_path_prefix="/docs/",
            output_subdir="antigravity",
        )

    def test_docs_slug_from_url(self):
        self.assertEqual(docs_slug_from_url("/docs/cli/headless/", self.source), "cli/headless")
        self.assertEqual(docs_slug_from_url("/docs/cli/headless.md", self.source), "cli/headless")
        self.assertEqual(docs_slug_from_url("https://antigravity.google/docs/cli/headless", self.source), "cli/headless")
        self.assertEqual(docs_slug_from_url("/docs/cli/headless?foo=bar#section", self.source), "cli/headless")
        self.assertEqual(docs_slug_from_url("https://antigravity.google/docs/cli/headless.md?v=2#top", self.source), "cli/headless")
        self.assertEqual(docs_slug_from_url("/docs/home/", self.source), "home")
        self.assertEqual(docs_slug_from_url("/docs/", self.source), "home")
        self.assertEqual(docs_slug_from_url("/docs", self.source), "home")
        self.assertIsNone(docs_slug_from_url("/download/linux", self.source))
        self.assertIsNone(docs_slug_from_url("https://github.com/google", self.source))
        self.assertIsNone(docs_slug_from_url("/docs/../etc/passwd", self.source))

    def test_safe_rel_path(self):
        self.assertEqual(safe_rel_path("cli/headless"), "cli/headless.md")
        self.assertEqual(safe_rel_path("home"), "home.md")
        with self.assertRaises(RuntimeError):
            safe_rel_path("../secret")

    def test_sidebar_dom_parsing(self):
        html = """
        <nav aria-label="Main" class="sidebar">
          <ul class="top-level">
            <li><a href="/docs/home/"><span>Home</span></a></li>
            <li>
              <details>
                <summary>
                  <span class="group-label">
                    <span>Antigravity CLI</span>
                    <span class="sl-badge note small">v1.0.0</span>
                  </span>
                </summary>
                <ul>
                  <li><a href="/docs/cli/overview/"><span>Overview</span></a></li>
                  <li>
                    <details>
                      <summary><span class="group-label"><span>Agent Capabilities</span></span></summary>
                      <ul>
                        <li><a href="/docs/cli/headless/"><span>Headless Mode</span></a></li>
                      </ul>
                    </details>
                  </li>
                </ul>
              </details>
            </li>
          </ul>
        </nav>
        """
        soup = BeautifulSoup(html, "html.parser")
        top_ul = soup.find("ul", class_="top-level")
        sidebar_tree, doc_pages = parse_starlight_sidebar_dom(top_ul, self.source)

        self.assertEqual(len(sidebar_tree), 2)
        self.assertEqual(sidebar_tree[0]["label"], "Home")
        self.assertEqual(sidebar_tree[0]["slug"], "antigravity/home")

        cli_group = sidebar_tree[1]
        self.assertEqual(cli_group["label"], "Antigravity CLI")
        self.assertEqual(cli_group["badge"], {"text": "v1.0.0", "variant": "note"})
        self.assertTrue(cli_group["collapsed"])

        nested_group = cli_group["items"][1]
        self.assertEqual(nested_group["label"], "Agent Capabilities")
        self.assertEqual(nested_group["items"][0]["label"], "Headless Mode")
        self.assertEqual(nested_group["items"][0]["slug"], "antigravity/cli/headless")

        self.assertIn("cli/headless", doc_pages)
        headless_page = doc_pages["cli/headless"]
        self.assertEqual(headless_page.category_path, ("Antigravity CLI", "Agent Capabilities"))
        self.assertEqual(headless_page.section, "Antigravity CLI")

    def test_supplemental_merge_and_fallback(self):
        llms_text = """
## Documentation

### Antigravity CLI
- [cli-overview](https://antigravity.google/docs/cli/overview): Learn overview
- [cli-headless](https://antigravity.google/docs/cli/headless): Learn headless
        """
        llms_pages = parse_llms_doc_pages(llms_text, self.source)
        self.assertEqual(len(llms_pages), 2)

        fallback_tree = build_fallback_sidebar_from_llms(llms_pages, self.source)
        self.assertEqual(len(fallback_tree), 1)
        self.assertEqual(fallback_tree[0]["label"], "Antigravity CLI")
        self.assertEqual(len(fallback_tree[0]["items"]), 2)

        extra_page = DocPage(
            section="Antigravity CLI",
            slug="cli/extra",
            url="https://antigravity.google/docs/cli/extra.md",
            rel_path="cli/extra.md",
            label="Extra CLI Tool",
            category_path=("Antigravity CLI",),
        )
        merged_tree = merge_supplemental_pages_into_sidebar_tree(fallback_tree, [extra_page], self.source)
        self.assertEqual(len(merged_tree[0]["items"]), 3)
        self.assertEqual(merged_tree[0]["items"][2]["slug"], "antigravity/cli/extra")

    def test_invariants_and_summary_generation(self):
        tree = [
            {"label": "Home", "slug": "antigravity/home"},
            {
                "label": "Antigravity CLI",
                "badge": {"text": "v1.0.0", "variant": "note"},
                "collapsed": True,
                "items": [
                    {"label": "Overview", "slug": "antigravity/cli/overview"},
                    {
                        "label": "Agent Capabilities",
                        "collapsed": True,
                        "items": [
                            {"label": "Headless Mode", "slug": "antigravity/cli/headless"}
                        ],
                    },
                ],
            },
        ]
        summary_md = generate_summary_md(tree)
        self.assertIn("- [Home](antigravity/home.md)", summary_md)
        self.assertIn("- Antigravity CLI `v1.0.0`", summary_md)
        self.assertIn("- [Headless Mode](antigravity/cli/headless.md)", summary_md)

        sidebar_slugs = extract_sidebar_leaf_slugs(tree)
        summary_slugs = extract_summary_links(summary_md)
        self.assertEqual(sidebar_slugs, summary_slugs)
        self.assertEqual(sidebar_slugs, ["antigravity/cli/headless", "antigravity/cli/overview", "antigravity/home"])


class TestSyncIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.tmp_path = Path(self.tmp.name)
        self.docs_dir = self.tmp_path / "docs"
        self.docs_dir.mkdir(parents=True)
        self.config_file = self.tmp_path / "sources.json"
        self.config_data = {
            "sources": [
                {
                    "id": "antigravity",
                    "site_root": "https://antigravity.test",
                    "llms_path": "/llms.txt",
                    "docs_path_prefix": "/docs/",
                    "output_subdir": "antigravity",
                }
            ]
        }
        self.config_file.write_text(json.dumps(self.config_data), encoding="utf-8")
        self.manifest_file = self.docs_dir / "docs_manifest.json"
        self.sidebar_file = self.docs_dir / "starlight_sidebar.json"
        self.summary_file = self.docs_dir / "SUMMARY.md"

    def tearDown(self):
        self.tmp.cleanup()

    def test_degraded_discovery_blocks_deletions(self):
        """Test that if HTML sidebar parsing fails and we fallback to llms.txt, existing files are NEVER deleted."""
        source_dir = self.docs_dir / "antigravity"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "doc1.md").write_text("# Doc 1", encoding="utf-8")
        (source_dir / "doc2.md").write_text("# Doc 2", encoding="utf-8")
        (source_dir / "doc3.md").write_text("# Doc 3 (HTML only)", encoding="utf-8")

        initial_manifest = {
            "files": {
                "antigravity/doc1.md": {"sha256": sha256_text("# Doc 1"), "fetched_at": "2026-08-01T00:00:00Z"},
                "antigravity/doc2.md": {"sha256": sha256_text("# Doc 2"), "fetched_at": "2026-08-01T00:00:00Z"},
                "antigravity/doc3.md": {"sha256": sha256_text("# Doc 3 (HTML only)"), "fetched_at": "2026-08-01T00:00:00Z"},
            }
        }
        self.manifest_file.write_text(json.dumps(initial_manifest), encoding="utf-8")

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                raise RuntimeError("HTML 500 Internal Server Error")
            if "llms.txt" in url:
                return (
                    "## Documentation\n### General\n- [doc1](https://antigravity.test/docs/doc1): d1\n- [doc2](https://antigravity.test/docs/doc2): d2\n",
                    "text/plain",
                )
            if "doc1.md" in url:
                return "# Doc 1", "text/markdown"
            if "doc2.md" in url:
                return "# Doc 2", "text/markdown"
            raise RuntimeError(f"Unexpected url {url}")

        code, manifest = sync_docs(
            config_path=self.config_file,
            docs_root=self.docs_dir,
            manifest_path=self.manifest_file,
            sidebar_path=self.sidebar_file,
            summary_path=self.summary_file,
            strict_fetch=False,
            fetch_text_fn=mock_fetch,
        )

        self.assertEqual(code, 0)
        self.assertTrue(manifest["is_degraded"])
        self.assertEqual(manifest["stats"]["removed_files"], 0)
        self.assertTrue((source_dir / "doc3.md").exists())

    def test_invariant_violation_aborts_commit_in_all_modes(self):
        """Test that if a newly discovered page fails downloading, invariant failure blocks committing corrupt files."""
        html = """
        <nav aria-label="Main">
          <ul class="top-level">
            <li><a href="/docs/doc1/"><span>Doc 1</span></a></li>
            <li><a href="/docs/doc2/"><span>Doc 2</span></a></li>
          </ul>
        </nav>
        """

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                return html, "text/html"
            if "llms.txt" in url:
                return "", "text/plain"
            if "doc1.md" in url:
                return "# Doc 1 Content", "text/markdown"
            if "doc2.md" in url:
                raise RuntimeError("504 Gateway Timeout on new doc2")
            raise RuntimeError(f"Unexpected {url}")

        code, res = sync_docs(
            config_path=self.config_file,
            docs_root=self.docs_dir,
            manifest_path=self.manifest_file,
            sidebar_path=self.sidebar_file,
            summary_path=self.summary_file,
            strict_fetch=False,  # Even in non-strict mode!
            fetch_text_fn=mock_fetch,
        )

        self.assertEqual(code, 1)  # Must return 1
        self.assertEqual(res["error"], "invariant_violation")
        # Ensure production files were NOT created/corrupted
        self.assertFalse(self.sidebar_file.exists())
        self.assertFalse(self.summary_file.exists())

    def test_existing_doc_fetch_failure_preserves_local_copy(self):
        """Test that if an existing doc fails re-download in a multi-doc run, local copy and manifest entry are preserved."""
        source_dir = self.docs_dir / "antigravity"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "doc1.md").write_text("# Existing Doc 1", encoding="utf-8")
        (source_dir / "doc2.md").write_text("# Existing Doc 2", encoding="utf-8")

        initial_manifest = {
            "files": {
                "antigravity/doc1.md": {
                    "source": "antigravity",
                    "section": "Documentation",
                    "category_path": [],
                    "slug": "doc1",
                    "label": "Doc 1",
                    "url": "https://antigravity.test/docs/doc1.md",
                    "sha256": sha256_text("# Existing Doc 1"),
                    "bytes": len("# Existing Doc 1"),
                    "fetched_at": "2026-08-01T00:00:00Z",
                },
                "antigravity/doc2.md": {
                    "source": "antigravity",
                    "section": "Documentation",
                    "category_path": [],
                    "slug": "doc2",
                    "label": "Doc 2",
                    "url": "https://antigravity.test/docs/doc2.md",
                    "sha256": sha256_text("# Existing Doc 2"),
                    "bytes": len("# Existing Doc 2"),
                    "fetched_at": "2026-08-01T00:00:00Z",
                },
            }
        }
        self.manifest_file.write_text(json.dumps(initial_manifest), encoding="utf-8")

        html = """
        <nav aria-label="Main">
          <ul class="top-level">
            <li><a href="/docs/doc1/"><span>Doc 1</span></a></li>
            <li><a href="/docs/doc2/"><span>Doc 2</span></a></li>
          </ul>
        </nav>
        """

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                return html, "text/html"
            if "llms.txt" in url:
                return "", "text/plain"
            if "doc1.md" in url:
                return "# Updated Doc 1", "text/markdown"
            if "doc2.md" in url:
                raise RuntimeError("500 Network Timeout on doc2")
            raise RuntimeError(f"Unexpected url {url}")

        code, manifest = sync_docs(
            config_path=self.config_file,
            docs_root=self.docs_dir,
            manifest_path=self.manifest_file,
            sidebar_path=self.sidebar_file,
            summary_path=self.summary_file,
            strict_fetch=False,
            fetch_text_fn=mock_fetch,
        )

        self.assertEqual(code, 0)
        self.assertTrue((source_dir / "doc2.md").exists())
        self.assertEqual(manifest["files"]["antigravity/doc2.md"]["last_fetch_status"], "failed")
        self.assertEqual((source_dir / "doc1.md").read_text(encoding="utf-8"), "# Updated Doc 1")

    def test_idempotency_keeps_original_timestamp(self):
        """Test that identical content does not update fetched_at timestamp (zero git noise)."""
        source_dir = self.docs_dir / "antigravity"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "doc1.md").write_text("# Unchanged Content", encoding="utf-8")

        initial_manifest = {
            "files": {
                "antigravity/doc1.md": {
                    "source": "antigravity",
                    "section": "Documentation",
                    "category_path": [],
                    "slug": "doc1",
                    "label": "Doc 1",
                    "url": "https://antigravity.test/docs/doc1.md",
                    "sha256": sha256_text("# Unchanged Content"),
                    "bytes": len("# Unchanged Content"),
                    "fetched_at": "2026-08-01T00:00:00Z",
                }
            }
        }
        self.manifest_file.write_text(json.dumps(initial_manifest), encoding="utf-8")

        html = '<nav aria-label="Main"><ul class="top-level"><li><a href="/docs/doc1/"><span>Doc 1</span></a></li></ul></nav>'

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                return html, "text/html"
            if "llms.txt" in url:
                return "", "text/plain"
            if "doc1.md" in url:
                return "# Unchanged Content", "text/markdown"
            raise RuntimeError(f"Unexpected url {url}")

        code, manifest = sync_docs(
            config_path=self.config_file,
            docs_root=self.docs_dir,
            manifest_path=self.manifest_file,
            sidebar_path=self.sidebar_file,
            summary_path=self.summary_file,
            strict_fetch=False,
            fetch_text_fn=mock_fetch,
        )

        self.assertEqual(code, 0)
        self.assertEqual(manifest["files"]["antigravity/doc1.md"]["fetched_at"], "2026-08-01T00:00:00Z")

    def test_legitimate_deletion_in_authoritative_mode(self):
        """Test that only when authoritative HTML discovery succeeds, missing files are safely removed."""
        source_dir = self.docs_dir / "antigravity"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "doc1.md").write_text("# Doc 1", encoding="utf-8")
        (source_dir / "old_doc.md").write_text("# Old Obsolete Doc", encoding="utf-8")

        initial_manifest = {
            "files": {
                "antigravity/doc1.md": {"sha256": sha256_text("# Doc 1"), "fetched_at": "2026-08-01T00:00:00Z"},
                "antigravity/old_doc.md": {"sha256": sha256_text("# Old Obsolete Doc"), "fetched_at": "2026-08-01T00:00:00Z"},
            }
        }
        self.manifest_file.write_text(json.dumps(initial_manifest), encoding="utf-8")

        html = '<nav aria-label="Main"><ul class="top-level"><li><a href="/docs/doc1/"><span>Doc 1</span></a></li></ul></nav>'

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                return html, "text/html"
            if "llms.txt" in url:
                return "## Documentation\n### General\n- [doc1](https://antigravity.test/docs/doc1): d1\n", "text/plain"
            if "doc1.md" in url:
                return "# Doc 1", "text/markdown"
            raise RuntimeError(f"Unexpected url {url}")

    def test_partial_html_discovery_blocks_mass_deletion(self):
        """Test that if upstream returns truncated HTML (e.g. 1/10 pages), mass deletion is blocked and files are preserved."""
        source_dir = self.docs_dir / "antigravity"
        source_dir.mkdir(parents=True, exist_ok=True)
        initial_files = {}

        # Create 10 existing files on disk
        for i in range(1, 11):
            doc_name = f"doc{i}.md"
            (source_dir / doc_name).write_text(f"# Doc {i}", encoding="utf-8")
            initial_files[f"antigravity/{doc_name}"] = {
                "source": "antigravity",
                "section": "Documentation",
                "category_path": [],
                "slug": f"doc{i}",
                "label": f"Doc {i}",
                "url": f"https://antigravity.test/docs/doc{i}.md",
                "sha256": sha256_text(f"# Doc {i}"),
                "bytes": len(f"# Doc {i}"),
                "fetched_at": "2026-08-01T00:00:00Z",
            }

        initial_manifest = {"files": initial_files}
        self.manifest_file.write_text(json.dumps(initial_manifest), encoding="utf-8")

        # Mock HTML returning only 1 page (truncated upstream layout)
        truncated_html = '<nav aria-label="Main"><ul class="top-level"><li><a href="/docs/doc1/"><span>Doc 1</span></a></li></ul></nav>'

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                return truncated_html, "text/html"
            if "llms.txt" in url:
                return "", "text/plain"
            if "doc1.md" in url:
                return "# Doc 1", "text/markdown"
            raise RuntimeError(f"Unexpected url {url}")

        code, manifest = sync_docs(
            config_path=self.config_file,
            docs_root=self.docs_dir,
            manifest_path=self.manifest_file,
            sidebar_path=self.sidebar_file,
            summary_path=self.summary_file,
            strict_fetch=False,
            fetch_text_fn=mock_fetch,
        )

        self.assertEqual(code, 0)
        self.assertEqual(manifest["stats"]["removed_files"], 0)
        # Verify all other 9 files were preserved on disk!
        for i in range(2, 11):
            self.assertTrue((source_dir / f"doc{i}.md").exists())
            self.assertIn(f"antigravity/doc{i}.md", manifest["files"])

    def test_partial_html_discovery_fails_strict_fetch(self):
        """Test that in STRICT_FETCH=1, suspicious drop in discovered pages fails the build."""
        source_dir = self.docs_dir / "antigravity"
        source_dir.mkdir(parents=True, exist_ok=True)
        initial_files = {}

        for i in range(1, 11):
            doc_name = f"doc{i}.md"
            (source_dir / doc_name).write_text(f"# Doc {i}", encoding="utf-8")
            initial_files[f"antigravity/{doc_name}"] = {
                "source": "antigravity",
                "sha256": sha256_text(f"# Doc {i}"),
                "fetched_at": "2026-08-01T00:00:00Z",
            }

        self.manifest_file.write_text(json.dumps({"files": initial_files}), encoding="utf-8")
        truncated_html = '<nav aria-label="Main"><ul class="top-level"><li><a href="/docs/doc1/"><span>Doc 1</span></a></li></ul></nav>'

        def mock_fetch(url: str):
            if "overview" in url or "home" in url:
                return truncated_html, "text/html"
            if "llms.txt" in url:
                return "", "text/plain"
            if "doc1.md" in url:
                return "# Doc 1", "text/markdown"
            raise RuntimeError(f"Unexpected url {url}")

        code, res = sync_docs(
            config_path=self.config_file,
            docs_root=self.docs_dir,
            manifest_path=self.manifest_file,
            sidebar_path=self.sidebar_file,
            summary_path=self.summary_file,
            strict_fetch=True,
            fetch_text_fn=mock_fetch,
        )

        self.assertEqual(code, 1)
        self.assertEqual(res["error"], "deletion_integrity_failed")


if __name__ == "__main__":
    unittest.main()

