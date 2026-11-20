# Xcode

You can access Antigravity directly inside Apple’s **Xcode** to build across Apple platforms (including macOS, iOS, iPadOS, watchOS, and visionOS) without leaving your native development environment.

* * *

## Prerequisites

Ensure that you meet the following prerequisites before installing the extension:

*   **Xcode**: Xcode 27 beta 6 or later on macOS.
*   **Antigravity entitlement**: A Google Account with any Antigravity plan (including the free tier) or **Gemini Enterprise**.

* * *

## Installation and setup

Complete the following steps to install Antigravity in Xcode:

1.  Open **Xcode** (Xcode 27 beta 6 or later).
2.  Navigate to **Xcode** > **Settings** (or press Cmd + ,).
3.  Select the **Intelligence** settings panel.
4.  Install Antigravity by clicking **Get**.
5.  After Antigravity installs, select **Antigravity** and click **…** to start authentication.

![Antigravity in Xcode](/assets/image/blog/xcode-extension-marketplace.png)

* * *

## Authentication and licensing

### Google Accounts

For individual Google AI subscription plans (including Free, Pro, and Ultra):

```json
{
  "auth": {
    "type": "oauth-personal"
  }
}
```

### Gemini Enterprise

Reach out to your cloud administrator for your GCP Project ID and Region:

```json
{
  "auth": {
    "type": "oauth-business"
  },
  "gcp": {
    "project": "<YOUR_GCP_PROJECT_ID>",
    "location": "<YOUR_GCP_REGION>"
  }
}
```

### Gemini API

Authenticate using a Gemini API key:

```json
{
  "auth": {
    "type": "gemini-api-key"
  }
}
```

### API / ADC

Authenticate with Gemini Enterprise using an API Key or Application Default Credentials (ADC) (Preview). When using ADC, specify your GCP Project ID and Region:

```json
{
  "auth": {
    "type": "agent-platform"
  },
  "gcp": {
    "project": "<YOUR_GCP_PROJECT_ID>",
    "location": "<YOUR_GCP_REGION>"
  }
}
```