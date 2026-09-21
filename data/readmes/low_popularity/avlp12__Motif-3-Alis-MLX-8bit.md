---
language: [en, ko]
license: mit
library_name: mlx
pipeline_tag: text-generation
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
tags: [mlx, moe, korean, quantized, apple-silicon, motif, 8-bit, reasoning]
---

# Motif-3 — MLX 8-bit (Q8, single Apple M3 Ultra)

**314.8B total parameters (13.2B active per token).** The sidebar "params" chip is currently
miscounted by the Hub for quantized MLX repos (it counts packed uint32 elements; the correct
`total_parameters` is declared in `model.safetensors.index.json` — reported upstream).

8-bit (group-size 64, affine) MLX quantization of
**[Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)** — the final release of
Motif Technologies' Korean-emphasized reasoning MoE (MIT license).

## At a glance

| | |
|---|---|
| Architecture | 53 layers (2 dense + 51 MoE) · 384 routed experts, top-8 + 1 shared |
| Attention | GDLA — grouped differential latent attention, 80 heads (16 KV), gated output |
| Extras | Expert-wise PolyNorm activation · mHC (manifold-constrained hyper-connections, E=4) |
| Context | 262,144 (YaRN ×64 from 4,096; `apply_yarn_scaling: false` per vendor config) |
| Vocab | 220,160 · reasoning chat template (auto-opens a `<think>` channel) |
| Size on disk | **312 GiB (8.50 bpw)** — fits a single 512 GB M3 Ultra with ~180 GB headroom |

## Measured performance (M3 Ultra 512 GB, greedy)

| Metric | Value |
|---|---|
| Decode | **37.1 tok/s** with MTP self-spec (k=2, 5-prompt avg, range 34–39) · 24.5 plain (fused stack) · 14.4 eager |
| Prefill | **~790 tok/s** @ 8k on natural mixed text · ~575 @ 2k, matching the 4.5bpw build (prefill is compute-bound; was 143 before the fused-kernel stack). Highly repetitive prompts can drop to ~545 — expert-routing skew, see the [upstream report](https://github.com/ml-explore/mlx/issues/4246) |
| Peak memory | ~334 GB |

The mHC gates' 20-iteration Sinkhorn loop is ~4,200 tiny GPU dispatches per token in the
eager path; the fork fuses it into one Metal kernel, and further compiles the remaining
elementwise glue (PolyNorm activations, router, mHC mixes, attention epilogue — all
bit-exact, kill switches `MOTIF_SINKHORN_KERNEL/MOTIF_COMPILE_ACT/MOTIF_COMPILE_GLUE=0`):
eager 14.4 → 24.5 tok/s plain decode, and an mHC-transition mega-kernel (one threadgroup
per position fuses the 16K rmsnorm, gate projections, Sinkhorn, premix, and input
layernorm; `MOTIF_MHC_TRANS=0`) worth another +21% under MTP. Numerics vs eager: KL 2.2e-3, 0% top-1 flips over
256 positions.

## Speed-tier sibling

Need more speed and can spare a little fidelity? The
[4.5bpw sibling build](https://huggingface.co/avlp12/Motif-3-Alis-MLX-4.5bpw) (167 GiB)
decodes at ~50 tok/s — about +35% over this build — at a small measured quality cost
(KO long-form NLL +2.4% vs this 8-bit reference). This 8-bit build remains the fidelity
reference.

## MTP self-speculative decoding (opt-in)

This build ships the vendor-trained MTP (nextn) block, quantized 8-bit
(`model-mtp.safetensors`, +267 MB). With the fork, `--mtp --mtp-num-draft-tokens 2` chains
two draft tokens per step and verifies them in one batched forward — distribution-lossless:
**24.5 → 37.1 tok/s (+51%)**. (On this 8-bit build k=2 is optimal: the fused-kernel stack
pushes decode toward bandwidth-bound, where 8-bit's larger per-token reads make wide
verify costlier — the 4.5bpw sibling prefers k=3.) The wiring is vendor-confirmed
([discussion](https://huggingface.co/Motif-Technologies/Motif-3/discussions/4)): post-final-norm
hidden anchor, `[h ; embed_norm(emb)]` concat, SWA attention for the MTP block, and chained
drafts fed back from `final_layernorm` output (re-normalizing the chain crushes chained
acceptance — the fork handles this correctly). **k=3 wins on Apple silicon** because batch-1
decode is latency-bound: verifying 4 tokens costs ~1.5x one token, inverting Motif's
compute-bound "1 speculative token is optimal" vLLM guidance. Per-draft acceptance is ~70-80%
greedy (an earlier revision of this card quoted "38–41%" — that was the fraction of emitted
tokens from the draft, a/(1+a), not per-draft acceptance). For k=1 only, Leviathan
rejection-sampling acceptance is auto-enabled for pure-temperature requests (~60% → ~73%
acceptance at T=0.8; kill switch `MLX_MTP_REJECTION=0`) — with k≥2 sampled drafts degrade
the chained anchors, so equality acceptance is used. Note: greedy transcripts under MTP can
diverge from the plain path after many tokens (batched-verify vs single-step kernels —
ULP-class tie flips); the sampling distribution is equivalent.

## Install & run

```bash
pip install git+https://github.com/avlp12/mlx-lm.git@motif3-support
mlx_lm.generate --model avlp12/Motif-3-Alis-MLX-8bit \
  --prompt "한국의 전통 건축양식을 요약해줘." --max-tokens 400 --temp 0.7
# OpenAI-compatible server:
mlx_lm.server --model avlp12/Motif-3-Alis-MLX-8bit --port 8003
```

## Quantization recipe

All expert/attention/dense projections 8-bit g64 affine (632 tensors, per-tensor map in
`config.json`). Kept in bf16: router gate, `mhc_*`, `lambda_proj`, norms, PolyNorm
coefficients. The MTP head is dropped (not instantiated by the modeling code). Tensors with
>2³¹ elements are sanitized without `mx.split` (upstream mlx#3836 silent-corruption
workaround; byte-verified).

## Usage notes

- **Sampling**: use temp ≈ 0.6–0.7. At temp 0 the think channel can enter repetition loops.
- **Verbatim recall** (anthems, poems, legal text) is unreliable — the model may blend
  historical variants; pair with retrieval/web grounding for exact quotations.
- The chat template opens `<think>` automatically; servers that split reasoning
  (e.g., this fork) return it in `message.reasoning`.

## Provenance & verification

Port lineage: the Motif-3-Beta port (avlp12/Motif-3-Beta-Alis-MLX-*) — 4-layer parity vs the
vendor's fixed reference at ~1e-7 KL/token, plus the PolyNorm/BUG-5 saga resolved with the
Motif team (HF discussions). The final release confirms the Beta RoPE hypothesis B
(`apply_yarn_scaling: false`, amplitude 1.0). Methodology and receipts:
[alis-dwq](https://github.com/avlp12/alis-dwq).

Smoke-verified on Korean and English prompts; served as a web chat (Open WebUI over
`mlx_lm.server`) on a single M3 Ultra.
