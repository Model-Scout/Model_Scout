---
license: cc-by-4.0
language:
- en
- zh
- hi
- es
- ar
- fr
- ru
- ja
- tr
- ko
- sw
- pt
- el
- vi
task_categories:
- token-classification
- text-generation
tags:
- emoji
- multilingual
- span-annotation
- emojinization
pretty_name: Emojinize Multilingual (emoji-span annotations)
size_categories:
- 100K<n<1M
configs:
- config_name: all
  default: true
  data_files:
  - split: train
    path: all/train-*
  - split: validation
    path: all/validation-*
  - split: test
    path: all/test-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
  - split: validation
    path: en/validation-*
  - split: test
    path: en/test-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
  - split: validation
    path: zh/validation-*
  - split: test
    path: zh/test-*
- config_name: hi
  data_files:
  - split: train
    path: hi/train-*
  - split: validation
    path: hi/validation-*
  - split: test
    path: hi/test-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
  - split: validation
    path: es/validation-*
  - split: test
    path: es/test-*
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
  - split: validation
    path: ar/validation-*
  - split: test
    path: ar/test-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
  - split: validation
    path: fr/validation-*
  - split: test
    path: fr/test-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
  - split: validation
    path: ru/validation-*
  - split: test
    path: ru/test-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
  - split: validation
    path: ja/validation-*
  - split: test
    path: ja/test-*
- config_name: tr
  data_files:
  - split: train
    path: tr/train-*
  - split: validation
    path: tr/validation-*
  - split: test
    path: tr/test-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
  - split: validation
    path: ko/validation-*
  - split: test
    path: ko/test-*
- config_name: sw
  data_files:
  - split: train
    path: sw/train-*
  - split: validation
    path: sw/validation-*
  - split: test
    path: sw/test-*
- config_name: pt
  data_files:
  - split: test
    path: pt/test-*
- config_name: el
  data_files:
  - split: test
    path: el/test-*
- config_name: vi
  data_files:
  - split: test
    path: vi/test-*
---

# Emojinize Multilingual

A multilingual dataset of 108,478 sentences across 14 languages for emoji-based text augmentation. In each sentence, selected spans (individual words or fixed multi-word expressions) are identified by character offsets and paired with emoji sequences representing their meaning in context. The dataset supports downstream span detection and emoji generation tasks, and was created using a two-stage LLM annotation pipeline with `gpt-5.4` for span marking and `gpt-5.5` for emoji annotation.

## Loading

```python
from datasets import load_dataset

# Load all 14 languages using the default "all" configuration:
ds = load_dataset("yagizgencer/emojinize-multilingual")

# Load only one language:
en = load_dataset("yagizgencer/emojinize-multilingual", "en")

# Load a specific split:
train_all = load_dataset(
    "yagizgencer/emojinize-multilingual",
    "all",
    split="train",
)

# Held-out languages ("pt", "el", "vi") are reserved for zero-shot evaluation
# and therefore contain only a test split:
test_vi = load_dataset(
    "yagizgencer/emojinize-multilingual",
    "vi",
    split="test",
)
```

## Schema

| field | type | description |
|-------|------|-------------|
| `id` | int64 | Sentence ID. |
| `lang` | string | ISO language code. |
| `sentence` | string | Raw sentence. |
| `spans` | list of structs | Annotated spans. |

Each element of `spans` contains:

- `start` (int32, inclusive)
- `end` (int32, exclusive)
- `text` (string)
- `emojis` (string)

Invariant: `sentence[start:end] == text`. Offsets are Unicode character offsets.

### Example Dataset Row

```json
{
  "id": 3516,
  "lang": "en",
  "sentence": "A drivers' license suspension is one of the primary sentences that you can receive.",
  "spans": [
    {"start":  2, "end": 18, "text": "drivers' license", "emojis": "🪪🚗✅"},
    {"start": 19, "end": 29, "text": "suspension",       "emojis": "🚫🪪⏸️"},
    {"start": 44, "end": 51, "text": "primary",          "emojis": "🥇⭐"},
    {"start": 52, "end": 61, "text": "sentences",        "emojis": "⚖️👨‍⚖️📜"},
    {"start": 75, "end": 82, "text": "receive",          "emojis": "📥🤲"}
  ]
}
```

## Languages and Splits

11 trained languages (`en`, `zh`, `hi`, `es`, `ar`, `fr`, `ru`, `ja`, `tr`, `ko`, `sw`) have train/validation/test splits (80/10/10, sentence-level). 3 held-out languages (`pt`, `el`, `vi`) have a test split only. The `all` configuration combines all languages into a single multilingual dataset.

| lang | train | validation | test |
|------|------:|-----------:|-----:|
| en | 7,706 | 963 | 964 |
| zh | 7,757 | 970 | 970 |
| hi | 7,346 | 918 | 919 |
| es | 7,730 | 966 | 967 |
| ar | 7,642 | 955 | 956 |
| fr | 7,708 | 964 | 964 |
| ru | 7,625 | 953 | 954 |
| ja | 7,750 | 969 | 969 |
| tr | 7,792 | 974 | 975 |
| ko | 7,765 | 971 | 971 |
| sw | 7,913 | 989 | 990 |
| pt *(held-out)* | — | — | 846 |
| el *(held-out)* | — | — | 840 |
| vi *(held-out)* | — | — | 867 |
| **all** | **84,734** | **10,592** | **13,152** |

## License and Attribution

Released under **CC-BY-4.0**. Raw sentences are derived from [agentlans/high-quality-multilingual-sentences](https://huggingface.co/datasets/agentlans/high-quality-multilingual-sentences) (CC-BY-4.0, all languages except `sw`) and [castorini/afriberta-corpus](https://huggingface.co/datasets/castorini/afriberta-corpus) (Apache-2.0, `sw`; mostly BBC News and Common Crawl). Span and emoji annotations are OpenAI model outputs (`gpt-5.4`, `gpt-5.5`); downstream users should comply with OpenAI's Terms of Use.
