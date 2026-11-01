---
language:
- en
- zh
- hi
- ar
- bn
- ja
- ko
- ta
- th
- ka
- am
size_categories:
- 10K<n<100K
task_categories:
- text-classification
---

# Poly-FEVER: A Multilingual Hallucination Detection Benchmark

Poly-FEVER is a controlled multilingual benchmark for factuality judgment and
hallucination detection. It extends FEVER, Climate-FEVER, and SciFact to 77,973
aligned claims in 11 languages. Each claim shares the same binary label across
languages and includes topic metadata from a 22-topic LDA model, allowing
language to vary while factual content and ground truth remain fixed.

## Dataset overview

| Claims | Languages | Supported | Refuted |
| ---: | ---: | ---: | ---: |
| 77,973 | 11 | 46,808 (60.03%) | 31,165 (39.97%) |

## Languages

English (`en`), Mandarin Chinese (`zh-CN`), Hindi (`hi`), Arabic
(`ar`), Bengali (`bn`), Japanese (`ja`), Korean (`ko`), Tamil
(`ta`), Thai (`th`), Georgian (`ka`), and Amharic (`am`).

## Data fields

- `ID`: unique claim identifier.
- `Label`: `true` for Supported and `false` for Refuted.
- `Topic Distribution`: the five highest-probability LDA topic identifiers.
- `en`: English source claim.
- `zh-CN`, `hi`, `ar`, `bn`, `ja`, `ko`, `ta`, `th`, `ka`,
  `am`: aligned translations.
- `cometkiwi_score_<language>`: reference-free translation-quality estimate
  for each target language; higher scores indicate better predicted quality.

## Translation quality

Translations were produced with Google Cloud Translation and evaluated through
targeted human review, GEMBA, and COMETKiwi. GEMBA averaged 91.2 on the
evaluated 5% sample. Across all source--translation pairs, the macro-average
COMETKiwi score was .8441, and 93.70% received a score of at least .75.
