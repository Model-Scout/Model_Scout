---
license: other
license_name: lfm1.0
license_link: https://www.liquid.ai/lfm-license
library_name: mlx
pipeline_tag: text-generation
base_model: LiquidAI/LFM2.5-1.2B-Thinking
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
tags:
- mlx
- optiq
- quantized
- 4bit
- mixed-precision
- lfm2
- liquid-ai
- apple-silicon
- on-device
- reasoning
---

# mlx-community/LFM2.5-1.2B-Thinking-OptiQ-4bit

> **Built with [mlx-optiq](https://mlx-optiq.com)**, the MLX-native toolkit to quantize, fine-tune, and serve LLMs locally on Apple Silicon, no PyTorch and no cloud. [All OptiQ quants](https://mlx-optiq.com/models) · [Docs](https://mlx-optiq.com/docs/)

An OptiQ mixed-precision quant of [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking). 820 MB on disk, down from 2.34 GB at bf16, and it scores 84% on IFEval and 83% on GSM8K at that size.

This is the reasoning variant of LFM2.5-1.2B. It thinks before answering, which is worth a lot at this size: against the Instruct model it gains 21 points on MMLU and 13 on GSM8K.

LFM2.5 is a hybrid architecture: convolutional blocks interleaved with full attention, so only a few blocks carry a KV cache. OptiQ measures each layer's sensitivity and assigns per-layer bit-widths, keeping 8-bit where it matters and 4-bit elsewhere.

## What it is

| Property | Value |
|---|---|
| Base | [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) |
| Architecture | `lfm2` — hybrid conv + full attention |
| Method | OptiQ mixed-precision, sensitivity-driven (bf16 reference) |
| On disk | 820 MB (bf16: 2.34 GB) |
| Context | 128k |
| KV cache | mixed-precision `kv_config.json` bundled (6 attention layers, 4.67 avg bits) |

## Capability Score

Six-metric mean, the standard OptiQ eval. Run with reasoning enabled.

| Metric | Score |
|---|---:|
| MMLU (5-shot, 969 samples) | 64.7% |
| GSM8K (1000 samples) | 82.8% |
| IFEval (full set, strict) | 84.3% |
| BFCL-V3 simple (200 calls) | 83.5% |
| HumanEval (164 problems, pass@1) | 47.6% |
| HashHop (long-context retrieval) | 0.0% |
| **Capability Score** (mean of 6) | **60.47** |

Knowledge and instruction-following are the strengths, and 83% on GSM8K is unusual for a model under a gigabyte. Long-context multi-hop retrieval is the weak spot: at this size the model cannot produce the hash format the task requires, so it scores zero rather than partially.

## Run it

```bash
pip install mlx-optiq
```

```python
from mlx_lm import load, generate

model, tok = load("mlx-community/LFM2.5-1.2B-Thinking-OptiQ-4bit")
prompt = tok.apply_chat_template(
    [{"role": "user", "content": "What is 17 * 23? Think briefly then answer."}],
    tokenize=False, add_generation_prompt=True,
)
print(generate(model, tok, prompt=prompt, max_tokens=2048))
```

**Give it room.** The model spends its first few hundred tokens thinking, and that budget comes out of `max_tokens`. Cap it too low and the whole allowance is consumed inside the reasoning block, so you get an empty answer back rather than a short one. 2048 is a sensible floor for anything non-trivial.

Serve it with the bundled mixed-precision KV cache:

```bash
optiq serve --model mlx-community/LFM2.5-1.2B-Thinking-OptiQ-4bit --kv-config kv_config.json
```

## Tool calling

LFM2.5 writes Pythonic calls between special tokens:

```
<|tool_call_start|>[get_weather(city="Paris")]<|tool_call_end|>
```

Pass `tools=` to `apply_chat_template` and they are rendered into the system prompt.

## Links

- **Project website:** [mlx-optiq.com](https://mlx-optiq.com/)
- **All OptiQ quants:** [mlx-optiq.com/models](https://mlx-optiq.com/models)
- **Base model:** [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)
