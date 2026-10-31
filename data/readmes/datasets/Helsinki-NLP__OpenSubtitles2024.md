---
license: odc-by
pretty_name: OpenSubtitles2024 Bilingual Benchmark
task_categories:
- translation
language:
- ar
- az
- be
- bg
- bn
- bs
- ca
- cs
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- gl
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ka
- kk
- km
- kn
- ko
- ku
- lt
- lv
- mk
- ml
- mn
- ms
- my
- nl
- no
- pl
- ps
- pt
- ro
- ru
- si
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- te
- tl
- tr
- tt
- uk
- ur
- uz
- vi
- yue
tags:
- machine-translation
- subtitles
- multilingual
- evaluation
- opus
- opensubtitles
size_categories:
- 100M<n<1B
configs:
- config_name: default
  data_files:
  - split: validation
    path: dev/*/*.parquet
  - split: test
    path: test/*/*.parquet
---
# OpenSubtitles2024 Bilingual Benchmark

## Dataset Summary

This dataset is a bilingual held-out evaluation and development benchmark derived from the **OpenSubtitles2024** corpus.

It contains sentence-aligned subtitle pairs for machine translation development and evaluation. Unlike the multilingual aligned subset of OpenSubtitles2024, this dataset is **not multi-parallel**: different language pairs may originate from different movies or TV episodes, and aligned sentence pairs are organized independently for each bilingual direction.

The dataset was constructed as part of the OpenSubtitles2024 benchmark suite for evaluating multilingual and bilingual machine translation systems.

Key properties:

- Held-out year: **2024**
- Total languages: **70**
- Total language pairs (test): **2022**
- Total language pairs (validation): **1786**
- Structure: **pairwise bilingual subtitle alignments**
- Domain: **movie and TV subtitles**

The dataset is intended for **development and evaluation**, not for training large language models or machine translation systems.

---

# Dataset Description

## Source

The data originates from community-contributed subtitles available on **OpenSubtitles.org**, distributed through the **OPUS** corpus collection.

OpenSubtitles2024 extends previous OpenSubtitles releases with broader language coverage and a substantially larger aligned subtitle collection.

For benchmark construction, subtitles associated with **movies and TV episodes released in 2024** were withheld from the training corpus and reserved exclusively for development and evaluation.

This dataset is derived from that **held-out 2024 subtitle pool**.

---

# Bilingual Benchmark Construction

The bilingual benchmark was created to support standard **pairwise machine translation evaluation**.

## Test split

The **test set** contains high-quality bilingual subtitle alignments selected from the held-out 2024 subtitle pool.

For each supported language pair:

- up to **5 movies or TV episodes** were selected
- subtitle alignments had to satisfy an **alignment density â‰¥ 0.8**
- selections prioritize the **highest alignment quality**

Because selections are performed **independently for each language pair**, the resulting dataset is **not multi-parallel**.

Test set statistics:

- **Language pairs:** 2022
- **Languages:** 70

Supported languages:

```

['ar', 'az', 'be', 'bg', 'bn', 'bs', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'es_419', 'es_ES', 'et', 'eu', 'fa', 'fi', 'fr', 'gl', 'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'lt', 'lv', 'mk', 'ml', 'mn', 'ms', 'my', 'nl', 'no', 'pl', 'ps', 'pt', 'pt_BR', 'pt_MZ', 'ro', 'ru', 'si', 'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'tl', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi', 'yue', 'zh_CN', 'zh_TW']

```

---

## Validation split

The **validation split** (stored as `dev/` in the repository) contains additional high-quality subtitle alignments from the same held-out 2024 pool that were **not selected for the test split**.

This split is intended for:

- development
- hyperparameter tuning
- model selection

Validation set statistics:

- **Language pairs:** 1786
- **Languages:** 67

Supported languages:

```

['ar', 'az', 'be', 'bg', 'bn', 'bs', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'es_419', 'es_ES', 'et', 'eu', 'fa', 'fi', 'fr', 'gl', 'he', 'hi', 'hr', 'hu', 'id', 'is', 'it', 'ka', 'kk', 'kn', 'ko', 'ku', 'lt', 'lv', 'mk', 'ml', 'mn', 'ms', 'my', 'nl', 'no', 'pl', 'pt', 'pt_BR', 'pt_MZ', 'ro', 'ru', 'si', 'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'tl', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi', 'yue', 'zh_CN', 'zh_TW']

```

