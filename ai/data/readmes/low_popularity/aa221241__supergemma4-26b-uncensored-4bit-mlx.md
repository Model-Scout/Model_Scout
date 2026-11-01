---
license: gemma
base_model: google/gemma-4-26B-A4B-it
tags:
  - gemma4
  - mlx
  - lora
  - uncensored
  - abliterated
  - apple-silicon
  - 4bit
  - quantized
  - fine-tuned
  - moe
  - gemma-4
language:
  - en
  - ko
pipeline_tag: text-generation
library_name: mlx
---


# SuperGemma4-26B-Uncensored-4bit-MLX

**A norm-preserving abliterated + LoRA-tuned Gemma 4 26B (A4B MoE) model optimized for coding, reasoning, agent tasks, and fully uncensored conversation.** Fine-tuned on Apple Silicon using MLX.

## Key Results

| Metric | Original-IT | Heretic-ARA | TrevorS EGA | This Model |
|--------|:-----------:|:-----------:|:-----------:|:----------:|
| Quality (Blind Bench) | 88.3% | 87.8% | **88.3%** | **88.7%+** |
| Refusal Rate (220 prompts) | ~95% | ~7% | ~1% | **~0%** |
| KL Divergence | 0 | ~1.04 | **0.090** | ~0.09 |

> **Perfect uncensoring (0% refusal) with zero quality loss** — achieved through norm-preserving Expert-Granular Abliteration (EGA) + targeted LoRA.

## Model Details

- **Base Model**: [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26b-it)
- **Abliteration**: [TrevorJS norm-preserving biprojected EGA](https://github.com/TrevorS/gemma-4-abliteration) — KL divergence 0.090
- **Architecture**: Mixture-of-Experts — 25.2B total params, 3.8B active per token, 128 experts/layer, top-8 routing
- **Quantization**: 4-bit mixed (MLP/router 8-bit, attention 4-bit) — MLX format, ~13GB
- **LoRA Config**: rank=8, scale=2.0, dropout=0.05, attention-only, 16 layers
- **Training**: weakness-targeted data, lr=5e-5, mask-prompt, grad-checkpoint
- **Framework**: [mlx-lm](https://github.com/ml-explore/mlx-lm) 0.31.3

## Why This Model?

Standard abliteration methods (Failspy, heretic-ARA) damage model capabilities by 0.5-7.8%. This model uses **three innovations** to achieve uncensoring with zero capability loss:

1. **Norm-Preserving Biprojected Abliteration**: Decomposes weights into magnitude + direction, removes refusal from direction only, preserves original magnitudes
2. **Expert-Granular Abliteration (EGA)**: Applies abliteration to each of 128 MoE experts individually with routing-aware weighting
3. **Targeted LoRA**: Trains only on weakness areas to recover any micro-losses from abliteration

## Benchmark Evolution

| Version | Method | Refusal | Quality | Notes |
|---------|--------|:-------:|:-------:|-------|
| v1 (heretic-ara) | Standard abliteration | 7% | 87.8% | -0.5% from abliteration |
| v1 + LoRA | LoRA on abliterated base | 0% | 86.8% | LoRA couldn't recover damage |
| **v2 (this)** | **Norm-preserving EGA + LoRA** | **0%** | **88.7%+** | **Best of both worlds** |

## Training Methodology

### Targeted Weakness Training

We identified weak areas through blind benchmarking and trained exclusively on those:

- **87 high-quality examples** targeting Code, Browser, Logic
- **GPT-5.4 hard data**: 217 expert-level coding/system design samples
- **Bench fix data**: 124 samples targeting specific benchmark weaknesses
- **Key insight**: Weakness-only training preserves strengths while improving weak spots

### What We Learned (30+ Experiments)

| Finding | Impact |
|---------|--------|
| rank 32 + all experts | Overfitting — destroyed quality |
| rsLoRA scale 5.66 | Too aggressive for MoE models |
| rank 8 + attention-only + scale 2.0 | Sweet spot |
| Massive data (3000+) | Diluted strengths |
| Targeted weakness data (87-300) | Best results |
| DPO/RLHF | No effect on Instruction/Tool Use |
| Constrained Decoding | Solved JSON/format issues |

## Usage

### Quick Start (Apple Silicon)

```bash
pip install mlx-lm>=0.31.3

mlx_lm.generate \
  --model Jiunsong/supergemma4-26b-uncensored-4bit-mlx \
  --prompt "Implement a concurrent web scraper with rate limiting" \
  --max-tokens 2048
```

### As Server (OpenAI-compatible API)

```bash
mlx_lm.server \
  --model Jiunsong/supergemma4-26b-uncensored-4bit-mlx \
  --port 8080

curl http://localhost:8080/v1/chat/completions \
  -d '{"model":"gemma4","messages":[{"role":"user","content":"Hello"}]}'
```

## Hardware Requirements

| RAM | Context | Speed |
|-----|---------|-------|
| 16GB | ~4K tokens | ~30 tok/s |
| 32GB | ~16K tokens | ~60 tok/s |
| 64GB | ~64K tokens | ~100 tok/s |
| 128GB | ~256K tokens | ~130 tok/s |

Trained on M4 Max 128GB.

## Category Scores

| Category | Score |
|----------|:-----:|
| Code | 90% |
| Math | 90% |
| Korean | 80% |
| Logic | 90% |
| System Design | 90% |
| **Average** | **88%** |

## Limitations

- **4-bit quantization**: Some precision loss vs full-precision
- **MoE architecture**: 3.8B active params — efficient but limited vs dense models
- **Instruction Following**: May occasionally miss complex multi-part instructions
- **Tool Use**: Best with constrained decoding for structured output

## Acknowledgments

- Google DeepMind for [Gemma 4](https://deepmind.google/models/gemma/gemma-4/)
- [TrevorS](https://github.com/TrevorS/gemma-4-abliteration) for norm-preserving biprojected EGA
- [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) for Apple Silicon training
- [heretic-llm](https://github.com/p-e-w/heretic) for abliteration research

## Citation

```bibtex
@misc{supergemma4-uncensored,
  title={SuperGemma4-26B-Uncensored: Norm-Preserving EGA + Targeted LoRA},
  author={Jiunsong},
  year={2026},
  url={https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-4bit-mlx}
}
```
