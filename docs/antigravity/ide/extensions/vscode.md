# Visual Studio Code

The **Antigravity for Visual Studio Code** extension brings the full agentic capabilities of Google Antigravity into VS Code. Converse with agents in dedicated side panels, review granular inline diffs, inspect interactive plans, and execute multi-step engineering tasks without leaving your editor.

[1\. Download VS Code](https://code.visualstudio.com/)Get Visual Studio Code for macOS, Linux, or Windows if you don't have it yet.

[2\. Install Antigravity extension](https://marketplace.visualstudio.com/items?itemName=Google.google-antigravity)Download the official Google Antigravity extension from the VS Code Marketplace.

* * *

## Prerequisites

Ensure that you meet the following prerequisites before installing the extension:

*   **Visual Studio Code**: Version 1.90 or later on macOS, Linux, or Windows.
*   **Antigravity entitlement**: A Google Account with any Antigravity plan (including the free tier) or an enterprise account enabled for **Gemini Enterprise**.

* * *

## Installation and setup

Complete the following steps to install the VS Code extension:

1.  Open Visual Studio Code.
2.  Open the Extensions sidebar (Ctrl + Shift + X on Windows and Linux, Cmd + Shift + X on macOS) or visit the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Google.google-antigravity).
3.  Search for **Google Antigravity** (published by **Google**).
4.  Click **Install**.
5.  Click the Antigravity icon in the Activity Bar to sign in and begin setup. The extension automatically installs the local `agy` backend service on first launch.

![Antigravity in Visual Studio Code](/assets/image/blog/vscode-extension-marketplace.png)

* * *

## Authentication and sign-in

Antigravity uses a unified sign-in across all surfaces. Learn more about authentication and entitlements:

[Gemini Enterprise authentication](/docs/enterprise)Learn how enterprise developers and administrators configure sign-in with Google Cloud credentials and IAM policies.

[Antigravity App overview](/docs/overview)Learn how sign-in and account entitlements work across the Antigravity App and developer surfaces.

* * *

## Chat and context

Open the Antigravity chat by clicking the Antigravity icon in the Activity Bar, or press Cmd + L (macOS) or Ctrl + L (Windows and Linux). To add code to your prompt, select it in the editor and press the same shortcut.

### Attach terminal output (`@terminal`)

Type `@terminal` in the chat prompt to attach one of your open VS Code terminals to the prompt. Each mention includes that terminal’s working directory, its last command and exit code, and about the last 8,000 characters of its output, so the agent can diagnose a failing build or test run without you copying the output. This feature relies on VS Code’s [terminal shell integration](https://code.visualstudio.com/docs/terminal/shell-integration).

To attach output from the terminal itself, right-click in the terminal and choose **Add Terminal Selection or Output to Chat**. If you have text selected, only the selection is attached; otherwise, the terminal’s recent output is attached. On macOS, you can also press Cmd + L while the terminal is focused. In the Command Palette, the same command appears as **Antigravity: Add Terminal Selection or Output to Chat**.

* * *

## Review agent changes

When the agent edits files, its changes appear as inline diffs in the editor:

*   **Per-change review**: Use the **Accept** and **Reject** CodeLens actions above each change, or press Option + Enter (macOS) or Alt + Enter (Windows and Linux) to accept the focused change and Option + Shift + Enter or Alt + Shift + Enter to reject it.
*   **Batch review**: Use **Accept All** or **Reject All** to resolve all pending changes at once.
*   **Undo a decision**: Press Cmd + Z or Ctrl + Z to undo an individual or file-level **Accept** or **Reject** decision, and Cmd + Shift + Z or Ctrl + Y to redo it.

To review changes in a side-by-side diff tab instead, turn off `antigravity.enableInlineDiff`. The diff tab’s title bar then shows **Accept All** and **Reject All** buttons.

By default, sending a new chat message accepts pending changes in background files and keeps the active file’s inline diff open for review. To keep every pending review open across turns, turn off `antigravity.autoAcceptOnChat`.

* * *

## Keyboard shortcuts

| Action | macOS | Windows and Linux |
| --- | --- | --- |
| Toggle chat focus, or add the editor selection to chat | Cmd + L | Ctrl + L |
| Add terminal selection or output to chat (terminal focused) | Cmd + L | — |
| Start a new conversation | Cmd + Shift + L | Ctrl + Shift + L |
| Accept the focused change, side-by-side diff, or pending agent step | Option + Enter | Alt + Enter |
| Reject the focused change, side-by-side diff, or pending agent step | Option + Shift + Enter | Alt + Shift + Enter |
| Undo an inline diff decision | Cmd + Z | Ctrl + Z |
| Redo an inline diff decision | Cmd + Shift + Z | Ctrl + Y |
| Interrupt the running agent (Antigravity panel focused) | Esc | Esc |

To change a shortcut, open **Preferences: Open Keyboard Shortcuts** and search for its command ID:

*   **Chat**: `antigravity.toggleChatFocus`, `antigravity.insertSnippet`, `antigravity.insertTerminalSnippet`, `antigravity.startNewConversation`
*   **Accept**: `antigravity.inlineDiff.acceptFocusedHunk`, `antigravity.sideBySide.acceptAll`, `antigravity.dynamic.acceptAgentStep`
*   **Reject**: `antigravity.inlineDiff.rejectFocusedHunk`, `antigravity.sideBySide.rejectAll`, `antigravity.dynamic.rejectAgentStep`
*   **Undo and redo**: `antigravity.inlineDiff.undo`, `antigravity.inlineDiff.redo`
*   **Interrupt**: `antigravity.dynamic.interruptAgent`

* * *

## Extension settings

Configure the extension in VS Code’s **Settings** editor (search for `antigravity`) or in your `settings.json` file:

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `antigravity.enableInlineDiff` | Boolean | `true` | Shows agent changes as inline diffs with **Accept** and **Reject** CodeLens actions. When `false`, changes open in a side-by-side diff tab with **Accept All** and **Reject All** buttons in the tab title bar. |
| `antigravity.autoAcceptOnChat` | Boolean | `true` | When you send a new chat message, accepts pending changes in background files while keeping the active file’s inline diff open. When `false`, pending reviews stay open across turns. |
| `antigravity.autoOpenFiles` | Boolean | `false` | Opens files in the editor automatically when the agent proposes edits. |
| `antigravity.serverPort` | Number | `0` | Port for the Antigravity background server (`agy --hub`). Leave at `0` to use an automatically assigned port, or set a fixed port for remote and port-forwarded environments. |
| `antigravity.serverStartupTimeoutMs` | Number | `30000` | Time in milliseconds to wait for the background server to start. |
| `antigravity.enableTelemetry` | Boolean | `true` | **Deprecated.** Use the **Enable Telemetry** toggle in Antigravity **Settings** > **Account** instead, or run **Antigravity: Manage Data Sharing & Telemetry**. |

* * *

## Corporate networks

If your organization routes traffic through a proxy or inspects TLS traffic, configure the following before you start VS Code.

### Proxy servers

The extension and its background server use the standard `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables. If those variables are not set, the extension copies VS Code’s `http.proxy` and `http.noProxy` settings into them; environment variables always take precedence. The extension keeps `localhost` and `127.0.0.1` in the proxy bypass list so it can always reach the local `agy` background server.

### Custom root CA certificates

If a TLS inspection proxy (such as Zscaler) re-signs traffic with your organization’s root certificate, trust that certificate in two places:

1.  **Operating system trust store**: Install the root certificate in your system’s trust store (Keychain Access on macOS, the Windows certificate store, or your distribution’s CA bundle on Linux). The background `agy` server reads certificates from the OS trust store (through `SSL_CERT_FILE` and `NODE_USE_SYSTEM_CA`), so this step is required for the agent to reach Google services.
    
2.  **`NODE_EXTRA_CA_CERTS`**: Point this variable at a PEM file that contains the root certificate so the extension’s own requests, including the download of the background server, trust the certificate chain. Set it in your environment before you launch VS Code.
    
    On macOS and Linux:
    
    ```bash
    export NODE_EXTRA_CA_CERTS="$HOME/certs/corporate-root-ca.pem"
    code .
    ```
    
    On Windows, set it persistently from PowerShell or Command Prompt, then restart VS Code:
    
    ```powershell
    setx NODE_EXTRA_CA_CERTS "C:\certs\corporate-root-ca.pem"
    ```