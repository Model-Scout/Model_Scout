---
license: cc-by-4.0
language:
- ko
- en
- es
- pt
- ja
- zh
- id
- vi
- de
- fr
- th
size_categories:
- 10K<n<100K
task_categories:
- translation
- text-classification
- feature-extraction
tags:
- korean
- vocabulary
- language-learning
- k-pop
- k-drama
- multilingual
- parallel-corpus
pretty_name: Koko Korean 5K — Multilingual Vocabulary Dataset
configs:
- config_name: en
  data_files: words.en.jsonl
- config_name: es
  data_files: words.es.jsonl
- config_name: pt-BR
  data_files: words.pt-BR.jsonl
- config_name: ja
  data_files: words.ja.jsonl
- config_name: zh-TW
  data_files: words.zh-TW.jsonl
- config_name: id
  data_files: words.id.jsonl
- config_name: vi
  data_files: words.vi.jsonl
- config_name: de
  data_files: words.de.jsonl
- config_name: fr
  data_files: words.fr.jsonl
- config_name: th
  data_files: words.th.jsonl
---

# Koko Korean 5K — Multilingual Vocabulary Dataset

5,000 carefully curated Korean vocabulary entries with English translations,
romanization, contextual usage notes, and example sentences. Each entry is
also translated into **9 additional languages**, giving researchers and
developers a high-quality parallel corpus of **50,000 aligned vocabulary
records** anchored to Korean.

The dataset reflects real conversation patterns from K-dramas, K-pop, and
everyday Korean — not textbook-only material — making it especially useful
for training language models and apps that target modern, casual Korean.

## Languages

| Code | Language |
|---|---|
| `en` | English (source) |
| `es` | Spanish |
| `pt-BR` | Portuguese (Brazilian) |
| `ja` | Japanese |
| `zh-TW` | Chinese (Traditional) |
| `id` | Indonesian |
| `vi` | Vietnamese |
| `de` | German |
| `fr` | French |
| `th` | Thai |

Korean (`ko`) is present in every record as `korean_term`, `romanization`,
and `example_sentence_korean`.

## Use cases

- Train Korean language models (vocabulary acquisition, masked LM, translation)
- Build vocabulary apps and flashcard tools
- Linguistic research on Korean honorifics, romanization, and word categorization
- Translation quality evaluation across 10 target languages
- Cross-lingual retrieval and embedding benchmarks

## Data fields

Every record across every language file shares the same schema:

| Field | Type | Description |
|---|---|---|
| `slug` | string | URL-safe identifier (stable across all languages) |
| `english_term` | string | English meaning (or translated meaning in non-EN files) |
| `korean_term` | string | Korean (Hangul) text |
| `romanization` | string | Revised Romanization |
| `context_description` | string | Cultural and usage context |
| `example_sentence_korean` | string | Korean example sentence |
| `example_sentence_english` | string | English (or translated) gloss for the example |
| `difficulty` | string | `Beginner` / `Intermediate` / `Advanced` |
| `category` | string | Topic (Emotions, Greetings, Food, K-pop, etc.) |

The `slug` is consistent across all 10 language files, which lets you join
records by `slug` to assemble parallel multilingual rows.

## Quick start

```python
from datasets import load_dataset

# Load just the English source
ds = load_dataset("jaylee8864/korean-vocabulary-5000", "en")
print(ds["train"][0])

# Load Japanese version
ds_ja = load_dataset("jaylee8864/korean-vocabulary-5000", "ja")
```

Or load raw JSONL directly:
```python
import json
with open("words.en.jsonl") as f:
    rows = [json.loads(line) for line in f]
```

## Categories

Records cover ~80 categories including: Greetings, Emotions, Food, K-pop,
K-drama Expressions, Travel, Shopping, Work, Family, Slang, Idioms, Numbers,
Body Parts, Weather, Honorifics, and more.

## Source & live demo

Curated and audio-paired by **[Koko AI](https://kokoai.im)** — an AI-powered
Korean conversation tutor. Each vocabulary entry has native pronunciation
audio (TTS) and a dedicated learning page on the site.

Browse the full dataset with audio at **[kokoai.im/word](https://kokoai.im/word)**.

## License

**CC BY 4.0** — free to use commercially or non-commercially with attribution
to [kokoai.im](https://kokoai.im).

## Citation

```bibtex
@dataset{koko_korean_5k_2026,
  author    = {Koko AI},
  title     = {Koko Korean 5K — Multilingual Vocabulary Dataset},
  year      = {2026},
  url       = {https://huggingface.co/datasets/jaylee8864/korean-vocabulary-5000},
  homepage  = {https://kokoai.im}
}
```
