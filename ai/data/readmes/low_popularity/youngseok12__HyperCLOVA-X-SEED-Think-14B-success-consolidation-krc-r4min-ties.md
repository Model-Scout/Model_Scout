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
- ties-merge
- safetensors
- k-ai-leaderboard
---

# HyperCLOVA X SEED 14B Think — K/R/C Success-Consolidation, Minimal-Capacity TIES Merge

This repository contains a standalone BF16 model derived from
[`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
Three axis-specific LoRA adapters (K/R/C) were trained with a deliberately
minimal capacity and merged with TIES. The model name begins with
**HyperCLOVA X** as required by the base model license.

## Model details

- Base model: `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Architecture: `HyperCLOVAXForCausalLM`
- Weight format: BF16 `safetensors`, standalone merged full model
- Chat template: official HyperCLOVA X template, preserved byte-for-byte
- Merge: TIES, weights `[1.0, 1.0, 1.0]` for K/R/C, density `0.5`

## Training data

Each axis LoRA was trained on rows where the pristine base model's own
correct reasoning trace (from a free-generation pass) was kept as the SFT
target, restructured answer-first (`정답: X\n근거: ...`). This is a
success-consolidation (STaR-family) construction: the base solves its own
training pool under three conditions (A: free generation, B1: answer-letter
only, C: choice-order shuffled), and only rows the base gets right are used.

| Axis | Benchmark target | AI Hub source | Arm | Rows |
|---|---|---|---|---:|
| K | KMMLU-Pro | 71875 (필수의료 의학지식 QA) | correct_unstable | 300 |
| R | MuSR(Ko) | 71568 (경제·스포츠 숫자연산 MRC) | correct_unstable | 236 |
| C | Com2-main(Ko) | 71949 (인과관계 기반 추론) | correct_all | 300 |

`correct_unstable` = base answers correctly under free generation but fails
the letter-only or choice-shuffle condition (an unstable/fragile correct
answer). `correct_all` was used for C because its unstable pool was too
small (247 rows) to reach the target row count.

## LoRA configuration (Round 1-min capacity track)

- Rank: `4`, alpha: `8`, dropout: `0.05`
- Target modules: `q_proj`, `v_proj` only
- Learning rate: `5e-5`, cosine scheduler, warmup ratio `0.03`
- Epochs: `1`, effective batch size: `16` (per-device 4 × grad accum 4)
- Max sequence length: `4096`, loss: assistant-token-only
- Precision: BF16, seed: `42`

This capacity (rank 4, 2 target modules) was chosen because prior K-AI
leaderboard submissions on this base model showed every rank-4/2-module
LoRA scoring higher than every rank-16/7-module LoRA, regardless of training
data — the base model is already strong, and a larger LoRA perturbation
degrades it more than task-specific data helps.

## Merge verification

- NaN/Inf sweep: pass over all 421 merged parameters
- Generation smoke test: 24 real benchmark probes, 0 empty outputs

Public benchmark test data was not used for training.