---

# Dataset Structure

Each record corresponds to one aligned subtitle pair.

## Data Fields

| Field | Type | Description |
|------|------|-------------|
| `src_text` | string | Source subtitle segment |
| `tgt_text` | string | Target subtitle segment |
| `src_lang` | string | Source language code |
| `tgt_lang` | string | Target language code |

## Example

```json
{
  "src_text": "Where are you going?",
  "tgt_text": "Minne olet menossa?",
  "src_lang": "en",
  "tgt_lang": "fi"
}
```



## Hugging Face Loading Options

This repository supports two loading modes:

1. **Default parquet mode (no remote code):**

```python
from datasets import load_dataset

validation_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="validation",
)
test_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="test",
)
# validation -> repo folder dev/, test -> repo folder test/
```

2. **Filtered mode with dataset script (requires remote code trust):**

```python
from datasets import load_dataset

# Single language pair (order-insensitive), validation split
validation_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="validation",
    trust_remote_code=True,
    language_pairs="zh_CN-en",
)

# Multiple language pairs, test split
test_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="test",
    trust_remote_code=True,
    language_pairs=["en-fi", "ar-zh_CN"],
)

# Single language: keep all pairs that contain this language
validation_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="validation",
    trust_remote_code=True,
    languages="zh_CN",
)

# Multiple languages: keep all pairs that contain any of them
test_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="test",
    trust_remote_code=True,
    languages=["en", "zh_CN", "yue"],
)

# Combine both filters (intersection)
validation_ds = load_dataset(
    "Helsinki-NLP/OpenSubtitles2024",
    split="validation",
    trust_remote_code=True,
    language_pairs=["en-zh_CN", "en-fi"],
    languages=["en", "zh_CN"],
)
```

---

# Alignment Method

Subtitle alignment primarily relies on **timestamp overlap** between subtitle segments.

The OpenSubtitles2024 pipeline includes several additional steps:

* subtitle normalization
* language identification
* sentence segmentation
* subtitle synchronization using lexical anchor points
* filtering based on alignment density and quality criteria

---

# Intended Uses

This dataset is intended for:

* bilingual machine translation evaluation
* multilingual MT evaluation across pairwise directions
* multilingual language model benchmarking
* model development using held-out subtitle data

Users should **not train models directly on this dataset** if they intend to report benchmark results on it.

---

## Limitations

Users should be aware of several limitations:

* **Noise and inconsistencies:** Subtitles may contain translation errors or stylistic variations.
* **Informal domain:** The data reflects conversational movie dialogue and may not generalize to formal text domains.
* **Segment alignment variability:** Subtitle segmentation may differ across languages, which can introduce minor inconsistencies.
* **Non-parallel structure:** Different language pairs may come from different movies or episodes, meaning the dataset is **not fully aligned across languages**.

---

# Licensing

This dataset is released under the **ODC-BY license**. The dataset redistributes subtitle texts originally contributed to OpenSubtitles.org. The authors do not claim ownership of the subtitle content and maintain a takedown policy for copyright holders.

---

# Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{tiedemann-luo-2026-opensubtitles2024,
  title={OpenSubtitles2024: A Massively Parallel Dataset of Movie Subtitles for MT Development and Evaluation},
  author={Tiedemann, Jörg and Luo, Hengyu},
  booktitle={Proceedings of the 15th edition of the Language Resources and Evaluation Conference (LREC 2026)},
  year={2026}
}
```

---

# Acknowledgements

This work was supported by the European Union's Horizon Europe research and innovation programme under grant agreement No 101070350, by the OpenEuroLLM project, co-funded by the Digital Europe Programme under GA no. 101195233, and by the AI-DOC program hosted at the Finnish Center of Artificial Intelligence (decision number VN/3137/2024-OKM-6). 
The authors wish to also thank CSC - IT Center for Science, Finland, and LUMI supercomputers, owned by the EuroHPC Joint Undertaking, for providing computational resources.
