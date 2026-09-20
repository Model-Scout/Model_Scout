---
language:
- en
- zh
- ko
library_name: mlx
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
tags:
- jang
- quantized
- mixed-precision
- apple-silicon
- mlx
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

# Qwen 3.5 VL 9B — JANG_4S + CRACK

**JANG mixed-precision** · **CRACK abliterated** · **Vision-Language** · No guardrails · 6 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [Qwen 3.5 VL 9B](https://huggingface.co/Qwen/Qwen3.5-9B) — a 9B parameter dense hybrid SSM/Attention model with built-in vision capabilities.

It has been:
1. **JANG quantized** — JANG_4S profile (6-bit attention, 4-bit MLP) — **6 GB**
2. **CRACK abliterated** — permanent weight-level removal of safety refusal 

| | |
|---|---|
| **Architecture** | Qwen 3.5 VL Dense — 9B params, hybrid SSM/FA, 32 layers |
| **Quantization** | JANG_4S (6/4-bit mixed) — 6 GB |
| **Abliteration** | CRACK — novel weight surgery |
| **HarmBench** | **72.5%** (232/320) |
| **MMLU** | **70.8%** (base: 72.3%, -1.5%) |
| **Speed** | ~80 tok/s (M4 Max) |
| **Vision** | Yes — via [MLX Studio](https://mlx.studio) / vMLX |
| **Thinking** | ON/OFF supported |
| **Fits on** | **16 GB+ Macs** |

---

## JANG vs MLX Uniform Quantization

| Model | MMLU | Size | Notes |
|-------|:---:|:---:|-------|
| **JANG_4S + CRACK** | **70.8%** | **6 GB** | **This model** |
| JANG_4S (base) | 73.0% | 6 GB | Unmodified JANG |
| MLX 4-bit | 72.5% | 4.7 GB | Uniform quant |

---

## HarmBench Results

**232/320 (72.5%)** — tested with `enable_thinking=false`, `temperature=1.0`

| Category | Score | |
|----------|:---:|---|
| Misinformation / Disinfo | 46/54 | **85%** |
| Cybercrime / Intrusion | 41/52 | 79% |
| Chemical / Biological | 31/42 | 74% |
| Harmful | 13/18 | 72% |
| Illegal | 38/53 | 72% |
| Copyright | 53/80 | 66% |
| Harassment / Bullying | 10/21 | 48% |

> **Note:** Dense models have stronger distributed safety training than MoE models. This model prioritizes knowledge preservation over maximum compliance.

---

## MMLU Results

| | CRACK | Base | Delta |
|---|:---:|:---:|:---:|
| **Total** | **46/65 (70.8%)** | **47/65 (72.3%)** | **-1.5%** |

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("dealignai/Qwen3.5-VL-9B-JANG_4S-CRACK")

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

> **Tip:** Use `temperature=1.0` for chat. Use `temperature=0.0` for structured tasks like MMLU.

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon — the GGUF equivalent for MLX.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) removes safety alignment from LLMs at the weight level using per-layer projected vectors from 512 structurally-mirrored prompt pairs.

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

### Qwen 3.5 VL 9B — JANG_4S + CRACK

| 항목 | 내용 |
|------|------|
| 크기 | 6 GB |
| HarmBench | 72.5% (232/320) |
| MMLU | 70.8% (기본 72.3% 대비 -1.5%) |
| 비전 | 지원 (MLX Studio / vMLX) |
| 최소 요구사양 | 16 GB 메모리 Mac |

```bash
pip install "jang[mlx]"
```

[GitHub](https://github.com/jjang-ai/jangq) · [HuggingFace](https://huggingface.co/JANGQ-AI) · [MLX Studio](https://mlx.studio) · [Ko-fi](https://ko-fi.com/jangq) · [X @dealignai](https://x.com/dealignai)

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a> · 장진호 제작</p>
