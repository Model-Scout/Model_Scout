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

> **397B intelligence on a 128 GB Mac.** This model fits in 112 GB — the first 397B quantization that runs on M4 Pro/Max 128 GB machines. Uses reasoning mode for 86.5% MMLU accuracy.

> **LM Studio, Ollama, oMLX do NOT support JANG format.** Use **[MLX Studio](https://mlx.studio)** or `pip install "jang[mlx]>=2.1.5"`.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/jangq-logo-dark.png" alt="JANG" width="300">
</p>

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

<h3 align="center">Qwen3.5-397B-A17B — JANG_1L (2.1-bit, 8-bit attention) — Reasoning + VLM</h3>
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

- **86.5% MMLU** (200 questions, reasoning mode) — 397B on 128 GB Macs
- **36.1 tok/s** generation, 96 tok/s prefill
- **112 GB** on disk, 110 GB GPU RAM (peak 120 GB)
- **Reasoning mode**: `<think>...</think>` step-by-step problem solving
- **Vision (VLM)**: 333 vision tensors, 31.6 tok/s image processing
- **bfloat16 compute**: auto-detected for 512-expert models

## Results: JANG_1L vs MLX 4-bit (200-question MMLU)

Per-subject comparison across all modes. Both JANG and MLX 4-bit tested with and without reasoning.

| Subject | JANG No-Think | JANG Reasoning | MLX 4-bit No-Think | MLX 4-bit Reasoning |
|---------|:------------:|:--------------:|:------------------:|:-------------------:|
| Abstract Algebra | 8/20 | 10/20 | 10/20 | 17/20 |
| Anatomy | 17/20 | 19/20 | 18/20 | 19/20 |
| Astronomy | 20/20 | 20/20 | 19/20 | 19/20 |
| College CS | 17/20 | 18/20 | 15/20 | 18/20 |
| College Physics | 17/20 | 18/20 | 15/20 | 19/20 |
| HS Biology | 19/20 | 20/20 | 19/20 | 19/20 |
| HS Chemistry | 17/20 | 18/20 | 17/20 | 19/20 |
| HS Mathematics | 8/20 | 10/20 | 12/20 | 19/20 |
| Logical Fallacies | 20/20 | 20/20 | 19/20 | 20/20 |
| World Religions | 19/20 | 20/20 | 19/20 | 19/20 |
| **Total** | **162/200 (81.0%)** | **173/200 (86.5%)** | **163/200 (81.5%)** | **188/200 (94.0%)** |

### Summary

| | JANG_1L | JANG_2L | MLX 4-bit | MLX 2/3-bit |
|--|---------|---------|-----------|-------------|
| **MMLU (no-think)** | 81.0% | 79.5% | 81.5% | NaN -- cannot run |
| **MMLU (reasoning)** | **86.5%** | **92.0%** | **94.0%** | NaN -- cannot run |
| **Size** | **112 GB** | 187 GB | 209 GB | N/A |
| **GPU RAM** | **110 GB** | 184 GB | ~210 GB | N/A |
| **Speed** | **36.1 tok/s** | 36.0 tok/s | ~36 tok/s | N/A |
| **Fits 128 GB?** | **YES** | No | No | N/A |

JANG_1L is **97 GB smaller** than MLX 4-bit and fits on 128 GB Macs where MLX 4-bit (209 GB) cannot run.
MLX 2-bit and 3-bit produce NaN -- cannot run (float16 overflow on 512-expert models). JANG solves this with bfloat16.

## Specs

| Metric | Value |
|--------|-------|
| Source | [Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) |
| Architecture | Hybrid MoE + SSM (GatedDeltaNet + Full Attention) |
| Experts | 512 per layer, top-10 active (17B active params) |
| Profile | JANG_1L (CRITICAL=8, IMPORTANT=8, COMPRESS=2) |
| Average bits | 2.13 bpw |
| Disk size | 112 GB |
| GPU RAM | 110 GB (peak 120 GB) |
| Speed | 36.1 tok/s generation, 96 tok/s prefill |
| Compute | bfloat16 (auto-detected) |
| VLM | 333 vision tensors, 31.6 tok/s |

## Requirements

- **Apple Silicon Mac** with 128+ GB unified memory
- **[MLX Studio](https://mlx.studio)** (recommended) or `pip install "jang[mlx]>=2.1.5"`

## Quick Start

```bash
pip install "jang[mlx]>=2.1.5"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("JANGQ-AI/Qwen3.5-397B-A17B-JANG_1L")

# With reasoning
messages = [{"role": "user", "content": "Prove that sqrt(2) is irrational."}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
    add_generation_prompt=True, enable_thinking=True)
result = generate(model, tokenizer, prompt=prompt, max_tokens=2048)

# Without reasoning (faster)
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
    add_generation_prompt=True, enable_thinking=False)
result = generate(model, tokenizer, prompt=prompt, max_tokens=100)
```

## VLM Usage

```python
from jang_tools.loader import load_jang_vlm_model
from mlx_vlm import generate as vlm_generate

model, processor = load_jang_vlm_model("JANGQ-AI/Qwen3.5-397B-A17B-JANG_1L")
messages = [{"role": "user", "content": [
    {"type": "image"},
    {"type": "text", "text": "Describe this image."},
]}]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
result = vlm_generate(model, processor, prompt=prompt, image=["photo.jpg"], max_tokens=200)
```


## Technical Notes

- **bfloat16**: 512-expert models overflow float16 (max 65,504) at the shared expert down_proj. JANG auto-detects and uses bfloat16 (max 3.4x10^38). Zero quality impact.
- **JANG_1L profile**: 8-bit for all attention + routers + embeddings, 2-bit for expert MLP. On MoE models, expert MLP is 97.9% of params — so 2-bit covers almost everything while critical components get maximum precision.

---

<p align="center">
  <b>JANG</b> — Created by <a href="https://jangq.ai">Jinho Jang</a> (eric@jangq.ai) · <a href="https://x.com/dealignai">@dealignai</a><br>
  <a href="https://github.com/jjang-ai/jangq">GitHub</a> · <a href="https://pypi.org/project/jang/">PyPI</a> · <a href="https://huggingface.co/JANGQ-AI">HuggingFace</a>
</p>

## 한국어

JANG_1L은 Qwen3.5-397B를 128 GB Mac에서 실행할 수 있는 최초의 양자화입니다. 112 GB, 36 tok/s, 86.5% MMLU.

```bash
pip install "jang[mlx]>=2.1.5"
```
