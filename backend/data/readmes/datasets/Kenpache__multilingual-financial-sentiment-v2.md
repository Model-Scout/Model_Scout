---
language:
- ar
- de
- en
- es
- fr
- hi
- ja
- ko
- pt
- zh
license: cc-by-nc-4.0
task_categories:
- text-classification
task_ids:
- sentiment-classification
tags:
- finance
- financial-sentiment
- multilingual
- perspective-aware
- news-headlines
- xlm-roberta
- sentiment-analysis
- financial-news
size_categories:
- 100K<n<1M
pretty_name: "FLAME — Perspective-Aware Multilingual Financial Sentiment"
dataset_info:
  features:
    - name: sentence
      dtype: string
    - name: label
      dtype: string
    - name: source
      dtype: string
    - name: language
      dtype: string
---

# FLAME — Perspective-Aware Multilingual Financial Sentiment Dataset

> **v2** · 145,637 headlines · 10 languages · Noise-cleaned

## What makes this dataset unique

Standard financial sentiment datasets label from a single "global investor" perspective.
**FLAME labels from the LOCAL INVESTOR perspective** of each language's primary economy.

This means **the same news event gets different labels** depending on the language/market:

| Headline | Arabic (Gulf) | Hindi (India) | English (US) |
|----------|:-------------:|:-------------:|:------------:|
| "OPEC+ increases oil production by 206,000 bpd" | ❌ **negative** | ✅ **positive** | ✅ **positive** |
| "Oil prices fall to $65 per barrel" | ❌ **negative** | ✅ **positive** | ✅ **positive** |
| "Yen weakens to 155 per dollar" | ➖ **neutral** | ➖ **neutral** | ➖ **neutral** |
| "Yen weakens to 155 per dollar" *(Japanese dataset)* | — | — | ✅ **positive** (helps exporters) |

## Dataset at a glance

| | |
|---|---|
| **Languages** | 10 (AR, DE, EN, ES, FR, HI, JA, KO, PT, ZH) |
| **Total samples** | 145,637 |
| **Labels** | negative / neutral / positive |
| **Source** | Financial news headlines (2024–2026) |
| **Noise filtering** | Applied — non-financial content removed |
| **Split strategy** | Group split by source domain (no data leakage) |

## Language distribution

| Language | Code | Economy Type | Oil Role | Samples | Neg% | Neu% | Pos% |
|----------|------|-------------|----------|---------|------|------|------|
| Arabic | ar | Gulf/Arab | **Exporter** | 14,481 | 19.1 | 43.4 | 37.5 |
| German | de | Germany/Eurozone | Importer | 14,680 | 23.6 | 44.2 | 32.1 |
| English | en | US/Global | Mixed | 15,000 | 20.6 | 51.0 | 28.4 |
| Spanish | es | Spain/LatAm | Importer | 13,984 | 25.8 | 37.4 | 36.7 |
| French | fr | France/Eurozone | Importer | 15,000 | 21.5 | 41.7 | 30.2 |
| Hindi | hi | India | Importer | 15,000 | 23.6 | 39.3 | 37.0 |
| Japanese | ja | Japan | Importer | 14,519 | 23.1 | 39.3 | 37.5 |
| Korean | ko | South Korea | Importer | 13,969 | 21.9 | 44.3 | 33.7 |
| Portuguese | pt | Brazil/Portugal | **Exporter** | 14,149 | 21.1 | 49.8 | 29.1 |
| Chinese | zh | China | Importer | 14,855 | 23.6 | 27.0 | 49.4 |
| **Total** | | | | **145,637** | **22.4** | **41.7** | **35.2** |

## Quick start

```python
from datasets import load_dataset
import pandas as pd

# Load full dataset
dataset = load_dataset("Kenpache/perspective-aware-financial-sentiment")
df = dataset["train"].to_pandas()

# Filter by language
ar_df = df[df["language"] == "ar"]   # Arabic — Gulf/Arab perspective
hi_df = df[df["language"] == "hi"]   # Hindi — Indian perspective
en_df = df[df["language"] == "en"]   # English — US/Global perspective

# Perspective-aware example: same oil event, opposite labels
oil_ar = ar_df[ar_df["sentence"].str.contains("oil|نفط", case=False, na=False)]
oil_hi = hi_df[hi_df["sentence"].str.contains("oil|तेल", case=False, na=False)]
```

## Use with the FLAME2 model

```python
from transformers import pipeline

# Load the perspective-aware model
classifier = pipeline(
    "text-classification",
    model="Kenpache/perspective-aware-financial-sentiment"
)

# Same event — different perspectives
headline_oil_drop = "Oil prices fall sharply to $60 per barrel"

print(classifier(f"[AR] {headline_oil_drop}"))  # → NEGATIVE (Arab exporter)
print(classifier(f"[HI] {headline_oil_drop}"))  # → POSITIVE (India importer)
print(classifier(f"[EN] {headline_oil_drop}"))  # → POSITIVE (US consumer)
```

## Data format

Each CSV file contains 4 columns:

| Column | Type | Description |
|--------|------|-------------|
| `sentence` | string | Financial news headline |
| `label` | string | `negative` / `neutral` / `positive` |
| `source` | string | Source URL |
| `language` | string | ISO 639-1 language code |

## Perspective-aware labeling rules

### Oil price rules

| Market | Oil price ↑ | Oil price ↓ | OPEC+ cuts | OPEC+ increases |
|--------|:-----------:|:-----------:|:----------:|:---------------:|
| **Arab (ar)** — Exporter | ✅ positive | ❌ negative | ✅ positive | ❌ negative |
| **Brazil/PT (pt)** — Exporter | ✅ positive | ❌ negative | ✅ positive | ❌ negative |
| **India/Korea/Japan/etc.** — Importer | ❌ negative | ✅ positive | ❌ negative | ✅ positive |
| **US (en)** — Mixed | depends | ✅ positive | ❌ negative | ✅ positive |

### Central bank rules

- **Home central bank rate cut** → ✅ positive (stimulative)
- **Home central bank rate hike** → ❌ negative (restrictive)
- **Foreign central bank action** → ➖ neutral (by default)

## Models trained on this dataset

| Model | Base | Accuracy | F1 Macro |
|-------|------|:--------:|:--------:|
| [perspective-aware-financial-sentiment](https://huggingface.co/Kenpache/perspective-aware-financial-sentiment) | XLM-RoBERTa-large | 84.11% | 84.20% |

## Comparison with v1

| | v1 | **v2 (this)** |
|--|:--:|:--:|
| Languages | 7 | **10** |
| Samples | 39,829 | **145,637** |
| Noise filtered | partial | **yes** |
| Perspective-aware | partial | **full** |
| Source-domain split | no | **yes** |

## License

**CC BY-NC 4.0** — Free for academic and non-commercial research.
Original headline texts remain copyright of respective publishers.
Commercial use requires licenses from original news sources.

For commercial use, you must obtain licenses from original sources directly.

If you are a rights holder and want content removed, open an issue or
email alisterclrouli@gmail.com — we will remove within 48h.

## Citation

```bibtex
@dataset{perspective_aware_financial_sentiment_2026,
  title     = {FLAME: Perspective-Aware Multilingual Financial Sentiment Dataset},
  author    = {Zaraki},
  year      = {2026},
  version   = {2.0},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/datasets/Kenpache/perspective-aware-financial-sentiment}
}
```
