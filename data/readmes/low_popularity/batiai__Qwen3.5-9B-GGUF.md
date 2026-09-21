---
language:
  - en
  - ko
  - ja
  - zh
license: apache-2.0
tags:
  - gguf
  - qwen
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - 9b
base_model: Qwen/Qwen3.5-9B
pipeline_tag: text-generation
library_name: llama.cpp
---

# Qwen 3.5 9B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3.5-9b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3.5--9b-green?style=for-the-badge" alt="Ollama"></a>
</p>

> Quantizations of **Qwen 3.5 9B** for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Why Qwen 3.5 9B?

- Strong tool calling and JSON structured output
- Multilingual (en, ko, ja, zh) — solid Korean
- Apache 2.0 — commercial-friendly
- **Fits 16GB Mac** with Q4

## Quick Start

```bash
ollama pull batiai/qwen3.5-9b:q4
```

## Available Quantizations

| Quant | Size | VRAM target | Recommended For |
|-------|------|-------------|-----------------|
| **Q4_K_M** | **5.2GB** | ~7GB | **16GB Mac** |
| **Q6_K** | **7.5GB** | ~10GB | 24GB+ Mac |

## RAM Requirements

| Your Mac RAM | Q4 (5.2GB) | Q6 (7.5GB) |
|-------------|-----------|-----------|
| **16GB** | **✅ Recommended** | ⚠️ Tight |
| 24GB+ | ✅ | ✅ Headroom |

## Model Comparison

| Your Mac | Best Pick |
|----------|-----------|
| 16GB | `batiai/qwen3.5-9b:q4` (this) or `batiai/gemma4-e4b:q4` |
| 24GB | `batiai/gemma4-26b:iq4` |
| 32GB | `batiai/nemotron3-nano:iq4` |
| 36GB+ | `batiai/qwen3.6-35b:iq4` |

## Why BatiAI?

- Quantized from [official Qwen weights](https://huggingface.co/Qwen/Qwen3.5-9B)
- Verified on real Mac hardware
- BatiAI metadata signed (`general.author=BatiAI`)
- Tool calling + Korean validated

## Technical Details

- **Original Model**: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp)
- **Quantized by**: [BatiAI](https://bati.ai)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited.

## Benchmarks

<!-- BENCH-START -->

| Machine | Quant | Cold start | Prompt eval | Token gen | Tested |
|---------|-------|------------|-------------|-----------|--------|
| Mac mini M4 16GB | Q4_K_M | —s | — t/s | — t/s | 2026-05-01 |
| Mac mini M4 16GB | Q6_K | —s | — t/s | — t/s | 2026-05-01 |
| MacBook Pro M4 Max 128GB | Q4_K_M | 2.274s | 272.23 t/s | 46.08 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q6_K | 2.552s | 304.85 t/s | 38.54 t/s | 2026-05-03 |

<!-- BENCH-END -->
