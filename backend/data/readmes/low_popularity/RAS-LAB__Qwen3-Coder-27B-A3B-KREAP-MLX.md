---
license: apache-2.0
base_model: Qwen/Qwen3-Coder-30B-A3B-Instruct
library_name: mlx
pipeline_tag: text-generation
language: [ko, en]
tags: [moe, pruning, reap, k-reap, mlx, korean, expert-pruning]
---

# Qwen3-Coder-27B-A3B-KREAP-MLX  (12.5% routed pruning)

Korean-preserving one-shot MoE expert pruning of [Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct), produced with [**K-REAP**](https://github.com/Chedrian07/K-REAP). Routed experts pruned **128 → 112** per layer (12.5%); ~27B total params, 3.3B active (top-8 unchanged). No fine-tuning.

Unlike vanilla REAP (English/code calibration), K-REAP detects and **hard-protects the experts that carry Korean**, so pruning preserves Korean without sacrificing English/coding. See [K-Guard-REAP](https://github.com/Chedrian07/K-Guard-REAP) for the full study.

## Korean loss minimized vs. standard REAP

The standard REAP recipe collapses Korean at comparable compression: Cerebras **Qwen3-Coder-REAP-25B** (19.5%, no language protection) drops Korean MC macro **79.3 → 56.6 (−22.7pp)** with generation collapse **115/128**. By hard-protecting the Korean expert path, **this model keeps Korean MC macro at 78.7 (−0.6pp) with 0/128 collapse**, i.e. the Korean loss is reduced to a few points or less. (K-REAP removes ~97% of REAP's Korean damage.)

## Benchmarks (vs base Qwen3-Coder-30B; Δ = base delta, %p)

### 한국어 (Korean, self-harness)

| benchmark | base | this model |
|---|---:|---:|
| KMMLU | 55.2 | 54.9 (−0.3) |
| KoBEST BoolQ | 93.6 | 92.4 (−1.2) |
| KoBEST COPA | 92.7 | 91.6 (−1.1) |
| KoBEST SentiNeg | 95.0 | 94.2 (−0.8) |
| KoBEST HellaSwag | 60.0 | 60.2 (+0.2) |
| Gen. collapse (/128, ↓) | 0 | 0 |

### English reasoning/knowledge (llm-evalbox)

| benchmark | base | this model |
|---|---:|---:|
| ARC-Challenge | 91.2 | 90.6 (−0.6) |
| HellaSwag | 84.4 | 86.4 (+2.0) |
| WinoGrande | 73.4 | 71.0 (−2.4) |
| MMLU-Pro | 50.2 | 49.8 (−0.4) |
| TruthfulQA | 71.2 | 72.4 (+1.2) |
| MMLU-en | 76.6 | 75.0 (−1.6) |

### Math

| benchmark | base | this model |
|---|---:|---:|
| GSM8K | 93.2 | 93.8 (+0.6) |
| MathQA | 55.2 | 61.2 (+6.0) |

### Coding

| benchmark | base | this model |
|---|---:|---:|
| HumanEval+ | 87.8 | 89.6 (+1.8) |
| MBPP+ | 77.2 | 76.2 (−1.0) |
| LiveCodeBench | 52.4 | 52.9 (+0.5) |

### Safety/Bias

| benchmark | base | this model |
|---|---:|---:|
| BBQ | 92.2 | 91.6 (−0.6) |
| SafetyBench | 83.2 | 82.2 (−1.0) |

### Macro

| benchmark | base | this model |
|---|---:|---:|
| Korean MC macro | 79.3 | 78.7 (−0.6) |
| Academic 10-bench macro | 74.7 | 75.2 (+0.5) |

## Usage (MLX)

```python
from mlx_lm import load, generate
model, tok = load("RAS-LAB/Qwen3-Coder-27B-A3B-KREAP-MLX")
print(generate(model, tok, prompt="한국어로 자기소개를 해줘.", max_tokens=256))
```

Standard HF safetensors (BF16) — also loadable with `transformers`. Coverage note: KoBEST & EvalPlus are full sets; KMMLU/evalbox/LiveCodeBench are deterministic subsets (seed 42). Effect sizes ≫ sampling CI. Details: K-Guard-REAP `docs/10_MASTER_RESULTS.md §7`.

## Method

REAP saliency (router gate × expert-output L2 norm, conditional mean) restricted to Korean segments + Korean↔English contrast + rare/rollout protection → hard-protected survivor set → streaming safetensors surgery (uniform experts/layer). Framework: https://github.com/Chedrian07/K-REAP