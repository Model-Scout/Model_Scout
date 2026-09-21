---
license: apache-2.0
base_model: Qwen/Qwen3-Coder-30B-A3B-Instruct
library_name: mlx
pipeline_tag: text-generation
language: [ko, en]
tags: [moe, pruning, reap, k-reap, mlx, korean, expert-pruning]
---

# Qwen3-Coder-16B-A3B-KREAP-MLX  (50% routed pruning)

Korean-preserving one-shot MoE expert pruning of [Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct), produced with [**K-REAP**](https://github.com/Chedrian07/K-REAP). Routed experts pruned **128 → 64** per layer (50%); ~16B total params, 3.3B active (top-8 unchanged). No fine-tuning.

Unlike vanilla REAP (English/code calibration), K-REAP detects and **hard-protects the experts that carry Korean**, so pruning preserves Korean without sacrificing English/coding. See [K-Guard-REAP](https://github.com/Chedrian07/K-Guard-REAP) for the full study.

## Korean loss minimized vs. standard REAP

The standard REAP recipe collapses Korean at comparable compression: Cerebras **Qwen3-Coder-REAP-25B** (19.5%, no language protection) drops Korean MC macro **79.3 → 56.6 (−22.7pp)** with generation collapse **115/128**. By hard-protecting the Korean expert path, **this model keeps Korean MC macro at 67.3 (−12.0pp) with 52/128 collapse** — still well ahead of REAP's 56.6 / 115 even at this aggressive ratio. (K-REAP removes ~47% of REAP's Korean damage.)

> **⚠️ Compression-ceiling model.** At 50% the per-layer protected set (up to 83) no longer fits the budget (64), so 93 Korean-protected experts were force-dropped. Korean **and** English reasoning degrade here — this checkpoint documents the limit, not a recommended operating point. Use 12.5–25% for preserved Korean.

## Benchmarks (vs base Qwen3-Coder-30B; Δ = base delta, %p)

### 한국어 (Korean, self-harness)

| benchmark | base | this model |
|---|---:|---:|
| KMMLU | 55.2 | 41.2 (−14.0) |
| KoBEST BoolQ | 93.6 | 80.4 (−13.2) |
| KoBEST COPA | 92.7 | 71.5 (−21.2) |
| KoBEST SentiNeg | 95.0 | 90.4 (−4.6) |
| KoBEST HellaSwag | 60.0 | 52.8 (−7.2) |
| Gen. collapse (/128, ↓) | 0 | 52 |

### English reasoning/knowledge (llm-evalbox)

| benchmark | base | this model |
|---|---:|---:|
| ARC-Challenge | 91.2 | 71.0 (−20.2) |
| HellaSwag | 84.4 | 63.4 (−21.0) |
| WinoGrande | 73.4 | 57.6 (−15.8) |
| MMLU-Pro | 50.2 | 37.0 (−13.2) |
| TruthfulQA | 71.2 | 46.6 (−24.6) |
| MMLU-en | 76.6 | 54.6 (−22.0) |

### Math

| benchmark | base | this model |
|---|---:|---:|
| GSM8K | 93.2 | 80.2 (−13.0) |
| MathQA | 55.2 | 33.8 (−21.4) |

### Coding

| benchmark | base | this model |
|---|---:|---:|
| HumanEval+ | 87.8 | 79.3 (−8.5) |
| MBPP+ | 77.2 | 59.3 (−17.9) |
| LiveCodeBench | 52.4 | 27.9 (−24.5) |

### Safety/Bias

| benchmark | base | this model |
|---|---:|---:|
| BBQ | 92.2 | 66.8 (−25.4) |
| SafetyBench | 83.2 | 73.4 (−9.8) |

### Macro

| benchmark | base | this model |
|---|---:|---:|
| Korean MC macro | 79.3 | 67.3 (−12.0) |
| Academic 10-bench macro | 74.7 | 55.8 (−18.9) |

## Usage (MLX)

```python
from mlx_lm import load, generate
model, tok = load("KCh3dRi4n/Qwen3-coder-16B-A3B-KREAP-MLX")
print(generate(model, tok, prompt="한국어로 자기소개를 해줘.", max_tokens=256))
```

Standard HF safetensors (BF16) — also loadable with `transformers`. Coverage note: KoBEST & EvalPlus are full sets; KMMLU/evalbox/LiveCodeBench are deterministic subsets (seed 42). Effect sizes ≫ sampling CI. Details: K-Guard-REAP `docs/10_MASTER_RESULTS.md §7`.

## Method

REAP saliency (router gate × expert-output L2 norm, conditional mean) restricted to Korean segments + Korean↔English contrast + rare/rollout protection → hard-protected survivor set → streaming safetensors surgery (uniform experts/layer). Framework: https://github.com/Chedrian07/K-REAP