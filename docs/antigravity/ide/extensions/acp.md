# Other editors (ACP)

Use Antigravity in any editor that supports the [Agent Client Protocol](https://agentclientprotocol.com) (ACP). Antigravity CLI includes an ACP server, `agy acp`, so any editor can run it and chat with the agent in its own panel. Zed, JetBrains IDEs, Android Studio, and Xcode support ACP natively. VS Code needs a community extension.

`agy acp` starts an ACP server that talks JSON-RPC over `stdin` and `stdout`. Your editor launches it as a subprocess, sends prompts, and renders the agent’s replies, tool calls, file diffs, and permission requests in its native UI. The agent, its tools, and your settings come from Antigravity CLI, so the agent behaves the same in the editor as it does in the terminal.

This video demo shows how to configure ACP in the Zed editor:

## Before you begin

*   [Install Antigravity CLI](/docs/install?tab=cli) and confirm that `agy` is on your `PATH`:
    
    ```bash
    agy --version
    ```
    
*   Sign in once with an interactive `agy` session, or run `agy acp --login`. `agy acp` reuses the cached credentials. To authenticate from the editor instead, refer to [Authentication](#authentication).
    
*   Find the absolute path to `agy`. Some editors launch agents without your shell’s `PATH`:
    
    ```bash
    which agy
    ```
    

## Connect your editor

Every client except Android Studio registers the same command: `agy` with the single argument `acp`.

### VS Code

VS Code doesn’t support ACP natively. Install the community [ACP Client](https://marketplace.visualstudio.com/items?itemName=formulahendry.acp-client) extension, then add Antigravity to your user `settings.json`:

```json
{
  "acp.agents": {
    "Antigravity": {
      "command": "agy",
      "args": ["acp"]
    }
  }
}
```

To start a session:

1.  Open the **ACP Client** view from the activity bar.
2.  Run **ACP: Connect to Agent** from the Command Palette and choose **Antigravity**.
3.  Type a prompt in the **Chat** panel.

Note

The ACP Client extension is maintained by the community, not by Google. For the official Antigravity extension for VS Code, refer to [VS Code](/docs/ide/extensions/vscode).

![VS Code user settings.json registering Antigravity under acp.agents with command agy and args acp](/assets/image/docs/cli/acp-vscode-config.png)

### Zed

Add Antigravity as a custom agent server in your Zed `settings.json` (**zed: open settings file**):

```json
{
  "agent_servers": {
    "Antigravity": {
      "type": "custom",
      "command": "agy",
      "args": ["acp"]
    }
  }
}
```

To start a session, open the Agent Panel, click **+**, and choose **Antigravity** under **External Agents**.

![Zed settings.json registering Antigravity under agent\_servers with command agy and args acp](/assets/image/docs/cli/acp-zed-config.png)

![The Zed Agent Panel new-thread menu listing Antigravity under External Agents](/assets/image/docs/cli/acp-zed-new-thread.png)

### JetBrains IDEs

JetBrains IDEs (IntelliJ IDEA, PyCharm, GoLand, WebStorm, and others) run ACP agents in the **AI Chat** tool window, which comes with the **AI Assistant** plugin. If AI Chat asks you to install the plugin, click **Install Plugin**.

The IDE reads custom agents from `~/.jetbrains/acp.json`. Open it from the **AI Chat** tool window with **Add Custom Agent**, or create it yourself:

```json
{
  "agent_servers": {
    "Antigravity": {
      "command": "/absolute/path/to/agy",
      "args": ["acp"]
    }
  }
}
```

Use the absolute path from `which agy`. JetBrains IDEs don’t always inherit your shell’s `PATH`.

Reopen the **AI Chat** tool window, then pick **Antigravity** from the agent selector below the prompt box.

![IntelliJ IDEA AI Chat with Antigravity selected as the agent, showing a permission request with Allow and Deny buttons for an edit to main.py](/assets/image/docs/cli/acp-jetbrains-permission.png)

### Android Studio

In Android Studio, Antigravity is available via the ACP Registry. For installation, setup, and authentication instructions, refer to the dedicated [Android Studio](/docs/ide/extensions/android-studio) guide.

[Antigravity for Android Studio](/docs/ide/extensions/android-studio)Install and configure Google Antigravity in Android Studio from the ACP registry.

### Xcode

1.  Open **Xcode > Settings > Intelligence**.
2.  Under **Agents**, click **Add an Agent**.
3.  Set **Command** to the absolute path from `which agy`. Xcode doesn’t expand `~` or read your shell’s `PATH`.
4.  Set **Arguments** to `acp`, then click **Add**.

### Other clients

Any ACP client can launch Antigravity CLI. Configure it to run this command with the project directory as the working directory:

```bash
agy acp
```

The server speaks ACP protocol version 1 over `stdio` and identifies itself as `Antigravity ACP Server`.

## Work with the agent

After you connect, prompt the agent the same way you would in the terminal. The editor shows each step of the turn:

*   **Tool calls** appear as they run, with the command or file they touch.
*   **Edits** stream back as diffs, so you can review a change in the editor.
*   **Permission requests** pause the turn until you allow or deny the action.
*   **Slash commands** that Antigravity CLI supports appear in the client’s command menu.
*   **Conversation titles** update automatically as the session progresses.
*   **Images and embedded resources**: Paste images or attach files as context in your prompt.
*   **Questions**: When the agent asks a question, clients that support ACP elicitation forms show a native form. Other clients show the question in chat.
*   **Steering**: Sending a prompt while a turn runs steers that turn instead of starting a new one.
*   **Cancel**: Cancelling a turn ends open tool calls and abandons pending permission requests.

![A Zed permission card asking to allow or deny a git command requested by Antigravity](/assets/image/docs/cli/acp-zed-permission.png)

![Antigravity's inline diff, python3 run, and execution output in the Zed Agent Panel next to the edited main.py](/assets/image/docs/cli/acp-zed-result.png)

### Models and thinking level

The server exposes two session options that clients show as pickers:

| Option | Values |
| --- | --- |
| Model | The models available to your account |
| Thinking level | `Low`, `Medium`, `High`, `Extra`, `Max` |

Gemini models are available in every client. Third-party models are only offered to JetBrains IDEs (including JetBrains Air), Android Studio, Android Performance Analyzer, Zed, and Xcode.

### Permissions

When the agent wants to run a command or change a file, the client shows a permission request with **Allow** and **Deny** options. Your [permission rules](/docs/permissions) still apply: actions that your rules already allow or deny don’t prompt.

To skip prompts entirely, add `--dangerously-skip-permissions` to the agent’s `args`. Only do this in a [sandboxed](/docs/sandbox) or disposable environment.

### Sessions

The server supports loading, resuming, listing, and closing sessions. Clients that support these ACP features can reopen a previous Antigravity conversation instead of starting a new one. Resuming a session reopens the conversation without replaying its history. Editors with multi-root workspaces, such as Zed, can also send extra workspace folders.

## Authentication

`agy acp` uses the credentials you cached with an interactive `agy` session. If no credentials are available, requests fail with the error `Authentication required` (code `-32000`), and the client can ask you to sign in with one of these methods:

| Method | ID | Notes |
| --- | --- | --- |
| Log in with Google | `oauth-personal` | Opens a browser sign-in for a personal Google account |
| Log in with Gemini Enterprise | `oauth-business` | Opens a browser sign-in for a Gemini Enterprise account |
| Gemini API key | `gemini-api-key` | Reads `GEMINI_API_KEY` from the agent’s environment |
| Gemini Enterprise Agent Platform | `agent-platform` | Formerly Vertex AI. Uses Application Default Credentials with `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`, or `gcp.project` and `gcp.location` in `settings.json` |
| Log in from the terminal | `terminal-login` | Signs in with your Google account by pasting a code in a terminal. Works over SSH. Only offered to clients that support ACP terminal authentication |

To pass an API key through the editor, set it in the agent’s environment. For example, in Zed:

```json
{
  "agent_servers": {
    "Antigravity": {
      "type": "custom",
      "command": "agy",
      "args": ["acp"],
      "env": { "GEMINI_API_KEY": "<your-api-key>" }
    }
  }
}
```

Caution

Editor settings files are stored in plain text and are often synced or shared. Don’t commit a settings file that contains an API key. Where possible, sign in with `agy` instead, or export `GEMINI_API_KEY` in the environment that launches your editor.

## Flags

Add flags after `acp` in the client’s `args` list, for example `["acp", "--sandbox"]`.

| Flag | Default | Description |
| --- | --- | --- |
| `--add-dir` | — | Add a directory to the workspace. Repeat for more directories. |
| `--agent` | — | Agent to use for ACP sessions (refer to `agy agents`) |
| `--sandbox` | `false` | Run with terminal sandbox restrictions enabled |
| `--dangerously-skip-permissions` | `false` | Auto-approve all tool permission requests |
| `--process-per-session` | `false` | Serve each session from an isolated worker process. Required for HTTP MCP servers that your editor configures. |
| `--ide-mcp-port` | — | Port of the editor’s MCP server to expose its tools to the agent. Requires `nc` on `PATH`. |
| `--login` | `false` | Sign in with Google interactively in the terminal by pasting a code, then exit. Works over SSH. |
| `--log-file` | — | Write the ACP server log to this path |
| `--disable-telemetry` | `false` | Disable telemetry for this server |

## Troubleshooting

**The agent doesn’t start.** Run `agy acp --help` in a terminal to confirm that your installed version includes ACP. If it works in the terminal but not in the editor, replace `agy` with the absolute path from `which agy`.

**Requests fail with `Authentication required`.** Run `agy` interactively once to sign in, or pass credentials through the agent’s environment as shown in [Authentication](#authentication).

**Sign-in fails over SSH or without a browser.** Run `agy acp --login` in a terminal on that machine, then retry. Alternatively, use a Gemini API key.

**You need more detail.** The server writes logs to `~/.gemini/antigravity-cli/log/acp-*.log`. Use `--log-file` to choose a different path.

## Next steps

*   **[Permissions](/docs/permissions)**: Configure which actions the agent can take without asking.
*   **[MCP](/docs/mcp)**: Connect MCP servers to give the agent more tools.
*   **[Headless mode](/docs/cli/headless)**: Run the agent non-interactively in scripts and CI.
*   **[Reference](/docs/cli/reference)**: Full command and flag reference.