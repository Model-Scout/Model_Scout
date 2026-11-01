---
library_name: mlx
base_model: LiquidAI/LFM2.5-8B-A1B
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
pipeline_tag: text-generation
tags:
  - mlx
  - MoE
  - basequant-xl
  - lfm2.5
  - liquid
  - edge
  - 8bit
  - XL
language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
  - pt
  - it
---

# LFM2.5-8B-A1B 8-bit XL MLX

**LFM2.5-8B-A1B** by [Liquid AI](https://huggingface.co/LiquidAI) — a hybrid conv + attention MoE built for on-device deployment (extended pre-training + RL on the LFM2 architecture), quantized for Apple Silicon with the **BaseQuant_XL 8-bit** recipe.

8.3B total / **1.5B active** parameters. Designed to power on-device personal assistants: chained tool calls, complex instruction following, agentic tasks — at a memory footprint that fits 16 GB Macs.

## About XL Quantization

**BaseQuant_XL** is a fully **data-agnostic**, static quantization. No calibration dataset, no sensitivity analysis, no importance matrix. Precision is allocated purely by architectural role — routing-critical layers get higher precision, bulk expert parameters get lower precision. The result is a transparent, faithful capture of the source model.

Data-dependent calibration quantizations (iMatrix, AWQ, GPTQ, oQ, oQ4e, etc.) use a calibration set to guide bit allocation. This can produce a **skewed representation** of the model: domains well-represented in the calibration data (English, popular topics, public or leaked benchmarks) are preserved better, while underrepresented domains (non-English languages, niche use cases, your own data) are preserved worse. XL avoids this trade-off entirely — it generalizes honestly because it is never fit to any particular data distribution.

## Quickstart

```bash
pip install -U mlx-lm
mlx_lm.chat --model leonsarmiento/LFM2.5-8B-A1B-8bit-XL-mlx
```

Thinking is native to LFM2.5 — reasoning traces are emitted inline in the response.

## Quantization Strategy

| Layers | Bits | Rationale |
|--------|------|-----------|
| `feed_forward.gate` (router) | bf16 | Routing decisions — any quantization noise here causes expert misrouting |
| `embed_tokens` (tied = output head), attention, short-conv, dense MLP, routed experts | 8-bit | Near-lossless across every remaining layer — max-fidelity XL |

- **Bits per weight**: 8.501 · **Total size**: ~9.0 GB (2 shards) · **Group size**: 64

Note: `tie_word_embeddings=true` — the 8-bit embedding doubles as the output head (same treatment as our Gemma 4 XL builds).

Liquid AI also publishes their own uniform 8-bit MLX build ([LFM2.5-8B-A1B-MLX-8bit](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-MLX-8bit)); this XL variant differs by keeping the router gate in bf16.

## Recommended Inference Parameters

Per Liquid AI's model card / shipped `generation_config.json`:

| Parameter | Value |
|-----------|-------|
| `temperature` | 0.2 |
| `top_k` | 80 |
| `repetition_penalty` | 1.05 |

## Model Overview

| Property | Value |
|----------|-------|
| **Architecture** | Lfm2MoeForCausalLM (`lfm2_moe`) |
| **Parameters** | 8.3B total / 1.5B active |
| **Layers** | 24 — 18 double-gated short conv + 6 GQA full attention |
| **Experts** | 32 routed, 4 active/token + expert bias |
| **Training budget** | 38 trillion tokens |
| **Context window** | 128,000 tokens |
| **Vocabulary** | 128,000 |
| **Languages** | en, ar, zh, fr, de, ja, ko, es, pt, it |
| **License** | LFM Open License (lfm1.0) |

## Source Model Benchmarks (from Liquid AI)

| Benchmark | LFM2-8B-A1B | LFM2.5-8B-A1B | Δ |
| :--- | ---: | ---: | ---: |
| AA-Omniscience Index | -78.42 | -24.70 | +53.62 |
| IFEval | 79.44 | 91.84 | +12.40 |
| IFBench | 26.00 | 56.47 | +30.47 |
| Multi-IF | 58.54 | 79.93 | +21.39 |
| MATH500 | 74.80 | 88.76 | +13.96 |
| AIME25 | 20.00 | 42.53 | +22.53 |
| BFCLv3 | 45.07 | 64.36 | +19.29 |
| BFCLv4 | 25.52 | 48.50 | +22.98 |
| Tau² Telecom | 13.60 | 88.07 | +74.47 |
| Tau² Retail | 7.02 | 39.82 | +32.80 |

## Source

[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) — [Liquid AI docs](https://docs.liquid.ai/lfm/getting-started/welcome)
