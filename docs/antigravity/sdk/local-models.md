# Run agents with local models

Run Antigravity agents on your machine using local models without an API key or internet connection.

Depending on your setup, you can configure local model execution using the following classes:

*   **[`LiteRTAgentConfig`](#on-device-execution-with-litert)**: Runs `.litertlm` model checkpoints (such as [Gemma 4 26B A4B](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)) directly on-device using Google AI Edge’s [LiteRT](https://developers.google.com/edge/litert-lm/overview) runtime.
*   **[`LocalOpenAIAgentConfig`](#external-openai-compatible-servers)**: Connects to an external local server with an OpenAI-compatible API, such as [Ollama](https://ollama.com), [LM Studio](https://lmstudio.ai), or [vLLM](https://docs.vllm.ai).

## On-device execution with LiteRT

`LiteRTAgentConfig` runs local models using the LiteRT runtime. When the agent starts, the SDK spins up and manages a local loopback server backed by your `.litertlm` checkpoint. Supported hardware backends (`gpu` for Apple Silicon Metal and NVIDIA CUDA, or `npu`) are detected automatically at startup.

### Set up LiteRT and Gemma 4 26B A4B

Follow these steps to install the dependencies and import the model checkpoint:

> **Note:** A machine with at least 24 GB of VRAM or unified memory is recommended to run the Gemma 4 26B A4B checkpoint (which downloads about 16.8 GB).

1.  Create and activate a virtual environment:
    
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    
2.  Install the SDK and the `litert-lm` package:
    
    ```bash
    pip install google-antigravity litert-lm
    ```
    
3.  Use the `litert-lm` CLI to import the Gemma 4 26B A4B checkpoint:
    
    ```bash
    litert-lm import \
      --from-huggingface-repo=litert-community/gemma-4-26B-A4B-it-litert-lm \
      gemma-4-26B-A4B-it-gpu.litertlm \
      gemma4-26b
    ```
    
    This command downloads about 16.8 GB and registers the checkpoint at `~/.litert-lm/models/gemma4-26b/model.litertlm`.
    
    > **Note:** On macOS, if `litert-lm import` fails with an SSL certificate verification error, install `certifi` and export `SSL_CERT_FILE` before retrying:
    > 
    > ```bash
    > pip install certifi
    > export SSL_CERT_FILE=$(python3 -c "import certifi; print(certifi.where())")
    > ```
    

### Run a local LiteRT agent

Once you have configured LiteRT, run a local LiteRT agent by passing the `.litertlm` model file in `LiteRTAgentConfig`. For example:

> **Note:** Use the full path to your model file or use `os.path.expanduser()` because tilde (`~`) isn’t expanded automatically.

```python
import asyncio
import os

from google.antigravity import Agent, LiteRTAgentConfig

MODEL_PATH = os.path.expanduser(
    "~/.litert-lm/models/gemma4-26b/model.litertlm"
)


async def main():
    config = LiteRTAgentConfig(model_path=MODEL_PATH)

    async with Agent(config) as agent:
        response = await agent.chat("What files are in the current directory?")
        async for token in response:
            print(token, end="", flush=True)
        print()


if __name__ == "__main__":
    asyncio.run(main())
```

If you want to let the local agent edit files and run shell commands in a project directory, set `workspaces` and attach a tool policy. For example:

```python
import asyncio
import os

from google.antigravity import Agent, LiteRTAgentConfig
from google.antigravity.hooks import policy


async def main():
    workspace = os.path.expanduser("~/my-local-project")
    os.makedirs(workspace, exist_ok=True)

    config = LiteRTAgentConfig(
        model_path=os.path.expanduser(
            "~/.litert-lm/models/gemma4-26b/model.litertlm"
        ),
        workspaces=[workspace],
        policies=[policy.allow_all()],
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Create a static webpage index.html with a dark-mode toggle."
        )
        async for token in response:
            print(token, end="", flush=True)
        print()


if __name__ == "__main__":
    asyncio.run(main())
```

### Vision support

Use `LiteRTAgentConfig` to analyze images on-device with vision-capable `.litertlm` checkpoints (such as Gemma 4 26B A4B). This supports offline and hybrid visual workflows such as UI verification, screenshot debugging, and diagram analysis.

At startup, `LiteRTAgentConfig` inspects your checkpoint with `litert_lm.ModelInfo` to detect vision support and select the default hardware backend (`"gpu"` or `"cpu"`). You can also pass an explicit `vision_backend` override. Pass images alongside text prompts in `agent.chat()` using `from_file()` or `Image` (see [Multimodal attachments](/docs/sdk/structured-output#multimodal-attachments)):

```python
import asyncio
import os

from google.antigravity import Agent, LiteRTAgentConfig, from_file

MODEL_PATH = os.path.expanduser(
    "~/.litert-lm/models/gemma4-26b/model.litertlm"
)


async def main():
    config = LiteRTAgentConfig(
        model_path=MODEL_PATH,
        # Optional: override the auto-detected vision backend ("gpu" or "cpu")
        # vision_backend="gpu",
    )

    async with Agent(config) as agent:
        response = await agent.chat([
            "Inspect this UI screenshot and check for layout issues:",
            from_file("screenshot.png"),
        ])
        async for token in response:
            print(token, end="", flush=True)
        print()


if __name__ == "__main__":
    asyncio.run(main())
```

Note

On-device vision requires `google-antigravity >= 0.1.24`, `litert-lm >= 0.19.1` (`pip install -U google-antigravity litert-lm`), and a vision-capable `.litertlm` checkpoint. If you imported `gemma4-26b` before vision support was added, re-run the `litert-lm import` command above (with `gemma-4-26B-A4B-it-gpu.litertlm`) to fetch the vision-capable weights.

### Prefix caching

`LiteRTAgentConfig` automatically caches conversation prefixes across sequential agent turns with zero configuration changes. When the conversation prefix and tool schemas match the previous turn, the managed LiteRT-LM session reuses its in-memory KV cache instead of recomputing static system instructions, tool schemas, and prior history. LiteRT-LM prefills only newly added prompts and tool outputs, which reduces latency during multi-step tool calling.

LiteRT-LM persists compiled model graphs next to `model_path` by default. To override the on-disk compilation cache directory, create the directory first and pass its expanded path via `cache_dir`. LiteRT-LM does not expand tilde (`~`) automatically, and `litert_lm.Engine` requires the directory to already exist:

```python
cache_dir = os.path.expanduser("~/.litert-lm/cache")
os.makedirs(cache_dir, exist_ok=True)

config = LiteRTAgentConfig(
    model_path=MODEL_PATH,
    cache_dir=cache_dir,
)
```

### LiteRT configuration options

`LiteRTAgentConfig` automatically applies the `.lightweight()` preset when initialized. This preset restricts built-in tools to core coding operations, trims system instructions for smaller context windows, and sets a default context compaction threshold sized for the 64k LiteRT KV-cache.

In addition to standard [`AgentConfig`](https://github.com/google-antigravity/antigravity-sdk-python/blob/main/google/antigravity/connections/README.md#agentconfig) fields (`tools`, `policies`, `hooks`, `mcp_servers`, `subagents`, `workspaces`, and `system_instructions`), [`LiteRTAgentConfig`](https://github.com/google-antigravity/antigravity-sdk-python/blob/main/google/antigravity/connections/local/litert_connection_config.py) supports the following options:

| Key | Type | Default | Allowed values | Description |
| :-- | :-- | :-- | :-- | :-- |
| **`model_path`** | `str` | _Required_ | Absolute `.litertlm` file path | Path to the local `.litertlm` model checkpoint file. |
| **`backend`** | `LiteRTBackend` or `str` | `LiteRTBackend.GPU` | `'gpu'`, `'npu'`, `'cpu'` | Hardware backend used for model inference. |
| **`vision_backend`** | `LiteRTBackend`, `str`, or `None` | `None` (auto-detected) | `'gpu'`, `'npu'`, `'cpu'`, `None` | Hardware backend override for vision processing. When `None`, `LiteRTAgentConfig` inspects `litert_lm.ModelInfo` and selects `'gpu'` or `'cpu'`. |
| **`audio_backend`** | `LiteRTBackend`, `str`, or `None` | `None` | `'gpu'`, `'npu'`, `'cpu'`, `None` | Hardware backend override for audio processing. |
| **`enable_speculative_decoding`** | `bool` | `False` | `True`, `False` | Enables multi-token prediction for faster generation. |
| **`cache_dir`** | `str` or `None` | `None` | Existing expanded directory path or `None` | Overrides the default on-disk compilation cache location (when `None`, LiteRT-LM persists compiled artifacts next to `model_path`). Tilde (`~`) is not expanded automatically, and the directory must already exist on disk (use `os.path.expanduser()` and `os.makedirs(..., exist_ok=True)`). |
| **`port`** | `int` | `0` | `0` or TCP port | Local loopback port for the managed LiteRT server (`0` selects an available port automatically). |
| **`compaction_config`** | `CompactionConfig` or `None` | `token_threshold=40960` | `CompactionConfig` or `None` | Overrides the default context compaction threshold derived from the 64k LiteRT KV-cache. |

## External OpenAI-compatible servers

To connect to an external local server that exposes an OpenAI-compatible API (such as Ollama, LM Studio, or vLLM), use `LocalOpenAIAgentConfig`. Call `.lightweight()` on the configuration to apply the tool and prompt optimizations designed for local models if needed.

> **Note:** Don’t use `LocalOpenAIAgentConfig` to connect to `litert-lm serve`. Use `LiteRTAgentConfig` instead so the SDK manages the LiteRT server lifecycle for you.

For example, you can connect an agent to a local Ollama server running Gemma 4:

```python
import asyncio
from google.antigravity import Agent, LocalOpenAIAgentConfig


async def main():
    config = LocalOpenAIAgentConfig(
        model="gemma4:26b",
        base_url="http://localhost:11434/v1",
    ).lightweight()

    async with Agent(config) as agent:
        response = await agent.chat("What files are in this directory?")
        async for token in response:
            print(token, end="", flush=True)
        print()


if __name__ == "__main__":
    asyncio.run(main())
```

[`LocalOpenAIAgentConfig`](https://github.com/google-antigravity/antigravity-sdk-python/blob/main/google/antigravity/connections/local/local_openai_connection_config.py) supports all standard [`AgentConfig`](https://github.com/google-antigravity/antigravity-sdk-python/blob/main/google/antigravity/connections/README.md#agentconfig) options along with these connection parameters:

*   `model` (string or `ModelTarget`, optional): Model identifier registered on your local server (such as `"gemma4:26b"` or `"gemma-4-26B-A4B-it"`).
*   `base_url` (string, optional): URL of the local server’s OpenAI-compatible endpoint (such as `"http://localhost:11434/v1"` for Ollama or `"http://localhost:1234/v1"` for LM Studio).

## Sample code

To explore full working code examples, check out the following resources:

*   [`local_models.py`](https://github.com/google-antigravity/antigravity-sdk-python/blob/main/examples/getting_started/local_models.py): Getting-started script for `LiteRTAgentConfig` and `LocalOpenAIAgentConfig`.
*   [`multimodal.py`](https://github.com/google-antigravity/antigravity-sdk-python/blob/main/examples/getting_started/multimodal.py): Attaching images, documents, and audio with `Image.from_file()`, `Document.from_file()`, and `Audio.from_file()`.
*   [Antigravity Hybrid Gauntlet](https://goo.gle/47cKYyV): Hybrid workflow that pairs a cloud Gemini planner with local Gemma 4 26B agents for on-device code auditing and patching.