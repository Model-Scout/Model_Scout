---
license: odc-by
task_categories:
- zero-shot-classification
- text-classification
language:
- multilingual
- en
- de
- fr
- es
- pt
- it
- nl
- pl
- ru
- uk
- cs
- tr
- ar
- fa
- he
- hi
- bn
- zh
- ja
- ko
- vi
- id
- th
- sw
- el
- ro
- hu
- da
- fi
- sv
- tl
- ur
- ms
tags:
- synthetic
- zero-shot
- nli
- multilingual
- intent
- topic-classification
- sentiment
- emotion
- aspect-based-sentiment
size_categories:
- 100K<n<1M
pretty_name: Multilingual Zero-Shot Classification (synthetic)
---

# Multilingual Zero-Shot Classification (synthetic)

253,346 texts in 33 languages, each with a **set of candidate labels**, the **correct label(s)**, and often a
**hypothesis template**. Built to train multilingual zero-shot (NLI-style) classifiers; also usable for few-shot or
instruction data, label-set generalization studies, and multilingual intent/topic/sentiment classification.

This is the classification part of the training data of
[multilingual-zeroshot-small / base / large](https://huggingface.co/Horizon-Labs/multilingual-zeroshot-base). Code:
[github.com/horizon-ai-labs/agent-io-guards](https://github.com/horizon-ai-labs/agent-io-guards) (`zeroshot/gen_zeroshot.py`, `zeroshot/gen_zeroshot_v2.py`).

## Fields

| field | description |
|---|---|
| `text` | the text to classify (a short message, question, review, headline, or a web passage) |
| `lang` | the language the text was requested in (see limitations) |
| `task` | what is being classified (e.g. "customer message topic", "emotion", "aspects") |
| `candidate_labels` | the label set (English) |
| `gold_labels` | the correct label(s); several for multi-label items (aspects, some passages) |
| `hypothesis_template` | a natural template for the task, e.g. "This customer message is about {}." (empty for some items) |
| `kind` | `short` (invented label sets), `tax_short` (fixed generic taxonomies), `aspect` (multi-label review aspects), `passage` / `tax_passage` (labelled web passages) |
| `text_origin` | `qwen-generated` or `fineweb` |

Counts by kind: tax_short 94,639, short 77,616, tax_passage 47,368, aspect 21,725, passage 11,998.

## How it was made

All labels and generated texts come from [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) (Apache-2.0):

- **short**: for one of 26 task types (support tickets, voice-assistant intents, review sentiment, app-store issues, ...) in one of
  32 domains, the model invented a realistic label set and a hypothesis template, then wrote 8 short texts in a given
  language with their labels.
- **tax_short**: the same, but for fixed generic taxonomies (emotion, sentiment, Q&A question topic, news section,
  customer-message topic, urgency, formality, spam type); the prompt asked not to use the label word itself in the text.
- **aspect**: reviews of hotels, restaurants, phones, shops, airlines, software, courses and cars that mention 1-3 aspects
  without naming them (e.g. wifi problems for "internet"); multi-label.
- **passage / tax_passage**: passages from [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) and
  [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) (ODC-BY) labelled by the model for topic, text type,
  sentiment, audience, purpose or news section, with plausible wrong labels (including near misses).

Duplicates (same text and task) were removed. No benchmark data was used.

## Languages

English (59,665), Russian (6,788), Greek (6,787), Italian (6,627), Dutch (6,567), Korean (6,557), Arabic (6,500), Turkish (6,496), Czech (6,438), Swedish (6,437), Vietnamese (6,412), Thai (6,386), Bengali (6,369), Ukrainian (6,340), Spanish (6,337), Swahili (6,329), French (6,316), German (6,286), Indonesian (6,250), Portuguese (6,204), Japanese (6,188), Polish (6,166), Hindi (6,123), Hebrew (6,099), Persian (6,055), Chinese (5,888), Urdu (5,109), Hungarian (5,085), Finnish (5,084), Romanian (4,949), Danish (4,939), Malay (4,788), Tagalog (4,782).

## Limitations

- **Synthetic and not human-verified.** Labels come from one LLM. When we turned these items into NLI pairs, our trained
  large model disagreed with about 7% of the derived labels, which gives a rough idea of the noise level.
- **Language tags are the requested language.** The generator occasionally wrote English when another language was asked for.
- **Style**: the texts are cleaner and more prototypical than real user text, even where the prompt asked for typos and
  informal style.
- **Label-name overlap with benchmarks**: some fixed taxonomies (Q&A question topics, news sections, emotions) use label names
  that are close to public benchmarks such as Yahoo Answers, AG News and dair-ai/emotion. The texts are all new, but if you
  evaluate on those benchmarks, treat the label names as seen.
- Web passages may contain whatever FineWeb contains (FineWeb applies its own PII anonymization and filtering).

## License

ODC-BY 1.0 (the web passages come from FineWeb, ODC-BY; generated content is from an Apache-2.0 model). Please attribute
FineWeb for the passage texts.
