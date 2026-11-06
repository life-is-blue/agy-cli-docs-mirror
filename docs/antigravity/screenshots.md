# Screenshots

Available on: Antigravity App, Antigravity IDE

The browser subagent can take a screenshot of the visible page or of a single element on it, for example to check how a page rendered. Ask for a screenshot in your prompt, or the subagent may take one on its own when the task calls for it.

To start the browser subagent, type `/browser` in the message box, select it from the menu, and describe the task. The subagent drives your own Google Chrome, which must already be running with remote debugging turned on. Chrome doesn’t need to be signed in. For setup steps, refer to the [Browser command](/docs/commands/browser).

In your conversation, the subagent appears in a row that reads **Starting** or **Started**, followed by a name the agent gives it, such as “Web Browser Automation Agent”. Click that name, or the subagent in the **Subagents** section of the conversation overview, to open its conversation in the side panel. Each screenshot is a step labeled with a short summary of what the subagent captured. Expand the step to see the tool’s arguments, its result, and a thumbnail of the screenshot.

![The browser subagent's conversation open in the side panel, with the step "Executed take screenshot of hero image in view" expanded to show its result, "Took a screenshot of the current page's viewport.", and a thumbnail of the Gemini 4 Argon blog post on antigravity.google with its hero image](/assets/image/docs/artifacts/browser-screenshot-tool-2-29.png)

A screenshot isn’t an artifact on its own. To comment on one, ask the agent to save it to the conversation’s artifacts, then open the image from the agent’s reply. Drag to select a region of the image, type your comment, and click **Add Comment**. Comments aren’t sent right away: they’re held as pending comments and go to the agent with your next message, or when you submit them from the **Review** button in the artifact’s header.

![A screenshot of the Gemini 4 Argon blog post on antigravity.google open as an image artifact, with a region over the post's hero image selected and a comment box below it reading "Make this image wider so the wordmark stands out." with Cancel and Add Comment buttons](/assets/image/docs/artifacts/browser-screenshot-comment-2-29.png)