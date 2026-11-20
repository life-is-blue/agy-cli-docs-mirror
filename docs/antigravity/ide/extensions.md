# IDE extensions

Antigravity IDE extensions bring Google’s agentic development platform directly into your favorite editor. Without switching your development environment, you can converse with agents in dedicated side panels, review granular inline diffs, inspect interactive plans, and execute multi-step engineering tasks natively within your daily workflow.

* * *

## Supported IDEs and editors

### Visual Studio Code

Lightweight extension in the VS Code Marketplace for macOS, Linux, and Windows.

[Install & VS Code Guide](/docs/ide/extensions/vscode)

![Antigravity in Visual Studio Code](/assets/image/blog/vscode-extension-marketplace.png)

### Visual Studio

Official VSIX extension for Visual Studio 2026 and .NET solution architectures.

[Install & Visual Studio Guide](/docs/ide/extensions/visual-studio)

![Antigravity in Visual Studio 2026](/assets/image/blog/visual-studio-extension-marketplace.png)

### JetBrains

One-click installation for IntelliJ IDEA, PyCharm, WebStorm, GoLand, CLion, Rider, and more.

[Install & JetBrains Guide](/docs/ide/extensions/jetbrains)

![Antigravity in JetBrains IDEs](/assets/image/blog/jetbrains-extension-marketplace.png)

### Android Studio

Agentic coding with Google Antigravity inside the Android Studio Agent tool window via the ACP Registry.

[Install & Android Studio Guide](/docs/ide/extensions/android-studio)

![Antigravity in Android Studio](/assets/image/blog/android-studio-extension-marketplace.png)

### Zed

High-performance, native agentic editing in the Zed editor.

[Install & Zed Guide](/docs/ide/extensions/zed)

![Antigravity in Zed](/assets/image/blog/zed-extension-marketplace.png)

### Xcode

Native agentic development inside Xcode for macOS, iOS, iPadOS, watchOS, and visionOS.

[Install & Xcode Guide](/docs/ide/extensions/xcode)

![Antigravity in Xcode](/assets/image/blog/xcode-extension-marketplace.png)

### Eclipse

Agentic workflows, multi-step task execution, and diff reviews inside Eclipse on macOS, Linux, and Windows.

[Install & Eclipse Guide](/docs/ide/extensions/eclipse)

### Other editors and tools (ACP)

Antigravity also works in other editors that support the [Agent Client Protocol (ACP)](https://agentclientprotocol.com). Antigravity CLI includes an ACP server, `agy acp`, that these editors launch to run the agent in their own chat panel. Available features depend on the editor.

[Other editors (ACP)](/docs/ide/extensions/acp)Connect VS Code, Zed, JetBrains IDEs, Android Studio, Xcode, and other ACP clients to Antigravity CLI.

* * *

## Authentication and licensing

Antigravity uses a unified authentication system across all IDE extensions, the Antigravity CLI, and the Antigravity App (desktop). Your sign-in determines your model entitlements, quota limits, and data privacy policies.

### Individual developers

If you are an individual developer, you can sign in with any personal Google Account:

1.  Click the Antigravity icon in your editor’s activity bar or tool window and click **Sign In**.
2.  Complete authentication in your default web browser.
3.  Your session automatically connects to your account to use your plan’s model credits and rate limits (including the free tier).

[Antigravity pricing and plans](/pricing)Explore available plans, credit limits, and developer pricing.

### Enterprise teams and organizations

For enterprise developers, Antigravity integrates directly with **Gemini Enterprise** and Google Cloud governance (currently in **Preview** for Android Studio):

1.  Click **Sign In** and select **Sign in with Gemini Enterprise**.
2.  Authenticate using your corporate identity (including BYOID and Workforce Identity Federation).
3.  Select your target **Google Cloud Project** and **Region** when prompted.
4.  **Enterprise guarantees**: Review the following enterprise protections:
    *   **Data privacy**: Your code, prompts, and agent transcripts are **never** used to train Google foundation models.
    *   **Compliance**: All agent interactions operate under the enterprise-grade Google Cloud Terms of Service.
    *   **Security**: Respects your organization’s IAM policies, VPC Service Controls (VPC-SC), and custom dual-region or sovereign cloud boundaries.

[Gemini Enterprise documentation](/docs/enterprise)Learn more about enterprise deployment, IAM role mapping, VPC Service Controls, and data residency.