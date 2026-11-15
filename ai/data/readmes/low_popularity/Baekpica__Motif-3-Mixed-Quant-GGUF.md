---
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
license: mit
language:
  - en
  - ko
pipeline_tag: text-generation
library_name: gguf
tags:
  - gguf
  - motif
  - motif-3
  - mixture-of-experts
  - mixed-quantization
  - iq2_xxs
  - dgx-spark
  - long-context
---

# Motif 3 — Mixed-Quant GGUF

**A structurally intact 314.8B-parameter Motif-3 MoE compressed to 94.16 GB
(87.70 GiB).
Native H200 residency, latent-KV execution, OpenAI serving, tools, continuous
batching, and retrieval through 128K are validated. The ds4-dfm path also
passes a strict 262,080-token prompt plus decode gate on one DGX Spark.**

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>


Full-topology mixed-quant conversion of
[`Motif-Technologies/Motif-3`](https://huggingface.co/Motif-Technologies/Motif-3),
designed as the resident-weight baseline for one 128 GB-class DGX Spark.
This is an independent conversion, not an official Motif Technologies release.

Nothing is pruned, merged, expert-dropped, or layer-dropped. The artifact
retains all 53 target-model layers, the first two dense layers, all 51 sparse
layers, all 384 routed experts per sparse layer with top-8 routing, the shared
expert, Grouped Differential Latent Attention (GDLA), Expert-Specific
PolyNorm, modified mHC, and the complete one-layer MTP predictor.

| | |
|---|---:|
| Architecture | Motif-3, 53 layers, 14 full + 39 SWA GDLA |
| Routed experts retained | **384 / 384 per sparse layer** |
| Tensors | **2,287** |
| Artifact | **94.16 GB (87.6957 GiB)**, 11 shards |
| Native H200 model/runtime | **91.262 GiB**, conservative measured repeat |
| Native 256K session | **4.037 GiB**, measured |
| Source context limit | 262,144 tokens |
| H200 semantic execution | short/32K/64K/128K passed; 256K partial prefill only |
| Single-GB10 execution | **262,080-token prompt + 43-token decode; three-way 196K-context serving passed** |

## ds4-dfm

This model is served by **ds4-dfm**, a common ds4 release line for
**DFM (독자 파운데이션 모델, 독파모)** model families. It was developed to
serve full-scale models on a single NVIDIA DGX Spark with 128 GB of unified
memory through explicit model-family C/CUDA paths and device kernels.

The release line is the
[`dfm` branch](https://github.com/Baekpica/ds4/tree/dfm) of
[`Baekpica/ds4`](https://github.com/Baekpica/ds4). The integration tag is
[`v0.6.2-dfm`](https://github.com/Baekpica/ds4/tree/v0.6.2-dfm)
(Entrpi `v0.6.2` absorbed). The 32K/256K HTTP gates below remain the earlier
Spark evidence at
[`593d251`](https://github.com/Baekpica/ds4/commit/593d2511a10694f5a33fbafbd997ca24e819a853);
the original 8K `ds4-bench` point uses
[`cc2f277`](https://github.com/Baekpica/ds4/commit/cc2f27712482318aef4d83c30f59974739166990);
the persistent multi-bank measurements use
[`cf605e0`](https://github.com/Baekpica/ds4/commit/cf605e08a7f669333504962011c423b8d78196df).
The 8K/32K remesure uses
[`a09ff4f`](https://github.com/Baekpica/ds4/commit/a09ff4f) on `dfm`.
The 256K remesure uses
[`6500480`](https://github.com/Baekpica/ds4/commit/6500480)
(kernels through `a09ff4f`). The integration tag is not moved. One
`ds4-server` command and one HTTP contract cover the integrated DeepSeek,
Solar Open2, K-EXAONE, Motif-3, and dots3-note families; only the GGUF path
and its matching weight-owner manifest change. The server provides OpenAI
Chat Completions, OpenAI Completions, OpenAI Responses, and Anthropic
Messages.

The production GGUF in this repository was loaded through the common release
binary on DGX Spark. Context and throughput claims are limited to the exact
conditions below; model quality has not been evaluated by these serving tests.

## Artifact

| Variant | Split | Exact size | Purpose |
|---|---:|---:|---|
| **MQ87-88-FIT** | 11 files | 94,162,542,816 bytes (94.16 GB / 87.6957 GiB) | one-Spark capacity/release baseline |

The canonical merged/unsharded byte stream used by native ds4 is
94,162,541,472 bytes (94.16 GB / 87.6957 GiB) with SHA-256
`15755a735753bc1396e5ffa539e65a779a4fd769e8833360a4d743c4c60c2f25`.

Start with `Motif-3-MQ87-88-FIT-00001-of-00011.gguf`; compatible split-aware
runtimes discover the remaining shards automatically. Exact per-shard hashes
are published in `MQ87-88-FIT-SHA256SUMS`.

The weight files are fixed at Hub revision
`efd6044e25e7f8e3b459a737d021091e2e69b6c6`. Later model-card/report commits
do not change shard bytes or hashes.

```bash
hf download Baekpica/Motif-3-Mixed-Quant-GGUF \
  --revision efd6044e25e7f8e3b459a737d021091e2e69b6c6 \
  --include 'Motif-3-MQ87-88-FIT-*.gguf' \
  --include MQ87-88-FIT-SHA256SUMS \
  --local-dir ./Motif-3-MQ87-88-FIT
```

The name is a nominal recipe label, not the artifact's decimal size. The
actual payload is 94.16 GB (87.70 GiB), and the exact byte counts above are
authoritative. Admission depends on whether its measured aligned/repacked
resident form fits the target Spark together with latent KV, workspace, and
server state.

## Precision recipe

Precision is assigned by module role. Always-active and control paths stay
conservative; the 51×384 routed-expert stack carries the compression burden.

| Tensor group | Type | Rationale |
|---|---|---|
| Token embedding and LM head | `Q8_0` | token/logit fidelity |
| GDLA projections and differential/output-gate paths | `Q8_0` | attention and long-context stability |
| Dense MLP, shared expert, MTP projections | `Q8_0` | always active |
| Routed expert gate/up, layers 2–52 | `IQ2_XXS` + Q8 imatrix | dominant parameter mass |
| Routed expert down, layers 2–52 | `Q2_K` + Q8 imatrix | capacity baseline |
| Router weights | `F32` | top-8 decision stability |
| RMSNorm, Expert PolyNorm coefficients/biases | `F32` | normalization/activation stability |
| mHC controls/scalars | `F32` | sigmoid, clamp, Sinkhorn stability |
| mHC small projections | `BF16` | small protected matrices |

The completed GGUF contains 2,287 tensors: **1,273 F32, 318 BF16, 543
Q8_0, 102 IQ2_XXS, and 51 Q2_K**. The 102 IQ2 tensors are separately stored
gate and up matrices. They originate from 51 fused checkpoint gate/up tensors;
the split is lossless before quantization and retains every expert value.

No Q4 edge-layer promotion is included in this release. MQ95/MQ97 are outside
the scope of this capacity-first artifact.

## Q8_0 activation calibration

Calibration was collected only after producing and freezing the separate
full-topology Q8_0 reference in
[`Baekpica/Motif-3-GGUF`](https://huggingface.co/Baekpica/Motif-3-GGUF).

The corpus reuses the checksum-pinned normalization and target shares audited
for the preceding Solar Open 2 mixed-quant release, but every record is
rendered and counted again with Motif-3's official final tokenizer and chat
template. It contains 1,539 documents, 4,079,555 official-tokenizer tokens,
and 17,011,959 bytes.

| Calibration bucket | Target token share |
|---|---:|
| Instruction-following chat | 22% |
| Cascade stage 1 reasoning | 16% |
| Cascade stage 2 reasoning/tools | 16% |
| Korean | 16% |
| Other multilingual | 12% |
| Finance | 6% |
| SWE agentic | 6% |
| Algorithmic code | 6% |

The H200 calibration runtime directly dequantized the Q8_0 GGUF and executed
the official Motif-3 equations with a layer-major schedule: mHC, expanded
historical K/V GDLA, interleaved 128-token SWA/full attention, YaRN, the
differential signal/noise heads, elementwise attention output gate, sigmoid
top-8 routing with correction-bias selection and route renormalization, shared
experts, and per-expert PolyNorm.

| | |
|---|---:|
| Calibration chunks | 590 × 512 tokens |
| Total official-tokenizer tokens | 302,080 |
| Routed observations | 123,248,640 |
| Sparse layer/expert cells | 51 × 384 |
| Zero-coverage cells | **0** |
| Routes per layer/expert | min 313, median 5,934, p95 9,986.7, max 85,011 |
| Imatrix size | 742,004,501 bytes |
| Imatrix SHA-256 | `54fcc4d6d1fe96a3fc12bd24869eff128c724737ac07ce866ce08018a5e3cfbc` |

Gate/up importance observes the exact FFN-normalized input. Down importance
observes the Expert-Specific PolyNorm output after route weighting, matching
the ds4 routed-MoE execution order. No uniform, random, proxy-model, or
source-BF16 activation matrix was substituted.

The machine-readable activation report is published here as
`Q8_0-IMATRIX-REPORT.json`. Corpus construction is included in the public
reproduction materials; the exact rendered corpus, final imatrix, and
rank-local accumulators are preserved in the private Spark handoff.

## Provenance

| | |
|---|---|
| Source model | `Motif-Technologies/Motif-3` |
| Exact source revision | `ccceb1a5fd7b5eb32e47841216b3caf5666c07bc` |
| Source parameters | 314,841,775,750 |
| Source tensors | 2,236 |
| GGUF tensors | 2,287 |
| Native context metadata | 262,144 tokens |
| Full Q8_0 reference | `Baekpica/Motif-3-GGUF@5c266c95bf8c8d822d50e5e1cce9d108eaadb2af` |
| Fixed mixed-weight revision | `efd6044e25e7f8e3b459a737d021091e2e69b6c6` |
| Official implementation oracle | `MotifTechnologies/vllm@4cd9eb4129883565e69d508038d783d59ee01867` |
| Conversion base | `ggml-org/llama.cpp@1d2869c6e54d5003f3927a79efbca0fefa034a6d` |
| ds4 base | `Baekpica/ds4@b0309611041655f4e45671cfd9c9886aff161406` |
| Native ds4 implementation | `Baekpica/ds4:feature/motif-3-model-loader@d878ea1a1d67bc0f0bd60e20e75b4a011aa2d8d9` |
| DGX Spark long-context implementation | [`Baekpica/ds4@593d251`](https://github.com/Baekpica/ds4/commit/593d2511a10694f5a33fbafbd997ca24e819a853) |
| DGX Spark 8K throughput implementation | [`Baekpica/ds4@cc2f277`](https://github.com/Baekpica/ds4/commit/cc2f27712482318aef4d83c30f59974739166990) |
| DGX Spark multi-bank implementation | [`Baekpica/ds4@cf605e0`](https://github.com/Baekpica/ds4/commit/cf605e08a7f669333504962011c423b8d78196df) |
| DGX Spark 8K/32K remesure (`dfm`) | [`Baekpica/ds4@a09ff4f`](https://github.com/Baekpica/ds4/commit/a09ff4f) |
| ds4-dfm integration tag | [`v0.6.2-dfm`](https://github.com/Baekpica/ds4/tree/v0.6.2-dfm) |
| Public reproduction | [`Baekpica/motif-3-mixed-ds4`](https://github.com/Baekpica/motif-3-mixed-ds4) |
| Private Spark handoff | Expensive calibration state plus offline reproduction/runtime snapshots are preserved in `hf://buckets/Baekpica/motif-3-spark-handoff` |

Only the official final Motif-3 checkpoint was used. Motif-3-Beta was not used
as a source, calibration input, implementation oracle, or fallback.

## Model structure and context memory

Layers whose index is divisible by four use full attention (14 layers); the
other 39 layers use a bounded 128-token sliding window. The production target
does not retain expanded historical K/V. Its persistent context state is
latent KV plus the decoupled RoPE key for full-attention layers, bounded SWA
ring state, and cache identity/position state.

On H200, creating a native 262,144-token session while the model remained
resident allocated 4,236,751,872 bytes (3.946 GiB) of cache tensor payload and
produced a 4,334,813,184-byte (4.037 GiB) CUDA free-memory delta including
allocator overhead. This is a physical H200 measurement, not a Spark claim.
Physical unified-memory residency and OS headroom on the target GB10 remain
authoritative.

The higher of two native-`sm_90` H200 model/runtime initialization repeats plus
the 256K-session delta was 102,326,337,536 bytes (95.298828125 GiB). This supports the capacity design;
it does not predict GB10 driver, allocator, or OS overhead.
The conservative H200 component measurements place model/runtime at 91.262
GiB and the native 256K session at 4.037 GiB, inside the design preferences of
98 GiB and 5 GiB respectively; only the target GB10 can establish unified-
memory admission and final `MemAvailable`.

## Runtime compatibility

Motif 3 is not a Llama-family graph. A compatible runtime must implement its
384E sigmoid router, route normalization/scale, shared expert,
Expert-Specific PolyNorm, modified mHC, GDLA/differential heads and output
gate, interleaved SWA/full attention, YaRN, latent KV semantics, and MTP.

The target runtime is
[`Baekpica/ds4`](https://github.com/Baekpica/ds4) at the exact ds4-dfm Spark
commit pinned above. The earlier `feature/motif-3-model-loader` revision is
retained as H200 bring-up provenance. The private Spark handoff also carries
an offline source snapshot and commit metadata.
Stock GGUF runtimes should not be assumed to execute this architecture merely
because they can parse the container.

The current native branch has an explicit Motif tensor binder and CUDA graph,
production latent-KV/SWA-ring sessions, strict device-resident model loading,
the official tokenizer/chat/reasoning/tool protocol, and an OpenAI-compatible
`ds4-server` path. Motif sessions refuse streaming/offloaded weights and never
fall through to the generic DeepSeek graph.

A clean build at the pinned Spark revision completed the CPU and `cuda-spark`
targets, linked the five runtime programs, and produced only `sm_121a` CUDA
code objects. The same revision passed the Motif loader, tokenizer, CUDA
primitive, real-weight parity, resident-memory, and strict OpenAI gates below.

The public files use standard GGUF splitting. The current ds4 development
loader consumes one merged GGUF, so merge from the first shard with
`llama-gguf-split --merge` before launch. This is a one-time artifact assembly,
not SSD weight streaming; production admission still requires the merged or
repacked weights to be resident and forbids simultaneous physical residency of
duplicate raw/repacked mappings.

## Validation status

The unsharded artifact and the complete 11-file split set independently passed
strict source-map validation. The verifier checked the pinned revision,
architecture metadata, native 262,144-token context, all 53 target layers,
all routed gate/up/down tensors for sparse layers 2–52, all 384 experts, the
shared experts, and the complete MTP block. It found exactly 2,287 unique
tensors with no missing, duplicate, unexpected, mistyped, misshaped, or
out-of-bounds payloads. The split set totals 94,162,542,816 bytes (94.16 GB /
87.6957 GiB); every shard also has a published SHA-256 digest.

A separate 57-row numerical comparison sampled the embedding and LM head,
GDLA/control paths, dense/shared paths, routed experts at layers 2, 26, and 52,
both halves of the checkpoint's fused gate/up weights, and MTP. Protected
F32/BF16 rows were source-exact. Minimum sampled cosine was `0.9999740` for
Q8_0, `0.9417932` for IQ2_XXS, and `0.9580462` for Q2_K. The native ds4
Motif-3 binder also accepted the completed mixed artifact as the official-final
53-layer, 14-full/39-SWA, 384E top-8 topology with MTP present.

Two final explicitly rebuilt `sm_90` runtime repeats copied the full 94.16 GB
(87.70 GiB) image into one H200 in 9.560–12.070 seconds without SSD streaming
or CPU weight offload. The measured CUDA free-memory delta for model and runtime
initialization was 97,438,334,976–97,991,524,352 bytes; capacity accounting
uses the higher result. Strict residency fails startup instead of silently using
host-mapped weights.

Once optional CUDA preparation finishes, ds4 discards the raw GGUF tensor
pages while retaining only metadata/tokenizer mapping. Measured GGUF mapping
RSS fell from 91,955,608 kB to 9,416 kB and remained low through inference, so
the raw file is not kept as a second steady physical weight image beside the
CUDA-owned model copy.

The final all-`sm_90` full-question 256K H200 attempt also measured 9,416 kB
of GGUF mapping RSS during partial prefill with `VmSwap: 0`, after allocating
the complete 262,144-token production latent cache.

The automated resident gate caps this mapping at 262,144 kB both after copy
and after native graph/cache execution. Its final native-`sm_90` H200 run
measured 9,416 kB and 29,512–29,640 kB respectively.

The native expanded-path oracle and production latent path selected the same
first token and all top-8 logits on the short fixture; full-logit cosine was
`0.99490164`. Direct/chunked cache replay produced cosine `1.0`. The real
mixed sparse-layer diagnostic measured Q2 down cosine `0.9996071` and final
sparse-output cosine `0.9998363`. A real-weight MTP diagnostic evaluated 19
teacher-forced rows with finite logits.

### DGX Spark ds4-dfm evidence

These measurements use one DGX Spark GB10 with 128 GB unified memory, NVIDIA
driver 610.43.02, CUDA 13.3, Linux 6.17, and the production 11-shard artifact
merged to its canonical 94,162,541,472-byte stream. Generation was greedy,
single-request, non-streaming, and used no speculative decoding or thinking.
The default prefill chunk was 4,096 tokens.

| Gate | Interface | Prefill | Decode | Correctness |
|---:|---|---:|---:|---|
| 8K | `ds4-bench` | **8,192 tokens at 519.55 tok/s** | **64 tokens at 12.28 tok/s** | prefill throughput point; prefill-only 519.55, decode-run 516.17 / 12.28 |
| 32K | OpenAI chat | **32,768 tokens in 82.649 s (396.47 tok/s)** | **43 tokens in 4.799 s (8.96 tok/s)** | exact beginning/middle/end JSON |
| 256K | OpenAI chat | **262,080 tokens in 1,492.375 s (175.61 tok/s)** | **43 tokens in 17.072 s (2.52 tok/s)** | exact beginning/middle/end JSON; `finish_reason=stop` |

The 256K request completed in 1,509.460 seconds with 262,123 total tokens.
Because the request was non-streaming, it does not provide an independently
measured network-visible TTFM.

The resident gate measured a 4,422,546,432-byte (4.119 GiB) latent-cache
payload and a 10,418,716,672-byte (9.703 GiB) default-graph-plus-cache physical
delta. Source GGUF RSS settled at 29,632 KiB; owner and worker both remained at
`VmSwap: 0`. The weight owner held 7.00 GiB of raw tensors plus 86.07 GiB in
590 derived artifacts, with no duplicate model image or CPU weight offload.
About 12 GiB remained available during the final gate.

Nsight Compute confirmed that the expanded attention kernel fell from 55.79
ms to 28.83 ms (48.3%), and the Motif group-5 QK-absorb kernel fell from 38.91
ms to 10.97 ms (71.8%). Loaded SM-clock samples were 2,398–2,411 MHz; the prior
611 MHz pinned-clock condition did not recur.

The table above contains single-request results. Concurrent 256K serving,
other GB10 software configurations, other accelerators, and model quality are
not claimed. The Motif ds4-dfm path uses plain decoding with `--no-spec`;
MTP and DSpark support models remain DeepSeek-only.

### DGX Spark v0.6.2-dfm remesure

Same GB10 host (driver 610.43.02, CUDA 13.3, `sm_121a`), same MQ87-88
artifact, aligned-Q8 VMM owner (`--reserve-gb 24`), greedy, thinking
disabled. Engine:
[`Baekpica/ds4` `dfm` @ `6500480`](https://github.com/Baekpica/ds4/commit/6500480)
(kernels through [`a09ff4f`](https://github.com/Baekpica/ds4/commit/a09ff4f)).
The integration tag remains [`v0.6.2-dfm`](https://github.com/Baekpica/ds4/tree/v0.6.2-dfm);
that tag is not moved. The historical table above stays the
`v0.5.6.3-dfm` evidence.

| Gate | Interface | Prefill | Decode | Correctness |
|---|---|---:|---:|---|
| 8K | `ds4-bench` | **8,192 tokens at 627.19 tok/s** | **64 tokens at 15.06 tok/s** | throughput fixture |
| 32K | `ds4-bench` | **32,743 tokens at 545.62 tok/s** | **64 tokens at 12.95 tok/s** | same-session prior binary 519.57 / 13.00 |
| 32K | OpenAI chat | **32,751 tokens at 546.7 tok/s** | **52 tokens at 12.8 tok/s** | beginning/middle/end sentinels exact |
| 256K | OpenAI chat, `-c 262144` | **262,080 tokens in 1,098.433 s (238.59 tok/s)** | **43 tokens in 7.205 s (5.97 tok/s)** | exact beginning/middle/end JSON; `finish_reason=stop`; 262,123 total; `cached_tokens=0` |

Versus the merge-day `v0.6.2-dfm` baseline on this host (519.90 / 12.62 at
8K, 445.03 / 9.68 at 32K): 8K prefill **+21%**, 8K decode **+19%**, 32K
prefill **+23%**, 32K decode **+34%**. Versus the `v0.5.6.3-dfm` published
256K row (175.61 / 2.52): prefill **+35.9%**, decode **+137%**. Concurrent
256K banks are not claimed. The 256K worker held 10,429 MiB with 4.119 GiB
of latent KV; owner and worker `VmSwap` stayed 0; available memory stayed
11–12 GiB; SM clocks sampled 2,411–2,496 MHz.

### Partial prefix reuse

Runtime
[`Baekpica/ds4@cf817c7`](https://github.com/Baekpica/ds4/commit/cf817c7)
extends the shared partial-prefix checkpoint pool (introduced for Solar in
[`042bcea`](https://github.com/Baekpica/ds4/commit/042bcea5302bff775d0a508cec643f1f06754df9))
to the Motif-3 continuous lane. Motif-3 has no recurrent state, so a
checkpoint stores only each sliding-window layer's 128-row window (39
layers, 5.48 MiB per slot, 32 demand-mapped slots); full-attention latent
rows below the checkpoint copy directly from the retained source bank.
Request boundaries are checkpoints, long prefills and decode retain roughly
24 stride-aligned ones across the configured context, and a divergent
prompt restores the nearest checkpoint at or below the shared prefix and
replays only the gap.

One controlled A/B run used the same GB10, this artifact, the VMM owner
(`--reserve-gb 16`), a four-bank worker, `-c 65536`, 4,096-token prefill
chunks, and greedy no-think streaming Chat requests. The control set
`DS4_SERVER_FORK_PARTIAL=0`, which also skips checkpoint reservation; the
treatment used the default.

| Request | Prompt | Control cached | Treatment cached | Control TTFT | Treatment TTFT | Speedup |
|---|---:|---:|---:|---:|---:|---:|
| Source | 16,837 | 0 | 0 | 28,646.2 ms | 28,711.9 ms | 0.998× |
| Branch at ~7K | 7,140 | 0 | 4,096 | 11,319.4 ms | 5,196.3 ms | 2.18× |
| Branch at ~14K | 14,095 | 0 | 12,288 | 23,563.1 ms | 3,627.9 ms | 6.50× |

All three responses were byte-identical between control and treatment.
Treatment reported two partial-fork admits, 16,384 cached tokens, zero
failed requests, and zero admission rejects. Source checkpoint capture
added 65.7 ms (0.23%) in this single run. The engine fixture
(`test_motif3_batch --partial-only`) additionally pinned request-boundary
and periodic checkpoints and a two-segment ring-wrapping window restore,
each matching its cold oracle's greedy token.

This is a bounded worker-local cache, not an unbounded radix tree. Token
history and full-attention rows remain anchored to a retained bank, the
pool is not serialized into disk-KV payloads, and the EXAONE bank lane
keeps exact-frontier reuse only. Details:
[`docs/motif3-partial-reuse-2026-08-22.md`](https://github.com/Baekpica/ds4/blob/dfm/docs/motif3-partial-reuse-2026-08-22.md).

### DGX Spark 196K persistent multi-bank evidence

The current runtime was launched with a 196,608-token context, three resident
banks, an 8,192-token prefill chunk, and no speculative decoding. It completed
all four common endpoints--OpenAI Chat Completions, OpenAI Completions, OpenAI
Responses, and Anthropic Messages--with their native HTTP 200 response shapes.

| Gate | Verified result |
|---|---|
| 8K cold prefill | 8,214 prompt tokens at **266.3 tok/s**; exact `LONG_OK` response |
| Single decode | 192 output tokens; **490.4 ms TTFT**, **12.9 tok/s**, 15.350 s HTTP wall time |
| Three simultaneous Chat requests | 192 output tokens each in 24.885--25.030 s; **23.01 aggregate output tok/s**; `served=3 fallback=0` |

Settled `/v1/stats` showed zero failed or serial requests, zero continuous-batch
failures, three total and zero live banks, and zero speculative drafts. The VMM
weight owner used 90,119 MiB, the worker used 22,283 MiB after the 8K checks,
and about 6.5 GiB of system memory remained available without an OOM event.
Loaded SM clock remained 2,411 MHz instead of the earlier faulty 611 MHz pin.

### H200 end-to-end evidence

| Gate | Interface | Prefill | Decode | Correctness |
|---:|---|---:|---:|---|
| 2K | OpenAI chat | 346.72 tok/s | 12.64 tok/s | exact beginning/middle/end JSON |
| 32K | native, all-`sm_90` | 125.34 tok/s | 1.942 tok/s | exact beginning/middle/end JSON; 43-token decode |
| 32K | OpenAI chat, all-`sm_90` | 125.22 tok/s | 1.941 tok/s | exact JSON; model ID and 32,768 prompt tokens exact |
| 64K | native, all-`sm_90` | 68.72 tok/s | 1.021 tok/s | exact beginning/middle/end JSON; 52-token decode |
| 128K | native, all-`sm_90` | 36.36 tok/s | 0.524 tok/s | exact JSON; 131,072-token prompt + 49-token decode |
| 256K | native, legacy trim | 245,760/262,080 partial; 20.02 cumulative tok/s | not attempted | stopped for Spark handoff; not a correctness pass |
| 256K | native, all-`sm_90`, full question | 106,496/262,080 partial; 44.26 cumulative tok/s | not attempted | stopped for Spark handoff; not a correctness pass |

> [!CAUTION]
> These H200 figures are historical correctness-first bring-up measurements.
> The optimized Spark results above are separate and do not retroactively
> establish an H200 256K pass.

The isolated legacy-trim 256K row predates the final explicit `sm_90` rebuild
and executes through the CUDA toolkit-compatible default code object, with MMQ
already at `sm_90`. Its rate is partial bring-up data, not a native-`sm_90`
performance claim. The final overlay has every CUDA code object verified as
`sm_90`, passes the full resident graph/cache regression, and passes the
native-`sm_90` 32K API plus native 32K/64K/128K rows shown above. The
full-question attempt used that all-`sm_90` binary. At the user's direction,
both 256K attempts were stopped before decode and the remaining execution and
optimization were transferred to Spark. Precision, topology, and context were
not reduced to improve these figures.

The isolated 256K process also uses a legacy decode-reservation constant: it
keeps the final 20 tokens and omits the five-token prefix `QUESTION: Return
only a`, while retaining the full JSON/order instruction. Final ds4 revision
`d878ea1` corrects the tail to 25 tokens. The handoff's separately hash-pinned
262,080-token OpenAI fixture removes only filler and preserves the complete
question; that corrected server gate remains mandatory on GB10.

The OpenAI server also completed a structured `get_weather` tool-call/result
loop. Its no-thinking continuation reused the full 165-token live prefix and
evaluated only the 51-token tool-result/new-assistant suffix. Two simultaneous
deterministic requests on two resident sessions both returned the expected
output, exercising continuous batching and session isolation.

Machine-readable structural and numerical reports are included as
`MQ87-88-FIT-VERIFY.json` and `MQ87-88-FIT-SAMPLE-VERIFY.json`.
The human-readable artifact and host records are included as
`MIXED-QUANT.md` and `H200-DEVELOPMENT.md`.

H200 development has validated the pinned source inventory, official router,
PolyNorm, mHC, tokenizer/chat/tool handling, expanded and latent GDLA paths,
the full Q8_0 GGUF, the 302,080-token Q8 activation-collection pass, strict
residency, short/long native generation, and the OpenAI server path above.

This card claims the completed strict single-DGX-Spark 262,080-token-prompt
plus decode gate and the separate three-bank 196K-context serving gate only
under the exact conditions above. It does not claim concurrent 256K serving,
equivalent performance on other hardware or software configurations, or
downstream task quality.

## Limitations

- This is a hardware-oriented, very-low-bit routed-expert quantization. Quality
  must be evaluated for the intended languages, reasoning, code, tools, and
  long-context workloads.
- The public GGUF is a weight artifact, not a guarantee that an unrelated
  runtime implements Motif-3 correctly.
- The 262,144-token metadata comes from the source architecture; the measured
  validation in this card applies only to the pinned ds4-dfm configuration.
- DGX Spark uses coherent unified memory; conventional host-RAM plus discrete
  VRAM accounting describes a different deployment.

## Acknowledgements

- **[Motif Technologies](https://huggingface.co/Motif-Technologies)** — the
  Motif-3 model and official implementation.
- **[antirez/ds4](https://github.com/antirez/ds4)** — the original engine,
  loader, server, session machinery, and routed-MoE foundation.
- **[Entrpi/ds4-on-spark](https://github.com/Entrpi/ds4-on-spark)** — DGX Spark
  CUDA and unified-memory groundwork used by downstream ds4 development.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** — GGUF and the
  quantization formats used by this artifact.

Errors in this conversion, runtime port, calibration, or measurements are
ours, not theirs.

## License and attribution

The source model identifies its license as MIT. See the official
[`Motif-Technologies/Motif-3` model card](https://huggingface.co/Motif-Technologies/Motif-3)
for intended use, evaluation, citation, and license context.
