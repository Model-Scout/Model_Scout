---
license: apache-2.0
language:
- en
- ko
base_model:
- FINAL-Bench/Darwin-9B-Opus
pipeline_tag: text-generation
tags:
- darwin
- mfp4
- mixed-precision
- nvfp4
- quantization
- blackwell
- reasoning
library_name: transformers
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-9B-MFP4

**Mixed-Precision FP4** quantization of [Darwin-9B-Opus](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus), built on NVIDIA Blackwell-native NVFP4.

The first member of the **Darwin Mixed-Precision** family — quantization that respects what each layer actually does, instead of compressing everything uniformly.

---

## 🧬 Model Lineage

```
Qwen3.5 (Alibaba Qwen team — hybrid attention architecture)
    │
    ▼
Darwin-9B-Opus  (FINAL-Bench)
    │   evolutionary merge across the Qwen3.5 family
    │   Architecture: Qwen3_5ForConditionalGeneration
    │
    ▼
Darwin-9B-MFP4  ← this model
    Mixed-Precision FP4 via NVIDIA ModelOpt
    Targets MLP layers only; preserves attention pathways
```

---

## 💡 What is MFP4?

**MFP4 (Mixed FP4)** is a precision-allocation strategy, not a single bit-width. Different functional regions of the network get different precisions, chosen to match their role:

| Region | Precision | Why |
|---|---|---|
| **MLP / FFN layers** | NVFP4 (4-bit) | Per-token compute — tolerant to controlled noise |
| **Self-attention (Q/K/V/O)** | BF16 | Long-range coordination — sensitive to rounding |
| **Linear-attention blocks** | BF16 | Stateful recurrent paths — must remain stable |
| **LM head / Embeddings** | BF16 | Direct I/O surface — no degradation acceptable |
| **LayerNorms / scales** | BF16 | Tiny, but critical scale factors |

The bulk of parameters (the MLPs) move to FP4, while the small but architecturally critical attention/coordination paths stay full-precision.

---

## 🎯 Why mixed precision matters

Uniform quantization treats every weight the same. In practice, transformer layers have very different roles:

- **MLPs** are local, parallel, and compute-heavy — they account for the majority of the parameter count and tolerate compression noise gracefully because each forward pass averages over many independent activations.
- **Attention** is the model's coordination substrate. Even small perturbations there propagate across long contexts, fragmenting reasoning chains and causing decoding pathologies (looping, repetition, premature termination).

A **uniform 4-bit** quantization compresses all of these the same way and pays an attention-quality cost it didn't need to pay. **MFP4** isolates the cost to the layers that can absorb it.

This aligns with the Darwin philosophy: *let the architecture's structure dictate the optimization*, rather than imposing a single recipe everywhere.

---

## 🚀 Why NVFP4 (and not just FP4)?

NVFP4 is NVIDIA's microblock 4-bit floating-point format with FP8-scaled groups of 16 elements.

- **Native hardware acceleration on Blackwell** (B200, RTX 5090): NVFP4 GEMMs run on dedicated tensor cores at 2nd-generation FP4 throughput, with no software emulation in the hot path.
- **Higher numerical accuracy than INT4** at the same bit-width, thanks to the floating-point representation and per-block FP8 scales.
- **First-class support** in vLLM (`--quantization modelopt_fp4`), TensorRT-LLM, and the broader NVIDIA inference stack.

Combined with MFP4's selective application, the result is FP4-class memory savings on the bulk of the model with BF16-quality attention behavior — and on Blackwell, FP4-class throughput on the dominant cost center (MLP GEMMs).

---

## 📦 Specs

| | |
|---|---|
| Base model | [FINAL-Bench/Darwin-9B-Opus](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus) |
| Quantization scheme | MFP4 (MLP → NVFP4, attention → BF16) |
| Disk size | ≈ 11 GB *(base BF16: 19 GB)* |
| Architecture | Qwen3.5 hybrid (full + linear attention) |
| Quantization tool | [NVIDIA ModelOpt](https://github.com/NVIDIA/TensorRT-Model-Optimizer) |
| Inference runtime | vLLM ≥ 0.19 with `modelopt_fp4` backend |

---

## ⚙️ Where MFP4 fits in the Darwin platform

The Darwin platform produces base models through evolutionary merging of open-source families. MFP4 is the **first deployment-ready quantization** in that lineage — designed so that the structural decisions made during evolution (which attention type lives where, which MLP carries which capability) are preserved when the model is compressed for serving.

In other words: Darwin's value isn't only in *how the weights got there* — it's also in *making sure those weights still work when you halve the memory footprint*. MFP4 is the bridge between research-grade BF16 checkpoints and Blackwell-grade serving infrastructure.

Future Darwin releases will share this serving stack: same NVFP4 format, same MLP-only allocation policy, same vLLM path.

---

## 🚀 Usage

### vLLM (recommended)

```bash
pip install "vllm>=0.19" nvidia-modelopt

vllm serve FINAL-Bench/Darwin-9B-MFP4 \
    --quantization modelopt_fp4 \
    --trust-remote-code \
    --port 8000 \
    --enforce-eager \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.85
```

### OpenAI-compatible client

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="FINAL-Bench/Darwin-9B-MFP4",
    messages=[{"role": "user", "content": "..."}],
    max_tokens=4096,
    temperature=0.0,
)
```

---

## 🖥️ Hardware

| GPU family | Status |
|---|---|
| Blackwell (B200, RTX 5090) | ✅ Native NVFP4 tensor cores — best path |
| Hopper (H100/H200) | ✅ FLASHINFER_CUTLASS NVFP4 path |
| Ada (L40, RTX 6000 Ada) | ⚠️ Partial — depends on driver/runtime |
| Older Ampere/Volta | ❌ NVFP4 unavailable |

**Minimum VRAM for inference**: ~13 GB. Comfortable on a single 24 GB consumer card.

---

## 📍 When to use this model

**Good fit:**
- Latency- and memory-constrained serving on Blackwell or Hopper hardware
- Reasoning workloads where attention quality matters (multi-step deduction, long contexts)
- Workloads currently bottlenecked by 9B-class BF16 memory footprints

**Consider the BF16 base instead if:**
- You need bit-exact reproducibility against research baselines
- Your hardware lacks NVFP4 support
- You are doing further training / fine-tuning (quantize after, not before)

---

## 🙏 Credits

- **Base model**: [FINAL-Bench/Darwin-9B-Opus](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus)
- **Architecture lineage**: Qwen3.5 (Alibaba Qwen team)
- **Quantization framework**: [NVIDIA ModelOpt](https://github.com/NVIDIA/TensorRT-Model-Optimizer)
- **Inference runtime**: [vLLM](https://github.com/vllm-project/vllm)
- **Hardware target**: NVIDIA Blackwell NVFP4

---

This model is introduced in [Darwin Family](https://huggingface.co/papers/2605.14386).

## 📜 License

Apache 2.0 (inherited from base model).
