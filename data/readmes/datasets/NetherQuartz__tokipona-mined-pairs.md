---
language:
- tok
- en
- ru
- uk
- be
- fr
- es
- pt
- it
- de
- vi
- ja
- zh
- ko
- ar
- he
- pl
- tr
- la
- el
license: cc-by-sa-4.0
task_categories:
- translation
- sentence-similarity
size_categories:
- 100K<n<1M
---

# Wiki Mined Pairs (Toki Pona)

Sentence-level parallel pairs between Toki Pona and 19 other languages, mined from Wikipedia using [LaBSE-tokipona](https://huggingface.co/NetherQuartz/LaBSE-tokipona).

## Overview

| Split | Rows |
|-------|------|
| train | 163,583 |
| validation | 8,748 |

Each row is a **tok - one other language** pair (not all 20 languages at once).

## Mining method

Two-stage margin-based bitext mining with mutual nearest neighbors:
1. **Stage 1**: Paragraph alignment (margin score threshold >= 1.02)
2. **Stage 2**: Sentence alignment within matched paragraphs (threshold >= 1.04)

Source: ~3,475 Toki Pona Wikipedia articles and their counterparts in 19 languages. No machine translation involved — all texts are original Wikipedia content.

## Fields

- `qid` — Wikidata entity ID of the source article
- `lang` — target language code (e.g. `en`, `ru`, `ja`)
- `tok` — Toki Pona sentence
- `text` — sentence in the target language
- `score` — margin-based similarity score (higher = better alignment)

## Usage

```python
from datasets import load_dataset
ds = load_dataset("NetherQuartz/tokipona-mined-pairs")

# Filter for a specific language
en_pairs = ds["train"].filter(lambda x: x["lang"] == "en")
```

## Split method

Deterministic 95/5 train/validation split by MD5 hash of the Toki Pona text.

## License

CC BY-SA 4.0 — all data sourced from Wikipedia articles.
