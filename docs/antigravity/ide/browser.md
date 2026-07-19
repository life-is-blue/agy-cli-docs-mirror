---
slug: ide/browser
section: Antigravity IDE
title: Overview
path:
  - Antigravity IDE
  - Browser
  - Overview
---

# Browser Overview

Google Antigravity can open, read, and actuate a local Chrome browser, enabling you to test development websites, read documentation sources, and automate a variety of browser tasks.

---

## Core Mechanisms

Using the specialized [Browser Subagent](/docs/subagents), Antigravity operates on browser tabs as needed, capturing screenshots and saving action videos as interactive artifacts.

To completely disable browser tools, you can toggle the **Browser Tools** setting in the "Browser" section of the User Settings.

---

## Deep Dive

Explore the key security and privacy features of Antigravity's browser integration:

<IconCardGroup>
- link: /docs/ide/allowlist-denylist
  icon: security
  title: Allowlist & Denylist
  description: Learn about the two-layer security model (Denylist and Allowlist) used to control URL access.
- link: /docs/ide/separate-chrome-profile
  icon: account_box
  title: Isolated Profile
  description: Understand how the agent executes inside a completely separate Chrome profile to protect your personal data.
</IconCardGroup>
