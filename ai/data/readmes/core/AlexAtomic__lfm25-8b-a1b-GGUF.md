---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/raw/main/LICENSE
thumbnail: https://huggingface.co/AlexAtomic/lfm25-8b-a1b-GGUF/resolve/main/hero.png
base_model:
- LiquidAI/LFM2.5-8B-A1B
base_model_relation: quantized
quantized_by: AlexAtomic
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
pipeline_tag: text-generation
library_name: gguf
tags:
- atomic-chat
- lfm
- liquid
- lfm2
- gguf
- imatrix
- quantized
- llama.cpp
---

<center>

<div style="display:flex; justify-content:center; align-items:center; gap:2%; max-width:560px; margin:0 auto;">
<a href="https://atomic.chat" style="flex:0 1 auto; min-width:0;"><img src="https://huggingface.co/AlexAtomic/lfm25-8b-a1b-GGUF/resolve/main/pill_atomic_v3.png" alt="Atomic Chat" style="width:100%; height:auto; max-width:186px;"></a>
<a href="https://discord.gg/8wGSsvmg4V" style="flex:0 1 auto; min-width:0;"><img src="https://huggingface.co/AlexAtomic/lfm25-8b-a1b-GGUF/resolve/main/pill_discord_v3.png" alt="Join Discord" style="width:100%; height:auto; max-width:184px;"></a>
<a href="https://github.com/AtomicBot-ai/Atomic-Chat" style="flex:0 1 auto; min-width:0;"><img src="https://huggingface.co/AlexAtomic/lfm25-8b-a1b-GGUF/resolve/main/pill_github_v3.png" alt="GitHub" style="width:100%; height:auto; max-width:141px;"></a>
</div>

<br/>

<img src="https://huggingface.co/AlexAtomic/lfm25-8b-a1b-GGUF/resolve/main/hero.png" alt="LFM2.5 8B A1B" style="width:100%; max-width:100%; height:auto; margin-bottom:0.6em;"/>

<div style="display:flex; justify-content:center; gap:0.5em;">
<a href="https://huggingface.co/LiquidAI/LFM2.5-8B-A1B"><strong>Base model: LiquidAI/LFM2.5-8B-A1B</strong></a>
</div>
</center>

**LFM2.5 8B A1B**, self-quantized to GGUF by [Atomic Chat](https://atomic.chat). Built straight from Liquid AI's original weights with a per-tensor importance matrix. Runs fully offline.

## Highlights

- **Sparse MoE**: 8.3B total parameters, only 1.5B active per token.
- **LFM2 hybrid architecture**: 24 layers (18 double-gated LIV convolution blocks + 6 GQA attention), built on LFM2 with extended pre-training and reinforcement learning.
- **On-device assistant**: designed to chain tool calls and follow complex instructions, with day-one support for llama.cpp, MLX, vLLM and SGLang.
- **Reasoning model**: assistant turns include an explicit chain of thought before the final answer.
- **128K context**, 128,000 vocabulary, trained on a 38 trillion token budget.
- **Multilingual**: English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish.

> [!NOTE]
> These GGUFs are **self-quantized from the original weights**, not a repack. The importance matrix keeps low-bit quants closer to the full-precision model.

> [!IMPORTANT]
> Always pass `--jinja` so the **LFM2.5 8B A1B chat template** is applied. Without it the model can emit malformed turns.

## Model Overview

| Property | Value |
|---|---|
| Base model | `LiquidAI/LFM2.5-8B-A1B` |
| Total / active parameters | 8.3B total, 1.5B active (MoE) |
| Layers | 24 (18 LIV conv + 6 GQA) |
| Context length | 128,000 |
| Architecture | LFM2.5 hybrid (built on LFM2, extended pre-training + RL) |
| This repo | GGUF quants (imatrix) |

<img src="https://huggingface.co/AlexAtomic/lfm25-8b-a1b-GGUF/resolve/main/benchmark.png" alt="LFM2.5 8B A1B benchmark scores" style="width:100%; max-width:900px;"/>

Scores are Liquid AI's published results for the base `LiquidAI/LFM2.5-8B-A1B`. Quantization preserves the large majority of this; `Q4_K_M` and up sit within a point or two of full precision.

## Choosing a quant

| Quant | Size | Notes |
|---|---|---|
| `Q2_K` | 3.2 GB | Smallest. Minimal RAM, clear quality drop. |
| `IQ3_M` | 3.8 GB | Beats Q3 at similar size thanks to imatrix. Best low-RAM pick. |
| `Q3_K_M` | 4.1 GB | Low quality but usable. |
| `Q3_K_L` | 4.4 GB | A step above Q3_K_M. |
| `IQ4_XS` | 4.6 GB | Excellent quality for size. Recommended low-bit. |
| `Q4_K_S` | 4.9 GB | Compact Q4, fast. |
| **`Q4_K_M`** | 5.2 GB | **Recommended default. Best balance of size, speed and quality.** |
| **`UD-Q4_K_XL`** | 5.2 GB | **Dynamic. Embeddings and output kept at Q8_0 for higher quality at a Q4 footprint.** |
| `Q5_K_S` | 5.9 GB | Higher quality. |
| `Q5_K_M` | 6.0 GB | Higher quality, low loss. |
| `Q6_K` | 7.0 GB | Near lossless. |
| `Q8_0` | 9.0 GB | Effectively lossless, reference quality. |

> [!TIP]
> Pick the largest file that fits your (V)RAM with room for context. `Q4_K_M` or `UD-Q4_K_XL` is the sweet spot for most setups; `Q6_K` or `Q8_0` for maximum fidelity.

## Get started

Run LFM2.5 8B A1B locally with:

- **[Atomic Chat](https://atomic.chat):** the easiest path. Open the app, search `AlexAtomic/lfm25-8b-a1b-GGUF`, pick a quant, hit **Use this model**.
- **llama.cpp:** `llama-server -hf AlexAtomic/lfm25-8b-a1b-GGUF:Q4_K_M --jinja -c 8192`
- **Ollama:** `ollama run hf.co/AlexAtomic/lfm25-8b-a1b-GGUF:Q4_K_M`
- **LM Studio / Jan:** search the repo id, download any quant.

## Best practices

| Parameter | Value |
|---|---|
| temperature | 0.2 |
| top_k | 80 |
| repetition_penalty | 1.05 |

Liquid AI's recommended generation parameters.

## Run in llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cmake llama.cpp -B llama.cpp/build -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --target llama-cli llama-server
```

```bash
./llama.cpp/build/bin/llama-server \
    -hf AlexAtomic/lfm25-8b-a1b-GGUF:UD-Q4_K_XL \
    --jinja -ngl 99 -c 8192 -fa on
```

## How these were made

1. Download `LiquidAI/LFM2.5-8B-A1B` (original weights).
2. Convert to f16 GGUF with [llama.cpp](https://github.com/ggerganov/llama.cpp).
3. Build an importance matrix over `calibration_datav3` (100 chunks).
4. Quantize the full ladder with `--imatrix`.
5. `UD-Q4_K_XL` additionally pins the token-embedding and output tensors to `Q8_0`.

## License

Released by Liquid AI under their LFM1.0 license. Quantized by Atomic Chat.

