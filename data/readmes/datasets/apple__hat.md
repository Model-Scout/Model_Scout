---
license: cc-by-nc-nd-4.0
pretty_name: "HAT: Hallucination Annotation for Translation"
size_categories:
  - 100K<n<1M
annotations_creators:
  - expert-generated
task_categories:
  - translation
  - text-classification
language:
  - ar
  - nl
  - en
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - pl
  - pt
  - ru
  - zh
  - es
  - th
  - tr
  - uk
  - vi
tags:
  - machine-translation
  - hallucination-detection
  - mt-evaluation
configs:
  - config_name: default
    data_files:
      - {split: train, path: "data/train/*/*.parquet"}
      - {split: validation, path: "data/dev/*/*.parquet"}
      - {split: test, path: "data/test/*/*.parquet"}
  - config_name: ar_AE-en_US
    data_files:
      - {split: train, path: "data/train/ar_AE-en_US/*.parquet"}
      - {split: validation, path: "data/dev/ar_AE-en_US/*.parquet"}
      - {split: test, path: "data/test/ar_AE-en_US/*.parquet"}
  - config_name: de_DE-en_US
    data_files:
      - {split: train, path: "data/train/de_DE-en_US/*.parquet"}
      - {split: validation, path: "data/dev/de_DE-en_US/*.parquet"}
      - {split: test, path: "data/test/de_DE-en_US/*.parquet"}
  - config_name: en_US-ar_AE
    data_files:
      - {split: train, path: "data/train/en_US-ar_AE/*.parquet"}
      - {split: validation, path: "data/dev/en_US-ar_AE/*.parquet"}
      - {split: test, path: "data/test/en_US-ar_AE/*.parquet"}
  - config_name: en_US-de_DE
    data_files:
      - {split: train, path: "data/train/en_US-de_DE/*.parquet"}
      - {split: validation, path: "data/dev/en_US-de_DE/*.parquet"}
      - {split: test, path: "data/test/en_US-de_DE/*.parquet"}
  - config_name: en_US-es_ES
    data_files:
      - {split: train, path: "data/train/en_US-es_ES/*.parquet"}
      - {split: validation, path: "data/dev/en_US-es_ES/*.parquet"}
      - {split: test, path: "data/test/en_US-es_ES/*.parquet"}
  - config_name: en_US-fr_FR
    data_files:
      - {split: train, path: "data/train/en_US-fr_FR/*.parquet"}
      - {split: validation, path: "data/dev/en_US-fr_FR/*.parquet"}
      - {split: test, path: "data/test/en_US-fr_FR/*.parquet"}
  - config_name: en_US-hi_IN
    data_files:
      - {split: train, path: "data/train/en_US-hi_IN/*.parquet"}
      - {split: validation, path: "data/dev/en_US-hi_IN/*.parquet"}
      - {split: test, path: "data/test/en_US-hi_IN/*.parquet"}
  - config_name: en_US-id_ID
    data_files:
      - {split: train, path: "data/train/en_US-id_ID/*.parquet"}
      - {split: validation, path: "data/dev/en_US-id_ID/*.parquet"}
      - {split: test, path: "data/test/en_US-id_ID/*.parquet"}
  - config_name: en_US-it_IT
    data_files:
      - {split: train, path: "data/train/en_US-it_IT/*.parquet"}
      - {split: validation, path: "data/dev/en_US-it_IT/*.parquet"}
      - {split: test, path: "data/test/en_US-it_IT/*.parquet"}
  - config_name: en_US-ja_JP
    data_files:
      - {split: train, path: "data/train/en_US-ja_JP/*.parquet"}
      - {split: validation, path: "data/dev/en_US-ja_JP/*.parquet"}
      - {split: test, path: "data/test/en_US-ja_JP/*.parquet"}
  - config_name: en_US-ko_KR
    data_files:
      - {split: train, path: "data/train/en_US-ko_KR/*.parquet"}
      - {split: validation, path: "data/dev/en_US-ko_KR/*.parquet"}
      - {split: test, path: "data/test/en_US-ko_KR/*.parquet"}
  - config_name: en_US-nl_NL
    data_files:
      - {split: train, path: "data/train/en_US-nl_NL/*.parquet"}
      - {split: validation, path: "data/dev/en_US-nl_NL/*.parquet"}
      - {split: test, path: "data/test/en_US-nl_NL/*.parquet"}
  - config_name: en_US-pl_PL
    data_files:
      - {split: train, path: "data/train/en_US-pl_PL/*.parquet"}
      - {split: validation, path: "data/dev/en_US-pl_PL/*.parquet"}
      - {split: test, path: "data/test/en_US-pl_PL/*.parquet"}
  - config_name: en_US-pt_BR
    data_files:
      - {split: train, path: "data/train/en_US-pt_BR/*.parquet"}
      - {split: validation, path: "data/dev/en_US-pt_BR/*.parquet"}
      - {split: test, path: "data/test/en_US-pt_BR/*.parquet"}
  - config_name: en_US-ru_RU
    data_files:
      - {split: train, path: "data/train/en_US-ru_RU/*.parquet"}
      - {split: validation, path: "data/dev/en_US-ru_RU/*.parquet"}
      - {split: test, path: "data/test/en_US-ru_RU/*.parquet"}
  - config_name: en_US-th_TH
    data_files:
      - {split: train, path: "data/train/en_US-th_TH/*.parquet"}
      - {split: validation, path: "data/dev/en_US-th_TH/*.parquet"}
      - {split: test, path: "data/test/en_US-th_TH/*.parquet"}
  - config_name: en_US-tr_TR
    data_files:
      - {split: train, path: "data/train/en_US-tr_TR/*.parquet"}
      - {split: validation, path: "data/dev/en_US-tr_TR/*.parquet"}
      - {split: test, path: "data/test/en_US-tr_TR/*.parquet"}
  - config_name: en_US-uk_UA
    data_files:
      - {split: train, path: "data/train/en_US-uk_UA/*.parquet"}
      - {split: validation, path: "data/dev/en_US-uk_UA/*.parquet"}
      - {split: test, path: "data/test/en_US-uk_UA/*.parquet"}
  - config_name: en_US-vi_VN
    data_files:
      - {split: train, path: "data/train/en_US-vi_VN/*.parquet"}
      - {split: validation, path: "data/dev/en_US-vi_VN/*.parquet"}
      - {split: test, path: "data/test/en_US-vi_VN/*.parquet"}
  - config_name: en_US-zh_CN
    data_files:
      - {split: train, path: "data/train/en_US-zh_CN/*.parquet"}
      - {split: validation, path: "data/dev/en_US-zh_CN/*.parquet"}
      - {split: test, path: "data/test/en_US-zh_CN/*.parquet"}
  - config_name: en_US-zh_TW
    data_files:
      - {split: train, path: "data/train/en_US-zh_TW/*.parquet"}
      - {split: validation, path: "data/dev/en_US-zh_TW/*.parquet"}
      - {split: test, path: "data/test/en_US-zh_TW/*.parquet"}
  - config_name: es_ES-en_US
    data_files:
      - {split: train, path: "data/train/es_ES-en_US/*.parquet"}
      - {split: validation, path: "data/dev/es_ES-en_US/*.parquet"}
      - {split: test, path: "data/test/es_ES-en_US/*.parquet"}
  - config_name: fr_FR-en_US
    data_files:
      - {split: train, path: "data/train/fr_FR-en_US/*.parquet"}
      - {split: validation, path: "data/dev/fr_FR-en_US/*.parquet"}
      - {split: test, path: "data/test/fr_FR-en_US/*.parquet"}
  - config_name: hi_IN-en_US
    data_files:
      - {split: train, path: "data/train/hi_IN-en_US/*.parquet"}
      - {split: validation, path: "data/dev/hi_IN-en_US/*.parquet"}
      - {split: test, path: "data/test/hi_IN-en_US/*.parquet"}
  - config_name: id_ID-en_US
    data_files:
      - {split: train, path: "data/train/id_ID-en_US/*.parquet"}
      - {split: validation, path: "data/dev/id_ID-en_US/*.parquet"}
      - {split: test, path: "data/test/id_ID-en_US/*.parquet"}
  - config_name: it_IT-en_US
    data_files:
      - {split: train, path: "data/train/it_IT-en_US/*.parquet"}
      - {split: validation, path: "data/dev/it_IT-en_US/*.parquet"}
      - {split: test, path: "data/test/it_IT-en_US/*.parquet"}
  - config_name: ja_JP-en_US
    data_files:
      - {split: train, path: "data/train/ja_JP-en_US/*.parquet"}
      - {split: validation, path: "data/dev/ja_JP-en_US/*.parquet"}
      - {split: test, path: "data/test/ja_JP-en_US/*.parquet"}
  - config_name: ko_KR-en_US
    data_files:
      - {split: train, path: "data/train/ko_KR-en_US/*.parquet"}
      - {split: validation, path: "data/dev/ko_KR-en_US/*.parquet"}
      - {split: test, path: "data/test/ko_KR-en_US/*.parquet"}
  - config_name: nl_NL-en_US
    data_files:
      - {split: train, path: "data/train/nl_NL-en_US/*.parquet"}
      - {split: validation, path: "data/dev/nl_NL-en_US/*.parquet"}
      - {split: test, path: "data/test/nl_NL-en_US/*.parquet"}
  - config_name: pl_PL-en_US
    data_files:
      - {split: train, path: "data/train/pl_PL-en_US/*.parquet"}
      - {split: validation, path: "data/dev/pl_PL-en_US/*.parquet"}
      - {split: test, path: "data/test/pl_PL-en_US/*.parquet"}
  - config_name: pt_BR-en_US
    data_files:
      - {split: train, path: "data/train/pt_BR-en_US/*.parquet"}
      - {split: validation, path: "data/dev/pt_BR-en_US/*.parquet"}
      - {split: test, path: "data/test/pt_BR-en_US/*.parquet"}
  - config_name: ru_RU-en_US
    data_files:
      - {split: train, path: "data/train/ru_RU-en_US/*.parquet"}
      - {split: validation, path: "data/dev/ru_RU-en_US/*.parquet"}
      - {split: test, path: "data/test/ru_RU-en_US/*.parquet"}
  - config_name: th_TH-en_US
    data_files:
      - {split: train, path: "data/train/th_TH-en_US/*.parquet"}
      - {split: validation, path: "data/dev/th_TH-en_US/*.parquet"}
      - {split: test, path: "data/test/th_TH-en_US/*.parquet"}
  - config_name: tr_TR-en_US
    data_files:
      - {split: train, path: "data/train/tr_TR-en_US/*.parquet"}
      - {split: validation, path: "data/dev/tr_TR-en_US/*.parquet"}
      - {split: test, path: "data/test/tr_TR-en_US/*.parquet"}
  - config_name: uk_UA-en_US
    data_files:
      - {split: train, path: "data/train/uk_UA-en_US/*.parquet"}
      - {split: validation, path: "data/dev/uk_UA-en_US/*.parquet"}
      - {split: test, path: "data/test/uk_UA-en_US/*.parquet"}
  - config_name: vi_VN-en_US
    data_files:
      - {split: train, path: "data/train/vi_VN-en_US/*.parquet"}
      - {split: validation, path: "data/dev/vi_VN-en_US/*.parquet"}
      - {split: test, path: "data/test/vi_VN-en_US/*.parquet"}
  - config_name: zh_CN-en_US
    data_files:
      - {split: train, path: "data/train/zh_CN-en_US/*.parquet"}
      - {split: validation, path: "data/dev/zh_CN-en_US/*.parquet"}
      - {split: test, path: "data/test/zh_CN-en_US/*.parquet"}
  - config_name: zh_TW-en_US
    data_files:
      - {split: train, path: "data/train/zh_TW-en_US/*.parquet"}
      - {split: validation, path: "data/dev/zh_TW-en_US/*.parquet"}
      - {split: test, path: "data/test/zh_TW-en_US/*.parquet"}
