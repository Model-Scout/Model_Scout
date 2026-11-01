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
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - vision
  - audio
  - multimodal
base_model: google/gemma-4-E2B-it
pipeline_tag: text-generation
library_name: llama.cpp
---

# Gemma 4 E2B-it GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/gemma4-e2b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fgemma4--e2b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/google/gemma-4-E2B-it"><img src="https://img.shields.io/badge/Upstream-Gemma%204%20E2B--it-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> Optimized GGUF quantizations of **google/gemma-4-E2B-it** — Google's tiniest fully-multimodal Gemma 4 (text + image + **audio**) for on-device AI on Mac.
> Built directly from official Google BF16 weights by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

The "E" stands for **Edge**. Tiny enough to run on basically any Mac (8 GB+) while still understanding speech and images alongside text — the only Gemma 4 size with audio support shared with E4B.

## Quick Start

```bash
# Recommended
ollama pull batiai/gemma4-e2b:q4

# Higher quality
ollama pull batiai/gemma4-e2b:q6
```

## Available Quantizations

| Tag | Quant | Size | Recommended For |
|-----|-------|------|-----------------|
| `:q4` | **Q4_K_M** | **~2.1 GB** | **balanced (recommended default)** |
| `:q6` | Q6_K | ~2.8 GB | higher quality, near-lossless |

Sub-3 B models stay sharp at Q4 — quantization noise is tiny relative to model capacity.

## Two modes — text-only by default, multimodal opt-in

Upstream Gemma 4 E2B-it is **fully multimodal** — text + image + audio in one model. In the GGUF ecosystem this is delivered as **two files**: a main `model.gguf` (text tower) and a separate `mmproj.gguf` that holds **both vision and audio encoders together** (a single 1411-tensor projector covering image and speech input).

| | **Text-only** (default) | **Multimodal** (opt-in) |
|---|---|---|
| Files needed | main GGUF only | main GGUF **+** `mmproj-BF16.gguf` |
| Capabilities | Q&A, coding, tool calling, agents | + image (OCR, captioning, visual reasoning) + audio (speech understanding) |
| `ollama pull` | ✅ single command | ⚠ Ollama mmproj integration is still rough — use llama.cpp directly |
| Disk / RAM | smaller (no projector weights) | larger (+ ~940 MB) |
| Recommended for | most users (chat, code, agents) | OCR, image / speech understanding |

### Multimodal usage (llama.cpp)

```bash
# Pick a main model (text tower)
wget https://huggingface.co/batiai/Gemma-4-E2B-it-GGUF/resolve/main/google-gemma-4-E2B-it-Q4_K_M.gguf

# Get the multimodal projector (vision + audio in one file)
wget https://huggingface.co/batiai/Gemma-4-E2B-it-GGUF/resolve/main/mmproj-BF16.gguf
```

**Server mode (image input via OpenAI-compatible Vision API):**

```bash
llama-server \
  -m google-gemma-4-E2B-it-Q4_K_M.gguf \
  --mmproj mmproj-BF16.gguf \
  -c 32768 --host 127.0.0.1 --port 8080

curl http://127.0.0.1:8080/v1/chat/completions -d '{
  "messages": [{
    "role": "user",
    "content": [
      {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}},
      {"type": "text", "text": "What does this show?"}
    ]
  }]
}'
```

**One-shot CLI with image:**

```bash
llama-mtmd-cli \
  -m google-gemma-4-E2B-it-Q4_K_M.gguf \
  --mmproj mmproj-BF16.gguf \
  --image ~/Desktop/photo.jpg \
  -p "describe this image"
```

**One-shot CLI with audio:**

```bash
llama-mtmd-cli \
  -m google-gemma-4-E2B-it-Q4_K_M.gguf \
  --mmproj mmproj-BF16.gguf \
  --audio ~/Downloads/voice.wav \
  -p "transcribe and summarize"
```

### mmproj quantization

| File | Quant | Size | Why this only? |
|------|-------|------|---------------|
| `mmproj-BF16.gguf` | BF16 | ~940 MB | The vision + audio projector tensors don't satisfy K-quant block-alignment requirements (108+ tensors require fallback), so Q6_K reliably aborts on this combined projector. **BF16 is the only safe choice today** — applies to every quantizer of this model. The main text GGUF is unaffected. |

## Why E series (E2B / E4B) vs 26B / 31B?

| | E2B / E4B | 26B-A4B / 31B |
|---|---|---|
| Audio support | ✅ | ❌ (vision only) |
| Min RAM | 8 GB+ | 24 GB+ |
| Speed | very fast (small) | slower (larger) |
| Reasoning depth | lower | higher |
| Use case | edge / mobile-class Mac / voice + image | desktop chat + agents |

If you need **voice + image + text in one model on a small Mac**, E series is the only Gemma 4 option.

## Why BatiAI?

| | BatiAI | Third-party (unsloth, etc.) |
|---|---|---|
| **Source** | Quantized directly from [official Google weights](https://huggingface.co/google/gemma-4-E2B-it) | Often re-quantized from other GGUFs |
| **Compatibility** | ✅ Verified on Ollama 0.20+ | ❌ Known issues with Ollama 0.20+ |
| **Tested on** | Real Mac mini M4 (16 GB) + MacBook Pro M4 Max | Often untested |
| **Tool calling** | ✅ Verified with BatiFlow's 57 tool functions | Often broken |
| **Korean** | ✅ Validated | Not tested |
| **Multimodal** | ✅ Vision + audio mmproj available | Often missing |
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
| **Gemma 4 E2B-it** | text + image + audio | 8 GB | **this repo** |
| Gemma 4 E4B-it | text + image + audio | 8 GB | [batiai/Gemma-4-E4B-it-GGUF](https://huggingface.co/batiai/Gemma-4-E4B-it-GGUF) |
| Gemma 4 26B-A4B-it | text + image / video (no audio) | 24 GB | [batiai/Gemma-4-26B-A4B-it-GGUF](https://huggingface.co/batiai/Gemma-4-26B-A4B-it-GGUF) |
| Gemma 4 31B-it | text + image / video (no audio) | 24 GB | [batiai/Gemma-4-31B-it-GGUF](https://huggingface.co/batiai/Gemma-4-31B-it-GGUF) |

## Technical Details

- **Original Model**: [google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)
- **Architecture**: Gemma 4 (Edge variant)
- **Modalities**: Text (primary) + Image + Audio (via opt-in mmproj)
- **License**: Gemma (commercial use permitted under terms)
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp)
- **Quantized by**: [BatiAI](https://bati.ai)
- **GGUF metadata**: `general.author: BatiAI`, `general.url: https://flow.bati.ai`

## License

Mirrors the upstream **Gemma** license. Commercial use permitted per Google's [Gemma terms](https://ai.google.dev/gemma/terms).

BatiAI's quantization pipeline is provided under MIT.
