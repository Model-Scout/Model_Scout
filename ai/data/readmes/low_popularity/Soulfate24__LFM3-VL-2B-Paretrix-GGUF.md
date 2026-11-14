---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: image-text-to-text
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
  - LiquidAI/LFM3-VL-2B
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
  - vision
---

## 🧮 Paretrix GGUF quantizations of [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B)

| Model | MiB | PPL | ΔPPL | KLD | RMS Δp | top-p | Pareto |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Q8_0 (stock) | 1761 | 72.5538† | −0.2753 | 0.0023 | 1.01% | 97.6% | ★ |
| **Fidelity-48pc** | 1594 | 72.8550 | +0.0258 | 0.0037 | 1.30% | 96.8% | ★ |
| **Precision-42pc** | 1415 | 73.0043 | +0.1752 | 0.0063 | 1.68% | 96.0% | ★ |
| Q6_K-imx (stock) | 1362 | 71.6059† | −1.2232 | 0.0103 | 2.04% | 94.9% | ★ |
| **Quality-36pc** ⭐ | 1219 | 72.6376† | −0.1915 | 0.0171 | 2.65% | 93.5% | ★ |
| Q5_K_M-imx (stock) | 1200 | 74.3414 | +1.5122 | 0.0291 | 3.52% | 91.6% | ★ |
| **Compact-33pc** | 1121 | 72.1034† | −0.7258 | 0.0323 | 3.75% | 90.8% | ★ |
| **Mini-30pc** | 1021 | 68.6162† | −4.2129 | 0.0593 | 5.07% | 88.1% | ★ |
| IQ4_XS-imx (stock) | 957 | 81.4215 | +8.5924 | 0.1518 | 7.96% | 82.1% | < **Nano-27pc** |
| **Nano-27pc** | 927 | 68.0712† | −4.7579 | **0.0921** | 6.34% | 84.9% | ★ |
| **Pico-24pc** | 832 | 69.6922† | −3.1369 | 0.1717 | 8.68% | 80.2% | ★ |
| IQ3_M-imx (stock) | 829 | 77.6138 | +4.7846 | 0.2681 | 10.69% | 75.7% | ★ |
| **Femto-21pc** | 738 | 66.9075† | −5.9217 | 0.2902 | 10.90% | 74.2% | ★ |

## ℹ️ About [Paretrix Quantization Suite](https://huggingface.co/Soulfate24/Paretrix_Quantization_Suite)

[![Engine](https://img.shields.io/badge/Engine-llama.cpp%20%7C%20gguf--py-orange.svg)](https://github.com/ggml-org/llama.cpp)
[![Verdict regime](https://img.shields.io/badge/Verdict-ctx%204096%C3%978-blue.svg)](#-benchmarks)
[![llama.cpp build](https://img.shields.io/badge/llama.cpp-build%2012283-lightgrey.svg)](#-benchmarks)
[![Dominations](https://img.shields.io/badge/Pareto-18%20strict%20dominations-success.svg)](#summary--strict-pareto-dominations)

**Paretrix** is an empirical, activation-aware quantization suite for GGUF language models and speculative decoding modules.

**Pareto + Matrix → Paretrix.** Each rung is planned so that no better trade exists at its weight among the options measured. Around three stock bases (Q8_0, Q6_K-imx, IQ4_XS-imx), every tensor class is moved alone to every type and measured against the BF16 logits; an exact knapsack then plans each rung from those cells, and a duel at the verdict regime decides whether the plan replaces the champion. What one model measures, the next model of its family inherits.

Standard uniform quantization applies one bitwidth family across the whole network. Paretrix reads the model's own response to each move (which classes are expensive to cut, which are nearly free, which pay back a buy), then spends the budget where the measurements show the greatest return.
