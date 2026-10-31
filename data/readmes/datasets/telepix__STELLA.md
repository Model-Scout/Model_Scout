---
pretty_name: "STELLA: Aerospace Information Retrieval Benchmark"
language:
  - en
  - ko
  - id
  - th
  - fr
  - zh
  - ja
task_categories:
  - text-retrieval
tags:
  - beir
  - aerospace
  - benchmark
license: cc-by-4.0
---
<p align="center">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/61d6f4a4d49065ee28a1ee7e/Ml2xJjQcc2Nq0baqyVIGv.png" width="400"/>
<p>

# STELLA Benchmark

STELLA is an aerospace-domain Information Retrieval (IR) benchmark constructed from NASA Technical Reports Server (NTRS) documents. It is designed to evaluate both:

- **Lexical matching** ability (does the retriever benefit from exact technical terms? | TCQ)
- **Semantic matching** ability (can the retriever match concepts even when technical terms are not explicitly used? | TAQ).

STELLA provides **dual-type synthetic queries** and a **cross-lingual extension** for multilingual evaluation while keeping the corpus in English.

<p align="center">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/61d6f4a4d49065ee28a1ee7e/V38eA6w15pN965A5wkBFw.png" width="800"/>
    <em>Overall pipeline for constructing the STELLA benchmark</em>
</p>

## Data Source & Passage Construction (High-level)

- Source: **NASA Technical Reports Server (NTRS)**.
- Filtering (at collection time): English PDF, publication year ≥ 2000, exclude non-text-centric types (e.g., video/poster), select materials that are **not under copyright**.
- Parsing: document layout detection (figures/tables excluded), then chunk into passages using Recursive-Token-Chunker with **RT100-20** (chunk size 100 tokens, overlap 20).

> Note: This repository releases the *processed passages* and evaluation files (queries/qrels) in a BEIR-compatible format.

## Statistics of Dataset

- **Corpus**: ~2.4M English passages (retrieval units)
- **Evaluation queries**: 1,000 total (500 passages × {TCQ, TAQ})
- **Languages**: English + 6 query-translation languages (ko, id, th, fr, zh, ja)

## Usage
```python
from datasets import load_dataset
from huggingface_hub import hf_hub_download

REPO_ID = "telepix/STELLA"
LANG = "en"

corpus_path = hf_hub_download(REPO_ID, "corpus.jsonl", repo_type="dataset")
queries_path = hf_hub_download(REPO_ID, f"queries_{LANG}.jsonl", repo_type="dataset")

corpus = load_dataset("json", data_files=corpus_path, split="train")
queries = load_dataset("json", data_files=queries_path, split="train")

print(corpus[300])
print(queries[300])
```

## Citation
```
@article{kim2026stella,
    title={STELLA: Self-Reflective Terminology-Aware Framework for Building an Aerospace Information Retrieval Benchmark},
    author={Bongmin Kim},
    year={2026},
    eprint={2601.03496},
    archivePrefix={arXiv},
    primaryClass={cs.IR}
}
```