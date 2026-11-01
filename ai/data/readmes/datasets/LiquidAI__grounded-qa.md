---
license: other
language: [en, ar, zh, fr, de, it, ja, ko, pt, es, pl, vi, th, id, hi, ru]
task_categories: [text-generation]
tags: [question-answering, retrieval-augmented-generation, abstention, dpo, synthetic, multilingual]
size_categories: [1K<n<10K]
configs:
  - config_name: default
    data_files:
      - {split: train, path: train.parquet}
      - {split: test, path: test.parquet}
      - {split: test_unseen, path: test_unseen.parquet}
      - {split: showcase, path: showcase.parquet}
---
# Grounded QA

> [!Note]
> 📓 **Tutorial**: This is the dataset used in [DPO with TRL](https://colab.research.google.com/github/Liquid4All/cookbook/blob/main/finetuning/notebooks/lfm3_dpo_with_trl.ipynb)

Questions over short fictional documents. The answer must come from the documents. When they don't contain it, the expected answer is a fixed fallback sentence. About half of the questions are unanswerable, most of them near misses where the documents hold related but different information. 60 domains, 16 languages.

## Splits

| Split | Rows | Content |
|---|---:|---|
| `train` | 4,072 | preference pairs (`chosen`, `rejected`) |
| `test` | 500 | the same domains, other documents |
| `test_unseen` | 300 | 5 domains that are not in `train` |
| `showcase` | 8 | examples from the unseen domains |

## Fields

| Field | Description |
|---|---|
| `id` | row identifier |
| `language` | ISO 639-1 code of the question and the expected answer |
| `domain` | domain of the documents |
| `documents` | list of `{title, text}` |
| `question` | user question |
| `answerable` | whether the documents contain the answer |
| `answer` | short answer, or `null` |
| `reference_answer` | full answer, or the fallback sentence |
| `evidence` | quotes from the documents that support the answer |
| `unanswerable_type` | why the question can't be answered, or `null` |
| `fallback` | the fallback sentence in the question's language |
| `chosen` | `train` only: the preferred answer (`reference_answer`) |
| `rejected` | `train` only: an incorrect answer |
| `rejected_type` | `train` only: `hallucination`, `refusal` or `wrong_answer` |
