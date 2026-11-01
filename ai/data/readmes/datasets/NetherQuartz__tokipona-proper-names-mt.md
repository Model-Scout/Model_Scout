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
size_categories:
- 1K<n<10K
---

# Proper Noun Patterns (Toki Pona)

Template-generated multilingual sentences for teaching Toki Pona proper noun conventions (tokiponization).

## Overview

| Split | Rows |
|-------|------|
| train | 6,440 |

Covers **10 categories** of proper nouns: jan (people), ma (countries), ma tomo (cities), toki (languages), kulupu (organizations), musi (games), sitelen (scripts/shows), ilo (tools), telo (water bodies), nena (mountains).

Each proper noun from Toki Pona Wikipedia titles is used in **2-3 different sentence templates**.

## Fields

- `tok`, `en`, `ru`, ... `el` — parallel sentence in each language
- `pattern` — the Toki Pona sentence template used (e.g. `{name} li pona tawa mi.`)
- `category` — proper noun category (e.g. `jan`, `ma tomo`, `toki`)
- `source` — always `proper_noun_pattern`

## Example

| Field | Value |
|-------|-------|
| tok | `jan Alitotele li pali e ijo mute.` |
| en | `Aristotle did many things.` |
| ru | `Аристотель сделал много вещей.` |
| ja | `アリストテレスは多くのことを成し遂げました。` |
| pattern | `{name} li pali e ijo mute.` |
| category | `jan` |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("NetherQuartz/tokipona-proper-names-mt")
```

## License

CC BY-SA 4.0 — proper nouns from Toki Pona Wikipedia titles, sentence templates filled and translated by machine translation (translategemma-12b-it).
