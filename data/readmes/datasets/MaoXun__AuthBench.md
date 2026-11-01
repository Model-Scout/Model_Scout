---
pretty_name: AuthBench
license: other
language:
- ar
- de
- en
- es
- fr
- hi
- ja
- ko
- ru
- zh
multilinguality: multilingual
size_categories:
- 100K<n<1M
configs:
- config_name: documents
  default: true
  data_files:
  - split: train
    path: train/documents.jsonl
  - split: dev
    path: dev/documents.jsonl
  - split: test
    path: test/documents.jsonl
- config_name: queries
  data_files:
  - split: train
    path: train/queries.jsonl
  - split: dev
    path: dev/queries.jsonl
  - split: test
    path: test/queries.jsonl
- config_name: candidates
  data_files:
  - split: train
    path: train/candidates.jsonl
  - split: dev
    path: dev/candidates.jsonl
  - split: test
    path: test/candidates.jsonl
- config_name: ground_truth
  data_files:
  - split: train
    path: train/ground_truth.jsonl
  - split: dev
    path: dev/ground_truth.jsonl
  - split: test
    path: test/ground_truth.jsonl
---

# AuthBench

AuthBench is a multilingual benchmark for authorship representation across languages, genres, and document lengths. It supports:

- authorship attribution as open-world same-author retrieval
- authorship verification as same-author binary decision

This Hub export contains the full mixed-source AuthBench folder, including sources that the current paper classifies as Tier B / manifest-only from a redistribution standpoint.

## Release Summary

- Release mode: `full`
- Documents: 428,150
- Authors: 153,825
- Queries: 198,345
- Candidates: 229,805
- Ground-truth rows: 198,345
- Languages: 10

## Included Sources

- `amazon_multi`: 4,924 documents
- `arabic_poetry`: 2,503 documents
- `arxiv`: 1,784 documents
- `babel_briefings`: 73,676 documents (CC BY-NC-SA 4.0)
- `blog_authorship`: 22,494 documents
- `douban`: 10,424 documents
- `exorde`: 94,231 documents (MIT)
- `french_pd_books`: 8,761 documents (Public domain)
- `german_pd`: 8,400 documents (Public domain)
- `hindi_discourse`: 213 documents
- `project_gutenberg`: 18,739 documents
- `russian_pd`: 12,728 documents (Public domain)
- `spanish_pd_books`: 4,961 documents (Public domain)
- `stackexchange`: 4,651 documents (CC BY-SA (version depends on post date))
- `wikisource`: 78,984 documents
- `xiaohongshu`: 8,869 documents
- `ytcomments`: 71,808 documents

## Excluded Sources

- None

## Repository Layout

This dataset repository exposes four dataset configurations:

- `documents`: union of the query and candidate documents for each split
- `queries`: query-side records used for retrieval / verification evaluation
- `candidates`: candidate-side records used for retrieval / verification evaluation
- `ground_truth`: mapping from `query_id` to its same-author `positive_ids`

Each configuration has `train`, `dev`, and `test` splits.

## Load with `datasets`

```python
from datasets import load_dataset

documents = load_dataset("YOUR_HF_NAMESPACE/AuthBench", "documents", split="train")
queries = load_dataset("YOUR_HF_NAMESPACE/AuthBench", "queries", split="test")
candidates = load_dataset("YOUR_HF_NAMESPACE/AuthBench", "candidates", split="test")
ground_truth = load_dataset("YOUR_HF_NAMESPACE/AuthBench", "ground_truth", split="test")
```

## Split Sizes

| Split | Documents | Queries | Candidates | Ground Truth |
| --- | ---: | ---: | ---: | ---: |
| train | 342,519 | 156,335 | 186,184 | 156,335 |
| dev | 42,821 | 21,008 | 21,813 | 21,008 |
| test | 42,810 | 21,002 | 21,808 | 21,002 |

## Schema

`documents`

