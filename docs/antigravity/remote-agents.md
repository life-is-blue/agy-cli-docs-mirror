# Remote Agents

Available on: Antigravity App

Antigravity Remote Agents run your agent sessions and tools in an isolated, Google-managed remote environment rather than on your local machine.

Because execution happens remotely, Remote Agents continue working on long-running tasks and executing commands even when you close your browser, put your laptop to sleep, or switch between desktop and mobile devices.

Availability

Remote Agents is available to **Google AI Pro** and **Google AI Ultra** subscribers who sign in with a personal Google Account, and is rolling out gradually. It isn’t available on the free plan, on Google AI Plus, or for business accounts (Google Workspace or Google Cloud).

## Remote Agents vs. Remote Control

Antigravity provides two ways to work with agents remotely depending on where your code and tools live. Use the following table to compare **Remote Agents** and **[Remote Control](/docs/remote-control)**:

| Feature | Remote Agents | [Remote Control](/docs/remote-control) |
| :-- | :-- | :-- |
| **Execution environment** | Isolated, Google-managed remote environment | Your own desktop workstation or server |
| **Host machine requirement** | Runs independently; no local machine needs to stay on | Requires your host machine to remain powered on and online |
| **Workspace and files** | Remote **Resources** (GitHub repositories, Google Drive files, and uploaded files) | Local filesystem folders, local toolchains, and Git worktrees |
| **Best for** | Repository tasks, mobile workflows, and background execution while away | Tasks that require local hardware, local dev servers, or uncommitted local checkouts |

## Getting started

You can launch and manage Remote Agents from the **Antigravity App** on your desktop or directly from any web browser at [antigravity.google.com](https://antigravity.google.com).

### Start in the Antigravity App

To create a remote project alongside your local projects in the Antigravity App, do the following:

1.  In the left sidebar, click **+** next to **Projects** (or open the project selector in the message box) and select **New Remote Project**.
2.  _(Optional)_ Click **Add Resource** to attach GitHub repositories, Google Drive files, or uploaded files from your computer, and then click **Next** (or **Skip** if you do not add any resources yet).
3.  Enter a name in **Set Project Name** and click **Create**.
4.  Select your remote project and send a prompt in the message box to start a remote conversation.

You can also start a remote project directly from a GitHub repository in the message box:

1.  In the message box, click the project selector dropdown.
2.  Select **Remote** > **GitHub Repositories**. If you have not connected your GitHub account yet, click **Connect GitHub** to authorize access.
3.  Choose a repository from the list. Antigravity automatically selects an existing remote project for that repository or creates a new one.

### Start on the web

To use Remote Agents from a desktop or mobile browser without installing a local application, do the following:

1.  Open your browser and navigate to [antigravity.google.com](https://antigravity.google.com).
2.  Sign in with a personal Google Account on an eligible plan (Google AI Pro or Google AI Ultra).
3.  Enter a prompt in the message box to start a standalone remote conversation, or click **Create Project** next to **Projects** in the left sidebar to configure a project with GitHub repositories, Google Drive files, or uploaded files.

### Switch between Remote Agents and Remote Control

If you also use [Remote Control](/docs/remote-control) to connect to local Antigravity App or Antigravity CLI instances, use the instance switcher on [antigravity.google.com](https://antigravity.google.com) (in the left sidebar above **Settings** on desktop browsers, or in the top bar on mobile) to switch between **Remote Conversations** and any of your connected host machines.

## Remote projects and resources

While local [projects](/docs/projects) mount directories from your workstation under **Folders**, remote projects attach external context under **Resources**. You can attach or remove resources when creating a remote project, or at any time under **Project Settings** > **Resources** by clicking **Add Resource**:

*   **GitHub**: Authorize GitHub with OAuth and select one or more repositories to attach to the project. Conversations automatically clone and mount your connected repositories into the remote workspace for development. All private repositories within the same project must belong to the same GitHub user or organization owner; to work with private repositories from multiple owners, create a separate remote project for each owner.
*   **Google Drive**: Select files or folders from your Google Drive (using the Google Drive Picker on the web interface or the Drive file list in the Antigravity App), such as Google Docs, Sheets, Slides, PDFs, or folders. The remote agent reads attached Drive files on demand during conversations.
*   **Uploaded files**: Upload local files from your device (up to 8 MiB per file, 50 files and 100 MiB per project, and 2 GiB total across your account), including source code, text and data files, images, PDFs, and `.zip` archives. Uploaded files persist across conversations in the project and are staged under `/home/antigravity/upload`.

## Plugins and credentials

Remote Agents support [plugins](/docs/plugins) that connect your agent to external tools and services:

1.  Open **Customizations** in the left sidebar and select the **Marketplace** tab (under **Apps**, or **Installed** once connected).
2.  Browse available plugins, such as **GitHub**, **Google Drive**, **Google Docs**, **Google Sheets**, **Google Slides**, and **Google Calendar**.
3.  Click **Connect** next to a plugin to authorize your account with OAuth.

Your OAuth credentials are encrypted at rest and tokens are securely injected when the remote agent makes requests to authorized services.

* * *

## Next steps

Explore related documentation and guides:

*   [Remote Control](/docs/remote-control): Connect to and control local Antigravity App and CLI sessions running on your own machines.
*   [Projects](/docs/projects): Learn how projects organize workspaces, scoped settings, and conversations.
*   [Plugins](/docs/plugins): Configure plugins and external integrations across Antigravity surfaces.
*   [Permissions and security](/docs/permissions): Configure permission presets and fine-grained tool access rules.