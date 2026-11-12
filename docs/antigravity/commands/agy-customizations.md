# Customizations command (/agy-customizations)

Available on: Antigravity App, Antigravity CLI, Antigravity IDE

Load the Antigravity customization reference into the agent’s context before you ask it to create, change, or explain a [rule](/docs/rules), [skill](/docs/skills), [plugin](/docs/plugins), [hook](/docs/hooks), or [MCP server](/docs/mcp) configuration.

## Overview

`/agy-customizations` is a built-in skill available in the Antigravity App, the Antigravity CLI, and the Antigravity IDE. Running the command gives the agent the **Antigravity Customization System Guide** for the rest of the conversation, so the agent works from the documented formats, locations, and precedence rules. The agent can also load the guide on its own when a request is about customizations; running the command makes sure it does. The guide covers:

*   **Customization types**: what rules, skills, plugins, hooks, and MCP servers are for, and which file or folder defines each one.
*   **Discovery and precedence**: where Antigravity looks for customizations, such as the `.agents/` folder in your project and `~/.gemini/config/`, and which one wins when two have the same name. For the full rules, refer to [Customization discovery](/docs/customization-discovery).
*   **How customizations are applied**: progressive disclosure for skills and `model_decision` rules, and deduplication of rule files.
*   **Discovery manifests**: loading skills and plugins from other folders with `skills.json` and `plugins.json`. For all manifest types and fields, refer to [Discovery manifests](/docs/customization-discovery#discovery-manifests).

Each customization type links to a detailed guide that the agent reads on demand, so the reference adds little to the context window until a request needs it.

## Run `/agy-customizations`

Type `/agy-customizations` followed by a request. The agent loads the guide, reads the sections that apply, and carries out the request as it would any other prompt:

```prompt
/agy-customizations create a PreToolUse hook that blocks git push --force
```

```text
/agy-customizations my deploy skill never shows up as /deploy, figure out why
```

```text
/agy-customizations should this be a rule or a skill?
```

To load the reference without a request, for example before a longer conversation about your project’s setup, run the command on its own.

## Next steps

Explore related documentation:

*   [Rules](/docs/rules): Give the agent persistent guidelines and constraints.
*   [Agent skills](/docs/skills): Teach the agent procedures it can run on demand or as slash commands.
*   [Plugins](/docs/plugins): Package customizations to share across projects and teams.
*   [Lifecycle hooks](/docs/hooks): Run commands at specific points in the agent loop.
*   [MCP servers](/docs/mcp): Connect the agent to external tools and services.
*   [Customization discovery](/docs/customization-discovery): See where Antigravity looks for customizations and which one wins.
*   [Learn command (`/learn`)](/docs/commands/learn): Turn corrections from the current session into rules and skills.
*   [Slash commands overview](/docs/slash-commands): Browse every available slash command.