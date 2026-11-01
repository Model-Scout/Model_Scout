---
language:
- af
- ar
- az
- bn
- bs
- bg
- ca
- cs
- da
- de
- el
- en
- et
- fa
- fi
- fr
- gu
- ha
- he
- hi
- hr
- hu
- id
- it
- ja
- ka
- ko
- ku
- lv
- lt
- ml
- mr
- mk
- ms
- my
- ne
- nl
- 'no'
- pa
- pl
- pt
- ro
- ru
- si
- sk
- so
- es
- sq
- sr
- sw
- sv
- ta
- te
- tl
- th
- tr
- uk
- ur
- vi
- zh
license: cc-by-nc-sa-4.0
size_categories:
- 100K<n<1M
task_categories:
- text-classification
pretty_name: 'BLUFF: Benchmark for Linguistic Understanding of Fake-news Forensics'
tags:
- fake-news-detection
- multilingual
- misinformation
- authorship-attribution
- cross-lingual
- low-resource-languages
- benchmark
---

# BLUFF: Benchmark for Linguistic Understanding of Fake-news Forensics

**BLUFF** is a comprehensive multilingual benchmark for fake news detection spanning **79 languages** with over **202K samples**. It uniquely covers both high-resource "big-head" (20) and low-resource "long-tail" (59) languages, addressing critical gaps in multilingual disinformation research.

- **Paper:** [BLUFF: Benchmarking the Detection of False and Synthetic Content across 58 Low-Resource Languages](https://huggingface.co/papers/2603.00634)
- **Project Page:** [jsl5710.github.io/BLUFF](https://jsl5710.github.io/BLUFF/)
- **GitHub:** [github.com/jsl5710/BLUFF](https://github.com/jsl5710/BLUFF)
- **Authors:** Jason Lucas, Matt Murtagh-White, Adaku Uchendu, Ali Al-Lawati, Michiharu Yamashita, Dominik Macko, Ivan Srba, Robert Moro, Dongwon Lee

---

## Key Features

- **79 Languages** across 12 language families, 10 script types, and 4 syntactic orders.
- **202K+ Samples** combining human-written (122K) and LLM-generated (79K) content.
- **4 Content Types:** Human-Written (HWT), Machine-Generated (MGT), Machine-Translated (MTT), and Human-AI Hybrid (HAT).
- **39 Textual Modification Techniques:** 36 manipulation tactics for fake news + 3 AI-editing strategies for real news.
- **19 Diverse mLLMs** used for content generation.
- **4 Benchmark Tasks** with standardized train/val/test splits.

---

## Dataset Structure

This repository is organized into four main directories:

```
data/
├── meta_data/                          # Metadata for all samples
│   ├── metadata_human_written.csv    #   Human-written sample metadata (122K rows)
│   └── metadata_ai_generated.csv     #   AI-generated sample metadata (78K rows)
│
├── processed/                          # Cleaned, extracted text data (ready to use)
│   └── generated_data/
│       ├── ai_generated/             #   Per-model, per-language CSV files
│       └── human_written/            #   Per-organization, per-language CSV files
│
├── raw/                                # Original source data before processing
│   └── source_data/
│       ├── human/                    #   Raw human-written fact-check articles
│       ├── sd_eng_x_f/               #   Source data: English→X, fake news
│       ├── sd_eng_x_r/               #   Source data: English→X, real news
│       ├── sd_x_eng_f/               #   Source data: X→English, fake news
│       └── sd_x_eng_r/               #   Source data: X→English, real news
│
└── splits/                             # Evaluation split definitions (train + val only)
    └── evaluation/
        ├── multilingual/             #   Train on all languages
        ├── cross_lingual_bighead_longtail/  #  Train big-head, eval long-tail
        ├── cross_lingual_family/     #   Per language family (14 families)
        ├── cross_lingual_script/     #   Per script type (11 scripts)
        ├── cross_lingual_syntax/     #   Per syntactic word order (4 types)
        └── external_evaluation/      #   Held-out external dataset evaluation
```

> **Note:** Test splits are held out to preserve benchmark integrity. Only `train.json`, `val.json`, and `stats.json` are provided in each split directory. To evaluate on the test set, please contact the authors.

---

## Benchmark Tasks

| Task | Description | Classes | Metric |
|------|-------------|---------|--------|
| **Task 1** | Binary Veracity Classification | Real / Fake | F1 (macro) |
| **Task 2** | Multi-class Veracity Classification | Real / Fake × Source Type | F1 (macro) |
| **Task 3** | Binary Authorship Detection | Human / Machine | F1 (macro) |
| **Task 4** | Multi-class Authorship Attribution | HWT / MGT / MTT / HAT | F1 (macro) |

---

## Sample Usage

### Download Specific Files

```python
from huggingface_hub import hf_hub_download

# Download metadata
meta_path = hf_hub_download(
    repo_id="jsl5710/BLUFF",
    repo_type="dataset",
    filename="data/meta_data/metadata_ai_generated.csv"
)

# Download processed data for a specific model and language
data_path = hf_hub_download(
    repo_id="jsl5710/BLUFF",
    repo_type="dataset",
    filename="data/processed/generated_data/ai_generated/gpt-4.1/eng/data.csv"
)
```

### Download Entire Dataset

```python
from huggingface_hub import snapshot_download

# Download everything (~3.9 GB)
snapshot_download(
    repo_id="jsl5710/BLUFF",
    repo_type="dataset",
    local_dir="./BLUFF_data"
)
```

### Building a Training Dataset

```python
import json
import pandas as pd
from huggingface_hub import hf_hub_download

# 1. Load split definition (e.g., multilingual training)
split_path = hf_hub_download("jsl5710/BLUFF", "data/splits/evaluation/multilingual/train.json", repo_type="dataset")
with open(split_path) as f:
    train_uuids = set(json.load(f))

# 2. Load metadata
meta_path = hf_hub_download("jsl5710/BLUFF", "data/meta_data/metadata_ai_generated.csv", repo_type="dataset")
meta_ai = pd.read_csv(meta_path)

# 3. Filter to training split
train_ai = meta_ai[meta_ai["uuid"].isin(train_uuids)]
print(f"Training samples - AI generated: {len(train_ai)}")
```

---

## Ethical Considerations

BLUFF contains realistic synthetic disinformation created solely for research purposes. By accessing this dataset, you agree to:

1. Use the data solely for research aimed at improving disinformation detection
2. Not redistribute generated fake news content outside research contexts
3. Cite the dataset in any publications using BLUFF
4. Report any misuse discovered to the authors

All generated content includes metadata identifying it as synthetic research material.

---

## Citation

Paper currently under review. Citation will be provided upon acceptance.

---

## License

- **Code:** [MIT License](https://github.com/jsl5710/BLUFF/blob/main/LICENSE)
- **Dataset:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)