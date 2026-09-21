---
language:
- en
- zh
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
- moe
- abliterated
- uncensored
- crack
pipeline_tag: text-generation
thumbnail: dealign_mascot.png
---

> **Important:** This model uses the **JANG** quantization format — the GGUF equivalent for MLX on Apple Silicon. Currently only supported by **[MLX Studio](https://mlx.studio)** and the `jang-tools` Python package.

---

<p align="center">
  <a href="https://mlx.studio"><img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/mlx-studio-light.png" alt="MLX Studio" width="500"></a>
</p>

<p align="center">
  <a href="https://mlx.studio"><img src="https://mlx.studio/assets/screenshots/mlx-studio-featured.png?v=1" alt="MLX Studio App" width="600"></a>
</p>

<h4 align="center"><a href="https://mlx.studio">MLX Studio</a> — the only app that natively supports JANG models</h4>

---

<div align="center">

<img src="dealign_mascot.png" width="128" />

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

# MiniMax M2.5 — JANG_3L + CRACK

**JANG mixed-precision** · **CRACK abliterated** · No guardrails · 89 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [MiniMax M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) — a 230B parameter Mixture-of-Experts model with 256 experts (8 active per token), all standard attention (no SSM), and trained with chain-of-thought reasoning.

It has been:
1. **JANG quantized** — JANG_3L profile (8-bit attention, 4-bit important, 3-bit experts) — **89 GB**
2. **CRACK abliterated** — permanent weight-level removal of safety refusal

| | |
|---|---|
| **Architecture** | MiniMax M2.5 MoE — 230B total, ~10B active, 256 experts |
| **Quantization** | JANG_3L (8/4/3-bit mixed, 3.08 avg) — 89 GB |
| **Abliteration** | CRACK abliterated |
| **MMLU-208** | **91.8%** (4 subjects at 100%) |
| **Compliance** | 8/8 prompts |
| **Speed** | ~46 tok/s (M4 Ultra 256 GB) |
| **Fits on** | **128 GB+ Macs** |

---

## MMLU-208 Results (Per Subject)

| Subject | Score |
|---------|:---:|
| College Physics | **16/16 (100%)** |
| Conceptual Physics | **16/16 (100%)** |
| Professional Medicine | **16/16 (100%)** |
| High School Biology | **16/16 (100%)** |
| Abstract Algebra | 15/16 (94%) |
| College Mathematics | 15/16 (94%) |
| High School Geography | 15/16 (94%) |
| World Religions | 15/16 (94%) |
| College Computer Science | 14/16 (88%) |
| Machine Learning | 14/16 (88%) |
| Electrical Engineering | 13/16 (81%) |
| Formal Logic | 13/16 (81%) |
| High School Mathematics | 13/16 (81%) |
| **Total** | **191/208 (91.8%)** |

CRACK surgery with proper probe vectors actually **improves** reasoning on MiniMax. Safety guardrails were constraining the model's full reasoning capacity.

---

## vs JANG_2L CRACK

| | JANG_2L | **JANG_3L** |
|---|:---:|:---:|
| Avg bits | 2.1 | **3.08** |
| Size | 63 GB | **89 GB** |
| MMLU | 84.7% | **91.8%** |
| Compliance | 7/8 | **8/8** |
| Fits on | 96 GB Mac | 128 GB Mac |

Higher precision quantization = better reasoning AND compliance.

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools import load_for_inference
from mlx_lm import generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load_for_inference("dealignai/MiniMax-M2.5-JANG_3L-CRACK")
sampler = make_sampler(temp=1.0)  # MiniMax requires temp=1.0 for chat

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False)

response = generate(model, tokenizer, prompt=prompt, max_tokens=2000, sampler=sampler)
print(response)
```

### Disable Thinking (direct answers)
```python
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False,
    enable_thinking=False)
```

> **Note:** MiniMax generates a `<think>` chain before answering by default. Use `max_tokens=2000+` for complex questions. For chat, use `temperature=1.0` (greedy causes loops).

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon — the GGUF equivalent for MLX. Classifies tensors into sensitivity tiers and assigns bits accordingly.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) removes safety alignment from LLMs at the weight level. This model has been abliterated using proprietary techniques achieving full compliance while preserving reasoning quality.

---

## Links

<p align="center">

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=flat-square" alt="Ko-fi"></a>
<a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/X-@dealignai-000000?logo=x&logoColor=white&style=flat-square" alt="X/Twitter"></a>
<a href="https://github.com/jjang-ai/jangq"><img src="https://img.shields.io/badge/GitHub-jjang--ai/jangq-181717?logo=github&logoColor=white&style=flat-square" alt="GitHub"></a>
<a href="https://mlx.studio"><img src="https://img.shields.io/badge/MLX_Studio-App-blue?style=flat-square" alt="MLX Studio"></a>
<a href="https://jangq.ai"><img src="https://img.shields.io/badge/Website-jangq.ai-green?style=flat-square" alt="Website"></a>

</p>

---

## Disclaimer

This model is provided for research and educational purposes. The creators are not responsible for any misuse. By downloading this model, you agree to use it responsibly and in compliance with applicable laws.

---

## 한국어

### MiniMax M2.5 — JANG_3L + CRACK

| 항목 | 내용 |
|------|------|
| 크기 | 89 GB |
| MMLU | 91.8% (4과목 100%) |
| 최소 요구사양 | 128 GB 메모리 Mac |

```bash
pip install "jang[mlx]"
```

[GitHub](https://github.com/jjang-ai/jangq) · [HuggingFace](https://huggingface.co/JANGQ-AI) · [MLX Studio](https://mlx.studio) · [Ko-fi](https://ko-fi.com/jangq) · [X @dealignai](https://x.com/dealignai)

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a> · 장진호 제작</p>
