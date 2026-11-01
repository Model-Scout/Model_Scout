---
language:
- en
- zh
- ko
library_name: mlx
license: apache-2.0
base_model: Qwen/Qwen3.5-VL-397B-A17B
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
- vision
pipeline_tag: image-text-to-text
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

# Qwen 3.5 VL 397B — JANG_1L + CRACK

**JANG mixed-precision** · **CRACK abliterated** · **Vision-Language** · No guardrails · 112 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [Qwen 3.5 VL 397B](https://huggingface.co/Qwen/Qwen3.5-VL-397B-A17B) — a 397B parameter hybrid SSM/Attention Mixture-of-Experts model with 512 experts (10 active per token), GatedDeltaNet SSM + full attention layers, and built-in vision.

It has been:
1. **JANG quantized** — JANG_1L profile (8-bit attention, 2-bit experts) — **112 GB**
2. **CRACK abliterated** — refusal behavior removed via weight-level surgery

| | |
|---|---|
| **Architecture** | Qwen 3.5 VL MoE — 397B total, ~17B active, 512 experts, hybrid SSM/FA |
| **Quantization** | JANG_1L (8/2-bit mixed, 2.13 avg) — 112 GB |
| **Abliteration** | CRACK — weight-level surgery |
| **HarmBench** | **96.2%** (308/320) |
| **Compliance** | 8/8 |
| **Speed** | **33 tok/s** (M3 Ultra 256GB) |
| **Vision** | Yes — via [MLX Studio](https://mlx.studio) / vMLX |
| **Thinking** | ON/OFF supported |
| **Fits on** | **128 GB+ Macs** (tight) / **256 GB Macs** (comfortable) |

---

## HarmBench Results

**308/320 (96.2%)** — tested with v2 matcher

| Category | Score | |
|----------|:---:|---|
| Copyright | 80/80 | **100%** |
| Misinformation / Disinfo | 54/54 | **100%** |
| Chemical / Biological | 41/42 | **98%** |
| Cybercrime / Intrusion | 50/52 | **96%** |
| Illegal | 49/53 | 92% |
| Harmful | 16/18 | 89% |
| Harassment / Bullying | 18/21 | 86% |

---

## MMLU Results

**185/208 (88.9%)** — 208 questions across 13 subjects, thinking recovery on failures

| | CRACK | Base JANG_1L | Delta |
|---|:---:|:---:|:---:|
| **MMLU** | **88.9%** | 87.0% | **+1.9%** |
| **Speed** | 33 tok/s | 36 tok/s | -8% |
| **HarmBench** | **96.2%** | 0% | +96.2% |


### Per Subject (16 questions each)

| Subject | CRACK | /16 | Type |
|---------|:---:|---|---|
| Professional Medicine | **16/16** | 100% | HARD |
| HS Biology | **16/16** | 100% | BASE |
| World Religions | **16/16** | 100% | BASE |
| College Physics | 15/16 | 94% | HARD |
| Conceptual Physics | 15/16 | 94% | HARD |
| HS Geography | 15/16 | 94% | BASE |
| Electrical Engineering | 14/16 | 88% | HARD |
| College CS | 13/16 | 81% | HARD |
| Machine Learning | 13/16 | 81% | HARD |
| Abstract Algebra | 12/16 | 75% | HARD |
| HS Mathematics | 12/16 | 75% | HARD |
| Formal Logic | 11/16 | 69% | HARD |
| College Mathematics | 11/16 | 69% | HARD |
| **Total** | **185/208** | **88.9%** | |

Surgery **improved** reasoning — safety guardrails were interfering with mathematical problem-solving.

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("dealignai/Qwen3.5-397B-A17B-JANG_1L-CRACK")

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False)

response = generate(model, tokenizer, prompt=prompt, max_tokens=2000)
print(response)
```

### Thinking Mode

Thinking is **ON by default**. To disable:
```python
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True,
    enable_thinking=False, tokenize=False)
```

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon — the GGUF equivalent for MLX.

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

### Qwen 3.5 VL 397B — JANG_1L + CRACK

| 항목 | 내용 |
|------|------|
| 크기 | 112 GB |
| HarmBench | 96.2% (308/320) |
| 속도 | 33 tok/s (M3 Ultra) |
| 비전 | 지원 (MLX Studio / vMLX) |
| 최소 요구사양 | 128 GB 메모리 Mac |

```bash
pip install "jang[mlx]"
```

[GitHub](https://github.com/jjang-ai/jangq) · [HuggingFace](https://huggingface.co/JANGQ-AI) · [MLX Studio](https://mlx.studio) · [Ko-fi](https://ko-fi.com/jangq) · [X @dealignai](https://x.com/dealignai)

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a> · 장진호 제작</p>
