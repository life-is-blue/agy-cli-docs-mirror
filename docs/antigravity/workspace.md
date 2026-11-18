# Antigravity for Google Workspace accounts

This page is for Google Workspace accounts: email addresses on your own domain, such as `you@yourcompany.com`, that are managed through Google Workspace or Cloud Identity. This includes companies with only one person. It explains how to get access to Google Antigravity and what each option costs.

Workspace subscriptions don’t include Antigravity plans

You can sign in with a Workspace account and use a limited starter quota, but Google Workspace plans don’t currently include Antigravity plans, higher rate limits, or AI credits. We’re working to improve this. Until then, for more usage, choose one of the options below.

## Check whether you have a Google Workspace account

Your account is a Google Workspace account if any of these apply:

*   Your organization signed up for Google Workspace or Cloud Identity for your domain, even if you’re the only user.
*   You, or someone at your company, manage your domain’s users in the Google Admin console ([admin.google.com](https://admin.google.com)).
*   Your [Google Account](https://myaccount.google.com) page says your account is managed by your domain.

If you created a personal Google Account with an existing non-Gmail address, and your domain doesn’t use Google Workspace, you have a personal account. You can use [Google AI Pro and Google AI Ultra](/pricing) directly, and you don’t need this page.

## Choose an option

| Option | How you pay | Terms and controls | Setup |
| :-- | :-- | :-- | :-- |
| **[Use a personal Google Account](#option-1-use-a-personal-google-account)** | Free, or a Google AI Pro or Google AI Ultra subscription | [Antigravity Terms of Service](/terms). No organization admin controls. You can turn off telemetry yourself. | A few minutes |
| **[Connect a Google Cloud project](#option-2-connect-a-google-cloud-project)** | Pay as you go, per token, at Google Cloud API pricing | Google Cloud Terms of Service. Telemetry is always off. | A Google Cloud project with billing |
| **[Use Gemini Enterprise](#option-3-use-gemini-enterprise)** | Gemini Enterprise seat licenses or the pay-as-you-go edition | Google Cloud Terms of Service with centralized admin controls | An administrator sets up Gemini Enterprise |

## Option 1: Use a personal Google Account

Sign in with a personal Google Account, such as an `@gmail.com` address, instead of your Workspace account. This is the quickest way to get started, and it’s the only option that works with [Google AI Pro and Google AI Ultra](/pricing) subscriptions. Because your domain is managed by Google Workspace, use a separate address for your personal account, such as a Gmail address.

*   **Plans**: The free plan works without a subscription. For higher rate limits, more models, and AI credits, subscribe to Google AI Pro or Google AI Ultra with your personal account. Refer to [Plans](/docs/plans).
*   **Tradeoffs**: Personal accounts use the [Antigravity Terms of Service](/terms) instead of the Google Cloud Terms of Service, and your organization can’t manage them with admin controls.
*   **Data collection**: You can turn off telemetry at any time. In the Antigravity App, go to **Settings** > **Account** and turn off **Enable Telemetry**. In the Antigravity CLI, run `/config` and set **Enable Telemetry** to off. Refer to [Data collection settings](/docs/settings#data-collection-settings).

To switch accounts, sign out of Antigravity (run `/logout` in the Antigravity CLI), then sign in again and select **Continue with Google** (**Google OAuth** in the Antigravity CLI) with your personal account.

## Option 2: Connect a Google Cloud project

Sign in with your Workspace account, choose the **Pay As You Go** billing model, and connect Antigravity to a Google Cloud project. Requests go to Gemini Enterprise Agent Platform in your project, and you pay only for the tokens you use. You don’t need a Gemini Enterprise subscription.

*   **Tradeoffs**: You pay API pricing for every request instead of a flat subscription, and there are no included quotas.
*   **Terms**: Usage is covered by the Google Cloud Terms of Service, and Antigravity doesn’t collect telemetry.
*   **Setup**: You need a Google Cloud project with billing and the Gemini Enterprise API (`aiplatform.googleapis.com`) turned on. If you’re the only person in your company, you’re usually also the administrator, and you can set this up in the [Google Cloud console](https://console.cloud.google.com) with your Workspace account.

For project setup and sign-in steps, refer to [Pay As You Go](/docs/pay-as-you-go).

## Option 3: Use Gemini Enterprise

If your organization wants seat-based licensing, included quotas, and centralized administrative controls, an administrator can set up Antigravity through a Gemini Enterprise subscription. This option takes the most setup: an administrator must purchase Gemini Enterprise, turn on AI developer tools, and assign licenses before developers can sign in.

[Antigravity in Gemini Enterprise](/docs/enterprise)Administrator setup, license assignment, sign-in, and network requirements for Gemini Enterprise.

[Compare plans and pricing](/pricing)See what's included in each individual plan and the business plan through Google Cloud.

## Frequently asked questions

### What happens if I sign in with my Workspace account using Continue with Google?

By default, Antigravity gives your Workspace account a limited starter quota, shown as **Antigravity Starter Quota**. If your Workspace administrator has turned off access for individuals, Antigravity shows that your account is ineligible instead. The starter quota doesn’t support higher rate limits or AI credits, and you can’t upgrade it with a Workspace subscription. For more usage, choose one of the [options above](#choose-an-option).

### Which Antigravity products does this page cover?

The sign-in steps on this page cover the Antigravity App and the Antigravity CLI. The standalone Antigravity IDE doesn’t support business accounts. For Antigravity IDE extensions, refer to [Antigravity in Gemini Enterprise](/docs/enterprise).