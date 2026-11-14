---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
pipeline_tag: text-generation
inference: false
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
tags:
- gguf
- velociq8
- q8a64
- cpu
- 8-bit
- quantized
- arm64
- aarch64
- x86_64
- liquid
- lfm3
- text-generation
- conversational
- tool-calling
- reasoning
---

<!-- velociq8:common:header -->
<p align="center">
  <a href="https://huggingface.co/VelociQ8"><img src="https://huggingface.co/spaces/VelociQ8/README/resolve/main/logo.png" alt="VelociQ8" width="96"></a>
</p>

<p align="center">
  <b>Q8A64 model file for VelociQ8</b><br>
  Fast CPU inference for GGUF models on Arm and x86<br>
  Embeddings, dense and MoE LLMs<br>
  <a href="https://github.com/dhaern/VelociQ8">Runtime</a> ·
  <a href="https://github.com/dhaern/VelociQ8/releases">Releases</a> ·
  <a href="https://github.com/dhaern/VelociQ8/blob/main/docs/usage.md">Usage</a> ·
  <a href="https://huggingface.co/VelociQ8">All models</a>
</p>
<!-- /velociq8:common:header -->

# LFM3-1.7B · Q8A64

This repository holds [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) converted to Q8A64, the 8-bit weight format of VelociQ8, to run on the CPU. Liquid AI designed it for local agents, tool calling, structured outputs and fine-tuning on your own domain. It reasons before it answers.

<table>
<tbody>
<tr><th align="left" scope="row">Base model</th><td><a href="https://huggingface.co/LiquidAI/LFM3-1.7B">LiquidAI/LFM3-1.7B</a>, by Liquid AI</td></tr>
<tr><th align="left" scope="row">Type</th><td>Chat model with reasoning and tool calling, text in and text out</td></tr>
<tr><th align="left" scope="row">Size</th><td>1.73B parameters</td></tr>
<tr><th align="left" scope="row">Context</th><td>256K tokens in the original model</td></tr>
<tr><th align="left" scope="row">Weights license</th><td><a href="https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE">LFM Open License v1.0</a>, commercial use only below 10 million US dollars of annual revenue</td></tr>
<tr><th align="left" scope="row">Measurements</th><td>Speed and quality measured, see <a href="#speed-and-quality">Speed and quality</a></td></tr>
</tbody>
</table>

**Commercial use is limited by revenue.** The original model is released under the LFM Open License v1.0, which licenses commercial use only below 10 million US dollars of annual revenue (section 5), and this converted file has the same limit. The VelociQ8 runtime is free for commercial use, but that does not change the license of these weights.

The original repository has an official BF16 GGUF file. This file is that BF16 GGUF converted to Q8A64.

**LFM3-1.7B needs VelociQ8 1.5 or later.** That is the first version that runs this model; the version in the next paragraph is the general minimum for Q8A64 files.

<!-- velociq8:common:runtime -->
**This file loads only in VelociQ8 1.1 or later.** Other GGUF tools, including standard llama.cpp, cannot load Q8A64 files. The automatic snippets that Hugging Face shows under **Use this model** (for llama.cpp, Ollama and similar tools) do not work with these files.

## Get the runtime

