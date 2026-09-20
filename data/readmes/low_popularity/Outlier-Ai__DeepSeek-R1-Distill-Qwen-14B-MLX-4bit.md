---
license: mit
pipeline_tag: text-generation
library_name: mlx
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
base_model_relation: quantized
quantized_by: Outlier-Ai
tags:
- 4-bit
- 4bit
- apple-silicon
- chain-of-thought
- chat
- conversational
- deepseek
- deepseek-r1
- deepseek-r1-distill
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
- quantized
- r1
- r1-distill
- reasoning
- safetensors
- text-generation
- thinking
language:
- en
- zh
- fr
- es
- pt
- de
- ru
- ja
- ko
- ar
widget:
- example_title: Widget math
  messages:
  - role: user
    content: If it takes 5 machines 5 minutes to make 5 widgets, how long would it
      take 100 machines to make 100 widgets? Show reasoning.
- example_title: Logic grid
  messages:
  - role: user
    content: Alice, Bob, and Carol each own a different pet. Alice does not own the
      dog. Bob owns the parrot. Who owns what?
- example_title: Word problem
  messages:
  - role: user
    content: A train leaves station A at 60 mph and another leaves station B, 180
      miles away, at 40 mph toward each other. When do they meet?
---
> **Run this on your Mac with [Outlier](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=deepseek_r1_distill_qwen_14b_mlx_4bit)** — a one-click app that loads MLX models locally. macOS arm64, free download.

# DeepSeek-R1-Distill-Qwen-14B (MLX 4-bit)

MLX 4-bit conversion of [`deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), repackaged for Apple Silicon. Original weights, original license — see frontmatter above. This repo only changes the on-disk format (safetensors, MLX 4-bit, `chat_template.jinja`, tokenizer).

## About this conversion

- **Format:** MLX 4-bit safetensors (group size 64, symmetric)
- **Tooling:** `mlx-lm` 0.31.x compatible
- **Files:** `model.safetensors` shards · `config.json` · tokenizer · `chat_template.jinja`
- **License:** inherits from the upstream base model — see YAML `license` field

### Load directly with `mlx-lm`

```bash
pip install mlx-lm
python -m mlx_lm.generate \
  --model Outlier-Ai/DeepSeek-R1-Distill-Qwen-14B-MLX-4bit \
  --prompt "Hello, world." \
  --max-tokens 256
```

Or in Python:

```python
from mlx_lm import load, generate
model, tokenizer = load("Outlier-Ai/DeepSeek-R1-Distill-Qwen-14B-MLX-4bit")
print(generate(model, tokenizer, prompt="Hello, world.", max_tokens=256))
```

## What is Outlier?

Outlier is a free macOS app that runs language models on your Mac, fully offline. Pick a model from a tier picker, click download, and chat — no API keys, no cloud round-trips, no usage caps. It ships with its own curated tier of MLX-4bit models and can also load any compatible MLX conversion (including this one) via the model picker.

➡ Download Outlier (free, Apple Silicon): **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=deepseek_r1_distill_qwen_14b_mlx_4bit)**

For benchmark numbers (MMLU, HumanEval, tok/s on M-series Macs) with full provenance, see [outlier.host/benchmarks](https://outlier.host/benchmarks?utm_source=hf&utm_medium=modelcard&utm_campaign=deepseek_r1_distill_qwen_14b_mlx_4bit).

## Other Outlier conversions

- [DeepSeek-R1-Distill-Qwen-7B (MLX 4-bit) — MLX 4-bit conversion (1,932 downloads)](https://huggingface.co/Outlier-Ai/DeepSeek-R1-Distill-Qwen-7B-MLX-4bit)
- [DeepSeek-R1-Distill-Qwen-32B (MLX 4-bit) — MLX 4-bit conversion (1,353 downloads)](https://huggingface.co/Outlier-Ai/DeepSeek-R1-Distill-Qwen-32B-MLX-4bit)
- [DeepSeek-R1-Distill-Llama-8B (MLX 4-bit) — MLX 4-bit conversion (1,148 downloads)](https://huggingface.co/Outlier-Ai/DeepSeek-R1-Distill-Llama-8B-MLX-4bit)
- [Outlier-Core-27B (MLX 4-bit) — MLX 4-bit conversion (55 downloads)](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit)
- [Outlier-Nano-4B (MLX 4-bit) — MLX 4-bit conversion (67 downloads)](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit)

## License

This conversion preserves the upstream license declared in the frontmatter (`mit`). Refer to the upstream base model card for the canonical license text and any usage restrictions.
