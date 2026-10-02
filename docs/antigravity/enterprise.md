# Antigravity in Gemini Enterprise

To deploy Google Antigravity using models hosted directly within your organization’s Google Cloud infrastructure, you can integrate with Gemini Enterprise. Every session runs under Google Cloud’s enterprise security controls, data residency guarantees, and the Google Cloud Terms of Service.

Supported products: [Antigravity 2.0](/product/antigravity-2) [Antigravity CLI](/product/antigravity-cli) [Visual Studio Code](/docs/ide/extensions/vscode) [Visual Studio](/docs/ide/extensions/visual-studio) [JetBrains (Preview)](/docs/ide/extensions/jetbrains) [Zed (Preview)](/docs/ide/extensions/zed) [Xcode (Preview)](/docs/ide/extensions/xcode)

Note

**Note**: Enterprise integration is supported for Antigravity 2.0, Antigravity CLI, and Antigravity IDE extensions. **Antigravity IDE** (standalone) is currently not supported for enterprise deployments. [View supported models](/docs/models)

## Overview and key benefits

You can connect Antigravity to Gemini Enterprise in two ways:

*   **Google Cloud project and API**: Connect directly using Google Cloud project APIs to use Antigravity with consumption-based billing.
*   **Gemini Enterprise license**: Connect with your Gemini Enterprise license (Standard or Plus) to get access to included quotas, managed overages, and centralized administrative controls.

By connecting Google Antigravity to your Google Cloud project, your organization gains:

Enterprise governance

Operates under your existing Google Cloud Terms of Service with centralized administrative controls.

Data residency and security

Satisfies private networking (VPC Service Controls) and regional data residency constraints. Enterprise prompts, responses, code, and telemetry are never stored outside your private environments.

## Administrator setup guide

### Gemini Enterprise subscription setup

To set up Gemini Enterprise subscriptions, follow the official Google Cloud onboarding guide.

[Gemini Enterprise Documentation](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview)

### Google Cloud project and API setup

New to Gemini Enterprise Agent Platform?

If you are a new customer connecting via API, you will need an API key to authenticate. Visit the [API Key Quickstart Guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/api-keys?usertype=expressmode) to create your key first.

Complete the following three steps to provision your Google Cloud project and enable API access:

