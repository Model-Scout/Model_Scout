---
license: apache-2.0
base_model: Qwen/Qwen3-30B-A3B
tags:
  - nvfp4
  - quantized
  - modelopt
  - moe
pipeline_tag: text-generation
base_model_relation: quantized
library_name: transformers
language:
- en
- ko
---

# Qwen3-30B-A3B-NVFP4

NVFP4 (4-bit) quantization of Qwen/Qwen3-30B-A3B, produced with NVIDIA **modelopt 0.43.0**.
18.1 GB on disk against the 56.9 GB bf16 original.

This repository was published in May 2026 without a model card. This card was added on
2026-08-13 after we benchmarked the checkpoint; the numbers below describe the artifact that
has been sitting here, not a new build.

## Measured

Single B200, vLLM 0.27.1, lm-eval 0.4.12, full sets (MMLU n=14,042; GSM8K-CoT n=1,319,
8-shot). Every row was measured on the same GPU, engine and harness, so the columns are
comparable to each other.

| build | recipe | MMLU | GSM8K (strict) |
|---|---|---|---|
| Qwen3-30B-A3B (bf16 original) | — | **0.7779** | 0.8757 |
| ThakiCloud GPTQ NVFP4 | llm-compressor, GPTQ | 0.7643 | **0.8946** |
| **this model** | **modelopt 0.43.0** | **0.7624** | **0.8734** |
| ThakiCloud RTN NVFP4 | llm-compressor, RTN | 0.7619 | 0.8438 |
| RedHatAI/Qwen3-30B-A3B-NVFP4 | llm-compressor, RTN | 0.7611 | 0.8954 |

Harness standard error is ±0.34 points on MMLU and ±0.85 on GSM8K.

## What we expected, and what we got

We expected this checkpoint to be the weakest of the group. modelopt's default NVFP4 path
observes activation ranges and applies no weight-error correction, whereas GPTQ redistributes
each layer's rounding error using second-order statistics. We had written that gap up as a
reason our newer pipeline should supersede this one.

The measurement does not support that. On MMLU this checkpoint lands 0.19 points below our
GPTQ build — inside the harness standard error — and *above* our own RTN build. It gives up
about 2 points to GPTQ on GSM8K, which is the one place the expected ordering shows up.

So the honest summary is narrower than our prior claim: **GPTQ buys measurable ground on
multi-step generation, and is not distinguishable from modelopt on knowledge recall.** If you
already run this checkpoint, there is no MMLU reason to switch.

## Which GPU you measure on is part of the spec

The numbers above are from a Blackwell B200. FP4 tensor cores arrived with Blackwell; Hopper
(H100/H200) has none. An NVFP4 checkpoint still loads on Hopper, but the engine dequantises
the weights and computes at higher precision, which is a different arithmetic path and does
not produce the same scores. On a sibling model we measured the same file on both and the gap
to bf16 on MMLU moved by a full point purely from the hardware change. Treat any NVFP4
benchmark number as conditional on the GPU it was taken on, including these.

## Limitations

- Two benchmarks (MMLU, GSM8K-CoT). No coding, long-context, multilingual, or safety
  evaluation was run on this checkpoint.
- n=1 for this build. MMLU reproduced to four decimals across reruns of the sibling builds on
  this harness, so the MMLU figure is stable; the GSM8K figure carries the wider error above.
- Calibration details for this build were not recorded at production time in May 2026. We can
  state the tool and version from the checkpoint's own `quantization_config`, not the data.

## Provenance

`quantization_config.producer` reports `modelopt 0.43.0`, `quant_algo NVFP4`. The repository
also carries a `smoke_meta.json`, which indicates it was published from a smoke run.
