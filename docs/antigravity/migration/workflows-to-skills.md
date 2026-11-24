# Migrate from workflows to skills

Learn how to migrate your legacy Antigravity workflows to modern, standard [Agent skills](/docs/skills).

Changes to workflows

Workflows are deprecated, and a new workflows system is on the way. Your current workflows keep working for now. To move them to **[Agent skills](/docs/skills)**, run [`/migrate-workflows`](#using-migrate-workflows) in the Antigravity App 2.12.0 or later, or follow the [manual migration guide](#manual-migration-guide).

Tip

The new workflows system is [Dynamic Workflows](/docs/dynamic-workflows): the agent writes and runs a Python script that orchestrates many agents across parallel and sequential phases. To keep a legacy workflow’s step-by-step instructions, migrate it to a skill as described on this page.

## Why migrate to skills?

Workflows were originally introduced in the Antigravity IDE as single Markdown files designed for repeatable prompt sequences. While effective for simple instructions, monolithic files presented challenges as tasks grew in complexity.

In May 2026, Antigravity adopted the open industry standard for [Agent Skills](https://agentskills.io/home). Migrating to skills provides significant architectural and operational improvements:

Progressive context loading

Skills load only essential metadata (name and description) into the agent’s context upfront. Full instructions and reference materials are loaded on demand, preventing prompt bloat.

Multi-file directory bundling

Unlike single-file workflows, a skill is a directory bundle. You can co-locate executable helper scripts, documentation, sample schemas, and reference assets directly alongside `SKILL.md`.

Open ecosystem standard

Skills adhere to the cross-platform agent specification, enabling you to share and reuse skills across Antigravity IDE, Antigravity CLI, and other compliant agent tools.

Subagent integration

Skills can define specialized system prompts, specify tool requirements, and delegate subtasks to custom subagents directly from the skill bundle.

* * *

## Comparison: Workflows and skills

| Feature | Legacy Workflows (`.md`) | Agent Skills (`SKILL.md`) |
| --- | --- | --- |
| **Specification** | Proprietary Antigravity format | Open Agent Skills Standard ([agentskills.io](https://agentskills.io/home)) |
| **Structure** | Single standalone `.md` file | Directory bundle (`<skill-name>/SKILL.md` + assets) |
| **Workspace Path** | `.agents/workflows/<name>.md` | `.agents/skills/<name>/SKILL.md` |
| **Global Path** | `~/.gemini/config/global_workflows/<name>.md` | `~/.gemini/config/skills/<name>/SKILL.md` |
| **Context Loading** | Entire file loaded into prompt | **Progressive**: Metadata indexed upfront; body loaded on demand |
| **Bundled Assets** | Not supported (everything must fit in one prompt) | Supported (`scripts/`, `references/`, `examples/`) |
| **Slash Commands** | Supported (`/<workflow-name>`) | Supported (`/<skill-name>`) |
| **Autonomous Discovery** | Supported | Supported (enhanced semantic matching using description) |
| **File Size Limit** | 12,000 characters | Unrestricted bundle; modular multi-file architecture |

* * *

## Automatic migration

The Antigravity App provides an automated migration command that discovers your existing workflows and converts them to skill directory bundles.

### Using `/migrate-workflows`

The `/migrate-workflows` command is available only in the Antigravity App 2.12.0 and later, not in the Antigravity CLI or the Antigravity IDE. To migrate without the Antigravity App, follow the [manual migration guide](#manual-migration-guide).

Complete the following steps to automatically migrate your workflows:

1.  Open the Antigravity App 2.12.0 or later.
2.  Run the migration command:
    
    ```prompt
    /migrate-workflows
    ```
    
3.  The agent performs the following actions:
    *   Scans both global (`~/.gemini/config/global_workflows/` and `~/.gemini/config/workflows/`) and workspace-level (`.agents/workflows/`) directories.
    *   Parses each workflow’s YAML frontmatter and body.
    *   Scaffolds `~/.gemini/config/skills/<workflow-name>/SKILL.md` (for global workflows) or `.agents/skills/<workflow-name>/SKILL.md` (for workspace workflows) with compliant metadata.
    *   Archives original workflow files by appending `.bak` (for example, `deploy.md` becomes `deploy.md.bak`).
    *   Immediately activates the new skills for slash commands and autonomous agent usage.

* * *

## Manual migration guide

If you prefer to migrate your workflows manually or want to refactor monolithic prompts into modular skill packages, follow these steps:

1.  ### Create the skill directory
    
    In your workspace or global configuration directory, create a new folder named after your workflow under `skills/`:
    
    **Workspace Skill:**
    
    ```bash
    mkdir -p .agents/skills/deploy-staging
    ```
    
    **Global Skill:**
    
    ```bash
    mkdir -p ~/.gemini/config/skills/deploy-staging
    ```
    
2.  ### Create and populate `SKILL.md`
    
    Move your existing workflow Markdown file to `SKILL.md` inside the new folder:
    
    ```bash
    mv .agents/workflows/deploy-staging.md .agents/skills/deploy-staging/SKILL.md
    ```
    
3.  ### Standardize the YAML frontmatter
    
    Ensure your `SKILL.md` begins with the standard `name` and `description` frontmatter fields. The description should clearly explain **what** the skill does and **when** the agent should use it:
    
    ```yaml
    ---
    name: deploy-staging
    description: Deploys the current project build to the staging preview environment on App Engine. Use when testing staging releases or verifying PR previews.
    ---
    
    # Deploy Staging
    
    Follow these instructions to deploy the current build to staging...
    ```
    
4.  ### (Optional) Extract scripts and resources
    
    If your workflow contains embedded scripts, code snippets, or lengthy reference documentation, extract them into dedicated subdirectories to keep `SKILL.md` lean:
    
    ```text
    .agents/skills/deploy-staging/
    ├── SKILL.md
    ├── scripts/
    │   └── deploy.sh
    └── references/
        └── staging-endpoints.json
    ```
    
    In `SKILL.md`, instruct the agent to run or inspect those files when needed rather than duplicating them in the prompt.
    
5.  ### Verify the migrated skill
    
    Invoke the skill directly in the Antigravity App:
    
    ```prompt
    /deploy-staging
    ```
    
    The agent loads the skill metadata and executes the steps.
    

* * *

## Before and after migration example

### Before: Legacy monolithic workflow

```markdown
---
name: build-and-test
description: Run test suites and verify build
---

Run the following checks sequentially:
1. First run `npm run check` to verify TypeScript and template integrity.
2. Next execute `npm run test` for unit tests.
3. If tests pass, run `npm run build` and report the generated bundle size.
```

### After: Modular agent skill package

```text
.agents/skills/build-and-test/
├── SKILL.md
└── scripts/
    └── verify-bundle.js
```

```markdown
---
name: build-and-test
description: Runs full validation suite including TypeScript checks, unit tests, and production build verification. Use before submitting changes.
---

# Build and Test Suite

Execute the project verification pipeline:

1. **Type & Template Diagnostics**:
   ```bash
   npm run check
   ```

2. **Unit Tests**:
   ```bash
   npm run test
   ```

3. **Production Build & Bundle Size Analysis**:
   ```bash
   npm run build
   node scripts/verify-bundle.js
   ```
```

## Frequently asked questions

### Will my workflows stop working immediately?

No. Your current workflows keep working for now. A new workflows system is on the way, along with instructions for moving to it. In the meantime, you can keep using your workflows or migrate them to skills.

### Can I still invoke my migrated skills using slash commands?

Yes. You can invoke any skill located in `.agents/skills/<name>/` or `~/.gemini/config/skills/<name>/` by typing `/<name>` in chat, just like legacy workflows.

### What happens if I have both a workflow and a skill with the same name?

Skills take precedence over legacy workflows. If both `.agents/skills/deploy/` and `.agents/workflows/deploy.md` exist, Antigravity executes the skill.

### Where should I put global skills?

Place global skills in `~/.gemini/config/skills/<skill-name>/SKILL.md` to make them accessible across all your workspaces.

## Related documentation

Explore the following resources to learn more:

*   **[Agent skills overview](/docs/skills)**: Full guide on creating, configuring, and organizing skills.
*   **[Customizing agent rules](/docs/ide/rules)**: Learn how to define persistent workspace and global rules.
*   **[Antigravity CLI plugins and skills](/docs/cli/plugins)**: Manage skills in the Antigravity CLI.