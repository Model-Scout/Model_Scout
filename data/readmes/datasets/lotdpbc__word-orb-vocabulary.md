---
license: cc-by-nc-sa-4.0
task_categories:
  - text-classification
  - text-generation
  - translation
  - question-answering
language:
  - en
  - es
  - fr
  - de
  - pt
  - ja
  - ko
  - zh
  - ar
  - hi
  - ru
  - it
  - nl
  - tr
  - vi
  - th
  - pl
  - id
  - sv
  - da
  - no
  - fi
  - cs
  - ro
  - hu
  - el
  - uk
  - he
  - bn
  - ta
  - ms
  - tl
  - te
  - sw
  - ur
  - fa
  - ig
  - am
  - yo
  - my
  - zu
  - ha
  - km
  - kk
  - gu
  - ca
  - mr
  - pa
tags:
  - vocabulary
  - education
  - multilingual
  - ethics
  - nlp
  - linguistics
  - pronunciation
  - etymology
  - age-appropriate
  - cultural-sensitivity
  - gender-equity
  - dictionary
  - word-enrichment
pretty_name: Word Orb Vocabulary Intelligence
size_categories:
  - 100K<n<1M
---

# Word Orb Vocabulary Intelligence

Structured vocabulary intelligence for AI agents, educators, and researchers. 162,253 words with pronunciation, etymology, age-appropriate definitions, translations across 47 languages, and ethical context.

## Dataset Description

Word Orb is the world's most comprehensive structured vocabulary dataset designed for AI agents and education technology. Each word entry includes:

- **IPA pronunciation** for text-to-speech and phonetics research
- **Age-appropriate definitions** (child, adult, elder) for differentiated instruction
- **Etymology** tracing word origins across languages
- **Translations** across up to 47 languages with native pronunciations
- **Semantic connections** (related words, synonyms, antonyms)
- **Part of speech** classification

### Supported Tasks

- **Text Classification**: Age-appropriate content filtering, readability scoring
- **Text Generation**: Vocabulary-aware content generation for education
- **Translation**: Multilingual vocabulary with pronunciation guides
- **Question Answering**: Etymology and linguistics QA
- **Educational Content Generation**: Lesson planning, quiz generation, vocabulary curricula

### Languages

47 languages: English, Spanish, French, German, Portuguese, Japanese, Korean, Chinese, Arabic, Hindi, Russian, Italian, Dutch, Turkish, Vietnamese, Thai, Polish, Indonesian, Swedish, Danish, Norwegian, Finnish, Czech, Romanian, Hungarian, Greek, Ukrainian, Hebrew, Bengali, Tamil, Malay, Tagalog, Telugu, Swahili, Urdu, Persian, Igbo, Amharic, Yoruba, Burmese, Zulu, Hausa, Khmer, Kazakh, Gujarati, Catalan, Marathi, Punjabi.

## Data Splits

| Split | Rows | Description |
|-------|------|-------------|
| `full` | 162,253 | Complete vocabulary dataset |
| `english_core` | 10,000 | Most-looked-up English words |
| `multilingual_sample` | 1,000 | Words with the most translations across languages |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `word` | string | The vocabulary word |
| `ipa` | string | International Phonetic Alphabet pronunciation |
| `pos` | string | Part of speech (noun, verb, adjective, etc.) |
| `definition` | string | Standard definition |
| `etymology` | string | Word origin and historical development |
| `definition_child` | string | Age-appropriate definition for children (ages 5-12) |
| `definition_adult` | string | Definition for adults |
| `definition_elder` | string | Definition for seniors (65+) with life experience context |
| `translations` | dict | Translations keyed by ISO 639-1 language code |
| `translation_count` | int | Number of available translations |
| `connections` | list | Semantically related words |
| `lookups` | int | Number of API lookups (popularity proxy) |
| `created_at` | string | When the word was added to the dataset |

## Usage

```python
from datasets import load_dataset

# Load the full dataset
ds = load_dataset("nicoletterankin/word-orb-vocabulary", split="full")

# Load just the core English vocabulary
core = load_dataset("nicoletterankin/word-orb-vocabulary", split="english_core")

# Find a word
word = ds.filter(lambda x: x["word"] == "courage")[0]
print(f"IPA: {word['ipa']}")
print(f"Etymology: {word['etymology']}")
print(f"Child definition: {word['definition_child']}")
```

### Build a vocabulary quiz

```python
import random

ds = load_dataset("nicoletterankin/word-orb-vocabulary", split="english_core")
sample = random.sample(range(len(ds)), 4)
correct = sample[0]
word = ds[correct]

print(f"What does '{word['word']}' mean?")
for i, idx in enumerate(sample):
    print(f"  {chr(65+i)}. {ds[idx]['definition']}")
```

### Multilingual lookup

```python
ds = load_dataset("nicoletterankin/word-orb-vocabulary", split="multilingual_sample")
word = ds.filter(lambda x: x["word"] == "peace")[0]
for lang, translation in word["translations"].items():
    print(f"  {lang}: {translation}")
```

## Curation Rationale

This dataset was curated by Lesson of the Day, PBC specifically for AI education agents requiring age-appropriate, culturally sensitive, and gender-equitable vocabulary data. Unlike raw dictionary dumps, every entry is structured for machine consumption with typed fields, consistent formatting, and ethical annotations.

The age-appropriate definitions enable differentiated instruction: the same word is explained differently for a 7-year-old, a 30-year-old professional, and a 70-year-old retiree. This is critical for education AI that must adapt to learner age and context.

## Source Data

Curated and maintained by [Lesson of the Day, PBC](https://lotdpbc.com), a California Public Benefit Corporation building vocabulary infrastructure for AI agents and educators.

Live API: [wordorb.ai](https://wordorb.ai) (free tier: 50 calls/day, no API key required)

## Licensing

This dataset is released under **CC-BY-NC-SA 4.0**. Free for research and non-commercial use. Commercial applications requiring higher volume or real-time access should use the [Word Orb API](https://wordorb.ai/pricing).

## Citation

```bibtex
@dataset{wordorb2026,
  title={Word Orb Vocabulary Intelligence},
  author={Rankin, Nicolette},
  year={2026},
  publisher={Lesson of the Day, PBC},
  url={https://huggingface.co/datasets/nicoletterankin/word-orb-vocabulary},
  note={162,253 words, 47 languages, age-appropriate definitions, etymology, IPA pronunciation}
}
```
