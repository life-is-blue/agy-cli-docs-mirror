# Browser overview

Available on: Antigravity IDE

Google Antigravity can open, read, and actuate a local Chrome browser, enabling you to test development websites, read documentation sources, and automate a variety of browser tasks.

* * *

## Core mechanisms

Type [`/browser`](/docs/commands/browser) in the Agent panel to hand a task to the browser subagent. The subagent drives your own Google Chrome through the Chrome DevTools MCP server, which Antigravity IDE starts with `npx`. Before you use it, install [Node.js](https://nodejs.org/) so that `npx` is on your `PATH`, and start Chrome with remote debugging turned on, as described in [Set up Chrome](/docs/commands/browser#set-up-chrome).

The subagent can take screenshots, and when it interacts with a page, it can record its actions as a WebM video. For details, refer to [Browser recordings](/docs/ide/browser-recordings).

To control what the subagent can do, click **Antigravity - Settings** in the status bar and select **Browser**. **Browser Javascript Execution Policy** controls whether the agent can run custom JavaScript in the page, and **Browser Actuation Rules** sets the URLs the subagent is allowed or denied.