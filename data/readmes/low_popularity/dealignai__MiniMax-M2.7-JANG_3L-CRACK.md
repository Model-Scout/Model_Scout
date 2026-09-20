---
language:
- en
- zh
- ko
library_name: mlx
license: other
license_name: minimax-modified-mit
license_link: LICENSE
base_model: MiniMaxAI/MiniMax-M2.7
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
- reasoning
pipeline_tag: text-generation
thumbnail: dealign_mascot.png
---

> **Important:** This model uses the **JANG** quantization format -- the GGUF equivalent for MLX on Apple Silicon. Currently only supported by **[MLX Studio](https://mlx.studio)** and the `jang-tools` Python package. Follow [@dealignai](https://x.com/dealignai) for new releases.

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

# MiniMax M2.7 -- JANG_3L + CRACK

**JANG mixed-precision** | **CRACK abliterated** | Reasoning-only | 89 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [MiniMax M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) -- a 230B parameter Mixture-of-Experts reasoning model with 256 experts (8 active per token), all standard attention, and always-on chain-of-thought reasoning.

It has been:
1. **JANG quantized** -- JANG_3L profile (8-bit attention, 4-bit embeddings, 3-bit experts) -- **89 GB**
2. **CRACK abliterated** -- permanent weight-level removal of safety refusal

| | |
|---|---|
| **Architecture** | MiniMax M2.7 MoE -- 230B total, ~10B active, 256 experts |
| **Quantization** | JANG_3L (8/4/3-bit mixed) -- 89 GB |
| **Abliteration** | CRACK abliterated |
| **MMLU-200** | **93.5%** (base: 95.5%, delta: -2.0%) |
| **HarmBench-320** | **79.1%** overall, **89.4%** excluding copyright |
| **Reasoning** | Always ON (chain-of-thought) |
| **Speed** | ~46 tok/s (M4 Ultra 256 GB) |
| **Fits on** | **128 GB+ Macs** |

---

## MMLU-200 Results

| Subject | CRACK | Base | Delta |
|---------|:---:|:---:|:---:|
| High School Biology | **20/20 (100%)** | 20/20 | 0 |
| Abstract Algebra | 19/20 (95%) | 19/20 | 0 |
| Anatomy | 19/20 (95%) | 18/20 | **+1** |
| College Computer Science | 19/20 (95%) | 19/20 | 0 |
| College Physics | 19/20 (95%) | 20/20 | -1 |
| High School Chemistry | 19/20 (95%) | 19/20 | 0 |
| High School Mathematics | 19/20 (95%) | 20/20 | -1 |
| World Religions | 19/20 (95%) | 18/20 | **+1** |
| Astronomy | 18/20 (90%) | 19/20 | -1 |
| Logical Fallacies | 16/20 (80%) | 19/20 | -3 |
| **Total** | **187/200 (93.5%)** | **191/200 (95.5%)** | **-2.0%** |

---

## HarmBench-320 Results

| Category | Score | |
|----------|:---:|---|
| Cybercrime / Intrusion | 52/52 | **100%** |
| Misinformation / Disinfo | 52/54 | 96.3% |
| Chemical / Biological | 37/42 | 88.1% |
| Harmful | 15/18 | 83.3% |
| Illegal | 40/53 | 75.5% |
| Harassment / Bullying | 14/21 | 66.7% |
| Copyright | 43/80 | 53.8% |

> **Note on copyright:** M2.7's base model has strong copyright training and refuses to reproduce copyrighted books/lyrics regardless of abliteration. This is a base model limitation, not a surgery result.

---

## JANG CRACK M2.7 Series

| Model | Avg Bits | Size | MMLU | HarmBench | Speed | Fits on |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| [JANG_2L + CRACK](https://huggingface.co/dealignai/MiniMax-M2.7-JANG_2L-CRACK) | 2.1 | 63 GB | 84.0% | 83.4% | ~47 t/s | 96 GB Mac |
| **JANG_3L + CRACK** | **3.08** | **89 GB** | **93.5%** | **79.1%** | **~46 t/s** | **128 GB Mac** |

### vs MLX Uniform Quantization

MLX uniform quantization is **completely broken** on MiniMax at ALL bit levels (~25% MMLU = random chance). JANG is the only working quantization format for this architecture.

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools import load_for_inference
from mlx_lm import generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load_for_inference("dealignai/MiniMax-M2.7-JANG_3L-CRACK")
sampler = make_sampler(temp=1.0)  # MiniMax requires temp=1.0 for chat

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False)

response = generate(model, tokenizer, prompt=prompt, max_tokens=4000, sampler=sampler)
print(response)
```

> **Note:** M2.7 is a reasoning-only model -- it always generates a `<think>` chain before answering. Use `max_tokens=4000+` for complex questions. For chat, use `temperature=1.0` (greedy causes infinite loops).

---

## About JANG

**JANG** (Jang Adaptive N-bit Grading) is a mixed-precision quantization format for Apple Silicon -- the GGUF equivalent for MLX. Classifies tensors into sensitivity tiers and assigns bits accordingly.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) removes safety alignment from LLMs at the weight level, achieving compliance while preserving reasoning quality.

---

## Links

<p align="center">

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>
<a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/X-@dealignai-000000?logo=x&logoColor=white&style=for-the-badge" alt="X/Twitter"></a>
<a href="https://github.com/jjang-ai/jangq"><img src="https://img.shields.io/badge/GitHub-jjang--ai/jangq-181717?logo=github&logoColor=white&style=for-the-badge" alt="GitHub"></a>
<a href="https://mlx.studio"><img src="https://img.shields.io/badge/MLX_Studio-App-blue?style=for-the-badge" alt="MLX Studio"></a>
<a href="https://jangq.ai"><img src="https://img.shields.io/badge/Website-jangq.ai-green?style=for-the-badge" alt="Website"></a>

</p>

---

## Disclaimer

This model is provided for research and educational purposes. The creators are not responsible for any misuse. By downloading this model, you agree to use it responsibly and in compliance with applicable laws.

---

<p align="center">Created by <a href="https://jangq.ai">Jinho Jang</a></p>
