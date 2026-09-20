---
language:
- en
- zh
- ko
library_name: mlx
license: apache-2.0
base_model: Qwen/Qwen3.5-122B-A10B
tags:
- jang
- quantized
- mixed-precision
- apple-silicon
- mlx
- moe
- vlm
- abliterated
- uncensored
- crack
pipeline_tag: image-text-to-text
thumbnail: dealign_mascot.png
---

> **Important:** This model uses the **JANG** quantization format — the GGUF equivalent for MLX on Apple Silicon. Currently only supported by **[MLX Studio](https://mlx.studio)** and the `jang-tools` Python package. LM Studio, Ollama, and other apps do **not** support JANG yet.

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

# Qwen 3.5 VL 122B-A10B — JANG_4K + CRACK

**JANG K-quant** · **CRACK abliterated** · No guardrails · VLM · 62 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [Qwen 3.5 122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) — a 122B parameter Mixture-of-Experts model with 256 experts (8 active per token), hybrid GatedDeltaNet SSM + full attention architecture, and built-in vision-language capabilities.

It has been:
1. **JANG quantized** — JANG_4K profile (K-quant: 8-bit attention, 4-bit embeddings, 3-bit experts) — **62 GB**
2. **CRACK abliterated** — permanent weight-level removal of safety refusal behavior

JANG_4K is a budget-neutral K-quant: same total size as MLX uniform 4-bit, but with attention weights at 8-bit for maximum coherence. On MoE models where attention is <5% of parameters, this precision boost is nearly free.

| | |
|---|---|
| **Architecture** | Qwen 3.5 MoE — 122B total, 10B active, 256 experts |
| **Quantization** | JANG_4K (8/4/3-bit K-quant) — 62 GB |
| **Abliteration** | CRACK — permanent weight modification |
| **Vision** | Built-in VLM (333 vision encoder tensors) |
| **Thinking** | Supports `enable_thinking` ON/OFF |
| **Speed** | **~45 tok/s** (M4 Ultra 256GB) |
| **Fits on** | **96 GB+ Macs** |

---

## HarmBench Results (320 prompts)

| Category | Score | Rate |
|----------|-------|------|
| Copyright | 78/80 | **98%** |
| Misinformation | 53/54 | **98%** |
| Harmful content | 15/18 | **83%** |
| Harassment & bullying | 17/21 | **81%** |
| Cybercrime & intrusion | 37/52 | **71%** |
| Chemical & biological | 29/42 | **69%** |
| Illegal activities | 22/53 | **42%** |
| **Overall** | **251/320** | **78.4%** |

---

## MMLU-200 Results (Per Subject)

### This Model vs Base Models

| Subject | JANG_4K CRACK | JANG_4K Base | JANG_2S CRACK | MLX 2-bit | MLX 4-bit |
|---------|:---:|:---:|:---:|:---:|:---:|
| | **62 GB** | **69 GB** | **35 GB** | **36 GB** | **64 GB** |
| Abstract Algebra | 12/20 | 16/20 | 12/20 | 9/20 | 15/20 |
| Anatomy | 18/20 | 19/20 | 15/20 | 11/20 | 18/20 |
| Astronomy | 20/20 | 19/20 | 20/20 | 16/20 | 19/20 |
| College CS | 15/20 | 15/20 | 14/20 | 8/20 | 15/20 |
| College Physics | 13/20 | 14/20 | 12/20 | 10/20 | 14/20 |
| HS Biology | 18/20 | 19/20 | 18/20 | 15/20 | 19/20 |
| HS Chemistry | 17/20 | 18/20 | 17/20 | 13/20 | 18/20 |
| HS Mathematics | 12/20 | 14/20 | 11/20 | 4/20 | 14/20 |
| Logical Fallacies | 20/20 | 19/20 | 17/20 | 13/20 | 19/20 |
| World Religions | 18/20 | 19/20 | 19/20 | 14/20 | 19/20 |
| **Total** | **163/200** | **172/200** | **155/200** | **113/200** | **170/200** |
| **Accuracy** | **81.5%** | **86%** | **77.5%** | **56.5%** | **85%** |

**Key takeaway:** CRACK surgery costs 4.5 MMLU points vs unmodified JANG_4K (81.5% vs 86%). The JANG_4K base matches MLX 4-bit (86% vs 85%) at the same size with smarter bit allocation.

### Also available: [JANG_2S CRACK (35 GB)](https://huggingface.co/dealignai/Qwen3.5-VL-122B-A10B-JANG_2S-CRACK)
Smaller model for 48 GB+ Macs — 77.5% MMLU, 91.2% HarmBench.

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("dealignai/Qwen3.5-VL-122B-A10B-JANG_4K-CRACK")

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True,
    enable_thinking=False, tokenize=False)

response = generate(model, tokenizer, prompt=prompt, max_tokens=500)
print(response)
```

### VLM Inference

```bash
pip install "jang[vlm]"
```

```python
from jang_tools.loader import load_jang_vlm_model
from mlx_vlm import generate

model, processor = load_jang_vlm_model("dealignai/Qwen3.5-VL-122B-A10B-JANG_4K-CRACK")
result = generate(model, processor, "Describe this image.", image=["photo.jpg"], max_tokens=200)
print(result.text)
```

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon — the GGUF equivalent for MLX. Classifies tensors into sensitivity tiers and assigns bits accordingly.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) removes safety alignment from LLMs at the weight level. No custom model files, no runtime hooks — permanent and runs at full native speed.

---

## Links

<p align="center">

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=flat-square" alt="Ko-fi"></a>
<a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/X-@dealignai-000000?logo=x&logoColor=white&style=flat-square" alt="X/Twitter"></a>
<a href="https://github.com/jjang-ai/jangq"><img src="https://img.shields.io/badge/GitHub-jjang--ai/jangq-181717?logo=github&logoColor=white&style=flat-square" alt="GitHub"></a>
<a href="https://mlx.studio"><img src="https://img.shields.io/badge/MLX_Studio-App-blue?style=flat-square" alt="MLX Studio"></a>
<a href="https://jangq.ai"><img src="https://img.shields.io/badge/Website-jangq.ai-green?style=flat-square" alt="Website"></a>

</p>

- [JANG GitHub](https://github.com/jjang-ai/jangq) · [PyPI](https://pypi.org/project/jang/) · [Format Spec](https://github.com/jjang-ai/jangq/blob/main/FORMAT.md)
- [MLX Studio](https://mlx.studio) · [HuggingFace JANGQ-AI](https://huggingface.co/JANGQ-AI) · [HuggingFace dealignai](https://huggingface.co/dealignai)

---

## Disclaimer

This model is provided for research and educational purposes. The creators are not responsible for any misuse. By downloading this model, you agree to use it responsibly and in compliance with applicable laws.

---

## 한국어

### Qwen 3.5 VL 122B — JANG_4K + CRACK

**JANG** K-quant 혼합정밀도 양자화 + **CRACK** 안전장치 제거 모델입니다.

| 항목 | 내용 |
|------|------|
| 크기 | 62 GB |
| MMLU | 81.5% |
| HarmBench | 78.4% 준수 |
| 최소 요구사양 | 96 GB 메모리 Mac |

```bash
pip install "jang[mlx]"
```

[GitHub](https://github.com/jjang-ai/jangq) · [HuggingFace](https://huggingface.co/JANGQ-AI) · [MLX Studio](https://mlx.studio) · [Ko-fi](https://ko-fi.com/jangq) · [X @dealignai](https://x.com/dealignai)

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a> · 장진호 제작</p>
