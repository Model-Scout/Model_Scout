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
| **Fidelity-48pc** | 1594 | 21.0649† | −0.3815 | 0.0081 | 2.09% | 96.0% | ★ |
| **Precision-42pc** ⭐ | 1418 | 21.3036† | −0.1427 | 0.0100 | 2.19% | 95.3% | ★ |
| Q6_K-imx (stock) | 1362 | 21.1512† | −0.2952 | 0.0124 | 2.41% | 94.9% | ★ |
| **Quality-36pc** | 1218 | 21.0642† | −0.3821 | 0.0283 | 3.62% | 92.1% | ★ |
| Q5_K_M-imx (stock) | 1200 | 20.9749† | −0.4714 | 0.0415 | 4.37% | 90.6% | ★ |
| **Compact-33pc** | 1121 | 21.2786† | −0.1678 | 0.0553 | 4.82% | 89.0% | ★ |
| **Mini-30pc** | 1021 | 22.3830 | +0.9366 | 0.0972 | 6.58% | 85.0% | ★ |
| IQ4_XS-imx (stock) | 957 | 22.6938 | +1.2475 | 0.1512 | 8.37% | 81.5% | ≈ **Nano-27pc** |
| **Nano-27pc** | 927 | 22.8466 | +1.4002 | 0.1397 | 8.04% | 82.0% | ★ |
| **Pico-24pc** | 832 | 24.7068 | +3.2605 | 0.2104 | 10.08% | 78.3% | ★ |
| IQ3_M-imx (stock) | 829 | 21.1749† | −0.2714 | 0.2799 | 11.38% | 75.7% | ★ |
| **Femto-21pc** | 738 | 26.4226 | +4.9762 | 0.3574 | 13.04% | 71.3% | ★ |

## ℹ️ About [Paretrix Quantization Suite](https://huggingface.co/Soulfate24/Paretrix_Quantization_Suite)

[![Engine](https://img.shields.io/badge/Engine-llama.cpp%20%7C%20gguf--py-orange.svg)](https://github.com/ggml-org/llama.cpp)
[![Verdict regime](https://img.shields.io/badge/Verdict-ctx%204096%C3%978-blue.svg)](#-benchmarks)
[![Dominations](https://img.shields.io/badge/Pareto-9%20strict%20dominations-success.svg)](#summary--strict-pareto-dominations)

**Paretrix** is an empirical, activation-aware quantization suite for GGUF language models and speculative decoding modules.

**Pareto + Matrix → Paretrix.** Each rung is planned so that no better trade exists at its weight among the options measured. Around three stock bases (Q8_0, Q6_K-imx, IQ4_XS-imx), every tensor class is moved alone to every type and measured against the BF16 logits; an exact knapsack then plans each rung from those cells, and a duel at the verdict regime decides whether the plan replaces the champion. What one model measures, the next model of its family inherits.

Standard uniform quantization applies one bitwidth family across the whole network. Paretrix reads the model's own response to each move (which classes are expensive to cut, which are nearly free, which pay back a buy), then spends the budget where the measurements show the greatest return.
