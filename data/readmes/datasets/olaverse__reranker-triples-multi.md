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
  - text-ranking
tags:
  - multilingual
  - reranker
  - hard-negatives
size_categories:
  - 10K<n<100K
---

# reranker-triples-multi

Mined hard-negative triples for cross-encoder reranker training, across 25 languages — `(query, positive, negatives[5])`, built from [`olaverse/qg-passages-multi`](https://huggingface.co/datasets/olaverse/qg-passages-multi).

## Dataset Summary

For each `(query, positive)` pair, up to 5 **hard negatives** — passages that are semantically similar to the query but are not its true answer — mined via embedding similarity within a controlled rank window, with false-negative guards.

## Data Fields

| Field | Type | Description |
|---|---|---|
| `query` | string | A search-style question |
| `positive` | string | The passage that actually answers it |
| `negatives` | list[string] | Up to 5 similar-but-wrong passages |
| `language` | string | ISO 639-3 code |

## Data Instance

```json
{
  "query": "What causes ocean tides?",
  "positive": "Tides are caused by the gravitational pull of the moon and, to a lesser extent, the sun, acting on Earth's oceans.",
  "negatives": [
    "Ocean currents are driven primarily by wind patterns and temperature differences.",
    "The moon's surface is covered in craters formed by asteroid impacts.",
    "..."
  ],
  "language": "eng"
}
```

## Languages

Same 25-language set as `qg-passages-multi`.

## Dataset Creation

For each query, its passage pool (same language) was embedded with `Qwen/Qwen3-Embedding-0.6B`. Candidate negatives were drawn from rank window 2–50 (skipping the very top ranks, which are likely near-duplicates or the true positive), then filtered with two false-negative guards: an absolute similarity cap (0.85) and a margin below the true positive's score (0.05) — both intended to exclude passages that are actually also-correct, not just similar.

**Note**: these triples were mined against the *original* (uncleaned) passage text — see the "Known Limitations" section of `qg-passages-multi`'s card for what that means. They have not been re-mined against a cleaned variant.

## Intended Use

Pairwise or listwise ranking loss for cross-encoder reranker fine-tuning — a reranker scores one `(query, passage)` pair at a time, so it relies on explicit negatives like these rather than in-batch negatives.

## Licensing

Apache-2.0.

## Citation

```
@misc{reranker-triples-multi,
  title  = {reranker-triples-multi},
  author = {Olaverse},
  year   = {2026},
  url    = {https://huggingface.co/datasets/olaverse/reranker-triples-multi}
}
```