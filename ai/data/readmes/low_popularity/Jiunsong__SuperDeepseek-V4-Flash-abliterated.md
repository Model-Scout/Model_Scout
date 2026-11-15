---
license: mit
library_name: transformers
pipeline_tag: text-generation
base_model: deepseek-ai/DeepSeek-V4-Flash-0731
base_model_relation: finetune
tags:
  - deepseek-v4
  - mixture-of-experts
  - fp4
  - fp8
  - bf16
  - mixed-precision
  - long-context
  - 1m-context
  - reasoning
  - tool-calling
  - uncensored
  - vllm
  - abliterated
  - obliteratus
  - supertune
language:
  - en
  - ko
---

<div align="center">

# SuperDeepseek-V4-Flash-abliterated

**A less-refusing DeepSeek V4 Flash full checkpoint with verified 1M-token retrieval, intact tool use, and 123 tok/s-class two-node decode.**

[![Format](https://img.shields.io/badge/format-native%20FP4%20%2B%20FP8%20%2B%20BF16-0ea5e9)](#checkpoint-format-and-precision)
[![Context](https://img.shields.io/badge/verified%20context-1%2C028%2C621%20tokens-7c3aed)](#verified-long-context)
[![Decode](https://img.shields.io/badge/aggregate%20decode-123.3%20tok%2Fs-16a34a)](#measured-performance)
[![Tools](https://img.shields.io/badge/tool%20gates-100%25-0f766e)](#behavior-and-capability)
[![License](https://img.shields.io/badge/license-MIT-64748b)](#license)

</div>

SuperDeepseek-V4-Flash-abliterated is the general, independently downloadable full-checkpoint release of SuperDeepseek. It is built from [`deepseek-ai/DeepSeek-V4-Flash-0731`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731), keeps DeepSeek's official native tensor layout, and fuses the selected OBLITERATUS + SuperTune update directly into the checkpoint. No LoRA or inference-time adapter is required.

## Why this release

- **Far fewer unnecessary refusals:** worst-mode refusal fell from **97.92% to 4.17%** in the paired gate.
- **Tools stayed intact:** tool compliance and correct-tool selection both remained **100%**.
- **Real 1M-context proof:** a **1,028,621-token** prompt was accepted and its hidden needle was retrieved.
- **Fast verified serving:** the released weights reached **123.35 aggregate tok/s** on forced decode and **123.28 aggregate tok/s** on structured tool generation.
- **Surgical weight edit:** all 256 routed experts, routers, embeddings, mHC tensors, and untargeted parent tensors preserve their official representation.

## Release at a glance

| | |
|---|---|
| **Architecture** | DeepSeek V4 Flash, 304B-class MoE, 43 backbone + 3 MTP layers, 256 routed experts, top-6 |
| **Checkpoint** | Complete Transformers/safetensors checkpoint, about 169.5 GB, 48 parent shards plus fused SuperDeepseek overlays |
| **Native precision** | FP4 experts + FP8 E4M3 block-quantized paths + BF16 quality-sensitive paths |
| **Targeted update** | 46 `attn.wo_b` weight/scale pairs plus one bounded BF16 output-head recovery |
| **Context** | 1,048,576 configured; 1,028,621 actual prompt tokens accepted and retrieved |
| **Decode** | 123.3459 forced / 123.2819 structured-tool aggregate tok/s at p256/C6 |
| **Behavior** | Worst-mode refusal 97.92% -> 4.17%; tool gates 100% |

## Checkpoint format and precision

This is the **native-format full checkpoint**, not a full-BF16 reconstruction. DeepSeek's official V4 Flash checkpoint is itself hybrid precision; no authentic all-BF16 upstream checkpoint is published. This release deliberately preserves that official representation instead of dequantizing it and presenting approximated BF16 weights as “original.”

| Component | Precision / storage |
|---|---|
| MoE expert weights | **FP4**, inherited from the official `expert_dtype=fp4` layout |
| Block-quantized paths | **FP8 E4M3**, dynamic activation scaling, 128x128 blocks, UE8M0 scales |
| 43 backbone + 3 MTP `attn.wo_b` updates | Deterministic **FP8** weight/scale overlay, 92 tensors |
| Default unquantized and quality-sensitive paths | **BF16** (`torch_dtype=bfloat16`), with upstream F32 metadata/normalization where defined |
| Output-head recovery | One bounded **BF16** `head.weight` overlay, rank 64, relative Frobenius delta 0.0025 |
| Verified serving KV cache | **NVFP4 DS-MLA** |

The parent is pinned to `deepseek-ai/DeepSeek-V4-Flash-0731@9e165c30e2704aec5d9d593cce3eebd58bbef1cb`. All 48 parent shard identities were checked against that revision.

For the release name and scripts tuned specifically for a two-node DGX Spark deployment, see [`Jiunsong/SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX`](https://huggingface.co/Jiunsong/SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX). Both repositories contain the same released SuperDeepseek weights; this repository is the general/native-layout edition, while the sibling makes the measured MQ + 2xDGX deployment target explicit in its name.

## What changed

The release uses two measured refusal-subspace passes:

1. A robust rank-1 direction fitted across chat, think-high, and think-max modes, applied at strength 2.
2. A second rank-1 residual direction recaptured from the baked first pass, orthogonalized against it, and applied at strength 0.5.
3. A bounded rank-64 output-head recovery with relative Frobenius delta 0.0025.

The final checkpoint changes only the 43 backbone and three MTP `attn.wo_b` weight/scale pairs plus the bounded output head. The routed experts remain untouched.

## Behavior and capability

| Metric | Official parent | SuperDeepseek |
|---|---:|---:|
| Worst-mode refusal | 97.92% | **4.17%** |
| Worst empty answer | 0.00% | **0.00%** |
| Worst tool compliance | 100.00% | **100.00%** |
| Worst correct-tool rate | 100.00% | **100.00%** |
| Minimum capability mean | 0.9375 | **0.9583** |

The independently reloaded checkpoint reproduced the selected candidate's deterministic validation behavior. The release gate covered empty output, Unicode, repetition, serialization, reasoning, code, formatting, tool selection, and structured tool calls.

## Measured performance

These are **aggregate concurrent post-first-token decode** rates, not single-stream numbers. Six distinct prompts, fixed-length generation, and the sealed [sparkDash](https://github.com/MiaAI-Lab/sparkDash)-style p256/C6 contract were used.

| Workload | Prompt / concurrency | Three trials | Median |
|---|---:|---:|---:|
| Forced output | p256 / C6 | 117.7944, 123.3459, 125.9469 tok/s | **123.3459 tok/s** |
| Structured tool output | p256 / C6 | 123.6285, 123.2819, 117.1843 tok/s | **123.2819 tok/s** |

The benchmark follows sparkDash commit `dfde4214f32b174880832a4d317d3c0567750ac5`. Hardware and runtime were 2x NVIDIA DGX Spark / GB10, TP=2, direct CX-7 RoCEv2, vLLM, FlashInfer b12x MoE, DSpark K=1 speculative decoding, and NVFP4 DS-MLA KV cache. Hardware-specific figures should not be assumed on other systems.

## Verified long context

| Actual prompt tokens | Accepted | Needle retrieved |
|---:|:---:|:---:|
| 149,845 | Yes | Yes |
| **1,028,621** | **Yes** | **Yes** |

The configured maximum is 1,048,576 tokens. These are end-to-end acceptance and retrieval probes, not a claim of perfect recall for every task or needle position.

## Two-node reference serving

The verified profile uses TP=2 over direct CX-7 RoCEv2 with the `ghcr.io/anemll/dspark-vllm-gx10:0.1.1` runtime:

```bash
vllm serve /model \
  --served-model-name SuperDeepseek-V4-Flash-abliterated \
  --tensor-parallel-size 2 \
  --max-model-len 1048576 \
  --kv-cache-dtype nvfp4_ds_mla \
  --moe-backend flashinfer_b12x \
  --enable-prefix-caching \
  --async-scheduling \
  --enable-chunked-prefill \
  --speculative-config '{"method":"dspark","num_speculative_tokens":1,"draft_sample_method":"greedy"}'
```

The exact two-rank launcher and machine-readable release evidence are included under `repro/` and `evidence/`.

## Integrity

- Parent revision: `9e165c30e2704aec5d9d593cce3eebd58bbef1cb`
- 48 parent shard names and hashes verified
- 92 FP8 overlay tensors: exactly 46 `attn.wo_b` weight/scale pairs
- One bounded BF16 output-head tensor
- Independent reload, paired validation, decode, reasoning, tool, long-context, and output-integrity gates passed

| Artifact | SHA-256 |
|---|---|
| SuperDeepseek FP8 overlay | `86c8494d0b02a01ccb4d4de5ad48a66d26f56341e1dd3eb17eb61b40710f73ba` |
| BF16 head-recovery overlay | `3d49e3e05ba864666054328f475058a9558603aac70d1a191b352be65bce1428` |
| Sealed throughput report | `1cd7734205f4d03cddf241d5ed2a5f423f402d194222c9abc3bdacc965cce370` |
| 1M-context evidence | `6745453ee65b9e59581d715bf668bc710b0bc680fe726763e9a750dd25f45565` |

## Responsible use and limitations

“Abliterated” describes a measured reduction of the selected refusal subspace. It does not make every answer correct, remove the need for deployment controls, or transfer responsibility away from the operator. The capability suites are finite regression gates, and the upstream model's license and limitations continue to apply.

## License

MIT, following the upstream DeepSeek V4 Flash release.
