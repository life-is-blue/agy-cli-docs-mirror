# Slash commands overview

Available on: Antigravity App, Antigravity CLI

Slash commands provide quick shortcuts for invoking specialized agent workflows, reasoning modes, interactive planning tools, and background automations. These commands operate consistently across both the **Google Antigravity App** (Desktop and Web) and the **Antigravity CLI**.

Note

**Quick navigation**: Type `/` in any chat input or terminal prompt to open the interactive command autocompletion menu.

* * *

## Overview

Modern software development calls for different agent workflows depending on the complexity and scope of the task:

1.  **Everyday engineering**: Standard prompts for interactive feature development, navigation, and refactoring.
2.  **Agent orchestrators**: Multi-agent coordination for hard reasoning problems ([`/boost`](/docs/boost)), parallel tasks on a shared message board ([`/swarm`](/docs/swarm)), and multi-milestone campaigns ([`/teamwork`](/docs/teamwork)).
3.  **Structured planning**: Interactive requirement interviews and reviewable plans before modifying code.
4.  **Continuous autonomy**: Uninterrupted execution until every requirement and verification check passes ([`/goal`](/docs/commands/goal)).
5.  **Background tools**: Sandboxed browser research, scheduled automations, and side queries.

Slash commands give you precise, instantaneous control over these capabilities.

* * *

## Command catalog

The following table provides a complete reference for all public slash commands:

| Command | Category | Description | Plan Tier | Horizon |
| :-- | :-- | :-- | :-- | :-- |
| [`/boost`](/docs/boost) | Reasoning | Multi-agent deep reasoning for complex bugs, race conditions, and algorithms. | Paid plans | Seconds to hours |
| [`/teamwork`](/docs/teamwork) | Reasoning | Collaborative agent teams for repo-scale migrations, simulation, and research. | Paid plans | Hours to days |
| [`/run-workflow`](/docs/dynamic-workflows) | Reasoning | Writes and runs a Python script that orchestrates many agents across parallel and sequential phases. | Google AI Pro and Ultra | Minutes to hours |
| [`/swarm`](/docs/swarm) | Reasoning | Named workers and a verifier split a task and coordinate on a shared message board. | Google AI Pro and Ultra | Minutes to hours |
| [`/goal`](/docs/commands/goal) | Reasoning | Autonomous execution until the goal is achieved without intermediate pauses. | All plans | Minutes to hours |
| [`/plan`](/docs/plan) | Planning | Researches code, conducts requirement interviews, and drafts a reviewable plan artifact. | All plans | Minutes |
| [`/grill-me`](/docs/commands/grill-me) | Planning | Interviews you one question at a time, with a recommended answer for each, to align on design details and edge cases. | All plans | Minutes |
| [`/learn`](/docs/commands/learn) | Customization | Distills session feedback and corrections into persistent Rules or Skills. | All plans | Immediate |
| [`/agy-customizations`](/docs/commands/agy-customizations) | Customization | Loads the customization reference so the agent can create, fix, or explain rules, skills, plugins, hooks, and MCP servers. | All plans | Immediate |
| [`/plugin`](/docs/plugins) | Customization | Opens the interactive [Plugins Manager](/docs/marketplace) or manages and creates plugins. | All plans | Immediate |
| [`/automation`](/docs/commands/automation) | Automation | Has the agent set up a scheduled background automation managed in the **Automations** tab. Antigravity App only. | All plans | Scheduled |
| [`/schedule`](/docs/commands/schedule) | Automation | Schedules an instruction as a one-time timer or recurring cron job. | All plans | Scheduled |
| [`/browser`](/docs/commands/browser) | Tools | Launches a [browser subagent](/docs/browser) for live UI testing, screenshots, and web inspection (built-in browser on personal App accounts `v2.30.0+`, or Chrome DevTools MCP). | All plans | Minutes |
| [`/btw`](/docs/cli/commands/btw) | Tools | Asks a quick contextual question in the background without pausing work. | All plans | Immediate |
| [`/generative_ui`](/docs/commands/generative-ui) | Tools | Builds interactive widgets, such as diagrams, charts, and explainers, as HTML artifacts or inline in the conversation. Antigravity App only. | All plans | Minutes |
| [`/antigravity-guide`](/docs/commands/antigravity-guide) | Tools | Answers questions about using Antigravity from the official documentation. | All plans | Immediate |

