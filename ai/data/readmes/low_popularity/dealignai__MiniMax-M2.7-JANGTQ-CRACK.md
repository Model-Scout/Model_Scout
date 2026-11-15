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
- jangtq
- turboquant
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

> ## 🔧 2026-04-15 · chat_template.jinja — enable_thinking=False honored
>
> This release ships a chat_template that **respects `enable_thinking=False`** (synced with the JANG_2L template structure, M2.7 identity preserved). The `<think>` prefix is now conditional, so callers can skip reasoning mode for fast direct answers. Reasoning ON (default) is unchanged.
>
> **If you cloned this repo before 2026-04-15**, please re-download `chat_template.jinja`:
>
> ```bash
> hf download dealignai/MiniMax-M2.7-JANGTQ-CRACK chat_template.jinja --local-dir /path/to/your/local/copy
> ```
>
> Model weights are unchanged.

---

> **Important:** This model uses the **JANGTQ** (JANG TurboQuant) quantization format -- an extreme-compression variant of JANG for MLX on Apple Silicon that uses codebook + Hadamard rotation on MoE experts while keeping attention at affine 8-bit. Currently only supported by **[MLX Studio](https://mlx.studio)** and the `jang-tools` Python package. Follow [@dealignai](https://x.com/dealignai) for new releases.

---

<p align="center">
  <a href="https://mlx.studio"><img src="https://raw.githubusercontent.com/jjang-ai/jangq/main/assets/mlx-studio-light.png" alt="MLX Studio" width="500"></a>
</p>

<p align="center">
  <a href="https://mlx.studio"><img src="https://mlx.studio/assets/screenshots/mlx-studio-featured.png?v=1" alt="MLX Studio App" width="600"></a>
</p>

<h4 align="center"><a href="https://mlx.studio">MLX Studio</a> -- the only app that natively supports JANG / JANGTQ models</h4>

---

<div align="center">

<img src="dealign_mascot.png" width="128" />

<p align="center">
  <a href="https://vmlx.net"><img src="vmlx-app.png" alt="vMLX — run JANG models on Apple Silicon" width="820"></a>
</p>

<h3 align="center">⚡ All JANG models are meant to be run in <a href="https://vmlx.net">vMLX</a></h3>

# MiniMax M2.7 -- JANGTQ + CRACK

**JANGTQ TurboQuant mixed-precision** | **CRACK abliterated** | Reasoning-only | 55 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [MiniMax M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) -- a 230B parameter Mixture-of-Experts reasoning model with 256 experts (8 active per token), all standard attention, and always-on chain-of-thought reasoning.

It has been:
1. **JANGTQ quantized** -- JANGTQ profile (8-bit affine attention / embeddings / lm_head, 2-bit TurboQuant routed experts with codebook + Hadamard rotation) -- **55 GB**
2. **CRACK abliterated** -- permanent weight-level removal of safety refusal

| | |
|---|---|
| **Architecture** | MiniMax M2.7 MoE -- 230B total, ~10B active, 256 experts |
| **Quantization** | JANGTQ (affine 8-bit attention + TurboQuant 2-bit experts) -- 55 GB |
| **Abliteration** | CRACK abliterated |
| **MMLU-200** | **92.0%** (base: 91.5%, delta: **+0.5%**) |
| **HarmBench-320** | **93.1%** overall, **95.0%** excluding copyright |
| **Reasoning** | Always ON (chain-of-thought), `enable_thinking` kwarg supported |
| **Speed** | ~47 tok/s (M3 Ultra 256 GB) |
| **Fits on** | **96 GB+ Macs** |

---

## MMLU-200 Results

| Subject | CRACK | Base | Delta |
|---------|:---:|:---:|:---:|
| College Physics | **20/20 (100%)** | 18/20 | **+2** |
| High School Mathematics | **19/20 (95%)** | 19/20 | 0 |
| College Computer Science | **19/20 (95%)** | 19/20 | 0 |
| Astronomy | **19/20 (95%)** | 20/20 | -1 |
| High School Biology | **19/20 (95%)** | 20/20 | -1 |
| World Religions | **19/20 (95%)** | 17/20 | **+2** |
| High School Chemistry | **18/20 (90%)** | 18/20 | 0 |
| Logical Fallacies | **18/20 (90%)** | 16/20 | **+2** |
| Abstract Algebra | 17/20 (85%) | 19/20 | -2 |
| Anatomy | 16/20 (80%) | 17/20 | -1 |
| **Total** | **184/200 (92.0%)** | **183/200 (91.5%)** | **+0.5%** |

CRACK is **knowledge-neutral on this model** -- small per-subject variance, net positive. Gains on physics, fallacies, religions offset losses on algebra and anatomy.

---

## HarmBench-320 Results

| Category | Score | |
|----------|:---:|---|
| Cybercrime / Intrusion | 51/52 | **98.1%** |
| Misinformation / Disinformation | 53/54 | **98.1%** |
| Chemical / Biological | 41/42 | **97.6%** |
| Harmful | 17/18 | **94.4%** |
| Illegal | 48/53 | **90.6%** |
| Copyright | 70/80 | 87.5% |
| Harassment / Bullying | 18/21 | 85.7% |
| **Total** | **298/320** | **93.1%** |
| **Excluding copyright** | **228/240** | **95.0%** |

Scored with a strict classifier that rejects stuck-reasoning loops, empty template dumps, and false-positive compliance from thinking-trace leakage.

---

## JANG CRACK M2.7 Series

| Model | Format | Size | MMLU | HarmBench | Speed | Fits on |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| **JANGTQ + CRACK** | **TurboQuant 2-bit experts** | **55 GB** | **92.0%** | **93.1%** | **~47 t/s** | **96 GB Mac** |
| [JANG_3L + CRACK](https://huggingface.co/dealignai/MiniMax-M2.7-JANG_3L-CRACK) | Affine 3-bit mixed | 89 GB | 93.5% | 79.1% | ~46 t/s | 128 GB Mac |

### vs MLX Uniform Quantization

MLX uniform quantization is **completely broken** on MiniMax at ALL bit levels (~25% MMLU = random chance). JANG / JANGTQ is the only working quantization format for this architecture.

---

## About JANGTQ

**JANGTQ** (JANG TurboQuant) is an extreme-compression variant of JANG that replaces affine quantization on routed MoE experts with **codebook quantization + random Hadamard rotation**. Attention / embeddings / lm_head stay at affine 8-bit for precision-critical paths; the 256 routed experts use 2-bit packed codebook indices stored as `uint32`, with a per-row float16 norm and a tiny Lloyd-Max codebook per layer. Metal kernels do dequant + matmul fused on-GPU, no affine conversion.

For MiniMax M2.7 (230B total, 10B active, 256 experts) this brings the model from 460 GB (bf16) down to **55 GB** with minimal quality loss -- the JANGTQ profile beats every MLX uniform quant while fitting on a 96 GB Mac.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) is a weight-level intervention that removes safety alignment while preserving reasoning quality and compliance. The modification is permanently baked into the published weights — no LoRA, no fine-tuning, no system prompts.

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.load_jangtq import load_jangtq_model
from mlx_lm import generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load_jangtq_model("dealignai/MiniMax-M2.7-JANGTQ-CRACK")
sampler = make_sampler(temp=1.0)  # MiniMax requires temp=1.0 for chat

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False)

response = generate(model, tokenizer, prompt=prompt, max_tokens=4000, sampler=sampler)
print(response)
```

> **Note:** M2.7 is a reasoning-only model -- it always generates a `<think>` chain before the final answer. Use `max_tokens=4000+` for complex questions. For chat, use `temperature=1.0` (greedy causes infinite loops). Set `enable_thinking=False` in `apply_chat_template` to skip the `<think>` block on short responses.

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
