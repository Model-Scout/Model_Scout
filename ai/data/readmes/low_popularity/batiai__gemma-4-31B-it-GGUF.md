---
language:
  - en
  - ko
  - ja
  - zh
license: other
license_name: gemma
license_link: https://ai.google.dev/gemma/terms
tags:
  - gguf
  - gemma
  - gemma4
  - dense
  - quantized
  - imatrix
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - vision
  - multimodal
base_model: google/gemma-4-31B-it
pipeline_tag: text-generation
library_name: llama.cpp
---

# Gemma 4 31B-it GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/gemma4-31b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fgemma4--31b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/google/gemma-4-31B-it"><img src="https://img.shields.io/badge/Upstream-Gemma%204%2031B--it-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> Optimized GGUF quantizations of **google/gemma-4-31B-it** — Google's largest dense Gemma 4 model with native multilingual + vision capabilities.
> Built directly from official Google BF16 weights by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

Gemma 4 31B-it is a **dense** 31 B model (every parameter active per token) — different trade-off from 26B-A4B's MoE design (26 B total / 3.8 B active). Pick 31B for **deeper reasoning per query**, 26B-A4B for **higher throughput**.

## Quick Start

```bash
# 24 GB Mac — Smaller, imatrix-calibrated
ollama pull batiai/gemma4-31b:iq3

# 24 GB+ Mac — Imatrix 4-bit (recommended)
ollama pull batiai/gemma4-31b:iq4

# 32 GB+ Mac — Higher quality
ollama pull batiai/gemma4-31b:q4

# 36 GB+ Mac — Highest on-device quality
ollama pull batiai/gemma4-31b:q6
```

## Available Quantizations

| Tag | Quant | Recommended For |
|-----|-------|-----------------|
| `:iq3` | IQ3_M (imatrix) | 24 GB Mac, smaller footprint |
| `:iq4` | **IQ4_XS (imatrix)** | **24 GB+ Mac, recommended** |
| `:q4` | Q4_K_M | 32 GB+ Mac, higher quality |
| `:q6` | Q6_K | 36 GB+ Mac, near-lossless |

## Two modes — text-only by default, multimodal opt-in

