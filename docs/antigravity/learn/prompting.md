# Prompting and instructions

Good prompting is clear technical writing. State the goal, constraints, and definition of done up front. The model then spends its reasoning budget solving the real problem instead of guessing what you meant.

For model-level guidance beyond coding agents, see [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) and [Introduction to prompt design in Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

* * *

## Four parts of an effective prompt

You do not need a rigid template for every message. Strong task prompts usually answer four questions:

| Element | What it tells the agent | Example |
| --- | --- | --- |
| **Goal** | The exact outcome you want. | Add rate limiting to the `/api/export` endpoint. |
| **Scope and inputs** | Which files, modules, or logs matter. | Edit `src/routes/export.ts` and reuse the helper in `src/lib/limiter.ts`. |
| **Constraints** | Boundaries, libraries to avoid, or style rules. | Do not add new npm dependencies. Keep responses JSON-formatted. |
| **Verification** | How to prove the work is done. | Add unit tests for burst and window reset behavior, then run `npm test`. |

### Vague prompt vs. concrete specification

Vague prompts force the agent to guess architecture, file paths, and edge cases:

```text
Fix the search page so it works better on mobile.
```

A concrete specification narrows the blast radius and adds a check the agent can run itself:

```text
Fix horizontal overflow on the search results table below 480px in src/styles/search.scss without changing desktop column widths, then verify at 390px viewport width with /browser.
```

Try a self-contained prompt that works in any repository:

```prompt
Inspect this repository's build scripts, test runner, and code style config, then draft a concise AGENTS.md with our real commands and conventions without editing any other files.
```

* * *

## Layer your instructions

Repeating project conventions in every prompt wastes time and context. Place each instruction at the right layer so Antigravity loads it automatically:

*   **Workspace rules (`AGENTS.md`, `GEMINI.md`, or `.agents/rules/*.md`)**: Team conventions, test commands, banned dependencies, and architecture notes. Antigravity loads these from your workspace folder and parent folders up to the repository root. See [Rules](/docs/rules).
*   **Global rules (`~/.gemini/AGENTS.md`, `~/.gemini/GEMINI.md`, `~/.gemini/config/AGENTS.md`, `~/.gemini/config/GEMINI.md`, or `~/.gemini/config/rules/*.md`)**: Personal preferences that follow you across every project.
*   **Rule activation modes**: Standalone `AGENTS.md` and `GEMINI.md` files stay always on. Modular files in `rules/*.md` use YAML frontmatter with a `trigger` key. Choose `always_on` (every turn), `glob` (matching file patterns), `model_decision` (loaded from its `description`), or `manual` (`@`\-mentioned in the Antigravity App).
*   **Reusable skills (`SKILL.md`)**: Step-by-step procedures that load on demand when a task matches, or run explicitly via `/<skill-name>`. See [Skills](/docs/skills).
*   **Capture session fixes with [`/learn`](/docs/commands/learn)**: After correcting the agent or solving a tricky setup, run `/learn`. Antigravity drafts a reviewable proposal to save the lesson as a rule or skill.
*   **Turn prompt**: The specific goal, target files, and acceptance criteria for the task in front of you.

Start complex tasks with a plan

When requirements have open trade-offs, run [`/grill-me`](/docs/commands/grill-me) to resolve design questions one by one. Run [`/plan`](/docs/plan) to review a written plan before edits begin. You can also stack `/plan /grill-me <task>` in one prompt to interview first and then draft the plan.

* * *

## Write constraints and feedback loops

Four habits catch ambiguity before the agent writes the wrong diff:

*   **State negative constraints explicitly.** Tell the agent what to leave untouched, such as keeping database migrations unchanged or preserving public function signatures.
*   **Show one concrete example for custom formats.** Include a short JSON schema, log line, or layout snippet instead of describing the format in prose.
*   **End prompts with a runnable check.** Include `npm test`, `pytest`, or `/browser` so the agent catches and fixes its own mistakes before reporting back.
*   **Course-correct early.** Stop a drifting turn rather than waiting for it to finish. In the Antigravity CLI, press Esc and run `/rewind`. In the Antigravity App, click **Stop** and click **Revert** on an earlier prompt.

### Prompt failure modes

| Symptom | Likely gap | Fix |
| --- | --- | --- |
| Agent edits unrelated files | Missing scope or negative constraints | Name exact target files and list what to leave untouched. |
| Agent guesses library APIs or flags | Missing primary-source grounding | Point to workspace manifests (`package.json`, `pyproject.toml`) or docs via MCP. |
| Agent reports done while broken | Missing verification step | End the prompt with a runnable test command or `/browser` check. |
| You repeat the same correction | Standing convention stuck in chat | Move it to `AGENTS.md` or run [`/learn`](/docs/commands/learn) to save it. |

* * *

## Next steps

[

Next in Learn

Context windows and tokens

See how prompt size, file mentions, and long sessions affect accuracy and speed.

](/docs/learn/context-and-tokens/)[

Antigravity

Rules

Store persistent workspace and global instructions in AGENTS.md and rule files.

](/docs/rules/)[

Build guide

Build a playable 3D browser world

See how a well-scoped single prompt coordinates four parallel agents.

](/docs/learn/build-3d-browser-world/)