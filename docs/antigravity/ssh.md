# Connect over SSH

Available on: Antigravity App

Connect the Antigravity App to a remote Linux machine over SSH in its own window. Antigravity sets up its remote server automatically over OpenSSH so your [projects](/docs/projects), agents, Git worktrees, terminals, and customizations run directly on the host, and running agents keep working even if you close the window or put your laptop to sleep.

Working in a terminal instead?

To use Antigravity inside your own `ssh` session, install the **Antigravity CLI** on the host. See [Remote SSH OAuth](/docs/install?tab=cli#remote-ssh-oauth-flow) and [Voice dictation over SSH](/docs/cli/commands/voice).

## Choose how to work remotely

Use this table to compare Antigravity’s remote options:

| Option | Where agents run | Client | Host setup |
| :-- | :-- | :-- | :-- |
| **Connect over SSH** | Your remote Linux machine | Antigravity App | None (automatic over OpenSSH) |
| **[Remote Control](/docs/remote-control)** | Your own desktop or server | Web browser ([antigravity.google.com](https://antigravity.google.com)) | Install and sign in to the App or CLI |
| **[Remote Agents](/docs/remote-agents)** _(Pro / Ultra)_ | Google-managed environment | App, CLI, or web browser | None (attach repos or files) |

## Requirements

Check that both machines meet these requirements:

*   **Local computer**: Antigravity App (`v2.33.0+` on macOS, Windows, or Linux) and OpenSSH (`ssh` or `ssh.exe` in `PATH`, or set `ANTIGRAVITY_SSH_BIN`).
*   **Remote OS**: 64-bit Linux (`x86_64` or `arm64`) with `glibc` 2.26+ (such as Ubuntu 18.04+, Debian 10+, or RHEL 8+). macOS, Windows, and `musl` Linux (such as Alpine) aren’t supported.
*   **SSH port forwarding**: `AllowTcpForwarding yes` (or `local`) in `sshd_config` on the host and any `ProxyJump` host.
*   **Storage and network**: Outbound HTTPS access and a writable, executable `$HOME` directory (`~/.antigravity-hub-server/` for the server and `~/.gemini/` for agent data).

## Connect to an SSH host

Connect to an SSH host from the Antigravity App sidebar, open a remote project folder, and switch or stop the remote server.

Follow these steps to open a remote host:

1.  Open the SSH dialog:
    
    *   **Sidebar** (**Software Engineering** layout): Click **Create New Project** next to **Projects** and choose **SSH Host…**, or open **Select Project** in the message box and pick a host under **SSH Host**.
    *   **Command palette**: Press Cmd + Shift + P (macOS) or Ctrl + Shift + P (Windows and Linux) and run **Connect to SSH Host…**.
    *   **Command line**: Launch the App with `--ssh-host=<destination>`.
2.  Select a host from **Recent** or **SSH Config** (from `~/.ssh/config`), or enter a `Host` alias, `[user@]host[:port]`, or `ssh://[user@]host[:port]`. Click **Choose File…** to use an alternate config file (`ssh -F`), or hover a row to **Remove from Recent** or **Hide from this list**.
    
3.  Click **Connect** and authenticate. Antigravity uses your OpenSSH keys, `ssh-agent`, and `ProxyJump` settings automatically. On macOS and Linux, host-key checks, passphrases, passwords, 2FA codes, and security-key touches appear in the app; on Windows, if interactive prompts aren’t shown, load your key into `ssh-agent` and run `ssh <host>` once in a terminal to record `known_hosts`.
    
4.  Sign in when the **`(SSH: <host>)`** window opens. Your local browser completes the OAuth flow and saves credentials on `<host>` (supporting personal Google Accounts, [Google Workspace](/docs/workspace), [Pay As You Go](/docs/pay-as-you-go), and [Gemini Enterprise](/docs/enterprise)).
    

## Work in an SSH window

Each host opens in its own window, marked **`(SSH: <host>)`** in the title bar and **`SSH: <host>`** at the bottom of the left sidebar:

*   **Projects and worktrees**: Click **Create New Project** next to **Projects** to browse the remote filesystem and run agents in **Local mode** or **New worktree mode**.
*   **Tools, terminal, and sandbox**: Agent tools, shell commands, the Linux [terminal sandbox](/docs/sandbox), [permissions](/docs/permissions), and side-panel terminals (Cmd + J on macOS, Ctrl + J on Windows and Linux) run on the host.
*   **Customizations**: [Skills](/docs/skills), [rules](/docs/rules), [hooks](/docs/hooks), [MCP servers](/docs/mcp), and [plugins](/docs/plugins) load from `~/.gemini/` and project folders on the host, with [sidecar panels](/docs/sidecars) and plugin or MCP OAuth sign-ins relayed over SSH.
*   **Shell environment**: On startup, the server loads your environment from `$SHELL -l -i` (10s timeout). Run **Stop SSH Server…** and reconnect after editing `~/.bashrc` or `~/.zshrc`, skip slow prompts when `ANTIGRAVITY_RESOLVING_ENVIRONMENT=1` is set, and guard `exec zsh` with `[ -t 0 ]`.

### Differences from a local window

A few local desktop features differ in an SSH window:

*   **Links and built-in browser**: The side-panel browser isn’t shown; `http` and `https` links open in your local default browser.
*   **`/browser` command**: [`/browser`](/docs/commands/browser) attaches to Google Chrome running **on the remote host** with remote debugging enabled (`chrome://inspect/#remote-debugging`), not on your local computer.
*   **Voice and media**: [Voice mode](/docs/voice-mode) and dictation prompt **Allow `<host>` to use your microphone?** for the current app session; camera and screen access stay disabled.
*   **Local file actions**: **Open in IDE**, **Reveal in Finder** (or File Explorer), and local external-editor links are hidden.

## Switch windows and stop the server

To open a local window without disconnecting, click **`SSH: <host>`** in the sidebar and select **This Computer** (or run **Switch to This Computer** from the command palette).

Closing the window leaves the remote server and agents running:

| Action | Window and SSH tunnel | Remote server and agents |
| :-- | :-- | :-- |
| **Close window** | Closes and disconnects SSH. | Keep running on `<host>`; reconnect anytime. |
| **Restart or update App** | Reopens open SSH windows and reconnects; prompts **Restart** or **Later** before updating a busy server. | Keep running unless restarted for an update. |
| **Sleep or network drop** | Retries automatically (**Reconnecting to `<host>`…**), or click **Reconnect**. | Keep running and reattach when back online. |
| **Stop SSH Server…** _(sidebar, command palette, or **Workspace** menu on Windows and Linux)_ | Closes and disconnects SSH. | Stops agents, sidecars, and the server on `<host>`. |

## Configure OpenSSH

Standard OpenSSH settings in `~/.ssh/config` work directly:

```text
Host devbox
  HostName 203.0.113.10
  User alice
  Port 2222
  IdentityFile ~/.ssh/id_ed25519
  ProxyJump jump.example.com
```

Keep these details in mind:

*   Concrete `Host` aliases (without `*`, `?`, or `!`) appear under **SSH Config**; wildcard rules like `Host *` still apply when connecting.
*   Antigravity overrides `ForwardAgent=no`, `ForwardX11=no`, `ControlMaster=no`, `ControlPath=none`, `RemoteCommand=none`, `ServerAliveInterval=15`, and `ServerAliveCountMax=3` on the `ssh` command line.
*   Custom config files (**Choose File…**, `ssh -F`) skip the system `ssh_config` and must not be writable by others (`chmod 600` on macOS and Linux; on Windows, use a local path without spaces when using `ProxyJump`).

## Troubleshooting

If a background connection fails, click **Show Details** on the **`Couldn't connect to <host>`** notification. Server logs live in `~/.antigravity-hub-server/data/ls-*.log` on the host. To uninstall, run **Stop SSH Server…** and delete `~/.antigravity-hub-server` on the host (plus `~/.gemini` to delete saved conversations and settings).

Use this table to resolve error codes:

| Error code | Cause and fix |
| :-- | :-- |
| `INVALID_DESTINATION` | Invalid host format or unbracketed IPv6 port. Use `[user@]host[:port]`, `user@[ipv6]:port`, `ssh://...` (`%40` for `@` in usernames), or a `Host` alias. |
| `SSH_CONFIG_INVALID` | `ssh` rejected the config file (invalid option, unsafe permissions, UTF-8 BOM/UTF-16 encoding, or a non-config file like `known_hosts`). Fix the reported line or choose another file. |
| `AUTH_FAILED` | SSH authentication failed. Test `ssh <host>` in a terminal and check `IdentityFile` or `ssh-add -l`. |
| `HOSTKEY_REJECTED` | Missing or changed entry in `~/.ssh/known_hosts`. Confirm the host change before running `ssh-keygen -R <host>`. |
| `CONNECTION_FAILED` / `CONNECTION_CLOSED` | `ssh` binary missing, host unreachable, or tunnel dropped. Check `ssh -V`, `ssh <host>`, or `ANTIGRAVITY_SSH_BIN`, then click **Reconnect**. |
| `FORWARDING_PROHIBITED` | Port forwarding disabled. Set `AllowTcpForwarding yes` (or `local`) in `sshd_config` on the host and any jump host. |
| `UNSUPPORTED_HOST` | Host isn’t 64-bit Linux (`x86_64`/`arm64`) with `glibc` 2.26+, or uses `musl` (such as Alpine). |
| `SHARED_HOME_UNSUPPORTED` | Another host sharing the same networked `$HOME` is running the server. Connect to that host, click **Take Over** when prompted to move the server here (stopping agents there), or separate `$HOME` per host. |
| `INSTALL_FAILED` | Install in `~/.antigravity-hub-server/` failed. Check disk space (`df -h ~`), verify `$HOME` isn’t `noexec`, install `gzip` if `curl`/`wget` is absent, and keep `~/.bashrc` silent on non-interactive shells. |
| `LS_START_FAILED` / `LS_STOPPED` | Remote server failed to start or exited. Check `~/.antigravity-hub-server/data/ls-*.log` and reconnect. |

## Next steps

Explore related documentation:

*   [Projects](/docs/projects): Organize remote folders, Git worktrees, and scoped settings.
*   [Remote Control](/docs/remote-control): Control Antigravity App and CLI sessions from any web browser.
*   [Remote Agents](/docs/remote-agents): Run tasks in a Google-managed remote environment.
*   [Permissions](/docs/permissions) and [Terminal sandbox](/docs/sandbox): Configure approvals and Linux command isolation.