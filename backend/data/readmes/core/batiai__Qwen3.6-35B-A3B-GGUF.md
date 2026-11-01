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
  - qwen3.6
  - moe
  - quantized
  - imatrix
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - agentic
  - coding
base_model: Qwen/Qwen3.6-35B-A3B
pipeline_tag: text-generation
library_name: llama.cpp
---

# Qwen 3.6 35B-A3B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3.6-35b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3.6--35b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B"><img src="https://img.shields.io/badge/Upstream-Qwen3.6--35B--A3B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> **"Agentic Coding Power, Now Open to All"** — imatrix-calibrated GGUF quantizations of **Qwen/Qwen3.6-35B-A3B** (text-only) for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai) — free, unlimited, on-device AI automation.

Released by Alibaba on **April 15, 2026** as the successor to Qwen 3.5 35B-A3B, with substantial upgrades in **agentic coding**, **frontend workflows**, **repository-level reasoning**, and **thinking preservation** for iterative development.

## 🎬 See it in action — Qwen 3.6 + BatiFlow demo (55s)

![BatiFlow + Qwen 3.6 35B-A3B demo on M4 Max](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF/resolve/main/assets/qwen3.6-35b-batiflow-demo.gif)

55 seconds of real on-device inference on a MacBook Pro M4 Max — **100 % local, no cloud, no API keys**. Three scenarios in one continuous take:

1. **Real-time Q&A** — *"Give me 5 quick tips for writing professional emails."* → markdown-rendered streaming response at ~46 t/s. You can see tokens generated faster than you can read them.
2. **Code generation + file-system tools** — *"Write a Python function to extract emails from text."* → syntax-highlighted code → suggestion: *"save this code to a file"* → *"show the file in Finder"* → file appears in macOS Finder. The model is **calling Mac tools** (write file, reveal in Finder) directly from the conversation.
3. **Calendar integration** — *"Show me today's schedule."* → live macOS Calendar query → conversational event addition. Same conversation, multiple tool invocations.

