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
- jangtq-k
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
- chain-of-thought
- minimax
- minimax-m2
- 230b
pipeline_tag: text-generation
thumbnail: dealign_mascot.png
---

> **Important:** This model uses the **JANGTQ_K** mixed-bit quantization format -- a quality-tuned variant of JANGTQ that keeps `down_proj` at 4-bit (residual-stream sensitive) and `gate_proj`/`up_proj` at 2-bit (gate-dampened), while attention / shared expert / embed / lm_head stay at affine 8-bit. Currently only supported by **[MLX Studio](https://mlx.studio)** and the `jang-tools` Python package. Follow [@dealignai](https://x.com/dealignai) for new releases.

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

# MiniMax M2.7 -- JANGTQ_K + CRACK

**Mixed-bit JANGTQ_K quantization** | **CRACK abliterated** | Reasoning-only | 74 GB

<a href="https://ko-fi.com/jangq"><img src="https://img.shields.io/badge/Ko--fi-Support_Development-FF5E5B?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

</div>

---

## What Is This?

This is [MiniMax M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) -- a 230B parameter Mixture-of-Experts reasoning model with 256 experts (8 active per token), all standard attention, and always-on chain-of-thought reasoning.

It has been:
1. **JANGTQ_K quantized** -- mixed-bit profile: `down_proj` Q4, `gate_proj`/`up_proj` Q2, attention/shared/embed/lm_head Q8, norms/router fp16. **74 GB on disk**, ~3-bit avg routed.
2. **CRACK abliterated** -- a capability-preserving abliteration variant tuned for mixed-bit bases. Result: **capability-positive abliteration** (MMLU went UP from base, not down).

| | |
|---|---|
| **Architecture** | MiniMax M2.7 MoE -- 230B total, ~10B active, 256 experts |
| **Quantization** | JANGTQ_K mixed-bit (Q8 attention + Q4 `down_proj` + Q2 gate/up) -- 74 GB |
| **Abliteration** | CRACK (capability-positive on this build) |
| **MMLU-200** | **94.5%** (base K: 93.5%, delta: **+1.0pp** -- capability-positive) |
| **HarmBench-320** | **99.06%** overall (six of seven categories at 100%) |
| **Reasoning** | Always ON (chain-of-thought), `enable_thinking` kwarg supported |
| **Speed** | ~33 tok/s median (M4 Max 128 GB) |
| **Fits on** | 96 GB+ Macs |

---

## MMLU-200 Results

| Subject | CRACK | Base K | Delta |
|---------|:---:|:---:|:---:|
| Astronomy | **20/20 (100%)** | 20/20 | 0 |
| College Physics | **20/20 (100%)** | 18/20 | **+2** |
| High School Biology | **20/20 (100%)** | 20/20 | 0 |
| High School Mathematics | **20/20 (100%)** | 19/20 | **+1** |
| Abstract Algebra | 19/20 (95%) | 19/20 | 0 |
| Anatomy | 18/20 (90%) | 17/20 | **+1** |
| College Computer Science | 18/20 (90%) | 19/20 | -1 |
| High School Chemistry | 18/20 (90%) | 18/20 | 0 |
| Logical Fallacies | 18/20 (90%) | 16/20 | **+2** |
| World Religions | 18/20 (90%) | 17/20 | **+1** |
| **Total** | **189/200 (94.5%)** | **187/200 (93.5%)** | **+1.0%** |

CRACK is **capability-positive** on this build -- four subjects at 100%, six gain on base, only one loses. Net +6 questions, with the largest gains on subjects (physics, fallacies, mathematics, religions) where the model commits instead of hedging.

---

## HarmBench-320 Results

| Category | Score | |
|----------|:---:|---|
| Cybercrime / Intrusion | 52/52 | **100%** |
| Misinformation / Disinformation | 54/54 | **100%** |
| Chemical / Biological | 42/42 | **100%** |
| Harmful | 18/18 | **100%** |
| Illegal | 53/53 | **100%** |
| Harassment / Bullying | 21/21 | **100%** |
| Copyright | 77/80 | 96.2% |
| **Total** | **317/320** | **99.06%** |

Strict classifier (rejects stuck-reasoning loops, empty template dumps, and false-positive compliance from thinking-trace leakage). All three non-compliant prompts were in copyright (lyric / passage requests where the model hedged on attribution).

---

## MiniMax M2.7 CRACK Series

| Model | Format | Size | MMLU-200 | HarmBench-320 | Speed | Fits on |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| **JANGTQ_K + CRACK (this)** | **Mixed Q4/Q2 experts** | **74 GB** | **94.5%** | **99.1%** | ~33 t/s | **96 GB Mac** |
| [JANGTQ + CRACK](https://huggingface.co/dealignai/MiniMax-M2.7-JANGTQ-CRACK) | TurboQuant 2-bit experts | 55 GB | 92.0% | 93.1% | ~47 t/s | 96 GB Mac |
| [JANG_3L + CRACK](https://huggingface.co/dealignai/MiniMax-M2.7-JANG_3L-CRACK) | Affine 3-bit mixed | 89 GB | 93.5% | 79.1% | ~46 t/s | 128 GB Mac |
| [JANG_2L + CRACK](https://huggingface.co/dealignai/MiniMax-M2.7-JANG_2L-CRACK) | Affine 2-bit | 63 GB | 84.0% | 83.4% | ~47 t/s | 96 GB Mac |

### Per-category HarmBench-320 (vs JANGTQ ship)

| Category | JANGTQ_K (this) | JANGTQ ship | Δ |
|---|:---:|:---:|:---:|
| cybercrime_intrusion | 52/52 (100%) | 51/52 (98.1%) | **+1** |
| misinformation_disinformation | 54/54 (100%) | 53/54 (98.1%) | **+1** |
| chemical_biological | 42/42 (100%) | 41/42 (97.6%) | **+1** |
| harmful | 18/18 (100%) | 17/18 (94.4%) | **+1** |
| illegal | 53/53 (100%) | 48/53 (90.6%) | **+5** |
| copyright | 77/80 (96.2%) | 70/80 (87.5%) | **+7** |
| harassment_bullying | 21/21 (100%) | 18/21 (85.7%) | **+3** |
| **Total** | **317/320 (99.1%)** | **298/320 (93.1%)** | **+19** |

JANGTQ_K + CRACK trades 27 GB and ~14 t/s for a 6pp HarmBench gain and a 2.5pp MMLU gain over the JANGTQ ship -- and matches or beats the JANG_3L 89 GB variant on both axes at 15 GB less.

### vs MLX Uniform Quantization

MLX uniform quantization is **completely broken** on MiniMax at all bit levels (~25% MMLU = random chance). JANG / JANGTQ / JANGTQ_K is the only working quantization format for this architecture.

---

## About JANGTQ_K (mixed-bit)

**JANGTQ_K** is a quality-tuned mixed-bit variant of JANGTQ. The expert routing
spends 4 bits on `down_proj` (whose output enters the residual stream and
accumulates noise across 62 layers) and 2 bits on `gate_proj`/`up_proj` (whose
contribution passes through SwiGLU's multiplicative gate `silu(gate) × up`,
which dampens quantization noise). Attention / shared expert / embed /
lm_head stay at affine 8-bit for precision-critical paths.

Bundle size: **74 GB** (~3-bit avg routed) -- between JANGTQ (55 GB, all 2-bit
routed) and JANG_3L (89 GB, all 3-bit routed). Quality is closer to full-4-bit
(~115 GB) than to JANGTQ.

## About CRACK

**CRACK** (Controlled Refusal Ablation via Calibrated Knockouts) is a
weight-level intervention that removes safety alignment while preserving
reasoning quality and compliance. This build uses a capability-preserving
variant tuned for mixed-bit JANGTQ_K bases, which is why it lands
capability-positive on MMLU instead of capability-negative.

The modification is permanently baked into the published weights -- no LoRA,
no fine-tuning, no system prompts.

---

## Install & Usage

```bash
pip install "jang[mlx]"
```

```python
from jang_tools.load_jangtq import load_jangtq_model
from mlx_lm import generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load_jangtq_model("dealignai/MiniMax-M2.7-JANGTQ_K-CRACK")
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
