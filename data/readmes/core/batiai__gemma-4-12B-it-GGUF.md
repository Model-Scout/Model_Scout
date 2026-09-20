---
language:
  - en
  - ko
  - ja
  - zh
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
tags:
  - gguf
  - gemma
  - gemma4
  - quantized
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - multimodal
  - vision
  - audio
  - video
  - encoder-free
base_model: google/gemma-4-12B-it
pipeline_tag: image-text-to-text
library_name: llama.cpp
---

# Gemma 4 12B-it GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/gemma4-12b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fgemma4--12b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/google/gemma-4-12B-it"><img src="https://img.shields.io/badge/Upstream-Gemma%204%2012B--it-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> Optimized GGUF quantizations of **google/gemma-4-12B-it** — Google DeepMind's encoder-free multimodal model (text + image + **audio** + **video**) that runs on a 16 GB Mac.
> Built directly from official Google BF16 weights by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai).

## Why Gemma 4 12B?

- **26B-MoE-class quality at <half the memory** — Google's release notes put the 12B near the Gemma 4 26B MoE on standard benchmarks
- **Encoder-free multimodal** — first mid-sized model with **native audio**. Raw image patches and audio waveforms project directly into the LLM via lightweight linear layers — no separate vision/audio encoder
- **Strong vision + reasoning**: DocVQA 94.9 · InfoVQA 88.4 · MMMU-Pro 69.1 · AIME 2026 77.5 · MATH-Vision 79.7
- **256K context**, **140+ languages**
- **Apache 2.0** — commercial-friendly
- **Released June 3, 2026**

## Quick Start

```bash
ollama pull batiai/gemma4-12b:q4
```

## Available Quantizations

| Quant | Size | Recommended For |
|-------|------|-----------------|
| **Q2_K_S** | ~4.2 GB | 8GB Mac, ultra-compact (imatrix) |
| **IQ3_XXS** | ~4.6 GB | imatrix, smallest |
| **Q3_K_M** | ~5.7 GB | 8GB+ Mac, balanced |
| **IQ4_XS** | ~6.2 GB | imatrix, best size/quality |
| **Q4_K_M** | ~6.9 GB | **16GB Mac (recommended)** |
| **Q6_K** | ~9.2 GB | near-original quality |

> **Mac note on `Q3_K_M`:** in every model we've benchmarked on Apple Silicon, Q3_K_M generated
> *slower* than Q4_K_M despite the smaller file — Granite 4.1 (+27%), Gemma 4 26B (+12%),
> Qwen3.8‑27B (+18%), Qwen3.6‑27B (+8%), on both M4 Max and M4 mini. Metal's Q3_K path is limited by
> dequantization compute rather than bandwidth. We have not measured this particular model's
> Q3/Q4 pair yet, so treat it as a strong prior, not a measurement: **if Q4_K_M fits, take it.**
> On CUDA the two are effectively tied, so this applies to Macs only.

*IQ variants use imatrix calibration. Q2/Q3 (8GB Macs) are not in Google's reference set — BatiAI adds them.*

## Two modes — text-only by default, multimodal opt-in

Upstream Gemma 4 12B-it is multimodal. In the GGUF ecosystem this is delivered as **two files**: a main model GGUF (the LLM) and a small `mmproj` GGUF holding the **vision + audio projectors together** (encoder-free → the projector is tiny, ~167 MB, and one BF16 mmproj works with every quant).

**What actually works locally** (verified on M4 Max 128GB):

| Modality | Status | How |
|---|---|---|
| **Text** | ✅ | Ollama or llama.cpp. ~45 tok/s (q4, M4 Max) |
| **Image** (OCR, captioning, visual reasoning) | ✅ | `llama-server` + mmproj — verified (Korean screenshot OCR, ~13 s/image) |
| **Audio** (speech understanding, ≤30s) | ✅ *experimental* | `llama-server` + mmproj — verified (Korean call STT). `init_audio` flags reduced quality |
| **Video** (≤60s) | ❌ | Model supports it, but **llama.cpp has no gemma4 video projector yet** — image+audio only for now |

> ⚠️ **Ollama can't do images/audio for Gemma 4 yet** (0.20 doesn't know the `gemma4uv`/`gemma4ua` projectors). Multimodal needs **`llama-server` built from a recent llama.cpp master** that includes the Gemma 4 projectors (the `gemma4v/gemma4uv/gemma4a/gemma4ua` clip graphs). Older builds fail with `unknown projector type: gemma4uv`.

```bash
# Multimodal via llama-server (recent llama.cpp master + --jinja required)
llama-server -m gemma-4-12B-it-Q4_K_M.gguf \
  --mmproj mmproj-google-gemma-4-12B-it-BF16.gguf \
  --host 127.0.0.1 --port 8899 -ngl 99 -c 8192 --jinja
# → GET /props returns {"vision": true, "audio": true}; POST /v1/chat/completions with image_url / input_audio
```
*Gemma 4 12B is a reasoning model — give it enough `max_tokens` (image descriptions emit 700+ tokens incl. a thinking block; the answer arrives in `reasoning_content` + `content`).*