---

# HAT: Hallucination Annotation for Translation


## 🧭 Table of Contents
- [Overview](#-overview)
- [Usage](#-usage)
- [Data Creation Process](#-data-creation-process)
- [Data Statistics](#-data-statistics)
- [Dataset Structure](#-dataset-structure)
- [Paper Abstract](#-paper-abstract)
- [Citation](#-citation)
- [License](#-license)

---

## 📘 Overview
**HAT (Hallucination Annotation for Translation)** is a large-scale dataset for **hallucination detection in machine translation (MT)**.  
It is released as part of our publication at ACL 2026 ([paper](https://aclanthology.org/2026.acl-long.721.pdf)).

- **350,959 span-level annotated samples**  
- **38 language pairs**  
- **~8,000-10,000 samples per language pair**, divided into **train**, **dev**, and **test** sets  
- **Annotations** by professional translators under strict **quality control**  

HAT enables research on detecting and mitigating hallucinations in MT systems.

---

## 🚀 Usage
Load the dataset with the 🤗 [`datasets`](https://huggingface.co/docs/datasets) library:

```python
from datasets import load_dataset

# All 38 language pairs
ds = load_dataset("apple/hat")
train, validation, test = ds["train"], ds["validation"], ds["test"]

# A single language pair (e.g. English → Japanese)
ds = load_dataset("apple/hat", "en_US-ja_JP")
```

The available config names are the 38 language pairs (e.g. `en_US-ja_JP`, `fr_FR-en_US`); the
default config concatenates all pairs. Each config exposes `train`, `validation`, and `test` splits.

---

## ⚙️ Data Creation Process
The dataset was created through the following steps:

1. **Data Collection:**  
   Crawled ~5M sentences per language from the web, filtered by language ID, length, and deduplication.

2. **Translation:**  
   Translated monolingual sentences into target languages using a strong neural MT model.

3. **Sample Selection:**  
   Selected translations with lower quality (based on quality metrics) to increase the likelihood of hallucinations.

4. **Annotation:**  
   Professional translators labeled hallucinations under rigorous quality control.

5. **Post-processing:**  
   Removed samples with issues in source text to ensure data integrity.

---

## 📊 Data Statistics

| Split | Samples per language pair |
|--------|----------------------------|
| **Train** | ~10,000 |
| **Dev** | ~2,000 |
| **Test** | ~3,000 |

---

## 📂 Dataset Structure
Datasets are organized in the [`data/`](data/) directory:
```
data/
├── train/
├── dev/
└── test/
```
Each split contains subdirectories for each language pair which contains one parquet file.

> **Split naming:** the parquet files live under `data/train`, `data/dev`, and `data/test`.
> On the Hugging Face Hub the `dev` files are exposed as the standard `validation` split, so
> `load_dataset(...)` returns `train` / `validation` / `test`.

**Schema:**

| Field | Type | Description |
|--------|------|-------------|
| `source_locale` | `string` | Locale of the source text |
| `source_text` | `string` | Source sentence |
| `target_locale` | `string` | Locale of the target text |
| `target_text` | `string` | Machine-translated output |
| `split` | `string` | Dataset split (`train` / `dev` / `test`) |
| `label` | `int64` | Binary hallucination label (`0`: no hallucination, `1`: contains hallucination) |
| `score` | `float64` | Proportion (0–1) of hallucinated characters |
| `annotation` | `string` | Raw span-level hallucination annotation |


## 📄 Paper Abstract
Hallucinations in machine translation (MT)—outputs that may be fluent yet unfaithful to the source content—remain a critical obstacle. They hinder the reliable deployment of MT systems in real-world applications. Despite growing attention to this phenomenon, progress has been constrained by the lack of large-scale, high-quality benchmarks dedicated to hallucination detection. We introduce HAT (Hallucination Annotation for Translation), a novel dataset designed to advance research on this problem. HAT comprises 350,959 span-level annotated samples across 38 language pairs, with approximately 8,000–10,000 samples per pair partitioned into training, development, and test sets. Annotations were produced by professional translators under rigorous quality control protocols to ensure reliability. We provide a detailed analysis of hallucination distributions and establish benchmark performance using a diverse set of baselines, including automatic MT evaluation metrics as well as large language models. By providing the first large-scale, systematically annotated resource for hallucination detection in MT, HAT enables the development of more faithful translation models and lays the groundwork for future research on building trustworthy machine translation systems.

## 📚 Citation
If you use this dataset, please cite:

```bibtex
@inproceedings{chatterjee-etal-2026-hat,
    title = "{HAT}: Hallucination Annotation for Translation",
    author = "Chatterjee, Rajen  and
      Li, Xintong  and
      Charoenpornsawat, Paisarn  and
      Lee, Allen",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.721/",
    pages = "15865--15888",
    ISBN = "979-8-89176-390-6",
}
```

## 📄 License
The HAT dataset is licensed under CC BY-NC-ND 4.0 (https://creativecommons.org/licenses/by-nc-nd/4.0/).