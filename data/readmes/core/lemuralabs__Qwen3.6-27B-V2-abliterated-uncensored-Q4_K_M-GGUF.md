---
license: apache-2.0
language:
- en
- zh
- multilingual
tags:
- text-generation
- image-text-to-text
- gguf
- llama.cpp
- safetensors
- qwen
- qwen3
- qwen3.5
- qwen3.6
- claude-opus-distill
- reasoning
- vision
- multimodal
- abliterated
- refusal-ablated
- uncensored
- q4_k_m
- conversational
base_model:
- Jackrong/Qwopus3.6-27B-v2
- Qwen/Qwen3.6-27B
pipeline_tag: image-text-to-text
library_name: gguf
---

<p align="center">
  <img src="logo.png" alt="Lemura Labs" width="110"/>
</p>

# Qwen3.6-27B-V2-abliterated-uncensored-Q4_K_M-GGUF

![Format](https://img.shields.io/badge/Format-GGUF-0b7285?style=flat) ![Task](https://img.shields.io/badge/Task-Vision%20+%20Text-5f3dc4?style=flat) ![Params](https://img.shields.io/badge/Params-27B-1864ab?style=flat) ![Type](https://img.shields.io/badge/Type-Abliterated-862e9c?style=flat) ![Quant](https://img.shields.io/badge/Quant-Q4__K__M-1f6feb?style=flat) ![Size](https://img.shields.io/badge/Size-16%20GB-495057?style=flat) ![Refusals](https://img.shields.io/badge/Refusals-91%2F100%20to%204%2F100-2ea44f?style=flat) ![KL drift](https://img.shields.io/badge/KL%20drift-0.0176-2f9e44?style=flat) ![License](https://img.shields.io/badge/License-apache--2.0-6c757d?style=flat)


> Yes — **MULTIMODAL.** Bundled `mmproj.gguf` (~928 MB, F16) preserves the full Qwen3.6-VL vision tower. Use it with `llama-server --mmproj` or `llama-mtmd-cli` for text + image inference.

**Q4_K_M (4-bit K-quant medium, ~4.92 effective BPW)** of a abliterated Qwen 3.6 27B v2 (the Jackrong Claude-Opus reasoning distill of Qwen 3.6 27B). Refusals reduced from **91/100 → 4/100** with KL drift of just **0.0176**. By the Lemura Labs research team.

---

## TL;DR

| Property | Value |
|----------|-------|
| **Disk size** | ~16 GB (15.4 GB LM + 928 MB mmproj) |
| **BPW** | ~4.92 (Q4_K_M) |
| **Scheme** | llama.cpp Q4_K_M — super-block K-quantization with mixed Q4_K/Q6_K for attention-V and FFN-down. Industry-standard "best balance" quant — the most-downloaded GGUF format on HuggingFace. |
| **Refusal rate (the ablation toolkit, n=100)** | **4/100** (vs vanilla Qwen 3.6 **91/100**) |
| **KL divergence vs vanilla (at BF16)** | **0.0176** |
| **Vision** | Yes — via paired `mmproj.gguf` |
| **Recommended RAM/VRAM** | 24 GB+ Apple Silicon / 16 GB GPU |
| **Runtime** | stock `ggml-org/llama.cpp` (any recent build) — no custom fork needed for Q4_K_M. |
| **Released by** | Lemura Labs |

---

## All Qwen3.6-27B variants

The full Qwen3.6-27B family from Lemura Labs — same abliterated weights (refusal 4/100, KL 0.0176), different quant schemes for different runtimes.

| Quant | Format | BPW | Disk | Vision | Runtime | Link |
|---|---|---|---|---|---|---|
| 8-bit | MLX | 8.50 | ~27 GB | Yes — native | mlx-vlm | [`…-8-bit-mlx`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-8-bit-mlx) |
| 6-bit | MLX | 6.66 | ~21 GB | Yes — native | mlx-vlm | [`…-6-bit-mlx`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-6-bit-mlx) |
| OptiQ 3.7bpw | MLX | ~3.7 | ~14 GB | Yes — ViT spliced | mlx-vlm | [`…-OptiQ-3.7bpw-mlx`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-OptiQ-3.7bpw-mlx) |
| Q8_0 | GGUF | 8.50 | ~28 GB | Yes — via mmproj | llama.cpp | [`…-8-bit-GGUF`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-8-bit-GGUF) |
| Q6_K | GGUF | ~6.56 | ~22 GB | Yes — via mmproj | llama.cpp | [`…-6-bit-GGUF`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-6-bit-GGUF) |
| **Q4_K_M** **(this repo)** | GGUF | ~4.92 | ~16 GB | Yes — via mmproj | llama.cpp | — *(you are here)* |
| TQ3_4S | GGUF | 4.00 (~3.5 eff) | ~14 GB | Yes — via mmproj | [llama.cpp-tq3](https://github.com/turbo-tan/llama.cpp-tq3) | [`…-TQ3_4s-GGUF`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-TQ3_4s-GGUF) |
| TQ3_1S | GGUF | 4.00 (~3.5 eff) | ~14 GB | Yes — via mmproj | [llama.cpp-tq3](https://github.com/turbo-tan/llama.cpp-tq3) | [`…-TQ3_1s-GGUF`](https://huggingface.co/lemuralabs/Qwen3.6-27B-V2-abliterated-uncensored-TQ3_1s-GGUF) |

> All variants share the same abliterated base weights — pick by your runtime (Apple Silicon → MLX; CUDA/CPU/cross-platform → GGUF) and your RAM budget.

---

## Lineage

```
Qwen/Qwen3.6-27B (Qwen Team — base multimodal pretrain)
 │
 ▼
Jackrong/Qwopus3.6-27B-v2 (Jackrong — Claude-Opus reasoning distill)
 │
 ▼
ablation abliteration (TPE-50) (Lemura Labs)
 ├── 25 random startup trials
 ├── 2 community priors (coder3101, wangzhang)
 └── 23 TPE smart-sampling trials → best at trial 45
 │
 ▼
HF safetensors → F16 GGUF via llama.cpp-tq3 (Lemura Labs)
 │
 ▼
this repo — Qwen3.6-27B-V2-abliterated-uncensored-Q4_K_M GGUF + paired mmproj.gguf
```

Direct upstream links:
* Foundation: [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)
* Claude-Opus distill: [Jackrong/Qwopus3.6-27B-v2](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2)
* Abliteration tool: the ablation toolkit by Lemura Labs
* Quantization tool: [turbo-tan/llama.cpp-tq3](https://github.com/turbo-tan/llama.cpp-tq3) (a fork of [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp))

---

## Abliteration Results

| Stage | Refusals (n=100) ↓ | KL divergence ↓ |
|---|---|---|
| Vanilla Jackrong/Qwopus3.6-27B-v2 | **91 / 100** | — (reference) |
| Community prior: coder3101 (T27) | 4 / 100 | 0.0359 |
| Community prior: wangzhang (T28) | 30 / 100 | 0.0259 |
| **TPE best (T45) — shipped here** | **4 / 100** | **0.0176** |
| TPE second-best (T37) | 5 / 100 | 0.0210 |

→ **96% reduction in refusals** with capability preserved (KL ≈ 0.018, well below the 0.3 healing threshold). No SFT / LoRA healing was required.

---

## Method (TPE-50 with community priors → llama.cpp GGUF)

### Step 1. Abliteration (the ablation toolkit TPE-50, BF16 source)

1. 25 random startup trials + 2 community priors enqueued (coder3101 dir=37.97, wangzhang dir=34.66) + 23 TPE smart-sampling trials.
2. Best Pareto trial: **T45** (`direction_index=41.42`) — 4/100 refusals at KL=0.0176.
3. Auto-saved via the ablation toolkit's LoRA-adapter merge path with vision tower fully intact.

Total the ablation toolkit wall-clock: ~13 h on M4 Max 128 GB.

### Step 2. HF safetensors → F16 GGUF

```bash
python convert_hf_to_gguf.py \
 /path/to/Qwen 3.6 27B-v2-abliterated \
 --outfile Qwen 3.6 27B-v2-abliterated-F16.gguf \
 --outtype f16
```

The turbo-tan fork's converter registers `Qwen3_5ForConditionalGeneration` natively and emits proper SSM tensors (`ssm_a`, `ssm_conv1d`, `ssm_alpha`, `ssm_beta`, `ssm_out`) alongside the gated-attention layers.

### Step 3. Vision tower → mmproj.gguf

```bash
python convert_hf_to_gguf.py \
 /path/to/Qwen 3.6 27B-v2-abliterated \
 --outfile mmproj-Qwen 3.6 27B-v2-abliterated-F16.gguf \
 --outtype f16 \
 --mmproj
```

This emits a separate 928 MB GGUF containing the 27-block Qwen3-VL ViT (334 vision tensors at F16/F32) plus the multimodal projector.

### Step 4. Quantization

```bash
./build/bin/llama-quantize \
 Qwen 3.6 27B-v2-abliterated-F16.gguf \
 Qwen3.6-27B-V2-abliterated-uncensored-Q4_K_M.gguf \
 Q4_K_M
```

---

## Use it

### llama-server (OpenAI-compatible HTTP, multimodal)

```bash
./build/bin/llama-server \
 -m Qwen3.6-27B-V2-abliterated-uncensored-Q4_K_M.gguf \
 --mmproj mmproj-Qwen 3.6 27B-v2-abliterated-F16.gguf \
 --host 127.0.0.1 --port 8080 \
 -ngl 99 -c 8192 -fa on --jinja
```

Then point any OpenAI-compatible client at `http://127.0.0.1:8080/v1`.

### llama-mtmd-cli (one-shot multimodal generation)

```bash
./build/bin/llama-mtmd-cli \
 -m Qwen3.6-27B-V2-abliterated-uncensored-Q4_K_M.gguf \
 --mmproj mmproj-Qwen 3.6 27B-v2-abliterated-F16.gguf \
 --image photo.jpg \
 -p "Describe this image briefly."
```

### llama-cli (text-only)

```bash
./build/bin/llama-cli \
 -m Qwen3.6-27B-V2-abliterated-uncensored-Q4_K_M.gguf \
 -ngl 99 \
 -c 8192 \
 --jinja \
 -p "Explain the difference between SSM and softmax attention in three sentences."
```

### Ollama / LM Studio / Jan

Drop the two GGUF files into the runtime's models directory; standard multimodal flow.

---

## Quantization details

* **Source weights**: BF16 abliterated checkpoint (12 shards, ~50 GB) — the ablation toolkit T45 merged into `Jackrong/Qwopus3.6-27B-v2`.
* **Intermediate**: F16 GGUF (53.8 GB, 851 tensors) produced by `convert_hf_to_gguf.py` from `turbo-tan/llama.cpp-tq3`.
* **Final quantization**: see Step 4 above.
* **Vision projector**: F16, 928 MB, shipped as `mmproj-Qwen 3.6 27B-v2-abliterated-F16.gguf` in this repo. Mandatory for image input; standard llama.cpp `--mmproj` flag.

### Architecture notes

Qwen 3.6 27B uses a **hybrid attention stack** — 3 GatedDeltaNet (linear attention / SSM) layers followed by 1 full-softmax-attention layer, repeated 16× for 64 total layers; hidden 5120, vocab 248320, context 262144. The hybrid arch is supported in the `turbo-tan/llama.cpp-tq3` fork (the upstream `Qwen3_5ForConditionalGeneration` registration). The SSM kernels run via llama.cpp's `ssm_*` tensor types.

---

## Behavior caveats

* **Uncensored.** Refusal directions were surgically removed; this model will answer prompts the parent would refuse. Use responsibly and within applicable law. The release is provided for safety research, red-teaming, and creative/educational use cases.
* **Multimodal preserved.** Pair the LM GGUF with `mmproj.gguf` (in this repo) to get full vision input. Without mmproj, the model still loads as text-only.
* **Identity preserved.** The model still self-identifies as Qwen (developed by Alibaba's Tongyi Lab) — abliteration does not rewrite factual self-knowledge.
* **Heavy chain-of-thought.** Qwen 3.6 inherits Claude-Opus's verbose reasoning style. For terse answers, use a system prompt like `"Be brief and direct. Skip your reasoning."`.

---

## Credits

**Quantization & release** — Lemura Labs
**Claude-Opus reasoning distill** — [Jackrong](https://huggingface.co/Jackrong) (`Jackrong/Qwopus3.6-27B-v2`)
**Foundation model** — [Qwen Team @ Alibaba Tongyi Lab](https://huggingface.co/Qwen) (`Qwen/Qwen3.6-27B`)
**Abliteration toolkit** — the ablation toolkit by Lemura Labs
**Community priors** — [coder3101/Qwen3.5-27B-zerofuse](https://huggingface.co/coder3101/Qwen3.5-27B-zerofuse) · [wangzhang/Qwen3.6-27B-abliterated](https://huggingface.co/wangzhang/Qwen3.6-27B-abliterated)
**Runtime / converter** — [turbo-tan/llama.cpp-tq3](https://github.com/turbo-tan/llama.cpp-tq3) · [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

---

## License

Apache-2.0, inherited from the foundation (Qwen3.6-27B) and the distill (Qwen 3.6 27B-v2) upstream.

---

Need a hosted endpoint, custom quant, or larger-scale inference? Lemura Labs — multi-provider LLM routing for the Indian developer ecosystem.
