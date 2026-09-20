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
  - quantized
  - long-context
  - 1m-context
  - reasoning
  - tool-calling
  - uncensored
  - vllm
  - obliteratus
  - supertune
  - dgx-spark
language:
  - en
  - ko
---

<div align="center">

# SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX

**A fast, less-refusing DeepSeek V4 Flash with mixed quantization (MQ), verified 1M-token retrieval, and 123 tok/s-class aggregate decode on two DGX Spark nodes.**

[![Precision](https://img.shields.io/badge/precision-FP4%20%2B%20FP8%20%2B%20BF16-0ea5e9)](#quantization-and-precision)
[![Context](https://img.shields.io/badge/context-1%2C048%2C576-7c3aed)](#verified-long-context)
[![Decode](https://img.shields.io/badge/aggregate%20decode-up%20to%20123.3%20tok%2Fs-16a34a)](#decode-performance)
[![Tools](https://img.shields.io/badge/tool%20gate-100%25-0f766e)](#behavior-and-capability)
[![License](https://img.shields.io/badge/license-MIT-64748b)](#license)

</div>

SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX is the performance-focused SuperDeepseek release built from
[`deepseek-ai/DeepSeek-V4-Flash-0731`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731).
It keeps the official hybrid checkpoint layout, applies a surgical OBLITERATUS +
SuperTune update, and ships as a directly loadable checkpoint with no LoRA or runtime
adapter required.

## Release highlights

| | |
|---|---|
| **Architecture** | DeepSeek V4 Flash, 304B-class MoE, 43 backbone layers + 3 MTP layers, 256 routed experts, top-6 |
| **Release format** | Hybrid FP4 experts + FP8 E4M3 blocks + BF16 quality-sensitive tensors, about 169.5 GB on the Hub |
| **Targeted update** | 46 `attn.wo_b` weight/scale pairs, with all routed experts and untargeted parent tensors preserved |
| **Verified context** | 1,048,576 configured; 1,028,621-token prompt accepted with successful needle retrieval |
| **Aggregate decode** | **118.6 tok/s** forced output and **123.3 tok/s** structured tool output at p256/C6 |
| **Behavior shift** | Worst-mode refusal **97.92% -> 4.17%**, while the measured tool gates remain **100%** |
| **Capability floor** | Minimum capability mean **0.9375 -> 0.9583** against the pinned parent |

## Why run this model

- **Far fewer unnecessary refusals:** the selected checkpoint reduces the measured
  worst-mode refusal rate from 97.92% to
  4.17%.
- **Tools stay intact:** tool compliance and correct-tool selection remain at
  100.00% and
  100.00% in the paired release gate.
- **Real 1M context proof:** both 149,845-token and 1,028,621-token needle-retrieval
  requests completed successfully.
- **Fast on two DGX Spark nodes:** the measured serving profile reaches
  123.3 aggregate tok/s on structured tool generation.
- **Surgical rather than destructive:** experts, routers, embeddings, mHC tensors,
  and every untargeted parent tensor retain the official checkpoint representation.

## Quantization and precision

`MQ` in the model name means **mixed quantization**. This is an
**official-layout mixed-precision checkpoint**, not a full-BF16 release and not a
custom whole-model requantization.

| Component | Precision / storage |
|---|---|
| MoE expert weights | **FP4**, inherited from the official `expert_dtype=fp4` checkpoint layout |
| Block-quantized paths | **FP8 E4M3**, dynamic activation scaling, 128x128 weight blocks, UE8M0 scales |
| 43 backbone + 3 MTP `attn.wo_b` updates | Deterministic **FP8** weight/scale overlay, 92 tensors |
| Default unquantized and quality-sensitive paths | **BF16** (`torch_dtype=bfloat16`) with F32 metadata/normalization where defined upstream |
| Output head recovery | One bounded **BF16** `head.weight` overlay, rank-64, relative Frobenius delta 0.0025 |
| Measured serving KV cache | **NVFP4 DS-MLA** |

The parent checkpoint is pinned to `9e165c30e2704aec5d9d593cce3eebd58bbef1cb`. Only the declared FP8
`attn.wo_b` pairs and the single bounded BF16 output head are redirected by the final
weight index; the remaining parent tensors keep their original quantization and bytes.

## What was changed

The release uses two measured weight-space passes:

1. OBLITERATUS fits a robust rank-1 refusal direction across chat,
   think-high, and think-max modes and applies the selected strength
   2.
2. A second rank-1 residual pass is recaptured from the baked first pass,
   orthogonalized against it, and applied at strength
   0.5.
3. A bounded rank-64 output-head recovery was applied; its relative Frobenius delta was 0.0025.

The final checkpoint modifies only the 43 backbone and three MTP `attn.wo_b`
weight/scale pairs plus the bounded output head. There is no inference-time adapter.

## Behavior and capability

| Metric | Official parent | SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX |
|---|---:|---:|
| Worst-mode refusal | 97.92% | **4.17%** |
| Worst empty answer | 0.00% | 0.00% |
| Worst tool compliance | 100.00% | **100.00%** |
| Worst correct-tool rate | 100.00% | **100.00%** |
| Minimum capability mean | 0.9375 | **0.9583** |

The independently reloaded checkpoint reproduced the selected candidate's deterministic
validation behavior exactly. Empty-output, Unicode, repetition, serialization,
reasoning, code, formatting, and tool-use sentinels were included in the release gate.

## Decode performance

The numbers below are aggregate concurrent decode throughput, not single-stream speed.
They use six distinct prompts, fixed-length generation, and the sealed
[sparkDash](https://github.com/MiaAI-Lab/sparkDash)-style measurement contract at commit
`dfde4214f32b174880832a4d317d3c0567750ac5`.

| Workload | Prompt / concurrency | Aggregate decode |
|---|---:|---:|
| Forced output | p256 / C6 | **118.5505 tok/s** |
| Structured tool output | p256 / C6 | **123.2888 tok/s** |

- Median matched decode ratio vs the parent: **1.0012x**
- Minimum matched-case ratio vs the parent: **0.9627x**
- Regular CUDA graphs vs breakable: **1.2125x** at C1 and **1.2674x** at C6

## Verified long context

| Actual prompt tokens | Accepted | Needle retrieved |
|---:|:---:|:---:|
| 149,845 | Yes | Yes |
| **1,028,621** | **Yes** | **Yes** |

The configured maximum is 1,048,576 tokens. These are end-to-end acceptance and
retrieval probes; they are not a claim that every task benefits equally from the full
window.

## Two-node DGX Spark serving

The measured profile uses TP=2 over direct CX-7 RoCEv2 with the
`ghcr.io/anemll/dspark-vllm-gx10:0.1.1` runtime:

- NVFP4 DS-MLA KV cache
- DSpark speculative decoding with K=1 and greedy draft sampling
- FlashInfer b12x MoE and FlashInfer autotuning
- prefix caching, asynchronous scheduling, and chunked prefill
- regular CUDA graphs with `VLLM_USE_BREAKABLE_CUDAGRAPH=0`

The repository includes the exact two-rank launcher under
`repro/scripts/serve_superdeepseek_v4_dual.sh`. Its measured model-facing options are:

```bash
vllm serve /model \
  --served-model-name SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX \
  --tensor-parallel-size 2 \
  --max-model-len 1048576 \
  --kv-cache-dtype nvfp4_ds_mla \
  --moe-backend flashinfer_b12x \
  --enable-prefix-caching \
  --async-scheduling \
  --enable-chunked-prefill \
  --speculative-config '{"method":"dspark","num_speculative_tokens":1,"draft_sample_method":"greedy"}'
```

After the server is ready, it exposes an OpenAI-compatible API:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8888/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="SuperDeepseek-V4-Flash-abliterated-MQ-2xDGX",
    messages=[{"role": "user", "content": "Design a reliable tool-using agent."}],
    max_tokens=1024,
)
print(response.choices[0].message.content)
```

## Uncensored behavior

“Uncensored” means this checkpoint measurably reduces the selected refusal subspace
while retaining the declared capability and output-integrity gates. It does not imply
that every answer is correct or that downstream deployment controls are unnecessary.

## Release integrity

- Parent: `deepseek-ai/DeepSeek-V4-Flash-0731@9e165c30e2704aec5d9d593cce3eebd58bbef1cb`
- 48 original parent shard names preserved
- 92 FP8 overlay tensors: exactly 46 `attn.wo_b` weight/scale pairs
- 1 bounded BF16 output-head tensor
- Independently reloaded paired validation: passed
- Decode, tool, reasoning, long-context, and output-integrity gates: passed
- Machine-readable benchmark and release evidence included under `evidence/`

## Limitations

- The speed figures are measured on a specific two-node DGX Spark/CX-7 runtime and
  should not be treated as universal hardware results.
- Abliteration changes refusal behavior and can produce content the parent would
  decline. Operators remain responsible for access control and appropriate use.
- The capability and integrity suites are finite regression gates, not proof of
  universal correctness.
- One million token acceptance does not guarantee perfect recall at every position or
  on every task.
- The parent model's license and upstream limitations continue to apply.

## Evidence identities

| Evidence | SHA-256 |
|---|---|
| paired validation | `65aaf03e1ac5f88ea462c7500d36a06c254370dfa3f9e2a0d24183c482e23a46` |
| phase 1 selection | `a75b0f9c2c2c9d0c38e94c5a7e36139509178f7f9b74521925c9a1f011f0f207` |
| phase 2 selection | `b0fdb2c73f16954b56bde2460833b782b29bfe0a67aeedc611d65dc94764e4eb` |
| recovery decision | `39acc4c24694c7bb08615217d16e5e7d2f3d9e33c26425610ff1198054422a2f` |
| decode benchmark | `6745453ee65b9e59581d715bf668bc710b0bc680fe726763e9a750dd25f45565` |
| overlay audit | `c618a1a2da8295b07b1d93d9a59c9a66e8e430c2b8bdf1aca07a56ad56455e8e` |
| head recovery audit | `a5aa6531909444a5d6199d889030b6b9424868a7656e4db8d77c30aad4bfc8db` |

## License

MIT, following the upstream DeepSeek V4 Flash release.
