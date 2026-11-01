---
license: cc-by-4.0
language:
- en
- zh
- de
- fr
- es
- it
- pt
- ja
- ko
- ar
- ru
- nl
- pl
- tr
tags:
- affiliations
- nlp
- bibliometrics
- openalex
- ner
- institution-disambiguation
- academic
- text
pretty_name: OpenAlex Affiliation Dataset
size_categories:
- 1M<n<10M
task_categories:
- token-classification
- text-classification
configs:
- config_name: "2025-12"
  data_files: "data/2025-12/*.csv"
---

# OpenAlex Affiliation Dataset

This dataset provides raw and deduplicated academic affiliation strings from scholarly works published in December 2025. Affiliation strings are the raw, author-written institutional descriptions (e.g., "Department of Computer Science, MIT, Cambridge, MA, USA") that appear in academic papers — before any normalization or entity resolution.

## What are raw affiliation strings?

Affiliation strings are the institutional descriptions authors include in their papers, before any normalization or entity resolution:

```
Department of Computer Science, Stanford University, Stanford, CA 94305, USA
Institut fur Physik, Humboldt-Universitat zu Berlin, 12489 Berlin, Germany
Faculdade de Medicina, Universidade de Sao Paulo, Sao Paulo, Brasil
```

## Use cases

- **Institution disambiguation / NER** — parse and normalize to known entities (ROR, GRID, Wikidata)
- **NLP training data** — multilingual academic text for span detection, entity linking
- **Bibliometrics** — institutional analytics, collaboration networks
- **Affiliation normalization** — training data for models like AffilGood, S2AFF

## Data source & provenance

**Source:** [OpenAlex](https://openalex.org) — fully open index of scholarly works by OurResearch. CC BY 4.0.

**Pipeline:** [labid-base/openalex-pipeline](https://github.com/labid-base/openalex-pipeline)

Each chunk is deduplicated independently. `work_id` is the first work in which each string appeared within the chunk.

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("LabID-base/OpenAlex-Afillation", "2025-12")
print(ds["train"][0])
# {"work_id": "https://openalex.org/W...", "raw_affiliation_string": "Department of..."}
```

## Dataset statistics

| Month | Collection date | Works | Total entries | Unique strings | Chunks |
|-------|----------------|-------|---------------|----------------|--------|
| 2025-12 | 2026-03-27 | 704,702 | 3,595,056 | **1,557,802** | 71 |

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `work_id` | string | OpenAlex work ID (e.g. `https://openalex.org/W2741809807`) |
| `raw_affiliation_string` | string | Raw affiliation text as written by the author |


## Directory structure

```
data/
  2025-12/
    works_2025_12_chunk_0001.csv
    ...
    works_2025_12_chunk_0071.csv   (71 chunks, ~22K strings each)
```

## Update schedule

Updated **monthly**. Each update adds a new `data/{YYYY}-{MM}/` folder.

| Release | Period | Status |
|---------|--------|--------|
| v1 | 2025-12 | Available |
| v2 | 2026-01 | Planned |

## Citation

```bibtex
@misc{priem2022openalex,
  title={OpenAlex: A fully-open index of the world's research works},
  author={Priem, Jason and Piwowar, Heather and Orr, Richard},
  year={2022},
  eprint={2205.01833},
  archivePrefix={arXiv}
}
```
