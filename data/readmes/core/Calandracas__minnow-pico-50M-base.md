---
library_name: transformers
tags:
  - deepseek-v4
  - moe
  - from-scratch
  - multilingual
language:
  - multilingual
  - en
  - zh
  - es
  - fr
  - de
  - ja
  - ru
  - pt
  - ar
  - ko
license: other
license_name: openmdw-1.1
license_link: https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1
---

# minnow-pico-50M-base

A 48.5M parameter DeepSeek-V4 architecture model trained from scratch on a
multilingual blend of C4 data (108 languages). This is a research sandbox
model for studying the DeepSeek-V4 architecture at small scale — it is
**not** a production model and has no practical use.

## Architecture

Based on the [DeepSeek-V4](https://arxiv.org/abs/2606.19448) architecture,
consumed via HuggingFace `DeepseekV4ForCausalLM` (transformers ≥ 5.14):

- 256-dim hidden, 8 layers, 4 heads × 64 head_dim
- 16 experts, top-2 routing (Sqrt(Softplus) affinity)
- Hash-routed MoE on first 3 layers, learned routing on last 2
- Hybrid attention (CSA + HCA + sliding)
- Manifold-Constrained Hyper-Connections (mHC)
- Grouped low-rank attention output projection
- 48,538,724 parameters total

## Training

- **Data**: 1B tokens from a multilingual C4 blend (108 languages)
- **Optimizer**: AdamW (betas 0.9, 0.95)
- **Learning rate**: 6e-4, cosine schedule, 763 warmup steps
- **Batch size**: 131,072 tokens/step (2× RX 7900 XTX, NCCL DDP)
- **Steps**: 7,629
- **Final loss**: 3.49
- **Hardware**: 2× AMD RX 7900 XTX (gfx1100, RDNA3)

This model was trained from scratch (random initialization) — it does not
inherit weights from any pretrained model.

## Tokenizer

Uses the DeepSeek-V4-Flash-0731 tokenizer (vocab 129,280).

## Disclaimer

This model exists purely for architectural experimentation. At 48.5M
parameters, it cannot perform any useful tasks. Do not use it for anything.
