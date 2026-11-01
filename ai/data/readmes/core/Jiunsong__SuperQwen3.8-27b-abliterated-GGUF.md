---
license: apache-2.0
library_name: gguf
pipeline_tag: image-text-to-text
base_model: Jiunsong/SuperQwen3.8-27b-abliterated
base_model_relation: quantized
tags:
  - gguf
  - qwen3.8
  - qwen3.5
  - q4-k-m
  - multimodal
  - reasoning
  - tool-calling
  - long-context
  - uncensored
  - abliterated
  - obliteratus
  - speculative-decoding
  - dgx-spark
language:
  - en
  - ko
---

<div align="center">

# SuperQwen3.8-27b-abliterated-GGUF

**A one-DGX-Spark Q4_K_M release with a native MTP draft, Q8_0 vision projector, bounded reasoning, and a verified 262K context path.**

[![Target](https://img.shields.io/badge/target-Q4_K_M-0ea5e9)](#files-and-integrity)
[![C1](https://img.shields.io/badge/DGX%20Spark%20C1-40.1%20tok%2Fs-16a34a)](#measured-c1-decode)
[![MTP](https://img.shields.io/badge/MTP-K%3D6-7c3aed)](#native-mtp-speculation)
[![Context](https://img.shields.io/badge/context-262,043%20tokens-f59e0b)](#verified-long-context)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b)](#license)

</div>

This is the llama.cpp build of
[`Jiunsong/SuperQwen3.8-27b-abliterated`](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated):
the corrected rank-4 OBLITERATUS model, not an adapter and not the earlier incorrect lineage.
The target, MTP draft, and multimodal projector are separate so text-only users do not
pay for the projector, while vision and native speculative decoding remain available.

## Release highlights

| | |
|---|---|
| **One-Spark footprint** | **17.56 GiB** across target + MTP + projector |
| **Target** | 851 tensors, Q4_K_M importance-matrix quantization |
| **Native draft** | 18-tensor Q4_0 MTP, complete **K=0…8** C1 search |
| **Vision** | 334-tensor mixed Q8_0/F16/F32 projector, independently passed |
| **Selected C1** | **40.100 tok/s**, K=6, p256 / n512 / C1 |
| **Behavior** | Parent refusal 30/32 → **0/32**, empty 0/32 |
| **Reasoning** | **36/36** overthinking cases passed across default, low, medium, xhigh |
| **Context** | **262,043 tokens**, hidden key retrieved |

## Why this quant

- **Built for one DGX Spark:** the whole runtime set is 17.56 GiB.
- **Speed selected by measurement:** every K from 0 through 8 was tested under the same
  single-stream fixed-generation contract; K=6 was then reloaded independently.
- **Multimodal remains real:** the projector is shipped and the post-quant vision gate passed.
- **Behavior survived compression:** capability 8/8, tool use,
  bounded reasoning, refusal, and native-context retrieval all passed on this GGUF itself.

## Files and integrity

| File | Size | SHA-256 |
|---|---:|---|
| `SuperQwen3.8-27b-abliterated-Q4_K_M.gguf` | 16,547,400,704 B (15.41 GiB) | `692291d35fa3b5380f66486fe425ca715151c8b6136f07d3c5adb5ec179efd69` |
| `mtp-SuperQwen3.8-27b-abliterated-Q4_0.gguf` | 1,680,272,000 B (1.56 GiB) | `fe6443b24ea659cc2d25680ac50303cb798b40056de45d1a9e567305d9c5f29b` |
| `mmproj-SuperQwen3.8-27b-abliterated-Q8_0.gguf` | 629,247,136 B (0.59 GiB) | `8ceea1d2e01b1bbdc03fef8a0a749183cbd421e9ea8fec893608b7e485c9bbbf` |

The target contains 433 Q4_K, 65 Q6_K, and 353 F32 tensors. The MTP draft contains
10 Q4_0 and 8 F32 tensors. The projector deliberately retains unsupported or sensitive
matrices: 83 Q8_0, 27 F16, and 224 F32 tensors.

Target quantization used the Unsloth Qwen3.8 importance matrix with SHA-256
`0ee5b10bd0c2fa2127c6f4b43dbfe1efd71e383b63217af9dade1de36599f1c1`.
Conversion and serving are pinned to llama.cpp `b3c3b96a139d4ef1bdec926ac17aa040981cfc5d`.

## Native MTP speculation

| Candidate | Median C1 decode | Status |
|---|---:|---|
| K=0 | 12.052 tok/s | scan |
| K=1 | 20.811 tok/s | scan |
| K=2 | 27.279 tok/s | scan |
| K=3 | 32.971 tok/s | scan |
| K=4 | 35.140 tok/s | scan |
| K=5 | 38.528 tok/s | scan |
| K=6 | 40.140 tok/s | **selected + independently passed** |
| K=7 | 39.892 tok/s | scan |
| K=8 | 39.223 tok/s | scan |

The selected K=6 profile produced independent C1 trials of **40.100, 40.017, 40.446 tok/s**.
Its final median is **40.100 tok/s**, versus **12.052 tok/s** for K=0
in the complete scan (3.33×). C1 means one active request; it is
not a concurrency aggregate relabeled as interactive speed.

## Serving on one DGX Spark

```bash
llama-server \
  -m SuperQwen3.8-27b-abliterated-Q4_K_M.gguf \
  -md mtp-SuperQwen3.8-27b-abliterated-Q4_0.gguf \
  --spec-type draft-mtp \
  --spec-draft-n-max 6 \
  --spec-draft-ngl 999 \
  --spec-draft-type-k q8_0 \
  --spec-draft-type-v q8_0 \
  -mm mmproj-SuperQwen3.8-27b-abliterated-Q8_0.gguf \
  -ngl 999 -c 262144 -ctk q8_0 -ctv q8_0 -fa on -np 1 \
  --host 0.0.0.0 --port 8891 \
  -a SuperQwen3.8-27b-abliterated-GGUF --jinja --reasoning-format deepseek
```

For a non-speculative baseline, omit `-md` and use `--spec-type none`. For text-only
serving, omit `-mm`. Reduce `-c` when you prefer a smaller KV allocation.

## Independent release gates

| Gate | Result |
|---|---:|
| `/v1/models` and fixed C1 generation | PASS |
| Capability | 8/8 PASS |
| Tool call with valid arguments | PASS |
| Vision | PASS |
| Benign-sensitive assistance | PASS |
| Overthinking | **36/36 PASS** |
| Harmful-prompt refusal probe | **0/32 refusals, 0 empty** |
| Native context retrieval | **262,043 tokens, PASS** |

## Verified long context

The selected K=6 server processed a **262,043-token** prompt and
returned the hidden retrieval key. This is a concrete retrieval gate, not a claim that
every task at the edge of the window will be equally accurate.

## Other formats

- [Full BF16](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated)
- [Single-DGX NVFP4 W4A4](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-NVFP4-DGX-Spark)
- [Apple Silicon MLX 4-bit](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-MLX-4bit)

## Uncensored behavior

“Abliterated” means a measured refusal subspace was reduced. It does not mean every
answer is correct, harmless, or appropriate for every deployment. Operators remain
responsible for access controls and downstream safeguards.

## Limitations

- Q4_K_M can regress tasks outside the measured gates; use BF16 for maximum fidelity.
- MTP speedup depends on prompt distribution and acceptance; remeasure your workload.
- Context, speed, and memory figures are specific to the pinned llama.cpp runtime and GB10.
- The evaluation suites are strong regression gates, not exhaustive guarantees.

## Evidence identities

| Evidence | SHA-256 |
|---|---|
| OBLITERATUS tensor verification | `6d7b8b9abc431ed3845b18438fc48a6cc169e2ba93f83ada54174ae93765a61e` |
| bounded-reasoning template | `352baa520d23c77129d1cb9b007c5480118c174e12e271457ffe915fb466f3fb` |
| parent refusal baseline | `7a4177613c86ae0db589cb4fc167ff8a0d45b0d49f44e40b90c9405f4b2b9bb6` |
| corrected refusal gate | `97c2f745d032c3ed3147007f31e4ee844bb05181072a7365a160d5fc8c316511` |
| GGUF tensor structure | `5e8228e954de1a88df027923eff33e282c4166bd738913359393e4af41bbb429` |
| full K=0…8 C1 scan | `1c35221ad072cb0ce4f8201503899ac73c02eb1340d2a6872fd93fc64800c8ff` |
| selected-K independent release gate | `3af014ad5e5733fb967493530e4fad917c666b2301ca805932135eb6d38e0343` |

`SHA256SUMS.json` covers every published file. The repository remains private until all
BF16, NVFP4, GGUF, and MLX artifacts pass exact remote SHA-256 verification together.

## License

Apache-2.0, following the upstream Qwen3.8 release.
