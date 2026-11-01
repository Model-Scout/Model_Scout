---
license: other
task_categories:
  - multiple-choice
  - text-classification
language:
  - ko
pretty_name: KoBEST Query/Context Label-Preserving Stress v2 Extreme
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
---

# KoBEST Query/Context Label-Preserving Stress v2 Extreme

This repository packages an **extreme** paired Korean boundary-stress dataset
built from `skt/kobest_v1`.

## What it contains

Each row preserves:

- the original gold label
- the original answer options, or a synthetic label space for non-MCQ configs

and modifies only the natural input text fields to make the surface form more
tokenization-fragile while keeping:

1. identical non-space character sequence per stressed field
2. identical Kiwi token signature `(form, tag)` per stressed field
3. increased decoder-tokenizer boundary mismatch under
   `unsloth/Meta-Llama-3.1-8B`

Compared with the conservative v1 generator, the **extreme** variant deletes as
many safe internal spaces as possible before the final mismatch check.

## Field coverage

- `boolq`: `paragraph`, `question`
- `copa`: `premise`
- `hellaswag`: `context`
- `sentineg`: `sentence`
- `wic`: `context_1`, `context_2`

## Files

- `data/train.jsonl`: accepted stress pairs
- `metadata/build_report_query_context_stress.json`: generation summary
- `metadata/filtered_out_query_context_stress.jsonl`: audit log for rejected rows
- `metadata/review_query_context_stress.csv`: human-review sheet

## Summary

- source dataset: `skt/kobest_v1`
- tokenizer: `unsloth/Meta-Llama-3.1-8B`
- accepted candidates: `903`
- filtered-out rows: `3658`

Accepted subset counts:

- `boolq`: `423`
- `wic`: `305`
- `hellaswag`: `148`
- `copa`: `18`
- `sentineg`: `9`

## Construction Notes

The generation procedure is implemented in:

- `scripts/build_kobest_query_context_stress.py`

and documented in:

- `docs/kobest_query_context_stress_ruleset.md`

## Citation

If you use this dataset, cite the original KoBEST benchmark and describe this
repository as a derived **extreme label-preserving query/context stress**
variant.
