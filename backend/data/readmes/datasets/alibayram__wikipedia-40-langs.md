---
dataset_info:
  features:
  - name: lang
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 3836023771
    num_examples: 580000
  - name: validation
    num_bytes: 950087892
    num_examples: 174000
  - name: test
    num_bytes: 295565016
    num_examples: 58000
  download_size: 2779866648
  dataset_size: 5081676679
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
license: cc-by-sa-4.0
language:
- ar
- bg
- ca
- ce
- cs
- cy
- da
- de
- el
- en
- eo
- es
- eu
- fa
- fi
- fr
- he
- hu
- hy
- id
- it
- ja
- ko
- ms
- nl
- no
- pl
- pt
- ro
- ru
- sh
- tr
- tt
- uz
- vi
- zh
size_categories:
- 100K<n<1M
task_categories:
- text-generation
- fill-mask
tags:
- wikipedia
- multilingual
- nlp
- language-modeling
- text-corpus
pretty_name: Wikipedia 40 Languages
---

# Wikipedia 40 Languages

A curated multilingual dataset of Wikipedia articles spanning **40 languages** with **812,000 articles** total. Designed for multilingual NLP research, language modeling, and cross-lingual transfer learning.

## Dataset Summary

This dataset contains Wikipedia articles from 40 languages, sampled and split into train/validation/test sets with a consistent 10:3:1 ratio per language. English and Turkish are overrepresented (10x more samples) to support focused training scenarios, while the remaining 38 languages each contribute equally.

| Property | Value |
|---|---|
| **Total articles** | 812,000 |
| **Languages** | 40 |
| **Download size** | 2.78 GB |
| **Dataset size** | 5.08 GB |
| **License** | CC BY-SA 4.0 (Wikipedia) |

## Splits

| Split | Examples | Size |
|---|---|---|
| `train` | 580,000 | 3.84 GB |
| `validation` | 174,000 | 0.95 GB |
| `test` | 58,000 | 0.30 GB |

Split ratio is **10:3:1** (train:validation:test), applied consistently per language.

## Features

| Feature | Type | Description |
|---|---|---|
| `lang` | `string` | ISO 639 language code (e.g., `en`, `tr`, `ja`) |
| `title` | `string` | Wikipedia article title |
| `text` | `string` | Full article text content |
| `url` | `string` | Original Wikipedia article URL |

## Language Distribution

The dataset covers 40 languages. English (`en`) and Turkish (`tr`) each have **10x** the samples of other languages.

| Code | Language | Train | Validation | Test | Total |
|---|---|---|---|---|---|
| `en` | English | 100,000 | 30,000 | 10,000 | **140,000** |
| `tr` | Turkish | 100,000 | 30,000 | 10,000 | **140,000** |
| `ar` | Arabic | 10,000 | 3,000 | 1,000 | 14,000 |
| `arz` | Egyptian Arabic | 10,000 | 3,000 | 1,000 | 14,000 |
| `bg` | Bulgarian | 10,000 | 3,000 | 1,000 | 14,000 |
| `ca` | Catalan | 10,000 | 3,000 | 1,000 | 14,000 |
| `ce` | Chechen | 10,000 | 3,000 | 1,000 | 14,000 |
| `ceb` | Cebuano | 10,000 | 3,000 | 1,000 | 14,000 |
| `cs` | Czech | 10,000 | 3,000 | 1,000 | 14,000 |
| `cy` | Welsh | 10,000 | 3,000 | 1,000 | 14,000 |
| `da` | Danish | 10,000 | 3,000 | 1,000 | 14,000 |
| `de` | German | 10,000 | 3,000 | 1,000 | 14,000 |
| `el` | Greek | 10,000 | 3,000 | 1,000 | 14,000 |
| `eo` | Esperanto | 10,000 | 3,000 | 1,000 | 14,000 |
| `es` | Spanish | 10,000 | 3,000 | 1,000 | 14,000 |
| `eu` | Basque | 10,000 | 3,000 | 1,000 | 14,000 |
| `fa` | Persian | 10,000 | 3,000 | 1,000 | 14,000 |
| `fi` | Finnish | 10,000 | 3,000 | 1,000 | 14,000 |
| `fr` | French | 10,000 | 3,000 | 1,000 | 14,000 |
| `he` | Hebrew | 10,000 | 3,000 | 1,000 | 14,000 |
| `hu` | Hungarian | 10,000 | 3,000 | 1,000 | 14,000 |
| `hy` | Armenian | 10,000 | 3,000 | 1,000 | 14,000 |
| `id` | Indonesian | 10,000 | 3,000 | 1,000 | 14,000 |
| `it` | Italian | 10,000 | 3,000 | 1,000 | 14,000 |
| `ja` | Japanese | 10,000 | 3,000 | 1,000 | 14,000 |
| `ko` | Korean | 10,000 | 3,000 | 1,000 | 14,000 |
| `ms` | Malay | 10,000 | 3,000 | 1,000 | 14,000 |
| `nl` | Dutch | 10,000 | 3,000 | 1,000 | 14,000 |
| `no` | Norwegian | 10,000 | 3,000 | 1,000 | 14,000 |
| `pl` | Polish | 10,000 | 3,000 | 1,000 | 14,000 |
| `pt` | Portuguese | 10,000 | 3,000 | 1,000 | 14,000 |
| `ro` | Romanian | 10,000 | 3,000 | 1,000 | 14,000 |
| `ru` | Russian | 10,000 | 3,000 | 1,000 | 14,000 |
| `sh` | Serbo-Croatian | 10,000 | 3,000 | 1,000 | 14,000 |
| `simple` | Simple English | 10,000 | 3,000 | 1,000 | 14,000 |
| `tt` | Tatar | 10,000 | 3,000 | 1,000 | 14,000 |
| `uz` | Uzbek | 10,000 | 3,000 | 1,000 | 14,000 |
| `vi` | Vietnamese | 10,000 | 3,000 | 1,000 | 14,000 |
| `war` | Waray | 10,000 | 3,000 | 1,000 | 14,000 |
| `zh` | Chinese | 10,000 | 3,000 | 1,000 | 14,000 |

