# Agent side panel

Available on: Antigravity IDE

Use the **Agent** side panel in the editor to work directly with the agent. From the panel header, you can start a new conversation, open the sidebar to switch between your conversations, and search across conversations. In the prompt input, type `@` to mention files and other context, type `/` to run actions, click **+** to add files, folders, and other context, and select between [different models](/docs/models).

![The Agent side panel in the editor showing a new conversation, with the sidebar, search, and new conversation controls in the header and Gemini 4 Argon Medium selected in the prompt input's model picker](/assets/image/docs/editor/editor_agent_panel.png)

As your conversation progresses, the **Agent** side panel shows the agent’s work for each turn (expand **Worked for** to see the individual steps), its reply, and a summary of the files it changed with a **Review** button. While edits are waiting for your review, a bar above the prompt input (for example, **1 File With Changes**) lists each edited file with **Reject all** and **Accept all** buttons, and the edits are highlighted inline in the editor so you can [review each change](/docs/ide/review-changes-editor).

![An active conversation in the Agent side panel showing the agent's summary, a 1 file changed card with a Review button, and the 1 File With Changes bar with Reject all and Accept all, next to script.js with the agent's edits highlighted inline](/assets/image/docs/editor/agent_panel_toolbar.png)