---
license: apache-2.0
task_categories:
- text-generation
language:
- en
- ko
- multilingual
tags:
- reasoning
- math
- science
- stem
- filtered
size_categories:
- 100K<n<1M
---

# GLM-5.1-Reasoning-1M-filtered

Refusal-filtered subset of `zai-org/GLM-5.1-Reasoning-1M`.

## Filtering

Conservative regex/string match for explicit refusal patterns (e.g., "I cannot",
"I can't", "I'm not able to", "as an AI", "죄송합니다", etc.) applied on the
assistant response field. Drop ratio: ~0.00% (very few refusals in source).

## Files

| File | Size | Records (kept) |
|---|---|---|
| `main.jsonl` | 19 GB | (full main subset, refusals removed) |
| `Math.jsonl` | 4.1 GB | mathematics reasoning |
| `PHD-Science.jsonl` | 3.8 GB | 103,705 |
| `Multilingual-STEM.jsonl` | 3.6 GB | 92,781 |

Total: 30 GB JSONL.

## Source

- Original: [zai-org/GLM-5.1-Reasoning-1M](https://huggingface.co/datasets/zai-org/GLM-5.1-Reasoning-1M)
- Filter script: `filter_glm_refusals.py` (sequential to avoid HDD I/O contention)

## License

Inherits Apache-2.0 from the source dataset.
