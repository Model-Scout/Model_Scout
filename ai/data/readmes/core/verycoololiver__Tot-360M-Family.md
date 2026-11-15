---
license: apache-2.0
language:
  - en
  - ko
library_name: gguf
pipeline_tag: text-generation
tags:
  - gguf
  - llama.cpp
  - lmstudio
  - pocketpal
  - raspberry-pi
  - mobile
  - offline-ai
  - small-language-model
  - pretrained-from-scratch
  - tot-360m
  - obstudio
---

# Tot-360M Family (GGUF) ? 345M Local AI Model Trained From Scratch

**Official Project Hub & Live Raspberry Pi 4 Demo:**
- **Website:** [OB Studio (obstudio.org)](https://obstudio.org/)
- **Live Browser Demo (Running on a 4 GB Raspberry Pi 4):** [https://obstudio.org/tot-360m/demo/](https://obstudio.org/tot-360m/demo/)
- **Full Technical Specification & Loss Curve:** [https://obstudio.org/tot-360m/](https://obstudio.org/tot-360m/)
- **Tot Desktop AI Companion for Windows:** [https://obstudio.org/tools/tot/](https://obstudio.org/tools/tot/)
- **Drift Privacy-First AI Browser:** [https://obstudio.org/tools/drift/](https://obstudio.org/tools/drift/)

---

## Overview

**Tot-360M** is a community-funded **345,359,296-parameter** (`314,639,296` non-embedding) decoder-only Transformer language model trained **100% from random initialization (from scratch)** by Oliver at [OB Studio](https://obstudio.org/) across 8-core Kaggle Cloud TPU v5e-8 instances and Dual NVIDIA Tesla T4 GPUs.

Unlike fine-tuned Qwen or Llama derivatives, Tot-360M uses its own 32,000-token byte-level BPE tokenizer and was pre-trained and post-trained step-by-step in public. It exports directly to a standard **Qwen3-compatible GGUF layout** so that stock `llama.cpp`, **LM Studio**, **PocketPal AI** (iOS & Android), and **ChatterUI** can run it 100% offline with zero custom C++ patches.

At **241 MiB (`Q4_K_M`)** and **351 MiB (`Q8_0`)**, Tot-360M runs smoothly on:
- **Android & iPhone** (under 420 MB RAM in PocketPal AI or ChatterUI)
- **Raspberry Pi 4 & Pi 5 (4 GB / 8 GB RAM)**
- **Everyday Windows, macOS & Linux laptops** without a discrete GPU (35+ tok/s on CPU)

---

## Architecture & Hyperparameters

| Parameter | Value |
| :--- | :--- |
| **Architecture** | Decoder-only Transformer (Qwen3-compatible GGUF tensor layout) |
| **Total Parameters** | `345,359,296` (tied input/output embeddings) |
| **Non-Embedding Parameters** | `314,639,296` |
| **Layers (`n_layers`)** | `32` |
| **Hidden Size (`d_model`)** | `960` |
| **Intermediate (`d_ff`)** | `2,560` (SwiGLU MLP) |
| **Attention Heads** | `15` Query / `5` KV (3:1 GQA, `head_dim = 64`, QK-Norm) |
| **Positional Encoding** | RoPE (`theta = 10,000.0`) |
| **Normalization** | RMSNorm (`eps = 1e-6`) |
| **Vocabulary Size** | `32,000` (byte-level BPE) |
| **Context Window** | `4,096` tokens (expanded from `1,024` in Run 4) |
| **License** | Apache-2.0 |

---

## Training Runs & Checkpoints

All checkpoints and live telemetry are documented on the [Tot-360M Technical Specification page](https://obstudio.org/tot-360m/) and can be tested side-by-side on the [Live Raspberry Pi 4 Demo](https://obstudio.org/tot-360m/demo/):

| Checkpoint | Steps | Cumulative Tokens | Context | Loss | GGUF Downloads |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Run 1 (Batch 1)** | `439 ? 24,785` | `405,680,880` | `1,024` | `4.74 ? 2.73` | [Q4_K_M](https://obstudio.org/downloads/tot_360m_run1_q4_k_m.gguf) ? [Q8_0](https://obstudio.org/downloads/tot_360m_run1_q8_0.gguf) |
| **Run 2 (Batch 2)** | `24,785 ? 56,058` | `917,557,344` | `1,024` | `3.18 ? 2.81` | [Q4_K_M](https://obstudio.org/downloads/tot_360m_run2_q4_k_m.gguf) ? [Q8_0](https://obstudio.org/downloads/tot_360m_run2_q8_0.gguf) |
| **Run 3 (Batch 3)** | `56,058 ? 87,395` | `1,430,481,360` | `1,024` | `2.61 ? 2.03` | [Q4_K_M](https://obstudio.org/downloads/tot_360m_run3_q4_k_m.gguf) ? [Q8_0](https://obstudio.org/downloads/tot_360m_run3_q8_0.gguf) |
| **Run 3 Part 2 (Irish-360M)** | `87,395 ? 95,816` | `1,568,316,288` | `1,024` | `2.20 ? 2.00` | `run3_part2_1568m/` (in this repo) |
| **Run 4 (4K Context Expansion)** | `95,816 ? 101,591` | `1,662,910,788` | `4,096` | `1.39 ? 1.24` | `run4_instruct_4k/` (in this repo) |
| **Run 5 (4K Base)** | `101,591 ? 109,958` | `1,799,962,248` | `4,096` | `1.38 ? 1.14` | [Q4_K_M](https://obstudio.org/downloads/tot_360m_run5_4k_q4_k_m.gguf) ? [Q8_0](https://obstudio.org/downloads/tot_360m_run5_4k_q8_0.gguf) |
| **SFT v2 (Post-Trained ? EN + Code)** | `109,958 ? 113,958` | `1,865,482,248` | `4,096` | `2.64 ? 1.14` (masked) | `tot_360m_sft_v2_q4_k_m.gguf` ? `tot_360m_sft_v2_q8_0.gguf` |

---

## Quick Start (`llama.cpp`, LM Studio & PocketPal AI)

### 1. Command Line (`llama.cpp`)

```bash
./llama-cli -m tot_360m_sft_v2_q4_k_m.gguf -c 4096 \
  -p "<|im_start|>user\nWrite a Python function to compute gravitational force.<|im_end|>\n<|im_start|>assistant\n" \
  -n 256 --temp 0.7 --repeat-penalty 1.15
```

### 2. Android & iPhone (PocketPal AI / ChatterUI)
1. Install **PocketPal AI** or **ChatterUI** on your phone.
2. Search Hugging Face for `verycoololiver/Tot-360M-Family` or download `tot_360m_sft_v2_q4_k_m.gguf` (241 MiB).
3. Set context length to `4096` and chat 100% offline in airplane mode.
Full step-by-step phone & Raspberry Pi guide: [How to Run a Free Offline AI Model on Your Phone, Laptop, or Raspberry Pi 4](https://obstudio.org/blog/free-local-ai-for-phone-raspberry-pi-gguf/).

---

## Engineering Build Logs & Post-Training Notes

- [Tot-360M SFT v2 (1.87B) Is Live on a Raspberry Pi 4: Why We Switched to 100% English + Code](https://obstudio.org/blog/tot-360m-sft-v2-live-raspberry-pi-demo/)
- [How to Run a Free Offline AI Model on Your Phone, Laptop, or Raspberry Pi 4 (253 MB GGUF Guide)](https://obstudio.org/blog/free-local-ai-for-phone-raspberry-pi-gguf/)
- [Tot-360M at 1.66B Tokens: 4K Context Expansion & Post-Training Pipeline](https://obstudio.org/blog/tot-360m-first-post-trained-4k-checkpoint/)
- [Tot-360M Run 2 Complete (917M Tokens): Loss Curve & First GGUF Checkpoints](https://obstudio.org/blog/2nd-training-run-done/)
- [Tot-360M's First Real Training Run: 405 Million Tokens on a Kaggle TPU](https://obstudio.org/blog/tot-360m-first-real-training-run/)
- [More Browser Simulations, Games & Developer Tools at OB Studio](https://obstudio.org/work/)
