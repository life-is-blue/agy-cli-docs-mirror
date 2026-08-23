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

`antigravity.google` is an Astro Starlight site that publishes docs as Markdown endpoints:

- Official site HTML sidebar exposes the full hierarchical multi-level navigation tree (e.g. `Antigravity CLI` -> `Agent Capabilities` -> `Headless Mode`).
- Doc pages are additionally listed in `/llms.txt` under `## Documentation`.
- Raw Markdown lives at `/docs/<slug>.md` (`Content-Type: text/markdown`).

`scripts/fetch_agy_docs.py` therefore:

1. parses the official Astro Starlight sidebar navigation DOM tree and merges with `/llms.txt`,
2. downloads each `/docs/<slug>.md` (gzip responses are decompressed when present),
3. mirrors them under `docs/<output_subdir>/<slug>.md`,
4. generates `docs/starlight_sidebar.json` (Astro Starlight compatible sidebar configuration),
5. generates `docs/SUMMARY.md` (GitBook / standard nested Markdown index),
6. writes `docs/docs_manifest.json` with full `category_path` and `sidebar_label` metadata.

## Using with Astro Starlight

You can directly consume the auto-generated `starlight_sidebar.json` in your Starlight config (`astro.config.mjs`):

```js
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import agySidebar from './docs/starlight_sidebar.json';

export default defineConfig({
  integrations: [
    starlight({
      title: 'Antigravity Docs Mirror',
      sidebar: agySidebar,
    }),
  ],
});
```

## Sources

Configured in `config/sources.json`:
- `https://antigravity.google` (`llms_path=/llms.txt`, markdown under `/docs/*.md`)

## Layout

- `scripts/fetch_agy_docs.py`: fetcher + Starlight sidebar parser + manifest generator
- `config/sources.json`: source definitions
- `docs/`: mirrored markdown content
- `docs/starlight_sidebar.json`: Starlight sidebar configuration tree
- `docs/SUMMARY.md`: nested markdown index
- `docs/docs_manifest.json`: manifest with hashes and category paths
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
