---
language:
- en
- fr
- de
- es
- ja
- ko
- zh
library_name: mlx
license: apache-2.0
base_model: mistralai/Mistral-Small-4-119B-2603
tags:
- jang
- quantized
- mixed-precision
- apple-silicon
- mlx
- vlm
- reasoning
- thinking
- moe
- mla
pipeline_tag: text-generation
---

<p align="center">
  <a href="https://mlx.studio"><img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/mlx-studio-light.png" alt="MLX Studio" width="500"></a>
</p>

<h4 align="center"><a href="https://mlx.studio">MLX Studio</a> — the only app that natively supports JANG models with reasoning</h4>

---

<p align="center">
  <img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/jangq-logo-dark.png" alt="JANG" width="300">
</p>

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

<h3 align="center">Mistral Small 4 (119B-A6B) — JANG_2L (2.14-bit) — Reasoning + VLM</h3>
<p align="center"><b>JANG</b> — Jang Adaptive N-bit Grading | The GGUF Equivalent for MLX</p>

<p align="center">
  <a href="https://github.com/jjang-ai/jangq"><img src="https://img.shields.io/badge/GitHub-Source_Code-blue?logo=github" alt="GitHub"></a>&nbsp;
  <a href="https://pypi.org/project/jang/"><img src="https://img.shields.io/pypi/v/jang?label=PyPI&color=green" alt="PyPI"></a>&nbsp;
  <a href="https://jangq.ai"><img src="https://img.shields.io/badge/Web-jangq.ai-orange" alt="Website"></a>&nbsp;
  <a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/X-@dealignai-black?logo=x" alt="X/Twitter"></a>
</p>

> **JANG is fully open-source.** Quantization engine and full commit history: [github.com/jjang-ai/jangq](https://github.com/jjang-ai/jangq). Created by [Jinho Jang](mailto:eric@jangq.ai).

---

> **First Mistral Small 4 (119B) on Apple Silicon.** MLA attention + 128 MoE experts + Pixtral VLM. 5x faster prefill than MLX Community 4-bit.

> **Reasoning mode:** Set reasoning_effort to "high" for step-by-step reasoning with [THINK]...[/THINK] tags.

---

## Speed Comparison — JANG vs MLX Community

| Model | Size | Gen tok/s | Prefill tok/s | RAM | Fits On |
|-------|:----:|:---------:|:-------------:|:---:|---------|
| **JANG_2L (this model)** | **30 GB** | **82** | **216** | **40 GB** | **48 GB Macs** |
| JANG_4M | 57 GB | 80 | 202 | 68 GB | 96+ GB Macs |
| JANG_6M | 84 GB | 74 | 160 | 95 GB | 128+ GB Macs |
| MLX Community 4-bit | 63 GB | 84 | 43 | 68 GB | 96+ GB Macs |

- **5x faster prefill** (216 vs 43 tok/s)
- **Half the size** (30 GB vs 63 GB) at comparable generation speed
- Benchmarked on M3 Ultra 256 GB with bfloat16 compute

## Key Features

- **82 tok/s** generation on M3 Ultra — matches MLX 4-bit at half the size
- **30 GB** on disk, **40 GB** peak RAM — fits 48 GB Macs (M4 Pro, M2/M3 Max)
- **Vision (VLM)**: Pixtral encoder, 1540px max, processes images
- **Reasoning mode**: [THINK]...[/THINK] step-by-step reasoning
- **Code generation**: Complete functions with docstrings and optimized logic
- **Math**: Step-by-step calculations with distributive property
- **119B total / 6B active** per token — MLA attention + 128 MoE experts

## Architecture



## JANG_2L Bit Allocation

| Tensor Type | Bits | Purpose |
|------------|:----:|---------|
| Attention (q/k/v/o projections) | 8 | Critical — preserves MLA precision |
| Embeddings, lm_head | 8 | Critical — token representation |
| MoE gate (router) | 16 | Float16 passthrough — routing precision |
| Shared experts | 6 | Important — always active |
| Routed experts (128) | 2 | Compressed — many experts = redundancy |
| Norms, biases | full | Float — tiny tensors, keep exact |

## Results: 94.0% MMLU at 2-bit (200 Questions, Reasoning Mode)

| Subject | Score |
|---------|:-----:|
| Abstract Algebra | 13/20 (65%) |
| Anatomy | **20/20 (100%)** |
| Astronomy | **20/20 (100%)** |
| College CS | **20/20 (100%)** |
| College Physics | 19/20 (95%) |
| HS Biology | 19/20 (95%) |
| HS Chemistry | **20/20 (100%)** |
| HS Mathematics | 18/20 (90%) |
| Logical Fallacies | 19/20 (95%) |
| World Religions | **20/20 (100%)** |
| **Total** | **188/200 (94.0%)** |

**Five perfect 100% subjects.** 119B intelligence in 30 GB at 82 tok/s.

## Requirements

- **[MLX Studio](https://mlx.studio)** for native JANG support with reasoning
- Or: - Apple Silicon Mac with 48+ GB unified memory

## Install

\
---

*Created by [Jinho Jang](mailto:eric@jangq.ai) — [jangq.ai](https://jangq.ai) — [@dealignai](https://x.com/dealignai)*
