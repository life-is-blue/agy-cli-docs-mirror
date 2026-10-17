# Choose a model

Antigravity gives you access to leading frontier reasoning models from Google DeepMind and partner providers. You can switch models at any time and choose a thinking level (`Low`, `Medium`, or `High`) to balance response speed for quick edits against deeper multi-step reasoning for complex architecture and debugging tasks.

## Select a model

You can select which reasoning model you want to use from the model selector menu under the conversation prompt box:

Your choice of reasoning model persists between messages within a conversation. If you change the reasoning model while the agent is running, it continues to use the previously selected reasoning model until it completes its steps for that turn (or until you cancel the current execution).

## Reasoning model

For the core reasoning model, Antigravity offers leading frontier models. Availability depends on your plan:

| Model | Free & Google AI Plus | Google AI Pro | Google AI Ultra | Enterprise |
| --- | --- | --- | --- | --- |
| [Gemini 4 Argon](/blog/gemini-4-argon-in-google-antigravity)\*\*\* | ❌ | ✅\*\* | ✅ | ✅ |
| [Gemini 3.8 Flash](/blog/gemini-3-8-flash-in-google-antigravity) | ✅ | ✅ | ✅ | ✅ |
| [Gemini 3.7 Flash](/blog/gemini-3-7-flash-in-google-antigravity) | ❌ | ❌ | ❌ | ✅ |
| [Gemini 3.6 Flash](/blog/gemini-3-6-flash-in-google-antigravity) | ❌ | ❌ | ❌ | ✅ |
| [Gemini 3.1 Pro](/blog/gemini-3-1-pro-in-google-antigravity) | ❌ | ❌ | ❌ | ✅ |
| Claude Sonnet 5.5 (thinking)\*\* | ❌ | ✅\*\* | ✅ | ✅ |
| Claude Opus 5.5 (thinking)\*\* | ❌ | ✅\*\* | ✅ | ✅ |
| Claude Sonnet 4.6 (thinking)\* | ✅ | ✅ | ❌ | ❌ |
| Claude Opus 4.6 (thinking)\* | ✅ | ✅ | ❌ | ❌ |
| GPT-OSS-120b\* | ✅ | ✅ | ✅ | ❌ |

\* Will be removed on November 2, 2026.

\*\* Available on Google AI Pro for non-trial subscriptions only. To switch from a trial to a paid Google AI Pro plan, [submit an upgrade request](https://support.google.com/googleone/contact/googleone_ai_pro_signup_issues).

\*\*\* Not available in Antigravity IDE. Available in the Antigravity App, Antigravity CLI, and IDE extensions.

To learn more about reasoning model rate limits, refer to the [plans page](/docs/plans). If you are using Antigravity with Gemini Enterprise, see [Supported models in Gemini Enterprise](/docs/enterprise#supported-models-in-gemini-enterprise).

## Additional models

Antigravity uses other models for various parts of the stack that aren’t customizable:

*   **[Nano Banana 2](/blog/nano-banana-pro)**: Used by the generative image tool when the agent produces a UI mockup, generates images to populate a web page or application, creates system or architecture diagrams, or performs other generative image tasks.