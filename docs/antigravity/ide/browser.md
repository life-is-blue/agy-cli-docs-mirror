# IDE browser overview

Available on: Antigravity IDE

In the Antigravity IDE (`v2.6.0+`) and the Google Antigravity VS Code extension (`v1.9.0+`), the agent can open, read, and actuate a local Google Chrome browser through [`/browser`](/docs/commands/browser) to test local development sites, read documentation, and verify visual changes.

Tip

Looking for zero-setup built-in browser automation? The built-in side-panel browser, plain-language auto-invocation, parallel browser tabs, live animated cursor, and pause-and-resume sign-in handoff are available exclusively in the **[Antigravity App](/docs/browser)** (`v2.30.0+`, personal Google Accounts). Antigravity IDE doesn’t include a built-in browser and always runs browser tasks in your local Google Chrome when you invoke [`/browser`](/docs/commands/browser).

* * *

## Prerequisites and setup

Type [`/browser`](/docs/commands/browser) followed by your task in the Antigravity panel to delegate a web check to the `browser` subagent (plain-language prompts don’t auto-launch the browser subagent in the IDE). The subagent drives your local Google Chrome through the Chrome DevTools MCP server, which Antigravity IDE starts with `npx`:

1.  Install [Node.js](https://nodejs.org/) so that `npx` is available on your `PATH`.
2.  Open Google Chrome (version 144 or later) on the **same machine** as your workspace, go to `chrome://inspect/#remote-debugging`, and turn on **Allow remote debugging for this browser instance** (refer to [Set up Chrome](/docs/commands/browser#set-up-chrome)).
3.  Run `/browser <task>` in the Antigravity panel, and click **Allow** within 60 seconds when Chrome asks whether to allow remote debugging.

Note

**Local workspaces only**: Because the Chrome DevTools MCP server runs alongside the workspace agent process, `/browser` works in local workspaces where Antigravity IDE and Google Chrome run on the same computer. In Remote-SSH, Dev Containers, or cloud workstation sessions, the remote agent host can’t attach to Chrome on your local machine.

## Capabilities and settings

Once connected to Chrome, the `browser` subagent can navigate pages, click and fill in forms, inspect console messages and network requests, run performance traces and Lighthouse audits, take screenshots, and optionally record page interactions as a WebM video (refer to [Browser recordings](/docs/ide/browser-recordings)). Because `/browser` shares a single live Chrome connection and your active Chrome profile, run one browser session at a time; refer to [Chrome profile](/docs/ide/separate-chrome-profile).

To control what the subagent can do, click **Antigravity** in the status bar and select **Open Settings** > **Browser** (or click **More Actions…** in the Antigravity panel header > **Open Settings**, or run **Antigravity: Open Settings** from the Command Palette):

*   **Enable Browser Tools**: Turns agent browser tools on or off.
*   **Browser Javascript Execution Policy**: Controls whether the `/browser` subagent asks for review (**Request Review**, default), runs automatically (**Always Proceed**), or blocks custom JavaScript (`evaluate_script`) in the page (**Disabled**).
*   **Browser Actuation Rules**: Click **Edit** to configure allowed and denied sites for opening URLs and downloading files; refer to [Allowlist and denylist](/docs/ide/allowlist-denylist).