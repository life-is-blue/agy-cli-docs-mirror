# Allowlist and denylist

Available on: Antigravity App, Antigravity IDE

Antigravity asks before the [browser subagent](/docs/browser) opens a site or downloads a file from a domain that you haven’t allowed. To decide ahead of time, add rules to **Browser Actuation Rules**: allow the sites that the subagent can open or download from without asking, and deny the ones that it must never use.

## When the subagent opens a site or downloads a file

When the subagent tries to open a page on a site that has no rule, Antigravity prompts **Allow executing actions on this URL?** and asks you to choose one of the following:

| Option | What it does |
| :-- | :-- |
| **Yes, allow this time** | Allows the site for the rest of the subagent’s current task. |
| **Yes, allow** _domain_ **in this conversation** | Allows the site until the conversation ends. |
| **Yes, always allow** _domain_ | Adds an allow rule for the site to your Browser Actuation Rules. |
| **No** | Denies the request. You can tell the agent what to do instead. |

When the built-in browser agent triggers a file download (`v2.31.0+`), a matching **Allow the browser agent to download a file?** prompt offers per-run, conversation, or always-allow choices for that domain (`data:` and `blob:` downloads always ask for one-time approval, and executable or active-markup file types are automatically blocked). Refer to [Permissions and safety guardrails](/docs/browser#permissions-and-safety-guardrails).

## Edit the rules

To open **Browser Actuation Permissions**:

*   **Antigravity App** (`v2.30.0+`): Go to **Settings** > **Browser**, and in the **Browser Subagent** section, click **Edit** next to **Browser Actuation Rules**.
*   **Antigravity IDE** (`v2.6.0+`): Click **Antigravity** in the status bar and select **Open Settings** > **Browser** (or run **Antigravity: Open Settings** from the Command Palette), and then click **Edit** next to **Browser Actuation Rules**.

![The Browser Actuation Permissions screen in Antigravity App Settings showing Execute URLs and Download files cards with Add buttons](/assets/image/docs/browser/browser-actuation-permissions.png)

You can configure two separate rule lists:

*   **Execute URLs** (`execute_url`): Sites that the browser subagent is allowed, asked about, or denied from opening and interacting with.
*   **Download files** (`download_url`): Sites from which the browser subagent may download files.

Next to **Execute URLs** or **Download files**, click **Add**, choose **Allow**, **Ask**, or **Deny**, and enter a site such as `https://example.com` or `localhost:3000`. To change or delete a rule, click **Edit** or **Remove** next to it.

## How rules match

*   **Domain and subdomains**: A rule matches the domain and its regular subdomains. It doesn’t match paths, so a rule for `example.com` also covers `docs.example.com` and every page on both. Every cross-origin redirect hop is checked before the agent interacts with the destination.
*   **Deny takes precedence**: A **Deny** rule wins over an **Allow** rule for the same site, including under the **Turbo** permission preset.
*   **Per-port `localhost` isolation**: Loopback addresses (`localhost`, `127.0.0.1`, `[::1]`) are matched per port—a rule for `localhost:3000` doesn’t cover `localhost:8080`. Enter `localhost` without a port to match all ports on `localhost`.
*   **Sensitive Google subdomains**: Google properties that hold sensitive account or workspace data—such as `accounts.google.com`, `myaccount.google.com`, `mail.google.com`, `docs.google.com`, `drive.google.com`, `calendar.google.com`, `chat.google.com`, `colab.research.google.com`, and `console.cloud.google.com`—always require their own explicit rule. A rule for `google.com` or `cloud.google.com` doesn’t cover them (and sign-in and payment hosts remain blocked from agent actuation even if added).
*   **Direct URL reads**: These rules apply to the browser subagent. Web pages that the main agent reads directly without opening a browser tab are controlled by **Network Access Rules** (`read_url`) in [Permissions](/docs/permissions).

## Rules set by your organization

If your organization’s administrator sets the domains that the browser subagent can use, the subagent can’t open any other site. The administrator’s domains appear under **Organization Allowed Domains (Read-Only)** in the Browser Actuation Rules, and Antigravity still asks before opening them unless you add an allow rule. If your administrator disables the browser subagent, the **Browser Subagent** section of the settings shows a notice instead of the rules.