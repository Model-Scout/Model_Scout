---
license: apache-2.0
language:
  - en
  - ko
pipeline_tag: text-generation
library_name: transformers
tags:
  - aether
  - open-weights
  - heterogeneous-attention
  - mixture-of-experts
  - mamba2
  - state-space-model
  - hyena
  - mla
  - korean
  - vidraft
---

# Aether-6B-11Attn

> ⚠️ **Pretraining is still in progress.** This repository currently holds a mid-training checkpoint (step 174,000); it will be updated with the final weights as soon as training completes. The `-base` suffix denotes "no instruction tuning" — an `-it` variant will follow once pretraining is finished.


<!-- AETHER-FAMILY-LINKS -->

**Aether family** — [![5Attn Base](https://img.shields.io/badge/%F0%9F%A7%AC_Aether--7B--5Attn-Fully_Open-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) [![5Attn IT](https://img.shields.io/badge/%F0%9F%92%AC_Aether--7B--5Attn--it-Instruct-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) [![7Attn Base](https://img.shields.io/badge/%F0%9F%A7%A9_Aether--7B--7Attn--base-Open_Weights-teal)](https://huggingface.co/FINAL-Bench/Aether-7B-7Attn-base) [![Checkpoints](https://img.shields.io/badge/%F0%9F%97%82%EF%B8%8F_Checkpoints-Intermediate-lightgrey)](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints) [![Demo](https://img.shields.io/badge/%F0%9F%9A%80_Demo-Aether_Sovereign_AI-orange)](https://huggingface.co/spaces/FINAL-Bench/Aether-Sovereign-AI) [![Blog](https://img.shields.io/badge/%F0%9F%93%9D_Blog-Open_Source_LLM-yellow)](https://huggingface.co/blog/FINAL-Bench/opensource-llm) [![Collection](https://img.shields.io/badge/%F0%9F%93%9A_Collection-Aether_Foundation-blue)](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)

<!-- /AETHER-FAMILY-LINKS -->

### Which Aether model should I use?

| Model | What it is | Pick it if |
|---|---|---|
| [**Aether-7B-5Attn**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) | 6.59B MoE base. **Fully open** - weights + data recipe + training code + all 162k-step logs + checkpoints | You want to audit, verify or rebuild a foundation model end to end |
| [**Aether-7B-5Attn-it**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) | The same model, instruction-tuned | You want it to answer rather than continue text |
| [**AETHER-7B-7Attn-base**](https://huggingface.co/FINAL-Bench/AETHER-7B-7Attn-base) | Same 49-layer architecture, a different checkpoint. Open weights | You want a second run of this architecture to compare against |
| [**Aether-6B-11Attn-base**](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn-base) | 121 layers, **11 sequence-mixing mechanisms** in one network - attention, Mamba-2, Hyena, GDN, MLA - on an 11x11 Latin square | You research heterogeneous sequence mixing. It is a mid-training research artifact |

All four load the same way:

```python
AutoModelForCausalLM.from_pretrained(MODEL, trust_remote_code=True, dtype=torch.bfloat16)
```


<!-- LATIN-MAP -->

### Layer map — 11x11 Latin square

Eleven sequence-mixing mechanisms across 121 layers, each appearing **exactly once per row and per column**. Colour marks the family: attention (blue), linear (teal), state-space/Mamba2 (orange), convolutional/Hyena (purple) — the non-attention families are what make this heterogeneous rather than a variant sweep.

![Latin square layer map](latin_11x11.png)

<!-- /LATIN-MAP -->

**A 121-layer network that places 11 different sequence-mixing mechanisms on an 11x11 Latin square.**

To our knowledge, this is the first model to integrate **11 heterogeneous sequence-mixing mechanisms** — attention, state-space, convolutional and linear families — inside a single network. Existing hybrids combine two or three (e.g. Mamba + Transformer).

> **Release scope: open weights.** This repository ships the weights plus the minimum code needed to load them. Unlike [Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) — which is fully open (data recipe, training code, logs, checkpoints) — the training data recipe, training code, logs and intermediate checkpoints for this model are **not** released.

## The 11 mechanisms

121 layers = 11 x 11. Each mechanism occupies **exactly 11 layers**, one per row and column of the Latin square, so no mechanism concentrates at any depth.

| # | Mechanism | Family | Distinctive parameters (verifiable in the weights) |
|---|-----------|--------|---------------------------------------------------|
| 0 | `nsa` | sparse attention | `compress_mlp`, `gate_logit`, `select_score` |
| 1 | `differential` | attention | `lambda_q1/k1/q2/k2`, `subln` |
| 2 | `full` | attention | `q/k/v/o_proj` |
| 3 | `mla` | latent attention | `kv_a_proj`, `kv_b_proj`, `q_a_proj`, `q_b_proj` |
| 4 | `sliding` | attention | windowed masking over the full path |
| 5 | `compress` | attention | `full_attn.*` submodule |
| 6 | `hybrid` | attention | `nsa.*` + `diff.*` + `gate` + `merge_norm` |
| 7 | `linear` | linear attention | `gate`, `norm` |
| 8 | `mamba2` | **state-space** | `A_log`, `D`, `conv1d`, `dt_proj`, `B_proj`, `C_proj` |
| 9 | `gdn` | gated delta net | `conv1d_q`, `conv1d_k`, `gate_proj` |
| 10 | `hyena` | **convolutional** | `filter_dense` (implicit filter) |

*Precision matters here: `full` and `sliding` share the same parameters (sliding is masking over the full path), so the weights show **10 distinct parameter signatures for 11 labels**. And several of these are not "attention" in the strict sense — `mamba2`, `hyena`, `gdn` and `linear` are other sequence-mixing families, which is exactly the point of the experiment.*

## Specifications

| | |
|---|---|
| Parameters | 5.79B total (MoE) |
| Layers | 121 (11 x 11 Latin square) |
| Hidden size | 1024 |
| Attention heads | 8 query / 2 key-value (GQA), head dim 128 |
| Experts | 25 routed (top-7) + 1 shared |
| Vocabulary | 151,936 |
| Precision | bfloat16 |
| Checkpoint | training step 174,000 |
| License | Apache-2.0 |

## Provenance and honest caveats

This model was reconstructed from a sharded FSDP training checkpoint. **The exact training code was not archived**, so the architecture code shipped here was rebuilt and then validated two ways:

1. **Exact parameter match** — all 11,047 checkpoint tensors load with **0 missing / 0 unexpected** keys, and the parameter count matches the checkpoint exactly (5.7885B).
2. **Perplexity** — the loaded model predicts real text sensibly (PPL 11.8 English / 6.5 Korean on sample sentences). A mis-reconstructed architecture would produce perplexity orders of magnitude worse.

Treat this as a **research artifact**, not a polished product: it is a mid-training checkpoint of an architecture experiment, with no instruction tuning.

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "FINAL-Bench/Aether-6B-11Attn-base"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda"
).eval()
```

`trust_remote_code=True` is required — this is a custom architecture (`aether_v2_11attn`)
and the modeling code ships in this repository.

> **Run at batch_size = 1** (the NSA branches do not consume a padding mask), and run the forward under `torch.autocast(dtype=torch.bfloat16)` — several branches create fp32 intermediates.

> Greedy decoding degenerates into repetition (expected for an un-tuned base checkpoint) — use sampling with a repetition penalty. Generation is ~10 s/token: 121 layers with no KV cache. This is a research artifact, not a serving build.

## Related

- **Fully-open sibling:** [Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) (weights + data recipe + training code + logs + checkpoints)
- **Collection:** [Aether Foundation Model](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)

*Built by VIDRAFT. License: Apache-2.0*
