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
  - moe
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
base_model: Qwen/Qwen3.5-35B-A3B
pipeline_tag: text-generation
library_name: llama.cpp
---

# Qwen 3.5 35B-A3B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3.5-35b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3.5--35b-green?style=for-the-badge" alt="Ollama"></a>
</p>

> IQ4_XS quantization of **Qwen/Qwen3.5-35B-A3B** for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Quick Start

```bash
ollama pull batiai/qwen3.5-35b:iq4
```

## Available Quantizations

| Quant | Size | VRAM | M4 Max (128GB) | Recommended For |
|-------|------|------|----------------|----------------|
| **IQ4_XS** | **17GB** | **23GB** | **26.6 t/s** | **36GB+ Mac** |

## Why MoE Beats Dense

35B-A3B is a Mixture-of-Experts model — 35B total, only 3B active per token:

| | 35B-A3B (MoE) | 27B (Dense) |
|---|---|---|
| Total params | 35B | 27B |
| **Active params** | **3B** | **27B** |
| VRAM | **23GB** | 28GB |
| Speed | **26.6 t/s** | 17.0 t/s |

MoE activates 9x fewer parameters — same quality, much faster, less memory.

## Benchmarks — M4 Max (128GB)

| Metric | IQ4_XS |
|--------|--------|
| Token generation | **26.6 t/s** |
| Korean | ✅ |
| Tool call JSON | ✅ |
| VRAM | 23 GB |

## Full BatiAI Qwen 3.5 Lineup

| Model | Size | VRAM | Speed | Min Mac |
|-------|------|------|-------|---------|
| batiai/qwen3.5-9b:q4 | 5.2GB | ~8GB | 12.5 t/s | 16GB |
| batiai/qwen3.5-27b:iq4 | 14GB | 28GB | 17.0 t/s | 32GB |
| **batiai/qwen3.5-35b:iq4** | **17GB** | **23GB** | **26.6 t/s** | **36GB** |

## Technical Details

- **Original Model**: [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
- **Architecture**: MoE (35B total, 3B active, 256 experts, 8 routed + 1 shared)
- **Context Window**: 262K tokens
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) (build 400ac8e)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited.

## License

Quantized from [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B). License: **Apache 2.0**.

## Benchmarks

<!-- BENCH-START -->

| Machine | Quant | Cold start | Prompt eval | Token gen | Tested |
|---------|-------|------------|-------------|-----------|--------|
| MacBook Pro M4 Max 128GB | IQ4_XS | 4.825s | 205.28 t/s | 44.77 t/s | 2026-05-03 |

<!-- BENCH-END -->