VelociQ8 is free-to-use proprietary software built on llama.cpp. It ships the usual tools (`llama-server`, `llama-cli`, `llama-embedding`, `llama-bench` and `llama-quantize`) with the same options and the same HTTP API, including the OpenAI-compatible endpoints. Download the archive for your machine from the table (GitHub release) or from the [`runtime`](https://huggingface.co/VelociQ8/LFM3-1.7B-Q8A64-GGUF/tree/main/runtime) folder of this repository, which has the same files. Check it against `SHA256SUMS` from the same place.

| Archive | For |
|---|---|
| [`velociq8-1.5-linux-arm64.tar.gz`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-linux-arm64.tar.gz) | Arm servers with dotprod: Ampere Altra, AWS Graviton2 and later, Neoverse N1 and later |
| [`velociq8-1.5-linux-arm64-multi.tar.gz`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-linux-arm64-multi.tar.gz) | Any 64-bit Arm CPU; it picks the best kernels at startup |
| [`velociq8-1.5-linux-x64.tar.gz`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-linux-x64.tar.gz) | x86-64 with AVX2 and FMA (Intel Haswell, AMD Zen and later) |
| [`velociq8-1.5-windows-x64.zip`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-windows-x64.zip) | Windows on the same x86-64 CPUs (tested on Windows 11) |
| [`velociq8-1.5-ollama-0.40.13-linux-arm64.tar.gz`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-ollama-0.40.13-linux-arm64.tar.gz) | Portable Ollama 0.40.13 for the CPU, Linux on Arm |
| [`velociq8-1.5-ollama-0.40.13-linux-x64.tar.gz`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-ollama-0.40.13-linux-x64.tar.gz) | Portable Ollama 0.40.13, Linux on x86-64: CPU, or the GPU through Vulkan |
| [`velociq8-1.5-ollama-0.40.13-windows-x64.zip`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-ollama-0.40.13-windows-x64.zip) | Portable Ollama 0.40.13, Windows on x86-64: CPU, or the GPU through Vulkan |

The Ollama archives are a portable Ollama with VelociQ8 inside, and do not touch an installed Ollama. The x86-64 ones also use an NVIDIA, AMD or Intel GPU through Vulkan when its driver is installed; see [Ollama](https://github.com/dhaern/VelociQ8/blob/main/docs/usage.md#ollama). The Linux archives need glibc 2.28 or newer. There is also a Docker image for Linux on Arm and x86-64, [`ghcr.io/dhaern/velociq8`](https://github.com/dhaern/VelociQ8/pkgs/container/velociq8) (see [Docker](https://github.com/dhaern/VelociQ8/blob/main/docs/usage.md#docker)). The other archives and the Docker image run on the CPU. VelociQ8 tools cannot download models: download the file from this repository first and pass it with `-m`.

### NVIDIA GPUs (CUDA)

For NVIDIA GPUs there are also portable Ollama archives with CUDA. They are larger (about 1 GB), so they are only on GitHub: [`velociq8-1.5-ollama-0.40.13-windows-x64-cuda.zip`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-ollama-0.40.13-windows-x64-cuda.zip) and [`velociq8-1.5-ollama-0.40.13-linux-x64-cuda.tar.gz`](https://github.com/dhaern/VelociQ8/releases/download/v1.5/velociq8-1.5-ollama-0.40.13-linux-x64-cuda.tar.gz). They need an NVIDIA GPU of the Turing generation or newer (GeForce RTX 20 series onwards) with a current driver.

Questions about this file go to the [Community](https://huggingface.co/VelociQ8/LFM3-1.7B-Q8A64-GGUF/discussions) tab; problems with the runtime, to [GitHub issues](https://github.com/dhaern/VelociQ8/issues).
<!-- /velociq8:common:runtime -->

## Files

| File | Contents | Size |
|---|---|---|
| [`LFM3-1.7B-Q8A64.gguf`](https://huggingface.co/VelociQ8/LFM3-1.7B-Q8A64-GGUF/resolve/main/LFM3-1.7B-Q8A64.gguf) | Q8A64 weights | 1709.20 MiB |
| [`LICENSE`](https://huggingface.co/VelociQ8/LFM3-1.7B-Q8A64-GGUF/blob/main/LICENSE) | License text | |

SHA256 of the weights file, in the format `sha256sum -c` reads:

```text
b2086cc39f7753cadbd0a6d9161d1da9a6ff01c5f827b2cadca2526df749da0d  LFM3-1.7B-Q8A64.gguf
```

## Quick start

Unpack the archive that matches your CPU (Linux Arm64 shown) and download the file:

```sh
tar xf velociq8-1.5-linux-arm64.tar.gz && cd velociq8-1.5-linux-arm64
REPO=VelociQ8/LFM3-1.7B-Q8A64-GGUF
FILE=LFM3-1.7B-Q8A64.gguf
curl -L -O https://huggingface.co/$REPO/resolve/main/$FILE
```

You can also download it from the **Files** tab or with `hf download VelociQ8/LFM3-1.7B-Q8A64-GGUF LFM3-1.7B-Q8A64.gguf --local-dir .`. On Windows use `llama-server.exe` from the zip; the options are the same.

Start a server and talk to it through the OpenAI-compatible chat endpoint. Use `-t` for the number of physical cores you want to give the model and `-c` for the context you need (8192 tokens here). Without `-c`, `llama-server` sets up the full context of the model (see the *Context* row of the table above), which needs more memory than most uses do. The sampling flags are the settings that Liquid AI recommends:

```sh
./llama-server -m LFM3-1.7B-Q8A64.gguf -t 4 -c 8192 --temp 0.1 --top-k 50 --repeat-penalty 1.1 --port 8080
```

Ask a question:

```sh
curl -s http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"messages": [{"role": "user", "content": "What is C. elegans?"}]}'
```

LFM3-1.7B reasons before it answers. `llama-server` returns the reasoning in `reasoning_content`, apart from the answer in `content`. The reasoning counts against `max_tokens`: a small limit can stop the reply before `content` starts. The message looks like this (shortened):

```json
{"role": "assistant", "reasoning_content": "(the reasoning)", "content": "(the answer)"}
```

### Ollama

The portable Ollama 0.40.13 archives from the table above run this file too (Linux shown; the [usage guide](https://github.com/dhaern/VelociQ8/blob/main/docs/usage.md#ollama) covers Windows, the GPU and what to do if another Ollama is already running). Start the server from the unpacked folder with `./bin/ollama serve` and, in a second terminal, import the file with a Modelfile:

```sh
cat > Modelfile <<'EOF'
FROM ./LFM3-1.7B-Q8A64.gguf
RENDERER lfm3
PARSER lfm3
EOF
./bin/ollama create lfm3-1.7b-q8a64 -f Modelfile
./bin/ollama run lfm3-1.7b-q8a64 "What is C. elegans?"
```

Ollama cannot see the architecture or the chat template in a Q8A64 file, so the Modelfile names them with `RENDERER` and `PARSER`. Without those two lines chat works, but Ollama does not detect tools or reasoning and rejects requests with `tools`. With them, `ollama show lfm3-1.7b-q8a64` lists `tools` and `thinking`, tool calls work, and `"think": false` in a request turns the reasoning off. A request with one tool:

```sh
curl -s http://127.0.0.1:11434/api/chat -d '{
  "model": "lfm3-1.7b-q8a64", "stream": false,
  "messages": [{"role": "user", "content": "What is the weather in Paris?"}],
  "tools": [{"type": "function", "function": {
    "name": "get_weather", "description": "Get the weather of a city",
    "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]}'
```

The reply holds a `tool_calls` entry with the function name and its arguments. Run the function yourself and send the result back as a `tool` message.

## Prompt

Send ordinary `messages`: the server applies the chat template of the model, so you do not write the prompt format yourself. Reasoning is on by default. The sampling flags of the server command are the ones Liquid AI recommends; the other settings it gives, the chat template and the tool-call format are listed under *About the base model*.

## Speed and quality

### Speed

Tokens per second, higher is better. VelociQ8 1.5 against llama.cpp b11963 on the Arm machine (Oracle Cloud A1, 4 threads), `llama-bench` with 3 repetitions per run and flash attention on, two interleaved rounds; median of the six repetitions. VelociQ8 loaded this Q8A64 file and llama.cpp Liquid AI's official Q8_0 GGUF.

| Test | VelociQ8 | llama.cpp, Q8_0 |
|---|---|---|
| Prompt processing, 512 tokens | 168.9 | 103.2 |
| Text generation, 128 tokens | 17.8 | 18.6 |

Prompt processing is 1.64 times faster. Text generation is 4 % slower than llama.cpp with Q8_0. Two of VelociQ8's text-generation repetitions were disturbed (9.8 and 4.5 tok/s); without them its median is 18.2 tok/s.

### Quality against full precision

KL divergence against the original model, lower is better. "Same top token" is how often the most likely next token matches the original model's. The reference is the original BF16 model converted to F32, which loses nothing, run by llama.cpp b11963. `llama-perplexity --kl-divergence` on wikitext-2, 8 chunks of 512 tokens, 4 threads, on the Arm machine. VelociQ8 1.5 ran this file; llama.cpp b11963 ran Liquid AI's official Q8_0 GGUF.

| Build | KL divergence | Same top token |
|---|---|---|
| VelociQ8 | 0.001487 | 98.14 % |
| llama.cpp, Q8_0 | 0.001703 | 98.09 % |

VelociQ8 has 13 % less divergence than Q8_0. The standard errors are 0.000074 and 0.000080; the same-top-token rates differ by 0.05 points, under their standard error of 0.30 points.

Full tables, other builds and the method: [benchmarks.md](https://github.com/dhaern/VelociQ8/blob/main/docs/benchmarks.md) and [quality.md](https://github.com/dhaern/VelociQ8/blob/main/docs/quality.md).

## About the base model

**Source:** the original card of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), by Liquid AI ([release blog post](https://www.liquid.ai/blog/lfm3)). What follows is copied or condensed from it and is Liquid AI's statement, not VelociQ8's; it leaves out Liquid AI's speed, memory and benchmark claims. Read on 2026-10-29. If anything here differs from the original, the original is right. Benchmark tables and charts are not copied: they are in the *Performance* section of the original card.

### Description

LFM3-1.7B is a text model for local agents and specialized applications, based on Liquid AI's tri-hybrid architecture. It is post-trained for agentic harnesses such as Hermes Agent, Pi and OpenClaw, and it is made to be adapted to your own domains, formats and tools by fine-tuning on a single GPU. The LFM3 family also has base, vision, audio, omni and decision models; this repository holds only the text model.

### Architecture and size

| | LFM3-1.7B |
|---|---|
| Checkpoint | Post-trained, text-only language model |
| Parameters | 1.73B |
| Architecture | 24 layers: 13 gated short convolutions, 5 sliding-window attention, 6 global attention |
| Context length | 256K tokens (input + output) |
| Vocabulary | 128,000 tokens |

The base model is [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base), pre-trained on 22T tokens. Post-training has four stages: supervised fine-tuning, mixed reinforcement learning, multi-domain on-policy distillation and agentic reinforcement learning.

### Languages

English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian and Polish.

### Intended use

Local agents, tool calling, structured outputs and domain-specific fine-tuning.

### Limitations and risks

The original card says that, because of its small size, the model is not recommended for agentic coding or complex multi-step reasoning, and that retrieval or search should be used for knowledge-heavy tasks. It has no other section on limitations or risks.

### Prompt format

The model uses the ChatML format, generated by the chat template of the checkpoint:

```text
<|startoftext|><|im_start|>system
You are a helpful assistant trained by Liquid AI.<|im_end|>
<|im_start|>user
Explain how a heat pump works.<|im_end|>
<|im_start|>assistant
<think>
```

Reasoning is on by default. The original card says that disabling it (`enable_thinking=False` in Transformers) can be inconsistent, especially for reasoning-heavy tasks, and that the reasoning of earlier turns is removed unless `preserve_thinking=True`.

Tools are passed as function schemas, and the template formats them. The model writes a call in XML:

```text
<tool_call>
<function=get_weather>
<parameter=city>
Paris
</parameter>
</function>
</tool_call>
```

Your application runs the call, adds it to the history as a `tool_calls` entry and appends the result as a `tool` message. The original card also describes deferred tools (`defer_loading`), where the definitions of tools enter the prompt only after a search tool names them; see its *Tool search* section.

Sampling settings recommended by Liquid AI:

| Use | Settings |
|---|---|
| General: chat, tool use, agents, coding | `temperature=0.1`, `top_k=50`, `repetition_penalty=1.1` |
| Math and STEM | `temperature=1.0`, `top_p=0.95`, `top_k=20` |

The server command above uses the general settings. For math and science, replace them with `--temp 1.0 --top-p 0.95 --top-k 20`.

### License

The original card gives the license as the [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE) (`license_name: lfm1.0`). Its text is in the `LICENSE` file of this repository, copied unchanged from the original repository.

**Commercial use is limited by revenue.** Section 5 of the license licenses commercial use only below 10 million US dollars of annual revenue, and section 1 defines a legal entity as the acting entity together with the entities that control it, are controlled by it or are under common control with it. Section 5(c) lifts the limit for a qualified non-profit organization that uses the model for non-commercial or research purposes. The same limit applies to this converted file.

### Citation

```bibtex
@article{liquidAI2026LFM3,
  author  = {Liquid AI},
  title   = {Introducing LFM3: Every Modality for Specialized Intelligence},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm3},
}
```

<!-- velociq8:common:license -->
## Licenses

Two licenses apply, and they do not mix:

- **Runtime: VelociQ8 Software License Agreement.** It covers the VelociQ8 software only, that is, the archives in the [releases](https://github.com/dhaern/VelociQ8/releases). The runtime is free to use for personal or commercial work.
- **Weights: the license of the original model.** The weights in this repository are a converted copy of the model described in *About the base model*. They stay under the original license, stated below. The VelociQ8 license agreement does not cover them and does not limit the rights that license gives you.

VelociQ8 is not affiliated with the developers of the original model, and this conversion is not endorsed by them.
<!-- /velociq8:common:license -->

### License of this model

This repository contains a converted copy of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B). The weights were converted to Q8A64 and stored in a GGUF file. The model was not retrained or fine-tuned.

License: [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE). The full text is in the `LICENSE` file of this repository, copied unchanged from the repository of the original model.

**Commercial use is limited by revenue.** Section 5 of the license licenses commercial use only below 10 million US dollars of annual revenue, and section 1 defines a legal entity as the acting entity together with the entities that control it, are controlled by it or are under common control with it. Section 5(c) lifts the limit for a qualified non-profit organization that uses the model for non-commercial or research purposes. Read the license for the exact terms. The same limit applies to this file.

**Redistribution.** Section 4 asks anyone who passes the model on to give the recipient a copy of the license and to mark modified files. This repository has the license in `LICENSE`, and its weights are a modified version of the original files, converted to Q8A64.

<!-- velociq8:common:footer -->
<sub>Arm is a registered trademark of Arm Limited (or its subsidiaries) in the US and/or elsewhere. Other product and hardware names belong to their respective owners and are used only to say what VelociQ8 is compared against or measured on.</sub>
<!-- /velociq8:common:footer -->
