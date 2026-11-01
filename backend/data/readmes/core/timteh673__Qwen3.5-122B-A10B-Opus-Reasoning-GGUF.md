---
license: apache-2.0
base_model: Qwen/Qwen3.5-122B-A10B
tags:
  - qwen3.5
  - moe
  - gguf
  - uncensored
  - reasoning
  - fine-tuned
  - opus
  - claude
  - lora
  - 122b
  - 10b-active
model_type: qwen3_5_moe
quantized_by: timteh673
datasets:
  - nohurry/Opus-4.6-Reasoning-3000x-filtered
  - Roman1111111/claude-opus-4.6-10000x
  - Jackrong/Qwen3.5-reasoning-700x
  - TeichAI/claude-4.5-opus-high-reasoning-250x
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
pipeline_tag: text-generation
---

# Qwen3.5-122B-A10B-Opus-Reasoning-GGUF

**The first Claude Opus-distilled reasoning fine-tune of Qwen3.5-122B at full scale.** Enhanced multi-step reasoning, analytical depth, and uncensored output — trained where competitors can't reach.

122B total parameters, **10B active per token** (Mixture-of-Experts). LoRA fine-tuned on 12,840 Claude Opus 4.6 reasoning traces. 7 quantization levels from Q2_K to BF16.

⚡ **Forged on 8×H200 SXM5 | 1.1TB VRAM**

---

## Why This Model

| | Base Qwen3.5-122B | Jackrong (27B) | **TIMTEH (this)** |
|---|---|---|---|
| Scale | 122B/10B active | 27B dense | **122B/10B active** |
| Training data | Base alignment | Opus distillation | **Opus distillation** |
| Reasoning quality | Standard | Enhanced (small scale) | **Enhanced (full MoE scale)** |
| Uncensored | ❌ | ✅ | **✅** |
| Hardware required to train | Any | Consumer GPU | **8×H200 (1.1TB VRAM)** |

**Nobody else has fine-tuned Qwen3.5-122B on Opus reasoning data.** Jackrong stopped at 27B because they don't have the hardware. We do.

---

## Quantizations

| Quant | File | Size | BPW | RAM Required | Use Case |
|-------|------|------|-----|-------------|----------|
| **BF16** | `...-BF16.gguf` | 228 GB | 16.0 | ~235 GB | Maximum quality, reference |
| **Q8_0** | `...-Q8_0.gguf` | 121 GB | 8.5 | ~125 GB | Near-lossless, high-VRAM setups |
| **Q6_K** | `...-Q6_K.gguf` | 94 GB | 6.6 | ~98 GB | Excellent quality |
| **Q5_K_M** | `...-Q5_K_M.gguf` | 81 GB | 5.7 | ~85 GB | Great balance |
| **Q4_K_M** | `...-Q4_K_M.gguf` | 70 GB | 4.9 | ~74 GB | ⭐ **Recommended** — best quality/size |
| **Q3_K_M** | `...-Q3_K_M.gguf` | 55 GB | 3.9 | ~58 GB | Fits 2×48GB GPUs |
| **Q2_K** | `...-Q2_K.gguf` | 42 GB | 2.9 | ~45 GB | Single 48GB GPU |

---

## Training Details

| Parameter | Value |
|-----------|-------|
| **Base Model** | [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) |
| **Method** | LoRA (r=64, alpha=128, dropout=0.05) |
| **Trainable Parameters** | 66.8M / 122.1B (0.05%) |
| **Training Samples** | 12,840 |
| **Epochs** | 2 |
| **Steps** | 1,266 |
| **Final Avg Loss** | 0.1502 |
| **Training Time** | 6 hours 34 minutes |
| **Hardware** | 8× NVIDIA H200 SXM5 (141GB HBM3e each, NVLink 478 GB/s) |
| **Precision** | BF16 (full, no quantized training) |
| **Effective Batch Size** | 64 |
| **Learning Rate** | Cosine schedule, peak 2e-4 |
| **Max Sequence Length** | 4096 |

### Training Datasets

| Dataset | Samples | Source |
|---------|---------|--------|
| opus-10000x | 9,633 | Claude Opus 4.6 reasoning traces (10K filtered) |
| opus-3000x | 2,326 | Claude Opus 4.6 reasoning traces (3K filtered) |
| reasoning-700x | 633 | Qwen3.5 reasoning samples |
| high-reasoning-250x | 250 | High-quality Opus reasoning (curated) |

---

## Architecture

- **Type:** Qwen3_5MoeForCausalLM (Mixture-of-Experts)
- **Total Parameters:** 122.1B
- **Active Parameters:** ~10B per token
- **Hidden Size:** 3,072
- **Layers:** 48
- **Attention Heads:** 32 (GQA)
- **Experts:** 256 routed + shared expert, 10 active per token
- **Context Length:** 131,072 tokens (default), extensible to 262K
- **Vocab Size:** 248,320
- **Thinking Mode:** Supports `<think>` tags for explicit chain-of-thought
- **License:** Apache 2.0

---

## Usage

### llama.cpp

