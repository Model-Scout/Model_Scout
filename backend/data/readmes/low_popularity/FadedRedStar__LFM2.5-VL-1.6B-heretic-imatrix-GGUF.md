---
base_model: coder3101/LFM2.5-VL-1.6B-heretic
base_model_relation: quantized
library_name: gguf
license: other
license_name: lfm-1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-350M/blob/main/LICENSE
language:
- en
- ja
- ko
- fr
- es
- de
- ar
- zh
pipeline_tag: image-text-to-text
tags:
- gguf
- llama.cpp
- image-text-to-text
- heretic
- liquid-ai
- uncensored
- multimodal
- imatrix
- abliterated
- conversational
- iq4_nl
- q4_k_m
- q5_k_m
quantized_by: FadedRedStar
---

# 🤖 LFM2.5-VL-1.6B-heretic — Importance Matrix GGUF

This repository hosts importance-matrix (imatrix) optimized GGUF weights, available in multiple quantization formats, and the associated vision projection matrix for **LFM2.5-VL-1.6B-heretic**, quantized from the source floating-point tensors provided by [coder3101/LFM2.5-VL-1.6B-heretic](https://huggingface.co/coder3101/LFM2.5-VL-1.6B-heretic).

**🔄 Sister Repository:** Check out the [Standard GGUF Sister Repository](https://huggingface.co/FadedRedStar/LFM2.5-VL-1.6B-heretic-GGUF) for uncalibrated and full 8-bit precision options.

## 🎯 Matrix-Weighted Calibration (Imatrix)

An **Importance Matrix (imatrix)** calculation tracks activations across network layers using a calibration sequence, then weights the quantization process to preserve the parameters that matter most for output quality — improving fidelity at low bit depths.

➡️ **Calibration dataset:** Bartowski's `calibration_datav5.txt`.

> [!NOTE]
> * **`IQ4_NL` is included** because the matrix enables a non-linear 4-bit format that outperforms standard linear 4-bit quantization.
> * **`Q8_0` is absent** because 8-bit quantization already introduces near-zero degradation, making calibration unnecessary — see the standard sister repository for that variant.

## ℹ️ Model Profile & Core Features

**LFM2.5-VL-1.6B** is the larger vision-language model in Liquid AI's LFM2.5-VL family, pairing the **LFM2 hybrid language backbone** (gated short convolutions interleaved with GQA) with a **SigLIP2 NaFlex** vision encoder for single- and multi-image understanding. It is designed to run comfortably on a single commodity GPU while supporting a 32,768-token context window, and ships with day-one support for llama.cpp, vLLM, and MLX.

The **heretic** suffix denotes post-processing via the **[Heretic v1.3.0](https://github.com/p-e-w/heretic)** method performed by [coder3101](https://huggingface.co/coder3101), which suppresses refusal behavior while preserving the model's vision-language capabilities.

## 📋 Technical Specifications

| Property | Value |
|---|---|
| **Base Architecture** | LFM2 hybrid (gated conv + GQA) + SigLIP2 NaFlex vision encoder |
| **Developed by** | Liquid AI |
| **Total Parameters** | 1.6B (LM + vision encoder) |
| **Vision Encoder** | SigLIP2 NaFlex, shape-optimized 400M |
| **Primary Use** | Single/multi-image understanding, visual Q&A |
| **Context Window** | 32,768 tokens |
| **Vision Projector** | Integrated (see repository files below) |
| **Languages** | English, Japanese, Korean, French, Spanish, German, Arabic, Chinese |
| **Abliteration Tool** | Heretic v1.3.0 |
| **Prompt Format** | ChatML |

## 🛠️ Heretic Overrides (ARA)

| Property | Value |
|---|---|
| **direction_index** | 10.24 |
| **attn.o_proj.max_weight** | 1.22 |
| **attn.o_proj.max_weight_position** | 10.01 |
| **attn.o_proj.min_weight** | 1.21 |
| **attn.o_proj.min_weight_distance** | 7.36 |
| **mlp.down_proj.max_weight** | 1.11 |
| **mlp.down_proj.max_weight_position** | 12.44 |
| **mlp.down_proj.min_weight** | 0.21 |
| **mlp.down_proj.min_weight_distance** | 5.13 |

## 📊 Refusal Bypass Metrics

> [!NOTE]
> The metrics below are self-reported by the original model author ([coder3101](https://huggingface.co/coder3101)) and have not been independently reproduced.

| Metric | This model | Original ([LiquidAI/LFM2.5-VL-1.6B](https://huggingface.co/LiquidAI/LFM2.5-VL-1.6B)) |
|---|---|---|
| **KL divergence** | 0.0114 | 0 *(by definition)* |
| **Refusals** | 8/100 | 95/100 |

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
| `LFM2.5-VL-1.6B-heretic-IQ4_NL-imatrix.gguf` | `IQ4_NL` | `b9860` | 664 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-VL-1.6B-heretic-imatrix-GGUF/resolve/main/LFM2.5-VL-1.6B-heretic-IQ4_NL-imatrix.gguf) |
| `LFM2.5-VL-1.6B-heretic-Q4_K_M-imatrix.gguf` | `Q4_K_M` | `b9860` | 697 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-VL-1.6B-heretic-imatrix-GGUF/resolve/main/LFM2.5-VL-1.6B-heretic-Q4_K_M-imatrix.gguf) |
| `LFM2.5-VL-1.6B-heretic-Q5_K_M-imatrix.gguf` | `Q5_K_M` | `b9860` | 804 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-VL-1.6B-heretic-imatrix-GGUF/resolve/main/LFM2.5-VL-1.6B-heretic-Q5_K_M-imatrix.gguf) |

**mmproj — vision projector files**
| Filename | Quantization | Size | Download |
|---|---|---|---|
| `mmproj-LFM2.5-VL-1.6B-heretic-Q8_0.gguf` | `Q8_0` | 556 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-VL-1.6B-heretic-imatrix-GGUF/resolve/main/mmproj-LFM2.5-VL-1.6B-heretic-Q8_0.gguf) |
| `mmproj-LFM2.5-VL-1.6B-heretic-BF16.gguf` | `BF16` | 816 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-VL-1.6B-heretic-imatrix-GGUF/resolve/main/mmproj-LFM2.5-VL-1.6B-heretic-BF16.gguf) |

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
> LiquidAI recommends the following sampling configuration for best results:
> * Text: `temperature=0.1`, `min_p=0.15`, `repetition_penalty=1.05`.
> * Vision: `min_image_tokens=64`, `max_image_tokens=256`, `do_image_splitting=True`.

> [!TIP]
> Swap the `-m` filename below for either quantized file depending on your size/quality trade-off preference.

### llama.cpp CLI (with image)

```bash
./llama-cli \
  -m LFM2.5-VL-1.6B-heretic-IQ4_NL-imatrix.gguf \
  --mmproj mmproj-LFM2.5-VL-1.6B-heretic-Q8_0.gguf \
  -c 8192 \
  -ngl 99 \
  --image "path/to/image.jpg" \
  -p "<|im_start|>user\nDescribe what you see in this image.<|im_end|>\n<|im_start|>assistant\n"
```

### OpenAI-Compatible API Server

```bash
./llama-server \
  --host 0.0.0.0 \
  --port 8080 \
  -m LFM2.5-VL-1.6B-heretic-IQ4_NL-imatrix.gguf \
  --mmproj mmproj-LFM2.5-VL-1.6B-heretic-Q8_0.gguf \
  -c 16384 \
  -ngl 99 \
  --flash-attn
```

## 💬 Chat Templates & Prompt Design (ChatML)

```text
<|im_start|>system
You are a helpful multimodal assistant.<|im_end|>
<|im_start|>user
Your question or image payload here.<|im_end|>
<|im_start|>assistant
```

## ⚠️ Safety & Operational Notes

- This model is abliterated and will generate content that standard aligned models refuse. Use responsibly and in compliance with applicable laws.
- Fits comfortably on a single GPU with at least 8 GB VRAM at quantized precision.
- Context window is limited to 32,768 tokens — shorter than the text-only LFM2.5 models.
- Vision tensors are kept at BF16 or Q8_0 depending on the mmproj variant chosen, to preserve visual feature quality.
- Imatrix calibration improves perplexity recovery compared to non-imatrix quantization, particularly on low-frequency tokens.
- IQ4_NL produces a smaller file than Q4_K_M and tends to run faster on CPU and ARM devices; imatrix calibration narrows the quality gap between the two formats considerably.