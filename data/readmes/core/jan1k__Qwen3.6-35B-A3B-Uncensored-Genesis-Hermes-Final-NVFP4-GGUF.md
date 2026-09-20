---
license: apache-2.0
tags:
- text-generation
- gguf
- nvfp4
- fp4
- moe
- qwen3.6
- hermes
- uncensored
- vision
- multimodal
- genesis
- agentic
- llama-cpp
language:
- en
- zh
- multilingual
datasets:
- NousResearch/hermes-function-calling-v1
pipeline_tag: image-text-to-text
base_model:
- HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
- LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-GGUF
base_model_relation: quantized
---

# 🌟 Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-NVFP4-GGUF

This repository contains the **NVFP4 (NVIDIA 4-bit Floating Point)** quantized GGUF release of **LuffyTheFox**'s latest updated Hermes model: [LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-GGUF).

- **Original Model & Genesis Tensor Repair:** [LuffyTheFox](https://huggingface.co/LuffyTheFox) — [Original Model Repo](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-GGUF)
- **NVFP4 Quantization:** [jan1k](https://huggingface.co/jan1k)
- **Base Model:** [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) (0/465 refusals)
- **Hermes Finetune:** [DJLougen/hermes-qwen3.5-35b-a3b-GGUF](https://huggingface.co/DJLougen/hermes-qwen3.5-35b-a3b-GGUF) (Transferred data from finetune on Hermes dataset — around 2k blocks from two FFN expert tensors to HauhauCS uncensored base)
- **Quantization Format:** NVFP4 (NVIDIA FP4) GGUF (optimized for NVIDIA Ada Lovelace / Blackwell / Ampere GPUs)
- **Architecture:** Mixture of Experts (MoE) — 35B total parameters / ~3B active per token (8 routed experts + 1 shared)
- **Multimodal (Vision):** Supported via `mmproj-Hermes3.6-35B-A3B-Uncensored-Genesis-Final-F16.gguf`

---

## ⚡ Provided Files & Versions

| File | Size | Method / Description |
| :--- | :--- | :--- |
| **`Hermes3.6-35B-A3B-Uncensored-Genesis-Final-NVFP4-v4.gguf`** | ~20.0 GB | **Recommended (v4):** Inline NVFP4 scales only — no separate `.scale`/`.input_scale` tensors. LM Studio / Pelican compatible. Two-step (`Q8_K_P` &rarr; `F16` &rarr; `NVFP4`) with `--nvfp4-inline-scales-only`. |
| `Hermes3.6-35B-A3B-Uncensored-Genesis-Final-NVFP4-v2.gguf` | ~20.0 GB (21.47 GB) | **Deprecated (v2):** Uses separate `.scale`/`.input_scale` tensors that break LM Studio / Pelican. Use v4 instead. |
| `Hermes3.6-35B-A3B-Uncensored-Genesis-Final-NVFP4.gguf` | ~19.6 GB (21.05 GB) | **Deprecated (v1):** Flawed pipeline + separate scales. Do not use. |
| `mmproj-Hermes3.6-35B-A3B-Uncensored-Genesis-Final-F16.gguf` | ~899 MB | Vision projector (F16) for multimodal / vision tasks. |
| `chat_template.jinja` | ~3.3 KB | Optimized chat template (thanks to froggeric & qweefchief). |

### What makes v4 different from v2?

The v2 files use the extended NVFP4 format with separate `.scale` and
`.input_scale` tensors. Runtimes like LM Studio / Pelican only read inline
UE4M3 scales and ignore the separate scale tensors, producing garbage output.

v4 uses `--nvfp4-inline-scales-only` to emit native inline NVFP4 scales without
separate scale tensors. This matches the format used by Luffy's working NVFP4
files and is compatible with LM Studio, Pelican, and llama.cpp.

Imatrix variants (v4-imx-v5, v4-imx-v6) will follow after the plain v4 is
confirmed working in target runtimes.

---

## ⚡ What is Genesis?

> **Genesis** is a post-training data regeneration and calibration algorithm for neural networks (LLM) in GGUF format developed by [LuffyTheFox](https://huggingface.co/LuffyTheFox) over almost half a year of development with AI assistance. It is optimized, architecture-independent, works with any model in GGUF format, and is based on mathematical statistics.
>
> LLM models often suffer from:
> - **Saturated weights:** activations get stuck, gradients vanish, outputs degrade.
> - **Scale mismatches:** one layer's weights are 10× larger than peers for no valid reason.
> - **Mean drift:** weight distributions shifted positive or negative, breaking symmetry assumptions.
> - **Zero blocks:** zero blocks corrupt the signal, turning training into noise amplification.
> - **Training noise:** increases randomness and ruins output quality.
>
> Genesis fixes all of that without retraining — pure numerical surgery on the raw bytes of the file:
> 1. **Stage 1:** Scans `ssm_conv1d` tensors (handling long-context memory) and repairs balance between heads.
> 2. **Stage 2:** Scans blocks in chunks (via 3 parameters) and picks the best fit to weight distribution in the tensor, replacing zero blocks without touching learned structure.
> 3. **Stage 3:** Scans for noise via custom SVD (excluding `token_embd.weight`, `output.weight`, 1D tensors, bias, and norms). Reduces training noise based on the [Marchenko–Pastur law](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution) while preserving 99% of signal and learned gradient.

---

## ⚡ Recommended Settings & Prompts

Chat template: Use `chat_template.jinja` with `--jinja` flag in llama.cpp / LM Studio.

- Set **K Cache Quantization Type** and **V Cache Quantization Type** to **F16**.
- Set **GPU offload** to maximum. Set number of **active experts** to **8**.

### System Prompts
For best stability and first experience, start with:
```
You are Qwen (Tongyi Qianwen), a large language model developed by Alibaba Group's Tongyi Lab. You are a helpful assistant.
```

For agentic / function calling tasks:
```
You are Qwen (Tongyi Qianwen), a large language model developed by Alibaba Group's Tongyi Lab. You are a helpful assistant that answers in JSON. Here's the json schema you must adhere to:
<schema>
{schema}
</schema>
```

### Sampling Parameters

**Thinking mode (coding / precision):**
- Hermes agent: `temperature=0.6, top_p=disabled, top_k=20, min_p=disabled, seed=42, presence_penalty=disabled, repeat_penalty=1.05`
- Coding / precise tasks: `temperature=0.6, top_p=disabled, top_k=20, min_p=disabled, seed=42, presence_penalty=disabled, repeat_penalty=disabled`
- General: `temperature=0.95, top_p=disabled, top_k=20, min_p=disabled, seed=42, presence_penalty=disabled, repeat_penalty=disabled`

**Non Thinking mode (creative):**
- General: `temperature=0.95, top_p=disabled, top_k=20, min_p=disabled, seed=42, presence_penalty=disabled, repeat_penalty=disabled`
- Deterministic: `temperature=0.0, top_p=disabled, top_k=20, min_p=disabled, seed=42, presence_penalty=disabled, repeat_penalty=disabled`

---

## ⚡ Specs

- **Total parameters:** 35B (~3B active per forward pass MoE)
- **Experts:** 256 experts, 8 routed + 1 shared per token
- **Architecture:** Hybrid Gated DeltaNet linear attention + full softmax attention (3:1 ratio)
- **Layers:** 40 layers, pattern: 10 × (3 × DeltaNet-MoE + 1 × Attention-MoE)
- **Context:** 262K native context (extendable to 1M with YaRN)
- **Multimodal:** Natively multimodal (text, image, video) with mmproj
- **Vocabulary:** 248K vocabulary, 201 languages

---

## ⚡ Compatibility & Usage

Works seamlessly with `llama.cpp`, `LM Studio`, `koboldcpp`, and any NVFP4 / GGUF compatible runtime.

```bash
llama-cli -m Hermes3.6-35B-A3B-Uncensored-Genesis-Final-NVFP4-v4.gguf \
  --mmproj mmproj-Hermes3.6-35B-A3B-Uncensored-Genesis-Final-F16.gguf \
  --jinja -c 131072 -ngl 99
```

---

## ⚡ Credits & Acknowledgments

- [LuffyTheFox](https://huggingface.co/LuffyTheFox) — Creator of the Genesis algorithm and model repair.
- [HauhauCS](https://huggingface.co/HauhauCS) — Base uncensored model.
- [NousResearch](https://huggingface.co/NousResearch) — Hermes function calling dataset.
- [jan1k](https://huggingface.co/jan1k) — NVFP4 quantizations.
