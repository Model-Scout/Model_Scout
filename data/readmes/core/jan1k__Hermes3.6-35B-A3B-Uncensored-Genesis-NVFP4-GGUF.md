---
license: apache-2.0
tags:
- text-generation
- gguf
- nvfp4
- fp4
- moe
- qwen3.6
- hermes
- uncensored
- vision
- multimodal
- genesis
- mtp
- speculative-decoding
- llama-cpp
language:
- en
- zh
- multilingual
pipeline_tag: image-text-to-text
base_model:
- HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
- LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Final-GGUF
base_model_relation: quantized
---

# Hermes3.6-35B-A3B-Uncensored-Genesis-NVFP4-GGUF

> **DEPRECATED — All files in this repo use the extended NVFP4 format with
> separate `.scale`/`.input_scale` tensors that break LM Studio / Pelican.**
>
> For the current v4 release (inline scales, LM Studio compatible), use:
> - **[jan1k/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-NVFP4-GGUF](https://huggingface.co/jan1k/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-Final-NVFP4-GGUF)** — Hermes version
> - **[jan1k/Qwen3.6-35B-A3B-Uncensored-Genesis-NVFP4-GGUF](https://huggingface.co/jan1k/Qwen3.6-35B-A3B-Uncensored-Genesis-NVFP4-GGUF)** — Non-Hermes version
>
> The files below are kept for archival purposes only. They produce garbage
> output in LM Studio / Pelican because those runtimes do not support the
> separate NVFP4 scale tensor contract.

This repository contains the **NVFP4 (NVIDIA 4-bit Floating Point)** quantized GGUF releases of **LuffyTheFox**'s *Hermes 3.6 / Qwen 3.6 35B A3B Uncensored Genesis* series, including the **Genesis Final Release**.

- **Original Creators & Fine-Tuners:** [LuffyTheFox](https://huggingface.co/LuffyTheFox) & [HauhauCS](https://huggingface.co/HauhauCS)
- **Original Model Releases:**
  - Final Release: [LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Final-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Final-GGUF)
  - V13 Release: [LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-V13-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-V13-GGUF)
- **NVFP4 Quantization & MTP Integration:** [jan1k](https://huggingface.co/jan1k)
- **Quantization Format:** NVFP4 (NVIDIA FP4) GGUF (optimized for NVIDIA Ada Lovelace / Blackwell / Ampere GPUs)
- **Architecture:** Mixture of Experts (MoE) — 35B total parameters / ~3B active per token (8 active experts)
- **Multimodal (Vision):** Supported via `mmproj-Hermes3.6-35B-A3B-Uncensored-Genesis-F16.gguf`

---

## ⚡ What is Genesis?

> **Genesis** is a post-training data regeneration and calibration algorithm for neural networks (LLM) in GGUF format developed by [LuffyTheFox](https://huggingface.co/LuffyTheFox) over almost half a year of development with AI assistance. It is optimized, architecture-independent, works with any model in GGUF format, and is based on mathematical statistics.
>
> Genesis repairs signal purity without retraining:
> 1. **Stage 1:** Scans `ssm_conv1d` tensors (handling long-context memory) and repairs balance between heads.
> 2. **Stage 2:** Scans blocks in chunks (via 3 parameters) and picks the best fit to weight distribution in the tensor, replacing zero blocks without touching learned structure.
> 3. **Stage 3:** Scans for noise via custom SVD (excluding `token_embd.weight`, `output.weight`, 1D tensors, bias, and norms). Reduces training noise based on the [Marchenko–Pastur law](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution) while preserving 99% of signal and learned gradient.

---

## ⚡ Sampling Recommendations (Genesis SVD Stabilization)

According to tests after **Marchenko–Pastur SVD noise-gate stabilization**, the model is most stable when **Top P** and **Min P** sampling are **disabled** for coding and precise tasks (the tensor noise gate has been removed). Only **Temperature** and **Top K** sampling should be used.

### Recommended Parameters:

| Task Type | Temperature | Top K | Top P | Min P | Seed | Presence Penalty | Repeat Penalty |
|---|---|---|---|---|---|---|---|
| **Coding / Precise (Thinking ON)** | `0.6` | `20` | *Disabled (1.0)* | *Disabled (0.0)* | `42` | `0.0` | `1.0` (or `1.05` for agent) |
| **Creative / General (Thinking OFF)** | `1.0` | `20` | *Disabled (1.0)* | *Disabled (0.0)* | `42` | `0.0` | `1.0` |
| **Relaxed / Brainstorm (Thinking OFF)** | `1.0` | `40` | `0.95` | `0.05` | `42` | `0.0` | `1.0` |

---

## 🛠️ Tool Calling & Hermes Agent Compatibility Fix

If running with the `chat_template.jinja` chat template through **Hermes Agent**, the template defaults to XML tool call output (`<function=...><parameter=...>`), whereas Hermes Agent expects standard OpenAI **JSON tool calls**.

To ensure seamless JSON tool calling, pass `tool_call_format: "json"` in `--chat-template-kwargs`:
```json
{"enable_thinking": true, "tool_call_format": "json"}
```

---

## 💡 Recommended System Prompts

### 1. Default / First Experience (High Stability)
```text
You are Qwen (Tongyi Qianwen), a large language model developed by Alibaba Group's Tongyi Lab. You are a helpful assistant.
```

### 2. Agentic Tasks (JSON Schema Output)
```text
You are Qwen (Tongyi Qianwen), a large language model developed by Alibaba Group's Tongyi Lab. You are a helpful assistant that answers in JSON. Here's the json schema you must adhere to:
<schema>
{schema}
</schema>
```

---

## 🚀 Usage Examples (`llama-server` / `llama.cpp`)

### 1. Final NVFP4 Model (Thinking ON, 128K Context)

```bash
llama-server \
  --host 0.0.0.0 --port 8080 \
  --model Qwen3.6-35B-A3B-Uncensored-Genesis-Final-NVFP4.gguf \
  --override-kv qwen2moe.expert_used_count=int:8 \
  --n-gpu-layers all \
  --flash-attn on \
  --cache-type-k f16 \
  --cache-type-v f16 \
  --ctx-size 131072 \
  --parallel 1 \
  --batch-size 2048 \
  --ubatch-size 512 \
  --temp 0.6 \
  --top-p 1.0 \
  --top-k 20 \
  --min-p 0.0 \
  --seed 42 \
  --presence-penalty 0 \
  --repeat-penalty 1.0 \
  --jinja \
  --chat-template-file chat_template.jinja \
  --reasoning on \
  --reasoning-effort high \
  --reasoning-preserve \
  --reasoning-format deepseek \
  --chat-template-kwargs '{"enable_thinking":true}'
```

### 2. Speculative Decoding with Final MTP (Multi-Token Prediction)

```bash
llama-server \
  --host 0.0.0.0 --port 8080 \
  --model Qwen3.6-35B-A3B-Uncensored-Genesis-Final-MTP-NVFP4.gguf \
  --override-kv qwen2moe.expert_used_count=int:8 \
  --n-gpu-layers all \
  --flash-attn on \
  --cache-type-k f16 \
  --cache-type-v f16 \
  --ctx-size 131072 \
  --parallel 1 \
  --batch-size 2048 \
  --ubatch-size 512 \
  --spec-type draft-mtp \
  --spec-draft-n-max 2 \
  --spec-draft-p-min 0.75 \
  --temp 0.6 \
  --top-p 1.0 \
  --top-k 20 \
  --min-p 0.0 \
  --seed 42 \
  --presence-penalty 0 \
  --repeat-penalty 1.0 \
  --jinja \
  --chat-template-file chat_template.jinja \
  --reasoning on \
  --reasoning-effort high \
  --reasoning-preserve \
  --reasoning-format deepseek \
  --chat-template-kwargs '{"enable_thinking":true}'
```

### 3. Multimodal (Vision) Support

Simply add the vision projector parameter:
```bash
  --mmproj mmproj-Hermes3.6-35B-A3B-Uncensored-Genesis-F16.gguf
```

---

## 📦 Repository Files

| File | Size | Description |
|---|---|---|
| `Qwen3.6-35B-A3B-Uncensored-Genesis-Final-NVFP4.gguf` | ~20.0 GB | **Final Release** NVFP4 model (quantized by jan1k) |
| `Qwen3.6-35B-A3B-Uncensored-Genesis-Final-MTP-NVFP4.gguf` | ~20.6 GB | **Final Release** NVFP4 model with integrated MTP draft head |
| `Hermes3.6-35B-A3B-Uncensored-Genesis-V13-NVFP4.gguf` | ~20.0 GB | V13 release (NVFP4 GGUF) |
| `Hermes3.6-35B-A3B-Uncensored-Genesis-NVFP4.gguf` | ~20.0 GB | Initial release (NVFP4 GGUF) |
| `mmproj-Hermes3.6-35B-A3B-Uncensored-Genesis-F16.gguf` | ~857 MB | Vision multimodal projector (F16) |
| `chat_template.jinja` | ~16 KB | Jinja chat template with JSON tool call support |

---

## 🤝 Credits & Attribution

- **[LuffyTheFox](https://huggingface.co/LuffyTheFox)** for the Genesis post-training calibrations and Hermes fine-tuning.
  - [Genesis Final Release](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Final-GGUF)
  - [Genesis V13 Release](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-V13-GGUF)
- **[jan1k](https://huggingface.co/jan1k)** for NVFP4 quantizations and MTP draft head integration.
- **[HauhauCS](https://huggingface.co/HauhauCS)** for the base fine-tunes.
- Chat template by **[froggeric](https://huggingface.co/froggeric)** & **[qweefchief](https://huggingface.co/qweefchief)**.

---

## 📬 Contact & Support (LuffyTheFox)

> ⚡ If you like this Genesis LLM release you can [**donate**](https://web.tribute.tg/d/KIH) via [@Tribute](https://t.me/tribute) bot in Telegram to support future Genesis LLM development.

- Contact: `luffythefox@mail.ru`, `azakharchenko92@gmail.com`
- Telegram: `@LuffyTheFox`
- **[Join the Discord](https://discord.gg/SZ5vacTXYf)** for updates, roadmaps, projects, or just to chat.
- [Quantization Script with Unsloth profiles support](https://pastebin.com/hXhcMJn9)
