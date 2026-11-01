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

# HyperCLOVA X SEED 14B Think — K/R/C Success-Consolidation, Minimal-Capacity Monolithic LoRA (no TIES)

This repository contains a standalone BF16 model derived from
[`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
A single LoRA adapter was trained on the combined K/R/C success-consolidation
data (no per-axis LoRA, no TIES merge) — a monolithic control arm against
[`HyperCLOVA-X-SEED-Think-14B-success-consolidation-krc-r4min-ties`](https://huggingface.co/youngseok12/HyperCLOVA-X-SEED-Think-14B-success-consolidation-krc-r4min-ties),
which trains the same data as three separate LoRAs merged with TIES. The
model name begins with **HyperCLOVA X** as required by the base model license.

## Model details

- Base model: `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Architecture: `HyperCLOVAXForCausalLM`
- Weight format: BF16 `safetensors`, standalone merged full model
- Chat template: official HyperCLOVA X template, preserved byte-for-byte
- Merge: single LoRA adapter merged directly (no TIES, no per-axis split)

## Training data

The same 836 rows used to build the three axis-specific LoRAs of the TIES
sibling model, concatenated into one dataset and trained as a single LoRA.
Each row's target is the pristine base model's own correct reasoning trace
(from a free-generation pass), restructured answer-first (`정답: X\n근거: ...`) —
a success-consolidation (STaR-family) construction.

| Axis | Benchmark target | AI Hub source | Arm | Rows |
|---|---|---|---|---:|
| K | KMMLU-Pro | 71875 (필수의료 의학지식 QA) | correct_unstable | 300 |
| R | MuSR(Ko) | 71568 (경제·스포츠 숫자연산 MRC) | correct_unstable | 236 |
| C | Com2-main(Ko) | 71949 (인과관계 기반 추론) | correct_all | 300 |
| **Total** | | | | **836** |

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

- NaN/Inf sweep: pass over all merged parameters
- Generation smoke test on real benchmark probes: pass, non-empty outputs

Public benchmark test data was not used for training.
