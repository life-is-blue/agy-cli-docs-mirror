# Android Studio

In **Android Studio**, Antigravity is available directly via the [ACP Registry](https://agentclientprotocol.com/get-started/registry).

* * *

## Prerequisites

Ensure that you meet the following prerequisites before installing the agent:

*   **Android Studio**: An Android Studio release with [Bring Your Own Agent](https://developer.android.com/studio/releases#bring-your-own-agent) (ACP) support.
*   **Antigravity entitlement**: A Google Account with any Antigravity plan (including the free tier) or **Gemini Enterprise** (enterprise support is in Preview).

* * *

## Installation and setup

To start a session:

1.  Open the **Agent** tool window.
2.  Click the agent picker at the top of the panel and choose **Google Antigravity**. If it isn’t installed yet, Android Studio installs it for you.
3.  Sign in when prompted.
4.  Type a prompt. The model and thinking level pickers appear below the prompt box.

You can also install and manage agents in **Settings > Tools > AI > Agents**, on the **Marketplace** tab. To learn more, refer to [Bring Your Own Agent](https://developer.android.com/studio/releases#bring-your-own-agent) in the Android Studio documentation.

* * *

## Authentication and licensing

Note

Gemini Enterprise authentication for Android Studio is currently in **Preview**.

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