---
language:
  - en
  - zh
  - ko
license: apache-2.0
tags:
  - gguf
  - hunyuan
  - hy3
  - tencent
  - quantized
  - batiai
  - mixture-of-experts
  - frontier
  - 295b
  - agentic
  - tool-calling
  - swe-bench
  - coding
base_model: tencent/Hy3
pipeline_tag: text-generation
library_name: llama.cpp
---

# Hy3 (Hunyuan 3.0) GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-on--device%20AI-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://huggingface.co/tencent/Hy3"><img src="https://img.shields.io/badge/source-Tencent%20official-orange?style=for-the-badge" alt="tencent"></a>
  <a href="#-license--apache-20"><img src="https://img.shields.io/badge/license-Apache--2.0-green?style=for-the-badge" alt="Apache 2.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/295B--A21B-MoE-purple?style=for-the-badge" alt="MoE"></a>
</p>

> **A frontier coding & agent model that runs on your desk.**
> **Q4_K_M / IQ3_XXS** GGUF of **[tencent/Hy3](https://huggingface.co/tencent/Hy3)** (Hunyuan 3.0 — 295B total, **21B active**).
> Quantized **directly from official Tencent BF16 weights** by [BatiAI](https://bati.ai) — code+multilingual‑calibrated imatrix, MTP‑pruned, BatiAI‑signed.

---

## ⚡ Why Hy3?

**The smallest of the 2026 frontier MoEs — 295B that thinks like a giant but runs at 21B speed.**

| | Hy3 | GLM‑5.2 | DeepSeek‑V4 |
|---|---|---|---|
| Total params | **295B** | 753B | ~1.6T |
| Active / token | **21B** | 40B | ~37B |
| Fits a 128GB Mac? | **✅ (IQ3_XXS)** | ✗ | ✗ |

**Benchmarks** — competitive with models 2–5× its size:

| SWE‑Bench Verified | SWE‑Bench Pro | GPQA Diamond | BrowseComp |
|:---:|:---:|:---:|:---:|
| **78.0** | **57.9** | **90.4** | **84.2** |

<sub>Source: <a href="https://huggingface.co/tencent/Hy3">Tencent Hunyuan 3.0 official release</a> (295B‑A21B base). These are <b>base‑model (BF16)</b> figures; the IQ3_XXS / Q4_K_M quants in this repo were not separately benchmarked, so expect some low‑bit degradation from these numbers.</sub>

- 🛠️ **Production‑grade tool‑calling** — dedicated parsers, <4% variance across agent scaffolds. Built for agent pipelines.
- 🧠 **256K context**, 192 experts (top‑8) + shared expert, 80 layers, GQA, reasoning‑effort modes.
- 🔓 **Apache 2.0** — and the official 3.0 release **dropped the geo‑restriction** (Korea / EU / UK now cleared). Commercial use, fine‑tune, redistribute freely.

---

## 📦 Quantizations

| Quant | Size | Min RAM | Best for | Quality |
|-------|------|---------|----------|---------|
| **Q4_K_M** | **166 GB** (4 shards) | 192 GB | 256GB Mac Studio / server | ⭐ **Cleanest** — recommended when RAM allows |
| **IQ3_XXS** | **106 GB** (3 shards) | 128 GB | **128GB Mac Studio** | ✅ Great — fits a 128GB Mac (raise the Metal wired limit; ~106 GiB of weights leaves modest context room) |

Both are built **directly from the official BF16**, quantized with a **diverse code + EN + KO + ZH imatrix**,
and have the **MTP (multi‑token‑prediction) head pruned** (`--prune-layers 80`) — the speculative head gives
**no benefit on Apple Metal** and isn't imatrix‑covered, so a clean 80‑layer text model is the right target.

**✅ Verified (this build).** A captured greedy Q4_K_M run produced this exact, correct `binary_search` (verify log `hy3-q4-verify.log` shipped in this repo):

```python
# prompt: def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

<sub>The captured run also appended a correct test harness, but with a Chinese code comment (`# 测试`) — exactly the low‑bit zh mixing flagged below. Logic was correct; use Q4_K_M for the cleanest output.</sub>

> ⚠️ **Positioning — read this.** Hy3's strength is **frontier coding / reasoning / agentic tool‑calling** (EN/ZH).
> It is **not** a Korean‑specialized model (Tencent origin, no published Korean benchmark); lower‑bit quants can
> show occasional zh/en token mixing on Korean — **use Q4_K_M for the cleanest Korean**. For **Korean‑first**
> chat/STT on 16GB Macs, use [batiai/qwen3.6‑27b](https://huggingface.co/batiai/Qwen3.6-27B-GGUF). Hy3 is a **frontier / high‑RAM
> tier** model (like Kimi K2.6, GLM‑5.1, DeepSeek‑V4) — **128GB+ Apple Silicon or a workstation/server only**.

---

## 🚀 Usage (llama.cpp)

> ⚙️ **Build:** Hy3 (`hy_v3` arch) needs hy_v3 support — mainline merge pending
> ([ggml‑org/llama.cpp#25395](https://github.com/ggml-org/llama.cpp/pull/25395)); build from that PR for now.
> Ollama support follows the mainline merge.
>
> ⚠️ **Chat template:** the stock Hy3 Jinja template uses `.format()` calls llama.cpp rejects. This repo ships a
> **fixed template** (`Hy3-chat_template.jinja`) — pass it with `--jinja`.

```bash
# 1) download — sharded GGUF (llama.cpp auto‑loads all shards from the first one)
#    128GB Mac → IQ3_XXS   |   256GB / server → Q4_K_M
hf download batiai/Hy3-GGUF \
  "Hy3-IQ3_XXS-*.gguf" Hy3-chat_template.jinja --local-dir ./hy3

# 2) chat (Apple Silicon Metal)
./llama-cli -m ./hy3/Hy3-IQ3_XXS-00001-of-00003.gguf -ngl 99 -c 8192 \
  --jinja --chat-template-file ./hy3/Hy3-chat_template.jinja \
  -p "Refactor this function and explain the change."

# raw completion (no chat template): add -no-cnv
```

`Hy3-imatrix.dat` (the calibration matrix used) is included for transparency / re‑quantization.

---

## ✨ What BatiAI did

- **Direct from official Tencent BF16** — never a re‑quant of someone else's GGUF.
- **Diverse imatrix** (code + English + Korean + Chinese) for balanced multilingual + coding fidelity.
- **MTP head pruned** + **chat template fixed** so it actually runs in llama.cpp.
- **Verified**: load ✅ · coding ✅ · Korean ✅ · MoE routing ✅ — BatiAI metadata‑signed.

## 📜 License — Apache 2.0

Fully permissive: commercial use, modification, redistribution — **no geographic restriction** (Korea / EU / UK
cleared in the official Hunyuan 3.0 release). Base model © Tencent; quantized weights redistributed under Apache 2.0.

## 🔗 Source & citation

- Base: [tencent/Hy3](https://huggingface.co/tencent/Hy3) (Hunyuan 3.0)
- Quantized by: [BatiAI](https://bati.ai) · https://flow.bati.ai

```bibtex
@misc{batiai-hy3-gguf-2026,
  title  = {Hy3 (Hunyuan 3.0) GGUF — code+multilingual calibrated quantization},
  author = {BatiAI},
  year   = {2026},
  publisher = {Hugging Face},
  url    = {https://huggingface.co/batiai/Hy3-GGUF}
}
```

— **BatiAI** · on‑device frontier AI · https://flow.bati.ai
