# MCP Apps development command (/mcp-app-development)

Available on: Antigravity App

Load the built-in MCP Apps development guide into the agent’s context before you ask it to build, theme, package, or debug an interactive [MCP App](/docs/mcp-apps) plugin.

Note

`/mcp-app-development` is available in the Antigravity App. The Antigravity CLI and Antigravity IDE do not render interactive `ui://` MCP App views.

## Overview

`/mcp-app-development` runs a built-in [skill](/docs/skills) in the Antigravity App. Running the command gives the agent the full Antigravity MCP Apps reference for the rest of the conversation, so it scaffolds and debugs against the exact host requirements:

*   **UI resources and bundling**: Single-file `ui://` HTML resources (`text/html;profile=mcp-app`), default-deny CSP allowlisting, and `@modelcontextprotocol/ext-apps` bridge wiring.
*   **Antigravity entrypoints**: Inline chat cards, side panel (`aux_pane`), and full-page (`global`) entrypoints under `_meta["com.google.antigravity/ui"]`.
*   **Theming and host actions**: Host CSS variables, `tools/call`, `ui/message`, `ui/update-model-context`, and `com.google.antigravity/toggle-aux-pane`.
*   **Plugin packaging and debugging**: `mcp_config.json` with `${PLUGIN_ROOT}` and `${PLUGIN_DATA}`, `plugin.json`, and troubleshooting blank frames or CSP blocks.

The agent can also load this skill automatically when you ask it to build or debug an MCP App. Prefixing your prompt with `/mcp-app-development` ensures the skill loads on the first turn.

## Run `/mcp-app-development`

Type `/mcp-app-development` followed by your request in the message box, or type `/` and select **mcp-app-development** from the menu:

```prompt
/mcp-app-development Build an MCP App plugin for Antigravity that tracks release checklist items inline in chat and in a side panel board using @modelcontextprotocol/ext-apps.
```

```prompt
/mcp-app-development Add a full-page global entrypoint and host theme CSS variables to my existing MCP App plugin.
```

```prompt
/mcp-app-development Debug why my inline MCP App step renders blank and check my CSP resourceDomains and resources/read MIME type.
```

## Next steps

Explore related documentation:

*   **[MCP Apps](/docs/mcp-apps)**: Overview of MCP App surfaces, Antigravity extensions, and host limits.
*   **[MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview)**: Concepts and architecture on `modelcontextprotocol.io`.
*   **[`@modelcontextprotocol/ext-apps` API reference](https://apps.extensions.modelcontextprotocol.io/api/)**: Client and server SDK documentation.
*   **[Build plugins](/docs/build-plugins)**: Package `plugin.json`, `mcp_config.json`, and skills, and publish to the Marketplace.
*   **[Customizations command (`/agy-customizations`)](/docs/commands/agy-customizations)**: Load the general customization reference for rules, skills, plugins, hooks, and MCP servers.
*   **[Slash commands overview](/docs/slash-commands)**: Browse every available slash command.