### Script Families Covered

The dataset spans multiple writing systems:

- **Latin**: en, tr, ca, ceb, cs, cy, da, de, eo, es, eu, fi, fr, hu, id, it, ms, nl, no, pl, pt, ro, sh, simple, uz, vi, war
- **Cyrillic**: bg, ce, ru, tt
- **Arabic**: ar, arz, fa
- **CJK**: ja, ko, zh
- **Armenian**: hy
- **Greek**: el
- **Hebrew**: he

## Text Statistics (Train Split)

| Statistic | Value |
|---|---|
| **Min length** | 1 character |
| **Max length** | 518,241 characters |
| **Mean length** | 5,292 characters |
| **Median length** | 1,585 characters |
| **Std deviation** | 11,275 characters |

The distribution is heavily right-skewed: 98.8% of articles are under 51,826 characters, with a long tail of very lengthy articles.

## Usage

### Loading with Hugging Face Datasets

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("alibayram/wikipedia-40-langs")

# Load a specific split
train = load_dataset("alibayram/wikipedia-40-langs", split="train")

# Filter by language
turkish_articles = train.filter(lambda x: x["lang"] == "tr")
english_articles = train.filter(lambda x: x["lang"] == "en")

# Stream for memory efficiency
streamed = load_dataset("alibayram/wikipedia-40-langs", split="train", streaming=True)
```

### Example Data Point

```json
{
  "lang": "en",
  "title": "Machine learning",
  "text": "Machine learning (ML) is a field of study in artificial intelligence...",
  "url": "https://en.wikipedia.org/wiki/Machine_learning"
}
```

## Use Cases

- **Multilingual language modeling**: Pre-train or fine-tune language models across 40 languages
- **Cross-lingual transfer learning**: Evaluate how knowledge transfers between languages
- **Machine translation**: Use parallel topics across languages for indirect supervision
- **Text classification**: Train multilingual classifiers with language-balanced data
- **Information retrieval**: Build multilingual search and retrieval systems
- **Script-diverse NLP**: Study model behavior across Latin, Cyrillic, Arabic, CJK, and other scripts

## Dataset Creation

### Source

All articles are sourced from [Wikipedia](https://www.wikipedia.org/), the free encyclopedia. Each article's original URL is preserved in the `url` field for traceability.

### Sampling Strategy

- **English and Turkish**: 100,000 articles each in the train split (oversampled for focused training)
- **Other 38 languages**: 10,000 articles each in the train split
- **Split ratio**: A consistent 10:3:1 ratio (train:validation:test) is maintained across all languages

### Processing

Articles contain the full text content extracted from Wikipedia. The text field preserves the article body without markup.

## Limitations and Biases

- **Wikipedia coverage bias**: Languages with larger Wikipedia editions may have higher-quality or more diverse articles. Smaller Wikipedias (e.g., Chechen, Waray) may contain more bot-generated or stub articles.
- **Temporal snapshot**: The dataset represents Wikipedia at a specific point in time and does not reflect subsequent edits.
- **Content bias**: Wikipedia has known biases in topic coverage (e.g., overrepresentation of Western-centric topics, gender imbalance in biographies).
- **Uneven language oversampling**: English and Turkish have 10x more samples, which may bias multilingual models toward these languages if not accounted for during training.
- **No deduplication guarantees**: Some articles may contain near-duplicate content (e.g., bot-generated geographic articles across languages).

## License

The dataset inherits Wikipedia's [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Citation

```bibtex
@dataset{wikipedia_40_langs,
  title={Wikipedia 40 Languages},
  author={Ali Bayram},
  year={2026},
  url={https://huggingface.co/datasets/alibayram/wikipedia-40-langs},
  license={CC BY-SA 4.0}
}
```
