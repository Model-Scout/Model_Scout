---
language:
  - en
  - ko
  - ja
  - zh
license: other
license_name: nvidia-open-model
license_link: https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16/blob/main/LICENSE
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
  - text-only-extraction
base_model: nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
pipeline_tag: text-generation
library_name: llama.cpp
---

# Nemotron 3 Nano Omni 30B-A3B — Text-Only — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/nemotron3-nano-omni-text"><img src="https://img.shields.io/badge/Ollama-batiai%2Fnemotron3--nano--omni--text-green?style=for-the-badge" alt="Ollama"></a>
</p>

> **Text-only extraction** from NVIDIA's **Nemotron 3 Nano Omni Reasoning** multimodal model.
> The text backbone (NemotronH MoE 30B-A3B) extracted, BF16 → IQ3/IQ4/Q5 quantized.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## What Is This?

The original **Nemotron 3 Nano Omni** is a multimodal reasoning model with:
- ViT vision encoder (image understanding)
- Parakeet audio encoder (speech understanding)
- NemotronH MoE 30B-A3B text backbone (reasoning)

This GGUF release contains **only the text backbone** because llama.cpp does not yet support the Omni multimodal architecture. The vision and audio encoders are stripped; the text backbone (which is a standard `NemotronHForCausalLM`) is converted as-is.

**Get the multimodal version when available**: We are watching for upstream llama.cpp support and will publish the full Omni (vision+audio+text) GGUF as soon as it lands.

## Why Nemotron 3 Nano Omni (text)?

- **Reasoning-tuned** — the Omni variant is trained for step-by-step reasoning
- Same NemotronH MoE 30B-A3B backbone as Nemotron 3 Nano (3B active per token)
- Hybrid Mamba+Attention — long context with linear scaling
- NVIDIA Open Model License — commercial-friendly

## Quick Start

```bash
ollama pull batiai/nemotron3-nano-omni-text:iq4
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

## Nano vs Nano Omni (text-only)

Both share the same NemotronH MoE 30B-A3B backbone, but the Omni variant is **reasoning-tuned**:

| | Nemotron 3 Nano | Nemotron 3 Nano Omni (text) |
|---|---|---|
| Tuning | General agentic | **Reasoning-focused** |
| Step-by-step output | Standard | **Stronger** |
| Tool calling | ✅ | ✅ |
| Multimodal | — | ⚠️ Stripped (vision/audio not in this GGUF) |

If you want vision/audio, watch this repo — multimodal release pending llama.cpp support.

## Why BatiAI Extraction?

- We built a custom extraction script that filters `language_model.*` tensors and re-saves with the standard `NemotronHForCausalLM` config
- Quantized directly from official NVIDIA Omni weights
- imatrix calibrated (200 chunks wikitext-2)
- BatiAI signed (`general.author=BatiAI`)

## Technical Details

- **Source Model**: [nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) (multimodal)
- **Extraction**: text backbone only (`language_model.*` tensors → standard NemotronHForCausalLM)
- **Architecture**: NemotronH MoE (Mamba + Attention hybrid, 30B-A3B)
- **License**: NVIDIA Open Model License
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) — `imatrix --chunks 200` calibrated
- **Quantized by**: [BatiAI](https://bati.ai)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited. 57+ built-in tools for calendar, notes, reminders, files, email, browser, messaging.

## License

Quantized from [nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16). License: **NVIDIA Open Model License**.