**Why this matters**: the same Qwen 3.6 model that generates the answer is also driving **function calls** (file system, Calendar) on your Mac in real time. Through [**BatiFlow**](https://flow.bati.ai) — a 5 MB native macOS app — non-developers get one-click access to this entire pipeline. No code, no API keys, no cloud, no monthly subscription.

## Quick Start

```bash
# 16–24GB Mac
ollama pull batiai/qwen3.6-35b:iq3

# 24GB+ Mac (recommended)
ollama pull batiai/qwen3.6-35b:iq4

# 36GB+ Mac (highest quality on-device)
ollama pull batiai/qwen3.6-35b:q6

ollama run batiai/qwen3.6-35b:iq4
```

Aliases `:q3` / `:q4` point to the same blobs as `:iq3` / `:iq4`.

**Tool calling**: these GGUFs ship with a ChatML + `{{ .Tools }}` Modelfile template so Ollama reports `tools` and `thinking` capabilities. When calling tools, pass `"think": false` in your chat request (otherwise the model spends tokens on the `<think>` block before emitting the `<tool_call>`).

## Available Quantizations

Full Q2–Q8 spectrum. **imatrix is applied to every low/mid-bit quant** (IQ and Q4/Q5 K-quants) using wikitext-2-raw calibration — consistent quality recipe across the lineup.

| Tag (Ollama) | Quant | File Size | Min RAM | Recommended For |
|-----|-------|-----------|---------|-----------------|
| `:iq3` / `:q3` | **IQ3_XXS** (imatrix) | **13 GB** | 16 GB | Mac mini / MacBook Air 16 GB |
| `:iq4` / `:q4` | **IQ4_XS** (imatrix) | **18 GB** | 24 GB | MacBook Pro / Mac Studio 24 GB+ |
| HF-only | **Q4_K_M** (imatrix) | **20 GB** | 32 GB | K-quant alternative to IQ4 |
| HF-only | **Q5_K_M** (imatrix) | **24 GB** | 32 GB | 32 GB Mac sweet spot — IQ4/Q6 gap-filler |
| `:q6`          | **Q6_K**    (K-quant) | **27 GB** | 36 GB | MacBook Pro M4 Pro / Studio — near-lossless |
| HF-only | **Q8_0**    (K-quant) | **35 GB** | 48 GB | Quality ceiling / 64 GB Mac / benchmark reference |

`:iq3` / `:iq4` / `:q6` tags are published on Ollama. **Q4_K_M / Q5_K_M / Q8_0 are available on Hugging Face only** — Ollama lineup kept lean intentionally; pull via `huggingface-cli` or `wget` for these.

**Also included on Hugging Face:**
- `mmproj-Q6_K.gguf` (579 MB) / `mmproj-BF16.gguf` (861 MB) — vision projector (see [Two modes](#two-modes--text-only-by-default-multimodal-opt-in))
- `imatrix.dat` (184 MB) — our importance-matrix calibration data; use it to roll your own quants from the upstream BF16

## Why Qwen 3.6 35B-A3B?

Upstream headline: _"Agentic Coding Power, Now Open to All"_ — the model is tuned for multi-step coding agents, long-horizon repo reasoning, and tool use.

### Benchmarks (official Qwen BF16 figures)

**Coding & Agentic**

| Benchmark | Qwen 3.6-35B-A3B | Qwen 3.5-35B-A3B | Gemma 4-31B |
|---|---:|---:|---:|
| SWE-bench Verified | **73.4** | 70.0 | 52.0 |
| SWE-bench Multilingual | **67.2** | — | 51.7 |
| SWE-bench Pro | **49.5** | — | 35.7 |
| Terminal-Bench 2.0 | **51.5** | 40.5 | 42.9 |
| QwenWebBench | **1397** | 978 | — |

**Math & Reasoning**

| Benchmark | Qwen 3.6-35B-A3B | Gemma 4-31B |
|---|---:|---:|
| AIME26 | **92.7** | 89.2 |
| GPQA | **86.0** | — |
| HMMT Feb 26 | **83.6** | — |
| HLE | **21.4** | — |
| LiveCodeBench v6 | **80.4** | — |

**General Knowledge**

| Benchmark | Qwen 3.6-35B-A3B |
|---|---:|
| MMLU-Pro | 85.2 |
| MMLU-Redux | 93.3 |
| SuperGPQA | 64.7 |
| C-Eval | 90.0 |

**Agent / Tool Use**

| Benchmark | Qwen 3.6-35B-A3B |
|---|---:|
| TAU3-Bench | 67.2 |
| MCP-Atlas | 62.8 |
| WideSearch | 60.1 |
| MCPMark | 37.0 |
| Tool Decathlon | 26.9 |

### Key takeaways

- **SWE-bench Verified jumps +3.4** over Qwen 3.5 to **73.4** — top-tier agentic-coding among open models
- **Terminal-Bench 2.0 +11.0** over 3.5 → genuine real-world command-line competence
- **QwenWebBench 1397** vs 978 for 3.5 — a **43% jump** in agentic web tasks
- **Beats Gemma 4-31B on every published coding & reasoning benchmark** despite Gemma being a similar-sized dense model (A3B only activates 3B params per token)

_Note: these are upstream BF16 figures. IQ3_XXS / IQ4_XS quantization may cost a few points on the hardest benchmarks — post your own bench results and we'll update this card._

## MoE Advantage

| | 35B-A3B (MoE) | 27B (Dense) |
|---|---|---|
| Total params | 35B | 27B |
| **Active params / token** | **3B** | **27B** |
| Experts | 256 (8 routed + 1 shared) | — |
| Typical VRAM (IQ4) | ~23 GB | ~28 GB |
| Relative speed | **Faster** | Baseline |

Only 9 of 256 experts fire per token — same reasoning capacity, far less compute.

## RAM Requirements (on-device)

| Your Mac RAM | IQ3 (13 GB) | IQ4 (18 GB) |
|--------------|-------------|-------------|
| 16 GB        | ✅ fits (tight, swap-bound — single-turn only) | ❌ |
| 24 GB        | ✅ comfortable  | ✅ fits (tight) |
| 48 GB        | ✅              | ✅ fits — close other apps for headroom |
| 64 GB+       | ✅              | ✅ comfortable  |
| 128 GB       | ✅              | ✅ ideal        |

## On-device Benchmarks (measured)

Measured with BatiAI's bench harness on real Apple Silicon.

### Apple Silicon (100 % GPU, warm avg over 3 runs)

| Hardware | Quant | Gen (warm) | Prompt eval | Long resp (300 t) | Cold 1st gen | Load | Ollama RAM | Korean |
|---|---|---:|---:|---:|---:|---:|---:|:---:|
| **M4 Max** 128 GB | IQ3_XXS | **45.9 t/s** | 104.9 t/s | 45.2 t/s | 49.7 t/s | 3.0 s | 18 GB | ✅ |
| **M4 Max** 128 GB | IQ4_XS  | **46.5 t/s** | 105.0 t/s | 45.6 t/s | 51.3 t/s | 5.3 s | 23 GB | ✅ |
| **M4 Pro** 48 GB  | IQ3_XXS | **31.1 t/s** | 125.0 t/s | 30.2 t/s | 30.6 t/s | 7.8 s | 17 GB | ✅ |
| **M4 Pro** 48 GB  | IQ4_XS  | **32.3 t/s** | 143.6 t/s | 30.5 t/s | 33.8 t/s | 7.4 s | 22 GB | ✅ |

**Tool calling**: all tags support the Ollama `tools` + `thinking` capabilities. Qwen 3.6 is a thinking model by default — for fast, clean tool-call JSON, pass `"think": false` in your chat request. See the [Quick Start](#quick-start) section above.

### Mac mini M4 (16 GB RAM) — community-reported

| Model | Gen speed |
|-------|----------:|
| **IQ3_XXS** | ~2 – 3 t/s |
| IQ4_XS | ❌ does not fit (needs 24 GB+) |

IQ3 fits in 16 GB but exercises swap — usable for single-turn prompts but not for streaming chat.

### Key take-aways (Mac)

- **IQ3 ≈ IQ4 in speed across Mac tiers** — ~1 % apart on M4 Max, ~4 % on M4 Pro 48 GB. The MoE + Gated DeltaNet architecture is memory-bandwidth-bound, not compute-bound, so raising the bit-width does not buy throughput.
- **~1.75× faster than Qwen 3.5-35B-A3B IQ4** on the same M4 Max (46.5 vs 26.6 t/s measured previously).
- **M4 Max vs M4 Pro 48 GB**: M4 Max delivers ~45 % higher warm throughput (46.5 vs 32.3 t/s on IQ4) — consistent with its higher memory bandwidth. M4 Pro is noticeably snappier on prompt eval at IQ4 (143.6 vs 105 t/s) — likely cache / thermal behaviour.
- Both quants run 100 % on Apple Silicon GPU / Metal. No CPU fallback on machines that fit.
- Prompt evaluation is fast on every tested Mac (105–144 t/s) — long-context RAG / agent flows feel responsive.
- Tool calling works on every tag — remember to pass `"think": false` in the chat request if you don't want the model to spend its token budget on reasoning first.

## Reference — Server baseline (non-Mac, for context)

Not our target platform, but useful as an implementation-quality ceiling. Same Ollama binary, same GGUFs, **2× NVIDIA RTX 6000 Ada (96 GB total VRAM)** on Linux.

| Metric                 | IQ3_XXS | IQ4_XS | Q6_K |
|------------------------|--------:|-------:|-----:|
| **Gen speed (warm)**   | **133.0 t/s** | **115.4 t/s** | **112.3 t/s** |
| Gen range (3 runs)     | 123.9 – 140.3 | 114.0 – 117.6 | 111.5 – 113.3 |
| Prompt eval            | 721.7 t/s | 666.1 t/s | 515.9 t/s |
| Long response (~300 t) | 123.8 t/s | 120.2 t/s | 111.3 t/s |
| Cold-start first gen   | 111.2 t/s | 100.5 t/s | 106.3 t/s |
| Load time              | 4.0 s | 10.6 s | 14.5 s |
| Ollama VRAM (w/ KV)    | 18 GB | 23 GB | 33 GB |
| Korean generation      | ✅ | ✅ | ✅ |

**Mac ↔ Server comparison** (same GGUF files):
- Mac M4 Max reaches **~35–40 %** of the server's warm throughput despite the server having 97× the power budget.
- Prompt eval: M4 Max 105 t/s vs Server 666 t/s → **Mac is bound by memory bandwidth, not compute** — consistent with our "memory-bandwidth-bound" finding above.
- Q6_K fits in 33 GB VRAM and runs comfortably. On Mac, a 36 GB unified-memory configuration is the realistic floor.

### Try it yourself

```bash
ollama run batiai/qwen3.6-35b:iq4 --verbose "Write a haiku about Seoul in autumn."
```

Full benchmark harness (cold start, 3× warm runs, long response, Korean, tool call, memory delta):

```bash
./bench.sh           # interactive menu — pick by number
```

Works on both macOS and Linux (with GPU). Share the `reports/bench-*.json` and we'll add your hardware row.

## Two modes — text-only by default, multimodal opt-in

Upstream Qwen 3.6 35B-A3B is multimodal (text + image + video understanding). In the GGUF ecosystem this is delivered as **two files**: a main `model.gguf` (text tower) and a separate `mmproj.gguf` (multi-modal projector — the vision tower). We ship **both**, but separate, so you can pick:

| | **Text-only** (default) | **Multimodal** (opt-in) |
|---|---|---|
| Files needed | main GGUF only | main GGUF **+** `mmproj-*.gguf` |
| Capabilities | Q&A, coding, tool calling, RAG, agents | + image / video understanding (OCR, captioning, visual reasoning) |
| `ollama pull` | ✅ single command | ⚠ Ollama mmproj integration is still rough — use llama.cpp directly |
| Disk / RAM | **smaller** (no vision weights) | larger (+ ~580 MB to ~860 MB) |
| Recommended for | most users (chat, code, agents) | OCR, image understanding, multimodal RAG |

This is the same pattern unsloth / bartowski / mradermacher use for multimodal models — text-only on Ollama, full multimodal via llama.cpp + mmproj. Best of both worlds.

### Multimodal usage (llama.cpp)

Download the main GGUF + the mmproj file:

```bash
# Pick a main model (text tower)
wget https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF/resolve/main/Qwen-Qwen3.6-35B-A3B-IQ4_XS.gguf

# Pick the mmproj (vision tower) — Q6_K is the sweet spot, BF16 if you want zero loss
wget https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF/resolve/main/mmproj-Qwen3.6-35B-A3B-Q6_K.gguf
```

**Server mode (OpenAI-compatible Vision API):**

```bash
llama-server \
  -m Qwen-Qwen3.6-35B-A3B-IQ4_XS.gguf \
  --mmproj mmproj-Qwen3.6-35B-A3B-Q6_K.gguf \
  -c 32768 --host 127.0.0.1 --port 8080

# Then post images via the OpenAI Vision API shape
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
  -m Qwen-Qwen3.6-35B-A3B-IQ4_XS.gguf \
  --mmproj mmproj-Qwen3.6-35B-A3B-Q6_K.gguf \
  --image ~/Desktop/photo.jpg \
  -p "describe this image"
```

### mmproj quantizations available

| File | Quant | Size | When to use |
|------|-------|------|-------------|
| `mmproj-Qwen3.6-35B-A3B-Q6_K.gguf` | Q6_K | ~579 MB | balanced (recommended) |
| `mmproj-Qwen3.6-35B-A3B-BF16.gguf` | BF16 | ~861 MB | absolute zero quantization loss for vision |

(Q8_0 is not available because some Qwen3.6 vision tensors have shapes incompatible with Q8_0's column-32 alignment requirement — this is upstream-side, applies to every quantizer of this model. Q6_K's K-quant block layout handles them.)

### Related multimodal model in the BatiAI stack

For **multimodal embedding** (text + image vector search for RAG), see [Qwen3-VL-Embedding-2B](https://huggingface.co/batiai/Qwen3-VL-Embedding-2B-GGUF) / [8B](https://huggingface.co/batiai/Qwen3-VL-Embedding-8B-GGUF) — different use case where text and image must coexist in one vector space.

## Note on the "3.6" naming

Upstream Qwen released this model as **Qwen 3.6** publicly. Internally the Hugging Face config still registers the architecture as `Qwen3_5MoeForConditionalGeneration` (a transitional class name carried over from the 3.5 line). llama.cpp handles this via its `Qwen3_5MoeTextModel` converter, which is what these GGUFs were built from. For the upstream vision-language benchmarks (MMMU 81.7, MathVista 86.4, etc.), see the multimodal weights linked above.

## Technical Details

- **Original Model**: [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- **Released**: 2026-04-15
- **Architecture**: MoE + **Gated DeltaNet hybrid attention**
  - 40 layers, hidden 2048, expert-intermediate 512
  - Layout: 10× (3× Gated DeltaNet → MoE + 1× Gated Attention → MoE)
  - Linear-attention heads: 32 V / 16 QK (head dim 128)
  - Softmax-attention heads: 16 Q / 2 KV (head dim 256, RoPE dim 64)
- **Parameters**: 35 B total, ~3 B active per forward pass
- **Experts**: 256 total, 8 routed + 1 shared per token
- **Context Window**: 262,144 tokens native (extensible to ~1,010,000 via YaRN)
- **Vocabulary**: 248,320 tokens (padded)
- **Training**: Multi-token Prediction (MTP) applied for speculative decoding
- **Modes**: thinking / non-thinking switchable
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) build `bafae2765`
- **Quantized by**: [BatiAI](https://bati.ai)
- **Calibration data**: wikitext-2-raw

## How We Quantize

```
Qwen/Qwen3.6-35B-A3B (BF16 safetensors, ~70 GB)
  ↓ llama.cpp convert_hf_to_gguf.py  (text-only, vision excluded)
BF16 GGUF (65 GB)
  ↓ llama-imatrix  (wikitext-2-raw calibration, GPU-accelerated)
imatrix.dat
  ↓ llama-quantize --imatrix  (IQ3_XXS, IQ4_XS)
Quantized GGUF
  ↓ ollama push  +  hf upload
Published to batiai/ on Ollama & Hugging Face
```

No third-party intermediaries. Direct from official Qwen weights.

## About BatiFlow

[**BatiFlow**](https://flow.bati.ai) is a macOS-native AI automation app — just 5 MB, Swift-native. Free on-device AI via Ollama — no API costs, no usage limits, 100% private.

- **AI Command Bar** — natural-language action execution
- **KakaoTalk / iMessage / Slack** automation
- **Chrome** navigation, filling, screenshots via CDP
- **57 built-in tools** — calendar, mail, reminders, files, shell, etc.
- **Skill builder** — reusable YAML automations
- **Multilingual** — Korean / English

[Download BatiFlow](https://github.com/batiai/batiflow-releases/releases/latest)

## License

This repo mirrors the upstream license. `Qwen/Qwen3.6-35B-A3B` is released under **Apache 2.0** — commercial use permitted.

BatiAI's quantization pipeline is MIT.

## Sources

Benchmark numbers in this card come from the official upstream [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) model card and Qwen's [research blog](https://qwen.ai/blog?id=qwen3.6-35b-a3b). Quantization and on-device numbers are measured by BatiAI.

## Benchmarks

<!-- BENCH-START -->

| Machine | Quant | Cold start | Prompt eval | Token gen | Tested |
|---------|-------|------------|-------------|-----------|--------|
| MacBook Pro M4 Max 128GB | IQ3_XXS | 3.68s | 194.82 t/s | 44.54 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | IQ4_XS | 4.852s | 224.76 t/s | 45.13 t/s | 2026-05-03 |
| MacBook Pro M4 Max 128GB | Q6_K | 7.215s | 202.16 t/s | 44.78 t/s | 2026-05-03 |

<!-- BENCH-END -->
