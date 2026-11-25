# How AI agents work

A plain chat model can only suggest code in a reply. An **AI agent** pairs a reasoning model with tools: reading files, editing code, running terminal commands, and inspecting a live browser. That lets the agent observe real feedback and iterate until the task passes.

* * *

## The agent loop

When you give Antigravity a task, the agent works through a repeating loop rather than guessing the whole answer at once:

1.  **The agent inspects context.** It reads relevant files, searches symbols, and checks your workspace rules and prompt constraints.
2.  **The agent plans the next step.** It chooses which files to change or which diagnostic command to run next.
3.  **The agent calls a tool.** It edits a file, runs a test command, queries an MCP server, or opens a page in the browser.
4.  **The agent reads the result.** It checks compiler diagnostics, test assertions, console output, or screenshots from that tool call.
5.  **The agent iterates or finishes.** It fixes any failures and repeats until verification passes, then summarizes the diff for your review.

### Example: one bug fix through the loop

Here is how a single billing-date bug moves through those five steps:

1.  **Inspect**: The agent reads `src/billing/renewal.ts` and `tests/renewal.test.ts` to trace where renewal dates shift.
2.  **Plan**: It spots a local-midnight `Date` call that breaks across daylight saving transitions.
3.  **Call tools**: It updates the calculation to UTC and runs `npm test -- tests/renewal.test.ts`.
4.  **Read result**: One edge-case test fails on February 29 leap-year rollover.
5.  **Iterate and finish**: It clamps month-end dates, re-runs the tests until they pass, and hands back the diff.

* * *

## Tools, MCP, and hooks

Built-in tools cover local files, code search, terminal commands, and browser checks. For external context like issue trackers, databases, or cloud docs, the agent connects through the [Model Context Protocol (MCP)](/docs/mcp):

*   **Standardized external tools**: MCP lets agents discover and call external tools without custom glue code for each service.
*   **Global and workspace configs**: Configure global MCP servers in `~/.gemini/config/mcp_config.json` or project-scoped servers in `.agents/mcp_config.json`.
*   **Curated plugin bundles**: Install pre-built bundles of skills, MCP servers, rules, agents, and hooks from the [Marketplace](/docs/marketplace) or [Build with Google](/docs/build-with-google).
*   **Deterministic lifecycle hooks**: Configure [Hooks](/docs/hooks) in `.agents/hooks.json` or `~/.gemini/config/hooks.json` to run shell scripts on `PreToolUse` and `PostToolUse`. Use them to auto-format files or block risky commands.

* * *

## Choose an agent pattern

Most everyday tasks run best in a single conversation. Reach for specialized orchestrators when work is unusually hard, divides cleanly across files, or needs independent review:

| Pattern | How it works | Best for | Surfaces | Plans |
| --- | --- | --- | --- | --- |
| **Single agent** | One conversation reads, edits, and verifies sequentially. | Focused bug fixes, single-module edits, and quick prototypes. | All surfaces | All plans |
| **[Orchestrator](/docs/models#orchestrator)** | Pairs a planner model with a faster executor model inside one conversation. | Everyday feature work and multi-file debugging with lower latency. | App, CLI | Paid Pro, Ultra, Enterprise |
| **[Subagents](/docs/subagents) (built-in & custom)** | Main agent delegates scoped tasks (`research`, `browser`, or `.agents/agents/*.md`) to isolated child sessions. | Deep codebase research, browser checks, or reusable audit roles. | App, CLI, IDE | All plans |
| **[Swarm (`/swarm`)](/docs/swarm)** | A coordinator splits work across named workers and a `@verifier` on a shared live board. | Broad tasks that divide cleanly across separate files or packages. | App, CLI | All plans _(Preview)_ |
| **[Dynamic workflows (`/run-workflow`)](/docs/dynamic-workflows)** | Agent writes and runs a Python script coordinating `parallel()` and `pipeline()` agents. | Fan-out audits across many files or repeatable staged pipelines. | App, CLI | All plans |
| **[Boost (`/boost`)](/docs/boost)** | Multi-agent pipeline where workers implement, challenge, fix, and re-verify solutions. | Hard bugs, race conditions, and complex algorithms. | App, CLI | Paid plans |
| **[Teamwork (`/teamwork`)](/docs/teamwork)** | Scoping interview followed by milestone orchestration (`Critic`, `Challenger`, `Auditor`) in `~/teamwork_projects/`. | Multi-milestone migrations, simulations, and multi-day projects. | App, CLI | Paid plans |

Parallel agents and quota

Each parallel worker runs in its own fresh context window, preventing context bloat. Idle `/swarm` workers sleep on the board without using tokens. Active parallel workers still consume model quota faster than a single conversation.

Compare a focused single-agent prompt with a parallel `/swarm` prompt you can try in any repository:

```prompt
Find all TODO and FIXME comments in this repository, group them by directory, and list the top three with the highest bug risk without editing any files.
```

```prompt
/swarm Audit this repository's tests and docs in parallel: have @test-audit list untested edge cases, @docs-audit check README commands against project scripts, and @verifier cross-check both reports on the board.
```

* * *

## Where you stay in control

Agents do the heavy lifting, while you own the architecture and release bar:

*   **Define boundaries up front** with clear prompts, [Rules](/docs/rules), [Hooks](/docs/hooks), and [Permissions](/docs/permissions).
*   **Review plans and diffs** before accepting edits or running sensitive commands.
*   **Keep verification objective** by anchoring tasks to automated tests and visual checks.

* * *

## Next steps

[

Next in Learn

Verification and guardrails

Learn how to combine tests, live browser checks, hooks, and sandboxing to keep agent edits safe.

](/docs/learn/verification-and-guardrails/)[

Multi-agent

Swarm (/swarm)

Run parallel named workers and an independent verifier on a shared board.

](/docs/swarm/)[

Build guide

Build a playable 3D browser world

Watch four parallel swarm workers and /browser build and verify a live Three.js app.

](/docs/learn/build-3d-browser-world/)