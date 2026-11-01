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

<h3 align="center">Mistral Small 4 (119B-A6B) — JANG_4M (4.08-bit) — Reasoning + VLM</h3>
<p align="center"><b>JANG</b> — Jang Adaptive N-bit Grading | The GGUF Equivalent for MLX</p>

<p align="center">
  <a href="https://github.com/jjang-ai/jangq"><img src="https://img.shields.io/badge/GitHub-Source_Code-blue?logo=github" alt="GitHub"></a>&nbsp;
  <a href="https://pypi.org/project/jang/"><img src="https://img.shields.io/pypi/v/jang?label=PyPI&color=green" alt="PyPI"></a>&nbsp;
  <a href="https://jangq.ai"><img src="https://img.shields.io/badge/Web-jangq.ai-orange" alt="Website"></a>&nbsp;
  <a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/X-@dealignai-black?logo=x" alt="X/Twitter"></a>
</p>

> **JANG is fully open-source.** Quantization engine and full commit history: [github.com/jjang-ai/jangq](https://github.com/jjang-ai/jangq). Created by [Jinho Jang](mailto:eric@jangq.ai).

---

> **Supported apps:** [MLX Studio](https://mlx.studio) (full native support) and [oMLX](https://github.com/jundot/omlx) ([PR #364](https://github.com/jundot/omlx/pull/364)). LM Studio, Ollama, and Inferencer do not yet support JANG.

---

### Why JANG models?

Tools like mlx-lm, oMLX (oQ), and others can quantize models — but shipping a tool is the easy part. JANG models come from hundreds of hours of per-architecture testing: finding which layers break at which bit depths, which MoE routing survives quantization, which models need bfloat16 to avoid NaN. We don't just quantize — we convert, verify, benchmark, and publish every model with tested scores. No other project in the MLX ecosystem publishes pre-tested quantized models at this scale.

---

## Speed Comparison

| Model | Size | Gen tok/s | Prefill tok/s | RAM | Fits On |
|-------|:----:|:---------:|:-------------:|:---:|---------|
| **JANG_4M (this model)** | **57 GB** | **80** | **202** | **68 GB** | **96+ GB Macs** |
| JANG_2L | 30 GB | 82 | 216 | 40 GB | 48 GB Macs |
| JANG_4M | 57 GB | 80 | 202 | 68 GB | 96+ GB Macs |
| JANG_6M | 84 GB | 74 | 160 | 95 GB | 128+ GB Macs |
| MLX Community 4-bit | 63 GB | 84 | 43 | 68 GB | 96+ GB Macs |

**5x faster prefill** than MLX Community (216 vs 43 tok/s). JANG_2L runs on 48 GB Macs at half the size.

Benchmarked on M3 Ultra 256 GB with bfloat16 compute.

## Key Features

- **80 tok/s** generation on M3 Ultra
- **57 GB** on disk, **68 GB** peak RAM
- **Vision (VLM)**: Pixtral encoder, 1540px max
- **Reasoning mode**: [THINK]...[/THINK] step-by-step reasoning
- **Code generation**: Complete functions with optimized logic
- **Math**: Step-by-step calculations
- **119B total / 6B active** — MLA attention + 128 MoE experts
- **First Mistral Small 4 on Apple Silicon** with full MLA + MoE support

## Architecture

```
119B total parameters, 6B active per token
- 36 layers, all MoE (128 experts, top-4 routing)
- MLA attention: kv_lora_rank=256, q_lora_rank=1024
- Pixtral vision: 24 layers, 1540px max
- Reasoning: [THINK]...[/THINK] with reasoning_effort control
- bfloat16 compute (auto-detected)
```

## Benchmarks

*MMLU benchmarks in progress — will be updated with per-subject scores and MLX 4-bit comparison.*

## Install

```bash
pip install jang[mlx]
```

---

*Created by [Jinho Jang](mailto:eric@jangq.ai) — [jangq.ai](https://jangq.ai) — [@dealignai](https://x.com/dealignai)*
