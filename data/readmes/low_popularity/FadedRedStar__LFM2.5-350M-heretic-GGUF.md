---
base_model: coder3101/LFM2.5-350M-heretic
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

# 🤖 LFM2.5-350M-heretic — GGUF

This repository hosts GGUF weights for **LFM2.5-350M-heretic**, quantized from the source floating-point tensors provided by [coder3101/LFM2.5-350M-heretic](https://huggingface.co/coder3101/LFM2.5-350M-heretic).

**🔄 Sister Repository:** Check out the [Imatrix Sister Repository](https://huggingface.co/FadedRedStar/LFM2.5-350M-heretic-imatrix-GGUF) for enhanced precision at lower bit fractions.

> [!NOTE]
> If you plan on using 4-bit or 5-bit variants, consider the **imatrix** sister repository instead — importance matrix calibration improves logic retention at those bit depths. This repository is best suited if you want the near-lossless `Q8_0` build.

## ℹ️ Model Profile & Core Features

**LFM2.5-350M** is the smallest text-only model in Liquid AI's **Liquid Foundation Model 2.5** series, built for extreme on-device and edge deployment. It shares the family's hybrid architecture of double-gated LIV (Liquid, Input-adaptive, Value-selective) convolution layers interleaved with GQA (Grouped Query Attention) layers, pre-trained on 28 trillion tokens with large-scale reinforcement learning post-training. Despite its size, it is tuned for **instruction following, lightweight tool calling, and structured data extraction**, with day-one support across llama.cpp, MLX, vLLM, SGLang, ONNX, and OpenVINO.

The **heretic** suffix denotes post-processing via the **[Heretic v1.3.0](https://github.com/p-e-w/heretic)** method performed by [coder3101](https://huggingface.co/coder3101), which removes refusal conditioning while preserving the model's lightweight instruction-following behavior.

## 📋 Technical Specifications

| Property | Value |
|---|---|
| **Base Architecture** | LFM2 hybrid (double-gated LIV conv + GQA) |
| **Developed by** | Liquid AI |
| **Total Parameters** | 350M |
| **Primary Use** | Instruction following, lightweight tool calling, structured extraction |
| **Context Window** | 131,072 tokens |
| **Training Budget** | 28 trillion tokens |
| **Languages** | English, Arabic, Chinese, French, German, Japanese, Korean, Spanish, Portuguese |
| **Abliteration Tool** | Heretic v1.3.0 |
| **Prompt Format** | ChatML |

## 🛠️ Heretic Overrides (ARA)

| Property | Value |
|---|---|
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.08 |
| **attn.o_proj.max_weight_position** | 10.46 |
| **attn.o_proj.min_weight** | 0.87 |
| **attn.o_proj.min_weight_distance** | 3.56 |
| **mlp.down_proj.max_weight** | 1.44 |
| **mlp.down_proj.max_weight_position** | 12.00 |
| **mlp.down_proj.min_weight** | 1.22 |
| **mlp.down_proj.min_weight_distance** | 1.97 |

## 📊 Refusal Bypass Metrics

> [!NOTE]
> The metrics below are self-reported by the original model author ([coder3101](https://huggingface.co/coder3101)) and have not been independently reproduced.

| Metric | This model | Original ([LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M)) |
|---|---|---|
| **KL divergence** | 0.0440 | 0 *(by definition)* |
| **Refusals** | 6/100 | 90/100 |

## 🧮 Numerical & Tensor Formats

| Property | Value |
|---|---|
| **Quantization Type** | Q4_K_M, Q5_K_M, Q8_0 |

## 📦 Available Model Files

**Main model weights**
| Filename | Quantization | llama.cpp Build | Size | Download |
|---|---|---|---|---|
| `LFM2.5-350M-heretic-Q4_K_M.gguf` | `Q4_K_M` | `b9860` | 219 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-350M-heretic-GGUF/resolve/main/LFM2.5-350M-heretic-Q4_K_M.gguf) |
| `LFM2.5-350M-heretic-Q5_K_M.gguf` | `Q5_K_M` | `b9860` | 248 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-350M-heretic-GGUF/resolve/main/LFM2.5-350M-heretic-Q5_K_M.gguf) |
| `LFM2.5-350M-heretic-Q8_0.gguf` | `Q8_0` | `b9860` | 362 MB | [📥 Download](https://huggingface.co/FadedRedStar/LFM2.5-350M-heretic-GGUF/resolve/main/LFM2.5-350M-heretic-Q8_0.gguf) |

## 🎛️ Component Pairing Guide

Download exactly **one** main weights file:

* **`Q4_K_M`**: Balanced 4-bit format suitable for most everyday use.
* **`Q5_K_M`**: Higher-fidelity mid-range format recommended as a general default.
* **`Q8_0`**: Near-lossless 8-bit format for when memory is not a constraint.

## ⚡ Deployment & Execution Commands

> [!NOTE]
> Liquid AI recommends the following generation parameters for best results: `temperature: 0.1`, `top_k: 50`, `repetition_penalty: 1.05`.

> [!TIP]
> Swap the `-m` filename below for either quantized file depending on your size/quality trade-off preference.

### llama.cpp CLI

```bash
./llama-cli \
  -m LFM2.5-350M-heretic-Q4_K_M.gguf \
  -c 8192 \
  -ngl 99 \
  --temp 0.3 \
  --top-k 40 \
  --repeat-penalty 1.05 \
  -p "<|im_start|>system\nYou are a concise, helpful assistant.<|im_end|>\n<|im_start|>user\nState the capital of Italy and one interesting fact about it.<|im_end|>\n<|im_start|>assistant\n"
```

### OpenAI-Compatible API Server

```bash
./llama-server \
  --host 0.0.0.0 \
  --port 8080 \
  -m LFM2.5-350M-heretic-Q4_K_M.gguf \
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
- Despite its small footprint, IFBench and structured-extraction benchmarks show substantial generational gains over LFM2 predecessors.
- Best suited for constrained hardware: CPUs, NPUs, and edge devices rather than complex reasoning workloads.
- For better output quality at this quantization level, consider the imatrix variant in the companion repository.