---
base_model: upstage/Solar-Open-100B
language:
  - en
  - ko
license: other
license_name: upstage-solar-license
license_link: https://huggingface.co/upstage/Solar-Open-100B/blob/main/LICENSE
pipeline_tag: text-generation
library_name: furiosa-llm
tags:
  - furiosa-ai
  - upstage
  - solar
  - solar-open
  - solar_open
---
# Solar-Open-100B-NVFP4A16

This repository contains a build of
[upstage/Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B)
that FuriosaAI quantized in-house to **NVFP4A16**, together with a Furiosa
Executable Bundle (FXB) for running it on
[FuriosaAI RNGD](https://furiosa.ai) with [Furiosa-LLM](https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html).
The NVFP4A16 weights in this repository also run directly on other frameworks
(such as vLLM, SGLang, and Transformers); for the base model and general usage,
see the upstream
[upstage/Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B) model card.

## Overview

Solar-Open-100B is a large-scale open-weight language model developed by Upstage.
It is an auto-regressive **Mixture-of-Experts (MoE)** transformer that supports
English and Korean, and it handles both reasoning and non-reasoning chat as well
as tool (function) calling. Its intended use is the same as the upstream
[upstage/Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B), and it
is released under the [Upstage Solar License](https://huggingface.co/upstage/Solar-Open-100B/blob/main/LICENSE).

- **Architecture:** SolarOpen (Mixture-of-Experts)
- **Input / Output:** Text / Text
- **Supported Inference Engine:** Furiosa LLM
- **Supported Hardware:** FuriosaAI RNGD

### Quantization

The weights are quantized to **NVFP4** (4-bit floating point), while activations
and the KV cache remain in 16-bit precision (NVFP4A16).

### Features

- **Reasoning.** Solar-Open is a reasoning model. Launch the server with `--reasoning-parser solar_open` to have the chain of thought returned in a separate field. The reasoning depth is controllable per request through `reasoning_effort` (`"low"`, `"medium"`, `"high"`; default `"high"`).
- **Tool calling.** The model supports tool (function) calling through the `solar_open` tool-call parser.

### Parallelism Strategy

On RNGD, Solar-Open-100B-NVFP4A16 runs with a **tensor-parallel size of 32 PEs**,
which maps to **four RNGD cards** (8 PEs per card).

## Usage

To run this model with Furiosa-LLM, follow the example commands below after
[installing Furiosa-LLM and its prerequisites](https://developer.furiosa.ai/latest/en/get_started/furiosa_llm.html#installing-furiosa-llm).

### Launch the server

Serve the model with the `solar_open` reasoning parser so the chain of thought is
returned in a separate field:

```sh
furiosa-llm serve furiosa-ai/Solar-Open-100B-NVFP4A16 \
  --reasoning-parser solar_open
```

To also enable tool (function) calling, add the `solar_open` tool-call parser;
keep `--reasoning-parser solar_open` so thinking is still parsed into its own
field:

```sh
furiosa-llm serve furiosa-ai/Solar-Open-100B-NVFP4A16 \
  --reasoning-parser solar_open \
  --enable-auto-tool-choice \
  --tool-call-parser solar_open
```

When the server is ready, you will see:

```sh
INFO:     Started server process [27507]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Basic Usage

The server exposes an OpenAI-compatible API. You can send a request with `curl`:

```sh
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "furiosa-ai/Solar-Open-100B-NVFP4A16",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
    }' \
    | python -m json.tool
```

With `--reasoning-parser solar_open`, Solar-Open returns its reasoning separately
from the final answer:

* `response.choices[].message.reasoning` (non-streaming)
* `response.choices[].delta.reasoning` (streaming)

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="furiosa-ai/Solar-Open-100B-NVFP4A16",
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

**Controlling reasoning effort.** You can control how much the model reasons per
request with the `reasoning_effort` parameter (`"low"`, `"medium"`, or `"high"`;
default `"high"`). Solar-Open's chat template maps this to its thinking behavior:
`"high"` and `"medium"` produce a chain of thought — with `"high"` allowed a larger
reasoning-token budget than `"medium"` — while `"low"` (and `"minimal"`) prefill an
empty thinking block so the model skips reasoning and answers directly:

```python
response = client.chat.completions.create(
    model="furiosa-ai/Solar-Open-100B-NVFP4A16",
    messages=[{"role": "user", "content": "How many r's are in 'strawberry'?"}],
    extra_body={"reasoning_effort": "high"},
)

print("Reasoning:", response.choices[0].message.reasoning)
print("Answer:", response.choices[0].message.content)
```

**Tool calling.** With the server launched using
`--enable-auto-tool-choice --tool-call-parser solar_open` (see
[Launch the server](#launch-the-server)), pass `tools` in the request and let the
model decide when to call them. See the
[Tool Calling guide](https://developer.furiosa.ai/latest/en/furiosa_llm/toolcalling.html)
for a complete client example and details on tool-choice options.

## Learn more

* [Tool Calling](https://developer.furiosa.ai/latest/en/furiosa_llm/toolcalling.html) — parsers, tool-choice options, and more examples
* [Furiosa-LLM Server (`furiosa-llm serve`)](https://developer.furiosa.ai/latest/en/furiosa_llm/furiosa-llm-serve.html) — full OpenAI-compatible API reference and serving options
* [upstage/Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B) — upstream model card
