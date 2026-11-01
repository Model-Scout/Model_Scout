---
language: [en, ko]
license: other
pretty_name: Qwen3.8 Executor Unified Evaluation Dataset
tags: [qwen, executor, tool-calling, agents]
---

# Qwen3.8 Executor Unified Evaluation Dataset

> **DO NOT USE FOR TRAINING.** This repository contains evaluation-only tasks and model outputs.

## Purpose

Public, provenance-pinned executor records for tool use, repository agents, computer use, and Korean coverage. This is an attributed integration; the upstream authors collected or generated the source data.

## Schema

The Parquet files share the canonical fields documented in `manifests/schema.json`. `messages` uses role/content/tool-call structs. Dynamic tool arguments are validated JSON in `arguments_json`. Images and executable artifacts are self-contained bytes where included.

## Sources, revisions, licenses, and transformations

| HF repo | revision | config | source split | license | rows before | accepted | rejected | transformation |
|---|---|---|---|---:|---:|---:|---:|---|
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `default` | `validation` | apache-2.0 | 762 | 726 | 36 | canonicalized |
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `benchmark` | `g1_instruction` | apache-2.0 | 200 | 197 | 3 | canonicalized |
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `benchmark` | `g1_category` | apache-2.0 | 200 | 200 | 0 | canonicalized |
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `benchmark` | `g1_tool` | apache-2.0 | 200 | 198 | 2 | canonicalized |
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `benchmark` | `g2_instruction` | apache-2.0 | 200 | 197 | 3 | canonicalized |
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `benchmark` | `g2_category` | apache-2.0 | 200 | 177 | 23 | canonicalized |
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `benchmark` | `g3_instruction` | apache-2.0 | 100 | 100 | 0 | canonicalized |
| [gyung/toolllama-korean-function-calling](https://huggingface.co/datasets/gyung/toolllama-korean-function-calling/tree/73d96c3b1e383a806ee33c95ea1ba94721f17ee6) | `73d96c3b1e383a806ee33c95ea1ba94721f17ee6` | `default` | `train` | apache-2.0 | 1524 | 1438 | 86 | canonicalized |
| [UI-MOPD/OSWorld-Eval-Results](https://huggingface.co/datasets/UI-MOPD/OSWorld-Eval-Results/tree/a518b8776c172c9456f85b3fa5ef451d326a7969) | `a518b8776c172c9456f85b3fa5ef451d326a7969` | `default` | `train` | apache-2.0 | 361 | 359 | 2 | canonicalized |
| [xlangai/CUA-Gym](https://huggingface.co/datasets/xlangai/CUA-Gym/tree/3c021d06e2b01bbb6ad28cfddec41d856e4a78c5) | `3c021d06e2b01bbb6ad28cfddec41d856e4a78c5` | `tasks` | `train` | cc-by-4.0 | 10910 | 10903 | 7 | canonicalized |

No single license is asserted over the mixture. Apply each row's `source_license` and upstream attribution requirements.

## Build and isolation methodology

Evaluation data is canonicalized first. Exact SHA-256, normalized SHA-256 (whitespace, timestamps, UUIDs, and volatile IDs normalized), normalized user-prompt SHA-256, and 64-bit SimHash are then checked while admitting Train rows. Exact, normalized, prompt collisions, and near matches at Hamming distance <=3 are removed from Train. A trajectory/task is always one row and never split by turn.

High-confidence secrets, Korean resident registration numbers, empty assistant targets, invalid JSON tool arguments, missing tool references, broken images, and duplicate rows are rejected. `persona_seed` rows are not assistant targets. OpenWebRL and Uni-GUI are reference-only because their cards identify benchmark-derived task families. ProCUA uses deterministic shard 00000 only; Hermes-3 and Korean personas use documented deterministic sampling so general/persona data does not dominate.

## Multimodal and tool handling

Screenshots are not replaced with text descriptions. Included screenshots use bytes/path/mime/hash records and were decoded with Pillow. Tool definitions remain stable JSON strings; calls have name/id/type and validated `arguments_json`.

## Recommended filters and limitations

Sample by `record_type` and source instead of uniform row sampling. Exclude `persona_seed` from direct response loss. Eval is not an independent benchmark where `metadata.contamination_family` says ToolBench. Source licenses and upstream terms still apply. The near-duplicate index uses a bounded within-Train collision bucket; exact and normalized checks are exhaustive.

## Reproduction

```bash
pip install huggingface_hub pyarrow pillow requests numpy
python build_executor_datasets.py --output executor_dataset_build --cache /mnt/HDD0/executor_dataset_cache
python build_executor_datasets.py --validate-only --output executor_dataset_build
```

See `manifests/`, `reports/`, and `reports/sanity_sample.jsonl` for pinned source metadata and validation evidence.
