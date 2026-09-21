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

> **Important:** This model uses the **JANG** quantization format -- the GGUF equivalent for MLX on Apple Silicon. Currently only supported by **[MLX Studio](https://mlx.studio)** and the `jang-tools` Python package.

---

<p align="center">
  <a href="https://mlx.studio"><img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/mlx-studio-light.png" alt="MLX Studio" width="500"></a>
</p>

<p align="center">
  <a href="https://mlx.studio"><img src="https://mlx.studio/assets/screenshots/mlx-studio-featured.png?v=1" alt="MLX Studio App" width="600"></a>
</p>

<h4 align="center"><a href="https://mlx.studio">MLX Studio</a> -- the only app that natively supports JANG models</h4>

---

<div align="center">

<img src="dealign_mascot.png" width="128" />

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

# MiniMax M2.5 -- JANG_4M + CRACK

**JANG mixed-precision** | **CRACK abliterated** | No guardrails | 115 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [MiniMax M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) -- a 230B parameter Mixture-of-Experts model with 256 experts (8 active per token), all standard attention (no SSM), and trained with chain-of-thought reasoning.

It has been:
1. **JANG quantized** -- JANG_4M profile (8-bit attention, 4-bit experts) -- **115 GB**
2. **CRACK abliterated** -- permanent weight-level removal of safety refusal

| | |
|---|---|
| **Architecture** | MiniMax M2.5 MoE -- 230B total, ~10B active, 256 experts |
| **Quantization** | JANG_4M (8/4-bit mixed, 4.06 avg) -- 115 GB |
| **Abliteration** | CRACK abliterated |
| **MMLU-200** | **92.5%** (thinking ON) / 89.0% (thinking OFF) |
| **HarmBench** | **92.2%** (295/320) |
| **Compliance** | 8/8 prompts |
| **Thinking** | ON/OFF supported |
| **Speed** | ~48 tok/s (M4 Ultra 256 GB) |
| **Fits on** | **192 GB+ Macs** |

---

## MMLU-200 Results (Thinking ON)

| Subject | Score |
|---------|:---:|
| College Physics | **20/20 (100%)** |
| Anatomy | 19/20 (95%) |
| Astronomy | 19/20 (95%) |
| High School Biology | 19/20 (95%) |
| High School Chemistry | 19/20 (95%) |
| Logical Fallacies | 19/20 (95%) |
| Abstract Algebra | 18/20 (90%) |
| High School Mathematics | 18/20 (90%) |
| World Religions | 18/20 (90%) |
| College Computer Science | 16/20 (80%) |
| **Total** | **185/200 (92.5%)** |

---

## JANG CRACK Series Comparison

| Model | Avg Bits | Size | MMLU | HarmBench | Speed | Fits on |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| [JANG_2L + CRACK](https://huggingface.co/dealignai/MiniMax-M2.5-UNCENSORED-JANG_2L) | 2.1 | 63 GB | 84.7% | 98.1% | ~35 t/s | 96 GB Mac |
| [JANG_3L + CRACK](https://huggingface.co/dealignai/MiniMax-M2.5-JANG_3L-CRACK) | 3.08 | 89 GB | 91.8% | 8/8 | ~46 t/s | 128 GB Mac |
| **JANG_4M + CRACK** | **4.06** | **115 GB** | **92.5%** | **92.2%** | **~48 t/s** | **192 GB Mac** |

### vs MLX Uniform Quantization

| Model | MMLU | Size | Notes |
|-------|:---:|:---:|-------|
| **JANG_4M + CRACK** | **92.5%** | **115 GB** | **This model** |
| MLX 4-bit | 26.5% | 120 GB | **Broken** (~random) |
| MLX 3-bit | 24.5% | 93 GB | **Broken** (~random) |
| MLX 2-bit | 25.0% | 67 GB | **Broken** (~random) |

MLX uniform quantization is **completely broken** on MiniMax at ALL bit levels (~25% = random chance). JANG is the only working quantization format for this model.

---

## HarmBench Results

**295/320 (92.2%)**

| Category | Score | |
|----------|:---:|---|
| Harmful | 18/18 | **100%** |
| Chemical / Biological | 41/42 | 97.6% |
| Cybercrime / Intrusion | 50/52 | 96.2% |
| Misinformation / Disinfo | 52/54 | 96.3% |
| Illegal | 50/53 | 94.3% |
| Copyright | 67/80 | 83.8% |
| Harassment / Bullying | 17/21 | 81.0% |

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools import load_for_inference
from mlx_lm import generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load_for_inference("dealignai/MiniMax-M2.5-JANG_4M-CRACK")
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

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon -- the GGUF equivalent for MLX. Classifies tensors into sensitivity tiers and assigns bits accordingly.

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

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a></p>
