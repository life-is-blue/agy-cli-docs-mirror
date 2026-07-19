# Agy CLI Docs Mirror

Local mirror for official **Google Antigravity** ("agy") docs, including the Antigravity CLI.

## Open-Source Positioning

This repository is an open mirror of publicly available Antigravity documentation,
designed to make agent-oriented document ingestion and retrieval easier.

- Canonical source remains the official Antigravity docs site (`https://antigravity.google/docs`).
- This mirror does not redefine or replace official documentation.
- We only mirror documentation the site itself publishes as Markdown.
- Each mirrored file keeps source metadata (`section`, `slug`, `url`, `sha256`, `fetched_at`) in `docs/docs_manifest.json`.

## How discovery works

`antigravity.google` is a single-page app, so it works differently from a plain `llms.txt`
mirror:

- `/docs/<slug>` routes all return the same JavaScript shell (content is rendered client-side),
  so there is no server-rendered HTML or `<slug>.md` endpoint to scrape.
- The real Markdown lives at `/assets/docs/<path>/<filename>.md` (with YAML frontmatter).
- The `slug -> (path, filename)` mapping only exists inside the hashed `main-*.js` bundle.

`scripts/fetch_agy_docs.py` therefore:

1. loads the index HTML and discovers the current `main-*.js` bundle (auto-adapts to redeploys),
2. extracts the doc page table (`{section, path, slug, filename}`) from the bundle,
3. downloads each `/assets/docs/<path>/<filename>.md` (responses are gzip-encoded and decompressed),
4. mirrors them under `docs/<output_subdir>/<slug>.md` and writes `docs/docs_manifest.json`.

## Sources

Configured in `config/sources.json`:
- `https://antigravity.google` (docs assets under `/assets/docs`)

## Layout

- `scripts/fetch_agy_docs.py`: fetcher + manifest generator
- `config/sources.json`: source definitions
- `docs/`: mirrored markdown content and manifest
- `.cnb.yml`: CNB scheduled + manual sync workflow
- `.cnb/web_trigger.yml`: CNB page button configuration

## Run locally

```bash
pip install -r scripts/requirements.txt
python3 scripts/fetch_agy_docs.py
```

Optional strict mode:

```bash
STRICT_FETCH=1 python3 scripts/fetch_agy_docs.py
```

## Automation

This repository supports both CNB and GitHub Actions automation:

- CNB scheduled sync daily: `main -> "crontab: 0 0 * * *"`
- CNB manual sync button on `main` branch page: **Sync Agy CLI Docs**
- GitHub Actions scheduled sync daily: `.github/workflows/update-docs.yml`
- Push / PR validation on `main` for fetcher changes (`scripts/**`, `config/**`, `.cnb.yml`, `.cnb/web_trigger.yml`)

## Notes

- Source content remains property of Google.
- This repository stores mirrored copies to support machine-readable indexing and agent retrieval workflows.
- Official docs should always be treated as the source of truth when discrepancies appear.

## Roadmap

1. Keep a stable daily sync baseline.
2. Preserve manual sync triggers for urgent refreshes.
3. Add retrieval-focused artifacts (diff summaries / normalized indexes) to improve agent read quality.
4. Keep CNB and GitHub Actions workflows aligned with the same daily sync policy.
