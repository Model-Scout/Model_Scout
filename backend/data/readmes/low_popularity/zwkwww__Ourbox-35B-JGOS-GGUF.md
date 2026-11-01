---
license: apache-2.0
base_model: FINAL-Bench/Ourbox-35B-JGOS
tags:
  - gguf
  - llama.cpp
  - moe
  - qwen3.5-moe
  - a3b
  - vidraft
  - edge-inference
language:
  - en
  - ko
pipeline_tag: text-generation
quantized_by: VIDRAFT
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Ourbox-35B-JGOS — GGUF (consumer / edge)

GGUF quantizations of **Ourbox-35B-JGOS** — a **34.7B-total / ~3B-active (A3B)** sparse Mixture-of-Experts reasoning model (Qwen3.5-MoE / Qwen3-Next family: Gated-DeltaNet linear attention interleaved with full attention, 256 experts top-8).

These files are built to run a **35B-class reasoner on ordinary consumer hardware** — including an 8 GB gaming laptop.

## Highlight — measured on a gaming laptop

> **20.01 tok/s** decode for a 34.7B model on an **RTX 5060 Laptop GPU (8 GB VRAM)** + an AVX2-only laptop CPU.
> Coherent chain-of-thought output. Measured with `llama-bench` (tg64, stable ± 0.24).

The whole point of an A3B model is that decode cost scales with **active** parameters (~3B), not total (34.7B). So the experts sit in system RAM, only attention/router/shared layers occupy the GPU, and per token the machine moves ~1.45 GB instead of a dense 34B's ~16.7 GB — about **11× less memory traffic**.

### Same weights, both extremes (measured)

The identical model spans the entire hardware spectrum:

| Tier | Hardware | Throughput | Serving |
|---|---|---|---|
| **Datacenter ceiling** | single **B200** | **18,057 tok/s** aggregate | VIDRAFT optimized serving (VKAE) |
| **Consumer floor** | **8 GB laptop** (RTX 5060) | **20.01 tok/s** single-stream | open llama.cpp, Q3_K_M (VKUE) |

Both numbers are measured. One set of weights, from a datacenter B200 down to a gaming laptop.

## Files

| File | Quant | Size | Notes |
|---|---|---|---|
| `ourbox35b-Q3_K_M.gguf` | Q3_K_M (~3.9 bpw) | 16.8 GB | recommended for 8–12 GB VRAM + 24–32 GB RAM |
| `ourbox35b-Q4_K_M.gguf` | Q4_K_M (~4.5 bpw) | 21.2 GB | higher quality; needs a bit more RAM headroom |

## How to run (llama.cpp)

Requires a **recent llama.cpp build** with Qwen3.5-MoE / `qwen35moe` support (Feb 2026+; a current release is recommended). On Blackwell GPUs use the CUDA-13.x build.

The optimal consumer configuration keeps **all experts on CPU** and puts attention/router/shared layers on the GPU:

```bash
# 8 GB VRAM laptop — experts on CPU, rest on GPU
llama-bench -m ourbox35b-Q3_K_M.gguf -ngl 99 --n-cpu-moe 99 -n 128 -p 512

# interactive
llama-cli   -m ourbox35b-Q3_K_M.gguf -ngl 99 --n-cpu-moe 99 -c 8192 -p "..."
```

Tip: `--n-cpu-moe 99` (all experts on CPU) was measured to be the **optimum** on an 8 GB card — partially offloading experts to the GPU was *slower* (per-layer GPU↔CPU transfer overhead outweighs the GPU compute gain).

## Objective performance context

How this A3B result compares to running a **dense 32–35B** (same ~16 GB footprint) — decode is memory-bandwidth bound, so a dense model that reads all its params per token collapses on an 8 GB card, while this A3B stays usable.

**Head-to-head A/B, measured by us on the identical laptop** (same 8 GB GPU, same engine, same Q3_K_M class, near-identical footprint):

| Model | Active params | Footprint | Decode (same laptop) | Basis |
|---|---|---|---|---|
| **Ourbox-35B (A3B), this repo** | **~3 B** | 15.6 GiB | **20.01 tok/s** | **measured** |
| Qwen2.5-32B (dense) | 32.8 B | 14.84 GiB | **5.36 tok/s** | **measured (our A/B)** |

→ **3.7× faster from sparsity alone**, identical hardware. The only variable is active parameters (3 B vs 32.8 B).

External reference points (for context — not our hardware):

| Setup | Hardware | 35B-class decode | Basis |
|---|---|---|---|
| Dense 32B, best-case 8 GB | RTX 4060 8 GB, short ctx, minimal offload | 10.8 tok/s | published |
| Dense 30B+, forced 8 GB offload | 8 GB consumer GPU | 1–3 tok/s ("impractical") | published guides |
| Dense 32B, fully in VRAM | RTX 3090 / 4090 24 GB desktop (~$700–2,100) | 30–40 tok/s | published |

**Takeaways (honest):**
- On the **identical laptop**, we measured a dense 32B (Qwen2.5-32B, ~same footprint) at **5.36 tok/s** vs this A3B at **20.01** — a **3.7× speedup** attributable purely to A3B sparsity, and **~2× even the best-documented dense-32B result on any 8 GB machine** (10.8).
- This lifts a 35B-class model from the field's "impractical on 8 GB" band (1–3 tok/s) to a genuinely usable interactive speed.
- To *exceed* 20 tok/s on a **dense** 35B you normally need a **24 GB desktop GPU** ($700–2,100). This runs on an 8 GB laptop.
- We do **not** claim to beat a 24 GB card streaming a model fully in VRAM (those reach 30–40 tok/s dense, and 87–196 tok/s for an A3B held entirely in VRAM). This is explicitly the **8 GB-tier** result.
- Numbers labeled *estimate* are reasoned from public offload-cliff benchmarks, not single measurements. `tg64` is pure token-generation; real chat with long context is lower for every model.

## Live demo

Try the identical weights on GPU vs a GPU-less CPU box, live:

- **GPU vs CPU (one box):** https://huggingface.co/spaces/FINAL-Bench/Ourbox-35B-VKUE-Demo
- **CPU-only:** https://huggingface.co/spaces/FINAL-Bench/Ourbox-35B-VKUE-CPU
- **FREE CPU (HuggingFace free public CPU tier, ~6-7 tok/s):** https://huggingface.co/spaces/FINAL-Bench/Ourbox-35B-VKUE-FreeCPU
- **VKUE efficiency leaderboard:** https://huggingface.co/spaces/FINAL-Bench/VKUE

## Notes

- Text-only. An auxiliary prediction head that the base model carries is omitted in these GGUF files; it is not needed for standard decoding.
- Part of VIDRAFT's efficiency-serving line — the same weights run from a single datacenter GPU down to a consumer laptop.

## Learn more
- Running large models on-device without a GPU: [Can you run a large LLM without a GPU?](https://vidraft.net/insights/on-device-llm-without-gpu.html)
- What model quantization is: [What is model quantization?](https://vidraft.net/insights/what-is-quantization-llm.html)
