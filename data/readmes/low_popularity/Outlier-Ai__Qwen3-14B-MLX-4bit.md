---
license: apache-2.0
pipeline_tag: text-generation
library_name: mlx
base_model: Qwen/Qwen3-14B
base_model_relation: quantized
quantized_by: Outlier-Ai
tags:
- 4-bit
- 4bit
- apple-silicon
- chat
- conversational
- edge-ai
- function-calling
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
- private-ai
- quantized
- qwen
- qwen3
- reasoning
- safetensors
- text-generation
- thinking
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
- example_title: General knowledge
  messages:
  - role: user
    content: Explain mixture-of-experts models in plain language.
- example_title: Privacy rationale
  messages:
  - role: user
    content: Three practical reasons to run an LLM locally instead of in the cloud?
- example_title: Summarize
  messages:
  - role: user
    content: Summarize the difference between 4-bit and 8-bit quantization in two
      short paragraphs.
---
> **Run this on your Mac with [Outlier](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=qwen3_14b_mlx_4bit)** — a free macOS app for local MLX inference.

# Qwen3-14B (MLX 4-bit)

MLX 4-bit conversion of [`Qwen/Qwen3-14B`](https://huggingface.co/Qwen/Qwen3-14B). License and base-model fields inherit from the original — see YAML frontmatter above.

## Load with mlx-lm

```bash
pip install mlx-lm
python -m mlx_lm.generate --model Outlier-Ai/Qwen3-14B-MLX-4bit --prompt "Hello" --max-tokens 256
```

## What is Outlier?

A free macOS app that runs MLX models locally — no cloud, no API keys, no usage caps.

➡ **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=qwen3_14b_mlx_4bit)**

## Other Outlier conversions

- [Qwen3-Coder-30B-A3B-Instruct (MLX 4-bit) — MLX 4-bit conversion (1,598 downloads)](https://huggingface.co/Outlier-Ai/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit)
- [Qwen3-8B (MLX 4-bit) — MLX 4-bit conversion (107 downloads)](https://huggingface.co/Outlier-Ai/Qwen3-8B-MLX-4bit)
- [Qwen3-32B (MLX 4-bit) — MLX 4-bit conversion (98 downloads)](https://huggingface.co/Outlier-Ai/Qwen3-32B-MLX-4bit)
- [Outlier-Core-27B (MLX 4-bit) — MLX 4-bit conversion (55 downloads)](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit)
- [Outlier-Nano-4B (MLX 4-bit) — MLX 4-bit conversion (67 downloads)](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit)

## License

Inherits from upstream (`apache-2.0`). See base model card.
