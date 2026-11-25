# Verification and guardrails

AI models can write plausible code that breaks at runtime, misses an edge case, or calls an unrecognized API. Reliable agent workflows treat **verification as part of the prompt**, not an afterthought.

* * *

## Build a layered verification loop

Combine fast deterministic checks with real runtime checks so the agent catches bugs before you open the diff:

| Verification layer | What it catches | Example in Antigravity |
| --- | --- | --- |
| **Type checks and linters** | Syntax errors, bad imports, and mismatched types. | Ask the agent to run `tsc --noEmit`, `eslint`, or `go vet` after edits. |
| **Unit tests** | Logic regressions and broken math or data transformations. | Keep pure logic separate from UI code so `npm test` or `pytest` finishes in milliseconds. |
| **Live browser checks** | Blank renders, broken layouts, 404 assets, and console errors. | Use [Browser use](/docs/browser) or [`/browser`](/docs/commands/browser) to click through flows and inspect screenshots. |
| **Independent review** | Missed edge cases, weakened assertions, and unrequested edits. | Pair workers with `@verifier` in [`/swarm`](/docs/swarm) and inspect diffs in [Review changes](/docs/review-changes) or `/diff`. |

### Failure modes unit tests miss

| Failure mode | Why unit tests miss it | Antigravity guardrail |
| --- | --- | --- |
| **Unrecognized API or outdated flag** | Mocks hide real upstream signatures. | Ground prompts in package manifests or the [Google Developer Knowledge MCP server](/docs/mcp#example-search-google-developer-docs). |
| **Blank canvas, bad layout, or 404 assets** | Unit tests run without a live DOM or WebGL renderer. | Run [Browser use](/docs/browser) or [`/browser`](/docs/commands/browser) to verify console output and screenshots. |
| **Weakened or deleted assertions** | The suite still passes after loosening checks. | Review test diffs first in **Review** or `/diff`, or run a cross-model `@verifier` in [`/swarm`](/docs/swarm). |
| **Unsafe shell command or secret read** | Unit tests do not enforce host boundaries. | Combine the [Terminal sandbox](/docs/sandbox), `Deny` rules, and `PreToolUse` [Hooks](/docs/hooks). |

* * *

## Guardrails that protect your machine

Before giving an agent broad autonomy, set clear execution and review boundaries:

*   **Permissions (`Deny > Ask > Allow`)**: Control file access (`read_file`, `write_file`), shell commands (`command`), web URLs (`read_url`, `execute_url`, `download_url`), and MCP tools (`mcp`). Conflicting rules always evaluate in priority order: **Deny > Ask > Allow**. See [Permissions](/docs/permissions).
*   **Terminal sandbox**: Isolates shell commands at the OS level (Linux namespaces, macOS `sandbox-exec`, and Windows process security environments on Windows 11 24H2+). Outbound network access is **blocked by default** (only `read_url` domains are allowlisted), and sensitive files like `~/.ssh` and `.env` are blocked. See [Terminal sandbox](/docs/sandbox).
*   **Lifecycle hooks**: Deterministic shell scripts in `.agents/hooks.json` or `~/.gemini/config/hooks.json` (`PreToolUse`, `PostToolUse`). Unlike prompt instructions, hooks run every time and can block unsafe commands or run linters automatically. See [Hooks](/docs/hooks).
*   **Plan approval ([Artifact review](/docs/artifact-review))**: Controls **Plan Review Policy** (**Always Ask** vs. **Always Proceed**) for implementation plans. Invoking [`/plan`](/docs/plan) always pauses for your approval before code edits begin.
*   **Diff review ([Review changes](/docs/review-changes))**: Inspect Git diffs file by file, leave inline line comments for the agent, stage or discard files, and commit when satisfied.

### Guardrails by surface

### Antigravity App

*   **Permission presets**: Choose **Request Review**, **Default**, **Auto**, or **Turbo**. **Default** runs commands in the sandbox and asks outside. **Auto** checks safe host commands automatically (`v2.23.0+` macOS/Linux, `v2.26.0+` Windows, personal accounts). Switch presets in **Settings**, per project, or from the message box.
*   **Built-in browser guardrails**: On personal Google Accounts (`v2.30.0+`), the built-in browser isolates `localhost` by port and masks sign-in or payment frames. File uploads (and `data:`/`blob:` downloads) require one-time approval, while standard file downloads (`v2.31.0+`) prompt per domain unless allowed by **Browser Actuation Rules** or **Turbo**. Business and enterprise accounts use `/browser` with local Chrome (`v144+`).
*   **Review pane**: Open **Review** from **Overview** (Cmd + Option + O or Ctrl + Alt + O). Inspect **Uncommitted**, **Branch**, or **Agent Edits** diffs and send inline comments.

### Antigravity CLI

*   **Execution modes**: Press Shift + Tab to cycle between `default`, `accept-edits`, `auto`, and `plan`. `auto` is the default since `v1.5.7` where available and enables the sandbox automatically. Outside `auto` mode, enable the sandbox with `agy --sandbox` or `"enableTerminalSandbox": true`.
*   **Browser checks**: Run [`/browser`](/docs/commands/browser) against local Google Chrome (`v144+`) with remote debugging enabled.
*   **Interactive diff viewer**: Run [`/diff`](/docs/cli/commands/diff) to inspect **All Changes**, **Per Turn**, and **Commit Tree** views. Press c on any line to attach feedback for your next prompt.

### Example `Deny` rules

Add standing `Deny` rules in [Permissions](/docs/permissions) to block destructive commands and protect sensitive paths regardless of preset:

```text
command(rm -rf)                    # Block destructive deletions
command(regex:curl .*)             # Block unvetted curl downloads
command(sudo)                      # Block sudo privileges
write_file(.git/)                  # Safeguard Git history
write_file(/home/user/.ssh)        # Safeguard SSH keys
```

* * *

## Catch hallucinations before they ship

Three habits eliminate most hallucination issues:

*   **Ground the agent in primary sources.** Point to real workspace files, package manifests (`package.json`, `pyproject.toml`), or the [Google Developer Knowledge MCP server](/docs/mcp#example-search-google-developer-docs) instead of relying on model memory.
*   **Keep tests honest.** Review test diffs alongside implementation diffs so a failing assertion is fixed at the root cause, never deleted or loosened.
*   **Inspect visual output directly.** For frontend, canvas, or 3D apps, passing unit tests do not prove the page renders cleanly. Run a live browser check and inspect the screenshot.

Watch for silently weakened tests

Check test files first when reviewing a diff in **Review** or `/diff`. For high-stakes changes, run [`/swarm`](/docs/swarm) and pin `@verifier` to a different model. A second model helps ensure existing assertions stayed intact.

```prompt
Run the unit tests, start the local dev server, and use /browser to verify the main flow loads with zero console errors and no horizontal overflow on desktop and mobile viewports.
```

* * *

## Next steps

[

Put it into practice

Build a playable 3D browser world

See unit tests, a dedicated @verifier worker, and /browser visual checks working together.

](/docs/learn/build-3d-browser-world/)[

Security

Permissions

Configure Deny, Ask, and Allow rules across files, terminal commands, and MCP tools.

](/docs/permissions/)[

Verification

Browser use

Let Antigravity open your running web app, inspect console logs, and capture screenshots.

](/docs/browser/)