---
license: apache-2.0
pipeline_tag: text-generation
library_name: mlx
base_model: Qwen/Qwen2.5-Coder-32B-Instruct
base_model_relation: quantized
quantized_by: Outlier-Ai
tags:
- 4-bit
- 4bit
- apple-silicon
- chat
- code
- code-completion
- code-generation
- coding
- conversational
- edge-ai
- function-calling
- humaneval
- instruct
- local-llm
- m1
- m2
- m3
- m4
- mac
- mac-mini
- mac-studio
- macbook-air
- macbook-pro
- macos
- metal
- mlx
- mlx-community
- mlx-lm
- no-cloud
- offline
- on-device
- outlier
- outlier-app
- private
- quantized
- qwen25-coder
- safetensors
- text-generation
- tool-use
language:
- en
- zh
- fr
- es
- pt
- de
- it
- ru
- ja
- ko
- ar
- vi
- th
- nl
- pl
widget:
- example_title: Python prime check
  messages:
  - role: user
    content: Write a Python function that checks if a number is prime, with a short
      docstring and one edge case test.
- example_title: SQL join
  messages:
  - role: user
    content: Write a SQL query that returns the top 10 users by total purchase value
      in the last 90 days.
- example_title: Debug refactor
  messages:
  - role: user
    content: Refactor this for readability and flag one bug.
---

> **Conversion published by the Outlier team.** Not shipped in the Outlier app. Numbers below are from internal experiments, not our release tests. Shipped models: [Nano 4B](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit) · [Lite 9B](https://huggingface.co/Outlier-Ai/Outlier-Lite-9B-MLX-4bit) · [Quick 26B](https://huggingface.co/Outlier-Ai/Outlier-Quick-26B-MLX-4bit) · [Core 27B](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit).

> **Run this on your Mac with [Outlier](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=qwen2_5_coder_32b_instruct_mlx_4bit)** — a one-click app that loads MLX models locally. macOS arm64, free download.
> Outlier for Mac: free Nano and Lite; Pro is **$49 once**, on up to 3 Macs · `brew install --cask outlier-host/tap/outlier`

# Qwen2.5-Coder-32B-Instruct (MLX 4-bit)

MLX 4-bit conversion of [`Qwen/Qwen2.5-Coder-32B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct), repackaged for Apple Silicon. Original weights, original license — see frontmatter above. This repo only changes the on-disk format (safetensors, MLX 4-bit, `chat_template.jinja`, tokenizer).

## About this conversion

- **Format:** MLX 4-bit safetensors (group size 64, symmetric)
- **Tooling:** `mlx-lm` 0.31.x compatible
- **Files:** `model.safetensors` shards · `config.json` · tokenizer · `chat_template.jinja`
- **License:** inherits from the upstream base model — see YAML `license` field

### Load directly with `mlx-lm`

```bash
pip install mlx-lm
python -m mlx_lm.generate \
  --model Outlier-Ai/Qwen2.5-Coder-32B-Instruct-MLX-4bit \
  --prompt "Hello, world." \
  --max-tokens 256
```

Or in Python:

```python
from mlx_lm import load, generate
model, tokenizer = load("Outlier-Ai/Qwen2.5-Coder-32B-Instruct-MLX-4bit")
print(generate(model, tokenizer, prompt="Hello, world.", max_tokens=256))
```

## What is Outlier?

Outlier is a free macOS app that runs language models on your Mac, fully offline. Pick a model from a tier picker, click download, and chat — no API keys, no cloud round-trips, no usage caps. It ships with its own curated tier of MLX-4bit models and can also load any compatible MLX conversion (including this one) via the model picker.

➡ Download Outlier (free, Apple Silicon): **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=qwen2_5_coder_32b_instruct_mlx_4bit)**

For benchmark numbers (MMLU, HumanEval, tok/s on M-series Macs) with full provenance, see [outlier.host/benchmarks](https://outlier.host/benchmarks?utm_source=hf&utm_medium=modelcard&utm_campaign=qwen2_5_coder_32b_instruct_mlx_4bit).

## Other Outlier conversions

- [Qwen2.5-Coder-7B-Instruct (MLX 4-bit) — MLX 4-bit conversion (1,450 downloads)](https://huggingface.co/Outlier-Ai/Qwen2.5-Coder-7B-Instruct-MLX-4bit)
- [Qwen2.5-Coder-14B-Instruct (MLX 4-bit) — MLX 4-bit conversion (816 downloads)](https://huggingface.co/Outlier-Ai/Qwen2.5-Coder-14B-Instruct-MLX-4bit)
- [DeepSeek-R1-Distill-Qwen-7B (MLX 4-bit) — MLX 4-bit conversion (1,932 downloads)](https://huggingface.co/Outlier-Ai/DeepSeek-R1-Distill-Qwen-7B-MLX-4bit)
- [Outlier-Core-27B (MLX 4-bit) — MLX 4-bit conversion (55 downloads)](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit)
- [Outlier-Nano-4B (MLX 4-bit) — MLX 4-bit conversion (67 downloads)](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit)

## License

This conversion preserves the upstream license declared in the frontmatter (`apache-2.0`). Refer to the upstream base model card for the canonical license text and any usage restrictions.
