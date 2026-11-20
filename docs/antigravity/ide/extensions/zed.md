# Zed

Antigravity integrates directly into the **Zed** editor for high-performance, agentic editing within your native Rust-powered workflow.

* * *

## Prerequisites

Ensure that you meet the following prerequisites before installing the extension:

*   **Zed**: Version 0.140.0 or later on macOS or Linux.
*   **Antigravity entitlement**: A Google Account with any Antigravity plan (including the free tier) or **Gemini Enterprise**.

* * *

## Installation and setup

Complete the following steps to install Antigravity in Zed:

1.  Open Zed.
2.  Open the Command Palette (Cmd + Shift + P on macOS, Ctrl + Shift + P on Linux and Windows).
3.  Enter `agent: open settings` and press Enter.
4.  Navigate to **External Agents** > **Add** > **Install from Registry**.
5.  Search for **Antigravity**.
6.  Click **Install**.

![Antigravity in Zed](/assets/image/blog/zed-extension-marketplace.png)

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