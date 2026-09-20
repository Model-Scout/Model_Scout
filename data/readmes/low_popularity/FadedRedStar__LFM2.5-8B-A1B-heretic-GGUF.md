---
base_model: coder3101/LFM2.5-8B-A1B-heretic
base_model_relation: quantized
library_name: gguf
license: other
license_name: lfm-1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-350M/blob/main/LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
pipeline_tag: text-generation
tags:
- gguf
- llama.cpp
- text-generation
- heretic
- liquid-ai
- uncensored
- abliterated
- conversational
- q4_k_m
- q5_k_m
- q8_0
quantized_by: FadedRedStar
---

# 🤖 LFM2.5-8B-A1B-heretic — GGUF

This repository hosts GGUF weights for **LFM2.5-8B-A1B-heretic**, quantized from the source floating-point tensors provided by [coder3101/LFM2.5-8B-A1B-heretic](https://huggingface.co/coder3101/LFM2.5-8B-A1B-heretic).

**🔄 Sister Repository:** Check out the [Imatrix Sister Repository](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-imatrix-GGUF) for enhanced precision at lower bit fractions.

> [!NOTE]
> If you plan on using 4-bit or 5-bit variants, consider the **imatrix** sister repository instead — importance matrix calibration improves logic retention at those bit depths. This repository is best suited if you want the near-lossless `Q8_0` build.

## ℹ️ Model Profile & Core Features

**LFM2.5-8B-A1B** is a text-only model from Liquid AI's **Liquid Foundation Model 2.5** series, designed for on-device deployment. It uses a hybrid architecture with **24 layers — 18 double-gated LIV (Liquid, Input-adaptive, Value-selective) convolution layers plus 6 GQA (Grouped Query Attention) layers** — activating only approximately **1.5B parameters per forward pass** out of 8.3B total. This delivers fastest-in-class throughput at its size on both CPU and GPU, with day-one support for llama.cpp, MLX, vLLM, and SGLang. The model is a **reasoning model**: it produces a chain-of-thought before its final answer, and is tuned for **complex instruction following, tool calling, and chained agentic task execution**.

The **heretic** suffix denotes post-processing via the **[Heretic v1.2.0 Arbitrary-Rank Ablation (ARA)](https://github.com/p-e-w/heretic)** method with row-norm preservation performed by [coder3101](https://huggingface.co/coder3101), which removes refusal conditioning at multiple tensor ranks while maintaining the model's instruction-following and planning capabilities.

## 📋 Technical Specifications

| Property | Value |
|---|---|
| **Base Architecture** | LFM2.5 hybrid (18× double-gated LIV conv + 6× GQA) |
| **Developed by** | Liquid AI |
| **Total Parameters** | 8.3B |
| **Active Parameters** | ~1.5B per forward pass |
| **Primary Use** | Reasoning, instruction following, tool calling, agentic tasks |
| **Context Window** | 128,000 tokens |
| **Training Budget** | 38 trillion tokens |
| **Languages** | English, Arabic, Chinese, French, German, Japanese, Korean, Spanish, Portuguese |
| **Abliteration Tool** | Heretic v1.2.0 |
| **Abliteration Method** | Arbitrary-Rank Ablation (ARA) with row-norm preservation |
| **Prompt Format** | ChatML |

## 🛠️ Heretic Overrides (ARA)

| Property | Value |
|---|---|
| **start_layer_index** | 7 |
| **end_layer_index** | 21 |
| **preserve_good_behavior_weight** | 0.8548 |
| **steer_bad_behavior_weight** | 0.0004 |
| **overcorrect_relative_weight** | 0.9494 |
| **neighbor_count** | 8 |

## 📊 Refusal Bypass Metrics

> [!NOTE]
> The metrics below are self-reported by the original model author ([coder3101](https://huggingface.co/coder3101)) and have not been independently reproduced.

| Metric | This model | Original ([LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)) |
|---|---|---|
| **KL divergence** | 0.0239 | 0 *(by definition)* |
| **Refusals** | 12/100 | 91/100 |

## 🧮 Numerical & Tensor Formats

| Property | Value |
|---|---|
| **Quantization Type** | Q4_K_M, Q5_K_M, Q8_0 |

## 📦 Available Model Files

**Main model weights**
| Filename | Quantization | llama.cpp Build | Size | Download |
|---|---|---|---|---|
| `LFM2.5-8B-A1B-heretic-Q4_K_M.gguf` | `Q4_K_M` | `b9803` | 4.80 GB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-GGUF/resolve/main/LFM2.5-8B-A1B-heretic-Q4_K_M.gguf) |
| `LFM2.5-8B-A1B-heretic-Q5_K_M.gguf` | `Q5_K_M` | `b9870` | 5.62 GB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-GGUF/resolve/main/LFM2.5-8B-A1B-heretic-Q5_K_M.gguf) |
| `LFM2.5-8B-A1B-heretic-Q8_0.gguf` | `Q8_0` | `b9870` | 8.39 GB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-GGUF/resolve/main/LFM2.5-8B-A1B-heretic-Q8_0.gguf) |

## 🎛️ Component Pairing Guide

Download exactly **one** main weights file:

* **`Q4_K_M`**: Balanced 4-bit format suitable for most everyday use.
* **`Q5_K_M`**: Higher-fidelity mid-range format recommended as a general default.
* **`Q8_0`**: Near-lossless 8-bit format for when memory is not a constraint.

## ⚡ Deployment & Execution Commands

> [!NOTE]
> Liquid AI recommends the following generation parameters for best results: `temperature: 0.2`, `top_k: 80`, `repetition_penalty: 1.05`.

> [!NOTE]
> This model emits reasoning content before its final answer. If you require a clean final answer only, parse the output accordingly rather than expecting a single direct response.

> [!TIP]
> Swap the `-m` filename below for either quantized file depending on your size/quality trade-off preference.

### llama.cpp CLI

```bash
./llama-cli \
  -m LFM2.5-8B-A1B-heretic-Q4_K_M.gguf \
  -c 8192 \
  -ngl 99 \
  --temp 0.2 \
  --top-k 80 \
  --repeat-penalty 1.05 \
  -p "<|im_start|>system\nYou are a helpful and precise assistant capable of using tools and following complex instructions.<|im_end|>\n<|im_start|>user\nBreak down the following task and execute it step by step: summarise this document and list action items.<|im_end|>\n<|im_start|>assistant\n"
```

### OpenAI-Compatible API Server

```bash
./llama-server \
  --host 0.0.0.0 \
  --port 8080 \
  -m LFM2.5-8B-A1B-heretic-Q4_K_M.gguf \
  -c 16384 \
  -ngl 99 \
  --flash-attn
```

## 💬 Chat Templates & Prompt Design (ChatML)

```text
<|im_start|>system
You are a capable assistant. Follow instructions precisely.<|im_end|>
<|im_start|>user
Your task or query here.<|im_end|>
<|im_start|>assistant
```

## ⚠️ Safety & Operational Notes

- This model is abliterated and will generate content that standard aligned models refuse. Use responsibly and in compliance with applicable laws.
- This is a **text-only** model — it has no vision encoder and cannot process images.
- The LIV architecture activates only ~1.5B parameters per token, making it significantly faster to run than the total parameter count implies.
- For long-context workloads, set `-c` up to 131072 as needed.
- Liquid AI shipped a tokenizer fix for tool-calling after this model's initial release; if you encounter malformed tool-call output, verify your llama.cpp build includes this fix.
- For better output quality at this quantization level, consider the imatrix variant in the companion repository.