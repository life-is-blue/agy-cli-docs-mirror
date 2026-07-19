# Agy CLI Docs Mirror

Local mirror for official Agy CLI Markdown docs.

> ⚠️ **待确认**：`config/sources.json` 中的来源站点（`llms_txt` / `allowed_host`）目前为占位值
> `https://agycli.com/llms.txt`。请替换为 Agy CLI 官方文档站真实的 `llms.txt` 地址后再运行同步。

## Open-Source Positioning

This repository is an open mirror of publicly available Agy CLI documentation,
designed to make agent-oriented document ingestion and retrieval easier.

- Canonical source remains the official Agy CLI docs site.
- This mirror does not redefine or replace official documentation.
- We only mirror documentation discovered from official `llms.txt` indexes.
- Each mirrored file keeps source metadata (`url`, `sha256`, `fetched_at`) in `docs/docs_manifest.json`.

This repository is designed for automation-first ingestion:
- Periodically fetches `llms.txt` indexes from Agy CLI docs
- Resolves linked docs Markdown pages
- Stores mirrored files under `docs/`
- Writes `docs/docs_manifest.json` with hashes and source metadata

## Sources

Configured in `config/sources.json`:
- `https://agycli.com/llms.txt` (占位，待替换为官方地址)

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

- Source content remains property of its respective owner.
- This repository stores mirrored copies to support machine-readable indexing and agent retrieval workflows.
- Official docs should always be treated as the source of truth when discrepancies appear.

## Roadmap

1. Keep a stable daily sync baseline.
2. Preserve manual sync triggers for urgent refreshes.
3. Add retrieval-focused artifacts (diff summaries / normalized indexes) to improve agent read quality.
4. Keep CNB and GitHub Actions workflows aligned with the same daily sync policy.
