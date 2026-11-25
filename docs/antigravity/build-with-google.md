# Build with Google

The Antigravity App and Antigravity CLI make it straightforward to build with popular Google technology stacks. We’ve partnered with teams across Google to create curated plugins bundling skills, MCP servers, rules, and custom agents pre-configured for specific ecosystems.

Instead of searching for individual tools, you can open any plugin below directly in the Antigravity App or install it in one command from your terminal.

## How to enable

You can install and manage Build with Google plugins from the [Marketplace](/docs/marketplace) across the Antigravity App and Antigravity CLI:

*   **Direct deep link**: Click **Open in Antigravity** on any bundle card below to jump straight to its detail page in the Antigravity App, or click the companion CLI button to copy its `agy plugin install` command.
*   **Browse and install**: Click **Customizations** in the left sidebar, open the **Marketplace** tab, and browse the **Build with Google** shelf (or run `/plugin` in the Antigravity CLI).
*   **Manage installed plugins**: Open **Customizations** > **Installed** to enable, disable, configure, or uninstall plugins at any time.

[Open Marketplace in Antigravity](antigravity://customizations/marketplaces "Open Customizations > Marketplace in the Antigravity App")[Browse all Google plugins](/docs/marketplace/?source=google#browse-marketplace-plugins)

* * *

## Available bundles

The following official Google plugins are published in the Antigravity Marketplace (`antigravity-plugins-official`) for the Antigravity App and Antigravity CLI:

![](https://www.gstatic.com/images/branding/productlogos/firebase/v9/192px.svg)

Cloud & Data

### Firebase Bundle

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/firebase "Open Firebase Bundle in the Antigravity App")

Transform your AI coding agent into a specialized Firebase expert that can write code, configure Firebase Security Rules, and manage live resources.

#### What's included

*   Agent skills, custom security rules agent, and MCP integration for Firestore, Authentication, App Hosting, and Firebase AI Logic.

#### Key capabilities

*   **Take action:** Initialize services, manage Authentication users, deploy and audit Firebase Security Rules, and work directly with Cloud Firestore data.
*   **Stay up to date:** Use official, version-aware guidance to walk your agent through Firebase setup, AI Logic integration, and App Hosting deployment.
*   **Improve accuracy:** Access your project's environment and schemas to generate grounded configurations and rules.

Example prompt: “Write and audit Firestore security rules for my data model”

[Firebase Agent Skills Guide](https://firebase.google.com/docs/ai-assistance/agent-skills)

![](https://www.gstatic.com/images/branding/productlogos/gemini_2026/v1/web-96dp/logo_gemini_2026_color_2x_web_96dp.png)

AI & Science

### Gemini API

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gemini-api "Open Gemini API in the Antigravity App")

Build applications and shell workflows with the Gemini Interactions API, Live API, and official Google GenAI SDKs across text, image, video, and real-time audio.

#### What's included

*   Official Gemini API agent skills covering current model IDs, Interactions API, Live API multimodal streaming, and structured tool calling.

#### Key capabilities

*   **Current SDK patterns:** Write idiomatic Google GenAI SDK code with structured outputs, function calling, and stateful multi-turn interactions.
*   **Real-time multimodal workflows:** Build low-latency voice and video agents using the Gemini Live API and non-blocking tool execution.

Example prompt: “Create a real-time voice agent using the Gemini Live API and non-blocking function calling”

[Gemini API Documentation](https://aistudio.google.com/docs)

![](https://www.gstatic.com/images/branding/productlogos/chrome/v7/192px.svg)

Web & Chrome

### Chrome DevTools

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/chrome-devtools-plugin "Open Chrome DevTools in the Antigravity App")

Reliable automation, in-depth debugging, and performance analysis in Chrome using Chrome DevTools and Puppeteer.

#### What's included

*   Chrome DevTools MCP server and agent skills for live browser inspection, network tracing, and Puppeteer automation.

#### Key capabilities

*   Debug accessibility issues, audit Core Web Vitals (LCP, CLS, and INP), run visual checks, and diagnose runtime errors or memory leaks.

[Chrome DevTools MCP Repo](https://github.com/ChromeDevTools/chrome-devtools-mcp)

![](https://www.gstatic.com/antigravity/plugins/modern-web-guidance-plugin/assets/logo.svg?v=60a9c11e4177)

Web & Chrome

### Modern Web Guidance

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/modern-web-guidance-plugin "Open Modern Web Guidance in the Antigravity App")

Keep your coding agent up to date with the latest web platform features and Chrome best practices.

#### What's included

*   Evergreen, expert-vetted skills for modern HTML, CSS, JavaScript, Baseline APIs, and Manifest V3 Chrome Extensions.

#### Key capabilities

*   Build accessible, performant, and secure web experiences using native dialogs, popovers, View Transitions, and modern layout primitives.

Example prompt: “Audit this project for modern web best practices and modernization opportunities”

[Modern Web Guidance Docs](https://developer.chrome.com/docs/modern-web-guidance)

![](https://www.gstatic.com/antigravity/plugins/android-cli-plugin/assets/logo.png?v=9d8234ff50a7)

Mobile & Maps

### Android CLI

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/android-cli-plugin "Open Android CLI in the Antigravity App")

Core tools and knowledge required to develop, run, and verify Android apps.

#### What's included

*   Android CLI integration and curated Android skills for edge-to-edge adaptive UI, testing frameworks, Play compliance checks, and R8 optimization.

#### Key capabilities

*   Scaffold new Android projects and build adaptive Compose layouts.
*   Deploy and test apps on connected devices or Android virtual devices using natural language.
*   Analyze R8 rules and migrate to current AndroidX libraries and Gradle plugins.

Example prompt: “Create a new Android project called MyFirstApp using the empty-activity template”

[Android Agent Tools](https://developer.android.com/tools/agents)

![](https://www.gstatic.com/images/branding/productlogos/flutter/v6/192px.svg)

Mobile & Maps

### Dart and Flutter

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/flutter "Open Dart and Flutter in the Antigravity App")

Official Dart and Flutter plugin for building natively compiled applications for mobile, web, desktop, and embedded devices from a single codebase.

#### What's included

*   Flutter and Dart skills, rules, custom accessibility agent, and the Dart MCP server to inspect and drive running Dart or Flutter applications.

#### Key capabilities

*   **Live tooling integration:** Run static analysis, manage packages with pub, format code, fix layout overflows, and execute widget tests.
*   **Multiplatform & accessible UI:** Build adaptive layouts across mobile, web, and desktop and run automated Flutter accessibility audits.

Example prompt: “Build a responsive Flutter layout that adapts across mobile, tablet, and desktop form factors”

[Flutter Agentic Tools](https://docs.flutter.dev/ai/create-with-ai)

![](/assets/image/blog/marketplace-logos/google-cloud-developer.svg)

Cloud & Data

### Google Cloud Developer

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-cloud-developer "Open Google Cloud Developer in the Antigravity App")

Equip your coding agent with Google Cloud knowledge and workflows to design, deploy, and manage cloud infrastructure directly from Antigravity.

#### What's included

*   Google Cloud onboarding, IAM/ADC authentication, and gcloud CLI safety skills bundled with the Google Developer Knowledge MCP server.

#### Key capabilities

*   **Cloud-native deployment:** Author service architectures, container definitions, Terraform configs, and client integrations across Cloud Run, GKE, Cloud SQL, Firestore, Spanner, AlloyDB, and BigQuery.
*   **Guided setup & gcloud validation:** Streamline project provisioning, Application Default Credentials, IAM roles, and safety-checked gcloud CLI commands.

Example prompt: “Help me set up a new Google Cloud project, link billing, and configure local authentication.”

[Google Cloud Agent Skills](https://github.com/google/skills/tree/main/plugins/cloud/google-cloud-developer)

![](https://www.gstatic.com/antigravity/plugins/data-agent-kit-plugin/assets/logo.svg?v=057413350267)

Cloud & Data

### Data Agent Kit Starter Pack

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/data-agent-kit-plugin "Open Data Agent Kit Starter Pack in the Antigravity App")

Specialized suite of skills and tools for data engineers building end-to-end analytics, ETL, and AI workflows on Google Cloud.

#### What's included

*   Domain skills for BigQuery SQL & ML, dbt transformations, Apache Spark, Dataflow, Spanner, AlloyDB, Cloud SQL, Bigtable, and workflow orchestration.
*   Notebook, Streamlit dashboard, and semantic modeling guidance.

#### Key capabilities

*   **End-to-end data pipelines:** Architect ingestion and transformation pipelines across Cloud Storage, dbt, Spark, Dataflow, and BigQuery in natural language.
*   **SQL, ML & troubleshooting:** Write optimized BigQuery SQL, build PySpark ML notebooks, explore dataset lineage, and diagnose failed pipeline jobs.

Example prompt: “Create a PySpark notebook to train a distributed Random Forest model on the BigQuery table my\_transactions”

[Data Agent Kit Repository](https://github.com/GoogleCloudPlatform/data-agent-kit-plugin)

![](https://www.gstatic.com/antigravity/plugins/looker/assets/logo.svg?v=dd9ffd6d5c61)

Cloud & Data

### Looker

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/looker "Open Looker in the Antigravity App")

Connect to your managed Looker MCP server to explore semantic data models, run saved Looks, build dashboards, and validate LookML.

#### What's included

*   Managed Looker MCP server configuration and Looker analytics and LookML authoring skills.

#### Key capabilities

*   **Conversational BI & LookML:** Inspect Looker models and explores, query governed metrics, build dashboards, and audit instance health without leaving your workspace.

Example prompt: “List available Looker models and explores in my instance”

[Looker Documentation](https://cloud.google.com/looker/docs)

![](https://www.gstatic.com/images/branding/productlogos/google_developers/v8/192px.svg)

Cloud & Data

### Google Developer Knowledge

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-developer-knowledge "Open Google Developer Knowledge in the Antigravity App")

Search and retrieve official, up-to-date documentation across Google Cloud, Gemini, Android, Firebase, Flutter, Google Maps Platform, Web, and Antigravity.

#### What's included

*   Google Developer Knowledge MCP server and retrieval skill grounded in official Google developer documentation.

#### Key capabilities

*   **Live API & CLI verification:** Check current SDK signatures, IAM roles, gcloud flags, and architecture guides before generating code.

Example prompt: “Search official Google documentation for how to implement structured outputs with the Gemini API”

[Developer Knowledge Docs](https://developers.google.com/knowledge/mcp)

![](https://www.gstatic.com/antigravity/logos/antigravity-icon__full-color.png)

AI & Science

### Google Antigravity SDK

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-antigravity-sdk "Open Google Antigravity SDK in the Antigravity App")

Use the Antigravity Python SDK to build autonomous, tool-using AI agents.

#### What's included

*   Agent skill with architecture references, quickstart examples, and configuration guides for the Antigravity Python SDK (google-antigravity).

#### Key capabilities

*   **Build & secure custom agents:** Scaffold Python agents, configure models, register custom tools and MCP servers, and author declarative safety policies.
*   **Advanced orchestration:** Implement lifecycle hooks, multi-agent delegation, structured outputs, multimodal input, and token usage observability.

[Antigravity SDK Docs](/docs/sdk/overview)

![](https://www.gstatic.com/images/branding/productlogos/maps_2025/v1/web-96dp/logo_maps_2025_color_2x_web_96dp.png)

Mobile & Maps

### Google Maps Platform

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google_maps_platform "Open Google Maps Platform in the Antigravity App")

Design, build, and deploy location-aware experiences across Web, Android, iOS, and backend services with Google Maps Platform.

#### What's included

*   Agent skills covering Maps (2D/3D, Street View, Styling, Clustering), Places, Address Validation, Geocoding, Routes & ETA, Geofencing, and Environmental APIs.

#### Key capabilities

*   **Location-rich features:** Generate production-ready code for interactive maps, place search, route optimization, heatmaps, and air quality, solar, or weather insights.
*   **Guided key setup:** Prototype quickly and follow guided best practices to restrict API keys before shipping to production.

[Maps Agent Skills Repo](https://github.com/googlemaps/agent-skills)

![](https://www.gstatic.com/images/branding/productlogos/google_home/v6/192px.svg)

Mobile & Maps

### Google Home Developer

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-home-developer "Open Google Home Developer in the Antigravity App")

Search official Google Home, Matter, and OpenThread documentation and query Cloud-to-cloud integration diagnostics.

#### What's included

*   Google Home Developer MCP server covering Google Home APIs, Matter commissioning, Thread networking, and smart home traits.

#### Key capabilities

*   Implement Matter device commissioning, Cloud-to-cloud SYNC/EXECUTE intents, and OpenThread Border Router configurations with grounded references.

Example prompt: “How do I commission a Matter device and read its OnOff trait using the Google Home APIs on Android?”

[Google Home Developer MCP](https://developers.home.google.com/mcp/developer)

![](/assets/image/blog/marketplace-logos/science.svg)

AI & Science

### Science

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/science-overview "Open Science in the Antigravity App")

Curated collection of agent skills, scientific databases, and interactive viewers for computational research workflows.

#### What's included

*   Science Overview plugin plus dedicated domain plugins for Genomics, Structural Biology, Scientific Literature, and Chemistry.

Domain plugins:

[Genomics](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/genomics "Open Genomics in the Antigravity App")[Structural Biology](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/structural-biology "Open Structural Biology in the Antigravity App")[Scientific Literature](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/scientific-literature "Open Scientific Literature in the Antigravity App")[Chemistry](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/chemistry "Open Chemistry in the Antigravity App")

#### Key capabilities

*   Analyze DNA variants with AlphaGenome, inspect 3D protein structures with AlphaFold, run RDKit cheminformatics, and search PubMed, clinical trials, and preprints.

[Science Skills Repository](https://github.com/google-deepmind/science-skills)

![](https://www.gstatic.com/antigravity/plugins/robotics/assets/logo.svg?v=247c28138ebf)

AI & Science

### Robotics

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/robotics "Open Robotics in the Antigravity App")

Robotics skills for 3D perception, collision-free motion planning, visual servoing, MuJoCo simulation, and sim-to-real transfer.

#### What's included

*   Curated robotics and MuJoCo simulation skills, SimReady 3D asset auditing workflows, and an interactive MuJoCo Studio 3D web sidecar.

#### Key capabilities

*   Plan collision-free joint trajectories, train reinforcement learning locomotion policies in MuJoCo Playground, audit physics models, and run visual servoing loops.

Example prompt: “Plan a collision-free joint trajectory in MuJoCo”

![](https://www.gstatic.com/images/branding/productlogos/google_developers/v8/192px.svg)

AI & Science

### Google Health Developer

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-health-developer "Open Google Health Developer in the Antigravity App")

Search and retrieve official Google Health API documentation through the Google Health Developer MCP server.

#### What's included

*   Google Health Developer MCP server for grounded lookup of endpoints, OAuth scopes, data types, and webhook subscriptions.

#### Key capabilities

*   Implement health and wellness integrations—including sleep stages, heart rate metrics, OAuth authorization, and webhook updates—against current API specs.

Example prompt: “Which OAuth scopes does the Google Health API use, and which data types map to each scope?”

[Google Health Developer MCP](https://developers.google.com/health/mcp)

* * *

Google Workspace plugins

Connect your agent to your docs, spreadsheets, presentations, files, calendar, and inbox with official Google Workspace plugins—click any plugin below to open its detail page in the Antigravity App, or install from your terminal with `agy plugin install <id>` (for example, `agy plugin install gdocs`):

[![](https://www.gstatic.com/images/branding/productlogos/docs_2026/v2/web/192px.svg)Google Docs](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gdocs "Open Google Docs in the Antigravity App")

[![](https://www.gstatic.com/images/branding/productlogos/sheets_2026/v2/web/192px.svg)Google Sheets](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gsheets "Open Google Sheets in the Antigravity App")

[![](https://www.gstatic.com/images/branding/productlogos/slides_2026/v2/web/192px.svg)Google Slides](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gslides "Open Google Slides in the Antigravity App")

[![](https://www.gstatic.com/images/branding/productlogos/drive_2026/v2/web/192px.svg)Google Drive](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gdrive "Open Google Drive in the Antigravity App")

[![](https://www.gstatic.com/images/branding/productlogos/calendar_2026/v2/web/192px.svg)Google Calendar](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gcalendar "Open Google Calendar in the Antigravity App")

[![](https://www.gstatic.com/images/branding/productlogos/gmail_2020q4/v11/192px.svg)Gmail](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/gmail "Open Gmail in the Antigravity App")

Searching Google developer docs?

Bundles equip your agent for a specific stack. To ground its answers about any Google developer product in current documentation, pair them with the [Google Developer Knowledge plugin](https://developers.google.com/knowledge/mcp), which connects with your Google credentials and lets the agent search and read official documentation for Android, Firebase, Google Cloud, Google Maps Platform, Antigravity, and other Google developer products. For details and an example prompt, refer to [Search Google developer docs](/docs/mcp#example-search-google-developer-docs) in the MCP guide.

[Open in Antigravity](antigravity://customizations/marketplaces/antigravity-plugins-official/plugins/google-developer-knowledge "Open Google Developer Knowledge in the Antigravity App")

* * *

## Next steps

[

Marketplace

Plugin Marketplace

Search, filter, and open all curated Google and partner plugins directly in Antigravity.

](/docs/marketplace/#browse-marketplace-plugins)[

Integrations

Model Context Protocol (MCP)

Connect custom MCP servers and external tools to your agent workspace.

](/docs/mcp)[

Python SDK

Antigravity SDK

Build custom programmatic agents with the Antigravity Python SDK.

](/docs/sdk/overview)