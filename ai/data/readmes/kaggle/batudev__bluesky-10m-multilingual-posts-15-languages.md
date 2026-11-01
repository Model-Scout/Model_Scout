# Bluesky 10M Multilingual Posts (15 Languages)

10+ million public posts from Bluesky across 15 languages for NLP research

# 🦋 Bluesky 10M Multilingual Posts

A large-scale collection of **10,099,990 public posts** from Bluesky, spanning **15 languages**. This dataset captures organic, real-world social media conversations and is ideal for NLP research, sentiment analysis, language modeling, and cross-lingual studies.

---

## 📊 Dataset Overview

| Attribute | Details |
|-----------|---------|
| **Total Posts** | 10,099,990 |
| **Languages** | 15 |
| **Format** | JSONL |
| **Size** | ~3 GB |
| **Time Period** | August 2026 |

---

## 🌍 Language Distribution

| Language | Code | Posts | Share |
|----------|:----:|------:|------:|
| English | `en` | 6,843,995 | 67.8% |
| Japanese | `ja` | 1,547,179 | 15.3% |
| German | `de` | 373,626 | 3.7% |
| Portuguese | `pt` | 331,093 | 3.3% |
| Spanish | `es` | 325,865 | 3.2% |
| French | `fr` | 206,852 | 2.0% |
| Korean | `ko` | 171,704 | 1.7% |
| Dutch | `nl` | 90,198 | 0.9% |
| Turkish | `tr` | 59,949 | 0.6% |
| Italian | `it` | 45,348 | 0.4% |
| Russian | `ru` | 27,892 | 0.3% |
| Chinese | `zh` | 26,695 | 0.3% |
| Polish | `pl` | 24,793 | 0.2% |
| Arabic | `ar` | 24,451 | 0.2% |
| Hindi | `hi` | 360 | <0.1% |

> *The distribution reflects the natural language demographics of the Bluesky platform.*

---

## 📁 Data Fields

Each line in the JSONL file represents a single post with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `did` | string | Decentralized identifier of the author (pseudonymous) |
| `rkey` | string | Unique record key for the post |
| `text` | string | The full text content of the post |
| `lang` | string | Primary language code (ISO 639-1) |
| `created_at` | string | Post creation timestamp (ISO 8601) |
| `collected_at` | string | Collection timestamp (ISO 8601) |
| `is_reply` | boolean | Whether the post is a reply *(optional field)* |

---

## 💻 Usage Examples

### Load with Pandas
```python
import pandas as pd

df = pd.read_json("bluesky_10M_clean.jsonl", lines=True)
print(df.shape)
print(df.head())

출처: Kaggle (batudev/bluesky-10m-multilingual-posts-15-languages)
태그: nlp, text mining, classification, deep learning, multilingual
라이선스: CC BY-NC-SA 4.0
수정일: 2026-08-12T19:59:13.613Z
