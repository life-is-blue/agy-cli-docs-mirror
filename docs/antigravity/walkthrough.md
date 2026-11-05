# Walkthrough

Available on: Antigravity App, Antigravity IDE

The agent creates walkthrough artifacts when it completes task implementation. This type of artifact includes a concise summary of the changes made to remind you of what happened in the active conversation. Walkthroughs help you get up to speed with the state of your codebase after the agent makes changes, even if you weren’t following every step in real time.

![A walkthrough open in the side panel of the Antigravity App, with Changes Made and Validation Results sections for the GET /v1/bookmarks/ endpoint, including the npm test output with 6 passing tests, next to the conversation that produced it](/assets/image/docs/artifacts/artifact-walkthrough.png)

For browser tasks, you can ask the agent to embed screenshots of what it built or checked in the browser in the walkthrough. When you plan with [`/plan`](/docs/plan), the agent is asked to include screenshots, and recordings when available, in the walkthrough to show UI changes.

![A walkthrough titled "Google Antigravity Homepage Walkthrough" open in the Antigravity App, with an embedded browser screenshot of the antigravity.google homepage hero captioned "Google Antigravity Homepage Hero", a note summarizing the hero section, and the start of a Key Features & Platform Surfaces section](/assets/image/docs/artifacts/artifact-walkthrough-browser-2-29.png)