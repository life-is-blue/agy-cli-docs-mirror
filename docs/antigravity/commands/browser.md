# Browser command (/browser)

Available on: Antigravity App, Antigravity CLI

Hand a web task directly to the **`browser` subagent** to open pages, interact with your running app, inspect console and network activity, capture screenshots, and verify visual fixes.

## Overview

Many development tasks end in a browser: confirming that a layout fix rendered, reproducing a console error, filling in a form end to end, or verifying a signed-in flow. Typing `/browser` instructs the main agent to delegate your request to the specialized `browser` subagent in its own isolated context window:

*   **Antigravity App (built-in browser, personal Google Accounts `v2.30.0+`)**: Runs directly inside the App’s built-in side-panel browser with zero external browser setup, parallel tabs across concurrent subagents, an animated live cursor, a one-click **Stop** takeover button, and pause-and-resume sign-in handoff. On these accounts, the main agent also starts `browser` subagents automatically from plain-language prompts—you don’t have to type `/browser` unless you want to force a browser subagent run. For the complete App walkthrough and demos, refer to [Browser use](/docs/browser).
*   **Antigravity CLI, Antigravity IDE (`v2.6.0+`), and business/enterprise accounts in the Antigravity App (Chrome DevTools MCP)**: Controls your running local Google Chrome (`v144+`) through the Chrome DevTools MCP server, which Antigravity starts automatically when `/browser` is invoked (using `npx` in the CLI and IDE, or the App’s bundled Node.js runtime). Supports Chrome DevTools performance traces, Lighthouse audits, heap snapshots, device/network throttling, custom script evaluation (`evaluate_script`), and optional WebM session recordings when interacting with a page. Chrome must already be running on the same machine with remote debugging enabled; refer to [Set up Chrome](#set-up-chrome).

Note

Your organization’s administrator can disable browser access, in which case `/browser` doesn’t appear in the command menu. `/browser` is also supported in the Antigravity IDE (`v2.6.0+`) and the Google Antigravity VS Code extension (`v1.9.0+`) for local workspaces; refer to the [IDE browser overview](/docs/ide/browser).

## Run a browser task

Type `/browser` followed by the task. Describe a clear end condition so the subagent knows when to return, such as “report whether X renders” or “capture a screenshot of Y.”

### Antigravity App

Type `/browser` in the message box (or, on a personal Google Account in `v2.30.0+`, ask in plain language):

```prompt
/browser Open http://localhost:3000, resize to a 390px-wide mobile viewport, verify the navigation drawer opens and closes, and capture a screenshot of each state
```

On personal Google Accounts (`v2.30.0+`), the built-in browser opens a side-panel tab where you can watch the subagent live or click **Stop** to take over, or click the subagent’s name in your conversation to inspect its step log:

Running the browser subagent in the Antigravity App (via /browser or plain language on personal accounts v2.30.0+): watch the subagent open localhost:5174/checkout in a built-in browser tab, reproduce a calculation bug with the live animated cursor, and verify the updated total after applying a code fix.

To comment on a screenshot, ask the agent to save it to the conversation’s artifacts or click **Add screenshot to conversation** in the browser toolbar. For parallel tabs and sign-in handoff demos, refer to [Browser use](/docs/browser) and [Screenshots](/docs/screenshots).

### Antigravity CLI

Make sure Chrome remote debugging is enabled (refer to [Set up Chrome](#set-up-chrome)), and then type the command in the interactive prompt:

```prompt
/browser Open http://localhost:3000/dashboard, verify that the analytics charts render, and report any console errors
```

Press Alt + J or run [`/agents`](/docs/cli/commands/agents) to switch into the subagent’s conversation and watch it work, or press Ctrl + K to approve a site request from your main conversation.

## Set up Chrome

Tip

If you’re signed in to the Antigravity App (`v2.30.0+`) with a personal Google Account, skip this section—`/browser` runs inside the built-in browser with no Chrome or Node.js setup required.

When running `/browser` in the Antigravity CLI, in the Antigravity IDE (`v2.6.0+`, or the Google Antigravity VS Code extension `v1.9.0+`), or on a business or enterprise account in the Antigravity App, the subagent attaches to Google Chrome (version 144 or later) that’s already running on the **same local machine** as your workspace (remote SSH, Dev Container, and cloud workstation sessions cannot attach to Chrome on your local computer). It doesn’t launch Chrome for you, and Chrome doesn’t need to be signed in. Before you run `/browser`:

1.  **In the Antigravity CLI or IDE**: Ensure [Node.js](https://nodejs.org/) is installed so `npx` is on your `PATH` (used to launch `chrome-devtools-mcp`; the desktop Antigravity App includes its own bundled runtime).
2.  Open Google Chrome (`v144+`).
3.  Go to `chrome://inspect/#remote-debugging`.
4.  Turn on **Allow remote debugging for this browser instance**.

If remote debugging is off, Antigravity displays **Remote Debugging Required** with these steps. When the subagent connects, Chrome asks you to allow remote debugging—click **Allow** within 60 seconds so the subagent can attach to the browser.

## What the browser subagent can do

Both browser engines navigate pages, click, hover, drag, type, upload approved files, capture screenshots and page snapshots, resize viewports, and inspect console errors and network requests. When connected to Chrome through Chrome DevTools MCP, the subagent additionally exposes DevTools profiling and auditing tools:

| Capability | Built-in browser (App `v2.30.0+`, personal accounts) | Chrome DevTools MCP (CLI, IDE, and App business/enterprise) |
| :-- | :-- | :-- |
| **Navigate and manage tabs** | Open URLs, wait for pages, and run multiple `browser` subagents in parallel isolated tabs. | Open a URL, create or close pages, switch tabs, and wait for elements or text. |
| **Interact with the page** | Click, double-click, right-click, hover, drag, scroll, press keys, type text, select options, and upload or download approved files, with live cursor visualization and **Stop** takeover. | Click, hover, drag, press keys, type text, fill fields or forms, upload files, and handle dialogs. |
| **Inspect state** | Capture page snapshots and screenshots, and read console messages and sanitized network requests. | Capture accessibility snapshots and screenshots, list console messages and network requests, and record optional WebM interaction videos. |
| **Debug, profile, and emulate** | Resize the viewport and verify live hot-reload changes without external setup. | Evaluate JavaScript (`evaluate_script`), run performance traces and Lighthouse audits, take heap snapshots, and emulate slow networks or CPU throttling. |

In the Antigravity App (`v2.30.0+`), open **Settings** > **Browser** and go to the **Browser Subagent** section to configure browser permissions:

*   **Browser Actuation Rules**: Click **Edit** to manage **Execute URLs** (sites the subagent can open without asking or must never open) and **Download files** (sites the subagent may download from). For matching rules, `localhost:port` isolation, and enterprise domain policies, refer to [Allowlist and denylist](/docs/ide/allowlist-denylist).
*   **Browser Javascript Execution Policy** _(Chrome DevTools MCP only)_: Choose whether the Chrome-based subagent can run custom JavaScript (`evaluate_script`) in the page. **Request Review** (the default) asks for your approval first, **Always Proceed** runs scripts without asking, and **Disabled** blocks them. When the built-in browser agent is active, arbitrary in-page JavaScript execution isn’t used, so this setting is hidden.

If your organization’s administrator has disabled the browser subagent, the section displays a notice instead of these settings. In the Antigravity IDE (`v2.6.0+`), click **Antigravity** in the status bar and select **Open Settings** > **Browser** to manage the same controls; refer to the [IDE browser overview](/docs/ide/browser).

## Example tasks

The following prompts show typical `/browser` workflows:

*   **Verify a UI fix**:
    
    ```prompt
    /browser Reload http://localhost:5173/settings and confirm the save button is no longer disabled after editing the display name
    ```
    
*   **Reproduce a console error**:
    
    ```prompt
    /browser Go to http://localhost:3000/checkout, add any item to the cart, and report the full text and stack of any console errors
    ```
    
*   **Check responsive and slow-network behavior**:
    
    ```prompt
    /browser Load http://localhost:3000 with a Slow 3G network profile and a 375px viewport, then screenshot the hero section once it finishes loading
    ```
    
*   **Research documentation**:
    
    ```prompt
    /browser Open the Astro docs for content collections and summarize how to define a schema with zod
    ```
    

## Next steps

Explore related documentation:

*   [Browser use](/docs/browser): Watch live built-in browser workflows, parallel browser tabs, sign-in handoff, and browser settings in the Antigravity App.
*   [Subagents](/docs/subagents): Learn how built-in and custom subagents run in isolated contexts.
*   [Permissions](/docs/permissions): Control which browser tools run automatically and which ask first.
*   [Artifacts](/docs/artifacts): Find screenshots and session recordings the subagent produces.
*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.