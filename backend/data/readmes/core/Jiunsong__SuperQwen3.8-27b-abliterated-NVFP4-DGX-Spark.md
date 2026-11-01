---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
base_model: Qwen/Qwen3.8-27B
base_model_relation: finetune
tags:
  - qwen3.8
  - qwen3.5
  - multimodal
  - image-text-to-text
  - reasoning
  - tool-calling
  - long-context
  - 262k-context
  - uncensored
  - abliterated
  - obliteratus
  - supertune
  - vllm
  - nvfp4
  - w4a4
  - quantized
  - dgx-spark
  - speculative-decoding
language:
  - en
  - ko
---

<div align="center">

# SuperQwen3.8-27b-abliterated-NVFP4-DGX-Spark


**The single-DGX Spark performance release: true W4A4 NVFP4, quality-gated speculative decoding, corrected overthinking, and verified native 262K retrieval.**

[![Precision](https://img.shields.io/badge/precision-NVFP4%20W4A4%20G16-0ea5e9)](#quantization-and-integrity)
[![Decode](https://img.shields.io/badge/single%20DGX%20C1-25.8%20tok%2Fs-16a34a)](#decode-performance)
[![Overthinking](https://img.shields.io/badge/overthinking-36%2F36%20pass-7c3aed)](#bounded-reasoning)
[![Context](https://img.shields.io/badge/context-262,043%20tokens-f59e0b)](#verified-long-context)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b)](#license)

</div>

SuperQwen3.8-27b-abliterated-NVFP4-DGX-Spark is the performance-focused compression of
[`Jiunsong/SuperQwen3.8-27b-abliterated`](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated). It uses
compressed-tensors **W4A4 NVFP4 with group size 16**, preserves quality-sensitive
paths in BF16, and ships with the MTP layer required for Qwen speculative decoding.

## Release highlights

| | |
|---|---|
| **Format** | True NVFP4 W4A4, group size 16; 5 packed shards + 1 BF16 MTP shard; about 19.15 GiB |
| **Protected exactly** | Vision, MTP, conv1d, and `lm_head` |
| **Calibration** | 32 × 8,192-token samples, deterministic seed 38027 |
| **Stable speculative default** | **K=5**, TRITON draft attention; quality-selected after a complete K=0…7 C1 scan |
| **Single-node decode** | **25.7592 tok/s C1** at p256 |
| **Behavior** | Refusal **30/32 → 0/32**, tool PASS, vision PASS, overthinking **36/36** |
| **Context** | Native **262,043-token** retrieval at K=5 |

## Why run this model

- **Measured single-stream speedup over BF16 on the same DGX Spark:** 4.3411 → 25.7592 tok/s.
- **Speculative decoding without quality theater:** all K=0…7 candidates are C1-measured, and only the fastest independently passing depth is released (**K=5**).
- **Overthinking corrected:** bounded default reasoning and an explicit xhigh stop guard, verified 36/36.
- **Multimodal and tools preserved:** vision tensors, tool behavior, and the output head pass their release checks.

## Quantization and integrity

| Component | Precision / treatment |
|---|---|
| Eligible linear weights and activations | **NVFP4 W4A4**, group size 16 |
| Vision tower | Protected, exact |
| MTP | BF16 protected shard, exact |
| `conv1d` paths | Protected, exact |
| `lm_head` | BF16, exact |
| Serving KV cache | FP8 in the measured profile |

Structural verification covers 496 packed tensors: 64 full-attention, 192 MLP,
and 240 linear-attention tensors. The index and every packed shard are identified by
SHA-256 under `evidence/`. The full provenance chain is pinned to
`Qwen/Qwen3.8-27B@1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`.

## Stable speculative decoding

All K values from 0 through 7 were measured under the same C1 fixed-generation
contract. Independently reloaded K=5 passed:

- capability 7/8, tool PASS, vision PASS
- refusal 0/32 and empty 0/32
- overthinking 36/36 across default, low, medium, xhigh
- native 262,043-token needle retrieval

Use **K=5 through the native 262K window**. The official MTP draft
configuration is limited to 262,144 tokens.

## Bounded reasoning

Unspecified reasoning now defaults to bounded `medium`, not upstream `xhigh`. Explicit
`xhigh` remains available but carries a repeat/restart stop condition. This targets the
common failure mode where a correct answer is found and then reconsidered into a wrong
or needlessly long answer.

## Decode performance

The contract follows [sparkDash](https://github.com/MiaAI-Lab/sparkDash): aggregate
post-first-token decode, distinct prompts, fixed-length output, thinking disabled.

| Topology | Prompt / concurrency | Aggregate decode |
|---|---:|---:|
| 1× DGX Spark, K=5 | p256 / C1 | **25.7592 tok/s** |

This is a real one-request C1 decode measurement, not an aggregate concurrency number.
The 27B checkpoint fits and serves on one DGX Spark; a second node is not required.

## Verified long context

| Runtime | Actual prompt tokens | Needle retrieved |
|---|---:|:---:|
| Native, K=5 | 262,043 | Yes |

## Serving

```bash
QWEN38_SPECULATIVE_TOKENS=5   QWEN38_MAX_MODEL_LEN=262144   bash repro/scripts/serve_superqwen38_replica.sh   /model SuperQwen3.8-27b-abliterated-NVFP4-DGX-Spark 8888
```

The measured profile uses TRITON attention, FP8 KV cache, prefix caching, asynchronous
scheduling, chunked prefill, and eager execution. See `repro/` for the exact launcher.

## Uncensored behavior

“Abliterated” means the measured refusal direction was reduced. It is not a claim of
universal truthfulness or safety. Operators remain responsible for policy and access
control appropriate to their deployment.

## Limitations

- W4A4 compression can regress tasks outside the measured gates.
- Non-selected K values remain diagnostic profiles; the default is the fastest candidate
  that passed the independent capability, tool, vision, refusal, context, and 36-case
  overthinking gate.
- MTP speculative decoding is bounded to its native 262,144-token draft configuration.
- The 1M expansion run was explicitly stopped before completion and is not claimed as a pass.
- Throughput figures are specific to the measured DGX Spark runtime.

## Evidence identities

| Evidence | SHA-256 |
|---|---|
| abliteration verification | `6d7b8b9abc431ed3845b18438fc48a6cc169e2ba93f83ada54174ae93765a61e` |
| abliteration recipe | `3c057cf9364e72857d9a48b6c8888c6b438cbfb519459dcdfbf23b22c2bc6796` |
| 842-pair OBLITERATUS corpus manifest | `be770a8469fafe7a9a76db5d82a7893c706c4414e1de6089f1d329b906480aa8` |
| bounded-thinking template | `352baa520d23c77129d1cb9b007c5480118c174e12e271457ffe915fb466f3fb` |
| parent refusal baseline | `7a4177613c86ae0db589cb4fc167ff8a0d45b0d49f44e40b90c9405f4b2b9bb6` |
| BF16 release gate | `38a7093ce40a9aca2fc5e4389c041660ff56c51a4caec8411998a6d02ed48bc5` |
| BF16 refusal gate | `97c2f745d032c3ed3147007f31e4ee844bb05181072a7365a160d5fc8c316511` |
| BF16 native 262K retrieval | `01fdbc4bf458f457b9e403ff9fd43b72124b11b448f02bda4e9701eefccfe814` |
| User-authorized 1M skip (not a pass) | `a2c94a799d483e313debc1e9fb5e0fa234913c9e1c9fa503b8c466d70ad53dee` |
| NVFP4 provenance | `e4b5f7e956848a35990412cdd12d745b4761711e40f2cb1cb95087263fef261a` |
| stable MTP selection | `531940c9e04c1f89f11be4bd48dd0e8e88306fb0a4cb0f3528c1836a87ff24c4` |

## License

Apache-2.0, following the upstream Qwen3.8 release.
