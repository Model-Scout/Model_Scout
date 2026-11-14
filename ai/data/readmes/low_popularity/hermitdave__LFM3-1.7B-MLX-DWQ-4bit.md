---
base_model: LiquidAI/LFM3-1.7B
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
tags:
- mlx
- mlx-lm
- quantization
- dwq
- lfm3
- apple-silicon
- 4-bit
- text-generation
---

# LFM3-1.7B — MLX 4-bit DWQ

> **Provenance, up front.** The bit allocation and the **integer weights** in
> this model are Liquid AI's, from
> [LiquidAI/LFM3-1.7B-MLX-4bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-4bit).
> DWQ was applied on top by us, and it refines **only the per-group scales and
> biases** — the quantized integers are untouched. This is a derivative of
> their quantization, not an independent one.

LFM3-1.7B is a 1.7B-parameter hybrid model (alternating short-convolution,
full-attention and sliding-attention blocks, 24 layers, 128k vocab) from
Liquid AI. This repo is their official 4-bit MLX quant with distillation-
weighted quantization applied on top.

## Results

Measured on held-out text (32 sequences × 1024 tokens from FineWeb-Edu,
never used in calibration), against the BF16 original:

| Model | Perplexity ↓ | KL vs BF16 ↓ | top-1 agreement ↑ |
|---|---|---|---|
| BF16 teacher (reference) | 23.61 | — | — |
| Liquid AI 4-bit RTN | 27.35 | 0.1946 | 76.81% |
| DWQ, epoch 1 | 22.67 | 0.1424 | 80.50% |
| **DWQ, epoch 2 — this model** | **22.91** | **0.1181** | **81.94%** |

Lower KL and higher top-1 mean the quantized model stays closer to the BF16
reference.

### What the gain actually is

| Metric | RTN | DWQ (epoch 2) | Delta |
|---|---|---|---|
| KL vs BF16 | 0.1946 | 0.1181 | −39% |
| top-1 agreement | 76.81% | 81.94% | +5.13 pts |
| Perplexity | 27.35 | 22.91 | −16% |

**Be clear about the magnitude.** The KL improvement is the largest relative
gap. On the metric that maps to behaviour — how often a decisive token is
predicted differently from the teacher — the remaining disagreements are
mostly near-tie positions where the teacher's own distribution is nearly
flat. Between epoch 1 and epoch 2, KL improved a further 17% and top-1
agreement rose 1.4 points, while ground-truth perplexity ticked up ~1%:
the student is tracking the teacher's distribution more faithfully, and
where the teacher itself disagrees with ground truth that shows up as
higher perplexity. If you optimise purely for ground-truth perplexity on
this distribution, epoch 1 is marginally better; epoch 2 is the better
match to the model's own behaviour.

## Method

DWQ (distillation-weighted quantization) treats the quantization grid —
per-group scales and biases — as free parameters and fits them by gradient
descent against a higher-precision teacher's output distribution (a KL
loss over the teacher's top-1024 logits, temperature 2.0). The quantized
integer weights never change; only the grid moves. RTN (round-to-nearest)
leaves the grid at its analytic default.

Setup for this model:

- **Student:** [LiquidAI/LFM3-1.7B-MLX-4bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-4bit) —
  4-bit, group size 64, affine.
- **Teacher:** Liquid AI's BF16 original (`LiquidAI/LFM3-1.7B`).
- **Calibration:** FineWeb-Edu, LFM3-tokenized. Epoch 1: 512 samples (480
  train / 32 valid), sequence length 1024. Epoch 2: continuation from the
  epoch-1 checkpoint, 1,056 samples (1,024 train / 32 valid), sequence
  length 2048. Held-out evaluation on 32 fresh sequences.
- **Optimizer:** Adam. Epoch 1: lr 1e-6, batch size 4, 120 steps.
  Epoch 2: lr 5e-7 (continuation), batch size 4, 256 steps.

### Quantization details

- 4-bit, group size **64**, mode **affine** (inherited from the Liquid AI
  allocation)
- Trainable surface during DWQ: the per-group scales and biases only —
  3.147% of parameters (54.4M of 1,728.8M)
- Weights: 973 MB, single safetensors shard (unchanged from the RTN source)

## Usage

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("hermitdave/LFM3-1.7B-MLX-DWQ-4bit")

messages = [{"role": "user", "content": "What is the capital of Australia?"}]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=256,
               sampler=make_sampler(temp=0.1, top_k=50)))
```

Recommended generation settings from the upstream card: `temperature 0.1`,
`top_k 50`, `repetition_penalty 1.1`. For math and science, use
`temperature 1.0, top_p 0.95, top_k 20, repetition_penalty 1.0`.

## Limitations

- **Not a fine-tune.** A lossy compression of the upstream model. For
  knowledge-heavy work, pair it with retrieval.
- **Derivative artifact.** The integer weights are Liquid AI's; see the note
  at the top. Credit and licensing obligations follow the upstream model
  and quant.
- **Not evaluated on task benchmarks.** The numbers here are perplexity and
  teacher-agreement, not task accuracy. No claim is made about downstream
  agent or tool-use performance.
- **Marginal gain over epoch 1.** The second DWQ epoch is a small step —
  see "What the gain actually is" above.

## Attribution

- **Base model:** [Liquid AI](https://huggingface.co/LiquidAI/LFM3-1.7B) —
  LFM3-1.7B, LFM Open License v1.0.
- **Bit allocation and integer weights:**
  [LiquidAI/LFM3-1.7B-MLX-4bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-4bit)
  by Liquid AI.
- **DWQ refinement, pipeline, benchmarking and this card:** Hermes Agent
  (Nous Research).

See the upstream model card for training details, evaluation and licensing.
