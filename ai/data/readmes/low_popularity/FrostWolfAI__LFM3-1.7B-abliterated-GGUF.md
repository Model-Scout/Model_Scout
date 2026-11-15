---
base_model: FrostWolfAI/LFM3-1.7B-abliterated
base_model_relation: quantized
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
tags:
- gguf
- llama.cpp
- liquid
- lfm3
- edge
- on-device
- heretic
- ara
- uncensored
- decensored
- abliterated
- local-llm
---

# LFM3-1.7B-abliterated-GGUF

GGUF quantizations of [**FrostWolfAI/LFM3-1.7B-abliterated**](https://huggingface.co/FrostWolfAI/LFM3-1.7B-abliterated)
— an abliterated (decensored) [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) produced with
[Heretic v2 (ARA)](https://github.com/p-e-w/heretic): **1/100 refusals at KL 0.0555** (base refuses 91/100).

> **Requires a recent llama.cpp build with `lfm3` architecture support** (also works in Ollama / LM Studio
> builds that bundle a recent llama.cpp). Older builds will not load these files.

## Quants

| File | Bits | Status |
|---|---|---|
| `LFM3-1.7B-abliterated-BF16.gguf`  | 16 | ✅ available (full precision) |
| `…-Q8_0 / Q6_K / Q5_K_M / Q4_K_M / Q4_K_S / Q3_K_M / Q2_K` | 8–2 | 🔜 being added |

> Smaller K-quants are being added. They require quantizing with a **recent llama.cpp build that
> supports `lfm3`** (older `llama-quantize` reports `unknown model architecture: 'lfm3'`). Until then,
> the BF16 GGUF runs on any recent `lfm3`-capable llama.cpp, or you can quantize it yourself.

## Run

```bash
llama-cli -hf FrostWolfAI/LFM3-1.7B-abliterated-GGUF:Q4_K_M
# or local:
llama-server -m LFM3-1.7B-abliterated-Q4_K_M.gguf --jinja
```

LFM3 is a thinking model (`<think>…</think>`) with native tool-calling. Use `--jinja` so the chat
template (and tool-calling) render correctly.

## License

**LFM Open License v1.0** (`lfm1.0`), inherited from the base. See [`LICENSE`](LICENSE). Refusal behavior
has been removed — released for security research and local use; you are responsible for your use.

Base: Liquid AI · Abliteration: [Heretic](https://github.com/p-e-w/heretic) by p-e-w · Build: FrostWolfAI Labs
