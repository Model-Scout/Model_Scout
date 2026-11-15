---
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
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
  - mlx
  - mlx-vlm
  - safetensors
  - lfm3
  - lfm
  - liquid
  - liquid-ai
  - lfm3-1.7b
  - tri-hybrid
  - hybrid-architecture
  - short-convolution
  - edge
  - conversational
  - text-generation
  - quantized
  - quantization
  - 8-bit
  - oq
  - oqe
  - oq8e
  - omlx
  - apple-silicon
  - macos
  - mac
  - metal
  - local-llm
  - local-inference
  - on-device
  - edge-ai
  - agent
  - agentic
  - tool-calling
  - function-calling
  - structured-output
  - reasoning
  - thinking
  - long-context
  - 256k-context
  - multilingual
  - hermes-agent
  - openclaw
  - uraion-labs
  - uraionlabs
---

<p align="center">
  <a href="https://uraionlabs.com"><img src="https://uraionlabs.com/public/icons/icon-192.png" alt="Uraion Labs" width="56"></a>
</p>

<p align="center">
  <strong>Uraion Labs</strong><br>
  <sub>Foundational systems research.</sub>
</p>

# LFM3-1.7B — oQ8e (MLX)

> Liquid AI's LFM3-1.7B, quantized for Apple Silicon with oMLX oQe mixed precision. Maximum fidelity. Closest to the BF16 original.

<p align="center">
  <a href="https://huggingface.co/LiquidAI/LFM3-1.7B"><img src="https://img.shields.io/badge/Base%20Model-LFM3--1.7B-blue?style=for-the-badge&logo=huggingface" alt="Base model"></a>
  <a href="https://github.com/Blaizzy/mlx-vlm"><img src="https://img.shields.io/badge/Runtime-MLX%20%2F%20Apple%20Silicon-orange?style=for-the-badge&logo=apple" alt="MLX"></a>
  <a href="https://huggingface.co/UraionLabs/LFM3-1.7B-MLX-oQ8e"><img src="https://img.shields.io/badge/Precision-oQ8e%20(8--bit)-success?style=for-the-badge" alt="oQ8e"></a>
  <a href="https://huggingface.co/LiquidAI/LFM3-1.7B"><img src="https://img.shields.io/badge/Context-256K-purple?style=for-the-badge" alt="256K context"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-LFM%20Open%20v1.0-green?style=for-the-badge" alt="LFM Open License v1.0"></a>
</p>

**LFM3-1.7B-MLX-oQ8e** is an MLX quantization of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), Liquid AI's tri-hybrid text model for local agents, tool calling and structured outputs. It was quantized and published by [Uraion Labs](https://uraionlabs.com) with the oMLX oQ8e preset and runs natively on Apple Silicon Macs (M1 through M5) with [oMLX](https://github.com/jundot/omlx) and [mlx-vlm](https://github.com/Blaizzy/mlx-vlm) `>= 0.7.11`.

- **Size:** 1.84 GB of weights (~8.5 effective bits per weight, including group scales)
- **Speed:** ~130 tokens/s decode on an M5 Pro (measured by Uraion Labs, see below)
- **Context:** 256K tokens, native reasoning (`<think>`), XML tool calls, deferred tool search
- **Languages:** 16, including English, Chinese, Arabic, Japanese, Korean, Hindi and the major European languages

> **Runtime note:** LFM3 support in `mlx-lm` is still in progress upstream. Use **oMLX** or **mlx-vlm 0.7.11+** (which loads LFM3 as a text-only model) today.

## Pick your quant

