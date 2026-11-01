---
language:
- en
- zh
- ko
library_name: mlx
license: other
base_model: nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8
tags:
- jang
- quantized
- mixed-precision
- apple-silicon
- mlx
- reasoning
- thinking
- moe
- mamba
- nemotron
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

> **93% MMLU at same size as MLX 4-bit.** JANG_4M matches MLX 4-bit quality with 8-bit attention protection. Hybrid Mamba-2 SSM + Latent MoE + Attention.

> **LM Studio, Ollama, oMLX do NOT support JANG format.** Use **[MLX Studio](https://mlx.studio)** or \`pip install "jang[mlx]>=2.1.5"\`.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/jangq-logo-dark.png" alt="JANG" width="300">
</p>

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

<h3 align="center">Nemotron-3-Super-120B-A12B — JANG_4M (4.1-bit, 8-bit attention) — Reasoning</h3>
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

- **93.0% MMLU** (200 questions, reasoning mode) — matches MLX 4-bit at same size
- **55.1 tok/s** generation, 154 tok/s prefill
- **63 GB** on disk, 61.2 GB GPU RAM
- **Reasoning mode**: \`<think>...</think>\` step-by-step problem solving
- **Hybrid architecture**: 40 Mamba-2 SSM + 40 Latent MoE (512 experts) + 8 Dense Attention layers
- **bfloat16 compute**: auto-detected for 512-expert models

## Results: JANG vs MLX (200-question MMLU)

Per-subject comparison. All models tested with and without reasoning using identical methodology.

| Subject | JANG_4M No-Think | JANG_4M Reasoning | JANG_2L No-Think | JANG_2L Reasoning | MLX 4-bit No-Think | MLX 4-bit Reasoning |
|---------|:---------------:|:-----------------:|:---------------:|:-----------------:|:------------------:|:-------------------:|
| Abstract Algebra | 10/20 | 19/20 | 12/20 | 16/20 | 9/20 | 19/20 |
| Anatomy | 15/20 | 18/20 | 15/20 | 17/20 | 14/20 | 18/20 |
| Astronomy | 19/20 | 19/20 | 19/20 | 19/20 | 19/20 | 19/20 |
| College CS | 13/20 | 17/20 | 13/20 | 15/20 | 14/20 | 17/20 |
| College Physics | 14/20 | 19/20 | 14/20 | 18/20 | 13/20 | 20/20 |
| HS Biology | 19/20 | 20/20 | 19/20 | 18/20 | 18/20 | 20/20 |
| HS Chemistry | 15/20 | 18/20 | 15/20 | 16/20 | 16/20 | 19/20 |
| HS Mathematics | 6/20 | 18/20 | 8/20 | 18/20 | 6/20 | 18/20 |
| Logical Fallacies | 17/20 | 19/20 | 17/20 | 18/20 | 17/20 | 18/20 |
| World Religions | 17/20 | 19/20 | 18/20 | 17/20 | 16/20 | 19/20 |
| **Total** | **145/200 (72.5%)** | **186/200 (93.0%)** | **150/200 (75.0%)** | **172/200 (86.0%)** | **142/200 (71.0%)** | **187/200 (93.5%)** |

### Summary

| | JANG_4M | JANG_2L | MLX 4-bit | MLX 3-bit |
|--|---------|---------|-----------|-----------|
| **MMLU (no-think)** | 72.5% | **75.0%** | 71.0% | Crashes |
| **MMLU (reasoning)** | **93.0%** | 86.0% | 93.5% | Crashes |
| **Size** | 63 GB | **43 GB** | 63 GB | N/A |
| **GPU RAM** | 61.2 GB | **42.4 GB** | 63.3 GB | N/A |
| **Speed** | 55.1 tok/s | 51.6 tok/s | 59.8 tok/s | N/A |
| **Fits 64 GB?** | YES | **YES** | YES | N/A |

JANG_4M nearly ties MLX 4-bit (93.0% vs 93.5%) at the same 63 GB size with 8-bit attention protection.
MLX 3-bit cannot be created — \`mlx_lm.convert\` crashes on Nemotron's mtp.* weights. Only JANG can produce sub-4-bit quantizations.

Also see: [JANG_2L (43 GB)](https://huggingface.co/JANGQ-AI/Nemotron-3-Super-120B-A12B-JANG_2L) — 20 GB smaller, fits 64 GB Macs, 75% no-think / 86% reasoning.

## Specs

| Metric | Value |
|--------|-------|
| Source | [NVIDIA-Nemotron-3-Super-120B-A12B-FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8) |
| Architecture | Hybrid Mamba-2 SSM + Latent MoE + Dense Attention |
| Layers | 88 (40 Mamba-2 + 40 MoE + 8 Attention) |
| Experts | 512 per MoE layer, top-22 active (12B active params) |
| Profile | JANG_4M (CRITICAL=8, IMPORTANT=4, COMPRESS=4) |
| Average bits | 4.10 bpw |
| Disk size | 63 GB |
| GPU RAM | 61.2 GB (peak 66 GB) |
| Speed | 55.1 tok/s generation, 154 tok/s prefill |
| Compute | bfloat16 (auto-detected) |

## Requirements

- **Apple Silicon Mac** with 64+ GB unified memory
- **[MLX Studio](https://mlx.studio)** or \`pip install "jang[mlx]>=2.1.5"\`

## Quick Start

\`\`\`bash
pip install "jang[mlx]>=2.1.5"
\`\`\`

\`\`\`python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("JANGQ-AI/Nemotron-3-Super-120B-A12B-JANG_4M")

# With reasoning
messages = [{"role": "user", "content": "Explain quantum computing."}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
    add_generation_prompt=True, enable_thinking=True)
result = generate(model, tokenizer, prompt=prompt, max_tokens=2048)

# Without reasoning (faster)
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
    add_generation_prompt=True, enable_thinking=False)
result = generate(model, tokenizer, prompt=prompt, max_tokens=100)
\`\`\`

## Technical Notes

- **Latent MoE**: Nemotron-H compresses hidden states 4096→1024 before expert routing. JANG loader handles this automatically.
- **bfloat16**: Auto-detected for 512-expert models. Prevents float16 overflow. Zero quality impact.
- **trust_remote_code**: Custom Python files included (modeling_nemotron_h.py, configuration_nemotron_h.py).

---

<p align="center">
  <b>JANG</b> — Created by <a href="https://jangq.ai">Jinho Jang</a> (eric@jangq.ai) · <a href="https://x.com/dealignai">@dealignai</a><br>
  <a href="https://github.com/jjang-ai/jangq">GitHub</a> · <a href="https://pypi.org/project/jang/">PyPI</a> · <a href="https://huggingface.co/JANGQ-AI">HuggingFace</a>
</p>

## 한국어

Nemotron-3-Super-120B JANG_4M — MLX 4-bit과 동일한 크기(63 GB)에서 93% MMLU 달성.

| | JANG_4M | JANG_2L | MLX 4-bit |
|--|---------|---------|-----------|
| MMLU (추론 없음) | 72.5% | **75.0%** | 71.0% |
| MMLU (추론 포함) | **93.0%** | 86.0% | 93.5% |
| 크기 | 63 GB | **43 GB** | 63 GB |
| 속도 | 55.1 tok/s | 51.6 tok/s | 59.8 tok/s |

\`\`\`bash
pip install "jang[mlx]>=2.1.5"
\`\`\`
