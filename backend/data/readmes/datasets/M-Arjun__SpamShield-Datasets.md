---
license: cc-by-4.0
language:
- ar
- bn
- zh
- nl
- en
- fr
- de
- hi
- id
- it
- ja
- jv
- ko
- mr
- 'no'
- pa
- pt
- ru
- es
- sv
- tr
- uk
- ur
size_categories:
- 100K<n<1M
task_categories:
- text-classification
- token-classification
task_ids:
- text-scoring
- multi-class-classification
tags:
- spam
- ham
- multilingual
- sms
- content-moderation
- nlp
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': ham
          '1': spam
  - name: category
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_examples: 149359
configs: []
config:
  gated: true
---

<p align="center">
  <h1 align="center">🛡️ SpamShield Multilingual Training Datasets</h1>
  <p align="center">
    <a href="https://creativecommons.org/licenses/by/4.0/">
      <img src="https://img.shields.io/badge/License-CC_BY_4.0-blue?style=for-the-badge&logo=creativecommons" alt="License">
    </a>
    <a href="https://huggingface.co/datasets/M-Arjun/SpamShield-Datasets">
      <img src="https://img.shields.io/badge/🤗_Datasets-149.4K_messages-ffcc01?style=for-the-badge" alt="HF Datasets">
    </a>
    <img src="https://img.shields.io/badge/Languages-23-8A2BE2?style=for-the-badge" alt="Languages">
    <img src="https://img.shields.io/badge/Format-Parquet_+_JSONL-00C853?style=for-the-badge" alt="Format">
    <br>
    <img src="https://img.shields.io/badge/Ham-72.4K-success?style=flat-square" alt="Ham">
    <img src="https://img.shields.io/badge/Spam-76.9K-critical?style=flat-square" alt="Spam">
    <img src="https://img.shields.io/badge/Size-47_MB-informational?style=flat-square" alt="Size">
    <img src="https://img.shields.io/badge/Gated-✓-yellow?style=flat-square" alt="Gated">
  </p>
</p>

<div align="center">
  <h4>
    <a href="https://huggingface.co/M-Arjun/SpamShield">Model</a> •
    <a href="https://github.com/Arjun-M">Github</a>
  </h4>
</div>

---

## Access 
This dataset is openly available under CC-BY-4.0. 
Click "Request Access" for instant auto-approval. 

---

## 📋 Overview

**SpamShield Datasets** is a large-scale, multilingual spam detection corpus containing **149,359 messages** across **23 languages**, with balanced class distributions and consistent labeling. Designed for training robust production-grade spam classifiers, content moderation models, and multilingual NLP systems.

### Data Composition

| Source                 | Share   | Description                                                |
|:-----------------------|:--------|:-----------------------------------------------------------|
| Open-Source Corpora    | 80%     | Public spam/ham datasets, research corpora, community collections |
| Synthetic Augmentation | 20%     | Paraphrasing, translation, back-translation, leet/unicode variation |

### Use Cases

- ✅ Spam detection classifiers
- ✅ Content moderation pipelines
- ✅ Multi-class spam categorization
- ✅ Multilingual NLP & transfer learning
- ✅ Benchmarking & evaluation

---

## 📊 Dataset Stats

### Global Summary

| Metric          | Value      |
|:----------------|-----------:|
| Total messages  | **149,359** |
| Ham (normal)    | 72,439      |
| Spam            | 76,920      |
| Languages       | 23          |
| Files           | 84 (83 JSONL + 1 Parquet) |

### Category Breakdown

| Category   |   Count | % of Total |
|:-----------|--------:|-----------:|
| normal     |  72,439 |     48.50% |
| spam       |  72,313 |     48.42% |
| phishing   |     960 |      0.64% |
| crypto     |     892 |      0.60% |
| marketing  |     846 |      0.57% |
| job_scam   |     792 |      0.53% |
| giveaway   |     666 |      0.45% |
| adult      |     449 |      0.30% |
| promo      |       1 |      0.00% |
| scam       |       1 |      0.00% |

### Per-Language Composition

