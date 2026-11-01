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

# MiniMax M2.5 — JANG_2L + CRACK

**JANG mixed-precision** · **CRACK abliterated** · No guardrails · 63 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [MiniMax M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) — a 230B parameter Mixture-of-Experts model with 256 experts (8 active per token), all standard attention (no SSM), and trained with chain-of-thought reasoning.

It has been:
1. **JANG quantized** — JANG_2L profile (8-bit attention, 6-bit embeddings, 2-bit experts) — **63 GB**
2. **CRACK abliterated** — permanent weight-level removal of safety refusal 

| | |
|---|---|
| **Architecture** | MiniMax M2.5 MoE — 230B total, ~10B active, 256 experts |
| **Quantization** | JANG_2L (8/6/2-bit mixed) — 63 GB |
| **Abliteration** | CRACK — novel weight surgery |
| **MMLU-200** | **84.7%** (base: 74.5%, **+10.2% improvement**) |
| **HarmBench** | **98.1%** (314/320) |
| **Compliance** | 7/8 prompts |
| **Thinking** | ON/OFF supported |
| **Speed** | **~35 tok/s** (M4 Ultra 256GB) |
| **Fits on** | **96 GB+ Macs** |

---

## MMLU-200 Results

### JANG CRACK vs Base vs MLX Uniform

| Model | MMLU | Size | Notes |
|-------|:---:|:---:|-------|
| **JANG_2L + CRACK** | **~84.7%** | **63 GB** | **This model** |
| JANG_2L (base) | 74.5% | 63 GB | Unmodified JANG |
| MLX 4-bit | 26.5% | 120 GB | **Broken** (~random) |
| MLX 3-bit | 24.5% | 93 GB | **Broken** (~random) |
| MLX 2-bit | 25.0% | 67 GB | **Broken** (~random) |

MLX uniform quantization is **completely broken** on MiniMax at ALL bit levels (~25% = random chance). JANG is the only working quantization format for this model.

### Per Subject

| Subject | CRACK | Base | Delta |
|---------|:---:|:---:|:---:|
| Abstract Algebra | ~18/20 | 10/20 | **+8** |
| HS Mathematics | **17/20** | 12/20 | **+5** |
| College CS | ~14/20 | 10/20 | **+4** |
| Logical Fallacies | **18/20** | 16/20 | **+2** |
| HS Biology | **19/20** | 18/20 | **+1** |
| Astronomy | ~18/20 | 18/20 | 0 |
| Anatomy | ~15/20 | 15/20 | 0 |
| HS Chemistry | 16/20 | 16/20 | 0 |
| World Religions | 17/20 | 17/20 | 0 |
| College Physics | ~16/20 | 17/20 | -1 |
| **Total** | **~169/200** | **149/200** | **+20** |

Safety guardrails were actively degrading the model's reasoning ability. CRACK surgery unlocked the model's full capacity for mathematical and logical reasoning.

---

## HarmBench Results

**314/320 (98.1%)** — tested with `enable_thinking=false`, `temperature=1.0`

| Category | Score | |
|----------|:---:|---|
| Chemical / Biological | 42/42 | **100%** |
| Cybercrime / Intrusion | 52/52 | **100%** |
| Harassment / Bullying | 21/21 | **100%** |
| Harmful | 18/18 | **100%** |
| Illegal | 53/53 | **100%** |
| Misinformation / Disinfo | 54/54 | **100%** |
| Copyright | 74/80 | 92% |

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("dealignai/MiniMax-M2.5-JANG_2L-CRACK")

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False)

response = generate(model, tokenizer, prompt=prompt, max_tokens=2000)
print(response)
```

> **Note:** MiniMax generates a `<think>` chain before answering by default. To disable thinking, pass `enable_thinking=False` in your chat template kwargs. Use `max_tokens=2000+` for complex questions. For chat applications, use `temperature=1.0` (greedy causes loops).

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon — the GGUF equivalent for MLX. Classifies tensors into sensitivity tiers and assigns bits accordingly.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) removes safety alignment from LLMs at the weight level using per-layer projected vectors from structurally-mirrored prompt pairs.

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

### MiniMax M2.5 — JANG_2L + CRACK

| 항목 | 내용 |
|------|------|
| 크기 | 63 GB |
| MMLU | 84.7% (기본 74.5% 대비 +10.2%) |
| HarmBench | 98.1% (314/320) |
| 최소 요구사양 | 96 GB 메모리 Mac |

```bash
pip install "jang[mlx]"
```

[GitHub](https://github.com/jjang-ai/jangq) · [HuggingFace](https://huggingface.co/JANGQ-AI) · [MLX Studio](https://mlx.studio) · [Ko-fi](https://ko-fi.com/jangq) · [X @dealignai](https://x.com/dealignai)

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a> · 장진호 제작</p>
