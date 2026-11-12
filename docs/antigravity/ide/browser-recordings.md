# Browser recordings

Available on: Antigravity IDE

In Antigravity IDE (`v2.6.0+`), the browser subagent runs when you type [`/browser`](/docs/commands/browser) in the Antigravity panel. It drives your own Google Chrome through the Chrome DevTools MCP server (`npx`), so Node.js must be on your `PATH` and Chrome must already be running locally with remote debugging turned on. For setup steps, refer to [Set up Chrome](/docs/commands/browser#set-up-chrome).

When the subagent interacts with a page, such as clicking, typing, or filling in a form, Antigravity IDE can record those actions as a WebM video. Recording isn’t guaranteed: sessions that only open pages or take screenshots don’t produce a recording, and a session that interacts with a page might not produce one either.

When a recording is produced, it’s saved as `recording.webm` in the browser subagent’s artifacts after the subagent finishes, and the agent lets you know it’s available.