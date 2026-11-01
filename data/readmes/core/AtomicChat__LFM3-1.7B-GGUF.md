---
base_model: LiquidAI/LFM3-1.7B
license: other
license_name: lfm-open-license-v1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
language:
- en
- zh
- de
- fr
- es
- ja
- ar
- ko
pipeline_tag: text-generation
library_name: gguf
tags:
- gguf
- quantized
- lfm3
---

# LFM3-1.7B — GGUF (by AtomicChat)

<div style="display: flex; gap: 8px; align-items: center; margin-top: 10px; margin-bottom: 10px;">
  <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_lfm3_1_7b&utm_content=btn_atomic"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_atomic.png" width="162" alt="Atomic Chat"></a>
  <a href="https://discord.gg/8wGSsvmg4V"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_discord.png" width="119" alt="Discord"></a>
  <a href="https://github.com/AtomicBot-ai/Atomic-Chat"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_github.png" width="115" alt="GitHub"></a>
  <a href="https://x.com/atomic_chat_hq"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_x.png" width="108" alt="X"></a>
</div>
<ul style="margin: 0 0 12px 0;">
  <li>Built by the team behind <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_lfm3_1_7b&utm_content=bullet_app">Atomic Chat</a>, the app that runs open-weight models locally and offline.</li>
</ul>
<hr style="margin: 0 0 16px 0;">

Atomic-Dynamic (AD) GGUF quants of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), a dense short-convolution + gated-attention hybrid.

Each AD rung sets per-tensor types by role (FFN pressed hardest by depth band, `attn_gate` and `attn_k/v` kept high, the short-conv mixers tracked with attention, embeddings and head high) rather than a single uniform preset.

## Rungs

`top-1` is how often the rung picks the same next token as the original BF16 (30-language neutral set); mean KLD is the average divergence from BF16 (lower is better). LFM3-1.7B is a small hybrid model and is fairly quantization-sensitive.

| Rung | GB on disk | bpw | top-1 | mean KLD |
|---|---|---|---|---|
| Q8_0 | 1.85 | 8.51 | 96.3% | 0.004 |
| AD-Q6_K | 1.59 | 7.31 | 94.5% | 0.010 |
| AD-Q5_K_M | 1.31 | 6.03 | 90.3% | 0.034 |
| AD-Q4_K_M | 1.13 | 5.20 | 84.6% | 0.087 |
| AD-IQ4_XS | 1.09 | 5.02 | 83.2% | 0.105 |
| AD-IQ3_S | 0.92 | 4.23 | 77.0% | 0.203 |

**AD-Q4_K_M** is the recommended default. **AD-IQ3_S** is a research-grade rung (small, lower fidelity). The AD rungs replace llama.cpp's stock presets, which have no imatrix, at every size. Full metrics go to the `-metrics` repo after audit.

## Run (llama.cpp)

Needs a build with LFM3 support (merged in llama.cpp #31252; these files were produced at llama.cpp `19cce69`).

```bash
llama-cli   -hf AtomicChat/LFM3-1.7B-GGUF:AD-Q4_K_M -p "Hello"
llama-server -hf AtomicChat/LFM3-1.7B-GGUF:AD-Q4_K_M -c 8192 --jinja
```

## Base model & license

Base model: [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B). License: LFM Open License v1.0 (see `LICENSE`).

Quants by AtomicChat.