| Language     |   Ham |   Spam |   Total |
|:-------------|------:|-------:|--------:|
| Arabic       |   623 |    623 |   1,246 |
| Bengali      |   626 |    626 |   1,252 |
| Chinese      |   632 |    632 |   1,264 |
| Dutch        |     0 |  3,977 |   3,977 |
| English      | 59,903 | 59,202 | 119,105 |
| French       |   636 |    636 |   1,272 |
| German       |   634 |    634 |   1,268 |
| Hinglish     |   610 |    610 |   1,220 |
| Indonesian   |   635 |    635 |   1,270 |
| Italian      |     0 |  1,205 |   1,205 |
| Japanese     |   631 |    631 |   1,262 |
| Javanese     |   623 |    623 |   1,246 |
| Korean       |   632 |    632 |   1,264 |
| Marathi      |   612 |    612 |   1,224 |
| Norwegian    |   636 |    636 |   1,272 |
| Portuguese   |   636 |    636 |   1,272 |
| Punjabi      |   569 |    569 |   1,138 |
| Russian      |   636 |    636 |   1,272 |
| Spanish      |   634 |    634 |   1,268 |
| Swedish      |   635 |    635 |   1,270 |
| Turkish      |   628 |    628 |   1,256 |
| Ukrainian    |   632 |    632 |   1,264 |
| Urdu         |   636 |    636 |   1,272 |
| **Total**    | **72,439** | **76,920** | **149,359** |

> **Note:** Dutch and Italian subsets contain only spam messages (no ham samples). All other languages are approximately balanced (~50/50).

---

## 📁 Format

The dataset is available in two formats:

### JSONL (per-language files)

Each line is a JSON object with the following schema:

```json
{
  "text":     "Congratulations! You've won a free iPhone.",
  "label":    1,
  "category": "spam",
  "language": "English"
}
```

| Field      | Type   | Description                                  |
|:-----------|:-------|:---------------------------------------------|
| `text`     | `str`  | Message content                              |
| `label`    | `int`  | `0` = ham (normal), `1` = spam              |
| `category` | `str`  | Fine-grained category (10 values)            |
| `language` | `str`  | Language (23 values)                         |

### Parquet (single file)

`combined.parquet` consolidates all messages into a single **Apache Parquet** file (~47 MB, Snappy compressed). Columnar format enables fast predicate pushdown and efficient I/O in PyTorch / TensorFlow pipelines.

| Column     | Type     | Description              |
|:-----------|:---------|:-------------------------|
| `text`     | `string` | Message content          |
| `label`    | `int8`   | `0` = ham, `1` = spam    |
| `category` | `string` | Fine-grained category    |
| `language` | `string` | Language                 |

---

## 🌐 Languages

| #  | Language   | #  | Language   | #  | Language   |
|:---|:-----------|:---|:-----------|:---|:-----------|
| 1  | Arabic     | 9  | Indonesian | 17 | Portuguese |
| 2  | Bengali    | 10 | Italian    | 18 | Punjabi    |
| 3  | Chinese    | 11 | Japanese   | 19 | Russian    |
| 4  | Dutch      | 12 | Javanese   | 20 | Spanish    |
| 5  | English    | 13 | Korean     | 21 | Swedish    |
| 6  | French     | 14 | Marathi    | 22 | Turkish    |
| 7  | German     | 15 | Norwegian  | 23 | Ukrainian  |
| 8  | Hinglish   | 16 | Urdu       |    |            |

---

## 🚀 Usage

### Load Parquet (recommended)

```python
import pandas as pd

df = pd.read_parquet("SpamShield-Datasets/combined.parquet")
print(df.shape)  # (149359, 4)
```

### Load with 🤗 Datasets

```python
from datasets import load_dataset

dataset = load_dataset(
    "json",
    data_files="SpamShield-Datasets/**/clean-*.jsonl",
    split="train",
)
```

### Filter by language

```python
import pandas as pd

df = pd.read_parquet("SpamShield-Datasets/combined.parquet")
english = df[df["language"] == "English"]
print(f"English messages: {len(english)}")  # 119105
```

### Quick stats

```python
print(df["label"].value_counts())
# 1    76920
# 0    72439

print(df["language"].value_counts())
# English      119105
# Dutch          3977
# ...
```

---

## 📄 License

This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC-BY-4.0)**.

| Right                   | Granted |
|:------------------------|:--------|
| Share — copy & redistribute | ✅ |
| Adapt — remix, transform, build upon | ✅ |
| Commercial use          | ✅ |
| Attribution required    | ✅ See below |

**Attribution requirement:** You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Full license: [creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 🤝 Acknowledgments

This dataset builds upon work from the open-source community and research institutions. We acknowledge all dataset creators, annotators, and contributors who made this work possible.

---

<p align="center">
  <sub>Built with ❤️ for the open-source NLP community</sub>
</p>