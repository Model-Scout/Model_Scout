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

# Wiki Parallel Titles (Toki Pona)

Multilingual Wikipedia article titles aligned across 20 languages via Wikidata QIDs.

## Overview

| Split | Rows |
|-------|------|
| train | 3,204 |

Each row contains the title of the same Wikipedia article in **20 languages**: tok, en, ru, uk, be, fr, es, pt, it, de, vi, ja, zh, ko, ar, he, pl, tr, la, el.

## Pipeline

1. Extracted article titles from Toki Pona Wikipedia via Wikidata sitelinks
2. Normalized: stripped disambiguation parentheticals, category prefixes, `.com` suffixes
3. Missing titles filled via translategemma-12b-it translation from English (or fallback language)
4. Cleaned: reversed "Surname, Name" patterns fixed, stress marks removed, hallucinated translations replaced

## Fields

- `qid` — Wikidata entity ID (e.g. Q868 for Aristotle)
- `tok`, `en`, `ru`, ... `el` — article title in each language
- `source` — always `wiki_titles`

## Usage

```python
from datasets import load_dataset
ds = load_dataset("NetherQuartz/tokipona-wiki-titles-mt")
```

## License

CC BY-SA 4.0 — derived from Wikipedia article titles via Wikidata. Missing translations filled by machine translation (translategemma-12b-it).
