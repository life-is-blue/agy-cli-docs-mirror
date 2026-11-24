# Plans

Google Antigravity is available to individual accounts under [terms](/terms) derived from Google’s Terms of Service, and to teams under Google Cloud terms in Gemini Enterprise. To learn more, refer to [Antigravity in Gemini Enterprise](/docs/enterprise).

The plans on this page apply to personal Google Accounts. Google Workspace plans don’t include Antigravity plans or higher rate limits. If you use a Google Workspace account, refer to [Google Workspace accounts](/docs/workspace) for your options.

Rate limits and model availability differ based on your [Google AI](https://one.google.com/about/google-ai-plans/) plan. Refer to [Models](/docs/models) for a breakdown of model availability.

## Baseline quota

All plans receive the following baseline features:

*   Use of Gemini models, including Gemini 4 Hydrogen, as the core agent model
*   Unlimited Tab completions
*   Access to all product features, such as scheduled tasks and the CLI

**Google AI Ultra** subscribers receive the following benefits:

*   The highest, most generous quota, refreshed every five hours
*   The highest weekly rate limits
*   Full access to frontier Gemini models and third-party partner models

**Paid Google AI Pro** subscribers (and trials bundled with eligible premium devices) receive the following benefits:

*   A high, generous quota, refreshed every five hours until the weekly limit is reached
*   A higher weekly rate limit
*   Access to frontier Gemini models—including Gemini 4 Neon, Gemini 4 Carbon, Gemini 4 Argon, and Gemini 4 Hydrogen—within your shared Gemini quota, plus paid-tier third-party models (refer to [Models](/docs/models) for availability)

**Google AI Pro trial** subscribers (standard free and promotional trials) receive different entitlements from paid Google AI Pro plans:

*   A lower quota entitlement and a more limited set of models (including Gemini 4 Hydrogen) than paid Google AI Pro subscriptions, subject to available capacity
*   Trial and promotional benefits and usage limits may differ from paid subscriptions under the [Google One Terms of Service](https://one.google.com/terms-of-service)
*   To get paid Google AI Pro quotas and full model availability right away, [submit a request](https://one.google.com/support) to cancel your trial and switch to a paid plan (see [How do I upgrade to a paid Google AI plan?](/docs/faq#how-do-i-upgrade-to-a-paid-google-ai-plan))

**Free and Google AI Plus** users (not on Google AI Pro or Ultra plans) receive the following benefits:

*   A meaningful quota, refreshed weekly
*   A weekly rate limit
*   Access to Gemini 4 Hydrogen (and Gemini 3.8 Flash until November 30, 2026)

The baseline rate limits are primarily determined by available capacity and exist to prevent abuse. Under the hood, the rate limits correlate with the amount of work done by the agent, which can differ from prompt to prompt. As a result, you receive more prompts when your tasks are straightforward and the agent can complete the work quickly, while more complex tasks consume more quota.

Usage limits for this service are subject to modification. These adjustments may be necessary to manage system capacity and maintain service stability.

## Overages

Users on Google AI Pro or Ultra plans can use [purchased AI credits](https://one.google.com/ai/credits) (or any one-time promotional credits) for additional overage usage above the baseline quota. AI credits are consumed at standard Gemini Enterprise consumption pricing.

Once you exhaust the baseline quota for a particular model, credit usage is controlled by the **AI Credit Overages** user setting, which you can set to one of the following options:

*   **Never**: Never use AI credits automatically; wait until the baseline quota refreshes before using this model further.
*   **Always**: Always use AI credits when the baseline quota is exhausted (automatically switches back to using the baseline quota once it refreshes).

You can view baseline quota usage across models on the **Settings** page.

## Other

There is currently no support for the following options:

*   Bring-your-own-key (BYOK) or bring-your-own-endpoint for additional rate limits
*   Organizational tiers through a custom contract