---
base_model: dots-studio/dots3-note-prev
base_model_relation: quantized
license: apache-2.0
language:
  - en
  - ko
  - zh
pipeline_tag: text-generation
library_name: gguf
tags:
  - gguf
  - dots3
  - dots3-note
  - mixture-of-experts
  - mixed-quantization
  - iq2_xxs
  - dgx-spark
  - long-context
---

# dots3-note-prev — Mixed-Quant GGUF

> **Update 2026-09-06 — first optimization campaign on the native ds4 path.** Six rounds on [`ds4-dfm-rs`](https://github.com/Baekpica/ds4-dfm-rs) ([`84cbfe1`](https://github.com/Baekpica/ds4-dfm-rs/commit/84cbfe1); [`docs/dots3-optimization-2026-09-06.md`](https://github.com/Baekpica/ds4-dfm-rs/blob/84cbfe1/docs/dots3-optimization-2026-09-06.md)) move this artifact's cold 8,192-token single-shot prefill on one DGX Spark from **278.3 to 604.3 tok/s (+117 %)** and the following greedy decode from **11.66 to 16.78 tok/s (+44 %)**, time to first token 0.140 → 0.113 s, same VMM owner, one fresh serial worker per run, medians of three. Three prefill rounds put the absorbed-MLA path on the tensor cores — the DSA / sliding-window latent attention (+65 %), the value projection (+14 %) and the Q/K absorption (+14 %) — and three decode rounds split the per-token attention walk across the SMs (+42 %), group the decode-width value projection and fuse the attention-side launches. The prefill kernels round Q, P and activations to FP16 (the BF16 cache rows convert exactly); every decode-side change is bit-identical or an fp32 reorder of the previous kernels. Frontier logits at 8,192 tokens before and after: same argmax, top-10 9/10, KL 2.2e-3; the 64-token greedy continuation agrees through token 30 and then resolves a near-tie differently (it flips back and forth between rounds, see the doc); the CPU-reference forward gate, chunk/ring parity, the 2,600-token DSA determinism check and the 262,144-context allocation pass on the final binary. Still a short-context, text-only, serial-lane measurement — not a 524,288-token result.

**Language+MTP mixed-quant of `dots-studio/dots3-note-prev` for one 128 GB-class
DGX Spark at the source 524,288-token context.** Vision and audio encoders are
omitted. This is an independent conversion, not an official Dots Studio release.

Nothing is pruned, merged, expert-dropped, or layer-dropped. The artifact keeps
all 46 text layers, the extra MTP block, all 256 routed experts per sparse
layer with sigmoid top-8 / `noaux_tc` routing, the shared expert, MLA, the
headwise attention gate, and DSA indexer projections on the 13 full-attention
layers.

| | |
|---|---:|
| Architecture | dots3note, 46 text + 1 MTP, 13 full / 33 SWA MLA |
| Routed experts retained | **256 / 256 per sparse layer** |
| GGUF tensors | **956** |
| Unsharded artifact | **80.156 GiB** (86,072,934,272 bytes) |
| Split set | **10 shards**, 86,072,935,456 bytes |
| Source context limit | 524,288 tokens |
| Native Spark / ds4 execution | **verified (text-only, serial)** |

This file is a **ds4-native** conversion, not a llama.cpp drop-in. The header
is now `general.architecture = dots3note` with `dots3note.*` keys (the
hyphenated `dots3-note` form is still accepted by ds4). MLA is stored as a
fused `attn_kv_b` tensor. llama.cpp since
[#27060](https://github.com/ggml-org/llama.cpp/pull/27060) (2026-08-21)
registers the same architecture string but expects absorbed
`attn_k_b`/`attn_v_b` plus its own indexer and hparam names, so this artifact
still does not load there. For llama.cpp use a converter-native GGUF such as
[`bartowski/dots-studio_dots3-note-prev-GGUF`](https://huggingface.co/bartowski/dots-studio_dots3-note-prev-GGUF)
(`b10569+`). Native Spark execution of *this* artifact is on
[`Baekpica/ds4-dfm-rs`](https://github.com/Baekpica/ds4-dfm-rs).
Use the first public shard as the model path; no merge or requantization is
required.

## Native ds4 on DGX Spark

Keep the VMM weight owner alive while starting or restarting the serial worker:

```bash
MODEL=/path/to/dots3-note-prev-MQ87-00001-of-00010.gguf
RUN=/path/to/dots3-run

./ds4_weight_server --base "$MODEL" --manifest "$RUN/weights.manifest" \
  --backend vmm --scope base --reserve-gb 24 --no-repack-q8-aligned

DS4_SERVER_CONTINUOUS=0 \
DS4_CUDA_WEIGHT_IPC_MANIFEST="$RUN/weights.manifest" \
DS4_CUDA_WEIGHT_IPC_SCOPE=base \
./ds4-server -m "$MODEL" --cuda -c 4096 --host 0.0.0.0 --port 8003 \
  --model-id dots3-note-prev --no-spec --no-update-check --mem-floor-gb 8
```

On one DGX Spark GB10, `/v1/models`, a 21-token OpenAI Chat request plus
decode, and settled `/v1/stats` passed at `-c 4096`. The resident gate also
passed CPU/GPU forward parity, chunk/ring prefix reuse, a 2,600-token DSA
determinism smoke, and allocation of the 262,144-context graph. These are
correctness and lifecycle checks, not a 524,288-token throughput result.

The `dfm` build at `1126217` measured **267.53 tokens/s** for a 1,600-token
single-chunk prefill and **12.314 tokens/s** for the following single-token
decode (median of three resident-gate runs, public MQ87 shards, VMM owner,
serial worker). This short-context measurement is not a 524,288-token result.
The 2026-09-06 ds4-dfm-rs rounds below raise the 8,192-token cold prefill to
604.3 tokens/s and the following greedy decode to 16.78 tokens/s on the same
host (section "2026-09-06 optimization campaign").

## 2026-09-06 optimization campaign (ds4-dfm-rs)

Measured on one DGX Spark GB10 (driver 610.43.02, CUDA 13.3) with the VMM
weight owner (`ds4_weight_server --backend vmm --reserve-gb 24
--repack-q8-aligned`) resident and one fresh serial `ds4-bench` process per
run: an 8,192-token cold prefill of the official `modeling_dots3_note.py`
source (`--ctx-start 8192 --ctx-max 8192 --ctx-alloc 8257`), three
prefill-only runs plus one 64-token greedy continuation per cell, medians.
Every round is measured on one binary through its kill switch, so the
cells share the hour and the owner state. Full method, profiles and gates:
[`docs/dots3-optimization-2026-09-06.md`](https://github.com/Baekpica/ds4-dfm-rs/blob/84cbfe1/docs/dots3-optimization-2026-09-06.md).

| round | change | prefill tok/s | decode tok/s |
|---|---|---:|---:|
| baseline path (`1f7933f` kernels) | scalar FP32 latent attention, raw-row absorb / value walks | 278.3 | 11.66 |
| prefill 1 | DSA / sliding-window latent attention on tensor cores (FP16 operands, per-token key gather, `ldmatrix`, register prefetch) | 459.4 (+65.1 %) | 11.66 |
| prefill 2 | value projection GEMM per head on the transposed Q8_0 artifact planes (exact int8 codes, FP32 per-block scales) | 522.5 (+13.7 %) | 11.65 |
| prefill 3 | Q/K absorption GEMM per head over the raw Q8_0 rows | 595.3 (+13.9 %) | 11.65 |
| decode 1 | split-K decode attention (16 key ranges + combine) | 594.4 | 16.59 (+42.3 %) |
| decode 2 | grouped decode-width value projection (four column groups, fp32 reorder of the block sum); three decode absorb rewrites measured slower and rejected | 596.4 | 16.72 (+0.8 %) |
| decode 3 | fused attention-side launches (kv finish, gated value epilogue, indexer finish, one-pass FFN residual; all bit-identical) | 602.7 (+1.2 %) | 16.35 (+0.5 %) |

Numerics: the prefill kernels round Q, P, activations (and the absorption
weights) to FP16 and accumulate in FP32; the decode changes are bit-identical
or fp32 reorders. Gates on the final binary: frontier logits at 8,192 tokens
(baseline path vs all rounds) argmax 284 / 284 / top-10 9/10 / KL 2.2e-3 /
rel RMS 5.9e-2 (band: same argmax, top-10 ≥ 8, KL ≤ 0.05, rel RMS ≤ 0.11); the 64-token greedy continuation agrees through token 30 and resolves a near tie at token 31 differently (it flips back with the split attention and again with the grouped value projection, so this is a tie, not drift); `tests/test_dots3_resident`
(CPU FP32 reference cos 0.997816, one-shot/split cos 0.999253, argmax
3925 on all three; chunk/ring parity; DSA 2,600-token determinism; 262,144
context allocation) passed. Kill switches: `DS4_DOTS3_ATTN_NO_HMMA`,
`DS4_DOTS3_VALUE_NO_HMMA`, `DS4_DOTS3_ABSORB_NO_HMMA`, `DS4_DOTS3_ATTN_NO_SPLIT`,
`DS4_DOTS3_ABSORB_NO_DECODE`, `DS4_DOTS3_VALUE_NO_DECODE`, `DS4_DOTS3_NO_FUSED`
(`=1` restores the previous path).

This remains a short-context, text-only, serial-lane measurement; the
524,288-token prefill plus decode is still an open release gate.

## Precision recipe

| Tensor group | Type | Rationale |
|---|---|---|
| Token embedding, LM head, MTP embedding | `Q8_0` | token/logit fidelity |
| MLA projections, attention gate, DSA indexer | `Q8_0` | attention / long-context stability |
| Dense MLP (layer 0 + MTP), shared expert, `eh_proj` | `Q8_0` | always active |
| Routed expert gate/up, layers 1–45 | `IQ2_XXS` + BF16 imatrix | dominant parameter mass |
| Routed expert down, layers 1–45 | `Q2_K` + BF16 imatrix | capacity baseline |
| Router weights and `e_score_correction_bias` | `F32` | top-8 decision stability |
| RMSNorm, indexer k_norm | `F32` | normalization stability |

## Calibration

The corpus reuses the checksum-pinned Healing-Mix shares from
[`Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix`](https://huggingface.co/datasets/Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix)
@ `1931f3a40cc3463217f9c7d25906f80ded029264`, re-tokenized with the official
dots3-note tokenizer.

| | |
|---|---:|
| Documents | 1,330 |
| Official-tokenizer tokens | 4,120,456 |
| Imatrix chunks | 8,047 × 512 = 4,120,064 tokens |
| Seed | 1234 / collector 3407 |

Activation collection is official BF16 MLA + sigmoid top-8 MoE. Chunks are 512
tokens; SWA window is 513 and DSA top-k is 2048, so inside a chunk both sparse
attention modes attend to the entire causal prefix and the indexer is skipped.
A small number of never-routed expert cells (mostly layer 1) were filled with
that layer's mean importance; the raw gap is recorded in the imatrix report.

## Source pin

- Model: [`dots-studio/dots3-note-prev`](https://huggingface.co/dots-studio/dots3-note-prev)
- Revision: `1e1e7b0cd37a3a48a6c8d7fa55d5f9d14377006b`
- License: Apache-2.0

## Limitations

- This is a hardware-oriented, very-low-bit routed-expert quantization.
- The public GGUF is a weight artifact, not a guarantee that an unrelated
  runtime implements dots3-note correctly.
- 524,288-token metadata is the source architecture limit. The verified ds4
  evidence stops at a 262,144-context allocation and a short 4K prefill/decode;
  a real 524,288-token prefill plus decode remains an explicit release gate.
- ds4-dfm-rs serves text. Continuous banks are opt-in (`--max-seqs`);
  `ds4 --serving-check` qualifies them with partial prefix reuse, disk KV and
  snapshots ([record](https://github.com/Baekpica/ds4-dfm-rs/blob/b32e44f7a2f5c8ad66d7fba3d8897c4803b9ae16/docs/benchmarks/serving-checklist-2026-11-02/README.md)). The retained MTP block runs on the serial
  lane when selected (`--mtp-mode on`), unqualified.
- Vision and audio are not in this file.

## Acknowledgements

- **[Dots Studio](https://huggingface.co/dots-studio)** — the source model.
- **[antirez/ds4](https://github.com/antirez/ds4)** and the Baekpica Motif-3 /
  Solar Open 2 mixed-quant pipeline this conversion follows.
