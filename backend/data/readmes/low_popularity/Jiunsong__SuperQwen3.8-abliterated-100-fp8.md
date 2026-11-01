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
  - uncensored
  - abliterated
  - obliteratus
  - fp8
  - w8a8
  - compressed-tensors
  - vllm
  - h100
  - h200
  - speculative-decoding
language:
  - en
  - ko
---

<div align="center">

<img src="./assets/superqwen38-hero.svg" alt="SuperQwen3.8 — refusal-reduced Hopper FP8" width="100%">

# SuperQwen3.8-abliterated-100-fp8

<p><em>A business-oriented, refusal-reduced Qwen3.8-27B release in native Hopper FP8 W8A8 format.</em></p>

[![Precision](https://img.shields.io/badge/precision-FP8%20W8A8-0ea5e9)](#fp8-checkpoint)
[![Hopper](https://img.shields.io/badge/target-H100%20%2F%20H200-16a34a)](#h100--h200-serving)
[![Business gate](https://img.shields.io/badge/business%20suite-20%20cases-7c3aed)](#release-gates)
[![Capability](https://img.shields.io/badge/capability-8%2F8-16a34a)](#release-gates)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b)](#license)

</div>

## What this release is

`SuperQwen3.8-abliterated-100-fp8` is a directly loadable Qwen3.8-27B derivative for
teams that need fewer blanket refusals in legitimate research, security, policy,
healthcare, retail, compliance, and creative workflows. It keeps the upstream
multimodal, reasoning, long-context, and tool-use paths while applying a wider
OBLITERATUS-derived refusal-subspace projection than the earlier SuperQwen3.8 release.

The public artifact is already quantized as **FP8_DYNAMIC W8A8** using
`compressed-tensors`: per-channel FP8 weights and dynamic per-token FP8 activations.
That is the format intended for H100/H200 Tensor Cores; no calibration dataset is
required at load time.

## Release highlights

| | Verified release value |
|---|---|
| **Parent** | `Qwen/Qwen3.8-27B` at `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0` |
| **Refusal directions** | 842 canonical paired prompts, per-layer rank 8 |
| **Projection** | Language layers 12–63, embeddings 0.65 blend, output head 1.0 blend, norm-preserving |
| **FP8 format** | FP8_DYNAMIC W8A8, per-channel weights + dynamic per-token activations |
| **Protected paths** | Vision 333 tensors, conv1d 48, MTP 15, and `lm_head` retained exactly outside FP8 packing |
| **Checkpoint** | 7 FP8 target shards + protected BF16 MTP sidecar, about 29.08 GiB |
| **Runtime kernel** | vLLM selected `CutlassFP8ScaledMMLinearKernel` for `CompressedTensorsW8A8Fp8` |
| **Capability** | 8/8 deterministic checks |
| **Tool use** | OpenAI function call parsed with exact name and arguments |
| **Benign-sensitive gate** | 0/8 explicit refusals |
| **OBLITERATUS audit** | 0/64 refusals, 0 blank outputs, 0 token leaks or loops |
| **Vision** | PASS |
| **Bounded reasoning** | default/low/medium PASS; xhigh completed correctly at 240 reasoning tokens |
| **Speculative decoding** | Native MTP K=5; 22.6322 tok/s at p256 and 21.4891 tok/s after an 8K prompt on GB10 |
| **Long context** | 65,579 actual prompt tokens retrieved on the final 262,144-token K=5 server |
| **Measured hardware** | 1× NVIDIA DGX Spark / GB10, C1, TP=1 — not an H100/H200 throughput claim |

## Stronger refusal reduction

This release was rebuilt from the pinned parent rather than patched from an already
modified checkpoint. OBLITERATUS revision
`a5a1ffa5849b442cf188b3c03fd4de71ddf5bdcc` supplied 842 canonical harmful/harmless
pairs. A per-layer rank-8 subspace was fit and projected through the residual output
paths of layers 12–63, plus bounded projections of the embeddings and output head.

The independent geometric reload gate passed all 106 modified tensors. Typical
post-projection component residuals were about 0.12–0.17%, below the fixed 2% ceiling.
The direction artifact SHA-256 is
`f2a0ba2b3c9e3faad158ac475732f48c84561c6f7a512cfd6a0e69558d64fbe1` and the
independently reloaded BF16 tensor-manifest identity is
`1679546a7769831a90f303d5389b168d2218a04006b6e09bc2c6e9bd7f57a2b2`.

“Abliterated” means the measured refusal direction was substantially reduced. It does
not mean every possible refusal has disappeared, and it does not turn generated text
into verified business, legal, medical, or security advice.

## FP8 checkpoint

| Component | Precision / treatment |
|---|---|
| Eligible language-backbone linear weights | FP8, per-channel |
| Input activations | FP8, dynamic per-token |
| Vision tower | BF16, exact |
| Conv1d / hybrid-state paths | BF16, exact |
| Native MTP draft head | BF16 sidecar, exact |
| `lm_head` | BF16, exact |
| Recommended KV cache | FP8 |

Structural verification found 496 language-backbone FP8 scale tensors, no quantization
sidecars on protected modules, and exact equality for every protected tensor. The full
repository is covered by `SHA256SUMS.json`.

## H100 / H200 serving

This checkpoint is sized for **TP=1 on one H100 80GB or H200 141GB**. Use TP=2 when
your workload values prefill concurrency or operational headroom more than single-GPU
latency. The commands below are deployment profiles, not fabricated Hopper benchmarks.

### One GPU, production baseline

```bash
vllm serve Jiunsong/SuperQwen3.8-abliterated-100-fp8 \
  --served-model-name SuperQwen3.8-abliterated-100-fp8 \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --gpu-memory-utilization 0.92 \
  --kv-cache-dtype fp8 \
  --enable-chunked-prefill \
  --enable-prefix-caching \
  --async-scheduling \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3
```

### Two GPUs

```bash
vllm serve Jiunsong/SuperQwen3.8-abliterated-100-fp8 \
  --served-model-name SuperQwen3.8-abliterated-100-fp8 \
  --tensor-parallel-size 2 \
  --max-model-len 262144 \
  --gpu-memory-utilization 0.92 \
  --kv-cache-dtype fp8 \
  --enable-chunked-prefill \
  --enable-prefix-caching \
  --async-scheduling \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3
```

For H100/H200, keep the native `compressed-tensors` FP8 path. Converting this release
back to BF16 before serving discards the point of the Hopper build. Benchmark your own
prompt lengths and concurrency before fixing production limits.

## Speculative decoding

The repository retains the exact native Qwen MTP head. **K=5** is the selected fast
profile. It passed the complete capability, tool, benign-sensitive, bounded-reasoning,
vision, 8K throughput, and 32,811-token retrieval gates. On the measured GB10 runtime:

| Profile | p256 C1 decode | 8K-prompt C1 decode | Result |
|---|---:|---:|---|
| K=0 | 7.8140 tok/s | 7.7224 tok/s | Stable baseline |
| K=3 + prefix cache | 18.9919 tok/s | — | Rejected: 8K run stalled |
| **K=5, prefix cache off** | **22.6322 tok/s** | **21.4891 tok/s** | **Selected** |

K=5 is about **2.90×** the measured short-prompt K=0 decode rate. Across the final
K=5 validation process the server accepted 1,587 of 3,135 drafted token positions;
acceptance varied by workload. The bundled launcher therefore defaults to K=5 and
does not combine speculation with prefix caching. Set `MTP_TOKENS=0` for the most
conservative path.

## Measured GB10 baseline

The reproducible non-speculative benchmark follows the post-first-token decode window
used by [`MiaAI-Lab/sparkDash`](https://github.com/MiaAI-Lab/sparkDash) at commit
`bf2709a80ef25d0e1a6ee41efec4c9b8042a5b8b`.

| Prompt class | Concurrency | Decode | TTFT |
|---:|---:|---:|---:|
| 256 target tokens (292 after chat formatting) | C1 | **7.8140 tok/s** | 0.261 s |
| 8,192 target tokens (8,222 after chat formatting) | C1 | **7.7224 tok/s** | 10.801 s |

These are **DGX Spark / GB10** measurements in eager mode. They are not estimates for
H100 or H200. Hopper owners should expect different results and should publish the
exact GPU, vLLM revision, prompt tokens, output tokens, concurrency, and decode window
when comparing deployments.

## Release gates

The release gate stores prompt and output hashes rather than redistributing raw test
content.

| Gate | Result |
|---|---:|
| FP8 structure + exact protected tensors | PASS |
| Independent reload of projected BF16 source | PASS |
| Deterministic capability | 8/8 |
| Tool call | PASS |
| Benign-sensitive refusal | 0/8 |
| Vision | PASS |
| Bounded reasoning | PASS through xhigh |
| 32K retrieval, K=0 and K=5 | PASS / PASS |
| 65K retrieval on final 262,144-token K=5 server | PASS; 65,579 prompt tokens in 133.59 s |
| Business directness suite | **20/20**, 0 hard refusal, 0 evasion, 0 disclaimer, 0 moralizing markers |
| OBLITERATUS paired refusal audit | **0/64 refusals, 0/64 blank, 0 leaks, 0 loops** |

## API example

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")
response = client.chat.completions.create(
    model="SuperQwen3.8-abliterated-100-fp8",
    messages=[{"role": "user", "content": "Draft a concise supplier risk memo."}],
    temperature=0.2,
)
print(response.choices[0].message.content)
```

For bounded reasoning, pass `chat_template_kwargs` through your vLLM client:

```python
extra_body={"chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}
```

## Limitations

- Abliteration reduces measured refusal behavior; it does not guarantee universal
  compliance, factuality, safety, or suitability for a particular business decision.
- FP8 can regress workloads outside the measured suites. Validate your domain data.
- Tool calls must be authorized, sandboxed, logged, and checked by the application.
- Long-context capacity is not the same as perfect long-context recall.
- Speed varies with GPU, driver, vLLM build, prompt length, output length, batching,
  multimodal inputs, and sampling settings.
- H100/H200 commands are optimized launch guidance; only GB10 numbers are presented as
  measurements in this card.

## Evidence identities

The final public artifact includes hash-only release reports, quantization verification,
the exact build recipe, and a file-by-file SHA-256 manifest. Large files are uploaded as
Git LFS objects and their remote LFS OIDs are verified against the local SHA-256 values
before the repository is made public.

## License

Apache-2.0, following the upstream Qwen3.8 release.
