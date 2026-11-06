# Jupyter notebooks

Available on: Antigravity App, Antigravity CLI, Antigravity IDE

Inspect Jupyter notebooks (`.ipynb`) directly alongside your conversation, switch between rendered cells and raw JSON, leave inline comments on specific cells, and collaborate with the agent to create, update, and run notebooks.

## Antigravity App

In the Antigravity App, `.ipynb` files open in a native notebook viewer in the side panel so you can read Markdown documentation, syntax-highlighted code cells, and cell outputs without leaving your conversation.

### Open a notebook

To open a `.ipynb` file in the side panel, do any of the following:

*   Click a `.ipynb` file link or `@`\-mention chip in a conversation.
*   Click **+** in the side panel header, choose **Open File**, and search for the `.ipynb` file.
*   Open the **Overview** panel and select the `.ipynb` file from the file list.

![The Antigravity App with agile\_classifiers.ipynb open in the side panel on the right, showing the Preview and Raw toggle in the header, a rendered Markdown heading, code cell 1 with Python syntax highlighting and text output, and code cell 2 with an inline ROC curve plot](/assets/image/docs/jupyter-notebooks/notebook-viewer.png)

### What the notebook viewer renders

The viewer supports standard `nbformat` v4 notebooks as well as legacy `nbformat` v3 (`worksheets`) notebooks:

| Element | How it renders |
| --- | --- |
| **Markdown cells** | Formatted Markdown, including headings, lists, links, inline code, tables, and images resolved relative to the notebook’s directory. |
| **Code cells** | Execution count gutter (`[1]`, `[2]`, or `[ ]` when unexecuted) next to syntax-highlighted code using the notebook’s language metadata (defaulting to Python). |
| **Image outputs** | Inline `image/png`, `image/jpeg`, and `image/gif` plots and figures. |
| **Text outputs** | Standard output (`stdout`), standard error (`stderr`), and plain-text execution results (`text/plain`). |
| **Error outputs** | Exception names, messages, and tracebacks highlighted in error styling. |

### Switch between Preview and Raw views

Use the **Preview** / **Raw** toggle in the side panel header to switch between the rendered notebook cells and the underlying `.ipynb` JSON text.

If a `.ipynb` file contains malformed JSON or an invalid notebook structure, Antigravity automatically falls back to the **Raw** view and disables the **Preview** button with a tooltip describing the parse error.

### Comment on notebook cells

You can leave inline comments on rendered notebook cells to point the agent to specific code or Markdown:

1.  Hover over a cell or select lines in the rendered notebook, then click **Add inline comment** (**+**).
    
2.  Type your feedback and click **Add Comment**.
    

Comments are anchored to the corresponding lines in the underlying `.ipynb` file and attached to your next message to the agent.

### Review notebook diffs

When you inspect changes in the **Review** pane or toggle **Show Diff** on a modified `.ipynb` file, Antigravity strips cell outputs before computing conversation turn diffs so diffs stay focused on your code and Markdown edits rather than large output payloads.

### Work with notebooks using the agent

You can ask the agent to read, create, update, or execute notebooks in your workspace:

*   **Reference a notebook**: Type `@` followed by the notebook name (for example, `@analysis.ipynb`) to attach it to your prompt.
*   **Create or update cells**: Ask the agent to add analysis steps, refactor functions, or generate a new `.ipynb` file.
*   **Execute notebooks**: Ask the agent to run a notebook from the terminal (for example, with `jupyter nbconvert --to notebook --execute --inplace` or `papermill`) and summarize the resulting outputs or errors.

## Antigravity CLI

In the Antigravity CLI, you can reference, inspect, create, update, and run Jupyter notebooks (`.ipynb`) from your terminal session:

*   **Reference a notebook**: Type `@` followed by the path to a `.ipynb` file (for example, `@notebooks/analysis.ipynb`) to include it in your prompt.
*   **Create or edit notebooks**: Ask the agent to generate a new `.ipynb` file or update existing cells and metadata.
*   **Run notebooks**: Ask the agent to execute cells via `jupyter nbconvert --to notebook --execute --inplace <notebook.ipynb>` or `papermill` and report the outputs.
*   **Inspect diffs**: Run `/diff` to review changes to `.ipynb` files; Antigravity strips cell outputs from turn diffs so code and Markdown changes remain easy to read.

## Antigravity IDE

In the Antigravity IDE, you can open `.ipynb` files directly in the editor’s interactive notebook interface to edit cells, select local or remote Jupyter kernels, and run cells interactively while collaborating with the agent in the side panel:

*   **Interactive execution**: Run individual cells or the full notebook in the editor and inspect rich outputs inline.
*   **Agent collaboration**: Reference the active notebook in the agent side panel to ask for new cells, debugging help, or refactoring.

## Next steps

*   Learn how to reference files and quote selections in [Mentions and quoting](/docs/at-mentions).
*   Inspect workspace edits in [Review changes](/docs/review-changes).
*   Explore other capabilities in [Features](/docs/features).