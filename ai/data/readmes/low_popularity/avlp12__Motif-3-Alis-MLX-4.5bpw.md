---
language:
- en
- ko
license: mit
library_name: mlx
pipeline_tag: text-generation
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
tags:
- mlx
- moe
- korean
- quantized
- apple-silicon
- motif
- mixed-precision
- 4-bit
- conversational
---

# Motif-3 · Alis MLX 4.5bpw (speed tier)

Mixed-precision MLX build of [Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)
(314.8B total / 13.2B active MoE, MIT) for Apple silicon — the **speed tier** companion to
[avlp12/Motif-3-Alis-MLX-8bit](https://huggingface.co/avlp12/Motif-3-Alis-MLX-8bit).
Decode is read-bandwidth-bound at batch 1, so halving the bits nearly halves the per-token
read: **~50 tok/s** with MTP self-speculative decoding (k=3) on a single M3 Ultra —
about **+35% over the 8-bit build** at matching settings — at a small, measured quality cost (tables below).

| Build | Size | bpw | Decode (M3 Ultra, MTP k=1) |
|---|---|---|---|
| 8-bit (reference) | 312 GiB | 8.50 | 37.1 tok/s |
| **this repo** | **167 GiB** | **4.55** | **50.2 greedy (peak 53)** |

Fits a 256 GB Mac with full headroom; a 192 GB M2/M3 Ultra fits with a raised wired limit
and modest context.

## Measured performance (M3 Ultra 512 GB)

| Metric | Value |
|---|---|
| Decode, plain | 28.4 tok/s |
| Decode, MTP k=3 greedy | **50.2 tok/s** (5-prompt avg, range 43–53) |
| Decode, MTP k=3 @ T=0.8 | **32.1 tok/s** (equality acceptance; rejection sampling is a k=1-only option — sampled drafts degrade chained anchors) |
| Prefill | **~790 tok/s** @ 8k on natural mixed text · ~580 @ 2k (chunked, step 2048; ≈75% of the measured bf16-GEMM ceiling). Highly repetitive prompts can drop to ~545: expert-routing skew fattens the small-group tail in `gather_qmm` ([upstream report](https://github.com/ml-explore/mlx/issues/4246)) |
| Peak memory | ~180 GB |

Speed stack (all in the [install fork](https://github.com/avlp12/mlx-lm/tree/motif3-support)):
single-kernel Sinkhorn for the mHC gates, compiled activation/glue fusions (PolyNorm,
router, mHC mixes, attention epilogue — bit-exact, kill switches `MOTIF_COMPILE_ACT/GLUE=0`),
an mHC-transition mega-kernel (one threadgroup per position fuses the 16K rmsnorm, gate
projections, Sinkhorn, premix, and input layernorm — ~7 serial dispatches to 1, +17%;
`MOTIF_MHC_TRANS=0`),
and vendor-faithful MTP self-speculative decoding (wiring confirmed by Motif in
[this discussion](https://huggingface.co/Motif-Technologies/Motif-3/discussions/4)) with
correct chained-draft norm handling. **k=3 drafting wins on Apple silicon**: batch-1 decode
is latency-bound, so verifying 4 tokens costs only ~1.5x one token — the economics invert
Motif's (compute-bound, vLLM) "1 speculative token is optimal" guidance. Leviathan
rejection-sampling acceptance remains available for k=1 (`MLX_MTP_REJECTION=0` to disable).

## Quality vs the 8-bit build

Teacher-forced NLL and greedy top-1 agreement against the 8-bit reference on short
KO/EN/code probes (same final-release weights; probe-scale — treat as indicative, not
benchmark-grade. *top-1 measured on the shorter 300-token probe, on which the KO NLL delta
read +9.9% — probe-scale variance; the 1.5k-token probe is the better estimate):

| Probe | NLL Δ vs 8-bit | top-1 agreement |
|---|---|---|
| Korean prose (1.5k-token probe) | **+2.4%** | 89.0%* |
| English prose | −0.8% | 89.1% |
| Python code | −3.2% | 98.8% |

If you want maximum fidelity (e.g. as a distillation teacher), use the
[8-bit build](https://huggingface.co/avlp12/Motif-3-Alis-MLX-8bit). Motif themselves ship a
4-bit [NVFP4 checkpoint](https://huggingface.co/Motif-Technologies/Motif-3-NVFP4) for vLLM,
and report the MTP head keeps ≥70% draft acceptance at 4-bit — consistent with what this
build measures.

## Quantization recipe

C6 mixed profile: experts 4-bit g64, attention/dense/shared-expert 6-bit, `wkv_a` 8-bit
(latent chokepoint), router gate / mHC / `lambda_proj` / norms / PolyNorm coefficients in
bf16. MTP head 8-bit (`model-mtp.safetensors`, +254 MB). Per-tensor map in `config.json`.
Tensors >2³¹ elements sanitized without `mx.split` (mlx#3836 workaround, byte-verified).

## Install & run

```bash
pip install git+https://github.com/avlp12/mlx-lm.git@motif3-support
mlx_lm.generate --model avlp12/Motif-3-Alis-MLX-4.5bpw \
  --prompt "한국의 전통 건축양식을 요약해줘." --max-tokens 400 --temp 0.7 --mtp --mtp-num-draft-tokens 3
# OpenAI-compatible server:
mlx_lm.server --model avlp12/Motif-3-Alis-MLX-4.5bpw --port 8003 --mtp --mtp-num-draft-tokens 3
```

## Usage notes

- Sampling: temp ≈ 0.6–0.8. At temp 0 the think channel can enter repetition loops.
- `--mtp-num-draft-tokens 3` is optimal on Apple silicon (latency-bound verify makes
  wide drafting cheap; k=2 is within noise, k=1 is ~−20%). Motif's own "1 speculative
  token" guidance applies to compute-bound GPU serving, not this regime.
- Greedy transcripts under MTP can diverge from the plain path after many tokens (ULP-class
  tie flips between batched-verify and single-step kernels); the sampling distribution is
  equivalent.
