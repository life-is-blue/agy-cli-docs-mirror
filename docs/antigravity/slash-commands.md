# Slash commands overview

Slash commands provide quick shortcuts for invoking specialized agent workflows, reasoning modes, interactive planning tools, and background automations. These commands operate consistently across both **Google Antigravity 2.0** (Desktop and Web) and the **Antigravity CLI**.

Note

**Quick navigation**: Type `/` in any chat input or terminal prompt to open the interactive command autocompletion menu.

* * *

## Overview

Modern software development requires different modes of agent interaction depending on the complexity and scope of the task:

1.  **Everyday engineering**: Standard prompts for interactive feature development, navigation, and refactoring.
2.  **Deep reasoning**: Multi-agent exploration and independent verification.
3.  **Structured planning**: Interactive requirement interviews and reviewable plans before modifying code.
4.  **Long-horizon campaigns**: Collaborative multi-agent teams for repository-scale migrations.
5.  **Background tools**: Sandboxed browser research, scheduled automations, and side queries.

Slash commands give you precise, instantaneous control over these capabilities.

* * *

## Command catalog

The following table provides a complete reference for all public slash commands:

| Command | Category | Description | Plan Tier | Horizon |
| :-- | :-- | :-- | :-- | :-- |
| [`/boost`](/docs/boost) | Reasoning | Multi-agent deep reasoning for complex bugs, race conditions, and algorithms. | Paid plans | Seconds to hours |
| [`/teamwork-preview`](/docs/teamwork) | Reasoning | Collaborative agent teams for repo-scale migrations, simulation, and research. | Paid plans | Hours to days |
| `/goal` | Reasoning | Autonomous execution until the goal is achieved without intermediate pauses. | All plans | Minutes to hours |
| [`/plan`](/docs/implementation-plan) | Planning | Researches code and generates a reviewable implementation plan artifact. | All plans | Minutes |
| `/grill-me` | Planning | Conducts an interactive interview to align on design details and edge cases. | All plans | Minutes |
| [`/learn`](/docs/rules-workflows) | Customization | Distills session feedback and corrections into persistent Rules or Skills. | All plans | Immediate |
| [`/schedule`](/docs/sidecars) | Automation | Schedules an instruction as a one-time timer or recurring cron job. | All plans | Scheduled |
| `/browser` | Tools | Launches a sandboxed browser subagent for web research and UI inspection. | All plans | Minutes |
| `/btw` | Tools | Asks a quick contextual question in the background without pausing work. | All plans | Immediate |

* * *

## Reasoning and autonomy

### /boost

Activates the on-demand three-tier multi-agent reasoning hierarchy (`Orchestrator` -> `DeepCoder` / `DeepInvestigator` -> isolated workers). It explores multiple hypotheses, runs test suites, and independently verifies solutions before returning results.

To invoke Boost for an algorithmic optimization, run the following command:

```
/boost Optimize the sparse matrix multiplication routine using SIMD intrinsics and benchmark throughput.
```

For detailed architectural documentation and CLI keybindings, see the [Boost deep reasoning guide](/docs/boost) and the [CLI reference](/docs/cli/reference).

### /teamwork-preview

Initiates the multi-agent framework for multi-day engineering campaigns, subsystem rewrites, and open-ended scientific research. Begins with an interactive scoping interview led by the Sentinel to draft a binding specification plan.

To launch a multi-agent migration, run the following command:

```
/teamwork-preview Migrate our REST backend from Express to Fastify with full test parity and benchmarks.
```

For complete multi-agent lifecycle documentation and engineering patterns, see the [Teamwork agent teams guide](/docs/teamwork).

### /goal

Instructs the agent to work continuously until the specified objective is fully achieved. The agent autonomously runs builds, diagnoses errors, and applies corrective edits without pausing for turn-by-turn confirmations.

To run a test suite repair autonomously, run the following command:

```
/goal Fix all failing unit tests in the authentication package and ensure 100% pass rate.
```

* * *

## Planning and requirements

### /plan

Inspects the repository, analyzes affected files, and drafts a structured `Implementation Plan` artifact for review. You can annotate the plan with line comments, request revisions, or click **Proceed** to execute.

To generate an implementation plan, run the following command:

```
/plan Add rate limiting middleware to all public API endpoints using Redis token buckets.
```

For artifact interaction workflows, see the [Implementation plan guide](/docs/implementation-plan).

### /grill-me

