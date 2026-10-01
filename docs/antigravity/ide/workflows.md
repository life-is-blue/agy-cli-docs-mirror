# Workflows

Upcoming migration to skills

Workflows are being deprecated in favor of **[Agent skills](/docs/ide/skills)** by November 1, 2026. Refer to the **[Workflows to skills migration guide](/docs/migration/workflows-to-skills)** or use the `/migrate-workflows` slash command in chat to automatically migrate your existing workflows to skills.

Workflows enable you to define a series of steps to guide the agent through a repetitive set of tasks, such as deploying a service or responding to PR comments. These workflows are saved as Markdown files, giving you a repeatable way to run key processes. Once saved, you can invoke workflows in the agent using a slash command with the format `/workflow-name`.

While rules provide models with persistent, reusable context at the prompt level, workflows provide a structured sequence of steps or prompts at the trajectory level, guiding the model through a series of interconnected tasks or actions.

Complete the following steps to create a workflow:

1.  Open the **Customizations** panel using the **…** menu at the top of the editor’s Agent panel.
2.  Navigate to the **Workflows** panel.
3.  Click **\+ Global** to create a new global workflow that you can access across all your workspaces, or click **\+ Workspace** to create a workflow specific to your current workspace.

To run a workflow, invoke it in the agent using the `/workflow-name` command. You can also call other workflows from within a workflow. For example, `/workflow-1` can include instructions such as “Call `/workflow-2`” and “Call `/workflow-3`”. Upon invocation, the agent sequentially processes each step defined in the workflow, performing actions or generating responses as specified.

Workflows are saved as Markdown files and contain a title, a description, and a series of steps with specific instructions for the agent to follow. Workflow files are limited to 12,000 characters each.

## Agent-generated workflows

You can also ask the agent to generate workflows for you. This works particularly well after you manually work with the agent through a series of steps, because it can use the conversation history to create the workflow.