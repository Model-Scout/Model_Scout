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
tags:
  - liquid
  - lfm2.5
  - edge
  - speculative-decoding
  - dspark
  - lfm2
  - draft-model
  - quantization
  - gguf
  - ashq1
  - imatrix
---

**LFM2.5-2.6B with DSpark - ASHQ1-Remix**

This is a GGUF quantized version of the original model.

## 📈 Release Benchmarks (wiki.test.raw, symmetric FA-auto reference)

| Model | Size | PPL | KLD | RMS Δp | top-p | Speed |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Q8_0 (stock) | 2742 MiB | 55.0069 | 0.0030 | 1.22% | 97.4% | 3413 t/s |
| **Fidelity-48pc** | 2481 MiB | 55.6994 | 0.0074 | 1.97% | 96.0% | 2844 t/s |
| **Precision-42pc** 🥈 | 2199 MiB | 55.2931 | 0.0087 | 2.20% | 95.7% | 2695 t/s |
| Q6_K-imx (stock) | 2119 MiB | 55.6407 | 0.0122 | 2.54% | 94.7% | 2844 t/s |
| **Quality-36pc** ⭐ | 1850 MiB | 54.9504† | 0.0347 | 3.95% | 91.1% | 3200 t/s |
| Q5_K_M-imx (stock) | 1850 MiB | 54.9504† | 0.0347 | 3.95% | 91.1% | 2844 t/s |
| **Compact-33pc** | 1708 MiB | 53.0954† | 0.0734 | 6.01% | 87.5% | 2844 t/s |
| **Mini-30pc** | 1554 MiB | 49.8535† | 0.1291 | 8.10% | 83.4% | 2844 t/s |
| IQ4_XS-imx (stock) | 1447 MiB | 55.5126 | 0.1486 | 8.59% | 81.8% | 2560 t/s |
| **Nano-27pc** ✗ | 1399 MiB | 58.9388 | 0.2130 | 10.16% | 78.3% | 3012 t/s |
| **Pico-24pc** ✗ | 1276 MiB | 54.4368† | 0.3644 | 12.94% | 72.7% | 3200 t/s |
| IQ3_M-imx (stock) | 1225 MiB | 59.3136 | 0.3884 | 13.44% | 72.2% | 3012 t/s |

## ℹ️ About ASHQ1-Remix Suite
Activation-aware GGUF quantization whose every ratio, floor, and cap traces to a measured experiment. Plain-BF16-native first; AutoRound lineage supported with explicit saturation bounds. Full seven-tier ladder validated across six model families.

🔗 Link: https://huggingface.co/Soulfate24/AutoRound-ASHQ1-Remix_Double-Quantization_Suite