* * *

## Reasoning and autonomy

### /boost

Activates the on-demand three-tier multi-agent reasoning hierarchy (`Orchestrator` -> `DeepCoder` / `DeepInvestigator` -> isolated workers). It explores multiple hypotheses, runs test suites, and independently verifies solutions before returning results.

To invoke Boost for an algorithmic optimization, run the following command:

```prompt
/boost Optimize the sparse matrix multiplication routine using SIMD intrinsics and benchmark throughput.
```

For detailed architectural documentation and CLI keybindings, refer to the [Boost deep reasoning guide](/docs/boost) and the [CLI reference](/docs/cli/reference).

### /teamwork

Initiates the multi-agent framework for multi-day engineering campaigns, subsystem rewrites, and open-ended scientific research. Begins with an interactive scoping interview led by the Sentinel to draft a binding specification plan.

To launch a multi-agent migration, run the following command:

```prompt
/teamwork Migrate our REST backend from Express to Fastify with full test parity and benchmarks.
```

For complete multi-agent lifecycle documentation and engineering patterns, refer to the [Teamwork agent teams guide](/docs/teamwork).

### /run-workflow

Launches [Dynamic Workflows](/docs/dynamic-workflows): the agent writes a short Python script that orchestrates many agents, shows it to you for approval, and runs it in the background. The script fans out the same task across a list of items with `parallel()`, runs staged steps with `pipeline()`, and collects a structured result from each agent, while you follow phases and agents live in the workflow step.

To review every changed file in parallel, run the following command:

```prompt
/run-workflow List the Python files changed since main, review each file in parallel for unhandled exceptions, and log a one-line verdict per file.
```

For script building blocks, agent options, and permissions, refer to the [Dynamic Workflows guide](/docs/dynamic-workflows).

### /swarm

Turns your conversation into the coordinator of a swarm: named workers that each own one piece of the task, plus a verifier that reviews and tests their changes. The workers coordinate on a shared message board with `@mentions`, and idle workers wait without using tokens until someone mentions them.

To split a test expansion across workers, run the following command:

```prompt
/swarm Add unit tests for src/utils/date.ts and src/utils/currency.ts in parallel, and have a verifier run npm test.
```

In the Antigravity CLI, run `/swarm board` or press Alt+S to open the live board full screen.

For how to monitor the board, message workers, and choose between multi-agent commands, refer to the [Swarm guide](/docs/swarm).

### /goal

Instructs the agent to work continuously until the specified objective is fully achieved. The agent autonomously runs builds, diagnoses errors, and applies corrective edits without pausing for turn-by-turn confirmations.

To run a test suite repair autonomously, run the following command:

```prompt
/goal Fix all failing unit tests in the authentication package and ensure 100% pass rate.
```

For details on how goal mode intercepts stops, audits deliverables, and how to cancel a goal, refer to the [Goal command guide](/docs/commands/goal).

* * *

## Planning and requirements

### /plan

The `/plan` slash command facilitates structured planning, codebase exploration, and requirements discovery before jumping directly into execution. It makes sure complex tasks are well-understood, properly scoped, and organized before code changes are made.

#### How it works

When you invoke `/plan`, Antigravity runs a four-step workflow:

1.  **Analysis and discovery**: The agent examines your prompt, analyzes the workspace, reads relevant source files, and discovers dependencies or potential roadblocks.
2.  **Clarification and interviewing**: If details are underspecified or architectural decisions are ambiguous, the agent conducts a focused interview with you (leveraging interactive question prompts or structured options) to clarify requirements and trade-offs.
3.  **Structured plan creation**: The agent creates a comprehensive `Implementation Plan` artifact detailing the high-level approach, step-by-step task breakdowns with verification gates, and potential risks.
4.  **User review and approval**: The agent presents the plan artifact for your review. Once you review, comment on, or approve the plan, the agent transitions into execution mode.

#### When to use /plan

Use `/plan` in the following scenarios:

*   **Complex refactors**: When refactoring architectural components across multiple files or packages.
*   **Ambiguous requirements**: When starting a feature with open questions, trade-offs, or missing specifications.
*   **High-risk changes**: For database migrations, core protocol changes, or security-sensitive updates where an upfront checklist and risk assessment are critical.
*   **Collaborative alignment**: When you want to review and guide the agent’s proposed steps before any code modifications occur.

