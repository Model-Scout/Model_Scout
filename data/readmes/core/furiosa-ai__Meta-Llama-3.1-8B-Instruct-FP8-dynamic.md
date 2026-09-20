---
base_model: RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic
language:
  - en
  - de
  - fr
  - it
  - pt
  - hi
  - es
  - th
license: llama3.1
license_link: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE
pipeline_tag: text-generation
library_name: furiosa-llm
tags:
  - furiosa-ai
  - llama
  - llama-3
  - fp8
---
# Llama-3.1-8B-Instruct-FP8-dynamic

This repository contains
[RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic)
together with a Furiosa Executable Bundle (FXB) for running it on
[FuriosaAI RNGD](https://furiosa.ai) with
[Furiosa-LLM](https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html).
The same model also runs on other frameworks (such as vLLM, SGLang, and
Transformers); for usage with those, see the upstream
[RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic)
model card.

## Overview

Llama-3.1-8B-Instruct is Meta's 8B instruction-tuned model, an auto-regressive
dense transformer optimized for multilingual dialogue, instruction following,
and tool usage. This is the FP8-dynamic quantized variant published by RedHatAI,
derived from
[meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).
Its intended use is the same as the upstream
[RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic),
and it is released under the
[Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE).

- **Architecture:** Llama 3.1 (dense)
- **Input / Output:** Text / Text
- **Supported Inference Engine:** Furiosa LLM
- **Supported Hardware:** FuriosaAI RNGD

### Quantization

The linear (Transformer block) weights are quantized to FP8 (static), and
activations use dynamic FP8 quantization at runtime. Activations are quantized
per token at inference time rather than with offline calibration.

### Features

- **Tool calling.** The model supports tool (function) calling through the `llama3_json` tool-call parser, the parser used by the Llama 3 series.

### Parallelism Strategy

On RNGD, Llama-3.1-8B-Instruct-FP8-dynamic runs with a **tensor-parallel size of
8 PEs**, which maps to a **single RNGD card** (8 PEs per card).

## Usage

To run this model with Furiosa-LLM, follow the example commands below after
[installing Furiosa-LLM and its prerequisites](https://developer.furiosa.ai/latest/en/get_started/furiosa_llm.html#installing-furiosa-llm).

### Launch the server

The simplest way to serve the model is:

```sh
# Launch the server, listening on port 8000 by default
furiosa-llm serve furiosa-ai/Meta-Llama-3.1-8B-Instruct-FP8-dynamic
```

To also enable tool (function) calling, add the `llama3_json` tool-call parser
(the parser used by the Llama 3 series):

```sh
furiosa-llm serve furiosa-ai/Meta-Llama-3.1-8B-Instruct-FP8-dynamic \
  --enable-auto-tool-choice \
  --tool-call-parser llama3_json
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
    "model": "furiosa-ai/Meta-Llama-3.1-8B-Instruct-FP8-dynamic",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
    }' \
    | python -m json.tool
```

### Advanced Usage

**Tool calling.** With the server launched using
`--enable-auto-tool-choice --tool-call-parser llama3_json` (see
[Launch the server](#launch-the-server)), pass `tools` in the request and let the
model decide when to call them. See the
[Tool Calling guide](https://developer.furiosa.ai/latest/en/furiosa_llm/toolcalling.html)
for a complete client example and details on tool-choice options.

## Learn more

* [Tool Calling](https://developer.furiosa.ai/latest/en/furiosa_llm/toolcalling.html) — parsers, tool-choice options, and more examples
* [Furiosa-LLM Server (`furiosa-llm serve`)](https://developer.furiosa.ai/latest/en/furiosa_llm/furiosa-llm-serve.html) — full OpenAI-compatible API reference and serving options
* [RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic) — upstream model card
