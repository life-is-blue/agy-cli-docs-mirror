# Automation command (/automation)

Available on: Antigravity App

Set up a scheduled background [automation](/docs/sidecars#automations) by describing it to the agent in a conversation, instead of writing `sidecar.json` by hand.

Note

**Surface availability**: `/automation` is available in Antigravity App.

## Overview

Background automations (formerly called Scheduled Tasks) run an agent prompt on a recurring schedule, such as a daily digest, weekly pull request check, or nightly test report. Each run starts a fresh agent conversation with no memory of previous runs.

The `/automation` command has the agent walk you through creating one. You can also start the same flow from the **Automations** tab by selecting **Create with Prompt**, which opens a new conversation with the `/automation` command filled in for you to send. The agent:

*   **Asks for a schedule**: you choose a cadence, day, and time. The agent always pins the schedule to an IANA timezone with `CRON_TZ=<zone>`, using the zone or city you mention, or your computer’s timezone.
*   **Writes a self-contained prompt**: it refines what you want the task to do into instructions that work without any earlier conversation.
*   **Creates the automation**: it saves the automation to `~/.gemini/config/sidecars/<automation-id>/sidecar.json`. New automations start under **Paused** in the **Automations** tab until you turn them on.
*   **Sets up permissions now or later**: if you choose now, it runs the task in the current conversation and records the exact permissions the run needed.
*   **Summarizes the automation**: it lists the schedule, task, and permissions, with an **Open Automations Dashboard** button where you turn the automation on.

Automations run on Flash by default. You can choose Flash Lite, Flash, or Pro when you create or edit an automation in the **Automations** tab.

## Launch `/automation`

Start `/automation` from the conversation composer in either of the following ways:

*   **With an inline prompt**: type `/automation` followed by what the automation should do and when it should run:
    
    ```prompt
    /automation every Monday at 9am Pacific time, check my open pull requests and list any with failing checks
    ```
    
*   **Guided setup**: run `/automation` on its own, or select **Create with Prompt** in the **Automations** tab and send the pre-filled command. The agent then asks for each detail:
    
    ```prompt
    /automation
    ```
    

## How `/automation` works

The agent creates the automation through a short question-and-answer flow in the conversation:

1.  **Choose a cadence**
    
    The agent asks how often the automation should run: **Hourly**, **Daily**, **Weekly**, or a **Custom cron schedule**.
    
2.  **Choose the day and time**
    
    The agent asks for the day and time, then confirms the schedule with its timezone. It converts your answer into a five-field cron expression prefixed with `CRON_TZ=<IANA zone>`, such as `CRON_TZ=America/Los_Angeles 0 9 * * 1`.
    
3.  **Describe the task**
    
    The agent asks what the automation should do and refines your answer into a self-contained prompt that states the goal, where to look, and what to report:
    
4.  **Set permissions now or later**
    
    The agent creates the automation. It then asks whether to run a test now to configure the automation’s permissions. If you choose the test run, the agent runs the task once in the current conversation and records the exact permissions the run needed in the automation’s `agent_permissions`. If you decline, you can review permissions and turn the automation on in the Automations tab.
    
    Note
    
    Unattended runs automatically deny anything that would normally ask for your approval, which is why the test run matters. The agent is instructed to write only scoped grants, such as `command(gh issue list)`, `read_file(/abs/path)`, `write_file(/abs/path)`, `mcp(<server>/<tool>)`, or `read_url(github.com)`, rather than bare or wildcard grants. Review the grants before you turn the automation on.
    
5.  **Review the summary and open the Automations tab**
    
    The agent summarizes the automation: the name and ID, schedule, task, and any permissions granted. It also shows an **Open Automations Dashboard** button so you can turn the automation on:
    

To start using the automation, open the **Automations** tab, where it’s listed under **Paused**, review its permissions, and turn it on. Once it’s turned on, you can also start a run right away with **Run Now**.

For the `sidecar.json` fields an automation uses, including `arguments` and `agent_permissions`, refer to [Automations](/docs/sidecars#automations).

## Example prompts

The following prompts show common ways to use `/automation`:

*   **Weekly pull request check**:
    
    ```prompt
    /automation every Monday at 9am Pacific time, check my open pull requests and list any with failing checks
    ```
    
*   **Weekday issue triage**:
    
    ```prompt
    /automation every weekday at 9am in New York, triage new GitHub issues and label them by severity
    ```
    
*   **Nightly test report**:
    
    ```prompt
    /automation every night at midnight UTC, run the integration test suite and summarize any failures
    ```
    

## `/automation` compared with `/schedule`

Both `/automation` and [`/schedule`](/docs/commands/schedule) run agent work on a schedule, but at different scopes:

|  | `/automation` | [`/schedule`](/docs/commands/schedule) |
| :-- | :-- | :-- |
| **Best for** | Recurring jobs such as daily reports, nightly maintenance, and triage | Timers, CI polling, and check-ins during a task |
| **Surfaces** | Antigravity App | Antigravity App, Antigravity CLI, and Antigravity IDE |
| **Schedule** | Cron expression pinned with `CRON_TZ=<IANA zone>` | One-time timer or cron loop |
| **Lifetime** | Persists across sessions and restarts until you turn it off | Current conversation |
| **Context** | Starts a fresh agent conversation on each run | Wakes the existing agent with its full conversation history |
| **Where it lives** | `~/.gemini/config/sidecars/<automation-id>/sidecar.json`, managed in the **Automations** tab | A tool call the agent makes for you |
| **Permissions** | Scoped `agent_permissions` recorded after a test run | The current conversation’s permissions |

Use `/automation` for unattended work that should keep running when no conversation is open. Use `/schedule` when you want the agent in your current conversation to wake up after a timer or poll an operation while you keep working.

## Next steps

Explore related documentation:

*   [Sidecars](/docs/sidecars): Learn how automations and other sidecars are configured, including `arguments` and `agent_permissions`.
*   [Schedule command (`/schedule`)](/docs/commands/schedule): Set one-time timers and recurring schedules within a conversation.
*   [Permissions](/docs/permissions): Learn how access grants work.
*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.