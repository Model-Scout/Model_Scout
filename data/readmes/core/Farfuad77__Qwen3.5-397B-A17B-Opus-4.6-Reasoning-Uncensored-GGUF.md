---
license: apache-2.0
tags:
  - uncensored
  - abliterated
  - gguf
  - qwen
  - qwen3.5
  - moe
  - 397b
  - 17b-active
  - fine-tuned
  - reasoning
  - lora
  - opus
  - claude
base_model: Qwen/Qwen3.5-397B-A17B
model_type: qwen3_5_moe
pipeline_tag: text-generation
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
  - th
  - vi
  - id
---

# Qwen3.5-397B-A17B-Opus-4.6-Reasoning-Uncensored-GGUF

**The world's first reasoning-enhanced uncensored 397B model.** Abliterated + LoRA fine-tuned on 12,842 high-quality reasoning samples distilled from Anthropic's Opus 4.6 outputs.

This is **Stage 2** of the Qwen3.5-397B pipeline:
- **[Stage 1](https://huggingface.co/timteh673/Qwen3.5-397B-A17B-Uncensored-GGUF)** — Abliterated (refusals removed), no fine-tuning
- **Stage 2 (this repo)** — Abliterated + LoRA reasoning fine-tune. Better chain-of-thought, deeper analysis, more structured problem-solving

397B total parameters, **17B active per token** (Mixture-of-Experts). Trained for 3,046 steps across 8×H200 GPUs. Final loss: **0.363**, accuracy: **90.2%**.

## What's Different From Stage 1

| | Stage 1 (Abliterated Only) | **Stage 2 (This Model)** |
|---|---|---|
| Abliteration | ✅ Custom pipeline | ✅ Same pipeline |
| Fine-tuning | None | **LoRA r=64, 134.7M trainable params** |
| Training data | None | **12,842 reasoning samples (Opus 4.6 distillation)** |
| Reasoning quality | Base Qwen3.5 | **Enhanced chain-of-thought + structured analysis** |
| Thinking mode | Default | **Trained with `<think>` tags for explicit reasoning** |
| Final loss | N/A | **0.363** |
| Final accuracy | N/A | **90.2%** |

## Training Details

**LoRA Configuration:**
- Rank: 64, Alpha: 128
- Target modules: `self_attn.{q,k,v,o}_proj`, `shared_expert.{gate,up,down}_proj`
- Trainable parameters: 134.7M / 396.5B total (0.034%)
- Gradient checkpointing: enabled

**Training Hyperparameters:**
- Optimizer: AdamW (fused)
- Learning rate: 1.5e-5 (cosine scheduler)
- Effective batch size: 64
- Sequence length: 4,096
- Epochs: 2 (3,046 total steps)
- Warmup: 3%
- Precision: BF16

**Dataset Composition (12,842 samples, deduplicated):**
- `opus-10000x`: 9,633 multi-turn conversations with deep reasoning
- `opus-3000x`: 2,326 problem/thinking/solution samples with explicit chain-of-thought
- `reasoning-700x`: 633 complex reasoning and analytical tasks
- `high-reasoning-250x`: 250 elite-tier reasoning samples requiring multi-step deduction

All samples feature reasoning traces distilled from Anthropic's Claude Opus 4.6, including `<think>` tag formatting for explicit chain-of-thought.

**Training Curve:**
- Step 0: Loss 0.83
- Step 500: Loss ~0.52
- Step 1000: Loss ~0.42
- Step 2000: Loss ~0.39
- Step 3046: **Loss 0.363, Accuracy 90.2%**

## Quantizations

| Quant | Size | BPW | RAM Required | Description | Use Case |
|-------|------|-----|-------------|-------------|----------|
| **BF16** | 739 GB (2 splits) | 16.01 | ~750 GB | Full precision | Reference, maximum quality |
| **Q8_0** | 393 GB | 8.51 | ~400 GB | 8-bit | Best quality with compression |
| **Q6_K** | 304 GB | 6.57 | ~310 GB | 6-bit | High quality, good compression |
| **Q4_K_M** | 225 GB | ~4.85 | ~230 GB | 4-bit mixed | **Recommended for most users** |
| **Q3_K_M** | 177 GB | ~3.83 | ~185 GB | 3-bit mixed | Memory-constrained setups |
| **Q2_K** | 135 GB | ~2.92 | ~140 GB | 2-bit | Extreme compression |

> **Note:** Q5_K_M is unavailable due to infrastructure loss during upload. Will be regenerated and uploaded in a future update.

## Architecture

- **Type:** Qwen3.5MoeForConditionalGeneration (hybrid GatedDeltaNet + MoE Transformer)
- **Total Parameters:** 397B
- **Active Parameters:** 17B per token
- **Hidden Size:** 4,096
- **Layers:** 60
- **Attention:** 32 heads (GQA, 2 KV heads), head_dim 256
- **Experts:** 512 routed + shared expert, 10 active per token
- **Hybrid Attention:** GatedDeltaNet linear attention + self-attention every 4th layer
- **Context Length:** 262,144 tokens
- **Vocab Size:** 248,320
- **Multimodal:** Native vision encoder (text + image + video)
- **Languages:** 201+ (en, zh, ja, ko, fr, de, es, pt, ru, ar, th, vi, id, ...)
- **License:** Apache 2.0

## Usage

### llama.cpp

```bash
# Recommended: Q4_K_M for balanced quality/memory
./llama-cli -m Qwen3.5-397B-A17B-Opus-4.6-Reasoning-Uncensored-Q4_K_M.gguf \
  -p "You are a helpful uncensored assistant with strong reasoning abilities." \
  -n 2048 --temp 0.7 --top-p 0.9

# Server mode with large context
./llama-server -m Qwen3.5-397B-A17B-Opus-4.6-Reasoning-Uncensored-Q4_K_M.gguf \
  --port 8080 --host 0.0.0.0 -c 131072
```

### LM Studio

Download the GGUF file and load it in LM Studio. The model supports `<think>` reasoning tags — enable thinking mode for best results on complex tasks.

### Open WebUI / SillyTavern

Point your backend to a llama.cpp server. Full OpenAI-compatible API at `/v1/chat/completions`.

## Pipeline

```
Qwen3.5-397B-A17B (base)
    ↓ Custom abliteration (strength 20.0, attn.o_proj + shared_expert.down_proj)
    ↓ LoRA fine-tuning (12,842 Opus 4.6 reasoning samples, 3,046 steps)
    ↓ LoRA merge into base weights
    ↓ BF16 GGUF conversion (llama.cpp)
    ↓ Quantization cascade (Q8_0 → Q2_K)
```

All processing done in BF16 on 8×H200 SXM5 GPUs (1.1TB VRAM total). Abliteration and quantization applied in correct order: full-precision abliteration → training → merge → THEN quantize.

## Known Limitations

- **Q5_K_M missing:** Lost during infrastructure migration. Will be regenerated.
- **Packed expert abliteration:** The 512 routed experts use packed tensor format and were not individually abliterated. Some edge-case refusals may persist.
- **Vision:** Multimodal vision encoder is preserved but untested post-training. Text generation is the primary target.
- **Thinking mode:** The model generates `<think>` tags for reasoning. Strip them in post-processing if unwanted.

## Model Provenance

- **Base model:** [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) (Apache 2.0)
- **Stage 1:** [timteh673/Qwen3.5-397B-A17B-Uncensored-GGUF](https://huggingface.co/timteh673/Qwen3.5-397B-A17B-Uncensored-GGUF)
- **Training data:** Custom reasoning dataset distilled from Anthropic Opus 4.6 outputs
- **Quantization:** llama.cpp
- **Hardware:** 8×NVIDIA H200 SXM5, 1.1TB VRAM

## Disclaimer

⚠️ This model has had safety alignment significantly reduced and has been fine-tuned for enhanced reasoning. It may generate content that is harmful, offensive, or inappropriate. Users are solely responsible for ensuring their use complies with applicable laws and ethical standards. This release is intended for research, testing, and controlled environments.
---

## ☕ Support This Work

<a href="https://buymeacoffee.com/timteh" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="217" height="60">
</a>

<p align="center">
  <img src="bmac-qr.png" alt="Buy Me a Coffee QR Code" width="250">
</p>

Every donation helps fund more open-weight model releases. ⚡ Forged on 8×NVIDIA H200 SXM5 | 1.1TB VRAM

### 💎 Crypto Donations

| Currency | Address |
|----------|---------|
| **BTC** | `bc1p4q7vpwucvww2y3x4nhps4y4vekye8uwm9re5a0kx8l6u5nky5ucszm2qhh` |
| **ETH** | `0xe5Aa16E53b141D42458ABeEDb00a157c3Fea2108` |
| **SOL** | `9CXwjG1mm9uLkxRevdMQiF61cr6TNHSiWtFRHmUEgzkG` |
