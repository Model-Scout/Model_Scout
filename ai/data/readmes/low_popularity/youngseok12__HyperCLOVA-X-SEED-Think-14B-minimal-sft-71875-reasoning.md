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
- self-distillation
- safetensors
- k-ai-leaderboard
---

# HyperCLOVA X SEED 14B Think — Minimal Self-Distillation with Reasoning (71875)

This repository contains a standalone BF16 model derived from
[`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
It is a controlled ablation against the original
`HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875` Minimal SFT model — same source
pool, same candidate ordering/seed, same row-count target (512), same LoRA
capacity and hyperparameters. The **only** deliberate change is the target
schema: the original model's targets were a bare single letter (`A`–`E`)
because its prompt instructed the base model to output only the answer letter;
here the prompt instead invites a short rationale, and the target is
`정답: X\n근거: <the base model's own reasoning>`.

## Why this arm exists

Every prior HCX Minimal-capacity self-distillation model in this project used
label-only targets (1 character). This is the first one that keeps every other
variable fixed — source, row count, LoRA rank/modules/hyperparameters — and
isolates whether including the base model's own reasoning in the SFT target
changes the real K-AI leaderboard result. Because the prompt changed to invite
reasoning, the set of rows the base model answers correctly is not identical
to the original run's 512 rows (85.5% overlap, 438/512) — this is "same
source / same row-count target / same LoRA capacity, reasoning vs no-reasoning",
not literally the same 512 rows with rationale appended.

## Data construction

- Source: AI Hub 71875 (필수의료 의학지식 QA), the same 950-candidate pool used
  by the original Minimal SFT, same seed=42 domain round-robin ordering.
- Generation: the base model's own free-form response (max 256 new tokens,
  greedy/deterministic) to a prompt inviting reasoning ("문제를 풀고 정답을
  명확히 제시하세요. 필요한 경우 짧은 근거를 덧붙여도 됩니다."), instead of the
  original's instruction to output only the letter.
- A row is kept only if the parsed final answer matches the AI Hub gold label.
- 827 rows were attempted to reach 512 accepted (61.9% correctness rate, close
  to the original's 68.6% under the label-only prompt).
- Target: `정답: X\n근거: <trimmed model reasoning>` — the answer-first schema
  already causally validated as safe in this project's history (see project
  hard rule: format changes go through the training-data target schema only,
  never the chat template).

| Field | Value |
|---|---|
| Candidate pool | 950 |
| Attempted | 827 |
| Selected (unique) | 512 |
| Overlap with original 512-row Minimal SFT | 438 (85.5%) |
| Target length (chars) | min 53, max 519 |

## LoRA configuration (identical to the original Minimal SFT)

- Rank: `4`, alpha: `8`, dropout: `0`, target modules: `q_proj`, `v_proj` only
- Learning rate: `1e-6`, constant scheduler, warmup: `0`
- Steps: `32` (batch 1 × gradient accumulation 16 = effective batch 16, matching
  512 rows / 16 = 32 steps exactly, same as the original)
- Max sequence length: `2048` (raised from the original's `1024` because
  targets are no longer single tokens — the only non-target-schema parameter
  that had to change)
- Precision: BF16, seed: `42`, loss: assistant-token-only

## Merge verification

- NaN/Inf sweep: pass over all merged parameters
- Generation smoke test on synthetic probes: pass, non-empty, answer-first
  outputs in the trained schema (e.g. `정답: C. 6개\n민수는...`)

Public benchmark test data was not used for training.
