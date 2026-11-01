---
license: apache-2.0
base_model: AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored
base_model_relation: quantized
tags:
  - quantized
  - fp8
  - block-128
  - vllm
  - speculative-decoding
  - mtp
  - qwen3.5
  - qwen3.6
  - abliterated
  - uncensored
pipeline_tag: image-text-to-text
library_name: transformers
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - es
  - de
---

# Qwen3.6-27B-AEON-Ultimate-Uncensored-FP8-MTP

A vLLM-ready FP8 quantization of
[`AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored`](https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored)
(an abliterated fine-tune of Qwen3.6-27B), packaged in
**block-128 FP8** with the **Multi-Token Prediction (MTP) draft
head** taken verbatim from
[`Qwen/Qwen3.6-27B-FP8`](https://huggingface.co/Qwen/Qwen3.6-27B-FP8)
for vLLM speculative decoding.

In numbers:
- **0/100 refusals** on `mlabonne/harmful_behaviors[:100]`
  (vs 100/100 for vanilla Qwen3.6-27B-FP8) — abliteration preserved
- **+1–3 pp on gsm8k / ifeval** vs vanilla — capability preserved
- **+90 % decode TPS** vs the same checkpoint with no MTP, via
  speculative decoding at K=3 (~43–45 TPS on RTX A6000 / Ampere)
- **Byte-shape compatible with `Qwen/Qwen3.6-27B-FP8`** —
  `quant_method: "fp8"`, `weight_block_size: [128, 128]`, single
  vLLM `Fp8LinearMethod` loader path

## What's in the box

| Component | Format |
|---|---|
| Body weights (Linear modules outside the exclusion list) | FP8 e4m3fn, block-128 (`weight_scale_inv`, shape `(out/128, in/128)`) |
| Vision tower, `lm_head`, `embed_tokens`, `linear_attn.in_proj_{a,b,ba}` SSM state projections | BF16 (matches Qwen's `modules_to_not_convert` list, 882 entries) |
| MTP block (`mtp.*`) | Verbatim from `Qwen/Qwen3.6-27B-FP8` — 7 FP8 attention/MLP weights with block-128 scales + 8 BF16 norms / `mtp.fc` |
| Tokenizer | Same as upstream AEON-7 |
| Multimodal preprocessor configs | Same as upstream AEON-7 |

Total: 1606 tensors, ~31 GB across 7 safetensors shards.

## Why does this exist?

AEON-7's BF16 source ships **without** the `mtp.*` tensors that
Qwen ships in `Qwen/Qwen3.6-27B-FP8`. The fine-tune dropped them.
Loading AEON without MTP means `--speculative-config` is silently a
no-op — you can't speculative-decode AEON, even though the
architecture supports it.

We built this checkpoint by **re-quantizing AEON's BF16 source in
vanilla Qwen's exact FP8 format** (block-128 FP8, byte-shape
identical to `Qwen/Qwen3.6-27B-FP8`) and then dropping in vanilla's
`mtp.safetensors` shard verbatim. Because the body and the MTP
block share one quant scheme and one vLLM loader path
(`Fp8LinearMethod`, the same path Qwen tests their MTP block
against), the MTP head loads cleanly and the speculative decode
path works end-to-end.

The grafted MTP head was originally trained against vanilla Qwen
hidden states, so there's some risk that AEON's abliteration shift
would degrade draft acceptance. Measured result: **~58 %
acceptance** on both agentic prompts and harmful-behaviors prompts —
within ~1 pp of vanilla's own acceptance on the same K. Activation
drift from abliteration is small enough that the unmodified vanilla
MTP head generalizes to AEON's outputs.

Three other approaches were tried and rejected; full writeup with
methodology, comparison tables, and decision rationale is in the
companion repo
[`kasima/aeon-quantization`](https://github.com/kasima/aeon-quantization)
(`MTP-GRAFT.md`).

## Quick start — vLLM serve

```bash
vllm serve kasimat/Qwen3.6-27B-AEON-Ultimate-Uncensored-FP8-MTP \
  --host 0.0.0.0 --port 8000 \
  --served-model-name qwen3.6-27b-aeon \
  --max-model-len 262144 \
  --max-num-seqs 2 \
  --kv-cache-dtype fp8 \
  --gpu-memory-utilization 0.92 \
  --enable-chunked-prefill --enable-prefix-caching \
  --enable-force-include-usage --enable-prompt-tokens-details \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice --tool-call-parser qwen3_xml \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3}'
```

vLLM should log:
```
Resolved architecture: Qwen3_5MTP
Detected MTP model. Sharing target model embedding weights with the draft model.
Detected MTP model. Sharing target model lm_head weights with the draft model.
```

These three lines confirm MTP is wired up correctly. If you see
`Resolved architecture: Qwen3_5ForConditionalGeneration` instead,
vLLM fell back to the non-MTP path.

### Tested on
- vLLM 0.19.1
- Single RTX A6000 (Ampere, 48 GB VRAM, no native FP8 tensor cores
  — Marlin weight-only FP8 path on this hardware)
- Linux + CUDA 12.8

### Why K=3?

Vanilla `Qwen/Qwen3.6-27B-FP8` peaks at `num_speculative_tokens=4`.
AEON's grafted MTP head's draft acceptance falls faster than
vanilla's at deeper chain lengths — abliteration shift compounds
with chain depth. Measured AEON optimum:

| K | TPS @ 8k | accept |
|---:|---:|---:|
| 2 | 39.6 | 67 % |
| **3** | **45.4** | 60 % |
| 4 | 41.7 | 46 % |

K=3 wins on every bucket. Numbers above are decode TPS at 8 k input,
1024 output tokens, on the A6000.

## Eval results

### Refusal rate — `mlabonne/harmful_behaviors[:100]`

| Model | Refusals | Refusal rate | Wall clock |
|---|---:|---:|---:|
| `Qwen/Qwen3.6-27B-FP8` (vanilla baseline)        | 100/100 | 100.0 % | 709 s |
| `aeon-7-fp8` (AEON, no MTP — predecessor of this checkpoint) | **0/100** | 0.0 % | 1099 s |
| **This checkpoint** (block-128 FP8 + MTP K=3)    | **0/100** | 0.0 % | **592 s** (1.86×) |

Refusal rate stays at 0/100 — the body re-quant didn't perturb
abliteration, and the MTP graft didn't corrupt the target through
shared `lm_head` / embedding writes.

Wall-clock 1.86× faster than the no-MTP AEON variant on the same
100 prompts.

### Capability — gsm8k & ifeval (text-only subset)

Inherited from the AEON-7 BF16 quant; the block-128 re-quant uses the
same source weights and produces a checkpoint that vLLM serves via
the same `Fp8LinearMethod` path as the previous AEON FP8 build, so
these numbers transfer.

| Metric | `Qwen/Qwen3.6-27B-FP8` | AEON FP8 | Δ |
|---|---:|---:|---:|
| gsm8k strict-match (n=300)  | 84.67 % | **88.00 %** | +3.33 pp |
| gsm8k flexible-extract      | 86.67 % | **89.00 %** | +2.33 pp |
| ifeval prompt-strict (n=200)| 82.50 % | **84.00 %** | +1.50 pp |
| ifeval inst-strict (n=318)  | 88.05 % | **89.31 %** | +1.26 pp |

Both gsm8k and ifeval edge the vanilla baseline by 1–3 pp. The
deltas are within ~1 standard error on the sampled subsets, but the
consistent direction across two independent benches suggests it's
real (likely the "safety tax" — abliteration freeing latent
task-following capacity that was being suppressed by alignment).

### Speculative decode — vs no MTP, AEON only

Same checkpoint body, with vs without MTP K=3:

| Bucket | no MTP | MTP K=3 | Speedup |
|---|---:|---:|---:|
| 1k input, 1024 output  | 23.7 TPS | **43.5** | +83 % |
| 8k input, 1024 output  | 23.4 TPS | **45.4** | +94 % |
| 32k input, 1024 output | 22.9 TPS | **42.5** | +86 % |
| harmful_behaviors[:50], 1024 output | — | **44.6** | — |

Decode TPS = output_tokens / (last_chunk_t − first_chunk_t),
streaming `/v1/chat/completions`, `temperature=0`,
`enable_thinking=False`, 5 timed iters/bucket (warmup discarded).

## Reproducer

The file `quantize-aeon-deepseek.py` (included in this repo) is the
exact script used to produce this checkpoint. CPU-only, ~3 min wall
on a 64 GB host. Methodology in short:

1. Load `AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored` BF16 source
   on CPU via `AutoModelForImageTextToText` (preserves multimodal
   wrapping, tensors named `model.language_model.layers.*`).
2. For each `Linear` weight outside vanilla's 882-entry
   `modules_to_not_convert` list (vision tower,
   `linear_attn.in_proj_{a,b,ba}` SSM state projections, lm_head,
   embed_tokens), block-128 FP8 quantize:
   ```
   scale_inv[i, j] = max(|W[i*128:(i+1)*128, j*128:(j+1)*128]|) / 448
   W_fp8[...] = (W_bf16 / scale_inv).clamp(-448, 448).to(float8_e4m3fn)
   ```
   Symmetric per-tile scaling — dequantization is `W * scale_inv`
   per block. This matches the storage convention vLLM's
   `Fp8LinearMethod` reads when `quantization_config.quant_method`
   is `"fp8"` with `weight_block_size: [128, 128]`.
3. Append `mtp.safetensors` from `Qwen/Qwen3.6-27B-FP8` verbatim.
4. Stamp `quantization_config` with vanilla Qwen's exact shape
   (`quant_method: "fp8"`, `weight_block_size: [128, 128]`,
   `activation_scheme: "dynamic"`, `fmt: "e4m3"`, full 882-entry
   `modules_to_not_convert` list inherited).

To regenerate from scratch:

```bash
git clone https://github.com/kasima/aeon-quantization
cd aeon-quantization
# requires the `quant` venv (transformers 5.x, accelerate, ~64 GB RAM)
CUDA_VISIBLE_DEVICES="" python quantize/quantize-aeon-deepseek.py
```

## Inheritance & lineage

- **Base model:**
  [`AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored`](https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored)
  — abliteration of `Qwen/Qwen3.6-27B`, KL ≈ 0.000492 vs base
  (per AEON-7's published claim).
- **Format reference:**
  [`Qwen/Qwen3.6-27B-FP8`](https://huggingface.co/Qwen/Qwen3.6-27B-FP8)
  — block-128 FP8 release that `quant_method`, `weight_block_size`,
  the `modules_to_not_convert` list, and the `mtp.*` block are all
  inherited from.
- **Companion GGUF release** (different toolchain, BF16-source-derived):
  [`kasimat/Qwen3.6-27B-AEON-Ultimate-Uncensored-GGUF`](https://huggingface.co/kasimat/Qwen3.6-27B-AEON-Ultimate-Uncensored-GGUF)
  — 9 quants Q2_K → Q8_0 with imatrix, for llama.cpp / Ollama / LM Studio.

## Tooling versions

These exact versions produced this checkpoint:

| Tool | Version | Notes |
|---|---|---|
| transformers | 5.6.2 | needed for `qwen3_5` model architecture |
| torch | 2.10.0+cu128 | |
| safetensors | 0.6.x | |
| accelerate | 1.13.0 | for `device_map="cpu"` |
| Python | 3.12 | |

Loaded by:

| Tool | Version |
|---|---|
| vLLM | 0.19.1 |

## Intended use

Research, unrestricted generation, agentic workloads where
production-grade safety alignment is supplied at the application
layer (system prompts, output filtering, etc.) rather than baked
into the model.

This checkpoint inherits AEON-7's abliteration (refusal removal). It
will produce substantive answers to harmful prompts, including
detailed instructions for activities that the vanilla Qwen model
would refuse. **Do not deploy without an application-layer safety
strategy appropriate to your use case.**

## Limitations

- The MTP draft head was trained against vanilla Qwen3.6-27B, not
  against AEON's abliterated activations. Acceptance is ~58 % on
  agentic + harmful prompts at K=3 — strong, but a fresh MTP
  fine-tune on AEON activations would likely close the remaining
  ~1 pp gap to vanilla's own acceptance. Out of scope for this
  release.
- K=5 hits a known vLLM 0.19.x bug in the Gated DeltaNet attention
  backend's spec-decode metadata builder
  (`gdn_attn.py:spec_state_indices_tensor`). K=4 works; K=3 is the
  measured maxima for AEON anyway.
- Tested only on Ampere (RTX A6000). On Blackwell, the standalone
  `Fp8LinearMethod` path will use native FP8 tensor cores and
  performance characteristics will differ. The format itself is
  unchanged.

## License

Apache 2.0, inherited from both `Qwen/Qwen3.6-27B-FP8` and
`AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored`.

## Acknowledgements

- Qwen team for releasing FP8 weights including the MTP head, and
  the block-128 FP8 format that this checkpoint inherits
- AEON-7 / abliteration authors for the directional abliteration
  technique and the source checkpoint
- vLLM project for the speculative-decoding infrastructure
- Neural Magic / Red Hat AI for the `compressed-tensors` ecosystem
  that produced the predecessor AEON FP8 quant
