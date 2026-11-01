---
license: other
task_categories:
  - multiple-choice
  - text-classification
language:
  - ko
pretty_name: HAE-RAE Query/Context Label-Preserving Stress v3
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
---

# HAE-RAE Query/Context Label-Preserving Stress v3

This repository packages a **v3** paired Korean boundary-stress dataset built
from `HAERAE-HUB/HAE_RAE_BENCH_1.1`.

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

Compared with the conservative v1 generator, the **v3** variant selects the
highest local mismatch-increase edit at each step. On long contexts, v3 caps
candidate space-segment search for tractable full-dataset generation.

## Files

- `data/train.jsonl`: accepted stress pairs
- `metadata/build_report_query_context_stress.json`: generation summary
- `metadata/filtered_out_query_context_stress.jsonl`: audit log for rejected rows
- `metadata/review_query_context_stress.csv`: human-review sheet

## Summary

- source dataset: `HAERAE-HUB/HAE_RAE_BENCH_1.1`
- tokenizer: `unsloth/Meta-Llama-3.1-8B`
- accepted candidates: `3188`
- filtered-out rows: `1712`

Accepted subset counts:

- `correct_definition_matching`: `159`
- `csat_geo`: `114`
- `csat_law`: `206`
- `csat_socio`: `267`
- `date_understanding`: `475`
- `general_knowledge`: `176`
- `history`: `188`
- `loan_words`: `169`
- `rare_words`: `405`
- `standard_nomenclature`: `153`
- `reading_comprehension`: `876`

## Construction Notes

The generation procedure is implemented in:

- `scripts/build_haerae_query_context_stress.py`

and documented in:

- `docs/haerae_query_context_stress_ruleset.md`

## Citation

If you use this dataset, cite the original HAE-RAE benchmark and describe this
repository as a derived **v3 label-preserving query/context stress** variant.
