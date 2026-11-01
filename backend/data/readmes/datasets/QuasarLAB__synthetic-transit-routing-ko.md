---
language:
- ko
pretty_name: Synthetic Transit Routing KO
size_categories:
- n<1K
task_categories:
- text-generation
tags:
- synthetic
- transit-routing
- algorithmic-reasoning
- raptor
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
  - split: validation
    path: validation.jsonl
  - split: test
    path: test.jsonl
  - split: ood
    path: ood.jsonl
---

# Synthetic Transit Routing KO

A small synthetic dataset for studying whether language models can compute transit routes directly from a provided timetable, rather than calling an external routing engine during inference.

The dataset contains **352 examples**: 220 training, 44 validation, 44 test, and 44 out-of-distribution (OOD) examples. Training networks contain 5–6 stops, while OOD networks contain 8–10 stops. Stop names and routing questions are in Korean.

## Data format

Each JSONL record contains:

- `network`: synthetic stops, scheduled trips, and transfer time.
- `query`: origin, destination, departure time, and transfer limit.
- `question`: a Korean routing question.
- `target`: the earliest-arrival reference answer, including route legs, arrival time, total duration, boardings, and transfers.
- `trace`: offline RAPTOR computation snapshots.
- `schema_version`, `sample_id`, `split`, and `metadata`: identifiers and generation metadata.

Times are represented as seconds from the start of the service day and may exceed 86,400 for after-midnight service.

## Generation and validation

Reference answers were generated using a `raptor-demo` adapter and cross-checked against an independent bounded exhaustive boarding oracle. **All 352 reference answers matched, with zero mismatches.**

Examples cover direct journeys, up to three transfers, missed departures and connections, after-midnight journeys, unavailable routes, and timetable modifications that change the correct answer.

Network groups and recorded topology hashes are separated across splits. However, these hashes do not constitute a complete graph-isomorphism check.

## Intended use

Use the timetable and routing question as model inputs, and the reference answer as supervision. These files use a custom structured schema, not a ready-made `messages` chat format.

During evaluation, do not expose `target`, `trace`, or answer-related metadata to the model. Keep test and OOD examples held out from training.

## Limitations

This is an experimental synthetic pilot, not a nationwide or real-world transit benchmark. It excludes walking, real-time delays, frequency-based service, pickup/drop-off restrictions, and ambiguous stop names.

Reference-label validation does not imply that a fine-tuned model can reliably calculate routes or generalize to real transit networks. The dataset provides timetables as inputs; it does not encode an entire GTFS feed into model parameters.