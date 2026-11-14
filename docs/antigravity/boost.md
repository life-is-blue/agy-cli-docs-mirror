# Boost deep reasoning (/boost)

Available on: Antigravity App, Antigravity CLI

The `/boost` slash command activates an on-demand multi-agent reasoning pipeline designed for challenging software engineering tasks. When standard single-turn coding assistance falls short on complex bugs, race conditions, or intricate refactoring, `/boost` breaks down the problem, delegates focused workstreams to specialized subagents, and independently verifies solutions across iterative rounds.

Note

**Plan availability**: The `/boost` command is available on **paid plans** across the Google Antigravity App and the Antigravity CLI.

* * *

## Overview

Modern software development involves problems spanning a wide spectrum of complexity:

1.  **Everyday engineering**: Interactive feature development, codebase navigation, refactoring, and general programming workflows where speed and versatility shine.
2.  **Deep reasoning tasks**: High-difficulty concurrency bugs, algorithmic optimization, subtle regressions, and multi-file architecture puzzles that benefit from multi-agent exploration and iterative verification.
3.  **Long-horizon campaigns**: Repository-scale migrations, large subsystem builds, and multi-day exploratory research.

`/boost` addresses the crucial middle ground: **interactive, high-intensity developer productivity**. It delivers multi-agent deep reasoning directly within your day-to-day coding sessions without requiring complex setup or prolonged scoping interviews.

* * *

## How Boost works

When you invoke `/boost`, Antigravity initiates a three-phase multi-agent reasoning pipeline that separates task routing from iterative execution and verification:

### Phase 1: Goal and strategy formulation

The primary orchestrator receives your prompt, evaluates whether the task requires implementation (`DeepCoder`) or root-cause analysis (`DeepInvestigator`), and hands your verbatim task and relevant conversation context to a pipeline coordinator.

### Phase 2: Iterative execution and challenge rounds

The pipeline coordinator dispatches specialized workers in isolated subagent contexts:

*   **Initial implementation or investigation**: A first-pass worker explores the codebase, implements a candidate change or traces the root cause, and runs the project’s test suite and edge-case checks.
*   **Improvement rounds**: Follow-up improvement workers review the original requirements independently, attempt to break or find gaps in the prior worker’s output, fix any flaws, and re-run tests.

### Phase 3: Independent verification and delivery

Before presenting the final outcome, the primary orchestrator independently verifies the pipeline’s result:

*   The orchestrator spot-checks the code changes and test record against every requirement in your prompt.
*   If any edge case, limitation, or test failure remains, the orchestrator starts another delegation round with the updated progress context.
*   Once all requirements and tests pass, the orchestrator delivers a concise summary of the verified solution.

* * *

## When to use /boost

For everyday coding and quick questions, prompt the default agent directly. When a task benefits from multiple agents, compare Antigravity’s agent orchestrators and background subagents:

|  | [Subagents](/docs/subagents) | Boost (`/boost`) | [Swarm (`/swarm`)](/docs/swarm) | [Teamwork (`/teamwork`)](/docs/teamwork) |
| :-- | :-- | :-- | :-- | :-- |
| **Best for** | Delegating a focused side task, such as codebase research, browser checks, or a test run | **Hard bugs, race conditions, algorithms, and tricky refactors that need deep reasoning** | Broad tasks that split cleanly across independent files, packages, or investigation tracks | Multi-milestone projects, repository-scale migrations, simulations, and deep research |
| **How agents coordinate** | Each subagent runs in the background and reports back to the agent that started it | **An orchestrator runs an iterative pipeline where workers implement, challenge, fix, and re-verify solutions** | A coordinator splits the task across named workers and a verifier that talk on one shared message board | A `Sentinel` and `Project Orchestrator` run specialized roles through a milestone plan with review gates |
| **How you start** | Automatic delegation or `@subagent` mention | **`/boost <task>` (starts immediately)** | `/swarm <task>` (starts immediately) | `/teamwork <goal>`, followed by a scoping interview |
| **Workspace** | Current workspace (or an isolated branch or working copy when requested) | **Current workspace across isolated subagent contexts** | Current workspace by default, or per-worker working copies for overlapping edits | Dedicated project directory (`~/teamwork_projects/{PROJECT_NAME}`) with exclusive file ownership |
| **Verification** | Parent agent checks the subagent’s reply | **Improvement workers try to break prior attempts and run real tests before the orchestrator spot-checks** | A dedicated `@verifier` worker reviews diffs and runs tests before sign-off | Independent `Critic`, `Challenger`, `Auditor`, and `Success Auditor` gates verify each milestone |
| **Typical horizon** | Seconds to minutes | **Seconds to hours** | Minutes to hours | Hours to days |
| **Plan tier** | All plans | **Paid plans** | Google AI Pro and Ultra | Paid plans |

