---
license: cc-by-4.0
language:
- ko
- en
pretty_name: K-Guard Korean MoE Calibration v1
size_categories:
- 10K<n<100K
tags:
- mixture-of-experts
- calibration
- reap
- expert-routing
- korean
- qwen3.6
---

# K-Guard Korean MoE Calibration v1

> Korean dataset card: [README_ko.md](./README_ko.md)

This repository contains the Korean-centered calibration mixture and the
corresponding Qwen3.6 MoE observation table used for the K-Guard REAP 12.5%
and 25% MLX releases.

## Files

| Path | Description |
|---|---|
| `data/qwen3_6_text_24576.jsonl.gz` | 24,576 deterministic calibration records |
| `observation/qwen36-seed17-observer-results.csv` | Per-layer/per-expert routing and activation statistics, 10,240 rows |
| `metadata/observation.json` | Sanitized observation configuration and checksums |

## Composition

| View | Records |
|---|---:|
| General Korean instruction and reasoning | 8,192 |
| Korean-English semantic pairs | 8,192 |
| General capability replay | 4,096 |
| Qwen3.6 text and reasoning | 4,096 |
| **Total** | **24,576** |

The records are synthetic and deterministically generated. They cover Korean
instructions, reasoning, bilingual alignment, code and structured output,
tool-style prompts, and general capability replay. Calibration and evaluation
splits were built separately.

## Observation configuration

- Model family: Qwen3.6-35B-A3B 8-bit MLX
- Architecture: `qwen3_5_moe`
- MoE layers: 40
- Routed experts per source layer: 256
- Active routed experts per token: 8
- Observation seed: 17
- Maximum samples: 24,576
- Maximum sequence length: 8,192
- Importance field used for the releases: `reap`

The CSV is display- and analysis-friendly. Each row contains a layer ID, expert
ID, activation statistics, routing frequency/probability, and the final REAP
importance value.

## Loading the calibration records

```python
import gzip
import json

with gzip.open("data/qwen3_6_text_24576.jsonl.gz", "rt", encoding="utf-8") as f:
    first_record = json.loads(next(f))

print(first_record.keys())
```

## Related models

- [`eouya2/Qwen3.6-35B-A3B-KGuard-REAP12.5-8bit-MLX`](https://huggingface.co/eouya2/Qwen3.6-35B-A3B-KGuard-REAP12.5-8bit-MLX)
- [`eouya2/Qwen3.6-35B-A3B-KGuard-REAP25-8bit-MLX`](https://huggingface.co/eouya2/Qwen3.6-35B-A3B-KGuard-REAP25-8bit-MLX)

## License

The synthetic data and observation table are released under CC BY 4.0.
