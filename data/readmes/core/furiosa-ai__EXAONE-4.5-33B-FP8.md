---
base_model: LGAI-EXAONE/EXAONE-4.5-33B-FP8
language:
  - en
  - ko
  - es
  - de
  - ja
  - vi
license: other
license_name: exaone
license_link: https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-FP8/blob/main/LICENSE
pipeline_tag: image-text-to-text
library_name: furiosa-llm
tags:
  - furiosa-ai
  - lg-ai
  - exaone
  - exaone-4.5
  - exaone4_5
---
# EXAONE-4.5-33B-FP8

This repository contains
[LGAI-EXAONE/EXAONE-4.5-33B-FP8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-FP8)
together with a Furiosa Executable Bundle (FXB) for running it on
[FuriosaAI RNGD](https://furiosa.ai) with [Furiosa-LLM](https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html).
The same model also runs on other frameworks (such as vLLM, SGLang, and
Transformers); for usage with those, see the upstream
[LGAI-EXAONE/EXAONE-4.5-33B-FP8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-FP8)
model card.

## Overview

EXAONE-4.5-33B-FP8 is LG AI Research's 33-billion-parameter **dense
vision-language model**. It integrates a dedicated vision encoder with the
EXAONE 4 language-model architecture to handle images and text. It supports
hybrid reasoning, which is enabled by default but can be disabled per request,
and native tool (function) calling. Its intended use is the same as the upstream
[LGAI-EXAONE/EXAONE-4.5-33B-FP8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-FP8),
and it is released under the
[EXAONE AI Model License](https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-FP8/blob/main/LICENSE).

- **Architecture:** EXAONE 4.5 (dense vision-language), `Exaone4_5_ForConditionalGeneration`
- **Input / Output:** Image + Text / Text
- **Supported Inference Engine:** Furiosa LLM
- **Supported Hardware:** FuriosaAI RNGD

### Quantization

The upstream FP8 build statically quantizes selected linear weights to
per-channel FP8 and dynamically quantizes their activations per token at
runtime; this does not use offline activation calibration. The upstream
configuration excludes the vision encoder, attention projections, LM head, and
MTP attention projections from FP8 quantization. The KV cache stays in 16-bit
precision.

### Features

- **Vision-language.** The model accepts OpenAI-style multimodal chat messages with `image_url` content parts alongside text.
- **Reasoning.** The model is hybrid and thinking is **enabled by default**. Furiosa-LLM parses its chain of thought through the `qwen3` reasoning parser; pass `enable_thinking: false` to use non-reasoning mode.
- **Tool calling.** The model supports tool (function) calling through the `hermes` tool-call parser.

### Parallelism Strategy

On RNGD, EXAONE-4.5-33B-FP8 runs with a **tensor-parallel size of 32 PEs**,
which maps to **four RNGD cards** (8 PEs per card).

## Usage

To run this model with Furiosa-LLM, follow the example commands below after
[installing Furiosa-LLM and its prerequisites](https://developer.furiosa.ai/latest/en/get_started/furiosa_llm.html#installing-furiosa-llm).

### Launch the server

EXAONE 4.5 reasons by default and can switch thinking on and off (see
[Advanced Usage](#advanced-usage)). Launch the server with the `qwen3` reasoning
parser so its chain of thought is separated from the final answer:

```sh
# Launch the server, listening on port 8000 by default
furiosa-llm serve furiosa-ai/EXAONE-4.5-33B-FP8 \
  --reasoning-parser qwen3
```

To also enable tool (function) calling, add the `hermes` tool-call parser; keep
`--reasoning-parser qwen3` so thinking is still parsed into its own field:

```sh
furiosa-llm serve furiosa-ai/EXAONE-4.5-33B-FP8 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes
```

When the server is ready, you will see:

```sh
INFO:     Started server process [27507]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Basic Usage

The server exposes an OpenAI-compatible API. You can send a text-only request
with `curl`:

```sh
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "furiosa-ai/EXAONE-4.5-33B-FP8",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
    }' \
    | python -m json.tool
```

To ask about an image, pass an `image_url` content part in the message:

```sh
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "furiosa-ai/EXAONE-4.5-33B-FP8",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "https://github.com/LG-AI-EXAONE/EXAONE-4.5/blob/main/assets/exaone45_input1.jpg?raw=true"}},
            {"type": "text", "text": "What dish is the person preparing?"}
        ]
    }]
    }' \
    | python -m json.tool
