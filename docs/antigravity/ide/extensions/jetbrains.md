# IntelliJ-based IDEs

Antigravity supports the full suite of **IntelliJ-based IDEs**—including IntelliJ IDEA, PyCharm, WebStorm, GoLand, CLion, Rider, and more—starting with version **2026.2.1+**.

* * *

## Prerequisites

Ensure that you meet the following prerequisites before installing the extension:

*   **IntelliJ-based IDE**: Any IntelliJ-based IDE version 2026.2.1 or later on macOS, Linux, or Windows.
*   **Antigravity entitlement**: A Google Account with any Antigravity plan (including the free tier) or **Gemini Enterprise**.

* * *

## Installation and setup

Complete the following steps to install the Antigravity extension:

1.  Open your IntelliJ-based IDE.
2.  Open **JetBrains AI** > **Settings** > **Agents**.
3.  Search for **Antigravity**.
4.  Click **Install**.

![Antigravity in JetBrains IDEs](/assets/image/blog/jetbrains-extension-marketplace.png)

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