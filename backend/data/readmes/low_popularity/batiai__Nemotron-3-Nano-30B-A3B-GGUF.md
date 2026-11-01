---
language:
  - en
  - ko
  - ja
  - zh
license: other
license_name: nvidia-open-model
license_link: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/blob/main/LICENSE
tags:
  - gguf
  - nemotron
  - nemotron-h
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - moe
  - 30b
  - mamba-hybrid
  - reasoning
  - agentic
base_model: nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
pipeline_tag: text-generation
library_name: llama.cpp
---

# Nemotron 3 Nano 30B-A3B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/nemotron3-nano"><img src="https://img.shields.io/badge/Ollama-batiai%2Fnemotron3--nano-green?style=for-the-badge" alt="Ollama"></a>
</p>

> Quantizations of **NVIDIA Nemotron 3 Nano 30B-A3B** (NemotronH MoE, hybrid Mamba+Attention) for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Why Nemotron 3 Nano?

- **30B params, only 3B active per token** — A3B MoE architecture
- **Hybrid Mamba + Attention** — long context with linear scaling
- **Reasoning + agentic** — built for tool use, structured outputs
- **Apache-spirit NVIDIA Open Model License** — commercial-friendly
- **Runs on a 32GB Mac** with IQ3/IQ4

## Quick Start

```bash
ollama pull batiai/nemotron3-nano:iq4
```

## Available Quantizations

| Quant | Size | VRAM target | Recommended For |
|-------|------|-------------|-----------------|
| **IQ3_XXS** | **17GB** | ~20GB | 24–32GB Mac |
| **IQ4_XS** | **17GB** | ~20GB | 32GB Mac (recommended) |
| **Q5_K_M** | **25GB** | ~28GB | 36GB+ Mac (highest quality) |

## RAM Requirements

| Your Mac RAM | IQ3_XXS (17GB) | IQ4_XS (17GB) | Q5_K_M (25GB) |
|-------------|---------------|---------------|---------------|
| 16GB | ⚠️ Heavy swap | ⚠️ Heavy swap | ❌ |
| **24GB** | **✅** | **✅** | ❌ |
| **32GB** | **✅ Fast** | **✅ Recommended** | ⚠️ Tight |
| **36GB+** | **✅** | **✅** | **✅ Best quality** |
| 48GB+ | ✅ | ✅ | ✅ Headroom |

## Model Comparison — Which BatiAI Model for Your Mac?

| Your Mac | Best Model | Notes |
|----------|-----------|-------|
| 16GB | `batiai/gemma4-e4b:q4` | Fast, lightweight |
| 24GB | `batiai/gemma4-26b:iq4` or `batiai/nemotron3-nano:iq3` | Reasoning + tools |
| **32GB** | **`batiai/nemotron3-nano:iq4`** | **Hybrid MoE, agentic** |
| 36GB | `batiai/qwen3.5-35b:iq4` | Alibaba MoE |
| 48GB | `batiai/gemma4-31b:iq4` or `batiai/nemotron3-nano:q5` | High quality |
| 128GB | `batiai/minimax-m2.7:iq3` (229B) | Frontier on laptop |

## Why Nemotron-H Architecture?

NemotronH is NVIDIA's hybrid architecture combining **Mamba state-space layers** with **standard attention**:

- Linear scaling on long context (Mamba) + accuracy at short context (Attention)
- A3B MoE: 128 experts, 8 active per token
- 49 layers with hybrid override pattern
- Trained on reasoning, code, and agentic data

## Why BatiAI Quantization?

| | BatiAI | Third-party (TheBloke, etc.) |
|---|---|---|
| **Source** | Quantized from [official NVIDIA weights](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16) | Re-quantized from other GGUFs |
| **Tested on** | Real Mac hardware | Often untested on consumer hardware |
| **imatrix** | ✅ Calibrated (200 chunks wikitext-2) | Standard or none |
| **Tool Calling** | ✅ Verified | Often untested |
| **Korean** | ✅ Validated | Not tested |

## Technical Details

- **Original Model**: [nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
- **Architecture**: NemotronH MoE (Mamba + Attention hybrid, 30B-A3B)
- **License**: NVIDIA Open Model License
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) — `imatrix --chunks 200` calibrated
- **Quantized by**: [BatiAI](https://bati.ai)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited. 57+ built-in tools for calendar, notes, reminders, files, email, browser, messaging.

## License

Quantized from [nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16). License: **NVIDIA Open Model License**.

## Benchmarks

<!-- BENCH-START -->

| Machine | Quant | Cold start | Prompt eval | Token gen | Tested |
|---------|-------|------------|-------------|-----------|--------|
| MacBook Pro M4 Max 128GB | IQ3_XXS | 1.599s | 208.95 t/s | 86.15 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | IQ4_XS | 1.589s | 206.43 t/s | 88.77 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q5_K_M | 5.036s | 179.26 t/s | 75.82 t/s | 2026-05-03 |

<!-- BENCH-END -->
