# Antigravity IDE: Tab and navigation

Available on: Antigravity IDE

This guide covers the core navigation and completion tools: **Supercomplete** and **Tab-to-Jump**.

## Supercomplete

Supercomplete provides code suggestions in a region near your current cursor position.

![Supercomplete in main.py after a punctuation parameter is added to greet: it suggests a default value of "!" for the parameter and replaces the hard-coded ! in the f-string with punctuation](/assets/image/docs/editor/supercomplete.png)

### How it works

Supercomplete includes the following capabilities:

*   **File-wide suggestions**: Suggestions can modify code throughout the document, handling tasks like changing variable names or updating separate function definitions simultaneously.
*   **Inline preview**: Suggested insertions appear as gray text in the editor, and suggested deletions are highlighted in red and struck through.
*   **Missing imports**: Supercomplete can also suggest a missing import at the top of the file.
*   **Accepting**: Press `Tab` to accept the changes, or press `Esc` to dismiss them.

## Tab-to-Jump

Tab-to-Jump is a fluid navigation tool that suggests the next logical place in your document to move your cursor to.

![main.py after math is renamed to math\_lib on lines 1 and 4, with a Tab to Jump label at the end of line 9, where math.e still uses the old name](/assets/image/docs/editor/tab_to_jump.png)

### How it works

Tab-to-Jump works in the following ways:

*   **Navigation**: A **Tab to Jump** label appears at the end of the line where Antigravity predicts your next edit, for example after you accept a suggestion.
*   **Accepting**: Press `Tab` to immediately move your cursor to that location.

## Settings

To customize these features, click **Tab Settings** in the status bar:

*   **Suggestions in Editor**: Turns Tab suggestions in the editor on or off.
*   **Tab Speed**: Controls the responsiveness of suggestions:
    *   `Fast`: Provides rapid-fire suggestions. This is the default.
    *   `Slow`: Waits for more context before suggesting.
*   **Tab to Jump**: Turns Tab-to-Jump on or off.