```

The `image_url.url` field accepts a remote `http://`/`https://` URL, an inline
base64 `data:` URL, or a local `file://` path (the last requires the
`--allowed-local-media-path` flag described under [Advanced Usage](#advanced-usage)).

With `--reasoning-parser qwen3`, EXAONE 4.5 returns its reasoning separately
from the final answer:

* `response.choices[].message.reasoning` (non-streaming)
* `response.choices[].delta.reasoning` (streaming)

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="furiosa-ai/EXAONE-4.5-33B-FP8",
    messages=[{"role": "user", "content": "How many r's are in 'strawberry'?"}],
)

print("Reasoning:", response.choices[0].message.reasoning)
print("Answer:", response.choices[0].message.content)
```

> **Note:** The `reasoning` field is not part of the OpenAI API specification but
> is a widely followed convention (the OpenAI Agents SDK, vLLM, and others). It
> appears only in responses that contain reasoning content; accessing it otherwise
> raises an `AttributeError`.

### Advanced Usage

**Multimodal serving options.** This example allows local images under
`/srv/media`, restricts remote image fetches to `cdn.example.com`, and limits
each request to four images:

```sh
furiosa-llm serve furiosa-ai/EXAONE-4.5-33B-FP8 \
  --reasoning-parser qwen3 \
  --allowed-local-media-path /srv/media \
  --allowed-media-domains cdn.example.com \
  --image-limit-per-prompt 4
```

See [Server Options](https://developer.furiosa.ai/latest/en/furiosa_llm/vision-language.html#server-options)
in the Vision-Language Models guide for the full option reference and defaults.

**Image processing options.** This example sets a 10-second HTTP image-fetch
timeout and uses `min_pixels` and `max_pixels` to bound image resizing:

```sh
furiosa-llm serve furiosa-ai/EXAONE-4.5-33B-FP8 \
  --reasoning-parser qwen3 \
  --media-io-kwargs '{"image": {"timeout": 10}}' \
  --mm-processor-kwargs '{"min_pixels": 4096, "max_pixels": 200704}'
```

For supported values, sizing behavior, and per-request overrides, see
[Multimodal Options](https://developer.furiosa.ai/latest/en/furiosa_llm/vision-language.html#multimodal-options)
in the Vision-Language Models guide.

**Turning thinking off.** EXAONE 4.5 reasons by default. To turn thinking off
for a single request, pass `enable_thinking` through `chat_template_kwargs`; the
response then carries no reasoning content, so read only `message.content`:

```python
# Disable thinking for a single request
response = client.chat.completions.create(
    model="furiosa-ai/EXAONE-4.5-33B-FP8",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
)
print(response.choices[0].message.content)
```

To default every request to non-thinking, launch the server with
`--default-chat-template-kwargs` (a request can still re-enable thinking with its
own `chat_template_kwargs`):

```sh
furiosa-llm serve furiosa-ai/EXAONE-4.5-33B-FP8 \
  --reasoning-parser qwen3 \
  --default-chat-template-kwargs '{"enable_thinking": false}'
```

**Tool calling.** With the server launched using
`--enable-auto-tool-choice --tool-call-parser hermes` (see
[Launch the server](#launch-the-server)), pass `tools` in the request and let the
model decide when to call them. See the
[Tool Calling guide](https://developer.furiosa.ai/latest/en/furiosa_llm/toolcalling.html)
for a complete client example and details on tool-choice options.

## Learn more

* [Vision-Language Models](https://developer.furiosa.ai/latest/en/furiosa_llm/vision-language.html) — image input formats and multimodal server options
* [Tool Calling](https://developer.furiosa.ai/latest/en/furiosa_llm/toolcalling.html) — parsers, tool-choice options, and more examples
* [Furiosa-LLM Server (`furiosa-llm serve`)](https://developer.furiosa.ai/latest/en/furiosa_llm/furiosa-llm-serve.html) — full OpenAI-compatible API reference and serving options
* [LGAI-EXAONE/EXAONE-4.5-33B-FP8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-FP8) — upstream model card
