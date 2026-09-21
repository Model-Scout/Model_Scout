---
language:
- en
- zh
- ko
library_name: mlx
license: apache-2.0
base_model: Qwen/Qwen3.5-397B-A17B
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
pipeline_tag: text-generation
---

<p align="center">
  <a href="https://mlx.studio"><img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/mlx-studio-light.png" alt="MLX Studio" width="500"></a>
</p>

<p align="center">
  <a href="https://mlx.studio"><img src="https://mlx.studio/assets/screenshots/mlx-studio-featured.png?v=1" alt="MLX Studio App" width="600"></a>
</p>

<h4 align="center"><a href="https://mlx.studio">MLX Studio</a> — the only app that natively supports JANG models with reasoning</h4>

---

> **This model uses reasoning/thinking mode.** The model reasons inside `<think>...</think>` tags before answering. This dramatically improves accuracy on hard questions (abstract algebra: 50% → 80%, math: 50% → 85%). **[MLX Studio](https://mlx.studio)** is required to run this model — it handles JANG format, bfloat16 compute, and thinking mode natively.

> **LM Studio, Ollama, oMLX, Inferencer do NOT support JANG format.** Use **[MLX Studio](https://mlx.studio)** or `pip install "jang[mlx]"`.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/jangq-logo-dark.png" alt="JANG" width="300">
</p>

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

<h3 align="center">Qwen3.5-397B-A17B — JANG_2L (3.7-bit, 8-bit attention) — Reasoning + VLM</h3>
<p align="center"><b>JANG</b> — Jang Adaptive N-bit Grading | The GGUF Equivalent for MLX</p>

---

<p align="center">
  <a href="https://github.com/jjang-ai/jangq"><img src="https://img.shields.io/badge/GitHub-Source_Code-blue?logo=github" alt="GitHub"></a>&nbsp;
  <a href="https://pypi.org/project/jang/"><img src="https://img.shields.io/pypi/v/jang?label=PyPI&color=green" alt="PyPI"></a>&nbsp;
  <a href="https://jangq.ai"><img src="https://img.shields.io/badge/Web-jangq.ai-orange" alt="Website"></a>&nbsp;
  <a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/X-@dealignai-black?logo=x" alt="X/Twitter"></a>
</p>

> **JANG is fully open-source.** Quantization engine, research, and full commit history: [github.com/jjang-ai/jangq](https://github.com/jjang-ai/jangq). Created by [Jinho Jang](mailto:eric@jangq.ai).


## Key Features

- **92.0% MMLU** (200 questions, reasoning mode) — 397B intelligence on Apple Silicon
- **36 tok/s** generation speed on M4 Ultra 256 GB
- **Reasoning mode**: `<think>...</think>` for step-by-step problem solving
- **Vision (VLM)**: 333 vision tensors, processes images and video
- **187 GB** on disk, 197 GB peak GPU RAM
- **bfloat16 compute**: auto-detected by JANG loader for 512-expert models

## Results: JANG_2L vs MLX 4-bit (200-question MMLU)

Per-subject comparison across all modes. Both JANG and MLX 4-bit tested with and without reasoning.

| Subject | JANG No-Think | JANG Reasoning | MLX 4-bit No-Think | MLX 4-bit Reasoning |
|---------|:------------:|:--------------:|:------------------:|:-------------------:|
| Abstract Algebra | 10/20 | 16/20 | 10/20 | 17/20 |
| Anatomy | 17/20 | 19/20 | 18/20 | 19/20 |
| Astronomy | 19/20 | 19/20 | 19/20 | 19/20 |
| College CS | 18/20 | 19/20 | 15/20 | 18/20 |
| College Physics | 14/20 | 18/20 | 15/20 | 19/20 |
| HS Biology | 18/20 | 19/20 | 19/20 | 19/20 |
| HS Chemistry | 16/20 | 18/20 | 17/20 | 19/20 |
| HS Mathematics | 10/20 | 17/20 | 12/20 | 19/20 |
| Logical Fallacies | 19/20 | 20/20 | 19/20 | 20/20 |
| World Religions | 18/20 | 19/20 | 19/20 | 19/20 |
| **Total** | **159/200 (79.5%)** | **184/200 (92.0%)** | **163/200 (81.5%)** | **188/200 (94.0%)** |

### Summary

| | JANG_2L | JANG_1L | MLX 4-bit | MLX 2/3-bit |
|--|---------|---------|-----------|-------------|
| **MMLU (no-think)** | 79.5% | 81.0% | 81.5% | NaN -- cannot run |
| **MMLU (reasoning)** | **92.0%** | 86.5% | **94.0%** | NaN -- cannot run |
| **Size** | **187 GB** | 112 GB | 209 GB | N/A |
| **GPU RAM** | 184 GB | 110 GB | ~210 GB | N/A |
| **Speed** | **36.0 tok/s** | 36.1 tok/s | ~36 tok/s | N/A |
| **Fits 128 GB?** | No (256 GB) | YES | No | N/A |

JANG_2L is **22 GB smaller** than MLX 4-bit. MLX 4-bit with reasoning reaches 94.0%, while JANG_2L reaches 92.0% at significantly smaller size.
MLX 2-bit and 3-bit produce NaN -- cannot run (float16 overflow on 512-expert models). JANG solves this with bfloat16.

## Specs

| Metric | Value |
|--------|-------|
| Source | [Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) |
| Architecture | Hybrid MoE + SSM (GatedDeltaNet + Full Attention) |
| Experts | 512 per layer, top-10 active (17B active params) |
| Layers | 60 (45 GatedDeltaNet SSM + 15 Full Attention) |
| Profile | JANG_2L (CRITICAL=8, IMPORTANT=6, COMPRESS=2) |
| MLP Asymmetry | gate_proj=4-bit, up_proj=2-bit, down_proj=3-bit |
| Average bits | 3.72 bpw |
| Disk size | 187 GB (43 shards) |
| GPU RAM | 197 GB peak |
| Generation speed | **36.0 tok/s** (M4 Ultra 256 GB) |
| Prefill speed | 94.5 tok/s |
| Compute dtype | bfloat16 (auto-detected, prevents float16 overflow) |
| VLM | 333 vision tensors, Qwen3VLProcessor |

## Requirements

- **Apple Silicon Mac** with 256 GB unified memory (M3/M4 Ultra)
- **[MLX Studio](https://mlx.studio)** (recommended) or `pip install "jang[mlx]>=2.1.5"`
- Python 3.11+ for CLI usage

## Quick Start (Python)

```bash
pip install "jang[mlx]>=2.1.5"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("JANGQ-AI/Qwen3.5-397B-A17B-JANG_2L")
# bfloat16 is auto-applied for 512-expert models

# With reasoning (recommended for hard questions)
messages = [{"role": "user", "content": "Prove that sqrt(2) is irrational."}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
    add_generation_prompt=True, enable_thinking=True)
result = generate(model, tokenizer, prompt=prompt, max_tokens=2048)

# Without reasoning (faster for simple questions)
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
    add_generation_prompt=True, enable_thinking=False)
result = generate(model, tokenizer, prompt=prompt, max_tokens=100)
```

## VLM Usage

```python
from jang_tools.loader import load_jang_vlm_model
from mlx_vlm import generate as vlm_generate

model, processor = load_jang_vlm_model("JANGQ-AI/Qwen3.5-397B-A17B-JANG_2L")

# Format prompt with image tokens
messages = [{"role": "user", "content": [
    {"type": "image"},
    {"type": "text", "text": "Describe this image."},
]}]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
result = vlm_generate(model, processor, prompt=prompt, image=["photo.jpg"], max_tokens=200)
```

## What is JANG?

JANG (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon that classifies every weight tensor by sensitivity:

- **CRITICAL** (8-bit): Full attention Q/K/V/O, MoE routers, output head
- **IMPORTANT** (6-bit): Embeddings, GatedDeltaNet (linear attention)
- **COMPRESS** (2-bit): MoE expert MLP (512 experts provide redundancy)
- **MLP Asymmetry**: gate_proj=4-bit (SiLU amplifier), down_proj=3-bit (residual projection)

This gives 397B-level intelligence at 187 GB — fitting on a single M4 Ultra Mac Studio.


## Technical Notes

- **bfloat16 compute**: 512-expert models with hidden_size=4096 overflow float16 (max 65,504) at the shared expert down_proj. The JANG loader auto-detects this and uses bfloat16 (max 3.4×10^38). Zero quality impact — quantization noise dominates.
- **Reasoning mode**: The model uses `<think>...</think>` tags for step-by-step reasoning. On hard questions (math, physics, algebra), this improves accuracy by 25+ percentage points.
- **Chat template**: Includes `enable_thinking` toggle. Set to `False` for fast answers, `True` for reasoning.

---

<p align="center">
  <b>JANG</b> — Created by <a href="https://jangq.ai">Jinho Jang</a> (eric@jangq.ai) · <a href="https://x.com/dealignai">@dealignai</a><br>
  <a href="https://github.com/jjang-ai/jangq">GitHub</a> · <a href="https://pypi.org/project/jang/">PyPI</a> · <a href="https://huggingface.co/JANGQ-AI">HuggingFace</a>
</p>

## 한국어 안내

JANG은 Apple Silicon을 위한 혼합 정밀도 양자화 형식입니다. Qwen3.5-397B를 Mac Studio 한 대에서 36 tok/s로 실행할 수 있습니다.

- **92.0% MMLU** (추론 모드)
- **187 GB** 디스크 용량, M4 Ultra 256 GB에서 실행
- **[MLX Studio](https://mlx.studio)** 필요

```bash
pip install "jang[mlx]>=2.1.5"
```
