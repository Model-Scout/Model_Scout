---
license: apache-2.0
tags:
  - uncensored
  - abliterated
  - mistral
  - moe
  - gguf
  - text-generation
  - conversational
  - mistral-small-4
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - zh
  - ja
  - ko
  - multilingual
pipeline_tag: text-generation
base_model: mistralai/Mistral-Small-4-119B-Instruct-2503
model_type: mistral
---

# Mistral-Small-4-119B-Uncensored-GGUF

> ☕ **If this model saves you time, [buy me a coffee](https://buymeacoffee.com/timteh)!** Every cup fuels more open-weight releases.


>
Mistral Small 4 119B uncensored via abliteration by TIMTEH. **Refusal direction removed from layers 9-35.**

## About

Full abliteration of [mistralai/Mistral-Small-4-119B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-4-119B-Instruct-2503) — no dataset changes, no fine-tuning, no capability loss. The refusal direction was identified and projected out of the model's residual stream across decoder layers 9-35, covering attention output projections and MLP down projections.

This is the **first standard GGUF uncensored release** of Mistral Small 4 119B. The only other uncensored variant is [dealignai's JANG/MLX format](https://huggingface.co/dealignai) (Apple Silicon only, ~80 downloads).

## Architecture

- **119B total parameters** — Mixture of Experts (128 routed experts + 1 shared expert per layer, 4 active per token)
- **36 decoder layers** with Multi-Latent Attention (MLA): kv_lora_rank=256, q_lora_rank=1024
- **Multimodal base** (vision tower removed for text-only GGUF — text capabilities fully preserved)
- Released March 23, 2026 by Mistral AI

## Downloads

| File | Quant | Size | Use Case |
|------|-------|------|----------|
| Mistral-Small-4-119B-Uncensored-Q2_K.gguf | Q2_K | 41 GB | Minimum viable — fits 48GB+ |
| Mistral-Small-4-119B-Uncensored-Q3_K_M.gguf | Q3_K_M | 54 GB | Budget quality — 64GB+ recommended |
| Mistral-Small-4-119B-Uncensored-Q4_K_M.gguf | Q4_K_M | 68 GB | **Best balance** — 80GB+ VRAM |
| Mistral-Small-4-119B-Uncensored-Q5_K_M.gguf | Q5_K_M | 79 GB | High quality — 96GB+ VRAM |
| Mistral-Small-4-119B-Uncensored-Q6_K.gguf | Q6_K | 91 GB | Near-lossless — 2×48GB or 128GB+ |
| Mistral-Small-4-119B-Uncensored-Q8_0.gguf | Q8_0 | 118 GB | Reference quality — 128GB+ VRAM |
| Mistral-Small-4-119B-Uncensored-BF16.gguf | BF16 | 222 GB | Full precision — 256GB+ VRAM |

## Recommended Settings

- **Temperature:** 0.7-0.9 for creative, 0.3-0.5 for factual
- **Rep penalty:** 1.05-1.15 (important for abliterated models — prevents loops)
- **Top-P:** 0.9 | **Top-K:** 40
- **Context:** Up to 32K tokens (model supports 128K but GGUF runtimes vary)

## Abliteration Method

1. Model loaded across 8×H200 SXM5 GPUs with FP8→BF16 dequantization
2. Activations extracted from 30 harmful + 30 harmless prompt pairs
3. Per-layer refusal direction computed via mean difference of activations
4. Refusal direction projected out of `o_proj` (attention output) and `down_proj` (MLP) for layers 9-35
5. Modified weights saved as BF16 safetensors → converted to GGUF → quantized

No training, no dataset contamination, no capability degradation. The model retains 100% of its original knowledge and reasoning ability — only the refusal behavior is removed.

For details on abliteration, see [mlabonne's original blog post](https://huggingface.co/blog/mlabonne/abliteration).

## Usage

Works with llama.cpp, LM Studio, Jan, koboldcpp, Ollama, and other GGUF-compatible runtimes.

```bash
# llama.cpp
llama-cli -m Mistral-Small-4-119B-Uncensored-Q4_K_M.gguf \
  --jinja -c 32768 -ngl 99

# Ollama (after creating Modelfile)
ollama run mistral-small-4-uncensored
```

```
# Chat template
<s>[INST] Your message here [/INST]
```

## Notes

- This is a **text-only** GGUF. The vision tower from the original multimodal model was not included in conversion. All text/reasoning/coding capabilities are fully preserved.
- Abliterated models may occasionally include brief disclaimers in responses — this is residual behavior from base training, not a refusal.
- As with all uncensored models, **use responsibly.** The removal of safety guardrails means the model will comply with a wider range of requests.

## Other Models by TIMTEH

- More coming soon — follow [@timteh673](https://huggingface.co/timteh673) for updates.

## Support

If you find this useful, consider supporting the work:

☕ **[Buy Me a Coffee](https://buymeacoffee.com/timteh)**



All models are forged on 8×NVIDIA H200 SXM5 (1.1TB VRAM) — real hardware, real quantization, no compromises.

## Credits

- **Base model:** [Mistral AI](https://huggingface.co/mistralai/Mistral-Small-4-119B-Instruct-2503)
- **Abliteration technique:** [mlabonne](https://huggingface.co/blog/mlabonne/abliteration)
- **Quantization:** [llama.cpp](https://github.com/ggerganov/llama.cpp)
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