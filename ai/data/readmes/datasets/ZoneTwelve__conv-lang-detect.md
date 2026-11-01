---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- fr
- es
- de
- ar
- ru
- pt
- vi
- th
task_categories:
- text-classification
tags:
- language-detection
- multilingual
- conversational
- intent-language
pretty_name: conv-lang-detect
size_categories:
- 1K<n<10K
---

# conv-lang-detect

A multilingual dataset for **conversational turn-level language detection** — detecting which language a user prefers in a given turn, even when the turn contains pasted content (code, emails, articles, lyrics) in a different language.

## The Problem

Standard language detectors return the dominant language of the full text. In a conversational setting, users often paste foreign content and ask a question in their own language:

> *User (zh-Hant)*: 我這是一個很酷的文章，但我看不太懂，我可能需要你幫我翻譯一下
> ```
> Cosine similarity can be used to measure the similarity between two word vectors…
> ```

A naive detector returns `en`. The correct label is `zh-Hant` — the language the user actually wrote in.

## Dataset

### Loading

```python
from datasets import load_dataset

ds = load_dataset("ZoneTwelve/conv-lang-detect")
```

### Schema

| Column | Type | Description |
|---|---|---|
| `prompt` | `string` | The user's message (may contain embedded content in another language) |
| `language` | `string` | BCP 47 tag for the language the user wrote their question in |
| `source` | `string` | `synthetic` or `eval_lmsys` |

### Languages

13 BCP 47 tags:

| Tag | Language | Count |
|---|---|---|
| `en` | English | 1 059 |
| `ru` | Russian | 468 |
| `fr` | French | 460 |
| `pt` | Portuguese | 460 |
| `es` | Spanish | 456 |
| `vi` | Vietnamese | 446 |
| `ja` | Japanese | 444 |
| `zh-Hans` | Simplified Chinese | 444 |
| `th` | Thai | 440 |
| `de` | German | 435 |
| `ar` | Arabic | 432 |
| `ko` | Korean | 426 |
| `zh-Hant` | Traditional Chinese | 408 |
| **Total** | | **6 378** |

### Sources

| Source | Records | Description |
|---|---|---|
| `synthetic` | 5 637 | Generated via a two-stage LLM pipeline covering all 156 ordered language pairs (13 × 12), ≥20 examples per pair |
| `eval_lmsys` | 741 | First user turns from [lmsys/lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m), LLM-labeled |

### Data cleaning

All records are deduplicated by exact prompt text (synthetic data takes priority on collision), out-of-scope language tags are dropped, and prompts shorter than 4 characters are removed.
