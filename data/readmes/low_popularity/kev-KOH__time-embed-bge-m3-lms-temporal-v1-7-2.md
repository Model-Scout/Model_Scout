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
- lms
- temporal-retrieval
library_name: FlagEmbedding
pipeline_tag: feature-extraction
---

# time-embed-bge-m3-lms-temporal-v1-7-2

BGE-M3 fine-tune for Korean LMS temporal retrieval queries.

This model is trained to distinguish Korean relative and calendar time expressions for LMS item retrieval. The main target is to pull equivalent expressions together while separating hard negatives that are lexically similar but temporally different.

Examples:

- Positive: `일주일 전` = `7일 전` = `1주 전`
- Hard negative: `일주일 전` != `지난주`
- Hard negative: `7일 전` != `최근 7일`
- Hard negative: `내일까지` != `오늘까지`

## Base Model

- `BAAI/bge-m3`

## Dataset

- Dataset repo: `kev-KOH/time-embed-bge-m3`
- Training version: v1.7 Korean LMS temporal embedding dataset
- Split counts used for this run:
  - train: 94,368
  - dev: 31,857
  - test: 31,857

## Test Evaluation

Final model path before upload:

`~/Time-Embed/runs/time-embed-bge-m3-v1_7/20260530-051809`

Evaluated on the full v1.7 test split.

| Metric | Value |
|---|---:|
| evaluated_rows | 31,857 |
| positive_mean | 0.9673 |
| negative_mean | 0.4183 |
| margin_mean | 0.3824 |
| margin_p10 | 0.2655 |
| pairwise_accuracy | 0.9994 |
| hard_negative_violation_rate | 0.000596 |
| recall_at_1 | 0.9994 |
| mrr | 0.9997 |
| random_pair_p95 | 0.4722 |
| near_one_rate | 0.0392 |

The strict `near_one_rate < 0.01` gate is not passed. This metric currently counts all positive and negative candidate scores together, so high-confidence positives can inflate it. Pairwise ranking, margin, and random-pair metrics do not indicate the earlier collapse pattern.

## Known Remaining Weakness

The main remaining failure cluster is exact future offset vs window boundary around expressions like:

- Positive: `3일 뒤` = `글피`
- Hard negative: `3일 뒤` != `3일 이내`

This should be strengthened in the next dataset iteration.

## Usage

```python
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel(
    "kev-KOH/time-embed-bge-m3-lms-temporal-v1-7-2",
    use_fp16=True,
    pooling_method="cls",
)

sentences = [
    "일주일 전 업로드된 데이터 자료 찾아줘",
    "1주 전 업로드된 데이터 자료 찾아줘",
]
embeddings = model.encode(
    sentences,
    batch_size=16,
    max_length=128,
    return_dense=True,
    return_sparse=False,
    return_colbert_vecs=False,
)["dense_vecs"]
```
