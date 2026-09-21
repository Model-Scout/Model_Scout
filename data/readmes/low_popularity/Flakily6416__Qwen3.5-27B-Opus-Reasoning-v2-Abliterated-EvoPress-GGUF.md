---
license: apache-2.0
language:
- en
- zh
- ko
tags:
- gguf
- mamba
- uncensored
- reasoning
- chain-of-thought
- qwen3.5
base_model: Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2
pipeline_tag: image-text-to-text
datasets:
- nohurry/Opus-4.6-Reasoning-3000x-filtered
- Jackrong/Qwen3.5-reasoning-700x
- Roman1111111/claude-opus-4.6-10000x
---
# Note: This release currently does not have vision capabilities due to an oversight. 
I'll get this fixed as soon as my free lightning ai credits reset (or please get in touch if you would like to sponsor some A100 hours).

# Qwen 3.5 27B Opus-Reasoning v2 (Abliterated) - Mixed Precision GGUFs

This repository features traditional and EvoPress GGUF quants of an abliterated reasoning model. Built upon [**Jackrong's Claude-4.6-Opus Distillation v2**](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2), the model was uncensored via the [**Orion-Zhen pipeline**](https://github.com/Orion-zhen/abliteration) before being quantized with the [**EvoPress**](https://huggingface.co/EvoPress) mixed-precision strategy.
## 🔥 Model Lineage & Highlights
1. **Base:** [Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2) 
   - Distilled using 14,000+ Claude 4.6 Opus-style samples to drastically improve Chain-of-Thought (CoT) efficiency. 
   - Reduces unnecessarily long internal reasoning chains while maintaining top-tier benchmark scores (e.g., 96.91% pass@1 on HumanEval).
2. **Abliteration:** Processed via Orion-Zhen's open-source pipeline.

## ⚡ EvoPress Mixed-Precision Quantization
This release utilizes the **EvoPress** methodology to maximize intelligence-per-gigabyte in Hybrid Mamba architectures. Standard quantization often degrades the sensitive State Space Model (SSM) components; these quants solve that by using tiered-precision mapping.

**Key Methodology:** [EvoPress (GitHub/HF)](https://huggingface.co/EvoPress)

| File Name | Target BPW | VRAM Fit | Optimization Strategy |
| :--- | :---: | :--- | :--- |
| **Qwen-3.5-27B-Opus-Reasoning-Abliterated-EP3.5_bpw.gguf** | 3.5 | 12GB - 16GB | Q3_K Base + F32 Mamba/Norms |
| **Qwen-3.5-27B-Opus-Reasoning-Abliterated-EP4.25_bpw.gguf** | 4.25 | 16GB - 24GB | Q4_K Base + F32 Mamba/Norms |
| **Qwen-3.5-27B-Opus-Reasoning-Abliterated-EP5.0_bpw.gguf** | 5.0 | 24GB+ | Q5_K Base + F32 Mamba/Norms |

## 📊 Standard/Traditional Quantizations
Included for comparison and compatibility with older hardware.

| File | Type | Size |
| :--- | :--- | :--- |
| Qwen-3.5-27B-Opus-Reasoning-Abliterated-Q2_K.gguf | Q2_K | ~10 GB |
| Qwen-3.5-27B-Opus-Reasoning-Abliterated-Q3_K.gguf | Q3_K | ~13 GB |
| Qwen-3.5-27B-Opus-Reasoning-Abliterated-Q4_K.gguf | Q4_K | ~16 GB |
| Qwen-3.5-27B-Opus-Reasoning-Abliterated-Q5_K.gguf | Q5_K | ~19 GB |
| Qwen-3.5-27B-Opus-Reasoning-Abliterated-Q6_K.gguf | Q6_K | ~23 GB |

## 🛠️ Technical Details & Setup
- **Architecture:** Hybrid Mamba-Transformer (Qwen 3.5)
- **Quantization:** Performed using a modified `gptq-gguf-toolkit` for Mamba-aware layer mapping.
- **Requirements:** Use a recent build of `llama.cpp` (March 2026+) for full Hybrid Mamba support.

## 🤝 Credits & Acknowledgements
- **Jackrong:** For the Claude-4.6-Opus reasoning distillation methodology and published model.
- **Orion-Zhen:** For the abliteration and refusal-removal pipeline.
- **Alibaba Qwen Team:** For the base Qwen 3.5 architecture.
- **Flakily6416:** Quantization, layer-mapping, and Mixed-Precision optimization.