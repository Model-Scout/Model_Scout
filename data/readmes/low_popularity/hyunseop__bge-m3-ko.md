---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model: dragonkue/BGE-m3-ko
datasets:
  - nvidia/Nemotron-Personas-Korea
tags:
  - sentence-transformers
  - korean
  - embedding
  - contrastive-learning
---

# bge-m3-ko-h100

H100 fine-tuned Korean embedding model based on `dragonkue/BGE-m3-ko`.

This is the better fit for the local AutoRAG corpus among the two uploaded models. Compared with `qwen3-embedding-h100`, it is the stronger model to highlight for the domain-specific benchmark.

## Training

Fine-tuned from `dragonkue/BGE-m3-ko` (the official `BAAI/bge-m3` continued-trained on Korean MIRACL) with a **contrastive (in-batch-negative) objective**.

- **Base model:** [`dragonkue/BGE-m3-ko`](https://huggingface.co/dragonkue/BGE-m3-ko) — Korean-specialized BGE-M3
- **Training data:** [`nvidia/Nemotron-Personas-Korea`](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) — synthetic Korean personas (demographic / geographic / personality), used as `(query, positive-document)` pairs
- **Objective:** `sentence-transformers` `MultipleNegativesRankingLoss` (in-batch negatives, InfoNCE-style)
- **Hardware:** 4×H100 (Slurm)
- **Hyperparameters:** 3 epochs · per-device batch size 8 · gradient accumulation 4 · learning rate 2e-5 · warmup ratio 0.1 · weight decay 0.01 · bf16
- **Finetune run:** `111677_20260506_114341_both_2gpu`

## Benchmark Results

### AutoRAG

- Corpus size: 720
- Queries evaluated: 114
- MRR: 0.7773
- MAP: 0.7773
- Hit@1: 0.6754
- Hit@5: 0.9123
- Hit@10: 0.9474
- Hit@50: 0.9825

### MIRACL

- Task: `MIRACLRetrieval`
- Main score: 0.50
- Dataset revision: `9c09abc13478308c27598f350e31d8f06b9b5481`

| cutoff | Precision | Recall | F1 | mAP | mRR | NDCG |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| @1 | 0.39906 | 0.25093 | 0.30812 | 0.25093 | 0.399061 | 0.39906 |
| @3 | 0.26604 | 0.43788 | 0.33099 | 0.34631 | 0.50313 | 0.43568 |
| @5 | 0.20282 | 0.52623 | 0.29279 | 0.37510 | 0.523787 | 0.45984 |
| @10 | 0.13380 | 0.64972 | 0.22190 | 0.40375 | 0.537201 | 0.50233 |
| @20 | 0.08052 | 0.72989 | 0.14504 | 0.41724 | 0.540598 | 0.53096 |
| @100 | 0.02272 | 0.90287 | 0.04432 | 0.43030 | 0.543259 | 0.57932 |
| @1000 | 0.00254 | 0.98881 | 0.00507 | 0.43149 | 0.543447 | 0.59457 |

## Artifacts

- Model: `output/111677_20260506_114341_both_2gpu/bge`
- AutoRAG benchmark: `benchmark_results/autorag_benchmark.json`
- MIRACL summary: `benchmark_results/miracl_benchmark.txt`
- MIRACL details: `benchmark_results/mteb/MIRACLRetrieval.json`

## Comparison note

- Strongest AutoRAG result of the two uploaded models
- Weaker MIRACL-KO result than `rtfin-qwen3-embedding-h100`
- Below `dragonkue/snowflake-arctic-embed-l-v2.0-ko` and `rtfin-qwen3-embedding-h100` on the public Korean retrieval leaderboard, but still a strong local-domain model
- Good to cite when the audience cares about the local domain corpus rather than the widest public Korean retrieval leaderboard
