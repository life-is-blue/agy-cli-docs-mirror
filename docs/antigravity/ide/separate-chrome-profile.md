# Chrome profile

Available on: Antigravity App, Antigravity IDE

Which browser profile the browser subagent uses depends on where it runs:

*   **Built-in browser in the Antigravity App (personal Google Accounts, `v2.30.0+`)**: The browser subagent runs directly inside the App’s built-in side-panel browser rather than Google Chrome. It keeps an isolated, persistent cookie profile per Antigravity account, separate from Chrome; refer to [Browser use](/docs/browser).
*   **Google Chrome via [`/browser`](/docs/commands/browser) (Antigravity IDE, Antigravity CLI, and business/enterprise accounts in the Antigravity App)**: The subagent doesn’t create a separate Chrome profile. Instead, it connects to the Google Chrome that’s already running on your computer through Chrome’s remote debugging and works in that browser.

Because the Chrome-based `/browser` subagent works in your own Chrome, it shares the same cookies and sign-ins as your normal Chrome browsing. It can open pages on sites where you’re signed in, so allow only the sites that you want it to act on. For details, refer to [Allowlist and denylist](/docs/ide/allowlist-denylist).

## Connect the subagent to Chrome

1.  Open Google Chrome (version 144 or later).
2.  Go to `chrome://inspect/#remote-debugging`.
3.  Turn on **Allow remote debugging for this browser instance**.

When the subagent connects, Chrome asks whether to allow remote debugging—click **Allow** within 60 seconds. Chrome must be running on the same local machine as your workspace (and in the Antigravity IDE or CLI, Node.js must be installed so `npx` is on your `PATH`). For details, refer to [Set up Chrome](/docs/commands/browser#set-up-chrome).

## Built-in browser profile in the Antigravity App

The Antigravity App’s built-in browser opens web pages in the side panel with its own cookies and sign-ins for each account that you use in Antigravity, persisting across tabs and app restarts. To clear visited URLs and autocomplete suggestions, go to **Settings** > **Browser** (`v2.30.0+`) > **Built-in Browser** and click **Clear** next to **Browsing History**. To clear cookies and storage for a specific site, click the connection security icon in the address bar and select **Delete cookies and site data**. The Antigravity IDE doesn’t include a built-in browser.