```bash
# Recommended: Q4_K_M
./llama-cli -m Qwen3.5-122B-A10B-Opus-Reasoning-Q4_K_M.gguf \
  -p "Analyze the following problem step by step:" \
  -n 2048 --temp 0.7 --top-p 0.9

# Server mode
./llama-server -m Qwen3.5-122B-A10B-Opus-Reasoning-Q4_K_M.gguf \
  --port 8080 --host 0.0.0.0 -c 65536
```

### Ollama

```bash
ollama run timteh673/Qwen3.5-122B-A10B-Opus-Reasoning
```

### LM Studio

Download the GGUF file and load in LM Studio. Supports thinking/non-thinking modes via `enable_thinking` in chat template.

### Open WebUI / SillyTavern

Point your backend to a llama.cpp server running any quant. Full OpenAI-compatible API at `/v1/chat/completions`.

### Recommended Settings

| Setting | Value | Notes |
|---------|-------|-------|
| Temperature | 0.6–0.7 | Reasoning tasks |
| Temperature | 0.8–1.0 | Creative tasks |
| Top-P | 0.9 | |
| Min-P | 0.05 | Good alternative to Top-P |
| Context | 32K+ | Supports up to 131K |
| Thinking | Enabled | Use `enable_thinking=True` for best results |

---

## What's Different From Base

- **Enhanced reasoning chains** — trained on 12,840 Opus-quality multi-step analytical traces
- **Better instruction following** — deeper engagement with complex prompts
- **Uncensored** — no refusal training, responds to all prompts
- **MoE efficiency** — only 10B params active per token despite 122B total
- **Thinking mode** — native `<think>` tag support for explicit chain-of-thought

---

## Pipeline

```
Qwen3.5-122B-A10B (base)
  → LoRA fine-tune (r=64, 12,840 Opus traces, 8×H200, 6.5h)
  → Merge adapter into base weights
  → Convert to BF16 GGUF (llama.cpp, 879 tensors)
  → Quantize: Q8_0, Q6_K, Q5_K_M, Q4_K_M, Q3_K_M, Q2_K
```

All steps executed natively in BF16 — no quantized training, no optimization hacks. When you have 1.1TB VRAM, you use it.

---

## Model Provenance

- **Base:** [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) (Apache 2.0)
- **Training Framework:** transformers + PEFT + TRL (raw, no wrappers)
- **Quantization:** llama.cpp (build 8c60b8a)
- **Hardware:** 8×NVIDIA H200 SXM5 (IBM Cloud, 1.1TB VRAM total)

---

## Also From TIMTEH

| Model | Status | Description |
|-------|--------|-------------|
| [Qwen3.5-397B-A17B-Uncensored-GGUF](https://huggingface.co/timteh673/Qwen3.5-397B-A17B-Uncensored-GGUF) | ✅ Live | Abliterated 397B MoE — 7 quants |
| [Mistral-Small-4-119B-Uncensored-GGUF](https://huggingface.co/timteh673/Mistral-Small-4-119B-Uncensored-GGUF) | ✅ Live | First TIMTEH release — 7 quants |
| [Nemotron-3-Super-120B-A12B-Uncensored-GGUF](https://huggingface.co/timteh673/Nemotron-3-Super-120B-A12B-Uncensored-GGUF) | ✅ Live | Benchmarked — 7 quants |
| Qwen3.5-397B Opus-Reasoning | 🔥 Training | Stage 2 fine-tune (same technique, 397B scale) |

---

## ⚠️ Disclaimer

This model has been fine-tuned on uncensored reasoning data. It may generate content that is harmful, offensive, or inappropriate. Users are solely responsible for ensuring their use complies with applicable laws and ethical standards. Intended for research, testing, and controlled environments.

---

## ☕ Support This Work

Running 8×H200 GPUs isn't free. Every donation directly funds more open-weight model releases, better abliteration techniques, and pushing the frontier of what's possible with open models.

<a href="https://buymeacoffee.com/timteh" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="217" height="60">
</a>

<p align="center">
  <img src="bmac-qr.png" alt="Buy Me a Coffee QR Code" width="250">
</p>

### 💎 Crypto Donations

| Currency | Address |
|----------|---------|
| **BTC** | `bc1p4q7vpwucvww2y3x4nhps4y4vekye8uwm9re5a0kx8l6u5nky5ucszm2qhh` |
| **ETH** | `0xe5Aa16E53b141D42458ABeEDb00a157c3Fea2108` |
| **SOL** | `9CXwjG1mm9uLkxRevdMQiF61cr6TNHSiWtFRHmUEgzkG` |

---

## 🏢 Enterprise & Custom Models

**Need a custom 120B+ model aligned to your proprietary data?** TIMTEH provides bespoke enterprise fine-tuning, abliteration, and deployment on 8×H200 SXM5.

- Custom fine-tuning on your data (up to 400B+ parameters)
- Private CARE abliteration (Phase 2 technique)
- Deployment architecture consulting (tensor parallelism, speculative decoding)
- Bespoke distillation datasets

**📧 Contact:** [tim@timlex.co](mailto:tim@timlex.co)

---

*Part of the TIMTEH Cognitive Preservation Foundry — surgical capability preservation at scale.*
⚡ Forged on 8×NVIDIA H200 SXM5 | 1.1TB VRAM
