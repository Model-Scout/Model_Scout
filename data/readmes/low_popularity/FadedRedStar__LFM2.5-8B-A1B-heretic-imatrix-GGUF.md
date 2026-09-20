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
- imatrix
- abliterated
- conversational
- iq4_nl
- q4_k_m
- q5_k_m
quantized_by: FadedRedStar
---

# 🤖 LFM2.5-8B-A1B-heretic — Importance Matrix GGUF

This repository hosts importance-matrix (imatrix) optimized GGUF weights, available in multiple quantization formats, for **LFM2.5-8B-A1B-heretic**, quantized from the source floating-point tensors provided by [coder3101/LFM2.5-8B-A1B-heretic](https://huggingface.co/coder3101/LFM2.5-8B-A1B-heretic).

**🔄 Sister Repository:** Check out the [Standard GGUF Sister Repository](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-GGUF) for uncalibrated and full 8-bit precision options.

## 🎯 Matrix-Weighted Calibration (Imatrix)

An **Importance Matrix (imatrix)** calculation tracks activations across network layers using a calibration sequence, then weights the quantization process to preserve the parameters that matter most for output quality — improving fidelity at low bit depths.

➡️ **Calibration dataset:** Bartowski's `calibration_datav5.txt`.

> [!NOTE]
> * **`IQ4_NL` is included** because the matrix enables a non-linear 4-bit format that outperforms standard linear 4-bit quantization.
> * **`Q8_0` is absent** because 8-bit quantization already introduces near-zero degradation, making calibration unnecessary — see the standard sister repository for that variant.

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
| **Quantization Types** | IQ4_NL, Q4_K_M, Q5_K_M (all with imatrix calibration) |
| **Importance Matrix** | Bartowski's `calibration_datav5.txt` |

## 📦 Available Model Files

**Main model weights**
| Filename | Quantization | llama.cpp Build | Size | Download |
|---|---|---|---|---|
| `LFM2.5-8B-A1B-heretic-IQ4_NL-imatrix.gguf` | `IQ4_NL` | `b9843` | 4.51 GB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-imatrix-GGUF/resolve/main/LFM2.5-8B-A1B-heretic-IQ4_NL-imatrix.gguf) |
| `LFM2.5-8B-A1B-heretic-Q4_K_M-imatrix.gguf` | `Q4_K_M` | `b9803` | 4.80 GB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-imatrix-GGUF/resolve/main/LFM2.5-8B-A1B-heretic-Q4_K_M-imatrix.gguf) |
| `LFM2.5-8B-A1B-heretic-Q5_K_M-imatrix.gguf` | `Q5_K_M` | `b9870` | 5.62 GB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-8B-A1B-heretic-imatrix-GGUF/resolve/main/LFM2.5-8B-A1B-heretic-Q5_K_M-imatrix.gguf) |

## 🎛️ Component Pairing Guide

Download exactly **one** main weights file:

* **`IQ4_NL`**: Non-linear 4-bit format, best choice for constrained memory when imatrix calibration is present.
* **`Q4_K_M`**: Balanced 4-bit format suitable for most everyday use.
* **`Q5_K_M`**: Higher-fidelity mid-range format recommended as a general default.

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
  -m LFM2.5-8B-A1B-heretic-IQ4_NL-imatrix.gguf \
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
  -m LFM2.5-8B-A1B-heretic-IQ4_NL-imatrix.gguf \
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
- Imatrix calibration improves perplexity recovery compared to non-imatrix quantization, particularly on low-frequency tokens.
- IQ4_NL produces a smaller file than Q4_K_M and tends to run faster on CPU and ARM devices; imatrix calibration narrows the quality gap between the two formats considerably.