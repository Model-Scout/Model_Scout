---
license: apache-2.0
base_model: xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
base_model_relation: quantized
library_name: mlx
pipeline_tag: image-text-to-text
language:
- en
- zh
- ko
- ja
- es
- ru
tags:
- mlx
- optiq
- quantized
- 4bit
- mixed-precision
- qwen3.5
- reasoning
- distillation
- deepseek
- multimodal
- vision
- image-text-to-text
- mtp
- multi-token-prediction
- function-calling
- tool-use
- heretic
- uncensored
- apple-silicon
---

# mlx-community/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-OptiQ-4bit

> **Built with [mlx-optiq](https://mlx-optiq.com)**, the MLX-native toolkit to quantize, fine-tune, and serve LLMs locally on Apple Silicon, no PyTorch and no cloud. [All OptiQ quants](https://mlx-optiq.com/models) · [Docs](https://mlx-optiq.com/docs/)

OptiQ mixed-precision quant of [xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic), an uncensored (heretic) version of a DeepSeek-V4-Pro reasoning distill into Qwen3.5-9B. It is a Qwen3.5-family vision-language model with a bundled MTP speculation head. 8.2 GB on disk.

## What it is

| Property | Value |
|---|---|
| Base | xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic (Qwen3.5, 9B) |
| Method | OptiQ mixed-precision, per-layer 4/8-bit |
| Bit allocation | Reused from the [Qwen3.5-9B OptiQ recipe](https://huggingface.co/mlx-community/Qwen3.5-9B-OptiQ-4bit): the architecture is identical, so the per-layer sensitivity ranking transfers directly and no per-model sweep is needed |
| Layer split | 116 components at 4-bit, 134 at 8-bit |
| Group size | 64 |
| On disk | 8.2 GB |
| MTP | Speculation head preserved in `optiq/mtp.safetensors` |
| Vision | bf16 vision tower kept in `optiq_vision.safetensors` for image input |
| KV cache | Mixed-precision KV config in `kv_config.json` |

Following the naming `llama.cpp` uses for its mixed quants, the "4bit" label denotes the family, not the weighted average.

Checked after conversion against the bf16 model on the same prompts (facts, arithmetic, code, explanation): the answers match.

## Run it

```bash
pip install mlx-optiq
```

```python
import optiq  # registers the arch + MTP/vision sidecars
from mlx_lm import load, generate

model, tok = load("mlx-community/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-OptiQ-4bit")
prompt = tok.apply_chat_template(
    [{"role": "user", "content": "Explain mixed-precision quantization in two sentences."}],
    tokenize=False, add_generation_prompt=True,
)
print(generate(model, tok, prompt=prompt, max_tokens=400))
```

For image input plus an OpenAI- and Anthropic-compatible endpoint with mixed-precision KV cache:

```bash
optiq serve --model mlx-community/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-OptiQ-4bit
```

This is a reasoning model, so give it a generous token budget.

**LM Studio:** its downloader flattens the `optiq/` folder. Move `mtp.safetensors` back into `optiq/` or the speculation head is not found.

## Links

- **Project website:** [mlx-optiq.com](https://mlx-optiq.com/)
- **All OptiQ quants:** [mlx-optiq.com/models](https://mlx-optiq.com/models)
- **Base model:** [xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)
