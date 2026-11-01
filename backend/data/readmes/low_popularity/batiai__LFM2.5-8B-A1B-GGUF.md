---
language:
  - en
  - ko
  - ja
  - zh
license: other
license_name: lfm-open-license-v1.0
license_link: https://www.liquid.ai/lfm-license
tags:
  - gguf
  - lfm2
  - lfm2-moe
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - moe
  - reasoning
  - tool-calling
  - edge
base_model: LiquidAI/LFM2.5-8B-A1B
pipeline_tag: text-generation
library_name: llama.cpp
---

# Liquid LFM2.5-8B-A1B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/lfm2.5-8b"><img src="https://img.shields.io/badge/Ollama-batiai%2Flfm2.5--8b-green?style=for-the-badge" alt="Ollama"></a>
</p>

> Quantizations of **Liquid AI LFM2.5-8B-A1B** (8.3B total / 1.5B active MoE, reasoning + tool calling) for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Why LFM2.5-8B-A1B?

- **8.3B total, only 1.5B active** — MoE (32 experts, 4 active) gives 8B-class quality at ~1.5B-class speed
- **Hybrid architecture** — 24 layers: 18 double-gated LIV convolution + 6 GQA attention. Built for edge, not GPUs
- **Reasoning model** — explicit chain-of-thought before the final answer
- **Native tool calling** — Pythonic or JSON function calls (`<|tool_call_start|>` / `<|tool_call_end|>`)
- **128K context**, 38T-token training budget, 128K vocab (better non-Latin tokenization incl. Korean)
- **Blazing on-device** — Liquid reports 253 tok/s on M5 Max, 146 tok/s on Ryzen AI Max+ 395, all under 6GB
- **Released May 28, 2026**

## Quick Start

```bash
ollama pull batiai/lfm2.5-8b:q4
```

## Available Quantizations

| Quant | Size | Recommended For |
|-------|------|-----------------|
| **Q2_K_S** | ~2.8 GB | 8GB Mac, ultra-compact (imatrix) |
| **IQ3_XXS** | ~3.2 GB | imatrix, smallest K-class footprint |
| **Q3_K_M** | ~3.9 GB | 8GB+ Mac, balanced |
| **IQ4_XS** | ~4.3 GB | imatrix, best size/quality |
| **Q4_K_M** | ~4.9 GB | **16GB Mac (recommended)** |
| **Q6_K** | ~6.5 GB | near-original quality |

> **Mac note on `Q3_K_M`:** in every model we've benchmarked on Apple Silicon, Q3_K_M generated
> *slower* than Q4_K_M despite the smaller file — Granite 4.1 (+27%), Gemma 4 26B (+12%),
> Qwen3.8‑27B (+18%), Qwen3.6‑27B (+8%), on both M4 Max and M4 mini. Metal's Q3_K path is limited by
> dequantization compute rather than bandwidth. We have not measured this particular model's
> Q3/Q4 pair yet, so treat it as a strong prior, not a measurement: **if Q4_K_M fits, take it.**
> On CUDA the two are effectively tied, so this applies to Macs only.

*Lower quants (IQ3_XXS, Q2_K_S) and imatrix variants are not provided in the official Liquid GGUF repo — BatiAI adds them for 8GB Macs and tighter footprints.*

## RAM Requirements

This model is tiny in active params — even the largest quant fits comfortably on 16GB. With only 1.5B active params, throughput stays high regardless of quant.

| Your Mac RAM | IQ3 | Q2 | Q3 | IQ4 | Q4 | Q6 |
|-------------|-----|-----|-----|-----|-----|-----|
| **8GB** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **16GB** | ✅ | ✅ | ✅ | ✅ | **✅ Recommended** | ✅ |
| **24GB+** | ✅ | ✅ | ✅ | ✅ | ✅ | **✅** |

## Why BatiAI Quantization?

| | BatiAI | Official Liquid GGUF |
|---|---|---|
| **Source** | [Official Liquid weights](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) | Official |
| **Ollama** | ✅ `batiai/lfm2.5-8b` | ❌ HF only |
| **Low quants** | ✅ IQ3_XXS, Q2_K_S, Q3_K_M | ❌ Q4_0 floor |
| **imatrix** | ✅ IQ variants calibrated | Standard |
| **Tool calling** | ✅ Verified | — |
| **BatiAI signed** | ✅ `general.author=BatiAI` | — |

## Technical Details

- **Original Model**: [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)
- **Architecture**: `lfm2_moe` hybrid — 18 LIV conv + 6 GQA layers, 32 experts / 4 active per token
- **Parameters**: 8.3B total, 1.5B active
- **Context**: 131,072 tokens
- **Training**: 38T tokens
- **License**: LFM Open License v1.0 (Apache-2.0 based; free commercial use under $10M annual revenue)
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) + imatrix
- **Quantized by**: [BatiAI](https://bati.ai)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited.

## License

Quantized from [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B).
License: **LFM Open License v1.0** — see https://www.liquid.ai/lfm-license. Original Liquid AI attribution retained. Free for commercial use by organizations under $10M USD annual revenue; above that threshold, contact Liquid AI.

## Benchmarks

<!-- BENCH-START -->

_Benchmarks pending — measured on target Mac hardware via `bench.sh`._

<!-- BENCH-END -->
