---
license: apache-2.0
base_model: Qwen/Qwen3-8B-Base
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- continued-pretraining
- korean
- ablation
- research-artifact
---

# Keural Cortex 8B — pilot run (step 954, 3B tokens)

**This is a validation artifact, not a product.** It exists to answer one
question before committing ~19 GPU-days to a full run: *does this continued-pretraining
recipe move Korean up without moving English down?* It is published for
reproducibility and internal record, not for use.

Continued pretraining (CPT) of [`Qwen/Qwen3-8B-Base`](https://huggingface.co/Qwen/Qwen3-8B-Base)
by MKD Co., Ltd. — Phase 3 ("pilot + gate") of the Keural Cortex 8B plan.

## Why a pilot run exists

The project plan describes this phase as existing to *"catch in one day what
would otherwise be discovered on day 19."* CPT on a converged base model can
quietly damage it — the wrong learning rate, a bad domain mix, or a corpus
defect will show up as English regression that no amount of later training
undoes. A 3B-token run costs ~1 day and surfaces that before the 41B-token run
starts.

## Training

| | |
|---|---|
| Steps | 954 |
| Tokens | 3.00B (954 × 3,145,728) |
| Sequence length | 4,096 |
| Global batch | 3,145,728 tokens/step |
| Hardware | 4× H200, FSDP full shard |
| Precision | bf16 params, fp32 gradient reduction |
| Peak LR | 1.0e-5, WSD (2% warmup / 88% stable / 10% decay), min ratio 0.1 |
| Optimizer | AdamW, β=(0.9, 0.95), ε=1e-8, wd=0.1, grad clip 1.0 |
| Attention | flash_attention_2 |
| Final loss | ~1.82–1.94 |

The learning rate is deliberately 1e-5, not a pretraining-scale 3e-4:
pretraining LRs destroy a converged base. This value prioritizes retention over
Korean acquisition speed.

Corpus: the same 19-source, 38.78B-token manifest as the full run (Korean,
English, code, science/math), sampled proportionally by weight — so the pilot
sees the same domain ratios, just fewer tokens.

## Evaluation — the gate result

Gate criterion: **Korean up AND English within −0.5 pt.** Evaluated with
`lm-evaluation-harness` against `Qwen3-8B-Base` under identical settings.
Both models are base models, so this is a like-for-like comparison.

### Korean

| Benchmark | Qwen3-8B-Base | Pilot | Δ |
|---|---|---|---|
| KMMLU | 53.91 | 53.94 | +0.03 |
| HaeRae | 63.06 | 63.15 | +0.09 |
| KoBEST BoolQ | 57.05 | 62.96 | **+5.91** |
| KoBEST COPA | 72.30 | 70.40 | −1.90 |
| KoBEST HellaSwag | 47.20 | 47.60 | +0.40 |
| KoBEST SentiNeg | 83.88 | 82.62 | −1.26 |
| **Mean** | | | **+0.55** |

### English

| Benchmark | Qwen3-8B-Base | Pilot | Δ |
|---|---|---|---|
| MMLU | 74.70 | 74.24 | −0.46 |
| ARC-Challenge (acc_norm) | 57.25 | 59.30 | +2.05 |
| HellaSwag (acc_norm) | 78.59 | 78.38 | −0.21 |
| WinoGrande | 72.38 | 73.48 | +1.10 |
| **Mean** | | | **+0.62** |

**Verdict: PASS.** Korean mean up, English mean up (well inside the −0.5 pt
tolerance), no single English benchmark outside it. The full 41B-token run was
launched on this basis.

## How to read these numbers honestly

The headline "+0.55 Korean" overstates what was demonstrated:

- **KMMLU (+0.03) and HaeRae (+0.09) are flat.** These are the two substantive
  Korean knowledge benchmarks, and 3B tokens moved neither.
- **The mean is carried by one task.** KoBEST BoolQ (+5.91) is binary yes/no;
  a gain of that size on a 2-class task is as consistent with calibration shift
  as with knowledge gain. Two other KoBEST tasks *regressed*.
- **So the gate proved the safe half of its question.** It showed the recipe
  does not damage the model — English held and slightly improved, which is the
  genuinely valuable finding. It did not establish that Korean capability
  improves by a useful margin. The project's own plan records this as
  *"Korean gain magnitude — direction confident, magnitude not."*

Two further caveats:

- **GSM8K is not comparable.** Base was scored on all 1,319 samples (84.69
  strict-match); the pilot was scored on a 300-sample subset (85.33) to work
  around a generation-throughput problem. Do not read a delta into that pair.
- **Benchmark decontamination has not been run.** N-gram overlap against MMLU,
  GSM8K, KMMLU, HaeRae, KoBEST and others is an outstanding item. Until it is
  done, treat every number here as internal-only and not publishable.

## What this model cannot do

It is a **base model**. `Qwen3-8B-Base` has no instruction following, no chat
format, no tool calling and no thinking mode; CPT adds none of them. It continues
text rather than answering instructions, and will ramble or repeat. The
`chat_template.jinja` is inherited from the base tokenizer and does not indicate
chat tuning.

Context length is 32,768 (native, unchanged from base).

## Relationship to other checkpoints

| Checkpoint | Tokens | Purpose |
|---|---|---|
| **this** — pilot step 954 | 3B | recipe validation (Phase 3) |
| full step 5000 | ~15.7B | main run, in progress (Phase 4) |
| full step 13034 | 41B | main run target |

The pilot is a **separate run** from the main CPT, not an early checkpoint of
it. Both start from `Qwen3-8B-Base` with the same recipe and manifest.

## License and attribution

Apache 2.0, inherited from `Qwen/Qwen3-8B-Base`. This is a derivative work of
Qwen3-8B-Base by Alibaba Cloud.

## Intended use

Internal research, reproducibility and ablation reference only. Not for
production, not for public-facing deployment, and not a basis for capability
claims.
