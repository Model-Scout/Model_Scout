---
language:
  - en
  - fr
  - de
  - es
  - pt
  - it
  - ja
  - ko
  - ru
  - zh
  - ar
  - fa
  - id
  - ms
  - ne
  - pl
  - ro
  - sr
  - sv
  - tr
  - uk
  - vi
  - hi
  - bn
license: other
library_name: mlx-vlm
tags:
  - mlx
  - mlx-vlm
  - mistral3
  - conversational
  - vision
  - multimodal
  - reasoning
  - tool-use
base_model:
  - mistralai/Mistral-Medium-3.5-128B
pipeline_tag: image-text-to-text
quantization: 4-bit
---

<div align="center">

# Mistral Medium 3.5 128B

**MLX 4-bit &middot; Apple Silicon native**

Text &middot; Vision &middot; Thinking &middot; Tool Calling

[![LM Studio](https://img.shields.io/badge/LM_Studio-published-green)](https://lmstudio.ai/froggeric/mistral-medium-3.5-128b-mlx-4bit)
[![License](https://img.shields.io/badge/license-Modified_MIT-lightgrey)](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE)

</div>

> **Config fix applied (2026-05-02).** The original Mistral source had an incorrect `mscale_all_dim=1.0` in the YaRN RoPE config that disabled long-context scaling, degrading performance beyond 4096 tokens. Fixed to `mscale_all_dim=0.0` per [mistralai's commit](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/commit/c4be198050fb5789774a55b92ed697becfbf20ae). No weights were affected — this is a config-only fix.

---

## Why this model?

Mistral Medium 3.5 is Mistral AI's first flagship merged model — a dense 128B parameter model replacing Mistral Medium 3.1, Magistral, and Devstral 2. It handles instruction-following, reasoning, and coding in a single set of weights with a 256K context window.

**What makes this conversion different:**

1. **Vision included.** The Pixtral vision encoder is kept at full precision (not quantized), so image understanding is identical to the original FP8 model.

2. **Thinking mode.** Set `reasoning_effort="high"` for complex tasks — the model emits `[THINK]...[/THINK]` blocks with its reasoning chain before answering.

3. **Tool calling.** Native function calling with `[TOOL_CALLS]` tokens. Works with the included chat template.

---

## Quick start

### Text

```python
from mlx_lm import load, generate

model, tokenizer = load("froggeric/Mistral-Medium-3.5-128B-MLX-4bit")
response = generate(model, tokenizer, prompt="Hello", max_tokens=256, temp=0.7)
print(response)
```

### Vision

```python
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template

model, processor = load("froggeric/Mistral-Medium-3.5-128B-MLX-4bit")
image = ["path/to/image.jpg"]
prompt = "Describe this image."
formatted = apply_chat_template(processor, model.config, prompt, num_images=len(image))
result = generate(model, processor, formatted, image, max_tokens=256, temp=0.7)
print(result.text)
```

### CLI

```bash
# Text
mlx_lm.generate \
  --model froggeric/Mistral-Medium-3.5-128B-MLX-4bit \
  --prompt "Hello"

# Vision
mlx_vlm.generate \
  --model froggeric/Mistral-Medium-3.5-128B-MLX-4bit \
  --image image.jpg --prompt "Describe this image"
```

**Requirements:** `mlx-lm >= 0.31.2`, `mlx-vlm >= 0.4.4`

---

## System prompt

The model ships with a default system prompt ([`SYSTEM_PROMPT.txt`](SYSTEM_PROMPT.txt)) that includes date awareness and tool calling instructions. You can override it — the chat template injects the default only when no system message is provided.

---

## Thinking mode

Set `reasoning_effort` in your chat template call:

- `reasoning_effort="none"` — fast instant reply
- `reasoning_effort="high"` — deep reasoning with `[THINK]...[/THINK]` blocks

If your runtime doesn't support passing template variables (e.g. LM Studio community models), add `reasoning_effort=high` to your system prompt. This activates thinking mode the same way.

---

## Sampling

From [Mistral AI](https://docs.mistral.ai/models/best-practices/sampling) and [Unsloth](https://unsloth.ai/docs/models/mistral-3.5) recommendations.

### Reasoning mode (`reasoning_effort="high"`)

For complex prompts, coding, research, math, and agentic usage:

| Parameter | Value |
|-----------|-------|
| temperature | 0.7 |
| top_p | 0.95 |
| top_k | 20 |

### Non-reasoning mode (`reasoning_effort="none"`)

For fast replies, chat, extraction, and simple instructions:

| Parameter | Value |
|-----------|-------|
| temperature | 0.0–0.7 |
| top_p | 0.8 |

Lower temperature for deterministic/factual output, higher for creative tasks. Maximum context length: 262,144.

---

## This conversion

| | |
|---|---|
| **Source** | [mistralai/Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) (FP8 static, 133.6 GB) |
| **Quantization** | 4-bit affine, group_size=64 (~70 GB across 15 shards) |
| **Vision encoder** | Unquantized (Pixtral, 48 layers, full BF16) |
| **Projector + lm_head** | Unquantized |
| **Minimum RAM** | ~72 GB (70 GB weights + overhead) |

<details>
<summary>Architecture details</summary>

| Spec | Value |
|------|-------|
| Architecture | Dense — 127.7B params, all active per token |
| Text model | Ministral 3, 88 layers |
| Attention | 96 Q heads, 8 KV heads (GQA), head_dim 128 |
| FFN | intermediate_size 28672 |
| Context | 262K native (YaRN, factor 64) |
| RoPE | theta 1M, YaRN scaling |
| Vocab | 131K tokens (Tekken tokenizer) |
| Vision encoder | Pixtral — 48 layers, 1664 hidden, 16 heads |
| Image processing | 1540px max, patch_size 14, spatial_merge_size 2 |
| model_type | `mistral3` |

</details>

---

## Conversion notes

mlx-vlm's `mistral3` sanitize function had a bug where it did not strip the `model.` prefix from `model.vision_tower.*` and `model.multi_modal_projector.*` keys in the source safetensors. This caused 438 parameters to be rejected during weight loading. The fix: replace `model.vision_tower` → `vision_tower.vision_model` (strip prefix + add nesting) and add a `model.multi_modal_projector` → `multi_modal_projector` case. Applied locally to `mlx_vlm/models/mistral3/mistral3.py` before conversion.

---

## Credits

| Role | Author |
|------|--------|
| Original model | [Mistral AI](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) |
| MLX 4-bit conversion | [froggeric](https://huggingface.co/froggeric) |

## License

Modified MIT License — free for commercial and non-commercial use, with a revenue cap of $20M/month. See the [full license](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE).