Upstream Gemma 4 31B-it is **multimodal** (text + image + video understanding — but no audio; for audio see the smaller [E2B](https://huggingface.co/batiai/Gemma-4-E2B-it-GGUF) / [E4B](https://huggingface.co/batiai/Gemma-4-E4B-it-GGUF) variants). In the GGUF ecosystem this is delivered as **two files**: a main `model.gguf` (text tower) and a separate `mmproj.gguf` (multi-modal projector — the vision tower). We ship **both**, separate, so you can pick:

| | **Text-only** (default) | **Multimodal** (opt-in) |
|---|---|---|
| Files needed | main GGUF only | main GGUF **+** `mmproj-*.gguf` |
| Capabilities | Q&A, coding, tool calling, RAG, agents | + image / video understanding (OCR, captioning, visual reasoning) |
| `ollama pull` | ✅ single command | ⚠ Ollama mmproj integration is still rough — use llama.cpp directly |
| Disk / RAM | smaller (no vision weights) | larger (+ ~770 MB to ~1.2 GB) |
| Recommended for | most users (chat, code, agents) | OCR, image understanding |

### Multimodal usage (llama.cpp)

Download the main GGUF + the mmproj file:

```bash
# Pick a main model (text tower)
wget https://huggingface.co/batiai/Gemma-4-31B-it-GGUF/resolve/main/google-gemma-4-31B-it-IQ4_XS.gguf

# Pick the mmproj (vision tower) — Q6_K is the sweet spot, BF16 if you want zero loss
wget https://huggingface.co/batiai/Gemma-4-31B-it-GGUF/resolve/main/mmproj-Q6_K.gguf
```

**Server mode (OpenAI-compatible Vision API):**

```bash
llama-server \
  -m google-gemma-4-31B-it-IQ4_XS.gguf \
  --mmproj mmproj-Q6_K.gguf \
  -c 32768 --host 127.0.0.1 --port 8080

curl http://127.0.0.1:8080/v1/chat/completions -d '{
  "messages": [{
    "role": "user",
    "content": [
      {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}},
      {"type": "text", "text": "What does this screenshot show?"}
    ]
  }]
}'
```

**One-shot CLI:**

```bash
llama-mtmd-cli \
  -m google-gemma-4-31B-it-IQ4_XS.gguf \
  --mmproj mmproj-Q6_K.gguf \
  --image ~/Desktop/photo.jpg \
  -p "describe this image"
```

### mmproj quantizations available

| File | Quant | Size | When to use |
|------|-------|------|-------------|
| `mmproj-Q6_K.gguf` | Q6_K | ~770 MB | balanced (recommended) |
| `mmproj-BF16.gguf` | BF16 | ~1.2 GB | absolute zero quantization loss for vision |

(Q8_0 not available because some vision tensors have shapes incompatible with Q8_0's column alignment — applies to every quantizer of this model. Q6_K's K-quant block layout handles them.)

## Dense vs MoE — when to pick 31B vs 26B-A4B?

| | **31B-it (dense)** | 26B-A4B-it (MoE) |
|---|---|---|
| Active params / token | 31 B (all) | 3.8 B (8 experts of 32) |
| Throughput | slower (more compute per token) | **faster** |
| Reasoning depth | **better** (denser computation) | good |
| Memory at IQ4 | ~17 GB | ~13 GB |
| Best for | hard reasoning / single-thread workloads | high-throughput / agents / streaming chat |

Use **31B for quality-per-token**, **26B-A4B for tokens-per-second**.

## Why BatiAI?

| | BatiAI | Third-party (unsloth, etc.) |
|---|---|---|
| **Source** | Quantized directly from [official Google weights](https://huggingface.co/google/gemma-4-31B-it) | Often re-quantized from other GGUFs |
| **Compatibility** | ✅ Verified on Ollama 0.20+ | ❌ Known issues with Ollama 0.20+ |
| **Tested on** | Real Mac mini M4 + MacBook Pro M4 Max | Often untested |
| **Tool calling** | ✅ Verified with BatiFlow's 57 tool functions | Often broken |
| **Korean** | ✅ Validated | Not tested |
| **Multimodal** | ✅ Vision mmproj available (this repo) | Often missing |
| **Signing** | `general.author: BatiAI` for provenance | Varies |

## About BatiFlow

<p align="center">
  <a href="https://flow.bati.ai"><strong>flow.bati.ai</strong></a>
</p>

[BatiFlow](https://flow.bati.ai) is a **macOS-native AI desktop automation app** — just 5 MB, built with Swift.

- **Free & Unlimited** — On-device AI via Ollama, no API costs
- **100 % Private** — All data stays on your Mac
- **Ultra Lightweight** — Native macOS app, only 5 MB
- **57 built-in tools** — calendar, notes, reminders, files, email, browser, messaging, and more

## Related models in the BatiAI Gemma 4 lineup

| Model | Modalities | Min RAM | Repo |
|-------|------------|--------:|------|
| Gemma 4 E2B-it | text + image + audio | 8 GB | [batiai/Gemma-4-E2B-it-GGUF](https://huggingface.co/batiai/Gemma-4-E2B-it-GGUF) |
| Gemma 4 E4B-it | text + image + audio | 8 GB | [batiai/Gemma-4-E4B-it-GGUF](https://huggingface.co/batiai/Gemma-4-E4B-it-GGUF) |
| Gemma 4 26B-A4B-it | text + image / video (MoE) | 24 GB | [batiai/Gemma-4-26B-A4B-it-GGUF](https://huggingface.co/batiai/Gemma-4-26B-A4B-it-GGUF) |
| **Gemma 4 31B-it** | **text + image / video (dense)** | **24 GB** | **this repo** |

## Technical Details

- **Original Model**: [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)
- **Architecture**: Gemma 4 dense (31 B parameters, all active per token)
- **Modalities**: Text (primary) + Image / Video via opt-in mmproj. Audio not supported (use E2B / E4B for audio)
- **Context Window**: 128 K tokens
- **License**: Gemma
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp)
- **Quantized by**: [BatiAI](https://bati.ai)
- **GGUF metadata**: `general.author: BatiAI`, `general.url: https://flow.bati.ai`

## License

Mirrors the upstream **Gemma** license. Commercial use permitted per Google's [Gemma terms](https://ai.google.dev/gemma/terms).

BatiAI's quantization pipeline is provided under MIT.
