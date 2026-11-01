---
license: apache-2.0
task_categories:
- text-retrieval
language:
- ar
- de
- en
- es
- fa
- fi
- fr
- hi
- id
- ja
- ko
- ru
- te
- th
- zh
tags:
- mteb
- retrieval
- multilingual
- miracl
- hard-negatives
pretty_name: MIRACL Hard Negatives (Parquet)
size_categories:
- 1M<n<10M
default_config_name: ko-queries
configs:
- config_name: ar
  data_files:
  - split: dev
    path: ar/*.parquet
- config_name: corpus-ar
  data_files:
  - split: corpus
    path: corpus-ar/*.parquet
- config_name: queries-ar
  data_files:
  - split: queries
    path: queries-ar/*.parquet
- config_name: de
  data_files:
  - split: dev
    path: de/*.parquet
- config_name: corpus-de
  data_files:
  - split: corpus
    path: corpus-de/*.parquet
- config_name: queries-de
  data_files:
  - split: queries
    path: queries-de/*.parquet
- config_name: en
  data_files:
  - split: dev
    path: en/*.parquet
- config_name: corpus-en
  data_files:
  - split: corpus
    path: corpus-en/*.parquet
- config_name: queries-en
  data_files:
  - split: queries
    path: queries-en/*.parquet
- config_name: es
  data_files:
  - split: dev
    path: es/*.parquet
- config_name: corpus-es
  data_files:
  - split: corpus
    path: corpus-es/*.parquet
- config_name: queries-es
  data_files:
  - split: queries
    path: queries-es/*.parquet
- config_name: fa
  data_files:
  - split: dev
    path: fa/*.parquet
- config_name: corpus-fa
  data_files:
  - split: corpus
    path: corpus-fa/*.parquet
- config_name: queries-fa
  data_files:
  - split: queries
    path: queries-fa/*.parquet
- config_name: fi
  data_files:
  - split: dev
    path: fi/*.parquet
- config_name: corpus-fi
  data_files:
  - split: corpus
    path: corpus-fi/*.parquet
- config_name: queries-fi
  data_files:
  - split: queries
    path: queries-fi/*.parquet
- config_name: fr
  data_files:
  - split: dev
    path: fr/*.parquet
- config_name: corpus-fr
  data_files:
  - split: corpus
    path: corpus-fr/*.parquet
- config_name: queries-fr
  data_files:
  - split: queries
    path: queries-fr/*.parquet
- config_name: hi
  data_files:
  - split: dev
    path: hi/*.parquet
- config_name: corpus-hi
  data_files:
  - split: corpus
    path: corpus-hi/*.parquet
- config_name: queries-hi
  data_files:
  - split: queries
    path: queries-hi/*.parquet
- config_name: id
  data_files:
  - split: dev
    path: id/*.parquet
- config_name: corpus-id
  data_files:
  - split: corpus
    path: corpus-id/*.parquet
- config_name: queries-id
  data_files:
  - split: queries
    path: queries-id/*.parquet
- config_name: ja
  data_files:
  - split: dev
    path: ja/*.parquet
- config_name: corpus-ja
  data_files:
  - split: corpus
    path: corpus-ja/*.parquet
- config_name: queries-ja
  data_files:
  - split: queries
    path: queries-ja/*.parquet
- config_name: ko
  data_files:
  - split: dev
    path: ko/*.parquet
- config_name: corpus-ko
  data_files:
  - split: corpus
    path: corpus-ko/*.parquet
- config_name: queries-ko
  data_files:
  - split: queries
    path: queries-ko/*.parquet
- config_name: ru
  data_files:
  - split: dev
    path: ru/*.parquet
- config_name: corpus-ru
  data_files:
  - split: corpus
    path: corpus-ru/*.parquet
- config_name: queries-ru
  data_files:
  - split: queries
    path: queries-ru/*.parquet
- config_name: te
  data_files:
  - split: dev
    path: te/*.parquet
- config_name: corpus-te
  data_files:
  - split: corpus
    path: corpus-te/*.parquet
- config_name: queries-te
  data_files:
  - split: queries
    path: queries-te/*.parquet
- config_name: th
  data_files:
  - split: dev
    path: th/*.parquet
- config_name: corpus-th
  data_files:
  - split: corpus
    path: corpus-th/*.parquet
- config_name: queries-th
  data_files:
  - split: queries
    path: queries-th/*.parquet
- config_name: zh
  data_files:
  - split: dev
    path: zh/*.parquet
- config_name: corpus-zh
  data_files:
  - split: corpus
    path: corpus-zh/*.parquet
- config_name: queries-zh
  data_files:
  - split: queries
    path: queries-zh/*.parquet
---

# MIRACL Hard Negatives (Parquet Format)

This is a Parquet-converted version of [mteb/miracl-hard-negatives](https://huggingface.co/datasets/mteb/miracl-hard-negatives), compatible with the latest HuggingFace `datasets` library (4.0+).

## Why This Dataset?

The original `mteb/miracl-hard-negatives` uses a Python script-based loader, which is no longer supported in `datasets >= 4.0.0`. This dataset provides the same data in standard Parquet format.

## Dataset Description

MIRACL (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual retrieval dataset that focuses on search across 18 different languages.

The **hard negatives** version was created by pooling the top 250 documents per query from:
- BM25
- e5-multilingual-large
- e5-mistral-instruct

This makes the retrieval task more challenging compared to the standard MIRACL dataset.

## Languages

| Code | Language |
|------|----------|
| ar | Arabic |
| de | German |
| en | English |
| es | Spanish |
| fa | Persian |
| fi | Finnish |
| fr | French |
| hi | Hindi |
| id | Indonesian |
| ja | Japanese |
| ko | Korean |
| ru | Russian |
| te | Telugu |
| th | Thai |
| zh | Chinese |

## Usage

```python
from datasets import load_dataset

# Load English data (original config naming convention)
corpus = load_dataset("datalama/miracl-hard-negatives", "corpus-en", split="corpus")
queries = load_dataset("datalama/miracl-hard-negatives", "queries-en", split="queries")
qrels = load_dataset("datalama/miracl-hard-negatives", "en", split="dev")

print(f"Corpus: {len(corpus)} documents")
print(f"Queries: {len(queries)} queries")
print(f"Qrels: {len(qrels)} relevance judgments")
```

## Data Format

### Queries (`queries-{lang}`)
| Column | Type | Description |
|--------|------|-------------|
| `_id` | string | Query ID |
| `text` | string | Query text |

### Corpus (`corpus-{lang}`)
| Column | Type | Description |
|--------|------|-------------|
| `_id` | string | Document ID |
| `title` | string | Document title |
| `text` | string | Document text |

### Qrels (`{lang}`)
| Column | Type | Description |
|--------|------|-------------|
| `query-id` | string | Query ID |
| `corpus-id` | string | Document ID |
| `score` | int | Relevance score |

## Citation

```bibtex
@article{zhang2022miracl,
  title={MIRACL: A Multilingual Retrieval Dataset Covering 18 Diverse Languages},
  author={Zhang, Xinyu and Thakur, Nandan and Ogundepo, Odunayo and Kamalloo, Ehsan and Alfonso-Hermelo, David and Li, Xiaoguang and Liu, Qun and Rezagholizadeh, Mehdi and Lin, Jimmy},
  journal={arXiv preprint arXiv:2210.09984},
  year={2022}
}
```

## License

Apache 2.0 (same as the original dataset)

## Acknowledgments

- Original dataset: [mteb/miracl-hard-negatives](https://huggingface.co/datasets/mteb/miracl-hard-negatives)
- MIRACL benchmark: [miracl.ai](http://miracl.ai/)
- MTEB benchmark: [mteb](https://huggingface.co/mteb)
