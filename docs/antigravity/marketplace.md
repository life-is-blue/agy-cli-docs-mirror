# Marketplace

Available on: Antigravity App, Antigravity CLI, IDE extensions (VS Code, Visual Studio, Eclipse), Antigravity IDE

The Marketplace lets you discover, install, and manage curated Google and partner [plugins](/docs/plugins) that extend your agent with reusable [skills](/docs/skills), [MCP servers](/docs/mcp), [rules](/docs/rules), [lifecycle hooks](/docs/hooks), and [subagents](/docs/subagents). Jump straight to the [plugin catalog](#browse-marketplace-plugins) below to open any plugin directly in the Antigravity App or copy its CLI install command.

Note

**Cross-surface synchronization**: Plugins installed in the **Antigravity App** are automatically updated and displayed in the **Antigravity CLI**’s **Installed** tab.

## Antigravity App

### Browse and install plugins

Open **Customizations > Marketplace** directly in the Antigravity App, or follow the steps below:

[Open Marketplace in Antigravity](antigravity://customizations/marketplaces "Open Customizations > Marketplace in the Antigravity App")[Browse plugin catalog](#browse-marketplace-plugins)

To browse and install Marketplace plugins manually in the Antigravity App:

1.  In the left sidebar, click the **Customizations** tab (below **Automations**):
    
    ![The left sidebar of the Antigravity App with Customizations selected below New Conversation and Automations](/assets/image/docs/plugins/customization-tab.png)
    
2.  Click the **Marketplace** tab to view available plugins:
    
    ![The Marketplace tab of the Customizations page in the Antigravity App, with a search box, the featured Notion plugin with Add and Details buttons, and the Google Workspace plugins](/assets/image/docs/plugins/marketplace-plugins.png)
    
3.  Click any plugin card to inspect its details and bundled capabilities:
    
    ![The Dart and Flutter plugin detail view in the Antigravity App, with an Add button, starter prompts, Overview, Skills, MCP, Agents, and Rules tabs, and the plugin's README](/assets/image/docs/plugins/plugin-card.png)
    
4.  Click **Add** to install the plugin. You can also click **+** next to a plugin in the **Marketplace** list to install it without opening its details.
    

### Configure plugin credentials (API keys and OAuth)

Some plugins connect to external services that require authentication before their MCP tools can run:

*   **API tokens and configuration variables**: If a plugin requires an API key, token, or workspace URL, toggling the plugin on in **Customizations > Installed** opens a setup dialog prompting for each variable (with a direct link to generate or look up your token).
*   **OAuth sign-in**: If a plugin uses OAuth 2.0, Antigravity opens your browser to complete sign-in when the plugin’s MCP server connects.

### Manage installed plugins

To inspect, toggle, or uninstall existing plugins:

1.  In the **Customizations** panel, click the **Installed** tab:
    
    ![The Installed tab of the Customizations page in the Antigravity App, with five installed plugins, two of them marked Sign in required, above the Skills & Rules list](/assets/image/docs/plugins/installed-plugins.png)
    
2.  Click the **⋮** menu beside any installed plugin (or open the plugin card) to enable, disable, or configure it.
    
3.  Select **Uninstall** from the **⋮** menu (or on the plugin detail page) to remove a plugin.
    

Any plugins you install in the Antigravity App automatically sync and appear in the Antigravity CLI’s **Installed** tab.

### Open plugins with deep links

The Antigravity App handles `antigravity://` Marketplace links so you can open the catalog or a specific plugin’s detail page in a single click when signed in:

*   **Marketplace home**: `antigravity://customizations/marketplaces`
*   **Google plugin**: `antigravity://plugin/<plugin-name>` (or `antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/<plugin-name>`)
*   **Partner plugin**: `antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/<plugin-name>` (or `antigravity://plugin/<plugin-name>?marketplace=antigravity-plugins-partners`)

If a link names a plugin ID that isn’t found in the catalog, the Antigravity App opens the **Marketplace** browse tab instead. If you publish plugins and want to embed an **Open in Antigravity** link in your documentation or README, see [Share deep links to your plugin](/docs/build-plugins#share-deep-links-to-your-plugin).

## Antigravity CLI

#### Open the plugin manager in the CLI

In the Antigravity CLI, open the interactive plugin manager using the `/plugin` slash command (or its alias `/plugins`):

```text
/plugin
```

Press Tab to switch between the **Installed** tab and the **Discover** tab.

* * *

#### Discover tab

Use the **Discover** tab to browse the Marketplace catalog and install new plugins:

*   **Search plugins**: Start typing to search and filter for specific plugins.
*   **Install from a local directory**: Highlight **Install from local directory** and press Enter to provide a local filesystem path for plugin installation.
*   **View plugin details**: Highlight a plugin and press Enter to expand its details view. The details view displays the following information:
    *   Description
    *   Included components (MCP servers, skills, rules, agents, and more)
    *   Marketplace name
    *   Version
*   **Install or uninstall**: Press Ctrl + S on an uninstalled plugin to install it, or press Ctrl + S on an installed plugin to uninstall it.

The following example shows the **Discover** tab with the details of a selected plugin expanded:

![The Discover tab of the CLI plugin manager listing Marketplace plugins with their descriptions, the Install from local directory option at the top, and the details of the selected flutter plugin expanded](/assets/image/docs/plugins/plugin-discover-tab.png)

##### After installation

Once a plugin is installed, the interface updates as follows:

*   **Discover tab**: A green dot (`●`) appears beside the plugin name indicating its installed status.
*   **Installed tab**: The plugin name appears in the **Installed** tab list.

#### Installed tab

Use the **Installed** tab to inspect and manage the plugins you have installed:

*   **Search installed plugins**: Start typing to filter your installed plugins.
*   **Enable or disable**: Press Space on an installed plugin to toggle it between enabled and disabled. If the plugin declares required MCP credentials (`variables`), pressing Space opens an interactive prompt to fill in those values before enabling the plugin.
*   **View plugin details**: Press Enter on an installed plugin to expand its details view. The details view displays the following information:
    *   Description
    *   Skills (if applicable)
    *   MCP servers (if applicable)
    *   Rules (if applicable)
    *   Agents (if applicable)
    *   Marketplace name
    *   Local installation path
    *   Version
*   **Uninstall**: Press Ctrl + S on an installed plugin to uninstall it.

##### Keyboard shortcuts

The following keyboard shortcuts are available in the plugin manager:

| Key | Tab | Action |
| --- | --- | --- |
| Tab | Both | Switch between the **Installed** tab and **Discover** tab. |
| Any key | Both | Search and filter plugins in the active tab. |
| Enter | Both | Expand plugin details (or select **Install from local directory** in **Discover**). |
| Ctrl + S | Both | Install an uninstalled plugin, or uninstall an installed plugin. |
| Space | **Installed** | Toggle enable or disable on an installed plugin. |

* * *

#### Inline `/plugin` commands

In addition to the interactive panel, `/plugin` supports inline commands to `install`, `uninstall`, `enable`, `disable`, and `list` plugins directly from the prompt without opening the plugin manager UI:

*   **Install from a Marketplace catalog or local directory**: Specify `<plugin-name>@<marketplace-name>` using `antigravity-plugins-official` for Google plugins or `antigravity-plugins-partners` for partner plugins, or pass a local path:
    
    ```text
    /plugin install firebase@antigravity-plugins-official
    /plugin install stripe@antigravity-plugins-partners
    /plugin install <local-path>
    ```
    
    For example, running `/plugin install firebase@antigravity-plugins-official` outputs:
    
    ```text
    Successfully installed plugin "firebase" from "antigravity-plugins-official".
    ```
    
*   **Manage and list plugins inline**: Run the following commands:
    
    ```text
    /plugin uninstall <plugin-name>
    /plugin enable <plugin-name>
    /plugin disable <plugin-name>
    /plugin list
    ```
    

* * *

### Install from your shell (`agy plugin`)

Outside an interactive TUI session, you can install and manage plugins directly from your shell using `agy plugin`:

*   **Install from the Marketplace**: Once signed in to `agy`, install Google plugins from `antigravity-plugins-official` (or pass a bare `<plugin-name>`, which defaults to `antigravity-plugins-official`) and partner plugins from `antigravity-plugins-partners`:
    
    ```bash
    # Google plugins (bare name defaults to antigravity-plugins-official)
    agy plugin install firebase
    agy plugin install firebase@antigravity-plugins-official
    
    # Partner plugins
    agy plugin install stripe@antigravity-plugins-partners
    ```
    
    Running `agy plugin install firebase` outputs:
    
    ```text
    Installed plugin "firebase" from antigravity-plugins-official
    ```
    
*   **Install from a GitHub link**: Clone and stage a plugin directly from a GitHub repository URL:
    
    ```bash
    agy plugin install https://github.com/<owner>/<repo>
    ```
    
*   **Install from a local directory**: Stage a local plugin folder into your profile:
    
    ```bash
    agy plugin install </path/to/local/plugin>
    ```
    
*   **List installed plugins**: Run `agy plugin list` for a human-readable summary of installed plugins and their component counts, or pass `--json` to output a JSON array with installation paths and component names:
    
    ```bash
    agy plugin list
    agy plugin list --json
    ```
    
*   **Enable, disable, or uninstall plugins**:
    
    ```bash
    agy plugin enable <plugin-name>
    agy plugin disable <plugin-name>
    agy plugin uninstall <plugin-name>
    ```

* * *

## Browse Marketplace plugins

Filter curated Google (`antigravity-plugins-official`) and partner (`antigravity-plugins-partners`) plugins by publisher, shelf, or keyword. Click **Open in Antigravity** on any card to open its detail page in the Antigravity App (if the app isn’t installed yet, the button offers a direct download link), or click **Copy CLI** to copy its `agy plugin install` command.

![](https://www.gstatic.com/images/branding/productlogos/chrome/v7/192px.svg)

### Chrome DevTools

Google

Build with Google

Reliable automation, in-depth debugging, and performance analysis in Chrome using Chrome DevTools and Puppeteer

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/chrome-devtools-plugin "Open Chrome DevTools in the Antigravity App")

[Guide](/docs/build-with-google/#chrome-devtools "View in Build with Google")

![](https://www.gstatic.com/images/branding/productlogos/flutter/v6/192px.svg)

### Dart and Flutter

Google

Build with Google

Official plugin for Dart and Flutter that installs Flutter/Dart Skills, Rules, Custom Agents, and Dart MCP server for building natively compiled, visually stunning applications for mobile, web, des…

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/flutter "Open Dart and Flutter in the Antigravity App")

[Guide](/docs/build-with-google/#dart-and-flutter "View in Build with Google")

![](https://www.gstatic.com/images/branding/productlogos/firebase/v9/192px.svg)

### Firebase

Google

Build with Google

Prototype, build & run modern apps that users love with Firebase's backend, AI, and operational infrastructure.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/firebase "Open Firebase in the Antigravity App")

[Guide](/docs/build-with-google/#firebase-bundle "View in Build with Google")

![](https://www.gstatic.com/images/branding/productlogos/gemini_2026/v1/web-96dp/logo_gemini_2026_color_2x_web_96dp.png)

### Gemini API

Google

Build with Google

Build applications and shell workflows with the Gemini Interactions API, Decisions API, Live API, Genie 4 interactive worlds, and Gemini API CLI, including text, image, video, speech, and music gen…

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gemini-api "Open Gemini API in the Antigravity App")

[Guide](/docs/build-with-google/#gemini-api "View in Build with Google")

![](https://www.gstatic.com/images/branding/productlogos/docs_2026/v2/web/192px.svg)

### Google Docs

Google

Google Workspace

Read, draft, and edit docs.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gdocs "Open Google Docs in the Antigravity App")

![](/assets/image/blog/marketplace-logos/science.svg)

### Science Overview

Google

Science

Antigravity for science highlights, and an overview of the main science plugins.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/science-overview "Open Science Overview in the Antigravity App")

[Guide](/docs/build-with-google/#science "View in Build with Google")

![](https://www.gstatic.com/antigravity/plugins-partners/datadog/assets/logo.png?v=7bf6bcac5c85)

### Datadog

Partner

Developer Tools

Use Datadog directly in Antigravity through a preconfigured Datadog MCP server. Query logs, metrics, traces, dashboards, and more through natural conversation.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/datadog "Open Datadog in the Antigravity App")

[Docs](https://github.com/datadog-labs/antigravity-plugin "Docs / repository")

![](https://www.gstatic.com/antigravity/plugins-partners/figma/Figma_Icon_Full-color_.svg?v=de6902d8745a)

### Figma

Partner

Design, Creative & Media

Turn Figma designs into production code, map components with Code Connect, and create or edit Figma files in Antigravity.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/figma "Open Figma in the Antigravity App")

[Docs](https://github.com/figma/mcp-server-guide "Docs / repository")

![](https://www.gstatic.com/antigravity/plugins-partners/linear/assets/logo.svg?v=c39ac980c40c)

### Linear

Partner

Productivity & Project Management

The product development system for teams and agents. Manage issues, projects, and documents across your Linear workspace from Antigravity.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/linear "Open Linear in the Antigravity App")

[Docs](https://linear.app/docs/mcp "Docs / repository")

![](https://www.gstatic.com/antigravity/plugins-partners/notion/logo.svg?v=76d090749b28)

### Notion

Partner

Productivity & Project Management

Connect Antigravity to your Notion workspace with the Notion MCP server, plus skills for research, documentation, meeting prep, specs, trackers, and project updates.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/notion "Open Notion in the Antigravity App")

[Docs](https://developers.notion.com/docs/notion-mcp "Docs / repository")

![](https://www.gstatic.com/antigravity/plugins-partners/stripe/assets/logo.svg?v=e0002d0b4bd9)

### Stripe

Partner

Business

Accept payments and grow your business.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/stripe "Open Stripe in the Antigravity App")

[Docs](https://docs.stripe.com/mcp "Docs / repository")

![](/assets/image/blog/marketplace-logos/vercel.svg)

### Vercel

Partner

Cloud Hosting & Deployment

Build and deploy web apps and AI agents on Vercel with skills for Next.js, AI SDK, and cloud services, plus the official Vercel MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/vercel-plugin "Open Vercel in the Antigravity App")

[Docs](https://github.com/vercel/vercel-plugin#readme "Docs / repository")

### Android CLI

Google

Build with Google

Core tools and knowledge required to develop for Android.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/android-cli-plugin "Open Android CLI in the Antigravity App")

[Guide](/docs/build-with-google/#android-cli "View in Build with Google")

### Chemistry

Google

Science

RDKit cheminformatics, reaction and property tools, plus ChEMBL and PubChem, to work with molecules, their properties, and bioactivity data.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/chemistry "Open Chemistry in the Antigravity App")

[Guide](/docs/build-with-google/#science "View in Build with Google")

### Data Agent Kit

Google

Build with Google

This plugin provides a specialized suite of skills for data engineers and database practitioners working on Google Cloud.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/data-agent-kit-plugin "Open Data Agent Kit in the Antigravity App")

[Guide](/docs/build-with-google/#data-agent-kit-starter-pack "View in Build with Google")

### Elephant-Goldfish Model

Google

Build with Google

Develop ideas with context and review documents with fresh eyes.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/egm "Open Elephant-Goldfish Model in the Antigravity App")

[Docs](https://egm.dev/ "Docs / repository")

### Genomics

Google

Science

AlphaGenome and major genetics databases to analyze DNA variants, gene regulation, and links between genes and disease.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/genomics "Open Genomics in the Antigravity App")

[Guide](/docs/build-with-google/#science "View in Build with Google")

### Gmail

Google

Google Workspace

Search, read, draft, and send emails in Gmail.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gmail "Open Gmail in the Antigravity App")

### Google Antigravity SDK

Google

Build with Google

Using the Google Antigravity Python SDK to build AI agents

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-antigravity-sdk "Open Google Antigravity SDK in the Antigravity App")

[Guide](/docs/build-with-google/#google-antigravity-sdk "View in Build with Google")

### Google Calendar

Google

Google Workspace

Check availability, schedule events, and RSVP.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gcalendar "Open Google Calendar in the Antigravity App")

### Google Cloud Developer

Google

Build with Google

Google Cloud guidance for coding agents: first-project onboarding, authentication and credential selection, and safety-critical validation for gcloud CLI commands.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-cloud-developer "Open Google Cloud Developer in the Antigravity App")

[Guide](/docs/build-with-google/#google-cloud "View in Build with Google")

### Google Developer Knowledge

Google

Build with Google

Search and retrieve official documentation across Google Cloud, Gemini, Android, Firebase, Flutter, and Web. Requires Google Cloud credentials (ADC) or an API key.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-developer-knowledge "Open Google Developer Knowledge in the Antigravity App")

[Guide](/docs/build-with-google/#google-developer-knowledge "View in Build with Google")

### Google Drive

Google

Google Workspace

Search, upload, download, and share files.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gdrive "Open Google Drive in the Antigravity App")

### Google Health Developer

Google

Build with Google

Search and retrieve official Google Health API documentation on developers.google.com/health through the Google Health Developer MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-health-developer "Open Google Health Developer in the Antigravity App")

[Guide](/docs/build-with-google/#google-health-developer "View in Build with Google")

### Google Home Developer

Google

Build with Google

Search official Google Home, Matter, and OpenThread documentation and query Cloud-to-cloud user feedback integration diagnostics through the Google Home Developer MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-home-developer "Open Google Home Developer in the Antigravity App")

[Guide](/docs/build-with-google/#google-home-developer "View in Build with Google")

### Google Maps Platform

Google

Build with Google

Integration skill and tools for Google Maps Platform APIs

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google_maps_platform "Open Google Maps Platform in the Antigravity App")

[Guide](/docs/build-with-google/#google-maps-platform "View in Build with Google")

### Google Sheets

Google

Google Workspace

Read, write, and format spreadsheets.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gsheets "Open Google Sheets in the Antigravity App")

### Google Slides

Google

Google Workspace

Read, edit, and export presentations.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gslides "Open Google Slides in the Antigravity App")

### Looker

Google

Build with Google

Connect to your managed Looker MCP server to explore data, run saved Looks, build dashboards, and validate LookML.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/looker "Open Looker in the Antigravity App")

[Guide](/docs/build-with-google/#looker "View in Build with Google")

### Modern Web Guidance

Google

Build with Google

Keep your coding agent up to date with the latest web best practices.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/modern-web-guidance-plugin "Open Modern Web Guidance in the Antigravity App")

[Guide](/docs/build-with-google/#modern-web-guidance "View in Build with Google")

### Robotics

Google

Build with Google

Robotics skills for any robot: 3D perception, collision-free motion planning, visual servoing, robot bring-up, sim2real, agent iteration, MuJoCo simulation, SimReady 3D asset authoring and physics…

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/robotics "Open Robotics in the Antigravity App")

[Guide](/docs/build-with-google/#robotics "View in Build with Google")

### Scientific Literature

Google

Science

Search scientific papers, clinical trials, FDA records, and historical texts.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/scientific-literature "Open Scientific Literature in the Antigravity App")

[Guide](/docs/build-with-google/#science "View in Build with Google")

### Structural Biology

Google

Science

AlphaFold, 3D visualization tools, and protein databases to explore protein structures, sequences, pathways, and drug interactions.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/structural-biology "Open Structural Biology in the Antigravity App")

[Guide](/docs/build-with-google/#science "View in Build with Google")

### Adspirer Marketing Analytics

Partner

Business

Read-only marketing analytics: report spend, conversions, CPA and ROAS across ad platforms, GA4 and Search Console. It never changes your accounts.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/adspirer-analytics "Open Adspirer Marketing Analytics in the Antigravity App")

[Docs](https://www.adspirer.com/ "Docs / repository")

### Arize AX

Partner

Developer Tools

Query Arize AX projects, traces, datasets, and experiments from Antigravity, with skills for tracing, evals, and prompt optimization.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/arize-skills "Open Arize AX in the Antigravity App")

[Docs](https://arize.com/docs/api-clients/mcp/overview "Docs / repository")

### Atlassian Teamwork Graph CLI

Partner

Productivity & Project Management

Teamwork Graph CLI is Atlassian's agent-first interface to your entire work context: Jira issues, Confluence pages, Bitbucket PRs, along with your connected third-party data sources.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/atlassian-twg-cli "Open Atlassian Teamwork Graph CLI in the Antigravity App")

[Docs](https://developer.atlassian.com/cloud/twg-cli/ "Docs / repository")

### Auth0

Partner

Developer Tools

Add Auth0 authentication to any app: login, MFA, SSO, Organizations, RBAC, custom domains, and branding. Debug auth errors and migrate from other providers.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/auth0 "Open Auth0 in the Antigravity App")

[Docs](https://auth0.com/docs/quickstart/agent-skills "Docs / repository")

### Base44

Partner

Developer Tools

Build and deploy Base44 full-stack apps: CLI project management, JavaScript/TypeScript SDK development, and production troubleshooting skills.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/base44 "Open Base44 in the Antigravity App")

[Docs](https://docs.base44.com/ "Docs / repository")

### Better Stack

Partner

Developer Tools

Investigate incidents, check who's on call, and query logs, metrics, traces, errors and RUM in Better Stack. Build dashboards and manage uptime monitors.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/betterstack "Open Better Stack in the Antigravity App")

[Docs](https://betterstack.com/docs/getting-started/integrations/mcp/ "Docs / repository")

### Bigin

Partner

Business

Manage your Bigin CRM from Antigravity: review pipelines, find contacts and deals, log calls, plan follow-ups, and email customers.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/zoho-bigin "Open Bigin in the Antigravity App")

[Docs](https://www.bigin.com/developer/docs/apis/v2/ "Docs / repository")

### Browserbase

Partner

Developer Tools

Give your agent a real browser: navigate, click, type, screenshot, and extract data from any site, locally or on Browserbase cloud browsers.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/browse "Open Browserbase in the Antigravity App")

[Docs](https://docs.browserbase.com/ "Docs / repository")

### Canva

Partner

Design, Creative & Media

Create, edit, review, resize, and brand-check Canva designs with the Canva MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/canva "Open Canva in the Antigravity App")

[Docs](https://www.canva.com/developers/ "Docs / repository")

### Clerk

Partner

Business

Add authentication and user management with Clerk. Skills for setup, frameworks, organizations, billing, webhooks, and testing, plus the Clerk MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/clerk "Open Clerk in the Antigravity App")

[Docs](https://clerk.com/docs "Docs / repository")

### ClickUp

Partner

Productivity & Project Management

Connect Antigravity to your ClickUp workspace — manage tasks, track time, and collaborate with your team without switching context.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/clickup "Open ClickUp in the Antigravity App")

[Docs](https://clickup.com/ "Docs / repository")

### Cloudflare

Partner

Cloud Hosting & Deployment

Build, deploy and manage apps on Cloudflare Workers, storage and AI, with platform skills and the Cloudflare API through one MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/cloudflare "Open Cloudflare in the Antigravity App")

[Docs](https://developers.cloudflare.com/ "Docs / repository")

### Cobrief

Partner

Developer Tools

Search European procurement data and manage your tender pipeline.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/cobrief "Open Cobrief in the Antigravity App")

[Docs](https://cobrief.com/en/ "Docs / repository")

### CodeRabbit

Partner

Developer Tools

CodeRabbit is the governance and control layer for agentic software development helping developers trust AI written code.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/coderabbit "Open CodeRabbit in the Antigravity App")

[Docs](https://docs.coderabbit.ai/cli/antigravity "Docs / repository")

### Context7

Partner

Developer Tools

Up-to-date documentation lookup. Pull version-specific documentation and code examples directly from source repositories into your coding agent's context.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/context7 "Open Context7 in the Antigravity App")

[Docs](https://context7.com/ "Docs / repository")

### CrowdStrike Falcon

Partner

Developer Tools

Use the official CrowdStrike-hosted MCP server to work across Falcon: detections, cases, threat intel, SIEM, hosts, vulnerabilities, cloud, and more.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/crowdstrike "Open CrowdStrike Falcon in the Antigravity App")

[Docs](https://developer.crowdstrike.com/falcon-mcp/overview/ "Docs / repository")

### Databricks

Partner

Business

Databricks skills for the CLI, Apps, Lakebase, Model Serving, Lakeflow Jobs, Spark Declarative Pipelines, Declarative Automation Bundles (DABs), and classic-to-serverless migration.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/databricks "Open Databricks in the Antigravity App")

[Docs](https://github.com/databricks/databricks-agent-skills "Docs / repository")

### Descrybe Legal Engine

Partner

Developer Tools

Research U.S. case law, statutes, regulations, and court rules. Find authorities, check quotations against opinions, and see how later courts cite a case.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/descrybe-legal-engine "Open Descrybe Legal Engine in the Antigravity App")

[Docs](https://descrybe.com/user-guide/open-connector "Docs / repository")

### Docusign

Partner

Productivity & Project Management

Build, test, and debug Docusign integrations with developer skills for authentication, template-based signing, envelope status, and troubleshooting.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/docusign "Open Docusign in the Antigravity App")

[Docs](https://developers.docusign.com/ "Docs / repository")

### Dropbox

Partner

Productivity & Project Management

Connect Antigravity to Dropbox to search, inspect, summarize, share, collect uploads, organize folders, and clean up files with confirmation for write actions.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/dropbox "Open Dropbox in the Antigravity App")

[Docs](https://www.dropbox.com/ "Docs / repository")

### Dynatrace

Partner

Developer Tools

Investigate production issues with real Dynatrace data: problems and root causes, logs, metrics, traces, and vulnerabilities, via skills and the MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/dynatrace "Open Dynatrace in the Antigravity App")

[Docs](https://www.dynatrace.com/ "Docs / repository")

### Endor Labs Agent Kit

Partner

Developer Tools

Packaged workflows for SCA remediation, AI SAST triage, CI/CD posture, malware response, findings review, Endor Labs setup, and more.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/endor-labs-agent-kit "Open Endor Labs Agent Kit in the Antigravity App")

[Docs](https://github.com/endorlabs/ai-plugins "Docs / repository")

### Exabeam Agentic SOC

Partner

Developer Tools

Triage Exabeam New-Scale alerts and cases end to end: gather the evidence, map MITRE, reach a verdict, and record it behind an approval step.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/soc "Open Exabeam Agentic SOC in the Antigravity App")

### Grafana Cloud

Partner

Developer Tools

Query Grafana Cloud metrics, logs, traces and profiles, manage dashboards, alerts and incidents, and ask Grafana Assistant through the hosted MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/grafana-cloud-mcp "Open Grafana Cloud in the Antigravity App")

[Docs](https://github.com/grafana/ai-marketplace/tree/main/plugins/grafana-cloud-mcp "Docs / repository")

### Granola

Partner

Productivity & Project Management

The AI notepad for meetings. Connect to your meeting history and use your conversation context to get things done.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/granola "Open Granola in the Antigravity App")

[Docs](https://granola.ai/ "Docs / repository")

### Harness

Partner

Developer Tools

Build and debug pipelines, manage deployments, investigate security findings, and operate Harness with connected tools and reusable workflow skills.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/harness-antigravity "Open Harness in the Antigravity App")

[Docs](https://developer.harness.io/ "Docs / repository")

### incident.io

Partner

Developer Tools

Respond to and investigate incidents, manage on-call schedules and escalations, and write runbooks and skills. Bundles the official incident.io MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/incident-io "Open incident.io in the Antigravity App")

[Docs](https://incident.io/ "Docs / repository")

### Intercom

Partner

Business

Search Intercom conversations, contacts, and companies, spot support trends, and install the Intercom Messenger with secure identity verification.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/intercom "Open Intercom in the Antigravity App")

[Docs](https://developers.intercom.com/ "Docs / repository")

### invideo

Partner

Design, Creative & Media

Connect your agent to invideo's AI-native video editor. It trims, grades and mixes on a real timeline while you watch every change land.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/invideo "Open invideo in the Antigravity App")

[Docs](https://docs.invideo.io/start/antigravity "Docs / repository")

### Keenable

Partner

Developer Tools

Search the web and read any page as clean markdown with Keenable, a search engine built for AI agents. Keyless: no signup or API key needed.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/keenable "Open Keenable in the Antigravity App")

[Docs](https://keenable.ai/ "Docs / repository")

### Keenable SELECT

Partner

Developer Tools

Ask a question of the live web and get a table back. Keenable SELECT runs many searches, reads the pages and extracts the fields you need in one call. Sign in with a Keenable account.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/keenable-select "Open Keenable SELECT in the Antigravity App")

[Docs](https://docs.keenable.ai/select "Docs / repository")

### Kling AI

Partner

Design, Creative & Media

Generate images and V4 videos with Kling AI. Supports multimodal references, reusable subjects, motion control, and task tracking through secure OAuth.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/kling-ai "Open Kling AI in the Antigravity App")

[Docs](https://kling.ai/ "Docs / repository")

### Leapwork Play

Partner

Developer Tools

Create, run and debug Leapwork Play tests and runlists, build agents, and hand work to Play's AI workflows, right from Antigravity.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/leapwork-play "Open Leapwork Play in the Antigravity App")

[Docs](https://leapwork.ai/ "Docs / repository")

### Levels.fyi

Partner

Business

Salaries, jobs & career advice. Levels.fyi is your career companion to ensure you get paid fairly and find jobs you'll love.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/levels-fyi "Open Levels.fyi in the Antigravity App")

[Docs](https://www.levels.fyi/?from=antigravity_plugin "Docs / repository")

### Meshy

Partner

Developer Tools

Generate 3D models from text or images with Meshy, then texture them and download game-ready GLB, FBX, OBJ and USDZ files, using your Meshy credits.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/meshy "Open Meshy in the Antigravity App")

[Docs](https://docs.meshy.ai/en/api/ai "Docs / repository")

### Midpage Legal Research

Partner

Business

Research US case law, statutes, and regulations, plus live dockets from federal and state courts. A Midpage account is required.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/midpage "Open Midpage Legal Research in the Antigravity App")

[Docs](https://www.midpage.ai/ "Docs / repository")

### Mobbin

Partner

Design, Creative & Media

Give your AI agent 600,000+ real app screens, and the skills to use them.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/mobbin "Open Mobbin in the Antigravity App")

[Docs](https://mobbin.com/mcp "Docs / repository")

### monday.com

Partner

Productivity & Project Management

Plan and track work in monday.com from Antigravity: create, update and assign items, write docs, and build forms that turn requests into items.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/monday "Open monday.com in the Antigravity App")

[Docs](https://monday.com/w/mcp "Docs / repository")

### MongoDB Atlas (Managed MCP)

Partner

Developer Tools

Official Antigravity plugin for MongoDB Atlas (hosted MCP Server + Skills).

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/mongodb-atlas "Open MongoDB Atlas (Managed MCP) in the Antigravity App")

### mumo

Partner

Design, Creative & Media

Multi-model deliberation panel. Diverse AI voices + claim-level reactions on contested decisions.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/mumo "Open mumo in the Antigravity App")

[Docs](https://mumo.chat/install/antigravity "Docs / repository")

### n8n

Partner

Developer Tools

Build, test, and manage n8n workflows and Agents through your instance MCP server. Use official skills for node setup, credentials, and debugging.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/n8n-skills "Open n8n in the Antigravity App")

[Docs](https://github.com/n8n-io/skills "Docs / repository")

### Neo4j

Partner

Developer Tools

Agent skills for Neo4j graph database — write Cypher queries, design graph models, use drivers, run imports, build GraphRAG pipelines, run GDS algorithms, and manage Aura instances.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/neo4j "Open Neo4j in the Antigravity App")

[Docs](https://neo4j.com/ "Docs / repository")

### Netlify

Partner

Cloud Hosting & Deployment

Build and deploy on Netlify: functions, edge functions, blobs, database, identity, forms, image CDN, caching, and AI Gateway, plus the Netlify MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/netlify "Open Netlify in the Antigravity App")

[Docs](https://docs.netlify.com/ "Docs / repository")

### Orca Security

Partner

Developer Tools

Investigate cloud risk from your IDE: query Orca alerts, assets, attack paths, CVEs and compliance posture, and triage findings with Orca's MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/orca-security "Open Orca Security in the Antigravity App")

[Docs](https://orca.security/mcp-server/ "Docs / repository")

### PandaDoc

Partner

Productivity & Project Management

Create and send proposals, quotes, and contracts for e-signature. Track signing progress and identify documents that need follow-up.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/pandadoc "Open PandaDoc in the Antigravity App")

[Docs](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server "Docs / repository")

### Parallel

Partner

Developer Tools

Search the live web and fetch page content with Parallel's hosted MCP server. Free access with no Parallel account, API key, or Parallel CLI required.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/parallel "Open Parallel in the Antigravity App")

[Docs](https://docs.parallel.ai/search/search-mcp "Docs / repository")

### Passim AI

Partner

Business

U.S. immigration law research: published and unpublished BIA/AAO and federal cases, INA/CFR, USCIS policy, citator validity checks, and visa bulletins.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/passim "Open Passim AI in the Antigravity App")

[Docs](https://passimai.com/ "Docs / repository")

### PingOne

Partner

Developer Tools

Agent plugin for PingOne multi-tenant. Includes skills and a remote MCP server that lets AI agents configure and monitor your PingOne environments.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/ping-identity-pingone "Open PingOne in the Antigravity App")

[Docs](https://developer.pingidentity.com/ "Docs / repository")

### Postman

Partner

Developer Tools

Equip Antigravity with specialized Postman skills for the complete API lifecycle. Discover, design, test, document, mock, monitor, and improve APIs through agent-friendly, filesystem-first workflows.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/postman "Open Postman in the Antigravity App")

[Docs](https://github.com/postmanlabs/postman-plugin "Docs / repository")

### Qodo

Partner

Developer Tools

Set up Qodo, explore code and repository history, review local changes, and resolve pull-request findings directly from Antigravity.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/qodo "Open Qodo in the Antigravity App")

[Docs](https://www.qodo.ai/ "Docs / repository")

### Railway

Partner

Cloud Hosting & Deployment

Deploy, configure, monitor, and troubleshoot apps, databases, and infrastructure on Railway from Antigravity with Railway's agent skill and hosted MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/railway "Open Railway in the Antigravity App")

[Docs](https://docs.railway.com/agents "Docs / repository")

### Scandit SDK

Partner

Developer Tools

Skills for integrating the Scandit Data Capture SDK: product selection, docs and implementation guides for barcode scanning, ID capture and smart label capture.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/scandit-sdk "Open Scandit SDK in the Antigravity App")

[Docs](https://docs.scandit.com/ "Docs / repository")

### Scriptivox

Partner

Developer Tools

Transcribe meetings, interviews, podcasts and videos in 119 languages, then write minutes, show notes and subtitles from the transcripts.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/scriptivox "Open Scriptivox in the Antigravity App")

[Docs](https://www.scriptivox.com/docs/mcp "Docs / repository")

### Semrush

Partner

Business

SEO workflows on live Semrush data: keyword research, site audits, backlinks, competitor, traffic and market analytics, PPC, and AI brand visibility.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/semrush "Open Semrush in the Antigravity App")

[Docs](https://developer.semrush.com/api/v4/introduction/semrush-mcp/ "Docs / repository")

### SentinelOne Purple AI

Partner

Developer Tools

Query your SentinelOne Singularity Console from Antigravity through a self-hosted, read-only Purple AI MCP server. Requires an active console deployment, your console URL, and an API token.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/sentinelone-purple-mcp "Open SentinelOne Purple AI in the Antigravity App")

[Docs](https://github.com/Sentinel-One/purple-mcp "Docs / repository")

### Sentry

Partner

Developer Tools

Set up Sentry monitoring, investigate production errors, and configure alerts and releases with expert skills and live context from your Sentry projects.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/sentry "Open Sentry in the Antigravity App")

[Docs](https://sentry.io/ "Docs / repository")

### SonarQube

Partner

Developer Tools

SonarQube is the AI code quality and security verification platform used by millions of developers to catch bugs, vulnerabilities, and leaked secrets.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/sonarqube "Open SonarQube in the Antigravity App")

[Docs](https://www.sonarsource.com/ "Docs / repository")

### Spacefast

Partner

Cloud Hosting & Deployment

Turn an idea into a website, dashboard, report, or small web tool you can share. Build it in chat or bring your own work, and publish it with Spacefast.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/spacefast "Open Spacefast in the Antigravity App")

[Docs](https://spacefast.com/ "Docs / repository")

### Supabase

Partner

Developer Tools

Official Supabase plugin for Antigravity with Supabase skills and MCP access for project management, database work, auth, storage, and Postgres best practices.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/supabase "Open Supabase in the Antigravity App")

[Docs](https://supabase.com/ "Docs / repository")

### Superpowers

Partner

Developer Tools

Make your coding agent a better engineer

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/superpowers "Open Superpowers in the Antigravity App")

[Docs](https://github.com/obra/superpowers "Docs / repository")

### Tavily

Partner

Developer Tools

Web search, content extraction, website crawling, URL discovery, and deep research for Antigravity via Tavily's hosted MCP server and skills.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/tavily "Open Tavily in the Antigravity App")

[Docs](https://docs.tavily.com/ "Docs / repository")

### TestMu AI

Partner

Developer Tools

Run, debug and triage tests on the TestMu AI cloud, plus Kane CLI for browser and mobile test automation and Rook CLI for testing AI agents.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/testmu-ai "Open TestMu AI in the Antigravity App")

[Docs](https://www.testmuai.com/mcp/ "Docs / repository")

### Trello

Partner

Productivity & Project Management

Official Trello plugin with the Trello MCP server and a skill for boards, lists, cards, checklists, Inbox, and Planner.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/trello "Open Trello in the Antigravity App")

[Docs](https://trello.com/mcp "Docs / repository")

### Unity

Partner

Developer Tools

Unity's official plugin for Antigravity, with curated skills for game development, monetization, and performance optimization.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/unity "Open Unity in the Antigravity App")

[Docs](https://unity.com/ "Docs / repository")

### VirusTotal

Partner

Developer Tools

Investigate files, URLs, domains and IP addresses with VirusTotal threat intelligence, analysis and submission recovery.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/virustotal "Open VirusTotal in the Antigravity App")

### Why Won't AI

Partner

Business

See what GPTBot, ClaudeBot, PerplexityBot and other AI crawlers get from a website. Skills and a remote MCP server for robots.txt checks, AI visibility scans and agent directory listings.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/whywontai "Open Why Won't AI in the Antigravity App")

[Docs](https://whywontai.com/mcp-server "Docs / repository")

### Wispr Flow

Partner

Business

Search and read your Wispr Flow meeting notes, transcripts, scratchpad notes, and calendar events. Read-only access to your own account.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/wispr-flow "Open Wispr Flow in the Antigravity App")

[Docs](https://wisprflow.ai/ "Docs / repository")

### Wix

Partner

Cloud Hosting & Deployment

Build Wix apps and headless sites, and manage Wix stores, bookings, CMS and more, with Wix CLI skills and the official Wix MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/wix "Open Wix in the Antigravity App")

[Docs](https://dev.wix.com/docs/api-reference/articles/ai-tools/about-wix-skills "Docs / repository")

### WordPress

Partner

Cloud Hosting & Deployment

Build, publish, and manage WordPress.com and Jetpack-connected sites. Draft posts, edit blocks, check traffic stats, moderate comments, and manage plugins.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/wordpress "Open WordPress in the Antigravity App")

[Docs](https://wordpress.com/ "Docs / repository")

### Zapier

Partner

Business

Automate workflows across 10,000+ apps. Run one-off actions or build automations for YouTube, Instagram, Gmail, Facebook Pages, LinkedIn, Slack, Pinterest.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/zapier "Open Zapier in the Antigravity App")

[Docs](https://docs.zapier.com/mcp/home "Docs / repository")

### Zoho Books

Partner

Business

Run Zoho Books from Antigravity: invoicing, bills, banking, journals, projects, items, taxes, customization and automation.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/zohobooks-antigravity "Open Zoho Books in the Antigravity App")

[Docs](https://www.zoho.com/books/ "Docs / repository")

### Zoho CRM

Partner

Business

Build on Zoho CRM v8: REST API, Deluge functions, ClientScript, widgets, COQL and connections, with live CRM data through your Zoho MCP server.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/zoho-crm-plugin "Open Zoho CRM in the Antigravity App")

[Docs](https://github.com/zoho/crm-skills "Docs / repository")

### Zoho Desk

Partner

Business

Zoho Desk plugin for Antigravity.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/zoho-desk-antigravity "Open Zoho Desk in the Antigravity App")

[Docs](https://www.zoho.com/desk/ "Docs / repository")

### Zoho Projects

Partner

Business

Connect Zoho Projects to Antigravity to turn tasks and issues into working code. Access project context, investigate bugs, and update work items as you develop.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-partners/plugins/zoho-projects "Open Zoho Projects in the Antigravity App")

[Docs](https://www.zoho.com/projects/ "Docs / repository")

* * *

## Using installed plugins

Once a plugin is installed and enabled, its bundled capabilities are available in your workspace automatically:

| Component | How to use it in your workflow |
| --- | --- |
| **Starter prompts** | In the Antigravity App (**Customizations > Installed**), open a plugin’s detail view and click any **suggested prompt chip** to start a guided task immediately. |
| **[Skills](/docs/skills)** | Ask for a task in natural language—Antigravity loads relevant plugin skills on demand using progressive disclosure—or invoke a skill explicitly in chat with `/<skill-name>`. |
| **[MCP servers](/docs/mcp)** | Ask the agent to query or act on the connected service (such as Jira, Figma, Datadog, Stripe, or Firebase). Bundled MCP tools (namespaced as `<plugin-name>_<server-name>`) are available automatically while the plugin is enabled. |
| **[Custom agents & subagents](/docs/subagents)** | The main agent delegates specialized tasks (such as security reviews or accessibility audits) to bundled subagents automatically. You can also run a plugin’s custom agent directly as your primary session agent via the agent selector in the App, `/agents` in the CLI, or `agy --agent <agent-name>` from your terminal (run `agy agents` to list all available agents). |
| **[Rules](/docs/rules) & [Hooks](/docs/hooks)** | Run automatically in the background while the plugin is enabled—enforcing coding conventions, SDK standards, and pre- or post-tool policy checks without manual invocation. |

* * *

## Next steps

Explore related documentation and guides:

*   **[Plugins](/docs/plugins)**: Learn how to configure, use, and manage installed plugins across the Antigravity App, Antigravity CLI, and Antigravity IDE.
*   **[Build plugins](/docs/build-plugins)**: Author `plugin.json` manifests, bundle skills, MCP servers, custom agents, rules, and hooks, and validate your plugin locally with `agy plugin validate`.
*   **[Get your plugin in the marketplace](https://forms.gle/2EX5RFYPoJe1UgxR9)**: Fill out this interest form to submit your validated plugin to the Antigravity Marketplace.
*   **[Build with Google](/docs/build-with-google)**: Explore curated Google plugins for Firebase, Android, Flutter, Chrome DevTools, BigQuery, and more.
*   **[CLI reference](/docs/cli/reference)**: View all slash commands and keyboard shortcuts in the Antigravity CLI.