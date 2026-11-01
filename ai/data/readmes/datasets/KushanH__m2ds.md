---
license: mit
language:
  - en
  - ja
  - ko
  - si
  - ta
pretty_name: M2DS
tags:
  - multilingual summarisation
  - multi-document summarisation
  - dataset
  - nlp
  - bbc
task_categories:
  - summarization
size_categories:
  - 10K<n<100K
configs:
  - config_name: english
    default: true
    data_files:
      - split: train
        path: english/train.json
      - split: validation
        path: english/validation.json
      - split: test
        path: english/test.json
  - config_name: japanese
    data_files:
      - split: train
        path: japanese/train.json
      - split: validation
        path: japanese/validation.json
      - split: test
        path: japanese/test.json
  - config_name: korean
    data_files:
      - split: train
        path: korean/train.json
      - split: validation
        path: korean/validation.json
      - split: test
        path: korean/test.json
  - config_name: sinhala
    data_files:
      - split: train
        path: sinhala/train.json
      - split: validation
        path: sinhala/validation.json
      - split: test
        path: sinhala/test.json
  - config_name: tamil
    data_files:
      - split: train
        path: tamil/train.json
      - split: validation
        path: tamil/validation.json
      - split: test
        path: tamil/test.json
---

# M2DS v1.0 — Multilingual Dataset for Multi-document Summarisation

M2DS is a multilingual multi-document summarisation dataset built from BBC news articles and
professionally written BBC summaries across five languages: English, Japanese, Korean, Sinhala,
and Tamil.

## Quick start

```python
from datasets import load_dataset

# Load a specific language
ds = load_dataset("KushanH/m2ds", "english")

# Access splits
train = ds["train"]
val   = ds["validation"]
test  = ds["test"]

# Inspect a single example
print(train[0]["document"])  # concatenated source articles
print(train[0]["summary"])   # reference summary
```

Available config names: `english`, `japanese`, `korean`, `sinhala`, `tamil`.

## Dataset structure

Each language is released as split-based files compatible with Hugging Face `load_dataset()`.

### Splits

| Split      | Purpose                  |
|------------|--------------------------|
| `train`      | Model training           |
| `validation` | Hyperparameter tuning    |
| `test`       | Final evaluation         |

### Fields

Each row represents one **multi-document cluster** and contains two fields:

| Field      | Type   | Description                                                       |
|------------|--------|-------------------------------------------------------------------|
| `document` | string | Multiple related source articles concatenated into one text field |
| `summary`  | string | Reference summary combining BBC summaries for the cluster         |

### Document separator

Within the `document` field, individual articles are separated by:

```
|||||
```

Example:

```
Article one text here... ||||| Article two text here... ||||| Article three text here...
```

## Split ratios

- English: **80 / 10 / 10**
- Japanese, Korean, Sinhala, Tamil: **90 / 5 / 5**

## Statistics

| Language  |  Train | Validation |  Test |  Total |  Paper |
|-----------|-------:|-----------:|------:|-------:|-------:|
| English   | 13,496 |      1,688 | 1,687 | 16,871 |    17K |
| Japanese  |  9,891 |        549 |   551 | 10,991 |    11K |
| Korean    |  7,021 |        391 |   390 |  7,802 |     8K |
| Sinhala   |  4,942 |        275 |   275 |  5,492 |  5.5K  |
| Tamil     |  8,916 |        495 |   496 |  9,907 |    10K |
| **Total** | **44,266** | **3,398** | **3,399** | **51,063** | **~51.5K** |

Paper-reported values are rounded per-language presentation values.

## External resources

- OSF Archive: https://osf.io/7gjtm/
- GitHub Repository: https://github.com/KushanMH/m2ds

## License

The dataset structure, preprocessing pipeline, clustering methodology, metadata, and split definitions are released under the MIT License.

M2DS is constructed from publicly available BBC news articles and professionally written BBC summaries.

Original textual content remains subject to BBC copyright and applicable source terms.

This dataset is intended for research and educational purposes.

Users are responsible for ensuring compliance with original source rights when reusing the dataset.

## Citation

If you use M2DS in your research, please cite:

```bibtex
@inproceedings{hewapathirana2024m2ds,
  title={M2DS: Multilingual Dataset for Multi-document Summarisation},
  author={Hewapathirana, Kushan and de Silva, Nisansa and Athuraliya, CD},
  booktitle={International Conference on Computational Collective Intelligence},
  pages={219--231},
  year={2024},
  organization={Springer}
}
```
