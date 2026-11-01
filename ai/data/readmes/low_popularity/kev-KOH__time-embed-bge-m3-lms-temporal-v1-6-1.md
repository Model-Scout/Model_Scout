---
language:
- ko
license: apache-2.0
base_model: BAAI/bge-m3
tags:
- sentence-transformers
- feature-extraction
- embeddings
- bge-m3
- korean
- temporal-retrieval
- lms
---

# Time Embed BGE-M3 LMS Temporal v1.6.1

Fine-tuned BGE-M3 checkpoint for Korean LMS temporal query embedding.

This model targets equivalence and contrast around Korean relative-time expressions, for example 일주일 전, 7일 전, and 1주 전 as positives, while separating hard negatives such as 지난주 or 최근 7일 when the temporal meaning differs.

## Source

- Base model: BAAI/bge-m3
- Training run: runs/time-embed-bge-m3-v1_6_1/20260524-162559
- Training data: kev-KOH/time-embed-bge-m3, folder bge_m3_temporal_focus_v1_6_1
- Fine-tuning setup: batch 32, train group size 8, bf16, CLS pooling, normalized embeddings

## Evaluation

Evaluated with the project v1.6.1 temporal gates on 3,000-row dev/test subsets.

| split | pairwise_accuracy | hard_negative_violation_rate | margin_mean | margin_p10 | random_pair_p95 | near_one_rate | passed_gates |
|---|---:|---:|---:|---:|---:|---:|---|
| dev | 0.981000 | 0.019000 | 0.181198 | 0.060985 | 0.497738 | 0.001343 | True |
| test | 0.980667 | 0.019333 | 0.179639 | 0.059535 | 0.522146 | 0.001307 | True |

Full eval JSON files are included under eval_reports/.

## Intended Use

Use for Korean LMS retrieval/reranking pipelines where temporal semantics must distinguish exact offsets, deictic expressions, duration expressions, windows, and deadline boundaries.

## Limitations

This is a focused temporal adaptation. Validate on downstream LMS retrieval traffic before production promotion.
