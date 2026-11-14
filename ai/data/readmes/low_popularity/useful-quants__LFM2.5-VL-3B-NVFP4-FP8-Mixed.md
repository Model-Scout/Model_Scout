---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: image-text-to-text
base_model: LiquidAI/LFM2.5-VL-3B
tags:
- liquid
- lfm2.5
- multimodal
- nvfp4
- fp8
- vllm
- useful-quants
- edge
---

# LFM2.5-VL-3B (NVFP4 / FP8 Mixed Precision Quantization)

This repository provides the **latency-optimized mixed-precision quantized release** of [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) (pinned upstream commit `5a414ead75d45db003906d06fb62bd5b6846cec0`), engineered for NVIDIA GeForce RTX 50-series (Blackwell SM120) serving. It holds the **best single-image VQA/OCR response latency** of the NVFP4 releases.

> [!TIP]
> **Which variant?** For general serving, the **default recommendation** is [useful-quants/LFM2.5-VL-3B-NVFP4-FP8-MinVRAM](https://huggingface.co/useful-quants/LFM2.5-VL-3B-NVFP4-FP8-MinVRAM): it leads 5/6 offline workloads (2.21× BF16 decode, 2.55× prefill-heavy, 2.27× C4 aggregate) with a smaller footprint. Choose **this repo (Mixed)** for latency-sensitive single-image VQA/OCR (126.71 vs 117.96 tok/s VQA; 130.66 vs 123.45 tok/s OCR). Do NOT run either variant with `--enforce-eager` (debug only — it halves throughput; see postmortem in Section 3).

### Key Highlights
* **~2× BF16 Offline Throughput**: On SM120 (RTX 50-series) with CUDA graph execution, delivers **2.0× the BF16 baseline's decode/balanced/C4 throughput** and ≥1.99× on every offline workload (streamed E2E image latency improves 1.6–1.7×) while using half the weight memory (decode 148 vs 74 tok/s; C4 aggregate 511 vs 253 tok/s). Requires the provided serving container defaults — **do not run with `--enforce-eager`** (debug only; see postmortem in Section 3).
* **Best Single-Image VQA/OCR Latency**: Leads the NVFP4 family on single-image response latency (VQA 126.71 tok/s, OCR 130.66 tok/s; E2E 0.88–0.95 s streamed).
* **Optimal Hybrid Allocation**: Quantizes decoder feed-forward MLPs to **NVFP4 (W4A4 Block-Scaled E2M1)** and attention/vision MLPs to **FP8 (W8A8 Static E4M3)**, while retaining Short-Conv layers, multimodal projector, and embeddings in pure **BF16**.
* **51.2% Payload Reduction**: Shrinks the raw tensor checkpoint from **5.82 GiB to 2.84 GiB** (2.0505× compression ratio).
* **Significant KV-Cache Headroom**: Frees **2.87 GiB of GPU VRAM** on 16GB GPUs, granting +49.4% additional KV cache capacity for extended multi-turn conversations and high-concurrency serving.
* **Deterministic Multimodal Parity**: Retains exact deterministic accuracy parity on standard VQA, invoice/document OCR, and high-resolution multi-tile visual reasoning benchmarks.
* **Validated Containerized Serving**: Ships with a reproducible Docker container based on `vLLM 0.26.0` and `FlashInfer 0.6.14`, with baked JIT caches and a startup warm-up that absorbs per-shape Triton compilation before the server accepts client traffic.

---

## 1. Quantization Layout & Precision Policy

LFM2.5-VL-3B utilizes a hybrid linear-attention decoder architecture containing **30 decoder layers**:
* **8 Full-Attention Layers** (`layers.2, 5, 9, 13, 17, 21, 24, 27`)
* **22 Short-Convolution Layers** (`layers.0, 1, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 23, 25, 26, 28, 29`)

| Architecture Submodule | Precision | Format / Layout |
| :--- | :--- | :--- |
| **Decoder Feed-Forward MLPs (30 layers)** | **NVFP4** | W4A4 E2M1 Block-Scaled (16-element blocks) |
| **Decoder Attention Linears (8 layers)** | **FP8** | W8A8 E4M3 Static Tensor-Scaled |
| **Decoder Short-Conv Projections (22 layers)** | **BF16** | Pure Bfloat16 (Retains operator stability) |
| **Decoder 1D Depthwise Conv** | **BF16** | Pure Bfloat16 |
| **Vision Tower MLPs (SigLIP2, 27 layers)** | **FP8** | W8A8 E4M3 Static Tensor-Scaled |
| **Vision Attention & Patch Embeddings** | **BF16** | Pure Bfloat16 |
| **Multimodal Projector** | **BF16** | Pure Bfloat16 |
| **Embeddings & LM Head** | **BF16** | Pure Bfloat16 |

---

## 2. Checkpoint & Storage Accounting

Direct storage manifest audited on host storage:

| Metric | Measurement |
| :--- | :--- |
| **Raw Tensor Payload** | **3,046,489,592 bytes (2.83726 GiB)** |
| **Actual `.safetensors` File Size** | **3,046,623,896 bytes (2.83739 GiB)** |
| **Total Checkpoint Directory Size** | **3,064,602,817 bytes (2.85413 GiB)** |
| **Compression Ratio vs BF16 Q0** | **2.0505× (51.23% payload reduction)** |

---

## 3. SM120 Hardware Performance Benchmark (CUDA Graph Execution)

Evaluated on **NVIDIA GeForce RTX 5060 Ti (16GB GDDR7, SM120)** using validated `vLLM 0.26.0` with **CUDA graph execution enabled** (production serving mode; medians of 5 repetitions after warm-up, `results/gate7c_sm120_results.json`):

| Metric / Workload | BF16 Reference (Q0) | Mixed Release (This Repo) | MinVRAM Variant (Q2b) |
| :--- | :---: | :---: | :---: |
| **Raw Model Weights VRAM** | 5.82 GiB | **2.95 GiB (-2.87 GiB)** | 2.60 GiB (-3.22 GiB) |
| **Available KV Cache (0.75 util)** | 5.81 GiB | **8.68 GiB (+49.4%)** | 9.03 GiB (+55.4%) |
| **Theoretical Max KV-Cache Concurrency** | 84.8× (4096-tok reqs) | **126.7× (4096-tok reqs)** | 131.8× (4096-tok reqs) |
| **Decode-Heavy (128 in / 256 out)** | 74.06 tok/s | **148.27 tok/s (2.00× BF16)** | 163.34 tok/s (2.21×) |
| **Balanced (1024 in / 128 out)** | 69.29 tok/s | **138.01 tok/s (1.99× BF16)** | 152.91 tok/s (2.21×) |
| **Prefill-Heavy (3840 in / 32 out)** | 36.07 tok/s | **72.68 tok/s (2.02× BF16)** | 92.05 tok/s (2.55×) |
| **Single Image VQA (576 vision tokens)** | 63.81 tok/s | **126.71 tok/s (1.99× BF16)** | 117.96 tok/s |
| **Invoice OCR (1024 vision tokens)** | 63.66 tok/s | **130.66 tok/s (2.05× BF16)** | 123.45 tok/s |
| **High-Res Multi-Tile (5120 vision tokens)** | 42.44 tok/s | **94.15 tok/s (2.22× BF16)** | 100.67 tok/s |
| **Concurrency-4 Aggregate Throughput** | 252.92 tok/s | **511.16 tok/s (2.02× BF16)** | 574.13 tok/s (2.27×) |
| **Server E2E Image Analysis (108-153 tok, streamed)** | 1.49-1.51 s (72 tok/s) | **0.88-0.95 s (TTFT 27-92 ms)** | 0.96-1.25 s (TTFT 44-344 ms) |
| **Deterministic Multimodal Parity** | 100% Exact Parity | **100% Exact Parity** | 100% Exact Parity |

Kernel-dispatch profiling (Gate 7C evidence, `results/profiling/ANALYSIS.md`) confirms the decoder MLPs execute on the native CUTLASS FP4 `GemmUniversal` path via `FlashInferCutlassNvFp4LinearKernel` with CUDA graph replay: GPU time per decode token is **7.19 ms vs 13.87 ms for BF16 (1.93× faster)**, and graph execution delivers that advantage end-to-end.

> [!IMPORTANT]
> **Serving configuration requirement: do NOT use `--enforce-eager`.**
>
> **Postmortem (2026-08):** the originally published benchmark table was produced under `--enforce-eager` and showed this checkpoint at ~0.5× BF16 throughput (29.20 vs 60.48 tok/s decode). That result was a **serving-configuration defect, not a quantization defect**. The NVFP4 decode path issues ~800 small kernel launches per token (FP4 GEMMs, per-call activation quantization, scale/dequant ops); under eager execution the step becomes CPU-launch-bound (GPU utilization ~21%) and wall-clock throughput halves even though GPU kernel time is 1.93× *faster* than BF16. BF16 (~578 launches/step, 84% GPU-busy) is far less sensitive to eager mode, so the regression appeared to be "caused" by quantization. With CUDA graph execution enabled — the production default in the provided container since 2026-08-18 — this checkpoint is **≥1.99× BF16 on every offline workload** (decode 2.00×, VQA 1.99×, multi-tile 2.22×, C4 2.02×) and **1.6–1.7× BF16 on streamed end-to-end image latency** (0.88–0.95 s vs 1.50 s).
>
> `ENFORCE_EAGER=1` remains available in the entrypoint **for debugging only** and prints an explicit warning: it catastrophically degrades NVFP4 serving performance on this architecture.

---

## 4. Serving Environment & Integration Patches

### Canonical Recommendation
**Use the provided Docker runtime unless you independently apply and validate the compatibility patch suite in your own vLLM build.**

The supplied Docker environment pins the validated serving stack and applies four targeted compatibility patches required for this hybrid VLM representation:

1. **`patches/0001-flashinfer-backend-binding.patch`**
   - **Target File**: `vllm/utils/flashinfer.py`
   - **Scope**: Keyword argument compatibility workaround passing `backend="auto"` explicitly in `flashinfer_autotune_and_run` to prevent custom-op parameter collisions on PyTorch 2.11 / SM120.
2. **`patches/0002-modelopt-shortconv-resolution.patch`**
   - **Target File**: `vllm/model_executor/layers/quantization/modelopt.py`
   - **Scope**: Resolves `.conv.` $\leftrightarrow$ `.short_conv.` module routing, handles leaf parameter tensor transposition during safetensors loading, and safeguards missing NVFP4 scale default tensors.
3. **`patches/0003-scalar-scale-loader.patch`**
   - **Target Files**:
     * `vllm/model_executor/parameter.py`
     * `vllm/model_executor/layers/linear.py`
   - **Scope**: Broadcasts 0D scalar scale tensors to multidimensional parameter containers and safeguards weight parameter container loading.
4. **`patches/0004-shortconv-rank-alignment.patch`**
   - **Target Files**:
     * `vllm/model_executor/layers/mamba/short_conv.py`
     * `vllm/model_executor/models/lfm2.py`
     * `vllm/model_executor/models/lfm2_siglip2.py`
     * `vllm/model_executor/models/lfm2_vl.py`
   - **Scope**: Passes `quant_config` through `ShortConv` instantiation, aligns 1D depthwise convolution tensor shapes, and adds `WeightsMapper` prefix translations (`vision_model.`) for SigLIP2 vision encoder weights.

> **Zero Modification Statement**: These compatibility adaptations do not recalibrate the checkpoint, alter learned tensor values, change model topology, or modify the mathematical inference equations. All 86 FP8 scale tensors match the frozen PTQ calibration bit-for-bit (0 mismatches, max absolute difference = 0.0).

### Version Support Policy
* **Validated Runtime**: `vLLM 0.26.0` + `PyTorch 2.11.0+cu130` + `FlashInfer 0.6.14` (as packaged in the included `Dockerfile`).
* **Other Versions (e.g. vLLM 0.27.x)**: **UNVALIDATED**. Newer versions have not been qualified against this specific checkpoint representation and SM120 configuration.

---

## 5. Quick Start with Docker

### Step 1: Clone Repository & Build Serving Image
```bash
git clone https://huggingface.co/useful-quants/LFM2.5-VL-3B-NVFP4-FP8-Mixed
cd LFM2.5-VL-3B-NVFP4-FP8-Mixed
docker build -t lfm25vl-serving:v0.26.1 .
```

### Step 2: Run Serving Container
```bash
docker run --rm -it \
  --gpus all \
  --ipc=host \
  -p 8000:8000 \
  -v "$(pwd):/model" \
  -v lfm-jit-cache:/root/.cache \
  -e MODEL_PATH=/model \
  lfm25vl-serving:v0.26.1

# CUDA graphs are ON by default (required for rated throughput).
# The container performs a startup warm-up (text + image) after /health passes,
# absorbing per-shape Triton JIT before client traffic. WARNING: the FIRST boot
# of a given model/spec compiles FlashInfer CUTLASS kernels into /root/.cache -
# measured ~75 minutes on the validation host (12-core CPU) - and the server
# does not become healthy until it finishes. Mount a persistent volume (as
# above) so this one-time cost is paid once per model/spec, not per container.
# ENFORCE_EAGER=1 disables graphs (debug only, ~2-5x slower).
```

### Step 3: Run Deterministic Smoke Suite
```bash
# Text Generation Smoke Test
python examples/smoke_text.py --url http://localhost:8000/v1/chat/completions

# Multimodal VQA Smoke Test
python examples/smoke_image.py --url http://localhost:8000/v1/chat/completions
```

---

## 6. Notice of Modifications & License Compliance

* **Base Model**: [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) (pinned upstream revision `5a414ead75d45db003906d06fb62bd5b6846cec0`) by Liquid AI, Inc.
* **License**: [LFM Open License v1.0](LICENSE) (Liquid AI, Inc.).
* **Modifications Notice**: See [MODIFICATIONS.md](MODIFICATIONS.md) for an itemized record of post-training quantization, runtime patches, and derivative work notices in accordance with Section 4 of the LFM Open License v1.0.
* **Attribution**: Quantization, patch derivation, containerization, and release packaging created by `useful-quants`. Liquid AI, Inc. did not produce, sponsor, or endorse this derivative work.
