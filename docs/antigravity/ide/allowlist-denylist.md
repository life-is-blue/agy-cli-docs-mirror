# Allowlist and denylist

Available on: Antigravity App, Antigravity IDE

Antigravity asks you before the browser subagent opens a site that you haven’t allowed. To decide ahead of time, add sites to the **Browser Actuation Rules**: allow the sites that the subagent can open without asking, and deny the ones that it must never open.

## When the subagent opens a new site

When the subagent tries to open a page on a site that has no rule, Antigravity asks you to choose one of the following:

| Option | What it does |
| :-- | :-- |
| **Yes, allow this time** | Allows the site for the rest of the subagent’s current task. |
| **Yes, allow** _domain_ **in this conversation** | Allows the site until the conversation ends. |
| **Yes, always allow** _domain_ | Adds an allow rule for the site to your Browser Actuation Rules. |
| **No** | Denies the request. You can tell the agent what to do instead. |

## Edit the rules

To open the rules:

*   **Antigravity App**: Go to **Settings** > **General**, and in the **Browser Subagent** section, click **Edit** next to **Browser Actuation Rules**.
*   **Antigravity IDE**: Click **Antigravity - Settings** in the status bar, select **Browser**, and then click **Edit** next to **Browser Actuation Rules**.

Next to **Execute URLs**, click **Add**, choose **Allow**, **Ask**, or **Deny**, and enter a site, such as `https://example.com`. To change or delete a rule, click **Edit** or **Remove** next to it.

## How rules match

*   A rule matches the domain and all its subdomains. It doesn’t match paths, so a rule for `example.com` also covers `docs.example.com` and every page on both.
*   A deny rule wins over an allow rule for the same site.
*   Some Google sites that hold your data, such as `accounts.google.com`, `mail.google.com`, `docs.google.com`, and `drive.google.com`, need their own rule. A rule for `google.com` doesn’t cover them.
*   These rules apply to the browser subagent. Web pages that the agent reads without the browser are controlled by **Network Access Rules** in [Permissions](/docs/permissions).

## Rules set by your organization

If your organization’s administrator sets the domains that the browser subagent can use, the subagent can’t open any other site. The administrator’s domains appear under **Organization Allowed Domains (Read-Only)** in the Browser Actuation Rules, and Antigravity still asks before opening them unless you add an allow rule. If your administrator disables the browser subagent, the **Browser Subagent** section of the settings shows a notice instead of the rules.