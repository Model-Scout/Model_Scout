---
language:
  - en
  - ko
license: apache-2.0
datasets:
  - roneneldan/TinyStories
library_name: transformers
pipeline_tag: text-generation
tags:
  - npu
  - rebellions
  - atom-max
  - rbln
  - npu-training
  - npu-pretraining
  - inference-accelerator
  - backpropagation
  - from-scratch
  - pretraining
  - pretrained-from-scratch
  - vkore
  - vkte
  - vidraft
  - final-bench
  - small-language-model
  - slm
  - tiny-llm
  - language-model
  - causal-lm
  - decoder-only
  - transformer
  - rope
  - swiglu
  - rmsnorm
  - gqa
  - char-level
  - tinystories
  - edge-ai
  - on-device
  - low-power
  - cost-efficient
  - blackwell-alternative
  - gpu-alternative
  - korea
  - korean-ai
  - research
  - proof-of-concept
---

# VKORE-46M-NPU

![VKORE-46M-NPU: who said I can only do inference?](cartoon.png)

> **The common wisdom was absolute: an inference only NPU cannot train. Not even LoRA fine tuning, let alone pretraining from scratch. Its architecture, people said, simply cannot run backpropagation.**
>
> **This model is the counterexample.**

A small language model pretrained entirely from scratch on an inference only NPU, using backpropagation run on the chip itself. To the best of our knowledge, this is the first publicly released model pretrained from scratch on an inference only NPU.

## One line

We ran backpropagation on a chip built only for inference (Rebellions ATOM-Max) and grew a language model from zero, with no pretrained weights.

## Highlights

- Pretrained from scratch on a Rebellions ATOM-Max NPU (32 chips) in a few hours.
- Throughput on par with a two GPU B200 run on the same model.
- Loss fell from 5.65 to 0.42, and the model generates coherent English stories.
- Achieved on a first generation inference NPU released in 2025, not the latest hardware. Newer NPUs should do even better.

## Background: why an NPU

A single server of eight Blackwell class GPUs was quoted at about 1.7 billion KRW, up from the 1.2 billion KRW range not long ago. Delivery takes 40 weeks, close to ten months. Ten months is long enough to conceive and deliver a baby. On top of that there is a monthly data center colocation fee, and power draw is high. It is hard to put to work on site.

An NPU is cheaper, draws far less power, is easy to source, and can sit in an office. The chip used here is a first generation inference NPU released in 2025, not the newest silicon. The industry assumption, however, was clear. "An NPU only does inference. Its architecture cannot handle backpropagation, so training is impossible."

This model overturns that assumption. We performed backpropagation on an inference only NPU and pretrained a language model from zero.

## What is first here

- NPU driven training: forward and backward (gradient) computation were performed on an inference only NPU.
- Backpropagation succeeded: gradient descent training actually ran on an inference accelerator.
- From scratch: training started from random initialization, with no pretrained weights.
- No known precedent: we did not find a comparable case in public literature.

## Model specification

| Item | Value |
|---|---|
| Parameters | 45.8M |
| Architecture | Decoder only Transformer (RoPE, RMSNorm, SwiGLU, GQA) |
| Layers | 12 |
| Hidden width | 512 |
| Heads | 8 (KV 2) |
| Vocabulary | 256 (character level) |
| Context length | 256 |
| Training data | TinyStories (public dataset) |
| Final loss | 5.65 to 0.42 (cross entropy, training) |
| Held out loss | 0.70 (TinyStories v1 validation, not used in training) |

## Training data

- Dataset: [roneneldan/TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories) (public)
- Split used: TinyStoriesV2-GPT4 validation split
- Tokenization: character (byte) level, vocabulary 256
- Scale: about 22.5 million tokens (5,493 blocks at context 256)
- Preprocessing: used as is, with no extra processing. The training data is fully public, so anyone can reproduce training on the same data.

## Training setup

- Hardware: Rebellions ATOM-Max NPU, 32 chips (an inference only accelerator)
- Reference: a B200 GPU run with the same initialization, data and learning rate schedule. Throughput was comparable (NPU 32 chips about 260K tok/s, B200 two GPUs about 275K tok/s). The two runs used different synchronization, see below.
- The core technique that enables backpropagation based training on an inference only NPU was developed in house and is under patent application.
- The specific from scratch training method on the NPU will be disclosed in a forthcoming paper.

## Generation example

Prompt: `Once upon a time`

Output:

> Once upon a time, there was a little boy named Tim. Tim loved to play with his toy car. One day, he saw a big box in his room. Tim was very curious about the box.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("FINAL-Bench/VKORE-46M-NPU")
prompt = "Once upon a time"
ids = torch.tensor([list(prompt.encode("utf-8"))])   # byte level: token id = byte value
out = model.generate(ids, max_new_tokens=200, do_sample=False)
print(bytes(out[0].tolist()).decode("utf-8", errors="replace"))
```

A character level tokenizer is used (byte values 0 to 255), so no tokenizer file is needed. The original training format is also included as `tiny_ckpt.pt`.

## Numerical fidelity (per step)

The right way to test whether the NPU backward does the same work as a GPU is at the gradient level, not at the loss curve. We measured it directly on this 46M model, single chip, no sync, same seed and batch: the NPU computed gradients match an autograd reference at a per layer cosine of 0.99986 on average (min 0.99972, max 0.99996). As a correctness check of the hand written backward itself, it matches PyTorch autograd to a worst case relative gradient error of 8.96e-7 on the full model. These are measured on this model under these conditions.

A second check on the same model covers all 110 parameter tensors on a real TinyStories batch against CPU fp32 autograd: relative L2 error median 0.96%, worst 2.21%. A CPU bf16 autograd control on the same batch gives 1.67% and 3.42%. The NPU gradient is closer to fp32 than the bf16 control on every tensor. Per-tensor numbers: `gradcheck_46M_1chip.json`.

## NPU vs B200 (loss curve, secondary)

As a secondary check, the 32 chip run and a B200 GPU run under identical init, data, and schedule start from the same loss (5.65 vs 5.62) and both fall steadily, but they do not share the same learning dynamics: the gap grows to 0.42 vs 0.25 at step 2950 (single-batch training losses). A high correlation between two falling loss curves is weak on its own, so we do not lead with it. The 32 chip run averaged parameters every 8 steps (DiLoCo style); the B200 run synchronized gradients every step. A controlled GPU re-run that separates the effect of the sync scheme is in progress. Per step numerical fidelity (above) and multi chip convergence are separate properties. See `comparison_NPU_vs_B200_ko.md` for the full data.

## Scope

This is a small research demonstration model. It is suited to generating short English stories at the TinyStories level.

## Credits

VIDRAFT. Part of the VKORE project (NPU acceleration family). Published under FINAL-Bench.
