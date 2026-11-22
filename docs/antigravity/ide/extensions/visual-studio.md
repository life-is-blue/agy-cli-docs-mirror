# Visual Studio

The **Antigravity for Visual Studio** extension brings Google’s agentic engineering platform to Windows and .NET developers working with complex enterprise solutions and multi-project MSBuild architectures.

[1\. Download Visual Studio 2026](https://visualstudio.microsoft.com/vs/)Get Visual Studio 2026 for Windows if you don't have it installed yet.

[2\. Install Antigravity extension](https://marketplace.visualstudio.com/items?itemName=Google.GoogleAntigravity)Download the official Google Antigravity VSIX extension from the Visual Studio Marketplace.

* * *

## Prerequisites

Ensure that you meet the following prerequisites before installing the extension:

*   **Visual Studio**: Visual Studio 2022 (version 17.14 or later) or Visual Studio 2026 on Windows 10 or 11.
*   **Antigravity entitlement**: A valid Google Account with any Antigravity plan (including the free tier) or a **Gemini Enterprise** entitlement.

* * *

## Installation and setup

Complete the following steps to install the Visual Studio extension:

1.  Open Visual Studio 2026.
2.  In the top menu, navigate to **Extensions** > **Manage Extensions**.
3.  In the search box in the top-right corner, enter **Google Antigravity**.
4.  Select the official **Google Antigravity** extension published by **Google** and click **Download**.
5.  Close all Visual Studio instances to allow the VSIX installer to complete the installation.
6.  Reopen Visual Studio. The **Antigravity** tool window opens automatically on first launch, docked as a tab next to Solution Explorer. To open it later, navigate to **View** > **Other Windows** > **Antigravity**, or press Ctrl + \\, Ctrl + Alt + L.

![Antigravity in Visual Studio](/assets/image/blog/visual-studio-extension-marketplace.png)

* * *

## Authentication and sign-in

Antigravity uses a unified sign-in across all surfaces. Learn more about authentication and entitlements:

[Gemini Enterprise authentication](/docs/enterprise)Learn how enterprise developers and administrators configure sign-in with Google Cloud credentials and IAM policies.

[Antigravity App overview](/docs/overview)Learn how sign-in and account entitlements work across the Antigravity App and developer surfaces.

* * *

## Work with Antigravity in Visual Studio

The extension integrates with Visual Studio’s native windows and solution model:

*   **Antigravity tool window**: The chat window where you converse with the agent. Dock it anywhere, like any other Visual Studio tool window. Antigravity restores your last active conversation for each solution when you restart Visual Studio.
*   **Antigravity Settings tool window**: A separate, dockable settings window that keeps its state across restarts.
*   **Solution sync**: Antigravity uses the folder of the open solution (or your **Open Folder** workspace) as the agent’s workspace, and follows along when you switch solutions or folders, asking first if a chat is in progress.
*   **Output window**: Choose **Google Antigravity** in the Output window to see extension logs, or **Google Antigravity Language Server** to stream logs from the background server.

* * *

## Keyboard shortcuts

Antigravity shortcuts in Visual Studio are chords that start with Ctrl + \\. Press Ctrl + \\, release both keys, then press the second key combination.

| Action | Shortcut |
| --- | --- |
| Open or close the Antigravity tool window, adding the active file or selection as context | Ctrl + \\, Ctrl + Alt + L |
| Start a new conversation | Ctrl + \\, Ctrl + Shift + L |
| Approve a pending agent step | Ctrl + \\, Alt + Enter |
| Reject a pending agent step | Ctrl + \\, Shift + Alt + Enter |
| Interrupt the running agent | Ctrl + \\, Esc |

* * *

## Review agent changes

When the agent edits files, Antigravity shows each change as an inline or side-by-side diff in Visual Studio’s native diff viewer so you can review it:

*   **Accurate diffs**: Changes are computed with Visual Studio’s hierarchical diff engine, with word-level comparison and normalized line endings (`CRLF` and `LF`).
*   **Batch controls**: Use the **Accept All** and **Reject All** bar to apply or discard the agent’s edits. Files under review stay read-only until you decide.
*   **Artifacts**: [Artifacts](/docs/artifacts) such as implementation plans (for example, after you run [`/plan`](/docs/plan)) and walkthroughs open in Visual Studio document tabs.

* * *

## Agents and agent settings

In the **Antigravity** tool window, you can track the parent agent and any child [subagents](/docs/subagents) it starts, such as the built-in `research` and `self` subagents or your own custom subagents. Each subagent can share its parent’s workspace (`inherit`), work in an isolated Git worktree (`branch`), or share directory storage (`share`). Review the evidence each agent gathers in its [artifacts](/docs/artifacts).

In the **Antigravity Settings** tool window, you can control how much the agent does on its own:

*   **[Terminal command auto execution](/docs/agent-settings#terminal-command-auto-execution)**: Choose **Request Review** to approve each command, or **Always Proceed** to let the agent run commands without asking.
*   **[Non-workspace file access](/docs/agent-settings#agent-non-workspace-file-access)**: Allow or block the agent from reading and editing files outside your workspace.

* * *

## Model Context Protocol (MCP)

Connect the agent to databases such as BigQuery, Spanner, AlloyDB, and Cloud SQL for SQL Server, and to tools such as GitHub, Atlassian, Linear, and Notion, through [MCP servers](/docs/mcp):

*   **MCP Store**: Browse and install [supported MCP servers](/docs/mcp#supported-mcp-servers) from the built-in MCP Store.
*   **Configuration file**: Add servers manually in `~/.gemini/config/mcp_config.json` (all projects) or `.agents/mcp_config.json` in your workspace (that workspace only).

Credentials for MCP servers stay on your machine, and the agent asks for your approval before it calls an MCP tool, unless you change that in your [permission settings](/docs/permissions).