# Rules

Rules provide persistent, manually defined constraints to guide agent behaviors, code style, and architectural patterns.

A rule is a Markdown file containing constraints that guide the agent’s code generation, tool usage, and testing patterns. Rules files are limited to 12,000 characters each.

Note

**Note**: Antigravity defaults to `.agents/rules`, but still maintains backward compatibility for `.agent/rules`.

## Rule activation modes

At the rule level, you can configure how the agent applies constraints:

*   **Manual**: explicitly activated via `@mention` in the agent prompt.
*   **Always on**: continuously active for all agent interactions.
*   **Model decision**: the model dynamically evaluates the rule’s natural language description to determine relevance.
*   **Glob pattern**: automatically applied whenever the agent edits files matching specified patterns (such as `*.py` or `src/**/*.ts`).

## @ mentions

You can reference other files using `@filename` in a rules file:

*   **Relative path**: interpreted relative to the location of the rules file.
*   **Absolute path**: resolved as a true absolute path first; if that file does not exist, it falls back to resolving relative to the workspace root (for example, `@/path/to/file.md` resolves to `/path/to/file.md`, or `workspace/path/to/file.md` if `/path/to/file.md` does not exist).

## Configuration by surface

Select your surface below to configure global or workspace-specific rules:

*   [Antigravity 2.0](#tab-panel-48)
*   [Antigravity CLI](#tab-panel-49)
*   [Antigravity IDE](#tab-panel-50)

### Managing rules in Antigravity 2.0

To get started with rules in Antigravity 2.0:

1.  Open the **Customizations** panel from the application menu or project settings.
2.  Select the **Rules** tab.
3.  Click **\+ Global** to create global rules, or **\+ Workspace** to create rules scoped to the active project.

### Antigravity 2.0 file locations

*   **Global rules**: saved to `~/.gemini/GEMINI.md` and applied across all projects.
*   **Workspace rules**: saved to the `.agents/rules/` directory at the root of your workspace or Git repository.

### Managing rules in Antigravity CLI

The Antigravity CLI reads rules from standard workspace directories, user profiles, and installed plugins:

### CLI file locations

*   **Workspace rules**: place markdown files in `.agents/rules/` at your repository root (e.g., `.agents/rules/testing-style.md`).
*   **Global rules**: place markdown rules in `~/.gemini/antigravity-cli/rules/` or define persistent global constraints in `~/.gemini/GEMINI.md`.
*   **Plugin rules**: rules packaged inside installed CLI plugins under `~/.gemini/antigravity-cli/plugins/<plugin_name>/rules/` are activated automatically.

### CLI activation

The CLI evaluates all workspace and global rules during prompt expansion, injecting applicable rules into the agent’s context window before executing commands.

### Managing rules in Antigravity IDE

In the standalone Antigravity IDE:

1.  Click the **…** menu at the top of the agent side panel.
2.  Select **Customizations**, then navigate to the **Rules** tab.
3.  Click **\+ Global** to author workstation-wide rules, or **\+ Workspace** to create project-specific rules.

### Antigravity IDE file locations

*   **Workspace rules**: stored in `.agents/rules/` within your open project.
*   **Global rules**: stored in `~/.gemini/GEMINI.md`.