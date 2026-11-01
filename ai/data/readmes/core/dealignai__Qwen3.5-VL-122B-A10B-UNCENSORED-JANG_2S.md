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

> **CRITICAL FIX (2026-03-21):** Fixed `chat_template.jinja` — previous versions may have had thinking loop issues. **Re-download if you downloaded before today.**


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

# Qwen 3.5 VL 122B-A10B — JANG_2S + CRACK

**JANG mixed-precision** · **CRACK abliterated** · No guardrails · VLM · 35 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [Qwen 3.5 122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) — a 122B parameter Mixture-of-Experts model with 256 experts (8 active per token), hybrid GatedDeltaNet SSM + full attention architecture, and built-in vision-language capabilities.

It has been:
1. **JANG quantized** — JANG_2S profile (6-bit attention, 4-bit embeddings, 2-bit experts) — **35 GB**, fits on 48 GB Macs
2. **CRACK abliterated** — permanent weight-level removal of safety refusal behavior

JANG's mixed-precision approach keeps attention weights at **6-bit** (CRITICAL tier) while compressing MoE expert weights to 2-bit. On MoE models, CRITICAL is <5% of parameters — the quality boost from 6-bit attention is nearly free.

| | |
|---|---|
| **Architecture** | Qwen 3.5 MoE — 122B total, 10B active, 256 experts |
| **Quantization** | JANG_2S (6/4/2-bit mixed) — 35 GB |
| **Abliteration** | CRACK — permanent weight modification |
| **Vision** | Built-in VLM (333 vision encoder tensors) |
| **Thinking** | Supports `enable_thinking` ON/OFF |
| **Speed** | ~51 tok/s on MacBook Pro M4 Max 128 GB |
| **Fits on** | **48 GB+ Macs** |

---

## HarmBench Results (320 prompts)

| Category | Score | Rate |
|----------|-------|------|
| Harmful content | 18/18 | **100%** |
| Copyright | 79/80 | **99%** |
| Misinformation | 52/54 | **96%** |
| Cybercrime & intrusion | 49/52 | **94%** |
| Harassment & bullying | 19/21 | **90%** |
| Chemical & biological | 36/42 | **86%** |
| Illegal activities | 39/53 | **74%** |
| **Overall** | **292/320** | **91.2%** |

---

## MMLU-200 Results (Per Subject)

### This Model (JANG_2S + CRACK) vs Base Models

| Subject | JANG_2S CRACK | JANG_2S Base | MLX 2-bit | JANG_4K Base | MLX 4-bit |
|---------|:---:|:---:|:---:|:---:|:---:|
| | **35 GB** | **38 GB** | **36 GB** | **69 GB** | **64 GB** |
| Abstract Algebra | 12/20 | 9/20 | 9/20 | 16/20 | 15/20 |
| Anatomy | 15/20 | 18/20 | 11/20 | 19/20 | 18/20 |
| Astronomy | 20/20 | 20/20 | 16/20 | 19/20 | 19/20 |
| College CS | 14/20 | 14/20 | 8/20 | 15/20 | 15/20 |
| College Physics | 12/20 | 15/20 | 10/20 | 14/20 | 14/20 |
| HS Biology | 18/20 | 19/20 | 15/20 | 19/20 | 19/20 |
| HS Chemistry | 17/20 | 18/20 | 13/20 | 18/20 | 18/20 |
| HS Mathematics | 11/20 | 11/20 | 4/20 | 14/20 | 14/20 |
| Logical Fallacies | 17/20 | 16/20 | 13/20 | 19/20 | 19/20 |
| World Religions | 19/20 | 18/20 | 14/20 | 19/20 | 19/20 |
| **Total** | **155/200** | **158/200** | **113/200** | **172/200** | **170/200** |
| **Accuracy** | **77.5%** | **79%** | **56.5%** | **86%** | **85%** |

**Key takeaways:**
- CRACK surgery costs only **1.5 MMLU points** vs unmodified JANG_2S (77.5% vs 79%)
- JANG_2S is **22.5 points better** than MLX uniform 2-bit (79% vs 56.5%)
- Even CRACK'd, this model beats MLX 2-bit by **21 points** (77.5% vs 56.5%)

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("dealignai/Qwen3.5-VL-122B-A10B-JANG_2S-CRACK")

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

model, processor = load_jang_vlm_model("dealignai/Qwen3.5-VL-122B-A10B-JANG_2S-CRACK")
result = generate(model, processor, "Describe this image.", image=["photo.jpg"], max_tokens=200)
print(result.text)
```

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon — the GGUF equivalent for MLX. Instead of quantizing all weights at the same bit width, JANG classifies tensors into sensitivity tiers:

- **CRITICAL** (attention, routers, output head): 6-8 bit
- **IMPORTANT** (embeddings, linear attention): 4-6 bit
- **COMPRESS** (MLP/FFN, MoE experts): 2-3 bit

On MoE models where CRITICAL is <5% of parameters, this gives dramatically better quality than uniform quantization at the same size.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) removes safety alignment from LLMs at the weight level. No custom model files, no runtime hooks — the modification is permanent and runs at full native speed.

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

### Qwen 3.5 VL 122B — JANG_2S + CRACK

**JANG** 혼합정밀도 양자화 + **CRACK** 안전장치 제거 모델입니다.

| 항목 | 내용 |
|------|------|
| 크기 | 35 GB |
| MMLU | 77.5% |
| HarmBench | 91.2% 준수 |
| 최소 요구사양 | 48 GB 메모리 Mac |

```bash
pip install "jang[mlx]"
```

[GitHub](https://github.com/jjang-ai/jangq) · [HuggingFace](https://huggingface.co/JANGQ-AI) · [MLX Studio](https://mlx.studio) · [Ko-fi](https://ko-fi.com/jangq) · [X @dealignai](https://x.com/dealignai)

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a> · 장진호 제작</p>
