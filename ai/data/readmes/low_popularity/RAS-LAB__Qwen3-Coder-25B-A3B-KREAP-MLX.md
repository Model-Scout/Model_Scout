---
license: apache-2.0
base_model: Qwen/Qwen3-Coder-30B-A3B-Instruct
library_name: mlx
pipeline_tag: text-generation
language: [ko, en]
tags: [moe, pruning, reap, k-reap, mlx, korean, expert-pruning]
---

# Qwen3-Coder-25B-A3B-KREAP-MLX  (18.75% routed pruning)

Korean-preserving one-shot MoE expert pruning of [Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct), produced with [**K-REAP**](https://github.com/Chedrian07/K-REAP). Routed experts pruned **128 → 104** per layer (18.75%); ~25B total params, 3.3B active (top-8 unchanged). No fine-tuning.

Unlike vanilla REAP (English/code calibration), K-REAP detects and **hard-protects the experts that carry Korean**, so pruning preserves Korean without sacrificing English/coding. See [K-Guard-REAP](https://github.com/Chedrian07/K-Guard-REAP) for the full study.

## Korean loss minimized vs. standard REAP

The standard REAP recipe collapses Korean at comparable compression: Cerebras **Qwen3-Coder-REAP-25B** (19.5%, no language protection) drops Korean MC macro **79.3 → 56.6 (−22.7pp)** with generation collapse **115/128**. By hard-protecting the Korean expert path, **this model keeps Korean MC macro at 78.6 (−0.7pp) with 0/128 collapse**, i.e. the Korean loss is reduced to a few points or less. (K-REAP removes ~97% of REAP's Korean damage.)

## Benchmarks (vs base Qwen3-Coder-30B; Δ = base delta, %p)

### 한국어 (Korean, self-harness)

| benchmark | base | this model |
|---|---:|---:|
| KMMLU | 55.2 | 53.8 (−1.4) |
| KoBEST BoolQ | 93.6 | 92.9 (−0.7) |
| KoBEST COPA | 92.7 | 92.6 (−0.1) |
| KoBEST SentiNeg | 95.0 | 94.2 (−0.8) |
| KoBEST HellaSwag | 60.0 | 59.6 (−0.4) |
| Gen. collapse (/128, ↓) | 0 | 0 |

### English reasoning/knowledge (llm-evalbox)

| benchmark | base | this model |
|---|---:|---:|
| ARC-Challenge | 91.2 | 91.2 (±0.0) |
| HellaSwag | 84.4 | 84.0 (−0.4) |
| WinoGrande | 73.4 | 70.0 (−3.4) |
| MMLU-Pro | 50.2 | 48.6 (−1.6) |
| TruthfulQA | 71.2 | 69.8 (−1.4) |
| MMLU-en | 76.6 | 76.4 (−0.2) |

### Math

| benchmark | base | this model |
|---|---:|---:|
| GSM8K | 93.2 | 95.2 (+2.0) |
| MathQA | 55.2 | 56.0 (+0.8) |

### Coding

| benchmark | base | this model |
|---|---:|---:|
| HumanEval+ | 87.8 | 89.6 (+1.8) |
| MBPP+ | 77.2 | 74.1 (−3.1) |
| LiveCodeBench | 52.4 | 53.0 (+0.6) |

### Safety/Bias

| benchmark | base | this model |
|---|---:|---:|
| BBQ | 92.2 | 92.6 (+0.4) |
| SafetyBench | 83.2 | 81.2 (−2.0) |

### Macro

| benchmark | base | this model |
|---|---:|---:|
| Korean MC macro | 79.3 | 78.6 (−0.7) |
| Academic 10-bench macro | 74.7 | 74.2 (−0.5) |

## Usage (MLX)

```python
from mlx_lm import load, generate
model, tok = load("RAS-LAB/Qwen3-Coder-25B-A3B-KREAP-MLX")
print(generate(model, tok, prompt="한국어로 자기소개를 해줘.", max_tokens=256))
```

Standard HF safetensors (BF16) — also loadable with `transformers`. Coverage note: KoBEST & EvalPlus are full sets; KMMLU/evalbox/LiveCodeBench are deterministic subsets (seed 42). Effect sizes ≫ sampling CI. Details: K-Guard-REAP `docs/10_MASTER_RESULTS.md §7`.

## Method

REAP saliency (router gate × expert-output L2 norm, conditional mean) restricted to Korean segments + Korean↔English contrast + rare/rollout protection → hard-protected survivor set → streaming safetensors surgery (uniform experts/layer). Framework: https://github.com/Chedrian07/K-REAP