---
license: apache-2.0
language:
  - en
  - fr
  - de
  - es
  - pt
  - it
  - nl
  - ru
  - pl
  - tr
  - vi
  - id
  - hi
  - ja
  - ko
  - yo
  - ig
  - ha
  - sw
  - am
  - zu
  - xh
  - sn
  - so
  - af
task_categories:
  - text-generation
tags:
  - question-generation
  - multilingual
  - evaluation
size_categories:
  - n<1K
---

# qg-eval-multi-fresh

Held-out evaluation passages for [`olaverse/mist-qg-1.5b`](https://huggingface.co/olaverse/mist-qg-1.5b) — **provably never seen during training**, used to compute the model's published round-trip keep-rate.

## Dataset Summary

625 passages (~25 per language, 25 languages), sampled from the same source as the training data but explicitly deduplicated against every passage used to train `mist-qg-1.5b`, so scores on this set measure generalization rather than memorization.

## Data Fields

| Field | Type | Description |
|---|---|---|
| `passage` | string | Source text, unseen during training |
| `language` | string | ISO 639-3 code |

No `questions` field — this dataset intentionally ships passages only. Evaluation is done by generating questions with the model under test and checking round-trip retrieval, not by comparing against a fixed reference answer.

## Data Instance

```json
{
  "passage": "Photosynthesis converts sunlight into chemical energy in plants, using carbon dioxide and water to produce glucose and oxygen.",
  "language": "eng"
}
```

## Dataset Creation

Passages were streamed from the same source as `qg-passages-multi` (`CohereLabs/aya_collection_language_split`), using a different shuffle seed. Every candidate was hashed and checked against the hash set of all passages used across every training run of `mist-qg-1.5b` (both the original and a cleaned variant that was ultimately not published); any match was discarded before sampling.

## Intended Use

Evaluating question-generation models via round-trip self-consistency: generate questions on these passages, embed the questions and the passage pool, and check whether each question retrieves its own source passage. This is how `mist-qg-1.5b`'s published metric was computed — see its model card for the full per-language table and the embedder used to score it.

This is an **in-house benchmark**, not a third-party or standardized one — treat scores against it as directly comparable only across models evaluated the same way (same embedder, same distractor pool size, same top-k).

## Licensing

Apache-2.0.

## Citation

```
@misc{qg-eval-multi-fresh,
  title  = {qg-eval-multi-fresh},
  author = {Olaverse},
  year   = {2026},
  url    = {https://huggingface.co/datasets/olaverse/qg-eval-multi-fresh}
}
```