#### Usage examples

To plan a specific task, run `/plan` with your objective:

```prompt
/plan Refactor our authentication middleware to support OIDC token verification with JWKS caching
```

To begin an interactive discovery session for the current workspace context without a predefined prompt:

```text
/plan
```

For complete workflow details, refer to the [Plan slash command guide](/docs/plan) and the [Implementation plan artifact guide](/docs/implementation-plan).

### /grill-me

Has the agent interview you about a task before it starts work. The agent asks one question at a time and recommends an answer for each. It explores the codebase instead of asking you anything the code can answer, and keeps going until you share the same understanding of the task.

To align on design constraints, run the following command:

```prompt
/grill-me I want to redesign the notification dispatch queue to support priority scheduling.
```

To turn your answers into a reviewable plan, stack it with [`/plan`](/docs/plan) (`/plan /grill-me <task>`). For complete workflow details, refer to the [Grill me command guide](/docs/commands/grill-me).

* * *

## Workflows and customization

### /learn

Analyzes recent corrections, user feedback, and debugging resolutions from your active session, distilling them into persistent project rules (`AGENTS.md`, `GEMINI.md`, or `.agents/rules/*.md`) or reusable agent skills (`.agents/skills/<name>/SKILL.md`). The agent proposes changes in a `learning_proposal.md` artifact and writes files only after you approve.

To capture recent session patterns into persistent rules, run the following command:

```prompt
/learn Save our database transaction retry pattern as a project rule for all future database changes.
```

For the proposal workflow and the full list of rule and skill locations, refer to the [Learn command guide](/docs/commands/learn) and the [Rules documentation](/docs/rules).

### /agy-customizations

Loads the Antigravity Customization System Guide into the agent’s context for the rest of the conversation, so the agent works from the documented formats, discovery locations, and precedence rules when it creates, fixes, or explains rules, skills, plugins, hooks, and MCP servers. Available in the Antigravity App, the Antigravity CLI, and the Antigravity IDE.

To build a customization with the reference loaded, describe what you want after the command:

```prompt
/agy-customizations create a PreToolUse hook that blocks git push --force
```

For what the reference covers and more examples, refer to the [Customizations command guide](/docs/commands/agy-customizations).

### /plugin

Manages installed plugins, browses the [Marketplace](/docs/marketplace), and packages reusable skills, rules, subagents, MCP servers, and hooks into a single deployable plugin bundle.

In the **Antigravity CLI**, running `/plugin` (or its alias `/plugins`) opens the interactive Plugins Manager panel with **Installed** and **Discover** tabs, or executes inline subcommands directly (`<marketplace-name>` supports the official marketplace, `antigravity-plugins-official`):

```text
/plugin
/plugin install <plugin-name>@antigravity-plugins-official
/plugin install <local-path>
/plugin list
```

In the **Antigravity App**, you can also invoke `/plugin` with natural-language instructions to enable, disable, install, or scaffold custom plugins.

For complete plugin manifest and marketplace documentation, refer to the [Plugins guide](/docs/plugins) and the [Marketplace guide](/docs/marketplace).

* * *

## Automation and scheduling

### /automation

Has the agent set up a scheduled background automation (formerly called a Scheduled Task) in the **Google Antigravity App**. You can also start the same flow by selecting **Create with Prompt** in the **Automations** tab, which opens a new conversation with the command filled in for you to send. The agent asks for a cadence, day, and time, pins the schedule to an IANA timezone with `CRON_TZ=<zone>`, and writes a self-contained prompt. It then saves the automation to `~/.gemini/config/sidecars/<automation-id>/sidecar.json`, turned off until you turn it on in the **Automations** tab.

To set up a weekly pull request check, run the following command:

```prompt
/automation every Monday at 9am Pacific time, check my open pull requests and list any with failing checks
```

For the full flow and how `/automation` compares with `/schedule`, refer to the [Automation command guide](/docs/commands/automation).

### /schedule

Configures the agent to execute a prompt at a specified future time or on a recurring cron schedule using background scheduled tasks.

To set up a daily cleanup routine, run the following command:

