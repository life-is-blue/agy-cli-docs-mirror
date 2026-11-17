# Antigravity for Google Workspace accounts

This page is for Google Workspace accounts: email addresses on your own domain, such as `you@yourcompany.com`, that are managed through Google Workspace or Cloud Identity. This includes companies with only one person. It explains how to get access to Google Antigravity and what each option costs.

Workspace subscriptions don’t include Antigravity

Google Workspace plans don’t currently include Antigravity plans, higher rate limits, or AI credits. We’re working to improve this. Until then, choose one of the options below.

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

Connect Antigravity to a Google Cloud project and pay only for the tokens you use. Requests go to Gemini Enterprise Agent Platform (formerly Vertex AI) in your project and are billed to the project’s Cloud Billing account at [Agent Platform generative AI pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing). You don’t need a Gemini Enterprise subscription.

*   **Tradeoffs**: You pay API pricing for every request instead of a flat subscription, and there are no included quotas.
*   **Terms**: Usage is covered by the Google Cloud Terms of Service, and Antigravity doesn’t collect telemetry.

### Set up your Google Cloud project

A project owner or administrator completes these steps once. You can sign in to the [Google Cloud console](https://console.cloud.google.com) with the same Workspace account you use for Antigravity. If you’re the only person in your company, you’re usually also the administrator.

1.  **Select or create a project**: Choose an existing Google Cloud project or [create a new one](https://console.cloud.google.com/projectselector2).
2.  **Turn on billing**: Make sure the project is linked to an active [Cloud Billing account](https://console.cloud.google.com/billing).
3.  **Enable the API**: Enable the [Agent Platform API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com) (`aiplatform.googleapis.com`) in the project.
4.  **Grant access**: Grant each developer the **Agent Platform User** (`roles/aiplatform.user`) IAM role on the project, or another role that includes the `aiplatform.endpoints.predict` permission.
5.  **Enable partner models (optional)**: To use Anthropic Claude models, [enable them in Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models) for your project. Antigravity hides partner models that your project can’t access.

### Sign in with your project

Use Antigravity App `v2.31.0` or later, or Antigravity CLI `v1.4.11` or later.

### Antigravity App

1.  Launch the Antigravity App and select **Use Business Account**.
2.  Select **Continue with Google Cloud** and sign in with your Workspace account in the browser.
3.  In **Select Billing Model**, select **Pay As You Go**.
4.  In **Provide Google Cloud Project**, enter your project ID.
5.  In **Choose Region**, select **Global**, **United States**, or **Europe**.

### Antigravity CLI

1.  Run `agy`. If you’re already signed in, run `/logout` first.
2.  In **Select login method**, select **Use a Google Cloud project**.
3.  Select **Continue with Google Cloud** and sign in with your Workspace account in the browser.
4.  In **Select billing model**, select **Pay As You Go**.
5.  Enter your project ID, then choose a region: `global`, `us`, or `eu`.

To switch to a different project or region later, sign out and sign in again. For headless environments, you can authenticate with [Application Default Credentials](/docs/enterprise#application-default-credentials-adc) instead.

Using the Antigravity CLI only?

The Antigravity CLI can also run with a [Gemini API key](/docs/install?tab=cli#using-a-gemini-api-key) from Google AI Studio, billed at Gemini API pricing.

## Option 3: Use Gemini Enterprise

If your organization wants seat-based licensing, included quotas, and centralized administrative controls, an administrator can set up Antigravity through a Gemini Enterprise subscription. This option takes the most setup: an administrator must purchase Gemini Enterprise, turn on AI developer tools, and assign licenses before developers can sign in.

[Antigravity in Gemini Enterprise](/docs/enterprise)Administrator setup, license assignment, sign-in, and network requirements for Gemini Enterprise.

[Compare plans and pricing](/pricing)See what's included in each individual plan and the business plan through Google Cloud.

## Frequently asked questions

### What happens if I sign in with my Workspace account using Continue with Google?

By default, Antigravity gives your Workspace account a limited starter quota. If your Workspace administrator has turned off access for individuals, Antigravity shows **Sorry, this account is ineligible to use Antigravity** instead. The starter quota doesn’t support higher rate limits or AI credits, and you can’t upgrade it with a Workspace subscription. For more usage, choose one of the [options above](#choose-an-option).

### Which Antigravity products does this page cover?

The sign-in steps on this page cover the Antigravity App and the Antigravity CLI. The standalone Antigravity IDE doesn’t support business accounts. For Antigravity IDE extensions, refer to [Antigravity in Gemini Enterprise](/docs/enterprise).