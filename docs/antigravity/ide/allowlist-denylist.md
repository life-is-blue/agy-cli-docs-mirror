# Allowlist and denylist

Available on: Antigravity IDE

The browser uses a two-layer security system to control which URLs can be accessed:

*   **Denylist**: Denies dangerous or malicious URLs.
*   **Allowlist**: Explicitly allows trusted URLs.

## How it works

### Denylist

Google maintains and enforces the denylist on its servers. Before the browser opens a URL, Antigravity checks the hostname against this server-side denylist.

**Note:** If the server is unavailable, access is denied by default.

### Allowlist

The allowlist is a local text file (`~/.gemini/antigravity/browserAllowlist.txt`) that you can edit to explicitly trust specific URLs.

![Allowlist](/assets/image/docs/browser-allowlist.png)

The allowlist is initialized with only `localhost`, and you can edit it at any time.

When the browser attempts to navigate to a URL that isn’t on the allowlist, it prompts you with an **Always allow** button. Clicking this button adds the URL to the allowlist and enables the browser to open and interact with the web page, as shown in the following example:

![Always Allow](/assets/image/docs/always-allow-url.png)

You can also add or remove URLs from the allowlist manually. However, the denylist always takes precedence: you cannot allowlist a URL that appears on the denylist.