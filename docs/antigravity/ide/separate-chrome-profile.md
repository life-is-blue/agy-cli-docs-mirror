# Chrome profile

Available on: Antigravity App, Antigravity IDE

The browser subagent doesn’t use a separate Chrome profile. When you run [`/browser`](/docs/commands/browser), the subagent connects to the Google Chrome that’s already running on your computer, through Chrome’s remote debugging, and works in that browser. Antigravity doesn’t start Chrome for you or create a profile for the agent.

Because the subagent works in your own Chrome, it uses the same cookies and sign-ins as your normal browsing. It can open pages on sites where you’re signed in, so allow only the sites that you want it to act on. For details, refer to [Allowlist and denylist](/docs/ide/allowlist-denylist).

## Connect the subagent to Chrome

1.  Open Google Chrome.
2.  Go to `chrome://inspect/#remote-debugging`.
3.  Turn on **Allow remote debugging for this browser instance**.

When the subagent connects, Chrome asks whether to allow remote debugging. Click **Allow**. For details, refer to [Set up Chrome](/docs/commands/browser#set-up-chrome).

## Built-in browser in the Antigravity App

The Antigravity App also has a built-in browser, which opens web pages in the side panel. It’s separate from Chrome: it keeps its own cookies and sign-ins for each account that you use in Antigravity, and they persist when you restart the app. To clear its history, go to **Settings** > **General** > **Built-in Browser** and click **Clear** next to **Browsing History**. The Antigravity IDE doesn’t have a built-in browser.