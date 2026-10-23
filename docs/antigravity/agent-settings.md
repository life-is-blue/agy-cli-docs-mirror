# Agent settings

Available on: Antigravity App, Antigravity CLI

Configure how the Antigravity agent executes terminal commands, modifies files, and uses the terminal sandbox across the desktop application and CLI.

## Antigravity App

### Updated permission settings

#### Permission settings

This setting controls how agent actions—terminal commands, file access, MCP tools, and web page reads—are approved using a **permission preset**:

*   **Request Review** (_“Every command requires approval.”_): The sandbox is off and every terminal command requires approval. The agent can read and write the workspace, and needs approval for anything else.
*   **Default** (_“Ask before sensitive operations.”_): Commands run without prompting inside the [Terminal sandbox](/docs/sandbox); running outside the sandbox requires approval. The agent can read and write the workspace and temp directories, and needs approval for anything else.
*   **Auto (Preview)** (_“Automatically decide if commands run.”_): Commands run without prompting inside the [Terminal sandbox](/docs/sandbox), and the agent can read and write workspace and temporary directories without asking. When a command needs to run outside the sandbox, Antigravity automatically evaluates it so safe, reversible commands proceed without prompting while risky or irreversible actions still pause for your approval.
*   **Turbo** (_“Run all commands without restrictions.”_): All commands run without prompting with no isolation or restrictions, and the agent has full read and write access to your filesystem.

Your configured allow, deny, and ask permission rules are layered on top of the preset and always take precedence. To learn more, refer to **[Agent permissions](/docs/permissions)**.

Note

**Auto (Preview)** is available in `v2.23.0+`. It isn’t currently available for business or enterprise accounts, including [Antigravity in Gemini Enterprise](/docs/enterprise).

#### Change your permission preset

You can change the preset in three places:

*   **For all projects**: Open **Settings** > **General** > **Global Permissions** > **Permission Preset**.
*   **For a single project**: Override the global preset under **Settings** > **Projects**. Projects default to **Inherit Global**, which follows your global preset.
*   **From the message box** (`v2.23.0+`): Choose a preset from the permissions picker. The picker changes your global preset, or the project’s preset if the project overrides it. To remove a project override, choose **Use Global Settings**.

For screenshots of the Settings selector and the message box picker, refer to **[Change your permission preset](/docs/permissions#change-your-permission-preset)**.

### Previous permission settings

Note

Business and enterprise accounts use the following settings instead of the permission presets above.

#### Terminal command auto execution

This setting controls how the agent executes generated shell commands:

*   **Require Review**: The agent never executes terminal commands without prompting (except those explicitly added to your configurable Allow list).
*   **Proceed in Sandbox**: Commands run without prompting inside the [Terminal sandbox](/docs/sandbox); commands that need to run outside it still require review.
*   **Always Proceed**: The agent executes commands without prompting (except those explicitly added to your configurable Deny list).

#### Agent non-workspace file access

This setting allows the agent to view and edit files outside of the active project folders:

*   By default, the agent only has access to the folders inside your project and the application’s local app data directory `~/.gemini/antigravity/` (which contains artifacts, knowledge items, and more).
*   Enforcing this boundary protects your local sensitive data. Enable non-workspace access with caution.

#### Terminal sandbox mode

This setting restricts agent terminal commands to an isolated sandbox:

*   When enabled, shell commands execute inside the sandbox without access to sensitive system paths or unauthorized networks.
*   You can configure this setting globally in application preferences or override it per project.
*   To learn more, refer to the **[Terminal sandbox](/docs/sandbox)** guide.

## Antigravity CLI

### Agent execution and permission settings

Antigravity CLI lets you configure how the agent edits files, runs shell commands, and enforces workspace boundaries through `/config` (`/settings`), `~/.gemini/antigravity-cli/settings.json`, or command-line flags:

*   **Agent Mode (`agentMode` / `--mode`)**: Controls the session execution mode (cycle during a session with Shift + Tab):
    *   `default` (the default; leave `agentMode` unset): Prompts for interactive diff review before modifying or creating files.
    *   `accept-edits`: Automatically approves workspace file edits and creations.
    *   `auto` (Preview): Automatically approves workspace file edits, runs terminal commands inside the [Terminal sandbox](/docs/sandbox) by default, and automatically evaluates commands that need to run outside the sandbox so safe, reversible commands run without prompting while risky or irreversible commands pause for approval. When active, the bottom-right status bar shows `auto` and the prompt input displays `Auto mode: edits & safe commands auto-approved (shift+tab to cycle)`.
    *   `plan`: Analyzes the codebase and outlines a plan before making edits.
*   **Tool Permission (`toolPermission`)**: Controls the baseline authorization policy for tools:
    *   `request-review` (default): Prompts for approval before running write, shell, or web tools.
    *   `proceed-in-sandbox`: Automatically runs sandboxed terminal commands and prompts when commands need to run outside the sandbox.
    *   `strict`: Prompts before all non-read tool calls (overrides `auto` mode).
    *   `always-proceed`: Runs all tools without prompting (overrides `auto` mode; also activated by `--dangerously-skip-permissions`).
*   **Sandbox Mode (`enableTerminalSandbox` / `--sandbox`)**: Restricts agent shell commands to an OS-level container boundary (`false` by default, and enabled automatically in `auto` mode).
*   **Non-Workspace Access (`allowNonWorkspaceAccess`)**: Controls whether the agent can read or write files outside your active workspace directories (`false` by default).

Note

`auto` mode is available in `v1.3.5+` on **macOS and Linux** and `v1.4.4+` on **Windows**. Starting in `v1.4.4`, if the terminal sandbox isn’t available on your machine, `auto` and `proceed-in-sandbox` aren’t offered, and Sandbox Mode has no effect. To learn more, refer to **[Terminal sandbox](/docs/sandbox)**.

### Example configuration

Configure your preferred agent execution settings in `~/.gemini/antigravity-cli/settings.json`:

```json
{
    "agentMode": "auto"
}
```

To learn more, refer to **[Choose an execution mode](/docs/cli/modes)**, **[Settings](/docs/settings)**, **[Agent permissions](/docs/permissions)**, and **[Terminal sandbox](/docs/sandbox)**.