1.  **Select or create a Google Cloud project**: Select an existing project or create a dedicated project for your team’s Antigravity workloads.
    
    Note
    
    **Project switching note**: To switch to a different Google Cloud project or location, log out of the Antigravity CLI or Antigravity 2.0, then log back in to select your new project or region.
    
    [Go to GCP Project Selector](https://console.cloud.google.com/projectselector2)
2.  **Verify Cloud Billing**: Ensure that Cloud Billing is active for your selected Google Cloud project. You can inspect your project’s billing status in the Google Cloud Console.
    
    [Open Google Cloud Billing Console](https://console.cloud.google.com/billing)
3.  **Enable the API**: Enable the Gemini Enterprise API (`aiplatform.googleapis.com`) to allow Antigravity clients to connect to your project’s model endpoints.
    
    [Enable API in Cloud Console](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com)

## Sign in and license selection

Google Antigravity uses a single sign-on (SSO) flow. When you sign in with your corporate business account, your license tier is automatically detected without requiring manual tier selection.

### Sign-in workflow

Complete the following steps to sign in and select a license:

1.  Start **Antigravity 2.0**, the **Antigravity CLI**, or your supported **[IDE extension](/docs/ide/extensions)**.
2.  Select **Sign in** to open the browser authentication flow.
3.  Choose **Business account** _(subject to the Google Cloud Terms of Service)_.
4.  Select **Continue with Google Cloud** (or configure Advanced SSO and WIF).
5.  Complete authentication in your browser.
6.  Once authenticated, the **License Selector** displays your assigned licenses.
7.  Confirm the project linked to your license and select it. Alternatively, select **Other** to self-assign a license by entering your project ID and selecting a location (`global`, `us`, or `eu`).

Note

**Data-sharing and project logging notice**: Your customer telemetry and model interactions are logged directly to the Google Cloud project corresponding to the license you select. You can maintain **one license per project and location**.

## Bring your own identity (BYOID and WIF)

Bring Your Own Identity (BYOID) uses Workforce Identity Federation (WIF) to let your organization authenticate through an external identity provider, such as Okta, instead of a standard Google Account.

### Configuring BYOID

Complete the following steps to configure BYOID:

1.  In Antigravity, select **Business account**.
2.  Select **Advanced WIF Configuration**.
3.  Enter the **WIF Configuration String** provided by your organization’s administrator.
4.  Complete sign-in through your federated identity provider.
5.  Select or self-assign a license from the License Selector.

Note

**Note**: If the same email address exists across multiple identity providers, sign in with the identity that matches your Gemini Enterprise license.

## Application Default Credentials (ADC)

For headless environments and automated terminal workflows, Antigravity supports authentication using Google Cloud [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC). ADC is available across the **Antigravity CLI**, **Antigravity 2.0**, and **Antigravity IDE**.

Note

**Note**: Image generation is currently not available in `eu` and `us` locations.

### Setting up ADC

Complete the following steps to generate and verify your credentials:

1.  Generate local Application Default Credentials for your project using the Google Cloud SDK:
    
    ```
    gcloud auth application-default login --project {GCP_PROJECT}
    ```
    
2.  Verify that your credentials file exists. On Linux and macOS, the default path is:
    
    ```
    ~/.config/gcloud/application_default_credentials.json
    ```
    

### Enabling ADC

Enable ADC authentication based on your Antigravity surface:

*   **Antigravity CLI**: ADC is enabled only when the `AGY_ADC_AUTH` environment variable is set to `true`:
    
    ```
    export AGY_ADC_AUTH=true
    ```
    
*   **Antigravity 2.0 and IDE**: Enable ADC using one of the following two options:
    
    *   Launch from a terminal with `AGY_ADC_AUTH=true` set (same as the CLI).
        
    *   Because launching from a terminal is not always feasible, enable the `enableAdc` user setting manually in `~/.gemini/config/config.json`:
        
        ```
        {
          "userSettings": {
            "enableAdc": true
          }
        }
        ```
        

### Sign out of ADC

To sign out of ADC on the CLI, unset the environment variable and restart your terminal session:

```
unset AGY_ADC_AUTH
```

Similarly, for **Antigravity 2.0 and IDE**, undo any changes to `~/.gemini/config/config.json` (or unset `AGY_ADC_AUTH` if launched from a terminal) and restart the application.

### ADC quickstart

This section provides a brief walkthrough of key ADC parameters to be aware of.

#### How credentials are resolved

Antigravity resolves credentials using the standard ADC search order. [Learn more about how ADC finds credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials#order).

#### How the project ID is resolved

Antigravity resolves the Google Cloud project ID from the first source found, in this order:

1.  The `quota_project_id` field in the ADC file (set using the `gcloud` CLI, or edited manually).
2.  **\[CLI only\]**: The `GOOGLE_CLOUD_QUOTA_PROJECT` environment variable.
3.  The project ID reported by the metadata server (for service accounts).

#### How the location is resolved

Antigravity resolves the endpoint location from the first source found, in this order:

1.  The surface-specific configuration:
    *   **\[CLI\]**: The `GOOGLE_CLOUD_LOCATION` environment variable.
    *   **\[Antigravity 2.0 / IDE\]**: The `location` field in the ADC file.
2.  Otherwise, the location defaults to `global`.

Note

**Note**: When authenticating with ADC, models older than Gemini 3 Flash are not supported.

## Regional endpoints and capability matrix

Antigravity CLI, Antigravity 2.0, and IDE extensions support multi-region deployment endpoints to satisfy regional data residency requirements:

| Endpoint Region | Base Endpoint URI | Supported Capabilities |
| :-- | :-- | :-- |
| **Global** | `global` | Text Generation, Code Inference, Multimodal, Image Generation |
| **US Multi-Region** | `us` | Text Generation, Code Inference, Multimodal |
| **EU Multi-Region** | `eu` | Text Generation, Code Inference, Multimodal |

Note

**Note**: Image generation capabilities are currently available exclusively on **`global`** deployment endpoints.

For full endpoint specifications, consult the [Deployment endpoints documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#global).

## Security and governance

Request and response logging

Audit model interactions and maintain enterprise compliance records for your Gemini Enterprise instance. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/request-response-logging)

VPC Service Controls (VPC-SC)

Enforce private networking security perimeters by adding the Gemini Enterprise API (`aiplatform.googleapis.com`) to your VPC-SC perimeter. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls)

## Troubleshooting and diagnostics

### Common sign-in and license issues

Review the following solutions for common sign-in and license issues:

*   **No licenses appear during setup**: Licenses are assigned by your organization’s Google Cloud administrator. If the License Selector is empty, contact your administrator to ensure your account has been granted access to a Gemini Enterprise Standard or Plus license.
*   **Missing BYOID sign-in option**: Ensure you are running the latest release of **[Antigravity 2.0](/download)**, the **[Antigravity CLI](/docs/cli/install)**, or your **[IDE extension](/docs/ide/extensions)**, as enterprise authentication and BYOID support are included natively in all recent releases.

### Important API provisioning advisory

Caution

**Enable required APIs before purchasing licenses**: New Gemini Enterprise license purchases can fail or fail to provision if the **Gemini Enterprise API** (`aiplatform.googleapis.com`) is not enabled first. Enable the API in the Google Cloud Console and wait approximately five minutes for propagation before completing license purchases.

### Sharing diagnostics with support

When contacting Google Cloud Support, include the diagnostic log file from your most recent session:

*   **Antigravity CLI (Linux and macOS)**:
    
    ```
    ~/.gemini/antigravity-cli/cli.log
    ```
    
*   **Antigravity 2.0 (macOS)**:
    
    ```
    ~/Library/Logs/Antigravity/language_server.log
    ```
    

## What’s next

Explore the following resources to learn more:

*   Explore supported model architectures in the [Models guide](/docs/models).
*   Learn more about enterprise privacy and compliance in [Security and governance](#security-and-governance).
*   Check the [Antigravity CLI reference](/docs/cli/reference) for headless automation commands.