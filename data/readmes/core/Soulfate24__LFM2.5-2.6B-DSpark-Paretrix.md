---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
base_model:
  - LiquidAI/LFM2.5-2.6B
  - LiquidAI/LFM2.5-2.6B-DSpark
base_model_relation: quantized
tags:
  - liquid
  - lfm2.5
  - edge
  - llama.cpp
  - quantization
  - gguf
  - imatrix
  - hybrid-quantization
  - pareto
  - rco
  - speculative-decoding
  - draft
---

## 🧮 Paretrix GGUF quantizations of [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) with [DSpark draft](https://huggingface.co/LiquidAI/LFM2.5-2.6B-DSpark)

| Model | MiB | PPL | ΔPPL | KLD | RMS Δp | top-p | Pareto |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Q8_0 (stock) | 2742 | 51.8867 | +0.4677 | 0.0032 | 1.34% | 97.4% | ★ |
| **Fidelity-48pc** | 2481 | 52.2324 | +0.8134 | 0.0076 | 2.09% | 96.2% | ★ |
| **Precision-42pc** | 2138 | 52.8312 | +1.4122 | 0.0105 | 2.44% | 95.4% | ★ |
| Q6_K-imx (stock) | 2119 | 52.7076 | +1.2886 | 0.0131 | 2.66% | 94.7% | ★ |
| Q5_K_M-imx (stock) | 1850 | 51.5220 | +0.1030 | 0.0380 | 4.39% | 91.0% | < **Quality-36pc** |
| **Quality-36pc** ⭐ | 1848 | 52.6558 | +1.2368 | **0.0309** | 4.13% | 91.6% | ★ |
| **Compact-33pc** | 1712 | 49.4337 | −1.9853 | 0.0696 | 6.13% | 88.0% | ★ |
| **Mini-30pc** | 1560 | 46.9409† | −4.4780 | 0.0995 | 7.45% | 85.9% | ★ |
| IQ4_XS-imx (stock) | 1447 | 52.6602 | +1.2412 | 0.1652 | 9.56% | 81.6% | < **Nano-27pc** |
| **Nano-27pc** | 1405 | 52.7926 | +1.3736 | **0.1536** | 8.91% | 81.8% | ★ |
| **Pico-24pc** | 1273 | 55.9255 | +4.5065 | 0.3597 | 13.43% | 74.6% | ★ |
| IQ3_M-imx (stock) | 1225 | 60.9679 | +9.5490 | 0.4254 | 14.31% | 72.6% | ★ |
| **Femto-21pc** | 1096 | 71.9524 | +20.5334 | 0.5535 | 16.29% | 69.0% | ★ |

## ℹ️ About [Paretrix Quantization Suite](https://huggingface.co/Soulfate24/Paretrix_Quantization_Suite)

**Paretrix** is an empirical, activation-aware quantization suite for GGUF language models and speculative decoding modules.

**Pareto + Matrix → Paretrix.** Each tier is priced so that no better trade exists at that compression. The suite measures real activation sensitivity (ΔKLD/MiB) per tensor class through `llama-imatrix`, learns rate tables from cross-architecture campaigns (THE MATRIX), and allocates bitwidths under exact budget targets: flat recipes where uniformity wins, rate-calibrated knapsack where heterogeneity pays.

Standard uniform quantization applies one bitwidth family across the whole network. Paretrix reads the model's own activation field (which classes are expensive to cut, which are nearly free, and where depth matters), then spends the budget where measurements show the greatest return.
