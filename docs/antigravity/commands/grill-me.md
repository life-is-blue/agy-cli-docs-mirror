# Grill me command (/grill-me)

Available on: Antigravity App, Antigravity CLI

Have the agent interview you about a task before it starts work. With `/grill-me`, the agent asks one question at a time and recommends an answer for each. It explores your codebase instead of asking you anything the code can answer, and keeps going until you both share the same understanding of the task.

## Overview

A short request such as “add rate limiting” leaves many decisions open: which limits apply to which users, where request counts are stored, and what the API returns when a client is throttled. Without more detail, the agent fills those gaps with its own assumptions, which might not match what you had in mind.

The `/grill-me` command asks the agent to settle those decisions with you before it starts work. The interview changes only how the agent gathers requirements. Your [tool permissions](/docs/permissions) still apply, so you might be asked to approve commands that the agent runs while it explores.

## Start an interview

Type `/grill-me` followed by the task you want to discuss. Describe the outcome you want; the interview fills in the details.

### Antigravity App

Type the command in the message box:

```text
/grill-me Add per-user rate limiting to the bookmarks API
```

Each question appears in a card above the message box, with the agent’s recommended answer listed first:

![A /grill-me question in the Antigravity App, shown in a card above the message box, asking whether rate limits should be tiered by plan and what limits to use, with the recommended answer first, an Other field with Skip and Submit buttons, and a close button at the top right](/assets/image/docs/commands/grill-me-app-question.png)

Select an answer, or type your own in **Other (write your answer)**, and then click **Submit**. Click **Skip** to skip the question, or click the close button (**X**) at the top right of the card to cancel the questionnaire and stop the agent.

The message box stays available while a question is open, so you can type a follow-up and press Enter to queue it.

Note

In versions earlier than 2.26.0, each question replaces the message box, and **Cancel** is a button at the bottom of the card.

### Antigravity CLI

Type the command in the interactive prompt:

```text
/grill-me Add per-user rate limiting to the bookmarks API
```

Each question opens a numbered list of answers in the terminal, with the agent’s recommended answer first:

![A /grill-me question in the Antigravity CLI asking how rate limits should be structured across user plans, with the recommended answer first and a Write-in option last](/assets/image/docs/commands/grill-me-cli-question.png)

To answer a question:

*   Press ↑/↓ to highlight an answer and Enter to select it, or press the answer’s number.
*   Select **Write-in…** to type your own answer, then press Enter to submit it.
*   Press Esc to skip the question.

If you run `/grill-me` without a task, the agent typically explores the workspace and starts by asking what you want to work on.

## How an interview works

1.  **The agent explores the codebase.** When the code can answer a question, the agent reads the code instead of asking you, so its questions build on what’s already there.
2.  **It asks one question at a time.** Each question offers a few answers, with the agent’s recommendation listed first and marked **(Recommended)**, plus a field for writing your own answer.
3.  **Each answer shapes the next question.** The agent walks down each branch of the design, resolving dependencies between decisions one by one.
4.  **The interview ends when you’re aligned.** When no open questions remain, the agent continues with the task using your answers. To review a written plan before any code changes, [combine it with `/plan`](#combine-with-plan).

## Combine with `/plan`

To turn your answers into a plan you can review, stack [`/plan`](/docs/plan) and `/grill-me` in the same prompt:

```text
/plan /grill-me Add per-user rate limiting to the bookmarks API
```

The agent interviews you one question at a time, then writes an [implementation plan](/docs/implementation-plan) based on your answers. Unless your [artifact review policy](/docs/artifact-review) is set to [Always proceed](/docs/artifact-review#always-proceed), the agent then waits for you to review and approve the plan before it changes any code. In the Antigravity App, click **Proceed** to approve it.

## When to use `/grill-me`

`/grill-me` is most useful when a task has open decisions that the code can’t settle on its own:

*   **Underspecified features**: turning a short request into concrete endpoints, data models, and validation rules.
*   **Design trade-offs**: choosing between caching strategies, storage backends, concurrency models, or authentication flows.
*   **Risky refactors**: agreeing on compatibility, migration, and testing expectations before shared code changes.
*   **Testing your own design**: having the agent probe your assumptions for gaps and edge cases before you commit to an approach.

If you want a written plan to review and approve before any code changes, use [`/plan`](/docs/plan) instead, or combine the two.

## Next steps

Explore related planning and workflow documentation:

*   [Plan command (`/plan`)](/docs/plan): Get a reviewable implementation plan before the agent modifies code.
*   [Implementation plan artifact](/docs/implementation-plan): Learn how to review, comment on, and approve plan artifacts.
*   [Goal command (`/goal`)](/docs/commands/goal): Run a long task autonomously once you’ve agreed on the design.
*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.