---
license: other
task_categories:
  - multiple-choice
  - text-classification
language:
  - ko
pretty_name: HAE-RAE Query/Context Label-Preserving Stress v2 Extreme
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
---

# HAE-RAE Query/Context Label-Preserving Stress v2 Extreme

This repository packages an **extreme** paired Korean boundary-stress dataset
built from `HAERAE-HUB/HAE_RAE_BENCH_1.1`.

## What it contains

Each row preserves:

- the original answer options
- the original gold answer

and modifies only the `query/context` side to make the surface form more
tokenization-fragile while keeping:

1. identical non-space character sequence
2. identical Kiwi token signature `(form, tag)`
3. increased decoder-tokenizer boundary mismatch under
   `unsloth/Meta-Llama-3.1-8B`

Compared with the conservative v1 generator, the **extreme** variant deletes as
many safe internal spaces as possible before the final mismatch check.

## Files

- `data/train.jsonl`: accepted stress pairs
- `metadata/build_report_query_context_stress.json`: generation summary
- `metadata/filtered_out_query_context_stress.jsonl`: audit log for rejected rows
- `metadata/review_query_context_stress.csv`: human-review sheet

## Summary

- source dataset: `HAERAE-HUB/HAE_RAE_BENCH_1.1`
- tokenizer: `unsloth/Meta-Llama-3.1-8B`
- accepted candidates: `555`
- filtered-out rows: `4345`

Accepted subset counts:

- `correct_definition_matching`: `9`
- `csat_geo`: `81`
- `csat_law`: `129`
- `csat_socio`: `191`
- `general_knowledge`: `12`
- `history`: `25`
- `rare_words`: `6`
- `reading_comprehension`: `102`

## Construction Notes

The generation procedure is implemented in:

- `scripts/build_haerae_query_context_stress.py`

and documented in:

- `docs/haerae_query_context_stress_ruleset.md`

## Citation

If you use this dataset, cite the original HAE-RAE benchmark and describe this
repository as a derived **extreme label-preserving query/context stress**
variant.
