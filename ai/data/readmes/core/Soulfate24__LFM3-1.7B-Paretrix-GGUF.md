---
library_name: transformers
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
base_model:
  - LiquidAI/LFM3-1.7B
base_model_relation: quantized
tags:
  - liquid
  - lfm3
  - edge
  - conversational
  - custom_code
  - llama.cpp
  - quantization
  - gguf
  - imatrix
  - hybrid-quantization
  - pareto
  - rco
---

## 🧮 Paretrix GGUF quantizations of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)

| Model | MiB | PPL | ΔPPL | KLD | RMS Δp | top-p | Pareto |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Q8_0 (stock) | 1761 | 21.4793 | +0.0329 | 0.0037 | 1.19% | 97.3% | ★ |
| **Fidelity-48pc** | 1594 | 21.5744 | +0.1280 | 0.0062 | 1.67% | 96.3% | ★ |
| **Precision-42pc** ⭐ | 1418 | 21.3036† | −0.1427 | 0.0100 | 2.19% | 95.3% | ★ |
| Q6_K-imx (stock) | 1362 | 21.1512† | −0.2952 | 0.0124 | 2.41% | 94.9% | ★ |
| **Quality-36pc** | 1218 | 21.0996† | −0.3468 | 0.0248 | 3.35% | 92.7% | ★ |
| Q5_K_M-imx (stock) | 1200 | 20.6560† | −0.7904 | 0.0395 | 4.24% | 90.8% | ★ |
| **Compact-33pc** | 1121 | 21.2974† | −0.1489 | 0.0518 | 4.67% | 89.4% | ★ |
| **Mini-30pc** | 1021 | 22.3538 | +0.9075 | 0.0947 | 6.53% | 85.3% | ★ |
| IQ4_XS-imx (stock) | 957 | 22.6938 | +1.2475 | 0.1512 | 8.37% | 81.5% | < **Nano-27pc** |
| **Nano-27pc** | 927 | 22.8811 | +1.4347 | **0.1300** | 7.82% | 82.8% | ★ |
| **Pico-24pc** | 833 | 24.5628 | +3.1164 | 0.2026 | 9.98% | 78.6% | ★ |
| IQ3_M-imx (stock) | 829 | 21.1740† | −0.2723 | 0.2820 | 11.40% | 75.6% | ★ |
| **Femto-21pc** | 738 | 23.6781 | +2.2318 | 0.3486 | 12.60% | 71.9% | ★ |

## ℹ️ About [Paretrix Quantization Suite](https://huggingface.co/Soulfate24/Paretrix_Quantization_Suite)

[![Engine](https://img.shields.io/badge/Engine-llama.cpp%20%7C%20gguf--py-orange.svg)](https://github.com/ggml-org/llama.cpp)
[![Verdict regime](https://img.shields.io/badge/Verdict-ctx%204096%C3%978-blue.svg)](#-benchmarks)
[![Dominations](https://img.shields.io/badge/Pareto-9%20strict%20dominations-success.svg)](#summary--strict-pareto-dominations)

**Paretrix** is an empirical, activation-aware quantization suite for GGUF language models and speculative decoding modules.

**Pareto + Matrix → Paretrix.** Each rung is planned so that no better trade exists at its weight among the options measured. Around three stock bases (Q8_0, Q6_K-imx, IQ4_XS-imx), every tensor class is moved alone to every type and measured against the BF16 logits; an exact knapsack then plans each rung from those cells, and a duel at the verdict regime decides whether the plan replaces the champion. What one model measures, the next model of its family inherits.

Standard uniform quantization applies one bitwidth family across the whole network. Paretrix reads the model's own response to each move (which classes are expensive to cut, which are nearly free, which pay back a buy), then spends the budget where the measurements show the greatest return.
