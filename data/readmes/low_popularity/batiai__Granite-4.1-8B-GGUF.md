---
language:
  - en
  - ko
  - ja
  - zh
license: apache-2.0
tags:
  - gguf
  - granite
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - 8b
  - dense
  - enterprise
  - tool-calling
base_model: ibm-granite/granite-4.1-8b
pipeline_tag: text-generation
library_name: llama.cpp
---

# IBM Granite 4.1 8B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/granite4.1"><img src="https://img.shields.io/badge/Ollama-batiai%2Fgranite4.1-green?style=for-the-badge" alt="Ollama"></a>
</p>

> Quantizations of **IBM Granite 4.1 8B** (Dense, Apache 2.0, enterprise-grade) for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Why Granite 4.1 8B?

- **8B Dense beats 32B-A9B MoE** — IBM's tighter post-training pipeline matches/exceeds Granite 4.0-H-Small (4× larger MoE) across IFEval, AlpacaEval, MMLU-Pro, BBH, GSM8K, BFCL V3, MBPP+
- **15T tokens** training, 512K context extension
- **Strong tool calling** (BFCL V3: 68.3) and instruction following (ArenaHard: 69.0)
- **Apache 2.0** — true commercial-friendly, no use restrictions
- **Released April 29, 2026**

## Quick Start

```bash
ollama pull batiai/granite4.1:q4
```

## Available Quantizations

| Quant | Size | VRAM target | Recommended For |
|-------|------|-------------|-----------------|
| **Q3_K_M** | **~4.5GB** | ~6GB | 8GB+ Mac |
| **Q4_K_M** | **~5GB** | ~7GB | **16GB Mac (recommended)** |
| **Q5_K_M** | **~6GB** | ~8GB | 16GB+ Mac (higher quality) |
| **Q6_K** | **~7GB** | ~9GB | 24GB+ Mac (max quality) |

## RAM Requirements

| Your Mac RAM | Q3 (4.5GB) | Q4 (5GB) | Q5 (6GB) | Q6 (7GB) |
|-------------|-----------|---------|---------|---------|
| **8GB** | **✅ Tight** | ⚠️ | ❌ | ❌ |
| **16GB** | ✅ | **✅ Recommended** | ✅ | ⚠️ |
| **24GB+** | ✅ | ✅ | ✅ | **✅** |

## Why an 8B Dense?

Granite 4.1's 8B Dense model is built for enterprise: predictable latency, simple deployment, no MoE routing overhead. IBM's improved post-training (SFT + RL alignment) yields tool-calling and chat quality competitive with much larger models.

## Granite 4.1 vs Other 8B Models

| Model | Architecture | Tool Call (BFCL) | License |
|-------|-------------|------------------|---------|
| **Granite 4.1 8B** | Dense | 68.3 | **Apache 2.0** |
| Qwen 3.5 9B | Dense | — | Apache 2.0 |
| Llama 3.3 8B | Dense | ~63 | Llama License |

## Why BatiAI Quantization?

| | BatiAI | Third-party |
|---|---|---|
| **Source** | [Official IBM weights](https://huggingface.co/ibm-granite/granite-4.1-8b) | Re-quantized GGUFs |
| **imatrix** | ✅ wikitext-2 200 chunks | Standard |
| **Tool Calling** | ✅ Verified | Often untested |
| **BatiAI signed** | ✅ | — |

## Technical Details

- **Original Model**: [ibm-granite/granite-4.1-8b](https://huggingface.co/ibm-granite/granite-4.1-8b)
- **Architecture**: Dense decoder-only, 8B params
- **Training**: 15T tokens, multi-stage with 512K long-context extension
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) + imatrix
- **Quantized by**: [BatiAI](https://bati.ai)

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited.

## License

Quantized from [ibm-granite/granite-4.1-8b](https://huggingface.co/ibm-granite/granite-4.1-8b). License: **Apache 2.0**.

## Benchmarks

<!-- BENCH-START -->

| Machine | Quant | Cold start | Prompt eval | Token gen | Tested |
|---------|-------|------------|-------------|-----------|--------|
| Mac mini M4 16GB | IQ3_XXS | 2.156s | 45.74 t/s | 6.66 t/s | 2026-05-03 |
| Mac mini M4 16GB | IQ4_XS | 5.439s | 108.35 t/s | 15.55 t/s | 2026-05-03 |
| Mac mini M4 16GB | Q3_K_M | 4.97s | 90.12 t/s | 12.84 t/s | 2026-05-03 |
| Mac mini M4 16GB | Q4_K_M | 5.698s | 98.99 t/s | 14.26 t/s | 2026-05-03 |
| Mac mini M4 16GB | Q5_K_M | 6.517s | 84.44 t/s | 12.21 t/s | 2026-05-03 |
| Mac mini M4 16GB | Q6_K | 6.964s | 73.76 t/s | 10.49 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | IQ3_XXS | 2.265s | 514.87 t/s | 75.08 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | IQ4_XS | 3.44s | 542.74 t/s | 77.79 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q3_K_M | 2.186s | 420.42 t/s | 60.75 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q4_K_M | 2.184s | 529.1 t/s | 77.44 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q5_K_M | 2.18s | 410.75 t/s | 57.52 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q6_K | 3.72s | 424.95 t/s | 60.27 t/s | 2026-05-03 |

<!-- BENCH-END -->
