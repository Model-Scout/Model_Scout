---
license: apache-2.0
library_name: llama.cpp
pipeline_tag: text-generation
base_model:
- FINAL-Bench/Darwin-36B-Opus
tags:
- gguf
- llama.cpp
- conversational
- on-device
- mobile
- iphone
- android
- cpu
- local-llm
- edge
- mixture-of-experts
- moe
- quantized
- pocket
- vidraft
- qwen3_5_moe
- korean
- korean-llm
- darwin
---
> ### 📚 Collections
> **▶ [POCKET Models](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6)** — this family (on-device, no GPU)
> [Darwin Family](https://huggingface.co/collections/FINAL-Bench/darwin-family-699987b1f652864af0122193) · [Aether Foundation](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model-6a5c7f2fa1a4165c0414e53a) · [VKAE Accelerated](https://huggingface.co/collections/FINAL-Bench/vkae-accelerated-6a47231d7e7999dd8227675a)

![POCKET](./pocket_hero.svg)

# POCKET-KR-GGUF · 한국어

### **35B에서 한국어 전문가만 골라낸** 폰용 빌드. Android 8 GB+에서 **GPU 없이** 돕니다. iPhone은 [POCKET-KR-MLX](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX)를 받으세요.

> 🚀 **Try it live, no install →** [![POCKET-35B demo](https://img.shields.io/badge/🤗_Space-POCKET--35B_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![POCKET-26B demo](https://img.shields.io/badge/🤗_Space-POCKET--26B_CPU_chat-0f9d6e)](https://huggingface.co/spaces/FINAL-Bench/POCKET-26B-CPU) — both answering on a **CPU-only** box (no GPU). POCKET-26B is Gemma4-based.

[![License](https://img.shields.io/badge/License-Apache_2.0-0f6e56)](https://www.apache.org/licenses/LICENSE-2.0) [![Runtime](https://img.shields.io/badge/runtime-stock_llama.cpp-f0992a)](https://github.com/ggml-org/llama.cpp) [![No GPU](https://img.shields.io/badge/GPU-not_required-1baf7a)]() [![Base](https://img.shields.io/badge/base-Qwen3.5--35B--A3B-185fa5)]()

**Pick your build →** [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR GGUF](https://img.shields.io/badge/POCKET--KR-GGUF-7A1F3D)](https://huggingface.co/FINAL-Bench/POCKET-KR-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-MLX_(iPhone)-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN GGUF](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF) [![26B](https://img.shields.io/badge/POCKET--26B-GGUF-2a9d8f)](https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF)

## The POCKET lineup — pick by your device

| Repo | File | Size | Runs on | Best for | Korean PPL* |
|---|---|---|---|---|---|
| **POCKET-35B-GGUF** | `Q4_K_M` | 21 GB | PC / server (32 GB RAM) | top quality | **5.79** |
| **POCKET-35B-GGUF** | `Q2_K` ⭐ | 13 GB | mini-PC, no GPU | **daily driver** | 6.49 |
| **POCKET-35B-GGUF** | `IQ1_M` | 8.2 GB | 16 GB RAM box | smallest full model | 9.69 |
| **POCKET-KR-GGUF** | `IQ2_M` | 5.1 GB | Android 8 GB+ | 🇰🇷 Korean phone | 7.95 |
| **POCKET-KR-MLX** | 2-bit | 5.1 GB | 🍎 **iPhone / iPad / Mac** | 🇰🇷 Korean, Apple-native | 7.95 |
| **POCKET-EN-GGUF** | `iPhone-mix` | 5.3 GB | 🍎 iPhone (PocketPal) | 🌍 English phone | — |
| **POCKET-EN-GGUF** | `PC-mix` | 6.8 GB | PC / Android | 🌍 English, best quality | — |

*Wikipedia-Korean perplexity, lower is better. `Q4_K_M` = 5.79 baseline. English builds are tuned on English; see each repo.

> 🍎 **Why MLX for Korean but GGUF for English on iPhone?** Apple-native MLX only does uniform quantization. Korean survives it (96 experts hold up); English needs our proprietary quantization, which only GGUF supports — so the English iPhone build ships as a GGUF you run with [PocketPal](https://github.com/a-ghorbani/pocketpal-ai). Honest, not lazy.

> 🆕 **POCKET-26B** — a **Gemma4-26B-A4B**-based sibling that loads in **any app today** (Ollama · LM Studio · PocketPal · MLX), no bleeding-edge runtime needed: **[GGUF](https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF)** (`Q2_K` 11 GB · `Q4_K_M` 17 GB · GPQA-Diamond **67%**). Universal compatibility for 12 GB phones, PC, and browser.

![Speed vs Bonsai](./pocket_speed.svg)

## Benchmarks — what is measured, what is not

**We measure Bonsai on the same machine with the same stock `llama.cpp`, and we tell you where we lose.**

`[measured]` Generation speed — POCKET wins on both CPU and GPU:

| | POCKET-35B IQ1_M | Bonsai-27B Q1_0 | |
|---|---|---|---|
| CPU generate (Xeon, 16t) | **27.0 tok/s** | 10.1 | 🟢 2.69× |
| GPU generate (H100) | **197 tok/s** | 89 | 🟢 2.22× |
| GPU prompt (H100) | 753 | **1816** | 🔴 0.41× |
| Quality (HellaSwag, 400q) | 61.0% | 60.0% | ⚪ tie (CI overlaps) |

`[measured on a MacBook M3 Pro, 18 GB]` — and on a laptop, POCKET wins **every** axis, including prompt processing:

| | POCKET-35B IQ1_M | Bonsai-27B Q1_0 | |
|---|---|---|---|
| Metal generate (tg64) | **25.4 tok/s** | 12.8 | 🟢 1.99× |
| CPU generate (8 threads) | **13.8 tok/s** | 4.4 | 🟢 3.13× |
| Metal prompt (pp128) | **240.7 tok/s** | 73.4 | 🟢 3.28× |
| CPU prompt (pp128) | **45.5 tok/s** | 9.6 | 🟢 4.75× |

On a laptop GPU the arithmetic headroom that let Bonsai win prefill on an H100 is gone, so MoE sparsity wins across the board. `POCKET-35B-Q2_K` runs on the M3 Pro's CPU at **19.5 tok/s** — on an 18 GB Mac, run Q2_K on CPU (`-ngl 0`); its 13 GB exceeds the recommended Metal budget.

`[measured — GPQA Diamond, 198q, greedy]` reasoning quality vs quantization:

| Model | GPQA-Diamond (greedy) |
|---|---|
| Qwen3.6-35B-A3B | 73.2% |
| POCKET-35B Q4_K_M | 68.7% |
| POCKET-35B Q2_K | 60.1% |

`[pending — community reports welcome]` on-device **iPhone** and **Strix Halo** throughput. We publish only what we ran ourselves; help us fill the rest.

> The same-size rival `Ternary-Bonsai-27B-Q2_0` (7.2 GB) **fails to load in upstream llama.cpp** — it needs the PrismML fork. POCKET runs on the tools you already have.

## Files in this repo
| File | Size | Experts | Runs on | Korean PPL |
|---|---|---|---|---|
| **`POCKET-KR-IQ2_M.gguf`** ⭐ | 5.1 GB | 96 | Android 8 GB+ | 7.95 |
| `POCKET-KR-160-Q2_K.gguf` | 8.5 GB | 160 | phone/PC | 6.88 (quality-first) |
| `POCKET-KR-160-Q3_K_M.gguf` | 11 GB | 160 | PC | 6.35 |

Pruned from 256 experts to the ones Korean actually uses (94% routing coverage at 128). Active params unchanged → **same speed, half the size.**

## Quickstart
```bash
llama-cli -m POCKET-KR-IQ2_M.gguf -p "대한민국의 수도는" -ngl 0 -t 8
```
On Android: [PocketPal](https://github.com/a-ghorbani/pocketpal-ai) → import GGUF.

## Lineage — where POCKET comes from

POCKET is quantized from **[Darwin-36B-Opus](https://huggingface.co/FINAL-Bench/Darwin-36B-Opus)**, VIDRAFT's flagship — a model bred and evolved over several generations on the **Darwin platform** (crossbreeding, healing, expert surgery). Darwin-36B-Opus itself traces back to a Qwen3.5-family MoE architecture.

| Component | Origin |
|---|---|
| **Starting checkpoint** | **[Darwin-36B-Opus](https://huggingface.co/FINAL-Bench/Darwin-36B-Opus)** — VIDRAFT, multi-generation Darwin evolution |
| Base architecture | Qwen3.5-family MoE (256 experts, top-8), unchanged |
| Quantization (`Q4_K_M`…`IQ1_M`) | stock llama.cpp — no custom format |
| Runtime | upstream llama.cpp / Apple MLX — unmodified |
| Proprietary language-specific tuning (KR/EN builds) | **ours** (VIDRAFT) |

The CPU/GPU speed comes from the sparse-MoE architecture plus ordinary quantization — reproducible with the same base and the same tools. What we add is the Darwin-evolved weights, the honest measurement, the Korean tuning, and the pruning that makes the 5 GB phone builds.

## Limitations
- The iPhone/Mac speed is **not yet measured by us** — community reports welcome.
- Extreme quants (`IQ1_M`) hurt Korean ~2.8× more than English; use `Q2_K` or larger for quality.
- English phone builds trade quality for size; the PC build (`PC-mix`) is much closer to full quality.

## License
Apache-2.0.

---
*POCKET is a VIDRAFT model family. 35B, in your pocket. No GPU.*

## Learn more
- On-device LLMs without a GPU — and how POCKET measures up: [Can you run a large LLM without a GPU?](https://vidraft.net/insights/on-device-llm-without-gpu.html)
- What model quantization is, and why a 4-bit model stays smart: [What is model quantization?](https://vidraft.net/insights/what-is-quantization-llm.html)

<!-- POCKET-FAMILY -->

---

## 🧩 The POCKET Family — On-device AI by VIDRAFT

*Big models, small hardware. No GPU, no cloud.*

**Models**
- 📦 [POCKET-35B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) — flagship, PC / server, no GPU
- 📦 [POCKET-26B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF) — compact 26B
- 🇰🇷 [POCKET-KR-GGUF](https://huggingface.co/FINAL-Bench/POCKET-KR-GGUF) — Korean, Android
- 🍎 [POCKET-KR-MLX](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) — Korean, iPhone / Mac
- 🌍 [POCKET-EN-GGUF](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF) — English, phone / PC
- 🖼️ [POCKET-Image-Zimage](https://huggingface.co/FINAL-Bench/POCKET-Image-Zimage) — character-perfect text in any image

**Demos & tools (Spaces)**
- 🎨 [POCKET-Image Studio](https://huggingface.co/spaces/FINAL-Bench/POCKET-Image-Studio) — text-in-image, generate in-page
- 🖥️ [POCKET-35B-CPU](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) — 35B answering on a CPU
- 🖥️ [POCKET-26B-CPU](https://huggingface.co/spaces/FINAL-Bench/POCKET-26B-CPU) — 26B on a CPU

📚 [Full POCKET collection](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6)

<!-- /POCKET-FAMILY -->
