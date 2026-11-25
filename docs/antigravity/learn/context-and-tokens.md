# Context windows and tokens

Every language model reads and writes text in chunks called **tokens**. Each model has a maximum **context window** it can hold at once. Even with a large window, clean context makes replies faster, more accurate, and lighter on quota.

* * *

## What is a token?

Models split text and code into subword units before processing them:

*   In English prose, 1 token is roughly 4 characters or three-quarters of a word.
*   In source code, indentation, brackets, and punctuation often count as separate tokens. A 100-line TypeScript file usually uses 400 to 800 tokens.
*   Every turn shares one context window across system instructions, built-in tools, MCP tool schemas, and active rules. Conversation history, file contents, command outputs, and model reasoning tokens share that same window.

Antigravity reduces background overhead automatically. Connected [MCP](/docs/mcp) tools are **lazy-loaded** by default so full parameter schemas stay on disk until needed. Always-on [rules](/docs/rules) share a **20,000-token budget**, automatically demoting the largest files to on-demand pointers if exceeded.

For exact token-counting behavior on Gemini models, see [Understand and count tokens](https://ai.google.dev/gemini-api/docs/tokens).

* * *

## Why stuffing the context backfires

Dumping dozens of unrelated files into a single prompt rarely improves quality:

*   **Diluted attention**: Irrelevant logs, old stack traces, and unrelated files compete with the lines that matter for your edit.
*   **Higher latency and quota use**: Larger prompts take longer to process on every turn and consume more model quota.
*   **Stale assumptions**: Long threads accumulate outdated file snapshots and abandoned ideas that can confuse later turns.

* * *

## Active working set vs. on-demand search

Treat context like RAM, not a hard drive. Keep a small active working set and let the agent fetch reference code only when needed.

| Context layer | What belongs here | How to manage it |
| --- | --- | --- |
| **Active working set** | Target files, failing test output, and specs for the current task. | Reference files with [@-mentions](/docs/at-mentions) or paste only the failing error lines. |
| **Reference codebase** | Neighboring packages, utilities, and documentation. | Let the agent search and read files on demand instead of pasting whole folders. |
| **Durable rules** | Repo conventions and repeatable workflows. | Store in [Rules](/docs/rules) and [Skills](/docs/skills) rather than long chat intros. |

[@-mentions](/docs/at-mentions) pass the file or folder **path**, not its raw contents, so the agent reads only what it needs. In the Antigravity App, use **Quote** to send exact selected lines (Cmd + L on macOS; Ctrl + L on Windows and Linux).

* * *

## Keep long sessions sharp in Antigravity

Antigravity compacts older turns automatically as a thread nears the context limit. You can also manage context directly on both surfaces:

### Antigravity App

*   **Mention and quote**: Type `@` to reference files, folders, rules, or past conversations. Select text in a response, diff, or artifact and click **Quote** (Cmd + L or Ctrl + L).
*   **Compact on demand**: Run [`/compact`](/docs/commands/compact) (`v2.21.0+`) to checkpoint earlier turns. Pass `/compact <focus>` to summarize and continue in one turn.
*   **Ask side questions**: Run [`/btw`](/docs/commands/btw) (`v2.32.0+` with tools) to open a read-only **Side Question** tab. Its lookups stay out of your main thread.
*   **Revert or fork**: Click **Revert** on an earlier prompt to drop a dead end. Click **Fork** to test another approach in a new thread.

### Antigravity CLI

*   **Inspect token usage**: Run [`/context`](/docs/cli/commands/context) to open the visual **Context Usage** grid. Check how tokens split across messages, tool calls, rules, skills, MCP tools, and checkpoints.
*   **Mention paths**: Type `@` to fuzzy-search workspace files and directories without pasting their contents.
*   **Compact on demand**: Run [`/compact`](/docs/commands/compact) (`v1.2.15+`) or `/compact <focus>` to shrink context and view the token savings summary.
*   **Ask side questions**: Run [`/btw`](/docs/commands/btw) (`v1.5.0+`) for a read-only lookup above the prompt box that never enters main history.
*   **Rewind, fork, or clear**: Run `/rewind` (`/undo`) to roll back a wrong turn. Run `/fork` to branch an experiment, or `/clear` (`/new`) between unrelated tasks.

### Choose the right context tool

| Symptom or goal | Antigravity tool | What happens to context |
| --- | --- | --- |
| Long thread after exploration or a milestone | [`/compact <focus>`](/docs/commands/compact) | Summarizes earlier turns into a checkpoint and continues with your focus. |
| Quick tangential question while the agent works | [`/btw <question>`](/docs/commands/btw) | Answers in a read-only fork without adding to main history. |
| Unexpectedly high token usage (CLI) | [`/context`](/docs/cli/commands/context) | Breaks down token share across messages, tools, rules, and MCP servers. |
| Dead-end debugging tangent | `/rewind` (CLI) or **Revert** (App) | Drops failed turns so stale assumptions do not linger. |
| Switching to an unrelated task | `/clear` (CLI) or **New Conversation** (App) | Starts a clean thread with empty history. |
| Multi-module task across separate files | Subagents or [`/swarm`](/docs/swarm) | Gives each worker a fresh context focused only on its own files. |

Run compact-and-continue right after finishing codebase exploration:

```prompt
/compact Keep the key architecture decisions, target file paths, and failing test names, and now implement the next step.
```

Trim noisy logs and unused MCP servers

Run targeted tests (one test file or `--bail`) so passing logs do not flood your context. Disable unused MCP servers in **Customizations** > **Installed** (App) or `/mcp` (CLI). Reserve `"eager": true` for tools you call on nearly every turn.

* * *

## Next steps

[

Next in Learn

How AI agents work

Understand the agent loop, tool calling, MCP, and multi-agent coordination.

](/docs/learn/how-agents-work/)[

Command

Compact (/compact)

Summarize conversation history to reclaim context space during long sessions.

](/docs/commands/compact/)[

Antigravity

Mentions and quoting

Reference specific files, folders, and quoted passages directly inside your prompt.

](/docs/at-mentions/)