## RAM Requirements

| Your Mac RAM | Q2 | IQ3 | Q3 | IQ4 | Q4 | Q6 |
|-------------|-----|-----|-----|-----|-----|-----|
| **8GB** | ✅ | ✅ | ✅ tight | ⚠️ | ❌ | ❌ |
| **16GB** | ✅ | ✅ | ✅ | ✅ | **✅ Recommended** | ✅ |
| **24GB+** | ✅ | ✅ | ✅ | ✅ | ✅ | **✅** |

## Why BatiAI Quantization?

| | BatiAI | Third-party |
|---|---|---|
| **Source** | [Official Google weights](https://huggingface.co/google/gemma-4-12B-it) | Re-quantized |
| **imatrix** | ✅ IQ variants calibrated | varies |
| **Low quants** | ✅ Q2/Q3 for 8GB Macs | often Q4 floor |
| **mmproj (vision+audio)** | ✅ included | often text-only |
| **Tool calling** | ✅ Verified | often untested |
| **BatiAI signed** | ✅ `general.author=BatiAI` | — |

## Technical Details

- **Original Model**: [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)
- **Architecture**: `gemma4_unified` — encoder-free unified multimodal, 12B dense, 48 layers, 256K context
- **Modalities**: text + image + audio (≤30s) + video (≤60s)
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) + imatrix
- **Quantized by**: [BatiAI](https://bati.ai)

## File checksums (SHA-256)

| File | SHA-256 |
|------|---------|
| `google-gemma-4-12B-it-Q2_K_S.gguf` | `fd0c02b4d06272127e10eaedcdf240535317bb13fabbd4c63d52b8929f18f99c` |
| `google-gemma-4-12B-it-IQ3_XXS.gguf` | `21a4aaeadc6b17a4e9e168034f65f641f13f122f88b24b50776835dc02b84f7f` |
| `google-gemma-4-12B-it-Q3_K_M.gguf` | `f3f3549c7e1389452cd8df63db58156e3a66555fcd5047150c8d78ca48c459b6` |
| `google-gemma-4-12B-it-IQ4_XS.gguf` | `63d7370e4de1aba0cb7dd04382e4e52c6803eb8dd276f016367f144bae78eed8` |
| `google-gemma-4-12B-it-Q4_K_M.gguf` | `e6db34561a77012484641bf35cb14b09a8ef15dbeaecb29cf3939e66e3a6dbad` |
| `google-gemma-4-12B-it-Q6_K.gguf` | `36f399a3348a001ffc13b61ac6951a5028ca63f8889f99ad56f4d98210bc8a9f` |
| `mmproj-google-gemma-4-12B-it-BF16.gguf` | `4aa2bb56fc57d0b7d27d3ea77a0df1c424f7968011d9b4a581bf8ecda8857139` |

```bash
shasum -a 256 google-gemma-4-12B-it-Q4_K_M.gguf   # verify after download
```

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, on-device AI automation for Mac. 5MB app, 100% local, unlimited.

## License

Quantized from [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it). License: **Apache 2.0**.

## Benchmarks

<!-- BENCH-START -->

**Text** (`ollama run --verbose`, thinking ON default):

| Machine | Quant | Load | Warm gen | Prompt eval | Long resp | Cold 1st gen | Ollama RAM | Korean | Tool-call |
|---|---|---:|---:|---:|---:|---:|---:|:---:|:---:|
| **M4 Max** 128 GB | **Q4_K_M** | 2.8 s | **45.1 t/s** | 536 t/s | 22.7 t/s | 54.5 t/s | 16 GB | ✅ | ✅ |
| **M4 Max** 128 GB | **Q6_K** | 7.1 s | **38.9 t/s** | 506 t/s | 16.2 t/s | 43.2 t/s | 18 GB | ✅ | ✅ |

**Multimodal** (`llama-server` static [commit 308f61c](https://huggingface.co/batiai/llamacpp-server-macos) + Q4_K_M + mmproj, M4 Max 128GB — measured):

| Input | Latency | Throughput | Note |
|---|---:|---:|---|
| Cold start (incl. mmproj) | 2–6 s | — | mmproj worst-case ~359 MiB |
| Image (screenshot → full Korean analysis) | ~22 s | 42 t/s gen, 949 tok | OCR + visual reasoning, accurate |
| Audio (10 s clip → Korean STT) | ~23 s | RTF ~2.3 | speech transcription, *experimental* |

`/props` → `{"vision": true, "audio": true}`. Gemma 4 is a reasoning model — responses include a `<think>` block, so give generous `max_tokens`. Video not supported (no gemma4 video projector in llama.cpp).

<!-- BENCH-END -->
