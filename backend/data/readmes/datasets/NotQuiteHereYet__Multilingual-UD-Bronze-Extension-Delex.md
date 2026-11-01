---
license: cc-by-sa-4.0
task_categories:
  - text-generation
language:
  - ar
  - de
  - en
  - es
  - eu
  - fi
  - hi
  - hy
  - id
  - ja
  - ko
  - lv
  - ru
  - te
  - tr
  - zh
tags:
  - universal-dependencies
  - delexicalized
  - language-model
  - morphology
  - multilingual
---

# Delexicalized Universal Dependencies (UD 2.17 + Silver v2)

A multilingual language-modelling dataset built from Universal Dependencies 2.17
gold treebanks and UDPipe-parsed silver data. Lexemes (NOUN, VERB, ADJ, ADV, PROPN, NUM)
are replaced with structured tokens encoding part-of-speech, morphological features,
and a dependency-frame cluster label. Function words are kept as lowercased surface
forms, namespaced by language.

## Languages

ar, de, en, es, eu, fi, hi, hy, id, ja, ko, lv, ru, te, tr, zh

16 languages total: 13 with UD gold + silver data, 3 (de, ja, ru) with UD gold only.

## Token format

Each sentence is one line of space-separated tokens:

| Token type | Example | Meaning |
|---|---|---|
| Lexeme | `[en\|VERB\|frame3\|Mood=Ind\|Tense=Past]` | English verb, dependency frame 3, indicative past |
| Function word | `en::the` | English surface form "the" |
| Sentence end | `<eos>` | End of sentence marker |

- Language code is a two-letter ISO 639-1 code prepended to structural tokens.
- `frame0`–`frame7`: dependency frame cluster (K=8 KMeans on syntactic attachment features, fitted independently per POS per language).
- Morphological features are from the UD annotation, sorted alphabetically.

## Splits

| Split | Sentences | Notes |
|---|---|---|
| train | 1,374,513 | All training sections |
| dev | 64,817 | All dev sections |
| test | 98,888 | All test sections |

## Files

```
data/
  all_train.txt.gz        combined training set (all languages, randomised)
  all_dev.txt.gz          combined dev set
  all_test.txt.gz         combined test set
langs/
  {lang}/
    train_gold.txt.gz     UD gold training sentences for this language
    train_silver.txt.gz   UDPipe-parsed silver training sentences
    dev.txt.gz            dev sentences (UD gold only)
    test.txt.gz           test sentences (UD gold only)
dataset_info.json         per-language gold/silver/total token counts
factor_vocab.json         feature vocabulary for FactoredDelexLM
delex_vocab.txt           flat token vocabulary with counts
```

The `langs/` files allow selecting subsets of languages or gold-only training.
The `data/` aggregate files are pre-shuffled across languages and sources.

## Usage

Download with the HuggingFace CLI:

```bash
pip install huggingface-hub
huggingface-cli download REPO_NAME --repo-type dataset --local-dir ./delex_data
cd delex_data && gunzip data/*.gz langs/*/*.gz
```

Train on all languages (combined):

```bash
python train.py --data-dir delex_data/data/ --out-dir runs/run1/ \
    --factored --factor-vocab delex_data/factor_vocab.json
```

Train on a language subset (recombine from `langs/`):

```bash
cat delex_data/langs/en/train_gold.txt delex_data/langs/en/train_silver.txt \
    delex_data/langs/de/train_gold.txt > my_train.txt
```

## Source

- Universal Dependencies 2.17: https://universaldependencies.org
- Silver data: UDPipe v2 parses of Common Crawl data
- Dependency profiles: per-lemma syntactic attachment statistics, K=8 KMeans within POS
