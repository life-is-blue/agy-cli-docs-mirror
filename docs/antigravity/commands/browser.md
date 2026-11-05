# Browser command (/browser)

Available on: Antigravity App, Antigravity CLI

Hand a web task to the **`browser` subagent**, which drives Google Chrome to navigate pages, interact with your running app, inspect the console and network, capture screenshots, and record video of its actions on a page.

## Overview

Many development tasks end in a browser: confirming that a layout fix rendered, reproducing a console error, filling in a form end to end, or reading a page of documentation. The `/browser` command tells the main agent to delegate your request to the specialized `browser` subagent through its `invoke_subagent` tool.

The `browser` subagent is purpose-built for this work:

*   **Real Chrome, real DevTools**: the subagent controls your own Google Chrome through the Chrome DevTools MCP server, which Antigravity starts automatically when the subagent is invoked. Chrome must already be running with remote debugging turned on; refer to [Set up Chrome](#set-up-chrome).
*   **Isolated context**: like other [subagents](/docs/subagents), it runs in its own conversation with a clean context window, so long page snapshots and console logs don’t crowd out your main conversation.
*   **Session recordings**: when the subagent interacts with a page, such as clicking, typing, or filling in a form, Antigravity can record those actions and save a WebM video to the subagent’s artifacts after it finishes, so you can play back what it did. Sessions that only open pages or take screenshots don’t produce a recording.
*   **On demand only**: the `browser` subagent is hidden from the agent’s normal subagent list. The main agent uses it only when you invoke `/browser`.

Note

The `browser` subagent isn’t available in the Antigravity IDE, and your organization’s administrator can disable browser access, in which case `/browser` doesn’t appear in the command menu. For browser features in the Antigravity IDE, refer to the [IDE browser overview](/docs/ide/browser).

## Run a browser task

Type `/browser` followed by the task. Describe a clear end condition so the subagent knows when to return, such as “report whether X renders” or “capture a screenshot of Y.”

### Antigravity App

Type the command in the composer:

```prompt
/browser Open http://localhost:3000, resize to a 390px-wide mobile viewport, verify the navigation drawer opens and closes, and capture a screenshot of each state
```

Click the subagent’s name in your conversation to follow its progress in the side panel. Screenshots appear in its steps; to comment on one, ask the agent to save it to the conversation’s artifacts. For details, refer to [Screenshots](/docs/screenshots).

### Antigravity CLI

Type the command in the interactive prompt:

```prompt
/browser Open http://localhost:3000/dashboard, verify that the analytics charts render, and report any console errors
```

Press Alt+J or run `/agents` to switch into the subagent’s conversation and watch it work.

## Set up Chrome

The subagent attaches to Google Chrome (version 144 or later) that’s already running on your computer. It doesn’t launch Chrome for you, and Chrome doesn’t need to be signed in. Before you run `/browser`:

1.  Open Google Chrome.
2.  Go to `chrome://inspect/#remote-debugging`.
3.  Turn on **Allow remote debugging for this browser instance**.

If remote debugging is off, the App shows **Remote Debugging Required** with these steps. When the subagent connects, Chrome asks you to allow remote debugging. Accept the prompt so the subagent can attach to the browser.

## What the browser subagent can do

The subagent has access to a focused set of Chrome DevTools tools:

| Capability | Examples |
| :-- | :-- |
| **Navigate and manage tabs** | Open a URL, create or close pages, switch between tabs, wait for an element or text to appear. |
| **Interact with the page** | Click, hover, drag, press keys, type text, fill individual fields or whole forms, upload files, handle dialogs. |
| **Inspect state** | Take an accessibility snapshot of the page, capture a screenshot, list or fetch console messages and network requests. |
| **Debug and profile** | Evaluate JavaScript in the page, start and stop a performance trace, analyze performance insights, run a Lighthouse audit, take a heap snapshot. |
| **Emulate conditions** | Resize the viewport and emulate device and network conditions, such as throttled connections and CPU slowdown. |

Running JavaScript in the page (`evaluate_script`) prompts for your approval by default. All other browser tools are allowed automatically for the subagent. You can adjust this in your [tool permissions](/docs/permissions).

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

*   [Subagents](/docs/subagents): Learn how built-in and custom subagents run in isolated contexts.
*   [Permissions](/docs/permissions): Control which browser tools run automatically and which ask first.
*   [Artifacts](/docs/artifacts): Find screenshots and session recordings the subagent produces.
*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.