---
license: mit
pretty_name: Malicious Coding Intent Classifier Data
language:
  - en
  - zh
  - hi
  - es
  - ar
  - bn
  - pt
  - ru
  - ja
  - de
  - fr
  - tr
  - ko
  - vi
  - it
  - id
  - pl
multilinguality:
  - multilingual
annotations_creators:
  - machine-generated
language_creators:
  - machine-generated
source_datasets:
  - original
task_categories:
  - text-classification
tags:
  - safety
  - malware
  - code
  - multilingual
  - red-team
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.parquet
      - split: val
        path: data/val.parquet
      - split: test
        path: data/test.parquet
      - split: test_obfuscated
        path: data/test_obfuscated.parquet
      - split: test_malware_code
        path: data/test_malware_code.parquet
      - split: test_benign_code
        path: data/test_benign_code.parquet
dataset_info:
  - config_name: default
    description: >
      Classifier splits for multilingual malicious-coding-intent detection.
      Includes lexicon/template/HF-derived prompt rows, malware/decompiled-code
      positive hold-outs, and benign-code hard negatives. Total rows: 289171.
    features:
      - name: text
        dtype: string
      - name: malicious
        dtype: int64
      - name: categories
        sequence: string
      - name: source
        dtype: string
      - name: lang
        dtype: string
    splits:
      - name: train
        num_bytes: 74578671
        num_examples: 222950
      - name: val
        num_bytes: 10191786
        num_examples: 28485
      - name: test
        num_bytes: 9120515
        num_examples: 27736
      - name: test_obfuscated
        num_bytes: 76332
        num_examples: 4000
      - name: test_malware_code
        num_bytes: 2951351
        num_examples: 2000
      - name: test_benign_code
        num_bytes: 1301034
        num_examples: 4000
    download_size: 98219689
    dataset_size: 98219689
---

# Malicious Coding Intent Classifier Data

Dataset artifact for [https://github.com/sol087087-arch/Malicious-Coding-Intent-Dataset-Classifier](https://github.com/sol087087-arch/Malicious-Coding-Intent-Dataset-Classifier).

Variant: `v3_code_aware`

## Splits

| File | Rows | Role |
|------|-----:|------|
| `data/train.parquet` | 222,950 | train |
| `data/val.parquet` | 28,485 | validation |
| `data/test.parquet` | 27,736 | in-distribution test |
| `data/test_obfuscated.parquet` | 4,000 | positive hold-out: obfuscated malicious terms |
| `data/test_malware_code.parquet` | 2,000 | positive hold-out: malware/decompiled-code snippets |
| `data/test_benign_code.parquet` | 4,000 | negative hold-out: benign code hard negatives |

## Schema

- `text` - prompt/code snippet.
- `malicious` - `1` malicious intent/code, `0` benign.
- `categories` - multilabel category ids; empty for benign rows.
- `source` - provenance string.
- `lang` - language code when available; empty for legacy rows.

See `labels.json` and `dataset_report.json` for label names and build counts.

## Evaluation Context

This dataset supports the v6/v8 red-team evaluation:

- obfuscation recall,
- language-pivot recall,
- benign-code false-positive checks,
- code-vs-intent hard-negative ablations.

The malware-code and obfuscated splits are positive-only stress checks, so they
measure recall, not precision. Use matched negative hold-outs for FPR/precision.

GitHub: [https://github.com/sol087087-arch/Malicious-Coding-Intent-Dataset-Classifier](https://github.com/sol087087-arch/Malicious-Coding-Intent-Dataset-Classifier)
HF dataset repo id: `NecroMOnk/malicious-coding-intent-v6-data`
