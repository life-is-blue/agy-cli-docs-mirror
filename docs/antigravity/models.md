# Choose a model

Available on: Antigravity App, Antigravity CLI, Antigravity IDE

Antigravity gives you access to leading frontier reasoning models from Google DeepMind and partner providers. You can switch models at any time and choose a thinking level (`Low`, `Medium`, `High`, or `Extra` on supported models) to balance response speed for quick edits against deeper multi-step reasoning for complex architecture and debugging tasks. To combine planning on Gemini 4 Carbon or Gemini 4 Argon with fast Gemini 4 Hydrogen execution and use fewer tokens, select [Orchestrator](#orchestrator).

## Select a model

You can select which reasoning model you want to use from the model selector menu under the conversation prompt box:

† Available with paid Google AI Pro plans or on trial with eligible premium devices. To switch to a paid Google AI Pro plan, [submit a request](https://one.google.com/support).

Most adjustable Gemini models offer `Low`, `Medium`, and `High` thinking levels. **Gemini 4 Hydrogen** defaults to `High` and adds a fourth level labeled **`Extra`** in the model selector, which sets the **Extra High** reasoning budget (`xhigh` in the [Antigravity CLI](/docs/cli/commands/effort), such as `--model gemini-4-hydrogen-xhigh` or `--effort xhigh`) when a task needs maximum reasoning depth.

Your choice of reasoning model persists between messages within a conversation. If you change the reasoning model while the agent is running, it continues to use the previously selected reasoning model until it completes its steps for that turn (or until you cancel the current execution).

## Reasoning model

For the core reasoning model, Antigravity offers leading frontier models. Availability depends on your plan:

| Model | Free & Google AI Plus | Google AI Pro | Google AI Ultra | Enterprise |
| --- | --- | --- | --- | --- |
| [Gemini 4 Carbon](/blog/gemini-4-carbon-in-google-antigravity) | ❌ | ❌ | ✅ | ✅ |
| [Gemini 4 Argon](/blog/gemini-4-argon-in-google-antigravity) | ❌ | ✅† | ✅ | ✅ |
| [Gemini 4 Hydrogen](/blog/gemini-4-hydrogen-in-google-antigravity) | ✅ | ✅ | ✅ | ✅ |
| [Orchestrator (Carbon)](/docs/models#orchestrator) | ❌ | ❌ | ✅ | ❌ |
| [Orchestrator (Argon)](/docs/models#orchestrator) | ❌ | ✅† | ✅ | ❌ |
| [Gemini 3.8 Flash](/blog/gemini-3-8-flash-in-google-antigravity) | ✅ | ✅ | ✅ | ✅ |
| [Gemini 3.7 Flash](/blog/gemini-3-7-flash-in-google-antigravity) | ❌ | ❌ | ❌ | ✅ |
| [Gemini 3.6 Flash](/blog/gemini-3-6-flash-in-google-antigravity) | ❌ | ❌ | ❌ | ✅ |
| [Gemini 3.1 Pro](/blog/gemini-3-1-pro-in-google-antigravity) | ❌ | ❌ | ❌ | ✅ |
| Claude Sonnet 5.5 (thinking)\*\* | ❌ | ✅\*\* | ✅ | ✅ |
| Claude Opus 5.5 (thinking)\*\* | ❌ | ✅\*\* | ✅ | ✅ |
| Claude Sonnet 4.6 (thinking)\* | ✅ | ✅ | ❌ | ❌ |
| Claude Opus 4.6 (thinking)\* | ✅ | ✅ | ❌ | ❌ |
| GPT-OSS-120b\* | ✅ | ✅ | ✅ | ❌ |

\* Will be removed on November 18, 2026.

\*\* Available on Google AI Pro for non-trial subscriptions only. To cancel your trial and switch to a paid Google AI Pro plan, [submit a request](https://one.google.com/support).

† Available with paid Google AI Pro plans or on trial with eligible premium devices. To switch to a paid Google AI Pro plan, [submit a request](https://one.google.com/support).

To learn more about reasoning model rate limits, refer to the [plans page](/docs/plans). If you are using Antigravity with Gemini Enterprise, see [Supported models in Gemini Enterprise](/docs/enterprise#supported-models-in-gemini-enterprise).

## Orchestrator

**Orchestrator** is a model selector option that pairs two Gemini 4 models in a single conversation: a larger planner model does the planning and reviews, and the fast, lightweight **Gemini 4 Hydrogen** does the implementation work. There are two Orchestrator options, and the one you select sets the planner:

| Model selector option | Planner | Implementation | Available on |
| :-- | :-- | :-- | :-- |
| **Orchestrator (Carbon)** | [**Gemini 4 Carbon**](/blog/gemini-4-carbon-in-google-antigravity) | Gemini 4 Hydrogen | Google AI Ultra |
| **Orchestrator (Argon)** | [**Gemini 4 Argon**](/blog/gemini-4-argon-in-google-antigravity) | Gemini 4 Hydrogen | Google AI Ultra, Google AI Pro (paid plans, or trials with eligible premium devices) |

**Orchestrator (Carbon)** always plans with Gemini 4 Carbon, and **Orchestrator (Argon)** always plans with Gemini 4 Argon. Google AI Ultra includes both **Orchestrator (Carbon)** and **Orchestrator (Argon)** in the model selector, while Google AI Pro (paid plans, or trials with eligible premium devices) includes **Orchestrator (Argon)**. Hover over the **New** badge next to either option to see which planner it uses.

The planner and Gemini 4 Hydrogen are also available as standalone models in the model selector, depending on your plan. Orchestrator coordinates them automatically, so you get the planner’s quality while finishing faster and using fewer tokens than running the planner alone.

Orchestrator isn’t a router that classifies your prompt upfront and sends the whole request to a single model. Instead, both models collaborate within the same task and hand control back and forth as the work unfolds:

*   **The planner plans.** Each message you send starts with a read-only planning phase in which the planner explores the codebase, resolves ambiguities, and writes a concrete implementation plan, including the conditions that should trigger re-planning. If your message is a question, review, or explanation that doesn’t need changes, the planner answers it directly; for small follow-ups whose steps are already settled, it hands off a short plan right away.
*   **Gemini 4 Hydrogen does the work.** Once the plan is ready, Gemini 4 Hydrogen takes over to apply file edits, write code, run builds and tests, and verify the results against the plan.
*   **Control returns when something unexpected happens.** If Gemini 4 Hydrogen runs into friction, such as a verification step that fails twice, an interface that behaves differently than expected, or a design choice the plan didn’t settle, it hands control back to the planner, which inspects the conversation state, repairs the plan, and hands execution back to Gemini 4 Hydrogen.
*   **The planner reviews progress.** On longer tasks, and whenever you send a message while Gemini 4 Hydrogen is working, Gemini 4 Hydrogen reports its progress to the planner, which checks what was done against the plan and then wraps up the completed task, continues the remaining steps, or updates the plan.

These hand-offs happen automatically within a single response, so you don’t need to switch models manually between planning and execution.

Orchestrator runs with a fixed configuration, so you can’t choose a thinking level for it. To run every step on a single model or set a specific thinking level, select **Gemini 4 Carbon**, **Gemini 4 Argon**, or **Gemini 4 Hydrogen** directly in the model selector. Availability depends on your plan; refer to the [reasoning model table](#reasoning-model).

### Select Orchestrator

### Antigravity App

1.  Click the model selector under the conversation prompt box.
    
2.  Select **Orchestrator (Carbon)** or **Orchestrator (Argon)**.
    

Selecting Orchestrator (Carbon) in the Antigravity App: open the model selector under the prompt box, which lists Orchestrator (Carbon) and Orchestrator (Argon), hover the New badge next to Orchestrator (Carbon) to see what it does, choose it, and type a task.

Like any other model, Orchestrator stays selected for the rest of the conversation until you choose a different model.

### Antigravity CLI

Selecting Orchestrator (Carbon) in the Antigravity CLI: complete /model with Tab, choose Orchestrator (Carbon) from the list of models, which also shows Orchestrator (Argon), and check that /effort doesn't apply to it.

You can select Orchestrator in any of the following ways:

*   **Interactive picker**: Run `/model`, select **Orchestrator (Carbon)** or **Orchestrator (Argon)**, and press Enter. Your choice persists across sessions.
    
*   **At startup**: Pass the model’s name in quotes when you launch the CLI or run it in [headless mode](/docs/cli/headless):
    
    ```bash
    agy --model "Orchestrator (Carbon)"
    agy -p "Add input validation to the signup form and run the tests." --model "Orchestrator (Argon)"
    ```
    

Run `agy models` to list every model identifier available to your account. Because Orchestrator has a fixed configuration, `--effort` and `/effort` don’t apply to it; running `/effort` while Orchestrator is selected reports that effort isn’t adjustable for it, for example `Effort isn't adjustable for Orchestrator (Argon).`

### When to use Orchestrator

*   **Orchestrator (recommended default)**: Most day-to-day development, such as feature work, bug fixes, refactoring, and multi-file debugging, where you want Gemini 4 Carbon or Gemini 4 Argon to plan and review the work and Gemini 4 Hydrogen to carry out the implementation faster and with fewer tokens used.
*   **Gemini 4 Carbon or Gemini 4 Argon**: Work where every intermediate step needs maximum reasoning depth, such as designing complex distributed systems from scratch, untangling subtle concurrency race conditions, or running multi-repository migrations. Selecting the model directly also lets you choose its thinking level.
*   **Gemini 4 Hydrogen**: Fast, everyday coding and maintenance tasks where you don’t need a separate planning phase, such as package upgrades, code deduplication, scaffolding boilerplate, writing unit tests for well-defined functions, updating documentation, or generating quick scripts. Selecting Gemini 4 Hydrogen directly also lets you choose its thinking level.

Orchestrator keeps a single agent in your conversation and hands off between planning and execution within each turn. To have multiple agents work in parallel or check each other’s work, use [subagents](/docs/subagents), [Swarm](/docs/swarm), [Boost](/docs/boost), or [Teamwork](/docs/teamwork).

## Additional models

Antigravity uses other models for various parts of the stack that aren’t customizable:

*   **[Nano Banana 2](/blog/nano-banana-pro)**: Used by the generative image tool when the agent produces a UI mockup, generates images to populate a web page or application, creates system or architecture diagrams, or performs other generative image tasks.