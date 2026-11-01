---
pretty_name: Expert RAG Benchmarks
language:
- en
- ko
license: other
task_categories:
- question-answering
- text-retrieval
tags:
- legal
- rag
- retrieval
configs:
- config_name: questions
  default: true
  data_files:
  - split: housing
    path: "data/housing/questions-*.parquet"
  - split: barexam
    path: "data/barexam/questions-*.parquet"
  - split: kcl_essay
    path: "data/kcl-essay/questions-*.parquet"
  - split: legit_train
    path: "data/legit_train/questions-*.parquet"
  - split: legit_val
    path: "data/legit_val/questions-*.parquet"
  - split: legit_test
    path: "data/legit_test/questions-*.parquet"
- config_name: documents
  data_files:
  - split: housing
    path: "data/housing/documents-*.parquet"
  - split: barexam
    path: "data/barexam/documents-*.parquet"
  - split: kcl_essay
    path: "data/kcl-essay/documents-*.parquet"
  - split: legit_train
    path: "data/legit_train/documents-*.parquet"
  - split: legit_val
    path: "data/legit_val/documents-*.parquet"
  - split: legit_test
    path: "data/legit_test/documents-*.parquet"
- config_name: qrels
  data_files:
  - split: housing
    path: "data/housing/qrels-*.parquet"
  - split: barexam
    path: "data/barexam/qrels-*.parquet"
  - split: kcl_essay
    path: "data/kcl-essay/qrels-*.parquet"
  - split: legit_train
    path: "data/legit_train/qrels-*.parquet"
  - split: legit_val
    path: "data/legit_val/qrels-*.parquet"
  - split: legit_test
    path: "data/legit_test/qrels-*.parquet"
---
# Expert RAG Benchmarks

A unified collection of four expert-level legal RAG benchmarks, exposed as six
named splits and three relational configurations: `questions`, `documents`, and
`qrels`.

The KCL split is named `kcl_essay` because Hugging Face split identifiers do not
permit hyphens; its source name remains `kcl-essay`.

## Loading

```python
from datasets import load_dataset

repo_id = "jinulee-v/expert-rag-benchmarks"
questions = load_dataset(repo_id, "questions", split="housing")
documents = load_dataset(repo_id, "documents", split="housing")
qrels = load_dataset(repo_id, "qrels", split="housing")
```

Join `questions.qid` to `qrels.qid`, then join `qrels.doc_id` to
`documents.doc_id`.

## Sizes

| Split | Questions | Documents | Qrels |
|---|---:|---:|---:|
| `housing` | 6,853 | 1,837,403 | 17,862 |
| `barexam` | 1,195 | 856,835 | 1,195 |
| `kcl_essay` | 169 | 128,790 | 531 |
| `legit_train` | 24,262 | 128,789 | 87,423 |
| `legit_val` | 200 | 128,789 | 721 |
| `legit_test` | 300 | 128,789 | 1,229 |

The `kcl-essay`, `legit_train`, `legit_val`, and `legit_test` splits use the
shared 128,789-document Korean legal corpus. KCL additionally includes the
2020모633 judgment crawled from the National Law Information Center, bringing
its corpus to 128,790 documents. Each corpus is exposed under its applicable
split to keep the loading interface uniform.

## Schemas

- `questions`: `qid`, `question`, `answer`, `answer_type`, `choices_json`,
  `eval_json`, `meta_json`, `gold_contexts_json`
- `documents`: `doc_id`, `title`, `text`, `meta_json`
- `qrels`: `qid`, `doc_id`, `relevance`, `citation`, `issue_id`

Fields ending in `_json` contain JSON-encoded values. Encoding heterogeneous
nested metadata this way preserves it losslessly while maintaining one stable
Parquet schema across all six splits. Decode one with `json.loads(value)` when
the value is not null. `citation` is populated by Housing QA; `issue_id` is
populated by LEGIT; both are nullable elsewhere.

## Benchmark notes

- `housing`: yes/no questions about U.S. state housing law as of 2021. The full
  retrieval corpus contains statutes from 48 states.
- `barexam`: multiple-choice MBE questions over the complete annotated passage
  pool. The upstream train/validation/test examples are combined here as the
  requested `barexam` split.
- `kcl_essay`: Korean bar-exam essay questions with instance-level rubrics.
  A reviewed correction spreadsheet adds 13 unique relevance labels (531 total,
  covering 164 of 169 questions). Reference judgments are used where the fixed
  ID column was blank; 2020모633 was crawled from
  [law.go.kr](https://law.go.kr/LSW/precInfoR.do?precSeq=212509&vSct=%2A).
  The missing Constitutional Court judgment 2013헌바271 remains excluded.
- `legit_train`, `legit_val`, `legit_test`: Korean judgment prediction with
  legal issue-tree rubrics.

The metadata recorded with each source split is available under `metadata/`.
The published `legit_val` metadata records 721 qrels, matching the file; the
local precursor metadata had a stale count of 702.

`legit_train` contains 24,262 question rows but 24,086 distinct `qid` values:
176 identifiers each occur twice, with different question records. These source
rows are preserved rather than silently deduplicated. Consumers that require a
unique row key should combine `qid` with the row index; qrels continue to join
on the source `qid`.

## Sources, licenses, and attribution

This repository is a collection. The applicable license depends on the split:

- Housing QA and Bar Exam QA: **CC BY-SA 4.0**, from
  [Stanford RegLab](https://reglab.github.io/legal-rag-benchmarks/).
- KCL: **CC BY-NC 4.0**, from
  [Korean Canonical Legal Benchmark](https://huggingface.co/datasets/lbox/kcl)
  (arXiv:2512.24572).
- LEGIT: **CC BY-NC 4.0**, from
  [LEGIT](https://huggingface.co/datasets/jinulee-v/legit_ko_verl)
  (arXiv:2512.01020).

Users are responsible for following the license that applies to each split.
The non-commercial restriction applies to KCL and LEGIT. The Housing QA and Bar
Exam QA share-alike requirements continue to apply to those materials.

## Intended use and limitations

The collection is intended for research on retrieval and retrieval-augmented
generation in expert legal domains. It is not legal advice. Housing questions
and statutes describe law as of 2021 and may not reflect current law. Benchmark
answers, annotations, and retrieved materials can be incomplete or erroneous.
