# Side question command (/btw)

Available on: Antigravity App, Antigravity CLI

Use `/btw` to ask a quick question while the agent keeps working. The side question can read files and search your workspace to check its answer, and nothing it does is added to your main conversation.

## Antigravity App

In the Antigravity App, /btw opens a Side Question tab that searches the code, reads two files, and answers while the main task keeps running. Sped-up parts show a speed badge.

## Antigravity CLI

In the Antigravity CLI, the /btw card shows each tool call as it runs, then a Called 4 tools summary and the answer, while the main task keeps running. Sped-up parts show a speed badge.

## Overview

During a long task, you often need a quick fact: where a function is defined, which value a setting uses, or what the agent decided earlier. Asking in the main conversation interrupts the agent and adds turns that every later turn pays for. A side question avoids both:

*   **Knows your conversation**: it starts from everything said and done in the conversation so far.
*   **Checks your code**: it can read files, search your workspace, and run read-only commands instead of answering from memory.
*   **Runs alongside the agent**: you can ask while the agent is responding, running tests, or using long-running tools.
*   **Keeps your history clean**: the question, its tool calls, and its answer stay out of the main conversation.

## How side questions work

When you send `/btw`, Antigravity does the following:

1.  **Forks the conversation**: Antigravity creates a new conversation that starts with a copy of your conversation history. The main agent keeps running, and nothing in the fork is written back to the main conversation.
2.  **Asks the model to stay read-only**: the model is told it’s answering a side question. It can read files, search code, and read external context, but it doesn’t edit files, change your workspace or external state, start subagents or workflows, or schedule background tasks unless you explicitly ask it to.
3.  **Keeps your settings**: the fork uses the same model, [permission settings](/docs/permissions), [terminal sandbox](/docs/sandbox), MCP servers, and administrator policies as your main conversation. Read-only is an instruction to the model on top of these controls, not a separate sandbox, so if you ask a side question to make a change, such as `/btw fix that typo`, it can do so within your permissions.
4.  **Runs one agentic turn**: the model calls tools until it finishes its answer or you stop it. Like a normal turn, it has no time limit.

Side questions differ by surface:

| Behavior | Antigravity App | Antigravity CLI |
| :-- | :-- | :-- |
| Where the answer appears | A **Side Question** tab in the side panel. | A `/btw` card above the prompt box. |
| Tool calls | Appear as steps in the tab, like in a conversation. | Appear as live lines on the card, then one summary line. |
| Tool calls that need approval | The approval request appears in the tab. | Denied automatically, because the card can’t show approval prompts. |
| Follow-up questions | Send more messages in the tab. | Not supported. Each `/btw` starts a new fork. |
| Keep or discard | Promote the side question to a conversation, or delete it. | Dismiss the card. Answers stay in the card’s history for the session. |

## Ask a side question

### Antigravity App

In the Antigravity App (`v2.32.0+`), each side question opens as a **Side Question** tab in the [side panel](/docs/side-panel).

1.  In a conversation where you’ve already sent at least one message, type `/btw` followed by your question, and then press Enter:
    
    ```text
    /btw Where's the retry logic for API calls, and what's the max retry count?
    ```
    
    A **Side Question** tab opens with a short title based on your question. Its first message shows **Started from** or **Started during** and the message in the main conversation that the side question branched from. Tool calls, such as searches and file reads, appear as steps. When the side question finishes, the steps collapse into a **Worked for** summary that you can expand.
    
2.  Optional: To ask a follow-up, type in the composer at the bottom of the tab. Follow-ups continue the side question, not the main conversation.
    

You can also start a side question in these ways:

*   **New tab**: Click **New Tab** (**+**) in the side panel, and then click **Side Question**. This option is available once the main conversation has a message.
*   **Selected text**: Select text in the conversation, and then click **Ask /btw** to quote it into a new side question.

To stop a running side question, click **Stop Side Question** in the tab header. If a tool call needs your approval, the request appears in the tab, the same as in a conversation.

Note

In remote conversations and in Antigravity App versions earlier than `v2.32.0`, side questions can’t call tools. The answer opens in a floating **Side Question** panel above the composer instead of a tab.

### Antigravity CLI

In the Antigravity CLI (`v1.5.0+`), type `/btw` followed by your question in the prompt box. If you haven’t started a conversation yet, the CLI creates one:

```text
/btw Which port and timeouts does server.go configure? Read the file to check.
```

A `/btw` card opens above the prompt box while the main conversation continues. The card shows each tool call as it runs (`✓` done, `⋯` running, `✗` failed). When the answer is ready, the tool calls collapse into a summary line, such as `Called 4 tools (3 read_file, 1 run_command)`.

Keep the following in mind:

*   **One question per card**: each `/btw` starts a fresh fork of the main conversation and doesn’t see earlier side questions.
*   **One at a time**: if you ask another side question before the first finishes, the CLI asks you to wait or press Esc to cancel the running one.
*   **No approval prompts**: a tool call that would ask for your approval, such as a shell command that isn’t already allowed, is denied. If a side question still ends up waiting for an approval, it stops and tells you to ask in the main conversation instead.
*   **Interactive sessions only**: `/btw` isn’t available in headless mode (`-p` or `--print`) or in [remote agent](/docs/remote-agents) sessions.

Tip

Side questions often search with read-only shell commands such as `grep` or `find`. If those commands need approval in your setup, the card denies them and the side question can’t finish its search. To let side questions run them, add allow rules such as `command(grep)` and `command(find)` to your [permission settings](/docs/permissions).

## Manage side questions

In the Antigravity App, side questions are saved with the conversation until you delete them. In the Antigravity CLI, `/btw` answers are kept for the current session.

### Antigravity App

#### Reopen or rename a side question

Closing a **Side Question** tab doesn’t delete the side question. To reopen it, do either of the following:

*   In the [**Overview** panel](/docs/side-panel#the-overview-panel), click the side question in the **Side Questions** section.
*   Click **New Tab** (**+**) in the side panel and search for the side question. Matches appear under **Side Questions**.

To rename a side question, double-click its name in the tab header, type a new name, and then press Enter.

#### Promote or delete a side question

To turn a side question into a full conversation, wait for it to finish, and then click **Promote to Conversation** in the tab header. If you’re asked where to create the conversation, such as the current folder or a new worktree, choose one. Antigravity opens the new conversation and closes the side question tab. You can’t promote a side question that’s still running or one that you asked in a subagent’s conversation.

To permanently delete a side question, click **Delete Side Question** in the tab header, and then click **Delete** to confirm. You can’t undo this action.

### Antigravity CLI

#### Reopen previous `/btw` answers

To reopen the most recent `/btw` card without asking a new question, run `/btw` with no arguments:

```text
/btw
```

Note

If you haven’t asked any `/btw` questions in the current session yet, running bare `/btw` displays `Usage: /btw <question>`.

#### Card navigation controls

When a `/btw` card is visible in the CLI, use the following keyboard shortcuts:

| Key | Action |
| :-- | :-- |
| Tab | Expand a truncated answer or collapse an expanded card. |
| ↑ / ↓ | Scroll up or down by one line inside an expanded card when the answer exceeds the viewport height. Otherwise, these keys keep their usual prompt-history behavior. |
| PgUp / PgDn | Scroll up or down by one page inside an expanded card. |
| ← / → | Cycle through previous and next `/btw` responses in the current session. |
| Esc | Dismiss the `/btw` card, or cancel a side question that’s still running. |
| Enter | Dismiss the `/btw` card, or cancel a running side question, when the prompt box is empty. If you’ve typed a prompt, Enter submits it as usual. |

#### Copy a `/btw` response to the clipboard

To copy the latest `/btw` answer instead of the main agent’s last response, run:

```text
/copy btw
```

The CLI copies the full Markdown of the answer on screen, or of the most recent answer if you’ve dismissed the card, even when the card is collapsed or scrolled.

## Next steps

*   **[Context command (`/context`)](/docs/cli/commands/context)**: visualize how your main conversation consumes the model’s context window.
*   **[Side panel and Overview panel](/docs/side-panel)**: open side questions and other tabs next to your conversation in the Antigravity App.
*   **[Permissions](/docs/permissions)**: control which tool calls the agent, and any side question, can make without asking.
*   **[Slash commands overview](/docs/slash-commands)**: browse all cross-surface slash commands in Google Antigravity.
*   **[CLI reference](/docs/cli/reference)**: view all available CLI slash commands and keyboard shortcuts.