| Quant | Base bits | Mixed-precision profile | Output head | Size | Decode speed* | Best for | Repository |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **oQ8e** (this repo) | 8-bit | Uniform 8-bit | 8-bit | 1.84 GB | ~130 tok/s | Maximum quality | [UraionLabs/LFM3-1.7B-MLX-oQ8e](https://huggingface.co/UraionLabs/LFM3-1.7B-MLX-oQ8e) |
| oQ6e | 6-bit | Mixed 6/8-bit (33 layers @ 8-bit) | 6-bit | 1.45 GB | ~152 tok/s | Recommended: near-8-bit quality | [UraionLabs/LFM3-1.7B-MLX-oQ6e](https://huggingface.co/UraionLabs/LFM3-1.7B-MLX-oQ6e) |
| oQ5e | 5-bit | Mixed 5/6/8-bit (29 @ 6b, 8 @ 8b) | 6-bit | 1.23 GB | ~174 tok/s | Faster, still strong quality | [UraionLabs/LFM3-1.7B-MLX-oQ5e](https://huggingface.co/UraionLabs/LFM3-1.7B-MLX-oQ5e) |
| oQ4e | 4-bit | Mixed 4/5/6/8-bit (37 @ 5b, 2 @ 6b, 4 @ 8b) | 5-bit | 1.04 GB | ~203 tok/s | Smallest and fastest (~1 GB) | [UraionLabs/LFM3-1.7B-MLX-oQ4e](https://huggingface.co/UraionLabs/LFM3-1.7B-MLX-oQ4e) |

<sub>*Single-stream decode speed measured by Uraion Labs on an Apple M5 Pro (64 GB), macOS 27, oMLX 0.7.3, 800 generated tokens, average of 2 runs. Your numbers will vary with chip, context length and settings.</sub>

All four variants answered a short math check correctly and produced a valid OpenAI-style `get_weather` tool call through the oMLX server (oQ4e and oQ8e tool-call tested). This is a smoke test, not a full benchmark run.

## About this quantization

| Property | Value |
| :--- | :--- |
| Original model | [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) (Liquid AI) |
| Quantized by | [Uraion Labs](https://uraionlabs.com) |
| Quantization preset | `oQ8e` (oMLX oQ, enhanced mixed precision) |
| Base weight precision | 8-bit |
| Mixed-precision profile | Uniform 8-bit |
| Layer overrides | None (all projections at 8-bit) |
| Embeddings / output head (tied) | 8-bit |
| Group size / mode | 64 / affine (per-group scale and bias) |
| Bit allocation | Chosen per layer by oMLX oQ sensitivity analysis |
| Weight file | 1.84 GB (1,837,281,931 bytes), single `model.safetensors` |
| Effective bits per weight | ~8.50 |
| Format | MLX safetensors |
| Tested runtimes | oMLX 0.7.3, mlx-vlm 0.7.11 |

## Model information

| Property | Value |
| :--- | :--- |
| Architecture | `Lfm3ForCausalLM` (`lfm3`), tri-hybrid |
| Parameters | 1.73B |
| Layers | 24: 13 gated short convolutions, 5 sliding-window attention (window 256), 6 global attention |
| Attention | GQA, 16 query heads / 4 KV heads, head dim 128 |
| Context length | 262,144 tokens (input + output) |
| Vocabulary | 128,000 tokens |
| Languages | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish |
| License | [LFM Open License v1.0](LICENSE) |

## Quickstart

### oMLX (recommended)

[oMLX](https://github.com/jundot/omlx) is an OpenAI-compatible server for Apple Silicon with continuous batching and SSD-backed KV cache. Download the model into your oMLX models folder (or use the model downloader in the oMLX app), then serve it:

```bash
hf download UraionLabs/LFM3-1.7B-MLX-oQ8e --local-dir ~/.omlx/models/LFM3-1.7B-MLX-oQ8e
omlx serve --model-dir ~/.omlx/models --port 8000
```

Call it from any OpenAI client, tools included:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="your-omlx-key")

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

response = client.chat.completions.create(
    model="LFM3-1.7B-MLX-oQ8e",
    messages=[{"role": "user", "content": "What's the weather in Paris right now?"}],
    tools=tools,
    temperature=0.1,
    extra_body={"top_k": 50, "repetition_penalty": 1.1},
)
print(response.choices[0].message.tool_calls)
```

### mlx-vlm (CLI)

```bash
pip install -U "mlx-vlm>=0.7.11"

python -m mlx_vlm.generate \
  --model UraionLabs/LFM3-1.7B-MLX-oQ8e \
  --prompt "Explain how a heat pump works." \
  --max-tokens 1024 \
  --temperature 0.1 \
  --top-k 50 \
  --repetition-penalty 1.1
```

### mlx-vlm (Python)

```python
from mlx_vlm import load, generate

model, processor = load("UraionLabs/LFM3-1.7B-MLX-oQ8e")

messages = [{"role": "user", "content": "Explain how a heat pump works."}]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

result = generate(model, processor, prompt, max_tokens=1024, temperature=0.1, verbose=True)
print(result.text)
```

### Agent harnesses

LFM3 was post-trained inside agent harnesses such as Hermes Agent, Pi and OpenClaw. Point any OpenAI-compatible harness at the oMLX endpoint above. See Liquid AI's [Agent Harnesses guide](https://docs.liquid.ai/examples/agent-harnesses).

## Recommended sampling

From Liquid AI's official model card:

| Use case | Settings |
| :--- | :--- |
| General (chat, tool use, agents, coding) | `temperature=0.1`, `top_k=50`, `repetition_penalty=1.1` |
| Math and STEM | `temperature=1.0`, `top_p=0.95`, `top_k=20` |

The bundled `generation_config.json` already uses the general settings.

## Chat format, reasoning and tools

- **ChatML template** (`<|im_start|>` / `<|im_end|>`). Use `apply_chat_template(..., add_generation_prompt=True)`.
- **Reasoning is on by default.** Pass `enable_thinking=False` to the template to turn it off (upstream notes this can be inconsistent on reasoning-heavy tasks). Earlier-turn reasoning is dropped unless `preserve_thinking=True`.
- **Tool calls** are emitted as XML (`<tool_call><function=name><parameter=...>`). oMLX converts them to OpenAI `tool_calls` automatically.
- **Deferred tool search:** mark tools with `defer_loading=True` and return `tool_reference` parts from your search tool. Details in [Liquid AI's tool-use docs](https://docs.liquid.ai/lfm/key-concepts/tool-use).

## Upstream benchmarks

> Reported by Liquid AI for the original BF16 LFM3-1.7B (vLLM, full context). Uraion Labs has not re-run these on the quantized weights. Lower-bit quants may score somewhat lower.

| Benchmark | LFM3-1.7B | LFM2.5-2.6B | MiniCPM5-2B | Gemma 4 E4B | Qwen3.5-4B | Qwen3.5-9B |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| LiveClaw | **45.60** | 14.70 | 30.37 | 20.36 | 19.94 | 35.77 |
| Claw-Eval General (EN), average | **68.64** | 62.63 | 60.74 | 56.14 | 61.96 | 66.53 |
| BFCL V4 | **71.39** | 55.89 | 62.65 | 48.25 | 55.12 | 62.83 |
| ToolSandbox | **80.36** | 78.04 | 68.16 | 69.27 | 75.40 | 76.41 |
| τ³-bench (4 domains), average | 68.01 | 56.77 | **69.44** | 33.53 | 65.98 | 67.11 |
| MCP-Atlas | 32.57 | 16.45 | 26.38 | 6.19 | 41.37 | **42.67** |
| SWE-bench Verified (OpenCode) | 43.40 | 18.00 | 34.80 | 0.50 | 41.20 | **51.20** |
| LiveCodeBench v6 | **73.46** | 60.57 | 70.52 | 71.00 | 61.99 | 69.86 |
| IFEval | **96.66** | 95.39 | 87.83 | 90.02 | 92.52 | 92.08 |
| IFBench | **73.03** | 60.48 | 62.08 | 44.56 | 38.16 | 48.84 |
| IFStruct | **93.72** | 82.18 | 72.65 | 78.45 | 87.05 | 89.20 |
| GPQA Diamond | 63.37 | 57.78 | 65.15 | 57.88 | 75.76 | **80.40** |
| AA-Omniscience non-hallucination (public) | **92.93** | 53.69 | 84.44 | 72.09 | 13.64 | 52.59 |
| AA-LCR | 52.83 | 6.00 | 49.34 | 39.33 | 52.67 | **62.00** |
| RULER 128K | 65.56 | 1.15 | 37.96 | 18.82 | 84.63 | **87.11** |
| **Average** | **49.37** | 31.55 | 39.19 | 31.74 | 39.27 | 47.24 |

Full table, settings and per-benchmark details: [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B#benchmarks).

## Limitations

- Liquid AI positions LFM3-1.7B for local agents, tool calling, structured outputs and fine-tuning. It is **not recommended for agentic coding or complex multi-step reasoning** because of its size. Pair it with retrieval or search for knowledge-heavy tasks.
- Quantization reduces precision. The 4-bit and 5-bit variants trade some accuracy for size and speed; use oQ6e or oQ8e when quality matters most.
- Like any language model, it can produce inaccurate or biased output. Do not treat answers on legal, medical or financial topics as professional advice. Provided "AS IS", without warranty.

## Attribution and modifications

LFM3-1.7B was created by [Liquid AI](https://www.liquid.ai). The architecture, training, benchmarks and capabilities described here come from the upstream release. All credit for the model belongs to Liquid AI.

**Changes made by Uraion Labs:** the weights in `model.safetensors` were quantized to MLX format, and `config.json` was updated with quantization metadata. The tokenizer, chat template, generation config and custom code files are unchanged from upstream. No retraining or fine-tuning was performed.

Upstream resources: [model card](https://huggingface.co/LiquidAI/LFM3-1.7B) · [LFM3 blog post](https://www.liquid.ai/blog/lfm3) · [docs](https://docs.liquid.ai/lfm/getting-started/welcome) · [LFM3 collection](https://huggingface.co/collections/LiquidAI/lfm3) · [Discord](https://discord.com/invite/liquid-ai)

## License

Distributed under the **LFM Open License v1.0** (copy included in [`LICENSE`](LICENSE)), the same license as the original model. In short: free for research and non-commercial use, and for commercial use by organizations under US$10M in annual revenue. Commercial use above that threshold is not covered; contact [Liquid AI](https://www.liquid.ai/connect). Read the full license before use.

## Citation

```bibtex
@article{liquidAI2026LFM3,
  author  = {Liquid AI},
  title   = {Introducing LFM3: Every Modality for Specialized Intelligence},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm3},
}
```

<p align="center">
  <sub>Quantized and published by <a href="https://uraionlabs.com">Uraion Labs</a>. Foundational systems research.</sub>
</p>
