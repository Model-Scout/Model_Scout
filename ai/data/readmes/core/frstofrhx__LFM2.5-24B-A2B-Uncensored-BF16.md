---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-24B-A2B
base_model_relation: finetune
pipeline_tag: text-generation
library_name: transformers
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
- vi
- th
- id
- hi
- ru
- pl
tags:
- liquid
- lfm2.5
- moe
- uncensored
- abliterated
- refusal-direction
- agentic
- tool-calling
---

# LFM2.5-24B-A2B-Uncensored-BF16 (AtomicChat recipe, trainable)

Trainable (safetensors BF16) refusal-ablated version of
[LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B), produced by
replicating the published AtomicChat refusal-direction edit on the original BF16 weights.

Unlike Heretic-style ablations (attention-only), this edit also removes the refusal
direction from the **down-projections of all 64 experts in blocks 14-39** — where most of
the refusal behavior of this model lives.

## Method (replicated from public AtomicChat metrics)

- Directions: `enru` per-layer refusal directions from
  [AtomicChat/LFM2.5-24B-A2B-Uncensored-GGUF-metrics](https://huggingface.co/datasets/AtomicChat/LFM2.5-24B-A2B-Uncensored-GGUF-metrics)
  (`ablit/dirs/directions.npz`), difference of means of the residual stream at the last
  prompt token (544 harmful vs 544 harmless), projected against the harmless mean,
  unit-normalized.
- Edit: `W' = W - 1.75 * d * (W^T d)^T` for block b in 14..39 using direction
  `enru[b+1]`, applied in f32 and rounded once to BF16 (same as the original bake).
- Tensors edited: `self_attn.out_proj` (attention blocks) / `conv.out_proj` (conv blocks)
  and `feed_forward.experts.{0..63}.w2` — 1690 tensors total.
- Validated against the published rank-1 adapter: projection ratio 0.75 on every tensor
  (exact), cos(v, adapter) = 1.0 on mixers, and expert vectors match as a permutation
  (GGUF vs HF expert ordering).

## Verification (Mac M5 Pro, MLX 4-bit, thinking closed)

| Metric | Original | This model |
|---|---|---|
| Refusals (mlabonne/harmful_behaviors, 40) | 39/40 (97.5%) | **1/40 (2.5%)** |
| Tool calls valid (3/3) | 3/3 | 3/3 |
| KL vs original (neutral text, last-token logits) | — | 0.11 |
| MMLU (100-question sample, 0-shot, thinking closed) | 57% | 58% |

Reference (AtomicChat BF16 edit): refusals 96.3% -> 1.2%, MMLU 64.40 -> 65.55, KL 0.204.

## Usage

Same as the original model (transformers >= 5.3.0, vLLM, SGLang, mlx-lm with
`lfm2_moe`). Liquid AI recommends `temperature 0.1`, `top_k 50`, `repetition_penalty 1.05`.
The model always thinks before answering; allow a generous output budget.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("frstofrhx/LFM2.5-24B-A2B-Uncensored-BF16", dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained("frstofrhx/LFM2.5-24B-A2B-Uncensored-BF16")
```

## Intended use

Research and personal use, including safety research, alignment studies and red-teaming.
This is a **trainable base**: fine-tune it with your own data (e.g. cyber/terminal SFT)
to build a domain-specialized uncensored agent.

## License & credits

Derivative of `LiquidAI/LFM2.5-24B-A2B` under the **LFM Open License v1.0** (see
`LICENSE`). All rights to the base model remain with Liquid AI. Method and directions by
AtomicChat (public metrics dataset).

## Warning

This model has had its refusal behavior substantially reduced. It may produce harmful,
inaccurate, biased or offensive content. All outputs should be treated as untrusted and
independently verified. You are responsible for how you use it and for complying with
applicable laws and the base model license.