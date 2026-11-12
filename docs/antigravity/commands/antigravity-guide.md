# Antigravity guide command (/antigravity-guide)

Available on: Antigravity App, Antigravity CLI

Ask the agent how to use Antigravity. `/antigravity-guide` gives the agent the official product documentation, so it can answer “how do I…” questions about the Antigravity App, the Antigravity CLI, the Antigravity IDE, and the Antigravity SDK without you leaving the conversation.

## Overview

`/antigravity-guide` is a built-in skill available in the Antigravity App and the Antigravity CLI. Running the command gives the agent a quick-reference guide for each Antigravity surface and a sitemap of the official documentation. The agent can also load this skill on its own when you ask how to use Antigravity, even without the slash command:

*   **Antigravity CLI**: slash commands, flags, settings, and best practices.
*   **Antigravity IDE**: Tab completion, inline commands, the chat panel, and editor integrations.
*   **Antigravity App**: the sidebar, chat canvas, and agent settings and permissions.
*   **Antigravity SDK**: installing the Python SDK, a quickstart with the `Agent` class, streaming responses and tool calls, and an interactive chat loop.

For questions the quick references don’t cover, such as recent changes or advanced integrations, the agent fetches the relevant page from [antigravity.google/docs](/docs) and answers from the current documentation. Reading a documentation page is a web read, so depending on your [permission preset](/docs/permissions), the agent might ask for approval before it reads `antigravity.google`.

## Run `/antigravity-guide`

Type `/antigravity-guide` followed by your question. Ask the way you’d ask a teammate; the agent picks the right reference and links to the documentation page when there’s more to read:

```prompt
/antigravity-guide how do I run the CLI in headless mode in GitHub Actions with a JSON schema?
```

```prompt
/antigravity-guide where do I change the permission preset for this project?
```

```prompt
/antigravity-guide what's the keyboard shortcut for the inline command in the IDE?
```

Note

`/antigravity-guide` answers questions about using Antigravity. To have the agent create or debug a customization, such as a rule, skill, hook, plugin, or MCP server, use `/agy-customizations` instead, which loads the customization reference.

## Next steps

Explore related documentation:

*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.
*   [Antigravity CLI reference](/docs/cli/reference): Flags, subcommands, and CLI slash commands.
*   [Settings](/docs/settings): Configure the Antigravity App and CLI.
*   [Antigravity SDK overview](/docs/sdk/overview): Build on Antigravity programmatically.