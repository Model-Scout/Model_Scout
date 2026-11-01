---
license: apache-2.0
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
tags:
- mlx
- optiq
library_name: mlx
pipeline_tag: text-generation
base_model: mistralai/Mistral-Small-4-119B-2603
base_model_relation: quantized
---

# Mistral-Small-4-119B-2603-OptiQ-2bit

> **Built with [mlx-optiq](https://mlx-optiq.com)**, the MLX-native toolkit to quantize, fine-tune, and serve LLMs locally on Apple Silicon (no PyTorch, no cloud). [Try the Lab](https://mlx-optiq.com/docs/lab/) · [All OptiQ quants](https://mlx-optiq.com/models) · [Docs](https://mlx-optiq.com/docs/)
>
> **Supported loaders:** [mlx-optiq](https://mlx-optiq.com) (text, vision, and MTP) and stock [mlx-lm](https://github.com/ml-explore/mlx-lm) (text). Other front-ends load MLX weights through their own stack, so support there depends on that stack rather than on these files.

An [OptiQ](https://mlx-optiq.com) mixed-precision MLX quant of **Mistral-Small-4-119B-2603**, a 128-routed-expert sparse-MoE flagship. This is an extreme 2-bit build meant to run a 119B model on a 36 GB Mac.

- **Mixed 2/4-bit `static` build** — per-layer bit-widths assigned to a 2.5 target bits-per-weight: 352 projections at 4-bit, 82 at 2-bit.
- **239 GB bf16 to 43 GB on disk** (5.6x).
- **Runs on a 36 GB Mac.** OptiQ streams the routed experts off SSD on demand, so the resident footprint is ~9-12 GB while the full model never materializes.

## Requirements

Needs `optiq >= 0.4.4`, which ships the vendored `mistral4` decoder (the 128-expert MoE with MLA attention). Stock `mlx-lm` and older OptiQ load the base repo's `mistral3` wrapper, which falls back to `llama` and drops every expert. Do not load this repo that way.

```bash
pip install -U optiq
```

## Running it

This is a large sparse MoE, so serve it with SSD expert streaming (auto-detected):

```bash
optiq serve --model mlx-community/Mistral-Small-4-119B-2603-OptiQ-2bit
```

`optiq serve` installs the `mistral4` decoder, detects the streamable MoE, and loads it via `optiq.runtime.moe_stream` so the routed experts are read from disk per token instead of held in RAM. Use the OpenAI-compatible endpoint at `http://localhost:8000/v1`.

## No Capability Score by design

Extreme 2-bit quants of 100B+ models ship with a coherence demo instead of a benchmark suite. At 2-bit, this quant writes a complete, self-contained Flappy Bird that actually plays:

![Flappy Bird, written by this 2-bit quant](flappy_119b.gif)