```json
{
  "doc_id": "mix_009328",
  "lang": "ar",
  "genre": "social_media/technology",
  "content": "...",
  "source": "exorde",
  "token_length": 51,
  "author_id": "...",
  "retrieval_role": "candidate",
  "phase": "phase1",
  "input_split": "dev",
  "input_doc_type": "query"
}
```

`queries`

```json
{
  "query_id": "mix_009332",
  "lang": "ar",
  "genre": "social_media/entertainment",
  "content": "...",
  "source": "exorde",
  "token_length": 50,
  "retrieval_role": "query",
  "phase": "phase1",
  "input_split": "dev",
  "input_doc_type": "candidate"
}
```

`candidates`

```json
{
  "candidate_id": "mix_009328",
  "lang": "ar",
  "genre": "social_media/technology",
  "content": "...",
  "source": "exorde",
  "token_length": 51,
  "author_id": "...",
  "retrieval_role": "candidate",
  "phase": "phase1",
  "input_split": "dev",
  "input_doc_type": "query"
}
```

`ground_truth`

```json
{
  "query_id": "mix_009332",
  "positive_ids": ["mix_009328", "mix_009330", "mix_009329"],
  "author_id": "..."
}
```

## Language Coverage

- `en`: 97,974 documents
- `ru`: 66,084 documents
- `zh`: 55,368 documents
- `ar`: 42,091 documents
- `de`: 39,813 documents
- `ko`: 33,881 documents
- `es`: 33,395 documents
- `fr`: 31,225 documents
- `ja`: 21,494 documents
- `hi`: 6,825 documents

## Source Distribution

| Source | Documents | Share |
| --- | ---: | ---: |
| `exorde` | 94,231 | 22.0% |
| `wikisource` | 78,984 | 18.4% |
| `babel_briefings` | 73,676 | 17.2% |
| `ytcomments` | 71,808 | 16.8% |
| `blog_authorship` | 22,494 | 5.3% |
| `project_gutenberg` | 18,739 | 4.4% |
| `russian_pd` | 12,728 | 3.0% |
| `douban` | 10,424 | 2.4% |
| `xiaohongshu` | 8,869 | 2.1% |
| `french_pd_books` | 8,761 | 2.0% |
| `german_pd` | 8,400 | 2.0% |
| `spanish_pd_books` | 4,961 | 1.2% |
| `amazon_multi` | 4,924 | 1.2% |
| `stackexchange` | 4,651 | 1.1% |
| `arabic_poetry` | 2,503 | 0.6% |
| `arxiv` | 1,784 | 0.4% |
| `hindi_discourse` | 213 | 0.0% |

## Primary Genre Distribution

| Primary Genre | Documents | Share |
| --- | ---: | ---: |
| `social_media` | 174,908 | 40.9% |
| `literature` | 128,395 | 30.0% |
| `news` | 73,676 | 17.2% |
| `blog` | 22,494 | 5.3% |
| `media_reviews` | 10,424 | 2.4% |
| `poetry` | 6,894 | 1.6% |
| `ecommerce_reviews` | 4,924 | 1.2% |
| `qna` | 4,651 | 1.1% |
| `research_paper` | 1,784 | 0.4% |

## Licensing And Redistribution Notes

This release mixes upstream licenses and platform terms across both Tier A and Tier B sources. The paper explicitly recommends conservative manifest-only handling for several included sources. Do not treat this repository as a blanket relicensing of all component texts.

For the benchmark-wide source inventory and the Tier A / Tier B rationale, see:

- `DATASET.md` in the AuthBench repository
- `paper/colm_latex.tex`, especially the appendix licensing table

## Caveats

- `queries` intentionally omit `author_id`; the supervision lives in `ground_truth`.
- `documents` are a convenience union of query and candidate records, not an additional split.
- `input_split` and `input_doc_type` refer to the record's origin before the final combined export.
- Source balance is intentionally skewed; the largest sources dominate the benchmark.

## Citation

If you use AuthBench, cite the accompanying manuscript:

`AuthBench: A Large-Scale Multilingual Benchmark for Authorship Representation across Genres and Lengths`
