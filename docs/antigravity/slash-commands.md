# Slash commands overview

Available on: Antigravity App, Antigravity CLI, IDE extensions (VS Code, Visual Studio, Eclipse, JetBrains, Android Studio, Zed, Xcode), Antigravity IDE

Slash commands are shortcuts for agent workflows and tools. Type `/` in the prompt box of the **Antigravity App** or the **Antigravity CLI** to open the command menu, and keep typing to filter it.

The commands below are grouped by what you want to do, and each one links to its guide. **Available on** lists where you can use it: the Antigravity App (App), the Antigravity CLI (CLI), or IDE extensions. IDE extensions means VS Code, Visual Studio, and Eclipse unless noted. The standalone Antigravity IDE has the same commands as the VS Code extension.

For every CLI command, including utilities such as `/clear`, `/help`, and `/model`, see [CLI commands](/docs/cli/reference).

## Plan before you build

Agree on the approach before the agent changes any code.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/plan`](/docs/plan) | Explores the codebase, clarifies requirements, and drafts a reviewable implementation plan before any edits. | App, CLI, IDE extensions (all editors) |
| [`/grill-me`](/docs/commands/grill-me) | Interviews you one question at a time, with a recommended answer for each, before the agent starts work. | App, CLI, IDE extensions |

For example:

```prompt
/plan Refactor our authentication middleware to support OIDC token verification with JWKS caching
```

To turn the interview into a plan, use both: `/plan /grill-me <task>`.

## Delegate work

Give the agent more autonomy, deeper reasoning, more agents, a browser, or a schedule.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/goal`](/docs/commands/goal) | Keeps working, without pausing for confirmation, until the goal is verified complete. | App, CLI, IDE extensions |
| [`/boost`](/docs/boost) | Runs multi-agent deep reasoning on hard bugs, race conditions, and algorithms. Paid plans only. | App, CLI, IDE extensions |
| [`/swarm`](/docs/swarm) | Splits a task between named agents and a verifier that coordinate on a shared message board. All plans. | App, CLI |
| [`/teamwork`](/docs/teamwork) | Starts a team of agents for multi-day projects, migrations, and research. Paid plans only. | App, CLI, IDE extensions |
| [`/run-workflow`](/docs/dynamic-workflows) | Writes and runs a script that orchestrates many agents in parallel and sequential phases. All plans. | App, CLI |
| [`/browser`](/docs/commands/browser) | Hands UI testing, screenshots, and web checks to a browser subagent, in the App’s built-in browser or in Chrome. | App, CLI, IDE extensions |
| [`/automation`](/docs/commands/automation) | Sets up a recurring background task that you manage in the Automations tab. | App |
| [`/schedule`](/docs/commands/schedule) | Wakes the agent later in the same conversation, once or on a recurring schedule. | App, CLI, IDE extensions |

To choose between `/boost`, `/swarm`, and `/teamwork`, see [Choose between Swarm, Teamwork, Boost, and subagents](/docs/swarm#choose-between-swarm-teamwork-boost-and-subagents).

For example:

```prompt
/schedule "0 9 * * 1-5" Run git fetch, prune stale local branches, and summarize pending PR reviews.
```

```prompt
/browser Open http://localhost:3000/dashboard, verify that the analytics charts render, and capture a screenshot.
```

## Get help

Ask a side question, search your code, talk to the agent or dictate, get a visual explanation, or ask how to use Antigravity.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/btw`](/docs/commands/btw) | Answers a side question in a read-only fork of the conversation, without interrupting the agent or adding to its history. | App, CLI, IDE extensions |
| [`/codesearch`](/docs/cli/commands/codesearch) | Searches the code in your workspace without leaving the session. | CLI |
| [`/voice`](/docs/cli/commands/voice) | Talks with the agent out loud in voice mode, or dictates a prompt with a live transcript. | CLI |
| [`/generative_ui`](/docs/commands/generative-ui) | Builds an interactive widget, such as a diagram, chart, or explainer, in the side panel or inline in the conversation. | App |
| [`/antigravity-guide`](/docs/commands/antigravity-guide) | Answers questions about using and configuring Antigravity from the official documentation. | App, CLI |

For example:

```text
/btw Which file did you say defines the UserSession interface?
```

## Review and manage sessions

Check changes, compact or inspect context use, reopen past conversations, and monitor running agents.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/diff`](/docs/cli/commands/diff) | Shows workspace changes, commit history, and the agent’s turns in an interactive diff viewer. | CLI |
| [`/compact`](/docs/commands/compact) | Summarizes the conversation so far into a checkpoint to free up space in the model’s context window. | App, CLI |
| [`/context`](/docs/cli/commands/context) | Shows how much of the model’s context window the conversation uses. | CLI |
| [`/resume`](/docs/cli/commands/resume) | Finds and reopens a past conversation. | CLI |
| [`/agents`](/docs/cli/commands/agents) | Switches between custom agents and monitors background subagents. | CLI |

For example:

```prompt
/compact Keep the API schema findings, and now add integration tests for the handler.
```

## Customize the agent

Teach the agent how you work and add new capabilities.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/learn`](/docs/commands/learn) | Turns corrections from the session into rules or skills, through a proposal you approve. | App, CLI, IDE extensions |
| [`/agy-customizations`](/docs/commands/agy-customizations) | Loads the customization reference so the agent can create, fix, or explain rules, skills, plugins, hooks, and MCP servers. | App, CLI, IDE extensions |
| [`/mcp-app-development`](/docs/commands/mcp-app-development) | Loads the MCP Apps development guide so the agent can build, theme, package, or debug interactive MCP App plugins. | App |
| [`/plugin`](/docs/plugins) | Manages your plugins and browses the Marketplace. | App, CLI, IDE extensions |

## Configure the CLI

Adjust how the Antigravity CLI reasons, asks for permission, and looks.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/permissions`](/docs/cli/commands/permissions) | Manages the agent’s permission rules in an interactive panel. | CLI |
| [`/effort`](/docs/cli/commands/effort) | Sets how much reasoning effort the model spends, trading speed for depth. | CLI |
| [`/statusline`](/docs/cli/commands/statusline) | Turns the status line on or off, or sets a command that renders it. | CLI |
| [`/title`](/docs/cli/commands/title) | Turns live terminal window titles on or off. | CLI |

## Account and updates

Check your quota and credits, and see what’s new in the CLI.

| Command | What it does | Available on |
| :-- | :-- | :-- |
| [`/usage`](/docs/cli/commands/usage) | Shows how much of your model quota you’ve used. | CLI, IDE extensions (JetBrains, Android Studio, Zed, Xcode) |
| [`/credits`](/docs/cli/commands/credits) | Shows your AI credit balance, with links to buy more. | CLI |
| [`/changelog`](/docs/cli/commands/changelog) | Opens the Antigravity CLI release notes in your terminal. | CLI |

## Next steps

*   [CLI commands](/docs/cli/reference): Every CLI slash command, keyboard shortcut, and command-line flag.
*   [Implementation plans](/docs/implementation-plan): Review and approve the plans that `/plan` creates.
*   [Rules](/docs/rules) and [Skills](/docs/skills): Where `/learn` saves what the agent learns.
*   [Plugins](/docs/plugins) and [Marketplace](/docs/marketplace): Find and install extensions with `/plugin`.