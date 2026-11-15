---
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
pipeline_tag: text-generation
tags:
- mlx
- jang
- jang_6m
- quantized
- apple-silicon
- lfm3
- liquid
- osaurus
---

<p align="center"><a href="https://osaurus.ai"><img src="./osaurus-x-banner.png" alt="Osaurus AI"></a></p>

# OsaurusAI/LFM3-1.7B-JANG_6M

JANG_6M build of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) for Apple Silicon. LFM3 1.7B instruct: short-conv + full/sliding-attention hybrid, thinking on by default.

8-bit token mixers, 6-bit FFN, and every quantized matrix calibrated with GPTQ on the exact
storage grid plus activation-aware scaling, using calibration data weighted toward tool calls,
terminal agents, reasoning and code.

## Bundle

| | |
|---|---|
| Modalities | text |
| On-disk size | 1.55 GiB (one shard), float16 |
| Attention q/k/v/o, short-conv in/out projections | 8-bit affine, group 32, GPTQ |
| FFN w1 / w3 / w2 | 6-bit affine, group 32, AWQ + GPTQ |
| Tied embedding / lm_head | 8-bit affine, group 32 (it is the output head) |
| Kept at full precision | attention output gate, depthwise conv kernels, all norms |
| GPTQ | 142/142 tensors: fixed min-max grid (byte-identical layout to `mx.quantize`), act-order, Hessians accumulated over every calibration token, w2 Hessian rebuilt through the already-quantized w1/w3, best-of-RTN guard; mean calibration reconstruction error -52.7% vs round-to-nearest |
| AWQ | channel scales (alpha 0.25, clip 0.5-2) folded into `ffn_norm` and `w3` rows; function-preserving, no runtime cost |

## Calibration (556,418 tokens)

Every sample is rendered through the model's own chat template: structured `tools`, assistant
tool calls in LFM3's `<tool_call><function=...>` form, tool results as `tool` turns, and agent
thoughts inside `<think>`. Part of the set is the model's own answers (card sampling) to
reasoning, tool, terminal and coding prompts, so its serving distribution is in calibration.

| domain | tokens |
|---|---|
| tool calling (Hermes, native XML calls) | 167,615 |
| terminal / SWE agent trajectories | 175,655 |
| reasoning (long <think> traces) | 107,988 |
| coding and agentic text | 67,562 |
| general, science, systems, security, multilingual, long context | 37,598 |

## Measured against the bf16 source

58 held-out sequences never seen in calibration (13,494 scored
positions: tool calls, terminal and SWE agents, reasoning, code, general text).
KL divergence in nats per position (lower is better); top-1 is argmax agreement with bf16.

| build | size | KL median | KL mean | KL p95 | top-1 |
|---|---|---|---|---|---|
| **this bundle** | 1.55 GiB | 0.00015 | 0.00171 | 0.0067 | 98.58% |
| same layout, round-to-nearest | 1.55 GiB | 0.00021 | 0.00267 | 0.0094 | 98.38% |
| uniform 6-bit gs64 (mlx-vlm default recipe) | 1.31 GiB | 0.00055 | 0.00691 | 0.0247 | 97.53% |

## Use

- Runtimes with LFM3 support: vMLX / Osaurus (vmlx-swift with LFM3, Osaurus with LFM3 media
  support), and mlx-vlm with the LFM3 port.
- Thinking: on by default (`enable_thinking`). Tool calls: XML function format. Sampling defaults: temperature 0.1, top_k 50, repetition_penalty 1.1.
- License: LFM Open License v1.0 (see `LICENSE`), same as the base model.
