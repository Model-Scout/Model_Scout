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
- intermediate-checkpoint
---

# Keural Cortex 8B — intermediate checkpoint (step 10,000)

**An intermediate checkpoint published for research and reproducibility, not for
use.** For the completed model see
[`Keural-Cortex-8B-Base`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-Base).

Korean-focused continued pretraining (CPT) of
[`Qwen/Qwen3-8B-Base`](https://huggingface.co/Qwen/Qwen3-8B-Base), by
**MKD Co., Ltd.**

| | |
|---|---|
| Progress | **step 10,000 / 13,034 (76.7%)** |
| Tokens seen | **31,457,280,000 (31.46 B)** of 41.00 B |
| LR at this step | 1.0e-05 (WSD stable phase) |
| Context length | 32,768 (native) |
| Exported | 2026-09-05 |

## Why this checkpoint is published

Training loss in this run plateaued at ≈1.818 from roughly **step 5,200**
(16.4 B tokens) and did not improve materially through to step 13,034 — the WSD
decay phase contributed +0.0007. Whether downstream *capability* continued
improving after that plateau is an open question, and answering it requires
comparing checkpoints from across the run.

This checkpoint exists so that comparison is possible. Alongside
[`step5000`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-step5000)
(15.73 B tokens, 38%) and the
[final model](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-Base)
(41.00 B, 100%), it gives three points spanning the plateau — one before it, two
after — on an otherwise identical run.

## ⚠️ Limitations

- **Base model.** No instruction following, no chat format, no tool calling, no
  thinking mode. It continues text rather than answering instructions.
  Post-training has not been performed. The bundled `chat_template.jinja` is
  inherited from the base tokenizer and does **not** indicate chat tuning.
- **Not evaluated.** No benchmark numbers exist for this checkpoint.
- **Decontamination outstanding.** N-gram overlap against the evaluation suites
  has not been checked.
- **Mid-training.** The learning rate had not yet decayed at this point, so this
  is not a "finished" model in any sense — the final checkpoint saw a full decay
  to 1.0e-06.

## Training configuration

Identical to the final checkpoint: sequence length 4,096, global batch 3,145,728
tokens/step, peak LR 1.0e-05 on a WSD schedule, AdamW (β 0.9/0.95, wd 0.1), grad
clip 1.0, FSDP full shard on 4 × H200, bf16 with fp32 gradient reduction,
FlashAttention-2, activation checkpointing.

Corpus: 38.784 B tokens across 19 sources — 42.45% Korean, 29.71% English/other,
15.19% code, 12.66% science/math. NamuWiki, Falcon-RefinedWeb and arXiv were
excluded on licensing grounds.

Full details, including the loss analysis referenced above:
[github.com/MKD-CORP/Keural-Cortex-8B](https://github.com/MKD-CORP/Keural-Cortex-8B)
under `CPT_details/`.

## License

**Apache 2.0**, inherited from `Qwen/Qwen3-8B-Base`. Derivative work of
Qwen3-8B-Base by Alibaba Cloud; attribution required.

## Intended use

Research and checkpoint comparison only. Not for production or user-facing
deployment.
