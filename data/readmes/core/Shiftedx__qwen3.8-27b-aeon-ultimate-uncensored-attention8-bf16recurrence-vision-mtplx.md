---
license: apache-2.0
base_model:
- AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16
base_model_relation: quantized
library_name: mlx
pipeline_tag: image-text-to-text
language:
- en
- zh
- multilingual
tags:
- mlx
- mtplx
- qwen3.8
- mixed-precision
- affine-quantization
- speculative-decoding
- multi-token-prediction
- vision
- tool-calling
- reasoning
- uncensored
---

# AEON Qwen3.8 27B — Attention8 + BF16 Recurrence for MLX/MTPLX

A quality-first Apple Silicon conversion of
[AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16](https://huggingface.co/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16).
It packages the mixed-precision language model, BF16 vision tower, tokenizer,
tool template, and native BF16 multi-token-prediction head in one MTPLX-ready
repository.

This is an independent community conversion, not an official AEON-7, Qwen,
Apple, MLX, or MTPLX release.

## At a glance

| Property | Value |
|---|---|
| Model | 27B dense hybrid-attention/Gated DeltaNet |
| Format | MLX safetensors: affine 4-bit + affine 8-bit + BF16 |
| Download | 23.84 GB (22.20 GiB) |
| Modalities | Text and images |
| Agent features | Reasoning, native tools, structured output, optional Shiftedx Agent Harness |
| Speculative decoding | Native 15-tensor BF16 MTP head; qualified at depth 3 |
| Context | Configured for 262,144 tokens; qualified through 131,072 prompt tokens |
| Reference host | Apple M4 Max, 64 GiB unified memory |
| License | Apache-2.0, inherited from the source lineage |

Use this release when you have a 64 GB-or-larger Apple Silicon Mac and want the
quality-focused local build. If memory or storage is tighter, use the
[16.08 GB MXFP4 sibling](https://huggingface.co/Shiftedx/qwen3.8-27b-aeon-ultimate-uncensored-mxfp4-vision-mtplx).
The [29.53 GB MXFP8 sibling](https://huggingface.co/Shiftedx/qwen3.8-27b-aeon-ultimate-uncensored-mxfp8-vision-mtplx)
uses a larger, simpler precision strategy. The MXFP4+MTP sibling completed the
same Shiftedx Bench v0.3.0 gate and tied this release across all five published
lanes under its separately tuned D2 runtime contract. This Attention8 + BF16
recurrence artifact remains the quality-first precision recipe selected by the
earlier parent-comparison suite; use the MXFP4 sibling when deployment size and
memory matter more. Do not infer quality from file size alone.

## Why this hybrid is larger than a 4-bit model

The quantization recipe spends precision where local regression tests found the
architecture most sensitive:

- 168 language modules use affine 4-bit weights with group size 32.
- 234 attention, embedding, output, and late-MLP modules use affine 8-bit
  weights with group size 64.
- 96 recurrent `in_proj_a` and `in_proj_b` projections remain BF16.
- The vision tower and matching 15-tensor MTP head remain BF16.

This is a custom MLX affine mixed-precision model—not MXFP4, MXFP8, NVFP4,
GGUF, AWQ, or GPTQ. The exact module map is recorded in
[`BUILD_RECIPE.json`](BUILD_RECIPE.json).

## Qualification snapshot

The recipe-selection suite chose this hybrid over the compact local 4-bit
baseline: hard-task accuracy improved from 6/10 to **8/10**, repeated code
checks remained **6/6**, and code decode stayed close at 48.10 versus
50.56 tok/s. Full candidate comparisons are in [`BENCHMARKS.md`](BENCHMARKS.md).

### MTPLX 2.9 performance retest

A performance-only retest of the exact published weight-bearing revision
[`b5a54ea5d7745b6ddada238f83b66d63c979b9a5`](https://huggingface.co/Shiftedx/qwen3.8-27b-aeon-ultimate-uncensored-attention8-bf16recurrence-vision-mtplx/tree/b5a54ea5d7745b6ddada238f83b66d63c979b9a5)
used MTPLX 2.9.0 on the same Apple M4 Max 64 GiB host:

| Lane | Result |
|---|---:|
| Isolated D3 decode, three-run mean | **63.36 tok/s** |
| Isolated D3 decode, observed range | **59.67–65.77 tok/s** |
| Isolated D3 end-to-end, three-run mean | **56.66 tok/s** |
| OpenAI API code decode | **54.83 tok/s** |
| OpenAI API code end-to-end | **45.83 tok/s** |
| API code validation | **3/3** |

The API code decode result is 14.0% above the original MTPLX 2.7.1
recipe-selection result of 48.10 tok/s. D3 remained the winner with 90.76%
aggregate draft acceptance in the isolated lane. Testing used automatic fans;
no privileged fan pinning or 80–90 tok/s claim is included. The isolated lane
used the recommended temperature 1.0/top-p 0.95/top-k 20 target and draft
samplers. The API code lane was a deterministic temperature-0, thinking-off
diagnostic with unquantized KV cache.

This retest updates performance evidence only. The complete quality, context,
tools, agentic, and vision qualification below remains the MTPLX 2.7.1 run.
See [`BENCHMARKS.md`](BENCHMARKS.md) and the
[`MTPLX_2.9_PERFORMANCE.json`](MTPLX_2.9_PERFORMANCE.json) sanitized aggregate.

#### MTPLX 2.9.2 MTP runtime retest

A second performance-only retest kept the exact model weights and native BF16
MTP sidecar unchanged, then quantized only the loaded MTP runtime block and
draft-only vocabulary projection:

| Configuration | Eight-sample median decode | Peak memory |
|---|---:|---:|
| BF16 MTP block + Q4/G64 draft head | 38.70 tok/s | 26.16 GB |
| **Q6/G64 MTP block + Q4/G32 draft head** | **40.72 tok/s** | **25.73 GB** |

The selected D3 runtime improved median decode by 5.2% and reduced observed
peak memory by approximately 0.43 GB. On a separate API hard-suite lane it
improved mean decode by 3.7% and wall time by 2.8% with byte-identical
responses under that lane's request contract. These are deployment-runtime
results, not a weight-level quality improvement. The complete quality,
context, tools, agentic, and vision score below remains bound to its original
MTPLX 2.7.1 contract.

<!-- shiftedx-bench:start -->
### Post-publication Shiftedx Bench gate

| Lane | Result |
|---|---:|
| Quality | **8/10** |
| Long context | **15/15**, through 131,072 prompt tokens |
| Tool calling | **6/6** |
| Lightweight agentic | **2/2** |
| Vision | **4/4** |

- Evaluated model revision: [`c839d980679e9aec1ab66388ded0689040c9d93a`](https://huggingface.co/Shiftedx/qwen3.8-27b-aeon-ultimate-uncensored-attention8-bf16recurrence-vision-mtplx/tree/c839d980679e9aec1ab66388ded0689040c9d93a)
- Benchmark revision: [Shiftedx Bench v0.3.0 `3bbb0bfa`](https://huggingface.co/datasets/Shiftedx/shiftedx-bench/tree/3bbb0bfa01e33503163cb34ef52b4d507e456265)
- Runtime: MTPLX 2.7.1 turbo, MTP depth 3, thinking on/medium, temperature
  1.0, top-p 0.95, top-k 20, unquantized KV cache
- Host: Apple M4 Max with 64 GiB unified memory

Scores are reported separately; Shiftedx Bench does not produce a composite
“intelligence” score. The sanitized gate artifact is
[`SHIFTEDX_BENCH_V0.3_TOOLS_AGENTIC_VISION.json`](SHIFTEDX_BENCH_V0.3_TOOLS_AGENTIC_VISION.json).
<!-- shiftedx-bench:end -->

### Expanded agentic comparison

The two-case gate above is a regression check, not a broad agent-readiness
claim. Shiftedx Bench v0.5.1 ran three complete paired trials with and without
the optional `shiftedx-harness-v1` execution policy:

| Evaluation | Baseline | Shiftedx Agent Harness | Difference |
|---|---:|---:|---:|
| 30-case expanded matrix | **54/90 (60.0%)** | **86/90 (95.6%)** | **+35.6 points** |
| Disposable-repository repairs | **9/12 (75.0%)** | **11/12 (91.7%)** | **+16.7 points** |

The harness converts observable tool receipts into bounded execution state. It
does not change the weights or see hidden answers/tests. On the expanded matrix
it reduced dispatched tool calls from 282 to 267 but increased total wall time
by 11.4%. Repository trials were more variable; baseline won one of the three.
Treat this as a higher-reliability deployment policy at a different operating
point—not a weight-level intelligence improvement or a free speedup.

- Evaluated model revision: [`b5a54ea5d7745b6ddada238f83b66d63c979b9a5`](https://huggingface.co/Shiftedx/qwen3.8-27b-aeon-ultimate-uncensored-attention8-bf16recurrence-vision-mtplx/tree/b5a54ea5d7745b6ddada238f83b66d63c979b9a5)
- Benchmark revision: [Shiftedx Bench v0.5.1 `335e6694`](https://huggingface.co/datasets/Shiftedx/shiftedx-bench/tree/335e6694e4aec13e9370af8a993d8c8f14d7ffb5)
- [Readable report, family scores, telemetry, sanitized per-case rows, and manifests](https://huggingface.co/datasets/Shiftedx/shiftedx-bench/blob/9a43027a84dc4a4a283220f58314b5768245ec58/results/aeon-hybrid-shiftedx-harness-v1/README.md)

## Quick start

Install [MTPLX 2.9.2](https://pypi.org/project/mtplx/2.9.2/) or newer, then:

```bash
MODEL=Shiftedx/qwen3.8-27b-aeon-ultimate-uncensored-attention8-bf16recurrence-vision-mtplx

mtplx pull "$MODEL"
mtplx inspect "$MODEL" --require-mtp
mtplx start cli \
  --model "$MODEL" \
  --profile turbo \
  --depth 3 \
  --reasoning on \
  --reasoning-effort medium \
  --tool-prompt-mode native \
  --chat-template-profile tokenizer
```

For an OpenAI-compatible endpoint:

```bash
mtplx serve \
  --model "$MODEL" \
  --download \
  --host 127.0.0.1 \
  --port 8000 \
  --profile turbo \
  --generation-mode mtp \
  --load-mtp \
  --depth 3 \
  --context-window 198000 \
  --mtp-quant-bits 6 \
  --mtp-quant-group-size 64 \
  --mtp-quant-mode affine \
  --reasoning on \
  --reasoning-effort medium \
  --tool-prompt-mode native \
  --chat-template-profile tokenizer \
  --paged-kv-quantization off
```

The high-level `mtplx serve` wrapper reads the Q4/G32 draft-only projection
from this artifact's `recommended_draft_lm_head` runtime metadata. Do not pass
the lower-level `--draft-lm-head-*` server flags to the wrapper.

MTPLX accepts OpenAI tools and standard `image_url` content parts. For the
published 6/6 tool result, ordinary/multi-round requests used the hybrid tool
contract while explicit parallel intent used Qwen's native template. That
router policy is included as
[`MTPLX_2.7.1_QWEN38_EXPLICIT_PARALLEL_NATIVE.patch`](MTPLX_2.7.1_QWEN38_EXPLICIT_PARALLEL_NATIVE.patch).

Recommended starting point: turbo profile, MTP depth 3, thinking on at medium
effort, temperature 1.0, top-p 0.95, top-k 20, and unquantized KV cache. Run
`mtplx tune --model "$MODEL" --retune` on your own Mac because acceptance and
speed vary with chip, context, thermals, and workload.

The qualified default keeps thinking on at medium effort. For a low-latency
request that must suppress reasoning, send the canonical top-level OpenAI field
`"enable_thinking": false`. MTPLX 2.9.2 was verified to return zero reasoning
tokens for that field while preserving ordinary stop completions, strict tool
calls, and the long-context needle. Re-check per-request behavior after runtime
upgrades. The separate thinking-off diagnostic scored 5/10 on its local
ten-task hard suite; it does not replace the published 8/10 medium-thinking
quality score.

## Context and memory

The model advertises a 262,144-token context window and passed the exact-token
qualification grid through 131,072 prompt tokens with unquantized KV cache. A
260,096-token attempt exceeded the practical memory envelope of the 64 GiB
reference host and ended in a host watchdog. That is reported as **not
qualified on this host/runtime**, not as a wrong model answer.

Reaching the full window may require a larger-memory Mac or a separately
qualified q8/q4 KV-cache configuration. Changing KV precision creates a
different runtime candidate and requires new quality, context, performance, and
stability measurements. A 32 GiB Mac was not tested and may be too constrained;
prefer the MXFP4 sibling when memory is tight.

## Provenance and integrity

- Source: [AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16](https://huggingface.co/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16)
- Pinned source revision: `a6775a9a8ebb65cab3f707b4ab087fc7aa698634`
- [`BUILD_RECIPE.json`](BUILD_RECIPE.json): precision policy
- [`mtplx_runtime.json`](mtplx_runtime.json): native-MTP contract and defaults
- [`RELEASE_MANIFEST.json`](RELEASE_MANIFEST.json) and [`SHA256SUMS`](SHA256SUMS): file integrity
- [AEON Qwen3.8 MLX collection](https://huggingface.co/collections/Shiftedx/qwen38-27b-aeon-ultimate-uncensored-mlx-quants-6a81f529af306393b1b01849)

The vision tower and MTP sidecar are preserved from the qualified source
lineage. Model behavior still depends on the exact runtime, template, sampler,
reasoning mode, MTP depth, KV precision, and hardware.

## Limitations and safety

- Quantization can change outputs relative to BF16; qualification does not
  guarantee source parity on every prompt.
- Tool calls, JSON, code, image interpretations, and factual answers can be
  wrong. Validate output before allowing system changes or code execution.
- Only the Apple M4 Max 64 GiB configuration received the complete published
  qualification.
- This intentionally uncensored source lineage may produce harmful, illegal,
  offensive, or unsafe material. Quantization does not restore alignment.

Operators are responsible for prompts, outputs, authentication, rate limits,
moderation, audit logging, and human review appropriate to their deployment.
Do not treat output as professional legal, medical, financial, or security
advice.

## License and credits

Apache-2.0, inherited from the source lineage. Follow the source model's
license and attribution requirements when redistributing or deploying this
derivative.

Credits to [Qwen](https://huggingface.co/Qwen),
[AEON-7](https://huggingface.co/AEON-7),
[MLX](https://github.com/ml-explore/mlx),
[MLX-LM](https://github.com/ml-explore/mlx-lm), and
[MTPLX](https://github.com/youssofal/MTPLX).
