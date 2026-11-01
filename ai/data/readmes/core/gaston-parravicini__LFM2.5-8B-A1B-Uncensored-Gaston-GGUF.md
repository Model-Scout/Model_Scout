---
license: other
license_name: lfm-open-license-v1
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
base_model: LiquidAI/LFM2.5-8B-A1B
language:
- en
- es
- fr
- de
- zh
- ja
- ko
- ar
tags:
- gguf
- abliterated
- uncensored
- imatrix
- lfm2
- lfm2moe
- lfm2.5
- liquid-ai
- reasoning
- thinking
- hybrid-architecture
- conv-attention
- moe
- llama-cpp
- conversational
- text-generation
pipeline_tag: text-generation
---

![LFM2.5 Uncensored Banner](LFM2_5_UNCENSURED.png)

# LFM2.5-8B-A1B — Uncensored by Gastón Parravicini

> **First publicly available uncensored/abliterated GGUF of LFM2.5-8B-A1B.**  
> Base model released May 28, 2026. This release: May 29, 2026.

---

## TL;DR

Liquid AI dropped LFM2.5-8B-A1B yesterday. It refused everything. Today it doesn't.

**Refusal rate: 1/100 on AdvBench. Reasoning intact. iMatrix quants. Same-day release.**

---

## About LFM2.5-8B-A1B

[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) is Liquid AI's latest edge model — a hybrid **convolution + attention MoE** architecture with:

- **8.3B total parameters, 1.5B active per token** (MoE with 32 experts, 4 active)
- **128K context window** (up from 32K in LFM2)
- **Trained on 38T tokens** with large-scale reinforcement learning
- **Reasoning model** — generates `<think>...</think>` chains before answering
- Fastest in its class: 18,500 tokens/sec on H100 at high concurrency

The architecture is **not a standard Transformer**. It combines:
- 18 layers of gated short convolutions (LIV blocks) — O(n) complexity
- 6 layers of Grouped Query Attention (GQA) — O(n²) for global context
- MoE feed-forward with sparse expert routing

This hybrid design is what makes it fast. It's also what makes abliteration non-trivial.

---

## Why standard abliteration tools don't work here

Every existing abliteration tool — NousResearch, Heretic, OBLITERATUS — targets standard Transformer weight matrices:

```
self_attn.o_proj     ← doesn't exist in LFM2.5
mlp.down_proj        ← doesn't exist in LFM2.5
```

Running `sharded_ablate.py` on LFM2.5 without patching results in **0 shards modified**. The model is completely unchanged. This is why no abliterated version existed before this release.

---

## How this was done

### 1. Architecture reverse engineering

Full manual inspection of the LFM2.5 weight map to identify the correct abliteration targets:

```
Layer type          | Target matrix
--------------------|----------------------------------
Conv LIV block      | conv.out_proj    [2048, 2048]
GQA Attention block | self_attn.out_proj [2048, 2048]
Dense FFN (L0-L1)   | feed_forward.w2  [2048, 7168]
```

Key insight: `conv.in_proj` has shape `[6144, 2048]` — a 3x expansion projection that **cannot** be abliterated with the standard direction subtraction without a dimension mismatch error. Excluded intentionally.

### 2. Patch to sharded_ablate.py

```python
# LFM2/LFM2.5 hybrid architecture support patch
# by Gastón Parravicini — May 29, 2026
# Enables abliteration of lfm2moe models in NousResearch/llm-abliteration

lfm2_patterns = [
    f"{layer_prefix}.layers.{layer}.self_attn.out_proj.weight",
    f"{layer_prefix}.layers.{layer}.conv.out_proj.weight",
    f"{layer_prefix}.layers.{layer}.feed_forward.w2.weight",
]
```

Without this patch: **0/10 shards modified**.  
With this patch: **6/10 shards modified**, all correct targets.

### 3. Refusal direction analysis

Used `analyze.py` to map refusal signal strength across all 24 layers:

| Layers | Est. Signal Quality | Type |
|--------|-------------------|------|
| 0–2 | ~0.000 | Skip |
| 3–10 | 0.010–0.062 | Low |
| **11–17** | **0.108–0.240** | **Peak — abliterated here** |
| 18–23 | 0.049–0.145 | High |

Layer 16 was the peak signal layer (Est. Signal Quality: **0.242**). Used as the primary measurement reference for all ablated layers.

### 4. Abliteration parameters

```yaml
layers: 11–23
measurement: layer 16 (peak refusal signal)
scale: 2.0
flags: --projected --normpreserve
```

- `--projected`: orthogonalizes the refusal direction against the harmless direction before subtracting — cleaner removal, less capability damage
- `--normpreserve`: preserves weight matrix row norms after projection — prevents magnitude drift

### 5. Weight diff verification

Post-abliteration comparison against base model (via `compare.py`):

| Metric | Value |
|--------|-------|
| Avg weight diff | ~4–5 × 10⁻⁴ |
| Max weight diff | ~1–3% |
| Layers 0–10 | **Zero diff** — untouched ✅ |
| Layers 11–23 | Surgical modifications only ✅ |

Modifications are minimal and targeted. The model's general capabilities are preserved.

---

## Abliteration results

| Metric | Result |
|--------|--------|
| Refusal rate (AdvBench 100 prompts) | **1/100 (1%)** |
| Reasoning (`<think>` tags) | ✅ Fully intact |
| General capability | ✅ Verified |
| Same-day release | ✅ May 29, 2026 |

The single remaining refusal out of 100 is an edge case. The model reasons freely — the `<think>` block no longer contains refusal logic.

---

## Available quants

All generated with **iMatrix** calibration on harmful/harmless instruction data.

| File | Size | Use case |
|------|------|----------|
| `...IQ4_XS.gguf` | ~4.4 GB | Maximum compression |
| `...Q4_K_M.gguf` | ~4.9 GB | ⭐ **Recommended — best balance** |
| `...Q5_K_M.gguf` | ~5.7 GB | Better quality |
| `...Q6_K.gguf` | ~7.2 GB | High quality |
| `...Q8_0.gguf` | ~8.6 GB | Near-lossless |
| `...F16.gguf` | ~16 GB | Full precision |

---

## Usage

### llama-server
```bash
llama-server \
  -m LFM2.5-8B-A1B-Uncensored-Gaston-Q4_K_M.gguf \
  -ngl 99 -c 8192 --port 8080
```

### Ollama
```bash
ollama run hf.co/gaston-parravicini/LFM2.5-8B-A1B-Uncensored-Gaston-GGUF:Q4_K_M
```

### llama-cli (quick test)
```bash
llama-cli \
  -m LFM2.5-8B-A1B-Uncensored-Gaston-Q4_K_M.gguf \
  -ngl 99 -p "<|startoftext|><|im_start|>user\nHello!<|im_end|>\n<|im_start|>assistant\n"
```

---

## Notes

**Tool calling:** LFM2.5 supports tool calling natively in `transformers`. In llama.cpp there is a known bug with the chat template that breaks tool use — upstream is debugging (PR #23826).

**Prompt cache:** lfm2moe models clear the KV cache on every turn in llama.cpp (known upstream issue). Output quality is unaffected.

**Reasoning:** This is a thinking model. Responses include `<think>...</think>` before the final answer. This is expected and correct.

---

## Base model

- **Model:** [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)
- **Architecture:** lfm2moe — hybrid conv (LIV) + GQA + MoE
- **Parameters:** 8.3B total / 1.5B active
- **Context:** 128K tokens
- **License:** [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE)

---

*Released by **Gastón Parravicini** — [huggingface.co/gaston-parravicini](https://huggingface.co/gaston-parravicini)*  
*Architecture patch for lfm2moe abliteration — first of its kind.*