Prompts the agent to interview you before writing code. The agent asks targeted questions about architecture, error handling, performance targets, and backwards compatibility to eliminate ambiguity.

To align on design constraints, run the following command:

```
/grill-me I want to redesign the notification dispatch queue to support priority scheduling.
```

* * *

## Workflows and customization

### /learn

Analyzes recent corrections, user feedback, and debugging resolutions from your active session, distilling them into persistent project Rules (`.antigravity/rules.md`) or reusable Agent Skills (`SKILL.md`).

To capture recent session patterns into persistent rules, run the following command:

```
/learn Save our database transaction retry pattern as a project rule for all future database changes.
```

For customization syntax and configuration schemas, see the [Rules and workflows documentation](/docs/rules-workflows).

* * *

## Automation and scheduling

### /schedule

Configures the agent to execute a prompt at a specified future time or on a recurring cron schedule using background Scheduled Tasks.

To set up a daily cleanup routine, run the following command:

```
/schedule "0 9 * * 1-5" Run git fetch, prune stale local branches, and summarize pending PR reviews.
```

For background process architecture and cron expressions, see the [Sidecars and scheduled tasks guide](/docs/sidecars).

* * *

## Tools and context

### /browser

Spawns a sandboxed Chrome browser subagent capable of navigating web pages, reading documentation, inspecting DOM elements, capturing visual screenshots, and verifying frontend layouts.

To verify a local web server layout, run the following command:

```
/browser Open http://localhost:3000/dashboard, verify that the analytics charts render, and capture a screenshot.
```

### /btw

Submits an out-of-band query that runs in a lightweight background thread without interrupting or pausing the primary agent’s active execution.

To ask an aside while an implementation is running, run the following command:

```
/btw Which file defines the UserSession interface in this repository?
```

* * *

## Command selection guide

The following decision guide outlines when to use each command based on your task requirements:

| Primary Objective | Recommended Command | Key Capability |
| :-- | :-- | :-- |
| **Complex bug, race condition, or algorithmic puzzle** | [`/boost`](/docs/boost) | Multi-agent deep reasoning with isolated verification loops. |
| **Multi-day project, repository migration, or research** | [`/teamwork-preview`](/docs/teamwork) | Collaborative agent teams with scoping interviews and milestone roadmaps. |
| **Feature requiring review before making code edits** | [`/plan`](/docs/implementation-plan) | Researches code and generates a reviewable implementation plan. |
| **Vague requirements needing architectural alignment** | `/grill-me` | Conducts a step-by-step interview to clarify edge cases and constraints. |
| **Task that should run continuously until 100% complete** | `/goal` | Autonomous execution without turn-by-turn confirmation pauses. |
| **Distill recent corrections into permanent project rules** | [`/learn`](/docs/rules-workflows) | Analyzes session patterns and writes persistent Rules and Skills. |
| **Web research, UI validation, and layout inspection** | `/browser` | Sandboxed Chrome browser subagent for live page interactions. |
| **One-shot countdown timer or recurring background schedule** | [`/schedule`](/docs/sidecars) | Runs instructions in the background on cron schedules. |
| **Quick side query without pausing primary agent work** | `/btw` | Lightweight out-of-band query executed in the background. |

* * *

## Cross-surface compatibility

Public slash commands are supported across Antigravity developer surfaces:

| Surface | Input Method | Navigation & Management |
| :-- | :-- | :-- |
| **Antigravity 2.0 (Desktop & Web)** | Type `/` in the prompt input or select from the command menu. | Model selector dropdown, Artifact review panel, Visual diff viewer. |
| **Antigravity CLI** | Type `/` in the interactive prompt box. | `/agents` panel, Alt+J (switch threads), Ctrl+O (trajectory). |

* * *

## Next steps

Explore related documentation and guides:

*   [Boost deep reasoning (`/boost`)](/docs/boost): Dive deep into the 3-tier multi-agent reasoning hierarchy.
*   [Teamwork agent teams (`/teamwork-preview`)](/docs/teamwork): Learn how collaborative agent teams tackle large-scale migrations.
*   [Implementation plans (`/plan`)](/docs/implementation-plan): Master reviewable planning artifacts and structured workflows.
*   [Rules and workflows (`/learn`)](/docs/rules-workflows): Persist project-wide patterns and conventions.
*   [Sidecars and scheduled tasks (`/schedule`)](/docs/sidecars): Automate routine maintenance with cron expressions.