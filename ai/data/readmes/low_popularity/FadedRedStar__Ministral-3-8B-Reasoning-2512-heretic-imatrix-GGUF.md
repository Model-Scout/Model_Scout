---
base_model: coder3101/Ministral-3-8B-Reasoning-2512-heretic
base_model_relation: quantized
library_name: gguf
license: apache-2.0
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
pipeline_tag: image-text-to-text
tags:
- gguf
- llama.cpp
- image-text-to-text
- imatrix
- heretic
- mistral
- reasoning
- uncensored
- multimodal
- vision
- abliterated
- conversational
- iq4_nl
- q4_k_m
- q5_k_m
quantized_by: FadedRedStar
---

# 🤖 Ministral-3-8B-Reasoning-2512-heretic — Importance Matrix GGUF

This repository hosts importance-matrix (imatrix) optimized GGUF weights, available in multiple quantization formats, and the associated vision projection matrix for **Ministral-3-8B-Reasoning-2512-heretic**, quantized from the source floating-point tensors provided by [coder3101/Ministral-3-8B-Reasoning-2512-heretic](https://huggingface.co/coder3101/Ministral-3-8B-Reasoning-2512-heretic).

**🔄 Sister Repository:** Check out the [Standard GGUF Sister Repository](https://huggingface.co/FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-GGUF) for uncalibrated and full 8-bit precision options.

## 🎯 Matrix-Weighted Calibration (Imatrix)

An **Importance Matrix (imatrix)** calculation tracks activations across network layers using a calibration sequence, then weights the quantization process to preserve the parameters that matter most for output quality — improving fidelity at low bit depths.

➡️ **Calibration dataset:** Bartowski's `calibration_datav5.txt`.

> [!NOTE]
> * **`IQ4_NL` is included** because the matrix enables a non-linear 4-bit format that outperforms standard linear 4-bit quantization.
> * **`Q8_0` is absent** because 8-bit quantization already introduces near-zero degradation, making calibration unnecessary — see the standard sister repository for that variant.

## ℹ️ Model Profile & Core Features

**Ministral-3-8B-Reasoning-2512** is a vision-language model by Mistral AI from the Ministral 3 family, built for **edge deployment**. It combines an **8.4B language model** with a **0.4B vision encoder** for multimodal understanding, and is the reasoning post-trained variant — specifically optimised for **math, coding, STEM, and complex multi-step reasoning**. The model supports multilingual input, native function calling, JSON output, and best-in-class agentic capabilities at its scale.

The **heretic** suffix denotes post-processing via the **[Heretic v1.1.0](https://github.com/p-e-w/heretic)** abliteration framework performed by [coder3101](https://huggingface.co/coder3101), using the **direction_index** method to suppress refusal vectors while preserving reasoning chains and multimodal capabilities.

## 📋 Technical Specifications

| Property | Value |
|---|---|
| **Base Architecture** | Ministral-3 (8.4B LM + 0.4B Vision Encoder) |
| **Developed by** | Mistral AI |
| **Primary Use** | Reasoning, math, STEM, vision, agentic tasks |
| **Context Window** | 262,144 tokens |
| **Vision Encoder** | 0.4B (integrated, early-fusion) |
| **Languages** | English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic |
| **Abliteration Tool** | Heretic v1.1.0 |
| **Abliteration Method** | direction_index (single-direction refusal suppression) |
| **Prompt Format** | ChatML |

## 🛠️ Heretic Overrides (ARA)

| Property | Value |
|---|---|
| **direction_index** | 15.03 |
| **attn.o_proj.max_weight** | 1.17 |
| **attn.o_proj.max_weight_position** | 20.88 |
| **attn.o_proj.min_weight** | 0.55 |
| **attn.o_proj.min_weight_distance** | 2.72 |
| **mlp.down_proj.max_weight** | 1.49 |
| **mlp.down_proj.max_weight_position** | 23.45 |
| **mlp.down_proj.min_weight** | 1.40 |
| **mlp.down_proj.min_weight_distance** | 18.55 |

## 📊 Refusal Bypass Metrics

> [!NOTE]
> The metrics below are self-reported by the original model author ([coder3101](https://huggingface.co/coder3101)) and have not been independently reproduced.

| Metric | This model | Original ([mistralai/Ministral-3-8B-Reasoning-2512](https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512)) |
|---|---|---|
| **KL divergence** | 0.0712 | 0 *(by definition)* |
| **Refusals** | 4/100 | 96/100 |

## 🧮 Numerical & Tensor Formats

| Property | Value |
|---|---|
| **Text Tensor Types** | IQ4_NL, Q4_K_M, Q5_K_M (all with imatrix calibration) |
| **Importance Matrix** | Bartowski's `calibration_datav5.txt` |
| **Vision Tensors** | Q8_0, BF16 |

## 📦 Available Model Files

**Main model weights**
| Filename | Quantization | llama.cpp Build | Size | Download |
|---|---|---|---|---|
| `Ministral-3-8B-Reasoning-2512-heretic-IQ4_NL-imatrix.gguf` | `IQ4_NL` | `b9843` | 4.60 GB | [📥 Download](https://huggingface.co/FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-imatrix-GGUF/resolve/main/Ministral-3-8B-Reasoning-2512-heretic-IQ4_NL-imatrix.gguf) |
| `Ministral-3-8B-Reasoning-2512-heretic-Q4_K_M-imatrix.gguf` | `Q4_K_M` | `b9803` | 4.84 GB | [📥 Download](https://huggingface.co/FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-imatrix-GGUF/resolve/main/Ministral-3-8B-Reasoning-2512-heretic-Q4_K_M-imatrix.gguf) |
| `Ministral-3-8B-Reasoning-2512-heretic-Q5_K_M-imatrix.gguf` | `Q5_K_M` | `b9870` | 5.64 GB | [📥 Download](https://huggingface.co/FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-imatrix-GGUF/resolve/main/Ministral-3-8B-Reasoning-2512-heretic-Q5_K_M-imatrix.gguf) |

**mmproj — vision projector files**
| Filename | Quantization | Size | Download |
|---|---|---|---|
| `mmproj-Ministral-3-8B-Reasoning-2512-heretic-Q8_0.gguf` | `Q8_0` | 448 MB | [📥 Download](https://huggingface.co/FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-imatrix-GGUF/resolve/main/mmproj-Ministral-3-8B-Reasoning-2512-heretic-Q8_0.gguf) |
| `mmproj-Ministral-3-8B-Reasoning-2512-heretic-BF16.gguf` | `BF16` | 827 MB | [📥 Download](https://huggingface.co/FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-imatrix-GGUF/resolve/main/mmproj-Ministral-3-8B-Reasoning-2512-heretic-BF16.gguf) |

## 🎛️ Component Pairing Guide

Download exactly **one** main weights file:

* **`IQ4_NL`**: Non-linear 4-bit format, best choice for constrained memory when imatrix calibration is present.
* **`Q4_K_M`**: Balanced 4-bit format suitable for most everyday use.
* **`Q5_K_M`**: Higher-fidelity mid-range format recommended as a general default.

**mmproj files** (optional): multimodal vision projectors. Pass one via the `--mmproj` flag in llama.cpp to enable image input.
* **`BF16` (Recommended)**: Highest possible image processing accuracy. While older projectors were small, modern vision towers can hover around **1GB**. If you are tight on VRAM, it is completely viable to run this on system RAM (CPU) with a minimal performance penalty, saving your precious GPU space for the main model layers.
* **`Q8_0`**: Cuts the projector file size and memory footprint in half (~500MB for larger 1GB files). Use this if you prefer to keep the vision tower hosted entirely on your GPU but need to claw back some VRAM to avoid Out-Of-Memory (OOM) crashes.

## ⚡ Deployment & Execution Commands

> [!IMPORTANT]
> The vision projector (`--mmproj`) must be supplied at runtime whenever image inputs are used. Omitting it disables multimodal capability entirely.

> [!NOTE]
> Mistral AI recommends the following sampling configuration for best results: `temperature=0.7`, `top_p=0.95`.

> [!TIP]
> Swap the `-m` filename below for either quantized file depending on your size/quality trade-off preference.

### llama.cpp CLI (with image)

```bash
./llama-cli \
  -m Ministral-3-8B-Reasoning-2512-heretic-IQ4_NL-imatrix.gguf \
  --mmproj mmproj-Ministral-3-8B-Reasoning-2512-heretic-Q8_0.gguf \
  -c 8192 \
  -ngl 99 \
  --image "path/to/image.jpg" \
  -p "<|im_start|>user\nSolve the problem shown in the image step by step.<|im_end|>\n<|im_start|>assistant\n"
```

### OpenAI-Compatible API Server

```bash
./llama-server \
  --host 0.0.0.0 \
  --port 8080 \
  -m Ministral-3-8B-Reasoning-2512-heretic-IQ4_NL-imatrix.gguf \
  --mmproj mmproj-Ministral-3-8B-Reasoning-2512-heretic-Q8_0.gguf \
  -c 16384 \
  -ngl 99 \
  --flash-attn
```

---

## 💬 Chat Templates & Prompt Design (ChatML)

```text
<|im_start|>system
You are an expert reasoning assistant. Think step by step.<|im_end|>
<|im_start|>user
Your question or image payload here.<|im_end|>
<|im_start|>assistant
```

---

## ⚠️ Safety & Operational Notes

- This model is abliterated and will generate content that standard aligned models refuse. Use responsibly and in compliance with applicable laws.
- Designed for edge deployment; fits in 24 GB VRAM at BF16 and under 12 GB when quantized.
- Vision tensors are kept at BF16 or Q8_0 depending on the mmproj variant chosen, to prevent degradation of spatial and symbolic features in diagrams and formulas.
- Imatrix calibration improves perplexity recovery compared to non-imatrix quantization, particularly on low-frequency tokens.
- IQ4_NL produces a smaller file than Q4_K_M and tends to run faster on CPU and ARM devices; imatrix calibration narrows the quality gap between the two formats considerably.