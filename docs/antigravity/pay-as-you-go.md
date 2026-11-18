# Pay As You Go with a Google Cloud project

With the **Pay As You Go** billing model, Antigravity sends requests to Gemini Enterprise Agent Platform in your own Google Cloud project. You pay only for the tokens you use, billed to the project’s Cloud Billing account at [Agent Platform generative AI pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing). You don’t need a Gemini Enterprise license.

You sign in with the Google Account that has access to the project, such as your [Google Workspace account](/docs/workspace).

Not the same as the Gemini Enterprise Pay-as-you-go edition

The Gemini Enterprise Pay-as-you-go edition is a Gemini Enterprise license, which you select under **Subscription** when you sign in. If your organization uses Gemini Enterprise, refer to [Antigravity in Gemini Enterprise](/docs/enterprise) instead.

## What to expect

*   **Pricing**: You pay API pricing for every request instead of a flat subscription, and there are no included quotas.
*   **Terms**: Usage is covered by the Google Cloud Terms of Service, and Antigravity doesn’t collect telemetry.
*   **Models**: Anthropic Claude models are available only if they’re enabled for your project. Antigravity hides partner models that your project can’t access.

## Set up your Google Cloud project

A project owner or administrator completes these steps once. You can sign in to the [Google Cloud console](https://console.cloud.google.com) with the same account you use for Antigravity.

1.  **Select or create a project**: Choose an existing Google Cloud project or [create a new one](https://console.cloud.google.com/projectselector2).
2.  **Turn on billing**: Make sure the project is linked to an active [Cloud Billing account](https://console.cloud.google.com/billing).
3.  **Enable the API**: Enable the [Gemini Enterprise API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com) (`aiplatform.googleapis.com`) in the project.
4.  **Grant access**: Grant each developer the **Agent Platform User** (`roles/aiplatform.user`) IAM role on the project, or another role that includes the `aiplatform.endpoints.predict` permission.
5.  **Enable partner models (optional)**: To use Anthropic Claude models, [enable them in Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models) for your project.

## Sign in with your project

Use Antigravity App `v2.31.0` or later, or Antigravity CLI `v1.4.11` or later.

### Antigravity App

1.  Launch the Antigravity App and select **Use Business Account**. If you’ve signed in before, select **Other sign-in options** first.
2.  Select **Continue with Google Cloud** and sign in with your account in the browser.
3.  In **Select Billing Model**, select **Pay As You Go**.
4.  In **Provide Google Cloud Project**, enter your project ID.
5.  In **Choose Region**, select **Global**, **United States**, or **Europe**.

### Antigravity CLI

1.  Run `agy`. If you’re already signed in, run `/logout` first.
2.  In **Select login method**, select **Use a Google Cloud project**.
3.  Select **Continue with Google Cloud** and sign in with your account in the browser.
4.  In **Select billing model**, select **Pay As You Go**.
5.  Enter your project ID, then choose a region: `global`, `us`, or `eu`.

To switch to a different project or region later, sign out and sign in again. For headless environments, you can authenticate with [Application Default Credentials](/docs/enterprise#application-default-credentials-adc) instead.

Using the Antigravity CLI only?

The Antigravity CLI can also run with a [Gemini API key](/docs/install?tab=cli#using-a-gemini-api-key) from Google AI Studio, billed at Gemini API pricing.

## Troubleshooting

*   **Permission `aiplatform.endpoints.predict` denied**: Your account doesn’t have access to Agent Platform in the project. Ask a project administrator to grant you the **Agent Platform User** (`roles/aiplatform.user`) role, and check that billing and the Gemini Enterprise API are turned on. Refer to [Set up your Google Cloud project](#set-up-your-google-cloud-project).
*   **Selected model is not supported in the selected location**: Some models aren’t available in every region. Sign out and sign in again with a different region, or choose another model. Refer to [Regional endpoints](/docs/enterprise#regional-endpoints).
*   **A Claude model is missing**: Antigravity only shows partner models that your project can access. Enable the model for your project in [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models).

## Related pages

[Google Workspace accounts](/docs/workspace)Compare a personal Google Account, Pay As You Go, and Gemini Enterprise for Workspace accounts.

[Antigravity in Gemini Enterprise](/docs/enterprise)Gemini Enterprise licenses, administrator setup, BYOID, and network requirements.