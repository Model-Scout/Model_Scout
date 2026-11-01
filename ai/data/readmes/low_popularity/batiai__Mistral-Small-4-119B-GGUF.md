---
language:
  - en
  - ko
  - ja
  - zh
  - fr
  - de
license: apache-2.0
tags:
  - gguf
  - mistral
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - moe
  - 119b
  - reasoning
  - agentic
  - multimodal
base_model: mistralai/Mistral-Small-4-119B-2603
pipeline_tag: text-generation
library_name: llama.cpp
---

# Mistral Small 4 119B-A6B GGUF — Quantized by BatiAI

Mistral's unified open-weight model — **reasoning + multimodal + agentic coding in one**. 119B Mixture-of-Experts with only **6B active per token**, so it runs at small-model speed while keeping frontier quality. **Apache 2.0** (fully commercial-friendly, no gating).

Quantized **directly from [official Mistral weights](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)** — not a re-quant of someone else's GGUF. Signed with BatiAI metadata for [BatiFlow](https://flow.bati.ai).

## Quick Start

```
ollama run batiai/mistral-small-4:q4
```

## Available Quantizations

| Quant | Size | RAM target | Recommended For |
|-------|------|------------|-----------------|
| **Q3_K_M** | **54GB** | 64GB Mac | Compact |
| **Q4_K_M** | **68GB** | 96GB Mac | **Recommended (balance)** |
| **Q5_K_M** | **79GB** | 128GB Mac | Max quality |

> 119B total params → these are for **64GB+ Macs** (M-series Max/Ultra). The 6B active means inference is fast despite the size. IQ3/IQ4 (smaller, imatrix) can be added on request.

## RAM Requirements

| Your Mac RAM | Q3 (54GB) | Q4 (68GB) | Q5 (79GB) |
|---|---|---|---|
| 64GB | ✅ tight | ❌ | ❌ |
| 96GB | ✅ | ✅ | ❌ tight |
| 128GB | ✅ | ✅ | ✅ |
| 192GB+ | ✅ | ✅ | ✅ comfortable |

## Why Mistral Small 4?

- **One model, three jobs** — reasoning, multimodal understanding, and agentic coding unified (no model-switching).
- **6B active / 119B total MoE** — frontier-class capability at the inference speed/cost of a small model.
- **Apache 2.0** — no license friction, no gating. Build commercial products freely.
- **Native llama.cpp support** — Mistral ships official GGUF tooling; arch (`mistral3`) is mainstream.

## Why BatiAI Quantization?

- **Original-source** — quantized straight from Mistral's official weights, not a copy of a third-party GGUF.
- **BatiAI-signed** — `general.author: BatiAI`, `general.url: https://flow.bati.ai`.
- **Mac-tuned selection** — quant sizes chosen for real Apple Silicon RAM tiers.

## Technical Details

- **Original Model**: [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
- **Architecture**: `mistral3` MoE, 119B total / ~6B active per token
- **License**: Apache 2.0
- **Quantized with**: llama.cpp (Q8_0 intermediate → K-quants, `--allow-requantize`)
- **Quantized by**: [BatiAI](https://bati.ai)
- **Note**: YaRN config verified clean (no `yarn_log_multiplier` bug, unlike the earlier Medium 3.5 release).

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited. 60+ tools.

## License

Quantized from [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603). License: **Apache 2.0**.

## Benchmarks

<!-- BENCH-START -->
_Mac 하드웨어 실측 벤치 대기 중 (bench.sh). 측정 후 자동 갱신._
<!-- BENCH-END -->
