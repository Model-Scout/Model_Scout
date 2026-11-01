---
dataset_info:
  features:
  - name: wiki_pageid
    dtype: int64
  - name: language
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  - name: aligned_id
    dtype: int64
  - name: id
    dtype: string
  splits:
  - name: en
    num_bytes: 243235861
    num_examples: 11527
  - name: de
    num_bytes: 140373196
    num_examples: 11527
  - name: hi
    num_bytes: 86822617
    num_examples: 11527
  - name: it
    num_bytes: 104469518
    num_examples: 11527
  - name: ko
    num_bytes: 51282982
    num_examples: 11527
  - name: zh
    num_bytes: 71778569
    num_examples: 11527
  download_size: 388267378
  dataset_size: 697962743
configs:
- config_name: default
  data_files:
  - split: en
    path: data/en-*
  - split: de
    path: data/de-*
  - split: hi
    path: data/hi-*
  - split: it
    path: data/it-*
  - split: ko
    path: data/ko-*
  - split: zh
    path: data/zh-*
pretty_name: Multilingual Wikipedia Comparable Corpus (6 languages)
language:
- en
- de
- hi
- it
- ko
- zh
tags:
- wikipedia
- multilingual
- comparable-corpus
- document-alignment
size_categories:
- 10K<n<100K
---


# Multilingual Wikipedia Comparable Corpus (en, de, it, ko, hi, zh)

This dataset is a **document-level comparable corpus** of Wikipedia articles across **6 languages**: English (`en`), German (`de`), Italian (`it`), Korean (`ko`), Hindi (`hi`), and Chinese (`zh`).

The key property is **alignment across languages**: entries are topic-matched such that, for a given index `i`, `dataset["en"][i]` is comparable to `dataset["de"][i]`, `dataset["it"][i]`, … (and likewise via the `aligned_id` field).

## Dataset structure

The dataset loads as a `DatasetDict` with one split per language:

- `en`: 11,527 rows  
- `de`: 11,527 rows  
- `hi`: 11,527 rows  
- `it`: 11,527 rows  
- `ko`: 11,527 rows  
- `zh`: 11,527 rows  

**Aligned article groups:** 11,527  
**Total articles:** 11,527 × 6 = 69,162

## Columns / features

Each language split has the same schema:

- `wiki_pageid` *(int)*: Wikipedia page ID (curid) of the article in that language edition.
- `language` *(string)*: Language code (`en`, `de`, `it`, `ko`, `hi`, `zh`).
- `url` *(string)*: Canonical Wikipedia URL for the article.
- `title` *(string)*: Article title.
- `text` *(string)*: Article text.
- `aligned_id` *(int)*: Alignment group identifier shared across languages.
- `id` *(string)*: Language-specific identifier. (Can be used together with `aligned_id` / row index for alignment.)

### Alignment guarantee (how to join)
Articles are aligned across splits in two equivalent ways:

1. **By row index**: for any `i`, the examples across all language splits at index `i` are aligned/comparable.
2. **By `aligned_id`**: examples that share the same `aligned_id` are aligned/comparable across languages.

### Reconstruct Wikipedia curid
You can reconstruct a stable Wikipedia “curid” link from wiki_pageid: https://{language_code}.wikipedia.org/wiki/?curid={wiki_pageid}
- e.g. https://de.wikipedia.org/wiki/?curid=6679205

## Example

Example entry from the German split (`de`):
```python
{
  "wiki_pageid": 6679205,
  "language": "de",
  "url": "https://de.wikipedia.org/wiki/.in",
  "title": ".in",
  "text": ".in ist die länderspezifische Top-Level-Domain (ccTLD) Indiens. Sie wurde am 8. Mai 1989 ...",
  "aligned_id": 3,
  "id": "2de"
}
```

### Citation

If you use this dataset, please cite it using the following BibTeX entry:

```bibtex
@misc{schuhmacher2026informationrepresentationfairnesslongdocument,
      title={Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias}, 
      author={Elias Schuhmacher and Andrianos Michail and Juri Opitz and Rico Sennrich and Simon Clematide},
      year={2026},
      eprint={2601.16934},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2601.16934}, 
}