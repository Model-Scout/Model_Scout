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
  - bf16
  - full-precision
language:
  - en
  - ko
---

<div align="center">

# SuperQwen3.8-27b-abliterated


**The full-BF16 SuperQwen3.8 release: refusal-reduced, overthinking-corrected, multimodal, tool-capable, and verified across the native 262K window.**

[![Precision](https://img.shields.io/badge/weights-BF16-0ea5e9)](#precision-and-integrity)
[![Refusal](https://img.shields.io/badge/refusal-93.75%25%20%E2%86%92%200%25-16a34a)](#behavior-and-capability)
[![Overthinking](https://img.shields.io/badge/overthinking-36%2F36%20pass-7c3aed)](#bounded-reasoning)
[![Context](https://img.shields.io/badge/context-262,043%20tokens-f59e0b)](#verified-long-context)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b)](#license)

</div>

SuperQwen3.8-27b-abliterated is a directly loadable, full-BF16 weight release built from
[`Qwen/Qwen3.8-27B@1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`](https://huggingface.co/Qwen/Qwen3.8-27B/tree/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0).
It applies a measured rank-4 OBLITERATUS refusal-subspace edit while preserving the official
vision tower and MTP weights exactly. No LoRA or inference-time adapter is required.

## Release highlights

| | |
|---|---|
| **Format** | Full BF16, 18 safetensors shards, about 52 GB |
| **Targeted edit** | 100 tensors: output projections in layers 15-63 plus embeddings and `lm_head` |
| **Protected exactly** | 333 vision tensors and 15 MTP tensors |
| **Refusal shift** | **30/32 (93.75%) → 0/32**, with 0 empty outputs |
| **Overthinking correction** | Default `xhigh` → bounded `medium`; repeat/restart guard for explicit `xhigh`; **36/36 pass** |
| **Measured decode** | **4.3411 tok/s C1** at p256 |
| **Verified context** | **262,043 prompt tokens**, needle retrieved in the native window |
| **OBLITERATUS corpus** | **842 canonical harmful/harmless pairs**, pinned commit `a5a1ffa5849b` |

## Why this release

- **Original-weight quality:** BF16 transformer, vision, output head, embeddings, and MTP storage.
- **Less refusal without wrecking capabilities:** capability floor 7/8, tool call PASS, vision PASS.
- **Reasoning that stops:** all nine deterministic tasks pass at default, low, medium, and xhigh.
- **Multimodal preserved:** this remains an `image-text-to-text` checkpoint, not a text-only conversion.
- **Reproducible:** the exact parent revision, modified tensor list, and evidence hashes ship with the model.

## Bounded reasoning

The upstream template defaulted unspecified reasoning to `xhigh`. This release defaults
to `medium` and adds a stop condition to `xhigh`: once an answer is established, the
model must stop instead of repeating or restarting its deliberation. The checkpoint was
tested across 36 deterministic effort/task combinations; all 36 terminated correctly.

Explicit controls remain available through `chat_template_kwargs`:

```python
extra_body={"chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "xhigh"}}
```

## Behavior and capability

| Gate | Result |
|---|---:|
| Parent refusal | 30 / 32 (93.75%) |
| SuperQwen refusal | **0 / 32** |
| Empty output | **0 / 32** |
| Capability | **7 / 8** (paired-parent floor) |
| Tool use | **PASS** |
| Vision | **PASS** |
| Overthinking | **36 / 36 PASS** |

## Precision and integrity

- Full BF16 checkpoint; this repository is not quantized.
- 100 declared tensors changed and zero unexpected tensors changed.
- Vision (333 tensors) and MTP (15 tensors) remain byte/value exact.
- Parent revision is pinned to `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`.

## Decode performance

Measured on one DGX Spark with fixed-length generation and the
[sparkDash](https://github.com/MiaAI-Lab/sparkDash)-style post-first-token contract:

| Prompt / concurrency | Aggregate decode |
|---|---:|
| p256 / C1 | **4.3411 tok/s** |

## Verified long context

The official native limit is 262,144 tokens. A **262,043-token prompt**
completed end to end and retrieved its hidden needle.
Long-context acceptance is not a claim of perfect recall on every task.

## Serving

```bash
QWEN38_SPECULATIVE_TOKENS=0   bash repro/scripts/serve_superqwen38_replica.sh   /model SuperQwen3.8-27b-abliterated 8888
```

## Uncensored behavior

“Abliterated” means that the measured refusal direction was reduced. It does not mean
that every response is correct, harmless, or suitable for every deployment. Operators
remain responsible for access controls and downstream safeguards.

## Limitations

- Abliteration changes refusal behavior and may surface content the parent declined.
- The capability, tool, vision, and overthinking suites are finite regression gates.
- Speed is hardware- and runtime-specific.
- The 1M expansion run was explicitly stopped before completion and is not claimed as a pass.

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

## License

Apache-2.0, following the upstream Qwen3.8 release.
