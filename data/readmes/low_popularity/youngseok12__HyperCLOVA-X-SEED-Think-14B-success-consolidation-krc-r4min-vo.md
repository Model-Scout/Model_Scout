---
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
library_name: transformers
language:
- ko
license: other
license_name: hyperclovax-seed
license_link: LICENSE
pipeline_tag: text-generation
tags:
- korean
- hyperclovax
- sft
- lora-merged
- safetensors
- k-ai-leaderboard
---

# HyperCLOVA X SEED 14B Think — K/R/C Success-Consolidation, {v_proj, o_proj} Module A/B Arm (TIES)

This repository contains a standalone BF16 model derived from
[`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
It is a controlled module-selection A/B arm against
[`HyperCLOVA-X-SEED-Think-14B-success-consolidation-krc-r4min-ties`](https://huggingface.co/youngseok12/HyperCLOVA-X-SEED-Think-14B-success-consolidation-krc-r4min-ties):
identical data, identical LoRA rank/hyperparameters, identical trainable
parameter count (2,957,312) — the **only** difference is which two attention
projections the LoRA targets (`v_proj, o_proj` here vs. `q_proj, v_proj` in
the sibling repo). The model name begins with **HyperCLOVA X** as required
by the base model license.

## Why this arm exists

A base-parameter gradient probe (no LoRA, gradient accumulated over 192
stratified rows per axis) found that on this base model, `o_proj` receives
a gradient 1.70–1.76× larger per weight than `q_proj` (RMS) and requires
2.30–2.35× more relative change (SNIP-style), consistently across all three
K/R/C tasks — with both indicators agreeing in direction. `{v_proj, o_proj}`
was then trained and TIES-merged under conditions identical to the
`{q_proj, v_proj}` sibling to test whether this held at the same trainable
parameter budget. On a local 4-axis catastrophe-gate proxy (n=100/axis,
free-generation, seed-matched to the sibling and to the base model's own
diagnosis), this arm scored higher than the `{q_proj, v_proj}` sibling on
3/4 axes and above both the sibling and the pristine base model on average.
Local proxy scores do not reliably predict the real K-AI leaderboard in this
project's history; K-AI evaluation is the deciding measurement.

## Training data

The same 836 rows used to build the `{q_proj, v_proj}` sibling model,
unchanged. Each row's target is the pristine base model's own correct
reasoning trace (from a free-generation pass), restructured answer-first
(`정답: X\n근거: ...`) — a success-consolidation (STaR-family) construction.

| Axis | Benchmark target | AI Hub source | Arm | Rows |
|---|---|---|---|---:|
| K | KMMLU-Pro | 71875 (필수의료 의학지식 QA) | correct_unstable | 300 |
| R | MuSR(Ko) | 71568 (경제·스포츠 숫자연산 MRC) | correct_unstable | 236 |
| C | Com2-main(Ko) | 71949 (인과관계 기반 추론) | correct_all | 300 |
| **Total** | | | | **836** |

## LoRA configuration (Round 1-min capacity track)

- Rank: `4`, alpha: `8`, dropout: `0.05`
- Target modules: **`v_proj`, `o_proj` only**
- Learning rate: `5e-5`, cosine scheduler, warmup ratio `0.03`
- Epochs: `1`, effective batch size: `16` (per-device 4 × grad accum 4)
- Max sequence length: `4096`, loss: assistant-token-only
- Precision: BF16, seed: `42`
- Merge: TIES (weights `1.0/1.0/1.0`, density `0.5`) over the three per-axis LoRAs

## Merge verification

- NaN/Inf sweep: pass over all 421 merged parameters
- Generation smoke test on real benchmark probes: pass, non-empty outputs

Public benchmark test data was not used for training.
