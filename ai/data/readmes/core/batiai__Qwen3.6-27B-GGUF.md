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
  - dense
  - quantized
  - imatrix
  - apple-silicon
  - ollama
  - batiai
  - on-device
  - agentic
  - coding
  - multimodal
base_model: Qwen/Qwen3.6-27B
pipeline_tag: text-generation
library_name: llama.cpp
---

# Qwen 3.6 27B GGUF — Quantized by BatiAI

> 🆕 **Newer model available — [Qwen3.8-27B GGUF](https://huggingface.co/batiai/Qwen3.8-27B-GGUF)**
> Qwen's 2026-08 release. Same 27B class, six quants from 10 GB, vision included, Korean-verified.
> `ollama run batiai/qwen3.8-27b:iq4`


<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3.6-27b"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3.6--27b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/Qwen/Qwen3.6-27B"><img src="https://img.shields.io/badge/Upstream-Qwen3.6--27B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> **"Flagship Coding in a 27B Dense Package"** — imatrix-calibrated GGUF quantizations of **Qwen/Qwen3.6-27B** (dense, multimodal-capable) for on-device AI on Mac.
> Built and verified by [BatiAI](https://bati.ai) for [BatiFlow](https://flow.bati.ai) — free, unlimited, on-device AI automation.

> 🔥 **100,000+ downloads** — the most-pulled model in the [`batiai`](https://huggingface.co/batiai) org. Thanks for running it on your Mac. **Running this locally? [BatiFlow](https://flow.bati.ai) turns it into a full on-device automation assistant — free.**
>
> _If it's useful, a ❤️ helps other Mac users find it._

Released by Alibaba on **April 22, 2026** — the dense counterpart of the Qwen 3.6 family. Upstream reports this 27B dense model **matches or exceeds Qwen 3.5-397B-A17B MoE** on major agentic-coding benchmarks, despite having 14× fewer total parameters.

## Quick Start

```bash
# 16 GB Mac (tight, single-turn)
ollama pull batiai/qwen3.6-27b:iq3

# 24 GB Mac (recommended for Dense 27B)
ollama pull batiai/qwen3.6-27b:iq4      # imatrix, best quality-per-bit
ollama pull batiai/qwen3.6-27b:q4       # K-quant alternative

# 32 GB+ Mac (highest on-device quality)
ollama pull batiai/qwen3.6-27b:q6

ollama run batiai/qwen3.6-27b:iq4
```

**Tool calling**: every tag ships with a ChatML + `{{ .Tools }}` Modelfile template so Ollama reports `tools` and `thinking` capabilities. Qwen 3.6 thinks by default — pass `"think": false` in your chat request (or `--reasoning off` in llama.cpp) if you want clean tool-call JSON without a `<think>` prefix. The legacy `/no_think` prompt prefix (Qwen 3.5 convention) does **not** work on 3.6.

## Dense vs MoE — which Qwen 3.6 should you pull?

| | Qwen 3.6 **27B (this repo)** | [Qwen 3.6 **35B-A3B**](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |
|---|---|---|
| Architecture | **Dense** 27B | MoE, 35B total / **3B active** |
| Active params / token | **27B** | 3B |
| Typical speed on M4 Max | ~baseline (slower) | **~3-5× faster** (fewer active) |
| Quality on agentic coding | **Slightly higher** (dense wins on long-horizon) | Strong |
| Typical VRAM (IQ4) | ~14 GB | ~18 GB |
| When to pick | max quality, batch processing, tool-heavy agents where per-token latency isn't critical | interactive chat, streaming, low-latency UX |

Both are Apache 2.0, both support tools + thinking + 262K context. The 35B MoE is the better default for most BatiFlow users because chat feels snappier; this 27B dense is the quality ceiling when throughput doesn't matter.

## Available Quantizations

**imatrix is applied to every low/mid-bit quant** (IQ and Q4_K_M) using wikitext-2-raw calibration — consistent recipe across the BatiAI lineup.

| Tag (Ollama) | Quant | File Size | Min RAM | Recommended For |
|-----|-------|-----------|---------|-----------------|
| `:iq3` | **IQ3_XXS** (imatrix) | **11 GB** | 16 GB | 16 GB Mac mini / MacBook Air — smallest |
| `:q3` | **Q3_K_M** (imatrix) | **13 GB** | 16 GB | K-quant alternative to IQ3 |
| **`:iq4`** | **IQ4_XS** (imatrix) | **15 GB** | 24 GB | **24 GB Mac — recommended** |
| `:q4` | **Q4_K_M** (imatrix) | **16 GB** | 24 GB | K-quant alternative to IQ4 |
| `:q6` | **Q6_K** (K-quant) | **21 GB** | 32 GB+ | Near-lossless, MacBook Pro M4 Pro / Studio |

**Also on Hugging Face only:**
- `mmproj-Qwen-Qwen3.6-27B-Q6_K.gguf` / `mmproj-Qwen-Qwen3.6-27B-BF16.gguf` — vision projector (see [Multimodal mode](#multimodal-mode-opt-in))
- `imatrix.dat` — importance-matrix calibration data; use it to roll your own quants from the upstream BF16

## Why Qwen 3.6 27B Dense?

Upstream positions the 27B as _"flagship coding in a dense package"_ — the model is the **efficient-inference companion** to the 35B-A3B MoE, tuned to hold up on agentic coding when you need dense-model reliability for long-horizon tool use.

### Upstream benchmarks (Alibaba official BF16 figures)

Numbers from the [official Qwen3.6-27B model card](https://huggingface.co/Qwen/Qwen3.6-27B). **Post your own Mac bench results and we'll add them here.**

**Coding & Agentic**

| Benchmark | Qwen 3.6-27B (Dense) | Qwen 3.5-397B-A17B (prev gen, MoE) | Note |
|---|---:|---:|---|
| SWE-bench Verified | _TBD_ | 72.5 | 27B dense ≥ 397B MoE per upstream claims |
| Terminal-Bench | _TBD_ | 44.0 | |
| QwenWebBench | _TBD_ | — | |

_We'll fill in Alibaba's BF16 numbers after the upstream benchmark sheet is finalized; until then see [MarkTechPost summary](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)._

### Key capabilities

- **Agentic coding** — tuned for repo-level reasoning, multi-step tool-use flows
- **262 K native context**, extensible to 1,010,000 tokens via YaRN
- **Thinking mode** (default ON) — `<think>…</think>` block before final response
- **Tool calling** via `qwen3_coder` parser — works with BatiFlow's Tools API
- **Multimodal** (vision + video understanding) via separate `mmproj` file — see below
- **Apache 2.0** — commercial use permitted

## RAM Requirements (on-device, Dense 27B)

| Your Mac RAM | IQ3 (11 GB) | Q3 (13 GB) | IQ4 (15 GB) | Q4 (16 GB) | Q6 (21 GB) |
|--------------|:---:|:---:|:---:|:---:|:---:|
| 16 GB        | ❌ swap-bound (0.02 t/s) | ❌ | ❌ | ❌ | ❌ |
| 24 GB        | ✅ | ✅ | ✅ (but :iq4 slow — see Metal note) | ✅ | ❌ |
| 32 GB        | ✅ | ✅ | ✅ | ✅ | ✅ tight |
| 48 GB+       | ✅ | ✅ | ✅ | ✅ | ✅ comfortable |

**Dense 27B note:** on every forward pass **all 27B params are active**. Expect **slower per-token speed** than typical MoE models. On Mac, realistic Qwen 3.6-27B usage starts at **24 GB unified memory** — below that, single-turn inference is bottlenecked by swap.

## On-device Benchmarks (measured)

Measured with BatiAI's bench harness (`test-qwen3.6-27b.sh`) on real hardware. Run on your Mac and share the JSON — we'll add your row.

### Apple Silicon (M4 Max / mini — `ollama run --verbose`)

| Hardware | Quant | Gen (warm) | Prompt eval | Long resp | Cold 1st gen | Load | Ollama RAM | Korean | Tool-call |
|---|---|---:|---:|---:|---:|---:|---:|:---:|:---:|
| **M4 Max** 128 GB | **IQ3_XXS** | **17.83 t/s** | 108.66 t/s | 16.48 t/s | 18.04 t/s | 5.0 s | 24 GB | ✅ | ✅ |
| **M4 Max** 128 GB | **Q3_K_M**  | **15.30 t/s** | 111.66 t/s | 14.60 t/s | 16.36 t/s | 6.6 s | 26 GB | ✅ | ✅ |
| **M4 Max** 128 GB | **IQ4_XS**  | 5.52 t/s ⚠ | 82.54 t/s | 4.96 t/s | 6.36 t/s | 8.0 s | 28 GB | ✅ | ✅² |
| **M4 Max** 128 GB | **Q4_K_M**  | **16.56 t/s** | 114.49 t/s | 16.13 t/s | 18.96 t/s | 8.3 s | 29 GB | ✅ | ✅² |
| **Mac mini** M4 16 GB | IQ3_XXS | **0.02 t/s** ❌ | 0.64 t/s | — | — | 16.0 s | swap-bound | ✅ | — |

Measured with `ollama serve` thinking-ON (model default). `./test-qwen3.6-27b.sh` on the BatiAI repo reproduces these rows in 10 minutes per Mac.

**²Tool-call note**: first Mac bench returned empty JSON for IQ4/Q4 — **not a quant quality issue**. Ollama's default `think:true` produced long `<think>` blocks on higher-quality quants that consumed the 100-token test budget before the JSON appeared. Server-side retest with `--reasoning off` confirmed **all 5 quants emit the exact canonical JSON** `{"name":"send_message","arguments":{"recipient":"John","message":"hello"}}`. The `test-qwen3.6-27b.sh` script now passes `"think": false` on tool-call turns (matching real BatiFlow flows). Pull the updated script for clean green checks.

### ⚠ IQ4_XS is currently slow on Apple Metal — use Q4_K_M for now

`IQ4_XS` averaged **5.52 t/s on M4 Max** vs `Q4_K_M` at **16.56 t/s** (similar file size, same machine). This appears to be an **upstream llama.cpp regression on Apple M-series Metal** — [llama.cpp issue #21655](https://github.com/ggerganov/llama.cpp/issues/21655) reports a ~3.8× IQ4_XS slowdown on M4 between tags `b8680` → current, with the same quant running at expected speed on older builds and on NVIDIA (within 10 % of Q4_K_M on RTX 6000 Ada: 85.7 vs 79.0 t/s). This is a runtime-side issue, not a model-file issue — when upstream fixes the Metal IQ4 kernel, existing `:iq4` GGUFs will speed up without re-quantization.

**Until that fix lands, recommendation on Apple Silicon:**
- **`:q4` (Q4_K_M) — best speed/quality** on M-series Mac (16+ t/s)
- `:q3` or `:iq3` — smaller footprint if VRAM is tight
- `:iq4` — only on NVIDIA (where it matches Q4_K_M speed)
- `:q6` — quality ceiling on 32 GB+

### ❌ Qwen 3.6-27B does not fit usefully on 16 GB Macs

On base M4 Mac mini 16 GB, IQ3_XXS (11 GB) runs at **0.02 t/s** — ~30 minutes to generate a short greeting because unified memory overflows into swap once model + KV cache + macOS + Ollama exceed 16 GB. Larger quants do not load at all.

**If your Mac is 16 GB: this model is not for you.** The 27B Dense (and even the 35B-A3B MoE sibling) pushes past what 16 GB unified memory can stream without swap thrash. For 16 GB Macs consider smaller BatiAI models such as [Gemma 4 E4B-it](https://huggingface.co/batiai/Gemma-4-E4B-it-GGUF), [Qwen 3.5 9B](https://huggingface.co/batiai/Qwen3.5-9B-GGUF), or any ~4-8 B class model.

### Server reference (BatiAI build rig: 2× RTX 6000 Ada 48 GB, 96 GB total VRAM)

Not our target platform, but a useful ceiling. Configs: `llama-cli --reasoning off`, Linux, llama.cpp build `bafae2765`.

#### Single-GPU (CUDA_VISIBLE_DEVICES=1, where quantized GGUFs were verified)

| Metric              | IQ3_XXS | Q3_K_M | IQ4_XS | Q4_K_M | Q6_K |
|---------------------|--------:|-------:|-------:|-------:|-----:|
| Gen speed (single-turn) | **97.4 t/s** | **88.2 t/s** | **85.7 t/s** | **79.0 t/s** | **64.1 t/s** |
| Load time           | 5 s | 8 s | 9 s | 10 s | 13 s |
| VRAM (incl. 4 K ctx) | ~12 GB | ~15 GB | ~16 GB | ~18 GB | ~23 GB |

Tool-call JSON and Korean greeting (`안녕하세요!`) verified on every quant server-side.

#### Dual-GPU tensor-split (CUDA_VISIBLE_DEVICES=0,1)

| Metric | Q6_K single-GPU | Q6_K split across 2 GPUs |
|--------|----------------:|-------------------------:|
| Gen speed | **64.1 t/s** | 35.6 t/s |
| VRAM split | 23 GB / 0 GB | 19 GB / 22 GB |

**Takeaway**: splitting a 27 B model that already fits in one 48 GB card is **~45 % slower** than packing it on one. Multi-GPU tensor-split helps when the model is too large for a single card (e.g. Qwen 3.6-35B-A3B IQ4_XS 18 GB + long context, or 1 T+ MoE models like Kimi K2.6 that need both cards); it hurts for 27 B. Use `CUDA_VISIBLE_DEVICES=1` (or `=0`) for fastest inference on this lineup.

Full report: [Qwen-Qwen3.6-27B-20260423.md](https://huggingface.co/batiai/Qwen3.6-27B-GGUF/blob/main/reports/Qwen-Qwen3.6-27B-20260423.md).

### Takeaway: Mac vs server

| | M4 Max 128 GB | RTX 6000 Ada |
|---|---:|---:|
| Q4_K_M gen | 16.56 t/s | 79.0 t/s |
| IQ3_XXS gen | 17.83 t/s | 97.4 t/s |
| Mac / Server ratio | **~20 %** | 100 % |

Mac reaches ~20 % of the server's throughput on Dense 27B, as expected for memory-bandwidth-bound inference. This 27B is the pick when per-token latency matters less than single-pass dense-reasoning quality (batch tool-use agents, code-review loops, offline generation). For interactive streaming chat, wait for the Metal IQ4 fix to land upstream or pull `:q4` (K-quant) which currently delivers **the best Mac speed/quality combo at 16.5 t/s on M4 Max**.

### Try it yourself

```bash
ollama run batiai/qwen3.6-27b:iq4 --verbose "Write a haiku about Seoul in autumn."
```

Full harness (cold start, 3× warm, long response, Korean, tool call, memory delta):

```bash
./test-qwen3.6-27b.sh          # from the batiai-models repo, or download just this script
```

Share `reports/bench-qwen3.6-27b-*.json` and we'll add your hardware row.

## Multimodal mode (opt-in)

Upstream Qwen 3.6-27B is multimodal (text + image + video). GGUF delivers this as **two files**: main `model.gguf` (text tower) and `mmproj.gguf` (vision projector). This repo ships **both**, separate, so you pick:

| | Text-only (Ollama default) | Multimodal (llama.cpp) |
|---|---|---|
| Files needed | main GGUF | main GGUF + `mmproj-*.gguf` |
| Capabilities | Q&A, coding, tools, RAG, agents | + OCR, image captioning, visual reasoning |
| `ollama pull` | ✅ single command | ⚠ Ollama's mmproj support is rough — use llama.cpp |

### Multimodal usage (llama.cpp)

```bash
wget https://huggingface.co/batiai/Qwen3.6-27B-GGUF/resolve/main/Qwen-Qwen3.6-27B-IQ4_XS.gguf
wget https://huggingface.co/batiai/Qwen3.6-27B-GGUF/resolve/main/mmproj-Qwen-Qwen3.6-27B-Q6_K.gguf

# Server mode (OpenAI-compatible Vision API)
llama-server \
  -m Qwen-Qwen3.6-27B-IQ4_XS.gguf \
  --mmproj mmproj-Qwen-Qwen3.6-27B-Q6_K.gguf \
  -c 32768 --host 127.0.0.1 --port 8080

# One-shot CLI
llama-mtmd-cli \
  -m Qwen-Qwen3.6-27B-IQ4_XS.gguf \
  --mmproj mmproj-Qwen-Qwen3.6-27B-Q6_K.gguf \
  --image ~/Desktop/photo.jpg \
  -p "describe this image"
```

### mmproj variants

| File | Quant | Size | When to use |
|------|-------|------|-------------|
| `mmproj-Qwen-Qwen3.6-27B-Q6_K.gguf` | Q6_K | **590 MB** | balanced (recommended) |
| `mmproj-Qwen-Qwen3.6-27B-BF16.gguf` | BF16 | **889 MB** | absolute zero loss for vision |

(Q8_0 is unavailable for this mmproj — some Qwen 3.6 vision tensors have shapes incompatible with Q8_0's column-32 alignment; Q6_K's K-quant block layout handles them.)

## Technical Details

- **Original Model**: [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)
- **Released**: 2026-04-22
- **Architecture**: Dense 27B + **Gated DeltaNet / Gated Attention hybrid**
  - 64 layers, hidden 5120, FFN intermediate 17,408
  - Layer pattern: 16 × (3× linear-attention + 1× full-attention) — native softmax attention every 4 layers
  - Linear-attention heads: 48 V / 16 QK (head dim 128)
  - Softmax-attention heads: 24 Q / 4 KV (head dim 256, RoPE dim 64)
- **Parameters**: 27 B total, **27 B active per forward pass** (dense — no expert routing)
- **Context Window**: 262,144 tokens native (extensible to ~1,010,000 via YaRN)
- **Vocabulary**: 248,320 tokens (padded)
- **Multimodal**: vision encoder + `mmproj` (image/video understanding)
- **Modes**: thinking / non-thinking switchable (thinking is default ON)
- **License**: Apache 2.0
- **Quantized by**: [BatiAI](https://bati.ai)
- **Calibration data**: wikitext-2-raw (`imatrix.dat` included on HF)

## How We Quantize

```
Qwen/Qwen3.6-27B (BF16 safetensors, ~54 GB)
  ↓ llama.cpp convert_hf_to_gguf.py  (text tower)
BF16 GGUF (~54 GB)
  ↓ llama.cpp convert_hf_to_gguf.py --mmproj  (vision tower, separate)
mmproj-BF16.gguf
  ↓ llama-imatrix  (wikitext-2-raw, GPU-accelerated)
imatrix.dat
  ↓ llama-quantize --imatrix  (IQ3_XXS, Q3_K_M, IQ4_XS, Q4_K_M)
  ↓ llama-quantize             (Q6_K, mmproj Q6_K)
Quantized GGUF
  ↓ ollama push  +  hf upload
Published to batiai/ on Ollama & Hugging Face
```

No third-party intermediaries. Direct from official Qwen weights.

## About the "3.6" naming

Upstream calls this Qwen 3.6 publicly. Internally the HF config registers the architecture as `Qwen3_5ForConditionalGeneration` (transitional class name from the 3.5 line). llama.cpp handles this via `Qwen3_5TextModel` — the same converter path used for the 35B-A3B MoE sibling.

## About BatiFlow

[**BatiFlow**](https://flow.bati.ai) is a macOS-native AI automation app — 5 MB, Swift-native. Free on-device AI via Ollama — no API costs, no usage limits, 100 % private.

- AI Command Bar — natural-language action execution
- KakaoTalk / iMessage / Slack automation
- Chrome navigation, filling, screenshots via CDP
- 57 built-in tools — calendar, mail, reminders, files, shell, etc.
- Skill builder — reusable YAML automations
- Multilingual — Korean / English

[Download BatiFlow](https://github.com/batiai/batiflow-releases/releases/latest)

## More from BatiAI

Same recipe (official weights → imatrix GGUF → verified on Mac), across the lineup:

| Need | Model |
|------|-------|
| 🖼️ **Multimodal (image + audio)** on-device | [**gemma-4-12B-it-GGUF**](https://huggingface.co/batiai/gemma-4-12B-it-GGUF) — new, encoder-free, 16GB Mac |
| ⚡ Faster chat (MoE, 3B active) | [Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |
| 🪶 Smallest / fastest reasoning + tools | [LFM2.5-8B-A1B-GGUF](https://huggingface.co/batiai/LFM2.5-8B-A1B-GGUF) |
| 🔎 RAG stack (embed + rerank) | [Qwen3-Embedding-8B](https://huggingface.co/batiai/Qwen3-Embedding-8B-GGUF) · [Qwen3-Reranker-8B](https://huggingface.co/batiai/Qwen3-Reranker-8B-GGUF) |

Full org: [huggingface.co/batiai](https://huggingface.co/batiai)

## License

This repo mirrors the upstream license. `Qwen/Qwen3.6-27B` is released under **Apache 2.0** — commercial use permitted.

BatiAI's quantization pipeline is MIT.

## Sources

Benchmark numbers in this card come from the official upstream [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) model card and coverage at [MarkTechPost](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/) and [Let's Data Science](https://letsdatascience.com/news/qwen36-27b-delivers-flagship-coding-in-27b-dense-model-fd698bba). Quantization and on-device numbers are measured by BatiAI.

## Benchmarks

<!-- BENCH-START -->

| Machine | Quant | Cold start | Prompt eval | Token gen | Tested |
|---------|-------|------------|-------------|-----------|--------|
| MacBook Pro M4 Max 128GB | IQ3_XXS | 4.994s | 108.66 t/s | 17.83 t/s | 2026-04-23 |
| MacBook Pro M4 Max 128GB | IQ4_XS | 7.998s | 82.54 t/s | 5.52 t/s | 2026-04-23 |
| MacBook Pro M4 Max 128GB | Q3_K_M | 6.55s | 111.66 t/s | 15.3 t/s | 2026-04-23 |
| MacBook Pro M4 Max 128GB | Q4_K_M | 8.252s | 114.49 t/s | 16.56 t/s | 2026-04-23 |
| MacBook Pro M4 Max 128GB | Q6_K | 8.175s | 112.45 t/s | 13.34 t/s | 2026-05-03 |

<!-- BENCH-END -->