```prompt
/schedule "0 9 * * 1-5" Run git fetch, prune stale local branches, and summarize pending PR reviews.
```

For timer and cron parameters and managing active schedules, refer to the [Schedule command guide](/docs/commands/schedule). For how `/schedule` differs from persistent automations, refer to [`/automation` compared with `/schedule`](/docs/commands/automation#automation-compared-with-schedule).

* * *

## Tools and context

### /browser

Delegates a task directly to the `browser` subagent to open pages, test flows, capture screenshots, and inspect console errors or network requests. On personal Google Accounts in the Antigravity App (`v2.30.0+`), it runs inside the App’s built-in browser with zero Chrome setup (where plain-language prompts also invoke `browser` subagents automatically); in the Antigravity CLI, the Antigravity IDE, and business or enterprise accounts, it connects to Google Chrome (`v144+`) through Chrome DevTools MCP.

To verify a local web server layout, run the following command:

```prompt
/browser Open http://localhost:3000/dashboard, verify that the analytics charts render, and capture a screenshot.
```

For built-in browser workflows, parallel tabs, and sign-in handoff, refer to [Browser use](/docs/browser). For Chrome setup and DevTools profiling tools, refer to the [Browser command guide](/docs/commands/browser).

### /btw

Submits an out-of-band query that runs in a lightweight background thread without interrupting or pausing the primary agent’s active execution.

To ask an aside while an implementation is running, run the following command:

```text
/btw Which file did you say defines the UserSession interface?
```

For CLI card navigation, history browsing, and `/copy btw` clipboard support, refer to the [Side question (`/btw`) command guide](/docs/cli/commands/btw).

### /generative\_ui

Has the agent build an interactive widget, such as a diagram, chart, or step-by-step explainer, as an HTML artifact that you open in the side panel. Compact widgets can also appear inline in the conversation. Available in the Antigravity App only.

To see how a request moves through your middleware, run the following command:

```prompt
/generative_ui Show a simple left-to-right diagram of a request going from the client through requireApiKey and the bookmarks router to the database, with a toggle for a valid or invalid API key. Use icons, short labels, and no code.
```

For placement, sizing, and sandbox details, refer to the [Generative UI command guide](/docs/commands/generative-ui).

### /antigravity-guide

Gives the agent the official Antigravity documentation, with a quick reference for the Antigravity App, the Antigravity CLI, the Antigravity IDE, and the Antigravity SDK, so it can answer questions about using and configuring Antigravity. Available in the Antigravity App and the Antigravity CLI.

To ask how to do something in Antigravity, run the following command:

```prompt
/antigravity-guide how do I run the CLI in headless mode in GitHub Actions with a JSON schema?
```

For what the reference covers and more examples, refer to the [Antigravity guide command guide](/docs/commands/antigravity-guide).

* * *

## Command selection guide

The following decision guide outlines when to use each command based on your task requirements:

| Primary Objective | Recommended Command | Key Capability |
| :-- | :-- | :-- |
| **Complex bug, race condition, or algorithmic puzzle** | [`/boost`](/docs/boost) | Multi-agent deep reasoning with isolated verification loops. |
| **Multi-day project, repository migration, or research** | [`/teamwork`](/docs/teamwork) | Collaborative agent teams with scoping interviews and milestone roadmaps. |
| **Same task across many files or packages, or staged steps** | [`/run-workflow`](/docs/dynamic-workflows) | A reviewable Python script that runs agents in parallel or in sequence and collects structured results. |
| **Large task that splits across independent files or packages** | [`/swarm`](/docs/swarm) | Parallel named workers and a verifier coordinating on a shared message board. |
| **Feature requiring review before making code edits** | [`/plan`](/docs/plan) | Researches code, interviews requirements, and generates a reviewable plan. |
| **Vague requirements needing architectural alignment** | [`/grill-me`](/docs/commands/grill-me) | Conducts a step-by-step interview to clarify edge cases and constraints. |
| **Task that should run continuously until 100% complete** | [`/goal`](/docs/commands/goal) | Autonomous execution without turn-by-turn confirmation pauses. |
| **Distill recent corrections into permanent project rules** | [`/learn`](/docs/commands/learn) | Analyzes session patterns and writes persistent rules and skills. |
| **Create or debug a rule, skill, plugin, hook, or MCP server** | [`/agy-customizations`](/docs/commands/agy-customizations) | Loads the customization reference so the agent follows the documented formats and locations. |
| **Discover, install, or manage plugins and marketplace bundles** | [`/plugin`](/docs/plugins) | Interactive [Plugins Manager](/docs/marketplace) in the CLI and conversational plugin management. |
| **Web research, UI validation, and layout inspection** | [`/browser`](/docs/commands/browser) | [Built-in browser](/docs/browser) (`v2.30.0+` App personal accounts) or Chrome DevTools MCP browser subagent for live page interactions. |
| **Persistent scheduled background automation** | [`/automation`](/docs/commands/automation) | Creates a scheduled automation managed in the Automations tab. Antigravity App only. |
| **One-shot countdown timer or recurring background schedule** | [`/schedule`](/docs/commands/schedule) | Runs instructions in the background on cron schedules. |
| **Quick side query without pausing primary agent work** | [`/btw`](/docs/cli/commands/btw) | Lightweight out-of-band query executed in the background. |
| **Visual explanation, diagram, chart, or clickable prototype** | [`/generative_ui`](/docs/commands/generative-ui) | Interactive HTML widgets in the side panel or inline in the conversation (Antigravity App only). |
| **Question about how to use or configure Antigravity** | [`/antigravity-guide`](/docs/commands/antigravity-guide) | Answers from the official documentation for every Antigravity surface. |

* * *

## Cross-surface compatibility

Public slash commands are supported across Antigravity developer surfaces:

| Surface | Input Method | Navigation and Management |
| :-- | :-- | :-- |
| **Antigravity App (Desktop and Web)** | Type `/` in the prompt input or select from the command menu. | Model selector dropdown, Artifact review panel, Visual diff viewer. |
| **Antigravity CLI** | Type `/` in the interactive prompt box. | `/agents` panel, Alt + J (switch threads), Ctrl + O (trajectory). |

* * *

## Next steps

Explore related documentation and guides:

*   [Boost deep reasoning (`/boost`)](/docs/boost): Dive deep into the three-tier multi-agent reasoning hierarchy.
*   [Swarm (`/swarm`)](/docs/swarm): Coordinate named workers and a verifier on a shared message board for parallel tasks.
*   [Plan slash command (`/plan`)](/docs/plan): Conduct structured planning, requirement discovery, and interactive interviews.
*   [Teamwork agent teams (`/teamwork`)](/docs/teamwork): Learn how collaborative agent teams tackle large-scale migrations.
*   [Dynamic Workflows (`/run-workflow`)](/docs/dynamic-workflows): Orchestrate many agents with a reviewable Python script.
*   [Side question command (`/btw`)](/docs/cli/commands/btw): Ask quick background questions without adding to your conversation history.
*   [Antigravity guide command (`/antigravity-guide`)](/docs/commands/antigravity-guide): Ask how to use or configure Antigravity and get answers from the official documentation.
*   [Goal command (`/goal`)](/docs/commands/goal): Run long-horizon tasks autonomously until every deliverable is verified.
*   [Learn command (`/learn`)](/docs/commands/learn): Persist session corrections as rules and skills through a reviewable proposal.
*   [Customizations command (`/agy-customizations`)](/docs/commands/agy-customizations): Load the customization reference before building rules, skills, plugins, hooks, or MCP servers.
*   [Automation command (`/automation`)](/docs/commands/automation): Set up a persistent scheduled automation with the agent’s help.
*   [Schedule command (`/schedule`)](/docs/commands/schedule): Set one-shot timers and recurring cron schedules within a conversation.
*   [Browser command (`/browser`)](/docs/commands/browser): Delegate web tasks and UI verification to the browser subagent.
*   [Generative UI command (`/generative_ui`)](/docs/commands/generative-ui): Have the agent show answers as interactive widgets in the Antigravity App.
*   [Implementation plans artifact guide](/docs/implementation-plan): Master reviewable planning artifacts and structured workflows.
*   [Rules](/docs/rules): Persist project-wide patterns and conventions.
*   [Plugins (`/plugin`)](/docs/plugins) and [Marketplace](/docs/marketplace): Discover, install, and package reusable agent extensions.
*   [Sidecars and scheduled tasks (`/schedule`)](/docs/sidecars): Automate routine maintenance with cron expressions.