# Compact command (/compact)

Available on: Antigravity App, Antigravity CLI

Summarize your conversation so far into a structured checkpoint so the agent continues from a smaller context window, without starting a new conversation or waiting for automatic compaction.

## Overview

As a conversation grows, every file read, command output, and intermediate turn accumulates in the model’s context window. Antigravity automatically compacts older turns when a conversation approaches the model’s context limit, and `/compact` lets you trigger that same checkpointing step on demand—for example, right after finishing codebase exploration or completing a milestone:

*   **Frees up context on your schedule**: replaces earlier conversation turns with a concise continuation checkpoint before stale logs or exploratory searches crowd out your next task.
*   **Preserves working state**: retains key decisions, file paths, errors and fixes, attached media and files, active background tasks, live subagents, and session [artifacts](/docs/artifacts).
*   **Makes no workspace changes**: compaction calls no tools and modifies no files on disk.
*   **Supports compact-and-stop or compact-and-continue**: run `/compact` on its own to compact and pause, or pass instructions after `/compact` to compact first and immediately continue working.

## Run `/compact`

You can run `/compact` by itself or with follow-up instructions.

### Compact and stop

To summarize the conversation so far and end the turn immediately, send bare `/compact`:

```text
/compact
```

Antigravity writes the checkpoint summary and stops without calling the agent again, so your next message is the first to run on the compacted context.

### Compact and continue

To summarize the conversation first and then have the agent act on your next request in the same turn, add your message after `/compact`:

```prompt
/compact Keep the OAuth token refresh findings, and now add unit tests for the new middleware.
```

Your text after `/compact` guides the summarization step—so you can tell it which findings or constraints to emphasize—and is then answered by the agent using the newly compacted context.

Note

Only a leading `/compact` triggers compaction. If `/compact` appears after other text or attachments (for example, inside a pasted log or `"explain /compact"`), Antigravity treats it as normal prompt text and doesn’t compact the conversation.

## Surface behavior

### Antigravity App

In the Antigravity App (`v2.21.0+`), type `/compact` or `/compact <message>` in the composer and press Enter:

```text
/compact
```

*   **Live status**: while the checkpoint summary is being generated, the status line beneath your message shows **Compacting** (with an elapsed timer such as `Compacting · 45s` on longer conversations).
*   **Cancel**: click **Stop** while compaction is running to cancel it. Cancelled compactions don’t write a checkpoint, leaving your existing conversation context unchanged.

### Antigravity CLI

In the Antigravity CLI (`v1.2.15+`), type `/compact` or `/compact <message>` in the prompt box and press Enter:

```text
/compact
```

*   **Live progress and cancel**: while compaction runs, the pending line displays `Compacting conversation… (<elapsed> · esc to cancel)`. Press Esc / Ctrl + C to cancel; the CLI prints `Compaction cancelled. Conversation was not compacted.` and leaves your context unchanged.
    
*   **Compaction marker and token savings**: when compaction finishes, the transcript renders a `Conversation compacted` divider rule followed by a summary line:
    
    ```text
    ─────────────────────────── Conversation compacted ────────────────────────────
       142 steps summarized · context 182.4k → ~31.2k (5.1k summary) · took 48s
    ```
    
    The post-compaction estimate (`~31.2k` in this example) includes both the new checkpoint summary and the non-shrinkable system overhead—system instructions, tool definitions, and loaded customizations—so it matches what [`/context`](/docs/cli/commands/context) reports.
    
*   **Empty conversations**: if you run bare `/compact` before the agent has completed at least one response, the CLI prints `Nothing to compact yet.` without making a model request. Running `/compact <message>` before any response sends `<message>` to the agent normally.
    
*   **Inspect updated usage**: run [`/context`](/docs/cli/commands/context) after compacting to inspect your updated context window grid, free space, and **Checkpoints** count.
    
*   **Headless mode**: `/compact` also works when resuming a conversation in [headless mode](/docs/cli/headless) (for example, `agy -c -p "/compact Now run the integration test suite"`), unless `--disable-slash-commands` (or `"disableSlashCommands": true` in `settings.json`) is set.

## What compaction preserves

When `/compact` runs, Antigravity replaces older raw steps in the active model context with a checkpoint that combines a structured summary and deterministic session state:

1.  **Structured continuation summary**: captures your task overview and success criteria, completed progress (file paths, commands run, and verification outcomes), key technical findings and decisions, errors encountered and how they were fixed (including approaches that were tried and abandoned), active context, remaining next steps, and standing rules or constraints.
2.  **Deterministic session snapshots**: preserves recent user requests and attached images, PDFs, and files, active background tasks, live [subagents](/docs/subagents), and session [artifacts](/docs/artifacts) (such as implementation plans and walkthroughs) alongside the prose summary.
3.  **Workspace and customizations**: your files on disk and your loaded [rules](/docs/rules), [skills](/docs/skills), tools, and [MCP servers](/docs/mcp) remain active as usual.

Earlier messages stay visible in your conversation scrollback and saved session history; compaction only shortens what’s sent in future model requests.

## Choose the right context command

Use `/compact` alongside Antigravity’s other session and context tools depending on what you want to keep:

| Goal | Command or action | What happens to context |
| --- | --- | --- |
| Keep working on the same task with a smaller context window | `/compact [message]` | Summarizes earlier turns into a checkpoint and continues in the same conversation. |
| Ask a quick tangential question without adding to history | [`/btw <question>`](/docs/commands/btw) | Answers in a read-only fork so neither the question nor its tool calls enter the main conversation. |
| Inspect current token usage by category (CLI) | [`/context`](/docs/cli/commands/context) | Opens the Context Usage grid, token breakdown, and checkpoint count without modifying history. |
| Undo a wrong turn or failed tangent | `/rewind` (CLI) or **Revert** on an earlier prompt (App) | Rolls the conversation back to an earlier message instead of keeping failed attempts in context. |
| Try an alternative approach in parallel | `/fork` (CLI) or **Fork** (App) | Clones the conversation up to that point into a separate session. |
| Switch to a completely unrelated task | `/clear` / `/new` (CLI) or **New Conversation** (App) | Starts a fresh conversation with an empty history. |

## Next steps

*   **[Context windows and tokens](/docs/learn/context-and-tokens)**: learn how tokens work, why focused context outperforms dumping full repos, and when to compact.
*   **[Context command (`/context`)](/docs/cli/commands/context)**: visualize how your conversation consumes the model’s context window in the Antigravity CLI.
*   **[Side question command (`/btw`)](/docs/commands/btw)**: ask quick questions without adding turns to your active conversation.
*   **[Managing conversations](/docs/cli/conversations)**: resume, fork, and organize CLI sessions.
*   **[Slash commands overview](/docs/slash-commands)**: browse all cross-surface slash commands in Google Antigravity.
*   **[CLI commands](/docs/cli/reference)**: view all CLI slash commands, keyboard shortcuts, and flags.