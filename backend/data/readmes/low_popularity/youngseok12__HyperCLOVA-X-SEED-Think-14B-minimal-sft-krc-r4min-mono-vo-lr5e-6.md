---
language:
- ko
pipeline_tag: text-generation
tags:
- korean
- causal-lm
- lora
- hyperclovax
---

# HyperCLOVA-X-SEED-Think-14B Minimal SFT KRC MONO v/o LoRA

This is a merged Korean causal-language-model checkpoint trained for the KDS task. It is derived from the local `hcx_minimal_sft_71875` checkpoint, whose upstream base is HyperCLOVA-X-SEED-Think-14B.

## Training

- Starting checkpoint: `models/hcx_minimal_sft_71875`
- Training data: 836 fixed K/R/C success-consolidation MONO examples (`MONO_train.jsonl`, SHA-256 `f5c98fc8366ca99c4d83fa723a521108fa1d266a9a8b15c66b404da545e42023`)
- Method: LoRA merged into the base checkpoint
- LoRA configuration: rank 4, alpha 8, dropout 0.05; target modules `v_proj` and `o_proj`
- Learning rate: 5e-6, cosine schedule, warmup ratio 0.03
- One epoch, effective batch size 16 (per-device batch size 4, gradient accumulation 4), BF16
- Trainable parameters: 2,957,312

The data was reused as the existing 836-example consolidated set; K/R/C was not re-solved or re-sampled for this run.

## Run and validation

- Run ID: `TRAIN-20260908-HCX-MINIMAL-SFT-KRC-MONO-VO-LR5E-6-GPU0`
- Final training loss: `0.5008622160497701`
- Training completed: 2026-09-08 16:28:18 UTC
- Merge completed on a single GPU: 2026-09-08 16:31:27 UTC
- The merged checkpoint contains 16 BF16 SafeTensors shards (about 27.47 GiB).
- Adapter and merged-checkpoint NaN/Inf checks passed.
- Generation smoke tests passed for arithmetic and Korean social-situation prompts. The chat template is unchanged from the training base.

Local benchmark and K-AI leaderboard evaluation were not run for this checkpoint. The loss and smoke-test results should not be interpreted as a leaderboard score.

## Usage

Use this model with a recent `transformers` release and the included tokenizer and chat template. It is a merged model checkpoint, so no separate PEFT adapter is required.

## License and notices

Refer to the bundled `LICENSE` and `NOTICE` files. Use is subject to the applicable license and terms for the upstream model.
