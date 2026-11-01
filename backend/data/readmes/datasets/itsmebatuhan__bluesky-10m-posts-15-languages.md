---
license: cc-by-nc-sa-4.0
language:
  - en
  - tr
  - es
  - pt
  - de
  - fr
  - ja
  - it
  - nl
  - pl
  - ru
  - ko
  - zh
  - ar
  - hi
task_categories:
  - text-classification
  - text-generation
  - fill-mask
tags:
  - social-media
  - multilingual
  - bluesky
  - nlp
  - sentiment-analysis
  - text-classification
  - language-modeling
  - large-scale
  - text-data
  - posts
  - microblog
  - jsonl
  - firehose
pretty_name: Bluesky 10M Multilingual Posts (15 Languages)
size_categories:
  - 10M<n<100M
---

# Dataset Card: Bluesky 10M Multilingual

## 📊 Overview

- **Total Posts:** 10,099,990
- **Languages:** 15 (en, tr, es, pt, de, fr, ja, it, nl, pl, ru, ko, zh, ar, hi)
- **Collection Period:** August 9-12, 2026
- **Source:** Bluesky Jetstream API (public firehose)
- **Format:** JSONL
- **Size:** ~3 GB

## 🌍 Language Distribution

| Language | Code | Posts | % |
|----------|------|-------|---|
| English | en | 6,843,995 | 67.8% |
| Japanese | ja | 1,547,179 | 15.3% |
| German | de | 373,626 | 3.7% |
| Portuguese | pt | 331,093 | 3.3% |
| Spanish | es | 325,865 | 3.2% |
| French | fr | 206,852 | 2.0% |
| Korean | ko | 171,704 | 1.7% |
| Dutch | nl | 90,198 | 0.9% |
| Turkish | tr | 59,949 | 0.6% |
| Italian | it | 45,348 | 0.4% |
| Russian | ru | 27,892 | 0.3% |
| Chinese | zh | 26,695 | 0.3% |
| Polish | pl | 24,793 | 0.2% |
| Arabic | ar | 24,451 | 0.2% |
| Hindi | hi | 360 | 0.0% |

*Distribution reflects natural Bluesky demographics.*

## 📁 Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `did` | string | Decentralized user identifier |
| `rkey` | string | Record key (unique post ID) |
| `text` | string | Post content |
| `lang` | string | Primary language code |
| `created_at` | string | Post timestamp (ISO 8601) |
| `collected_at` | string | Collection timestamp |
| `is_reply` | bool | Whether post is a reply (optional) |

## 💻 Usage

```python
from datasets import load_dataset

# Load dataset
ds = load_dataset("itsmebatuhan/bluesky-10m-posts-15-languages", split="train")

# Access data
print(ds[0])
print(ds["lang"].value_counts())

Streaming (for large datasets)
ds = load_dataset("itsmebatuhan/bluesky-10m-posts-15-languages", streaming=True)
for sample in ds["train"]:
    print(sample["text"])
    break

📌 Citation
@dataset{bluesky_10m_multilingual_2026,
  title = {Bluesky 10M Multilingual Posts (15 Languages)},
  author = {itsmebatuhan},
  year = {2026},
  url = {https://huggingface.co/datasets/itsmebatuhan/bluesky-10m-posts-15-languages}
}