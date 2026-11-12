# Schedule command (/schedule)

Available on: Antigravity App, Antigravity CLI, Antigravity IDE

Set a one-time timer or a recurring cron schedule that wakes the agent with an instruction, without blocking the conversation while it waits.

## Overview

Some tasks need the agent to come back later: check whether a CI run finished, poll a deployment every few minutes, or send you a status summary at a set time. The `/schedule` command asks the agent to create that timer or schedule using its built-in `schedule` tool.

A schedule runs as a background task in the current conversation:

*   **Non-blocking**: the agent ends its turn after creating the schedule rather than idling in a shell `sleep`, so you can keep chatting or let it work on other steps.
*   **Wake-up prompt**: when the timer fires or the cron triggers, the agent receives your instruction as a high-priority notification and acts on it.
*   **Conversation-scoped**: timers and schedules belong to the conversation that created them. For standing jobs that outlive a session, use a persistent [sidecar](/docs/sidecars) or [automation](/docs/commands/automation) instead.

## Create a schedule

Type `/schedule` followed by when the agent should wake up and what it should do. The agent interprets natural language, a duration, or a five-field cron expression and fills in the tool parameters for you.

### Antigravity App

Type the command in the composer:

```prompt
/schedule in 10 minutes, check whether the deploy to staging finished and summarize any errors
```

The schedule appears in the conversation as a **Timed** or **Scheduled** step whose status updates from **Pending** to **Fired**, or from **Active** to **Completed**, as it runs.

### Antigravity CLI

Type the command in the interactive prompt:

```prompt
/schedule every weekday at 9am, run git fetch, list stale local branches, and summarize open PR reviews
```

Scheduled timers and recurring jobs appear alongside background shell commands in the `/tasks` panel and in the status line’s task count.

## Schedule types

The `schedule` tool supports two mutually exclusive modes. The agent picks the mode from your instruction, but you can name the parameters directly if you want precise control.

### One-shot timers

A timer waits for a fixed duration and then fires once:

| Parameter | Description |
| :-- | :-- |
| `DurationSeconds` | Seconds to wait before firing. |
| `Prompt` | Instruction delivered to the agent when the timer fires. |
| `TimerCondition` | Optional early-cancel condition: `never` (default), `any` (any incoming message), or the ID of a specific subagent or background task. |

Timers are useful for “check back in N minutes” workflows. With a `TimerCondition`, the timer is cancelled early when a matching message arrives, such as a subagent finishing, and that message itself wakes the agent, so it doesn’t wait the full duration unnecessarily.

```text
/schedule wait up to 5 minutes for the test subagent to report back, then check its results either way
```

### Recurring cron schedules

A cron schedule fires repeatedly on a standard five-field cron expression:

| Parameter | Description |
| :-- | :-- |
| `CronExpression` | Standard five-field cron expression, such as `*/5 * * * *` for every five minutes. |
| `Prompt` | Instruction delivered on each trigger, suffixed with the iteration number. |
| `MaxIterations` | Optional cap on the number of triggers. Defaults to unlimited. |
| `IsDaemon` | Optional. When `true`, the schedule keeps firing after the agent’s current task is done. |

Set `IsDaemon` only for an independent standing job. Non-daemon schedules are tied to the task that created them. When `MaxIterations` is reached, the agent is notified that the schedule completed.

```prompt
/schedule every 2 minutes for the next 30 minutes, poll the CI status for PR #482 and tell me when it goes green
```

## Manage active schedules

You can inspect and cancel schedules from either surface:

*   **Ask the agent**: tell the agent to list or cancel its schedules. It uses its task manager tool to show active timers and jobs and to kill the one you name.
*   **CLI task panel**: run `/tasks` to open the Task Manager. Use the arrow keys to select a timer or recurring job, press k to kill it, press x to remove finished entries, and press Enter for details.

## `/schedule` compared with Automations

`/schedule` runs work while you’re still working in the current conversation. For unattended, recurring jobs that should keep running when no conversation is open, use [`/automation`](/docs/commands/automation) to have the agent set up a background automation. For a side-by-side comparison, refer to [`/automation` compared with `/schedule`](/docs/commands/automation#automation-compared-with-schedule).

## Next steps

Explore related documentation:

*   [Automation command (`/automation`)](/docs/commands/automation): Set up a persistent background automation with the agent’s help.
*   [Sidecars](/docs/sidecars): Learn how automations and other sidecars are configured.
*   [Goal command (`/goal`)](/docs/commands/goal): Combine timers with long-running autonomous goals.
*   [Subagents](/docs/subagents): Learn about the background work that a `TimerCondition` can wait on.
*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.