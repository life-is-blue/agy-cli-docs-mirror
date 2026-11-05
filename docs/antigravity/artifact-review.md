# Artifact review

Available on: Antigravity App

When starting a new agent conversation, you can choose between two primary execution modes that determine how changes are proposed and reviewed:

*   **Planning mode**: The agent plans thoroughly before executing tasks. In this mode, the agent organizes its work in [task groups](/docs/ide/agent-side-panel), produces structured implementation plans called [artifacts](/docs/artifacts), and thoroughly researches the codebase for optimal quality.
*   **Fast mode**: The agent executes tasks directly without a dedicated planning phase. Use this for simple, highly localized tasks that can be completed quickly, such as variable renaming, running a specific Bash command, or small refactors.

When working in **Planning mode**, the artifact review policy controls how you interact with and approve these plans before changes are made to your codebase.

## Artifact review policy

You can customize the review workflow with **Plan Review Policy** in **Settings** > **General**. Choose between two policies:

### Request review (recommended)

Shown as **Always Ask** in Settings. The agent always halts and requests your explicit approval before proceeding with proposed changes:

*   When the agent generates an implementation plan or code diff, it pauses execution and notifies you.
*   This allows you to thoroughly review the proposed changes, add inline comments, and verify the plan in your workspace.
*   Once you’re satisfied, you can approve the plan to let the agent proceed.

![An Implementation Plan card in an Antigravity App conversation, followed by Proceeded with Implementation Plan after the plan was approved](/assets/image/docs/agent/settings-review-policy-manual.png)

### Always proceed

Shown as **Always Proceed** in Settings. This setting doesn’t make the agent continue past a plan. When you ask for a plan with [`/plan`](/docs/plan), the agent always stops and waits for your approval, whatever your review policy is:

*   To have the agent keep going after it writes a plan, say so in your prompt.
*   With **Always Proceed**, the plan’s card might not show a **Proceed** button. To approve the plan, reply in the message box, for example with `proceed`.

![The Plan Review Policy setting under Agent Behavior in Settings > General, set to Always Proceed](/assets/image/docs/agent/settings-review-policy-proceed.png)