Use the following guidelines to choose the right approach:

*   **Use [subagents](/docs/subagents) for focused background delegation**: Let your agent delegate a self-contained side task—such as codebase research, browser validation, or a test run—while you keep working in the main thread.
*   **Use `/boost` when the problem is hard rather than broad**: Choose `/boost` for root-cause debugging, race conditions, algorithmic optimization, or tightly coupled refactors where an initial attempt should be challenged, fixed, and verified across multiple rounds.
*   **Use [`/swarm`](/docs/swarm) when the task is broad and divides cleanly**: Choose `/swarm` when work splits into independent pieces across separate files, packages, test suites, or research questions, and you want named workers and a verifier to coordinate on a live message board you can monitor and steer.
*   **Use [`/teamwork`](/docs/teamwork) for long-horizon, multi-milestone projects**: Choose `/teamwork` when a project spans hours or days—such as a repository-wide migration, system simulation, or formal proof—and needs an upfront scoping interview, dedicated project directory, and milestone audit gates.

* * *

## How to use /boost

You can invoke Boost across all Antigravity surfaces.

### Antigravity App

Type `/boost` followed by your task prompt in any conversation turn:

```prompt
/boost Investigate the race condition in the session cache and implement a thread-safe fix with tests.
```

### Antigravity CLI

Type `/boost` directly into the terminal user interface (TUI) prompt box:

```prompt
/boost Optimize the matrix transposition algorithm to use SIMD vectorization and benchmark throughput.
```

* * *

## Key use cases

### Concurrency and race conditions

Use `/boost` to debug multithreaded timing issues, deadlocks, and cache synchronization bugs where reproduction requires careful trace analysis and isolated verification:

```prompt
/boost Reproduce and fix the intermittent deadlock in the connection pool during high connection turnover.
```

### Algorithmic problem solving

Use `/boost` to implement high-performance algorithms, custom data structures, graph traversals, or mathematical routines with rigorous boundary testing:

```prompt
/boost Implement a lock-free ring buffer for streaming telemetry events and write stress tests.
```

### Non-trivial refactoring

Use `/boost` to refactor tightly coupled modules, modernize legacy interfaces, or migrate synchronous APIs to asynchronous patterns across multiple files:

```prompt
/boost Refactor the authentication middleware to use asynchronous token validation without breaking existing routes.
```

### Deep root-cause investigation

Use `/boost` to trace execution paths across unfamiliar or large codebases to isolate the exact origin of an unexpected failure:

```prompt
/boost Trace why HTTP request timeouts spike when batch payload size exceeds 2MB, without modifying code.
```

* * *

## Safety and permissions

Boost respects all standard Antigravity security policies:

*   **Scoped permissions**: Subagents inherit file access rules and command permission policies configured for your active workspace or project.
*   **Interactive approvals**: When a worker proposes a protected terminal command or file edit outside trusted scopes, the authorization prompt surfaces to your interface for confirmation.
*   **Context isolation**: Subagents execute in isolated memory spaces, preventing verbose debug logs and scratch diffs from cluttering your primary chat history.

* * *

## Next steps

Explore related documentation and guides:

*   **[Slash commands catalog](/docs/slash-commands)**: Review all available slash commands across Antigravity surfaces.
*   **[Swarm (`/swarm`)](/docs/swarm)**: Coordinate named workers and a verifier on a shared message board for parallel tasks.
*   **[Teamwork agent teams (`/teamwork`)](/docs/teamwork)**: Learn how collaborative agent teams tackle large-scale migrations.
*   **[Subagents overview](/docs/subagents)**: Learn how asynchronous subagent workers operate in parallel.
*   **[Antigravity CLI reference](/docs/cli/reference)**: Explore terminal keybindings and the command reference for the CLI.