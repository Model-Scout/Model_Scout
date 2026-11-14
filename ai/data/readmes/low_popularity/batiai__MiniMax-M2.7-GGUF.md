---
language:
  - en
  - ko
  - ja
  - zh
license: other
license_name: modified-mit
license_link: https://huggingface.co/MiniMaxAI/MiniMax-M2.7/blob/main/LICENSE
tags:
  - gguf
  - minimax
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - 229b
base_model: MiniMaxAI/MiniMax-M2.7
pipeline_tag: text-generation
library_name: llama.cpp
---

# MiniMax M2.7 GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/minimax-m2.7"><img src="https://img.shields.io/badge/Ollama-batiai%2Fminimax--m2.7-green?style=for-the-badge" alt="Ollama"></a>
</p>

> IQ3_XXS quantization of **MiniMaxAI/MiniMax-M2.7** (229B Dense) for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Why MiniMax M2.7?

- **229B Dense** — one of the largest open models
- Outperforms GPT-5.3 on GDPval-AA (ELO 1495)
- Toolathon: 46.3% accuracy (global top tier)
- Agent Teams, complex Skills, dynamic tool search
- **Runs on a 128GB MacBook Pro** — no cloud needed

## Quick Start

```bash
ollama pull batiai/minimax-m2.7:iq3
```

## Available Quantizations

| Quant | Size | VRAM | M4 Max (128GB) | Recommended For |
|-------|------|------|----------------|----------------|
| **IQ3_XXS** | **82GB** | **104GB** | **36.7 t/s** | **128GB+ Mac** |

## Benchmarks — MacBook Pro M4 Max (128GB)

| Metric | IQ3_XXS |
|--------|---------|
| **Token gen (short)** | **22.1 t/s** |
| **Token gen (long, 300 tokens)** | **36.7 t/s** |
| Prompt eval | 14.8 t/s |
| VRAM | 104 GB (97% GPU / 3% CPU) |
| Cold start | 42 seconds |
| Korean output | ✅ |
| Tool call JSON | ✅ |
| Basic math (2+2) | ✅ |

### RAM Requirements

| Your Mac RAM | IQ3_XXS (82GB) |
|-------------|---------------|
| 64GB or less | ❌ Won't fit |
| 96GB | ⚠️ Heavy swap, unusable |
| **128GB** | **✅ 36.7 t/s** |
| 192GB+ | ✅ Fast, with headroom |

## 229B on a Laptop

This is a 229B parameter dense model running entirely on-device — no cloud, no API, no costs. IQ3_XXS quantization compresses from 457GB (BF16) to 82GB while maintaining Korean, tool calling, and reasoning capabilities.

## Model Comparison — Which BatiAI Model for Your Mac?

| Your Mac | Best Model | Speed |
|----------|-----------|-------|
| 16GB | `batiai/gemma4-e4b:q4` | 57 t/s |
| 24GB | `batiai/gemma4-26b:iq4` | 85 t/s |
| 36GB | `batiai/qwen3.5-35b:iq4` | 26.6 t/s |
| 48GB | `batiai/gemma4-31b:iq4` | 22.8 t/s |
| **128GB** | **`batiai/minimax-m2.7:iq3`** | **36.7 t/s** |

## Why BatiAI Quantization?

| | BatiAI | Third-party (unsloth, etc.) |
|---|---|---|
| **Source** | Quantized from [official MiniMax weights](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) | Re-quantized from other GGUFs |
| **Tested on** | Real MacBook Pro M4 Max (128GB) | Often untested on consumer hardware |
| **Tool Calling** | ✅ Verified | Often untested |
| **Korean** | ✅ Validated | Not tested |
| **imatrix** | ✅ Calibrated for quality | Standard or none |

## Technical Details

- **Original Model**: [MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
- **Architecture**: Dense (229B params, all active)
- **License**: Modified-MIT
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp)
- **Quantized by**: [BatiAI](https://bati.ai)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited. 57+ built-in tools for calendar, notes, reminders, files, email, browser, messaging.

## License

Quantized from [MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7). License: **Modified-MIT**.
