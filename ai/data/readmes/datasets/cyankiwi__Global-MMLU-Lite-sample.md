---
license: apache-2.0
task_categories:
  - question-answering
  - multiple-choice
language:
  - ar
  - bn
  - de
  - en
  - es
  - fr
  - hi
  - id
  - it
  - ja
  - ko
  - pt
  - sw
  - yo
  - zh
pretty_name: Global-MMLU-Lite (sample, 40 per language)
size_categories:
  - n<1K
tags:
  - mmlu
  - multilingual
  - evaluation
  - sample
configs:
  - config_name: ar
    data_files:
      - split: test
        path: ar/test-*.parquet
  - config_name: bn
    data_files:
      - split: test
        path: bn/test-*.parquet
  - config_name: de
    data_files:
      - split: test
        path: de/test-*.parquet
  - config_name: en
    data_files:
      - split: test
        path: en/test-*.parquet
  - config_name: es
    data_files:
      - split: test
        path: es/test-*.parquet
  - config_name: fr
    data_files:
      - split: test
        path: fr/test-*.parquet
  - config_name: hi
    data_files:
      - split: test
        path: hi/test-*.parquet
  - config_name: id
    data_files:
      - split: test
        path: id/test-*.parquet
  - config_name: it
    data_files:
      - split: test
        path: it/test-*.parquet
  - config_name: ja
    data_files:
      - split: test
        path: ja/test-*.parquet
  - config_name: ko
    data_files:
      - split: test
        path: ko/test-*.parquet
  - config_name: pt
    data_files:
      - split: test
        path: pt/test-*.parquet
  - config_name: sw
    data_files:
      - split: test
        path: sw/test-*.parquet
  - config_name: yo
    data_files:
      - split: test
        path: yo/test-*.parquet
  - config_name: zh
    data_files:
      - split: test
        path: zh/test-*.parquet
---

# Global-MMLU-Lite — Sample Subset

A small, fixed-size subset of [CohereLabs/Global-MMLU-Lite](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) intended for fast smoke-testing of multilingual MMLU evaluation pipelines.

## What this is

- **40 examples per language**, 15 languages, **600 examples total**.
- **Strictly non-overlapping windows** across languages: language *i* takes rows `[i*40, i*40+40)` from the per-language pool of `test` followed by `dev` (test=400, dev=200, pool=600). Concretely, languages 0–9 fall entirely within the original `test` split and languages 10–14 within `dev`.
- **Schema preserved** from the upstream dataset — same columns, same dtypes — so any code that runs on `CohereLabs/Global-MMLU-Lite` should run here unchanged.
