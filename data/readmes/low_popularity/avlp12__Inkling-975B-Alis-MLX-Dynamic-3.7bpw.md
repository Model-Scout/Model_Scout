---
language:
- en
- ko
- zh
license: apache-2.0
library_name: mlx
pipeline_tag: image-text-to-text
tags:
- inkling_mm_model
- image-text-to-text
- audio-text-to-text
- quantized
- mixture-of-experts
- moe
- multimodal
- apple-silicon
- mixed-precision
- 3-bit
- dwq
- conversational
base_model: thinkingmachines/Inkling
base_model_relation: quantized
---

# Inkling-975B-Alis-MLX-Dynamic-3.7bpw

> The **quality / golden-spot** tier of the Inkling · Alis MLX Dynamic family — siblings: the [\~2.7 bpw size-optimal build](https://huggingface.co/avlp12/Inkling-975B-Alis-MLX-Dynamic-2.7bpw) and the [\~6.6 bpw two-box Q6 performance build](https://huggingface.co/avlp12/Inkling-975B-Alis-MLX-Dynamic-6.6bpw). Full family: [Inkling 975B · Alis MLX Dynamic collection](https://huggingface.co/collections/avlp12/inkling-975b-alis-mlx-dynamic-6a5f2d32de21740f9fdfc390).

**Apple Silicon (MLX) mixed-precision quantization of [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling)** — a 975B-class multimodal Mixture-of-Experts model (66 hybrid decoder layers, **256 routed experts (top-6) + 2 shared** per MoE layer, hidden 6144, sliding-window attention + short-convolution hybrid, vision + audio front-ends, 201K vocab).

This build targets the **golden spot for a single 512 GB M3 Ultra: near-teacher quality in one box** — \~3.71 bits/weight, with the entire non-expert skeleton kept at **exact BF16**, and quantization scales certified by a **fully receipt-sealed, layer-local ALIS-DWQ pass** run as a distributed two-Mac pipeline.

---

## Quality-first recipe

Bits go where the parameters are; exactness stays where the control flow is. \~96% of weights (the routed expert bank) take the cheap bits; **everything a token's routing, attention, or modality path depends on stays BF16** — a stricter split than most mixed builds, which quantize attention too.

| Component | Precision | Share | Why |
|---|---|---|---|
| Routed experts `w13`/`w2` (layers 3–65) | **3-bit affine, g128** | 345 GiB | the parameter bulk |
| Attention (all 5 proj., hybrid + sconv) | **BF16** | — | every token's critical path |
| Router / gates | **BF16** | — | discrete top-6 routing — never quantized |
| Shared experts | **BF16** | — | on every token |
| Embeddings · LM head · norms | **BF16** | — | distribution-sensitive |
| Vision + audio towers | **BF16** | — | modality front-ends kept exact |
| Layers 0–2 (entirely) | **BF16** | — | early-layer protection |

> **Dropped:** the source's MTP head (`model.mtp.*`, 5.26B params) — a speculative-decoding accessory not used by the MLX runtime. All three family tiers drop it identically, which is why they report **947B logical params** vs the source's 952B.

| | |
|---|---|
| **Base model** | thinkingmachines/Inkling (975B-class; 952.4B source / 947.1B logical params) |
| **Bits/weight** | **3.706** effective (439 GB total) |
| **On-disk size** | 438.8 GB (408.7 GiB), 108 shards |
| **Format** | MLX safetensors (`inkling_mm_model`) |
| **Modalities** | text + image + audio inputs |
| **Attention** | sliding-window (512) hybrid + short conv — KV stays small at long context |

---

## What makes this build different: a sealed, audited DWQ pass

Most public quants ship converted weights. This one ships converted weights **plus a machine-checkable certification trail**. The quantization scales/biases were passed through **layer-local ALIS-DWQ** ([alis-dwq](https://github.com/avlp12/alis-dwq)) against exact **BF16 teacher activations**, under a guard-and-receipt harness originally built for reproducible two-box runs:

- **BF16 teacher boundaries, not logits-only:** the full-precision teacher was run as a **distributed pipeline across two 512 GB Macs** (layers 0–32 / 33–65), dumping per-layer input/target activations (h₀…h₆₆) for 72 calibration batches across **text, image, and audio** — so every decoder layer trains against its own exact teacher boundary, per modality.
- **Layer-local, memory-bounded training:** each layer is strict-loaded alone (never the full model) and its affine scales/biases tuned with stop-gradient teacher boundaries and valid-token NMSE. Differentiating a 256-expert quantized gather naively materializes \~150 GiB of dequantized workspace; this pass uses an **expert-group × token-block serialized backward** that provably matches the fused gradients (cosine ≥ 0.9985) at a **\~23 GiB peak** — the whole optimization ran inside a watchdog envelope of *min 90% system RAM free, zero swap growth*.
- **Do-no-harm acceptance, per layer:** a layer's new scales are kept **only if held-out boundary NMSE does not regress at all** (allowed regression: 0.0); otherwise the layer rolls back to baseline, byte-exact. Of 63 tuned layers, 62 certified neutral and **layer 40 committed a genuine improvement** — that accepted delta is what distinguishes these weights from the raw conversion.
- **Every step is evidence:** each layer ran as a sealed process chain (frozen runtime bundle → launch pin → guarded watchdog → atomic no-clobber receipts), and the 63 terminal receipts link into a hash chain closed by an **`advanced-completion` receipt (status: pass)**. Nothing in this repo was produced by an unaudited script run.

The result is conservative by construction: **you get provably-not-worse-than-baseline weights with a certified improvement where one was found** — not a quant that traded unknown regressions for a benchmark bump. (A higher-lr DWQ tier on the same evidence rails is planned as a separate revision.)

---

## Sibling builds

| Build | bpw | Size | For |
|---|---|---|---|
| **this** — quality / golden spot | **3.71** | 409 GiB | single 512 GB Mac, best quality in one box |
| [capacity / size-optimal](https://huggingface.co/avlp12/Inkling-975B-Alis-MLX-Dynamic-2.7bpw) | 2.72 | 299 GiB | single Mac with generous headroom / smaller boxes |
| [Q6 teacher (two-box)](https://huggingface.co/avlp12/Inkling-975B-Alis-MLX-Dynamic-6.6bpw) | 6.60 | 728 GiB | maximum fidelity, 2 × 512 GB pipeline serving |

---

## Usage

The `inkling_mm_model` architecture is served by the project's MLX port (hybrid sliding-window + short-conv attention, 256-expert gather MoE, multimodal towers); upstream `mlx-lm` support is not yet merged. Until the port lands upstream, treat this repo as **weights + provenance**, loadable with the Inkling MLX runtime from the alis pipeline:

```python
# Inkling MLX runtime (alis pipeline port)
from inkling_mlx.model import load_model
model = load_model("avlp12/Inkling-975B-Alis-MLX-Dynamic-3.7bpw")
```

Sliding-window attention keeps the KV cache small, so long contexts are memory-cheap relative to dense-attention peers; the binding constraint on a 512 GB box is the 409 GiB of weights, which fit with room for activations and a long-context cache.

## Hardware

Built for **512 GB Apple Silicon** (M3 Ultra). For ≤ 320 GB machines, use the upcoming 2.7 bpw capacity build.

## Validation status

The DWQ schedule itself is complete and certified (63/63 sealed layer receipts + advanced-completion pass). The remaining project gates — two-box candidate held-out evaluation, Q6 final gates, runtime verification, and final quality validation — are running now; this card will be updated with their measurements (held-out NMSE table, perplexity harness numbers) as they land. Until then, treat quality claims as *certified-not-worse than the baseline conversion* rather than benchmarked.

## Credits

- Base model: **Thinking Machines — Inkling** (Apache-2.0).
- **MLX**: Apple `ml-explore`.
- Two-box BF16 boundary pipeline, layer-local streamed-backward DWQ, sealed evidence harness, and the MLX `inkling_mm_model` port: **Alis (avlp12)**.

## Citation

> **Alis (avlp12)** (2026). *Inkling-975B-Alis-MLX-Dynamic-3.7bpw* — 3.7 bpw certified layer-local DWQ MLX quantization of [Inkling](https://huggingface.co/thinkingmachines/Inkling).
> <https://huggingface.co/avlp12/Inkling-975B-Alis-MLX-Dynamic-3.7bpw>
