---
base_model: LiquidAI/LFM3-VL-2B
license: other
license_name: lfm-open-license-v1.0
language:
- en
- zh
- de
- fr
- es
- ja
- ar
- ko
pipeline_tag: image-text-to-text
library_name: gguf
tags:
- gguf
- quantized
- lfm3
- multimodal
---

# LFM3-VL-2B — GGUF (by AtomicChat)

<div style="display: flex; gap: 8px; align-items: center; margin-top: 10px; margin-bottom: 10px;">
  <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_lfm3_vl_2b&utm_content=btn_atomic"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_atomic.png" width="162" alt="Atomic Chat"></a>
  <a href="https://discord.gg/8wGSsvmg4V"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_discord.png" width="119" alt="Discord"></a>
  <a href="https://github.com/AtomicBot-ai/Atomic-Chat"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_github.png" width="115" alt="GitHub"></a>
  <a href="https://x.com/atomic_chat_hq"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_x.png" width="108" alt="X"></a>
</div>
<ul style="margin: 0 0 12px 0;">
  <li>Built by the team behind <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_lfm3_vl_2b&utm_content=bullet_app">Atomic Chat</a>, the app that runs open-weight models locally and offline.</li>
</ul>
<hr style="margin: 0 0 16px 0;">

Atomic-Dynamic (AD) GGUF quants of [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B), a vision-language model on the LFM3 hybrid (short-convolution + gated attention) backbone.

Per-tensor AD layout by role (FFN pressed by depth band, `attn_gate` / `attn_k/v` kept high, short-conv mixers tracked with attention, embeddings and head high).

## Rungs (language model)

`top-1` is how often the rung picks the same next token as the original BF16 (30-language neutral set); mean KLD is the average divergence from BF16 (lower is better). This is a small hybrid model and is fairly quantization-sensitive.

| Rung | GB on disk | bpw | top-1 | mean KLD |
|---|---|---|---|---|
| Q8_0 | 1.85 | 8.51 | 96.6% | 0.003 |
| AD-Q6_K | 1.59 | 7.31 | 94.9% | 0.006 |
| AD-Q5_K_M | 1.31 | 6.03 | 90.7% | 0.024 |
| AD-Q4_K_M | 1.13 | 5.20 | 85.8% | 0.061 |
| AD-IQ4_XS | 1.09 | 5.02 | 83.8% | 0.078 |
| AD-IQ3_S | 0.92 | 4.23 | 78.3% | 0.151 |

**AD-Q4_K_M** is the recommended default. **AD-IQ3_S** is a research-grade rung. The AD rungs replace llama.cpp's stock presets (no imatrix) at every size. Full metrics go to the `-metrics` repo after audit.

## Vision

The vision projector is included: **`mmproj-LFM3-VL-2B-F16.gguf`** (BF16 also available). Pair it with any rung via `llama-mtmd-cli`:

```bash
llama-mtmd-cli -m LFM3-VL-2B-AD-Q4_K_M.gguf --mmproj mmproj-LFM3-VL-2B-F16.gguf --image img.jpg -p "Describe the image"
```

## Run (llama.cpp, text)

Needs a build with LFM3 support (merged in llama.cpp #31252; produced at llama.cpp `19cce69`).

```bash
llama-cli -hf AtomicChat/LFM3-VL-2B-GGUF:AD-Q4_K_M -p "Hello"
```

## Base model & license

Base model: LiquidAI/LFM3-VL-2B. License: LFM Open License v1.0 (see `LICENSE`).

Quants by AtomicChat.
