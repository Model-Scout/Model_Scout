---
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
tags:
  - vidraft
  - darwin
  - qwen3.6
  - qwen3_5_moe
  - a3b
  - moe
  - reasoning
  - gguf
  - korean
  - edge
language:
  - en
  - ko
pipeline_tag: text-generation
library_name: transformers
---

# Darwin-35B-A3B-Mythos

**A measured Qwen3.6-35B-A3B reasoning derivative — frontier-class quality with published benchmarks, Korean capability, and a real on-device story.** By VIDRAFT.

Most 35B-A3B derivatives on the hub ship a quant with no numbers. Darwin-35B-A3B-Mythos leads with **measured** results and stays fully reproducible under Apache-2.0.

## Highlights (all measured, labeled)

| Metric | Value | Method |
|---|---|---|
| GPQA Diamond | **86.4** | maj@8 |
| GPQA Diamond | **70.7** | greedy (single-pass) |
| On-device decode (VKUE) | **20.0 tok/s** | RTX 5060 Laptop 8GB, Q3_K_M, measured |
| vs dense 32B on same laptop | **3.7×** faster | measured A/B (dense 32B = 5.36 tok/s) |
| Datacenter throughput (VKAE) | **18,057 tok/s** aggregate | 1× B200, measured |

- **34.7B total / ~3B active** (A3B sparse MoE) — decode cost scales with the 3 active billion, so it is fast on small hardware.
- **Korean-capable** — no Korean-specialist model exists in the current trending set; Mythos speaks it.
- **Apache-2.0**, reproducible, honestly benchmarked.

## Files

| File | Quant | Size | Fits |
|---|---|---|---|
| `mythos-35b-Q4_K_M.gguf` | Q4_K_M | 21.2 GB | 24GB GPU / 32GB RAM |
| `mythos-35b-Q3_K_M.gguf` | Q3_K_M | 16.8 GB | 24GB card / laptop |
| `mythos-35b-Q2_K.gguf` | Q2_K | 12.9 GB | 16GB |
| `mythos-35b-IQ1_M.gguf` | IQ1_M (imatrix) | 8.2 GB | 12GB / edge |

Coming: MTP-GGUF (native multi-token-prediction head, for self-speculative decode), NVFP4, FP8.

## Run (llama.cpp)

Needs a recent llama.cpp build with `qwen35moe` support. Optimal on an 8GB card = experts on CPU, attention on GPU:

```bash
llama-cli -m mythos-35b-Q3_K_M.gguf -ngl 99 --n-cpu-moe 99 -c 8192 -p "..."
```

## What's in v1 vs roadmap (honest)

**v1 (this release):** the measured Qwen3.6-35B-A3B derivative above — GPQA 86.4/70.7, Korean, full GGUF ladder, VKUE on-device numbers. Text-only (the vision tower is not included in this build).

**Roadmap (not in v1 — will be labeled when shipped):** DELPHI test-time reasoning layer (token-efficient thinking), native function-calling SFT, extended context, restored vision (mmproj), MTP-GGUF / NVFP4 format parity, and a live demo Space. We ship numbers when they are measured, not before.

## Engines

- **VKUE** (ubiquity): the same weights run from a datacenter GPU down to an 8GB laptop — measured 20 tok/s on-device.
- **VKAE** (speed): VIDRAFT-optimized serving reaches 18,057 tok/s aggregate on a single B200 (measured).

Engine internals are proprietary; this card reports only measured results and standard open-tool run instructions.

## Notes

- `base_model: Qwen/Qwen3.6-35B-A3B` — Darwin-35B-A3B-Mythos is a VIDRAFT derivative of that base.
- Benchmarks are labeled by method (greedy vs maj@8); do not compare across methods.
- Not multimodal in v1 (text-only). Do not use for tasks requiring vision until the vision build ships.
