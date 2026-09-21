---
language:
- en
- zh
- ja
- ko
library_name: mlx
license: apache-2.0
base_model: MiniMaxAI/MiniMax-M2.5
tags:
- jang
- quantized
- mixed-precision
- apple-silicon
- mlx
- reasoning
- thinking
- moe
pipeline_tag: text-generation
---

<p align="center">
  <a href="https://mlx.studio"><img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/mlx-studio-light.png" alt="MLX Studio" width="500"></a>
</p>

<h4 align="center"><a href="https://mlx.studio">MLX Studio</a> — native JANG support with reasoning</h4>

---

<p align="center">
  <img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/jangq-logo-dark.png" alt="JANG" width="300">
</p>

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

<h3 align="center">MiniMax M2.5 (227B-A21B) — JANG_3L (3.08-bit) — Reasoning</h3>
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

## Results: 93.5% MMLU (200 Questions, Smart Two-Pass)

| Subject | Score |
|---------|:-----:|
| Abstract Algebra | 11/20 (55%) |
| Anatomy | 19/20 (95%) |
| Astronomy | **20/20 (100%)** |
| College CS | **20/20 (100%)** |
| College Physics | 19/20 (95%) |
| HS Biology | **20/20 (100%)** |
| HS Chemistry | 19/20 (95%) |
| HS Mathematics | **20/20 (100%)** |
| Logical Fallacies | 19/20 (95%) |
| World Religions | **20/20 (100%)** |
| **Total** | **187/200 (93.5%)** |

Pass 1 (no-thinking): 158/200 (79.0%) | Pass 2 (reasoning retry): +29 recovered

## JANG vs MLX — MiniMax M2.5

| Model | MMLU | Size | Speed | Notes |
|-------|:----:|:----:|:-----:|-------|
| **JANG_3L (this model)** | **93.5%** | **82 GB** | **41 tok/s** | 5 subjects at 100% |
| **JANG_2L** | **74.0%** | **63 GB** | 48 tok/s | Smallest working MiniMax |
| MLX 4-bit | 26.5% | 91 GB | ~50 tok/s | **Broken** — random answers |
| MLX 3-bit | 24.5% | 69 GB | — | **Broken** — random answers |
| MLX 2-bit | 25.0% | 46 GB | — | **Broken** — random answers |

**MLX is broken on MiniMax at ALL bit levels** (~25% = random chance). JANG is the ONLY working quantization for MiniMax M2.5 on Apple Silicon.

## Key Features

- **93.5% MMLU** — five subjects at 100%
- **41 tok/s** generation on M3 Ultra
- **82 GB** on disk — fits 96+ GB Macs
- **227B total / 21B active** — 256 MoE experts, top-8 routing
- **Reasoning mode**: `<think>...</think>` step-by-step reasoning
- **Sigmoid + bias routing**: MiniMax-specific MoE (not softmax)
- **FP8 source** with block-wise 128x128 scales

## Important Notes

- **Temperature must be 1.0** — greedy decoding (temp=0) causes infinite thinking loops on MiniMax
- **Tokenizer**: Known-good tokenizer included (mlx_lm.convert corrupts MiniMax tokenizer)

## Architecture

```
227B total parameters, 21B active per token
- 64 layers, all MoE (256 experts, top-8 routing)
- Sigmoid + bias expert routing (non-normalized)
- GQA attention: 48 heads, 8 KV heads
- FP8 E4M3 source with block-wise scales
```

## Install

```bash
pip install jang[mlx]
```

---

*Created by [Jinho Jang](mailto:eric@jangq.ai) — [jangq.ai](https://jangq.ai) — [@dealignai](https://x.com/dealignai)*
