---
license: apache-2.0
pipeline_tag: text-generation
library_name: gguf
base_model: Qwen/Qwen2.5-14B-Instruct
base_model_relation: quantized
quantized_by: Outlier-Ai
tags:
- gguf
- llama-cpp
- llama.cpp
- ollama
- lm-studio
- jan
- quantized
- 4bit
- 4-bit
- 5-bit
- 8-bit
- local-llm
- on-device
- cpu
- edge-ai
- offline
- outlier
- outlier-app
- qwen2.5
- qwen
- text-generation
- conversational
- chat
- instruct
- windows
- linux
- mac
- function-calling
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
    content: Explain how mixture-of-experts models work in plain language, for a curious
      but non-technical reader.
- example_title: Privacy rationale
  messages:
  - role: user
    content: What are three practical reasons someone might want to run an LLM locally
      instead of in the cloud?
- example_title: Summarize
  messages:
  - role: user
    content: Summarize the differences between 4-bit and 8-bit quantization in two
      short paragraphs.
---

> **Research checkpoint.** Not shipped in the Outlier app. Numbers below are from internal experiments, not our release tests. Shipped models: [Nano 4B](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit) · [Lite 9B](https://huggingface.co/Outlier-Ai/Outlier-Lite-9B-MLX-4bit) · [Quick 26B](https://huggingface.co/Outlier-Ai/Outlier-Quick-26B-MLX-4bit) · [Core 27B](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit).

> **Superseded.** This repo is a research artifact from an earlier Outlier lineage and is no longer the recommended download. The current shipping tier is at **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=outlier_compact_14b_gguf)**.
> Outlier for Mac: free Nano and Lite; Pro is **$49 once**, on up to 3 Macs · `brew install --cask outlier-host/tap/outlier`

# Outlier-Compact-14B (GGUF)

This repo predates the v1.8 Outlier lineup. It is preserved here for reproducibility and historical reference, not as a production recommendation.

## What replaced it

Current shipping tiers (see Outlier app v1.8+):

- [Outlier Nano 4B — current entry tier](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit)
- [Outlier Core 27B — current default tier](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit)
- [Outlier Vision 35B-A3B — current multimodal tier](https://huggingface.co/Outlier-Ai/Outlier-Vision-35B-A3B-MLX-4bit)
- [DeepSeek-R1-Distill-Qwen-7B — popular reasoning model](https://huggingface.co/Outlier-Ai/DeepSeek-R1-Distill-Qwen-7B-MLX-4bit)
- [Qwen3-Coder-30B-A3B — popular coding model](https://huggingface.co/Outlier-Ai/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit)

For the latest verified benchmarks and downloads, visit **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=outlier_compact_14b_gguf)**.

## Original notes

This was a research / preview artifact. It may contain experimental adapters, overlays, or quantization variants that did not graduate into the shipping product. Treat any technical claims in earlier revisions of this card as provisional.

## License

See YAML frontmatter above. Original license terms preserved.
