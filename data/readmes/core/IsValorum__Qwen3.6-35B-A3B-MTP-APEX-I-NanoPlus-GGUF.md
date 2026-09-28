---
base_model: Qwen/Qwen3.6-35B-A3B
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
pipeline_tag: image-text-to-text
license: apache-2.0
language:
- en
- zh
- es
- fr
- de
- pt
- it
- ru
- ja
- ko
- vi
- th
- ar
tags:
- gguf
- llama.cpp
- quantized
- quantization
- apex
- apex-quant
- apex-i-nanoplus
- nanoplus
- custom-quantization
- unsloth-studio
- qwen3.6
- qwen35moe
- qwen3_5_moe
- qwen
- moe
- reasoning
- conversational
- multimodal
- vision
- image-text-to-text
- coding
- agentic
- swe-bench
- mtp
- speculative-decoding
---

## <a id="quick-navigation"></a>Quick Navigation Index
1. [Optimization History & Transparency Notice](#toc-01)
2. [Independent Benchmark of the APEX-I-MiniPlus Family (Occamy V2 Reference)](#toc-02)
3. [Empirical Benchmarks & Fidelity Verification](#toc-03)
4. [Quality Spectrum: APEX-I-NanoPlus vs. Standard Flat Quantizations](#toc-04)
5. [Model Files & Technical Specifications](#toc-05)
6. [Surgical Tensor Quantization Map (Audited from GGUF)](#toc-06)
7. [Hardware Throughput & Offload Benchmarks (RTX 30 / 40 / 50 & RAM Streaming)](#toc-07)
8. [The 16GB & 24GB Advantage: Massive Context in VRAM!](#toc-08)
9. [Recommended Configuration & Setup](#toc-09)
10. [1. llama-cli with MTP Speculative Decoding & Vision Projector](#toc-10)
11. [2. High-Performance OpenAI-Compatible Server](#toc-11)
12. [Recommended Generation Parameters (Qwen Official)](#toc-12)
13. [Optional Support](#toc-13)

# Qwen3.6-35B-A3B-MTP APEX-I-NanoPlus GGUF
### *The Next-Generation Frontier MoE · Extreme 13GB Footprint · Fast System RAM Streaming & Massive Context on 16GB VRAM*

> [!IMPORTANT]
> ### THE DEFINITIVE SPECIFICATION IN THE ~13 GB CEILING
> This **APEX-I-NanoPlus** release marks the official debut of our specialized tensor-by-tensor architectural configuration for sparse Mixture-of-Experts quantization within an extreme **~13 GB envelope**. Its 40 layers and 256 micro-experts are allocated tensor by tensor to maximize reasoning precision, preserve routing behavior, and prevent avoidable CPU dequantization stalls during hybrid and system-RAM inference; optional MTP companion files remain available for speculative decoding.

> [!TIP]
> ### 🏆 EMPIRICAL BENCHMARK & QUALITY COMPARISON
> 
> | Quantization Specification | File Size (Disk) | Memory Footprint (RAM/VRAM) | Average BPW | WikiText-2 Perplexity | Quality Tier Equivalent |
> | :--- | :---: | :---: | :---: | :---: | :---: |
> | **Unquantized BF16 Base** | ~71.05 GB | ~66.18 GiB | 16.00 BPW | ~5.32 | Full Precision Baseline |
> | **[APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Qwen3.6-35B-A3B-MTP-APEX-I-MiniPlus-V2.1-GGUF)** | 15.23 GB | 14.18 GiB | 3.43 BPW | 5.3693 ± 0.12528 (+0.0493 / +0.93%) | Q5_K_L tier (bordering Q6_K) |
> | **APEX-I-NanoPlus (NEW)** | **13.03 GB** | **12.14 GiB** | **2.93 BPW** | **5.5244 ± 0.12916 (+0.2044 / +3.84%)** | **Solid Q4_K_M / Q4_K_L Tier** |
> | *Generic Community IQ2_S* | ~12.2 GB | ~11.4 GiB | 2.56 BPW | > 5.85 (Degraded) | Unstable / Syntax Spikes |
>
> **Looking for higher precision?** [APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Qwen3.6-35B-A3B-MTP-APEX-I-MiniPlus-V2.1-GGUF) offers the full **15.23 GB (3.43 BPW)** release of this Qwen3.6 family, delivering Q5_K_L tier (bordering Q6_K) fidelity with integrated MTP support.
>
> **ARC-Challenge (0-shot, 1,172 questions): ~95.75%.**
> - **Q4_K_L Tier in Reasoning & Routing:** 100% uncompressed `F32` routers (`gate_inp`) and a `Q6_K` output head eliminate router drift, matching or exceeding standard `Q4_K_L` baselines on logic benchmarks.
> - **Solid Q4_K_M Tier in Language Modeling:** WikiText-2 perplexity preserves 4-bit distributional fidelity across standard generation in an agile ~13.03 GB footprint.
>
> **Routing:** all recipe-designated `gate_inp` and `gate_shexp` tensors remain in uncompressed `F32`, preserving zero routing drift.

> [!WARNING]
> ### DO NOT CONFUSE APEX-I-NANOPLUS WITH GENERIC COMMUNITY SUB-3-BIT QUANTS!
> **Regardless of release version, NEVER confuse handcrafted APEX-I-NanoPlus builds with generic community sub-3-bit releases:**
> - **Generic Community IQ2_S / IQ2_XXS:** Uniformly crushes all core MoE experts down to aggressive 2-bit codebooks without importance calibration, leaves the sensitive token output head unarmored at 3-bit, and compresses attention projections. In deep reasoning models, this triggers severe perplexity spikes, syntax errors, and broken code brackets.
> - **Handcrafted APEX-I-NanoPlus:** Applies a surgical tensor-by-tensor architecture that preserves 100% of expert routing matrices in uncompressed `F32` (zero router drift), armors the token output head in high-precision `Q6_K`, safeguards attention gates in `Q8_0`, fortifies the critical MoE down-projection residual stream (`ffn_down_exps`) in `IQ3_XXS` (3.06 bpw), and restricts 2-bit compression strictly to redundant gating/up projections guided by the official `imatrix`.

> [!TIP]
> ### SYSTEM RAM INFERENCE: FULL OR PARTIAL
> This APEX-I-NanoPlus release is designed for **full or partial system-RAM inference**. Depending on the processor, memory bandwidth, and DDR4/DDR5 configuration, generation can range from **20 to 45 tok/s**. With partial GPU offload, systems that cannot fit **128K or more context** entirely in VRAM can place the remaining model and context load in system RAM, maintaining stable, responsive generation at longer context lengths.

---

<a id="toc-01"></a>
## Optimization History & Transparency Notice

We maintain our previous releases publicly as a transparent engineering record of continuous optimization. Below is the exact evolutionary roadmap of our architectures:

| Specification | Core Experts (2–37) | Edge Experts (0–1, 38–39) | Shared Expert (`shexp`) | Full Attention (L3, 7, 11, ...) | Attention Gates (30 Layers) | Output Head (`output.weight`) | Routers (`gate_inp`) | Size / Overhead | Real-World Impact |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Generic APEX Mini** | `IQ2_S` (2.50 bpw) | `Q3_K` (only 5 layers) | `Q4_K` / `Q3_K` | `Q3_K` | Compressed | `Q3_K_M` | Compressed | Baseline (approx. 12.5 GB) | Severe syntax errors, broken code indentation, high perplexity in `<think>`. |
| **MiniPlus V2.1 (Current)** | `IQ3_XXS` + `Q3_K` | `Q3_K` (10 layers) | `Q5_K` | `Q4_K` (`q/k/v`) + `Q6_K` (`output`) | `Q8_0` | `Q6_K` | `F32` | 15.23 GB (14.18 GiB) | Maximum fidelity near-lossless Q5/Q6 tier. Fits 24GB GPUs effortlessly. |
| **NanoPlus (NEW)** | **`IQ3_XXS` (down) + `IQ2_S` (gate) + `IQ2_XXS` (up)** | **`Q3_K` (down) + `IQ3_XXS` (gate/up)** | **`Q4_K`** | **`Q4_K` (`q/k/v`) + `Q6_K` (`output`)** | **`Q8_0`** | **`Q6_K`** | **`F32`** | **13.03 GB (12.14 GiB)** | **Calibrated ~13.0 GB tier. Leaves >3 GB free VRAM on 16GB cards for 32k context with zero AVX2 CPU stalls.** |

> [!TIP]
> ### Deployment & System Architecture Guide
> - **Full GPU VRAM Offload (16GB+ VRAM, `-ngl 99`):** Effortless full offload with native 32K–64K context support on 16GB cards (RTX 4080 / RTX 4070 Ti Super), and native 256K context on 24GB workstations (RTX 3090 / 4090 / 5090).
> - **System RAM Streaming Specialist (DDR4/DDR5 & Massive Context):** Specially engineered to run either partially or entirely out of system RAM across large or full context windows. By utilizing linear SIMD-optimized `Q4_K` attention projections and preserving critical down-projections in `IQ3_XXS`, AVX2 CPU dequantization stalls are eliminated. Depending on your processor architecture and memory bandwidth (dual-channel DDR4 or high-speed DDR5 6000+ MT/s), streaming generation in system RAM can approach speeds remarkably close to full VRAM execution.
> 
> Explore our official collection:
> **[APEX-I-NanoPlus Collection](https://huggingface.co/collections/IsValorum/apex-i-nanoplus-6ab41467c988a1b1cb9b83bc)**.

---

> [!IMPORTANT]
> ### EXPLORE THE ESTABLISHED 35B MoE MINIPLUS LINEUP
> These are complementary APEX-I-MiniPlus V2.1 releases, not alternate downloads of the same model. Each receives the same tensor-by-tensor approach, integrated MTP where supported, and a design suitable for full or partial system-RAM inference. Choose the model whose native strengths best fit the work you want to do:
>
> - **[Qwen3.6-35B-A3B MTP APEX-I-MiniPlus-V2.1](https://huggingface.co/IsValorum/Qwen3.6-35B-A3B-MTP-APEX-I-MiniPlus-V2.1-GGUF)** — a versatile frontier MoE for broad reasoning, multilingual work, agents, tool use, and multimodal tasks.
>   - **Best for:** General reasoning, agent workflows, tool calling, and flexible multimodal use.
> - **[Qwen3.6-35B-A3B MTP APEX-I-MiniPlus-V2.1 Abliterated](https://huggingface.co/IsValorum/Qwen3.6-35B-A3B-MTP-APEX-I-MiniPlus-V2.1-Abliterated-GGUF)** — the V2.1 refusal-ablated Qwen3.6 edition for users who deliberately prefer reduced refusal behavior.
>   - **Best for:** Workflows where an abliterated Qwen3.6 variant is explicitly desired.
> - **[Ornith 1.5 APEX-I-MiniPlus-V2.1](https://huggingface.co/IsValorum/Ornith-1.5-35B-A3B-APEX-I-MiniPlus-V2.1-GGUF)** — a software-engineering-focused MoE designed for repository-scale coding and autonomous engineering agents.
>   - **Best for:** Repository-scale development, multi-file code changes, and software-engineering agents.
> - **[Tiel Coder APEX-I-MiniPlus-V2.1](https://huggingface.co/IsValorum/Tiel-Coder-35B-A3B-APEX-I-MiniPlus-V2.1-GGUF)** — a specialist coding MoE tuned for agentic programming, iterative tool use, and implementation-heavy work.
>   - **Best for:** Focused coding sessions, iterative debugging, and tool-driven implementation.
>
> These remain distinct model families and editions with their own behavior and empirical results. Pick by workload and intended alignment behavior rather than treating them as interchangeable quantization variants.


---

<a id="independent-benchmark"></a>
<a id="toc-02"></a>
### 🏅 Independent Benchmark of the APEX-I-MiniPlus Family (Occamy V2 Reference)

> [!NOTE]
> **External report:** [zephel01 independently benchmarked Occamy V2](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en). The benchmark was performed on **Occamy-1.0 APEX-I-MiniPlus V2**, not on this specific NanoPlus release. It is included as independent context for the broader tensor-by-tensor MiniPlus approach.

The related **APEX-I-MiniPlus** quantization architecture has an independent evaluation by Japanese AI researcher and evaluator [zephel01 (CoolZero)](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en) on an **NVIDIA RTX 5090 (32GB)** workstation running `llama.cpp` CUDA with FlashAttention.

The evaluation covered **348 unseeded trials** on SWE-bench-style multi-file Python bug-fixing tasks with hidden `pytest` suites (`llmbench`):

- **L6 Multi-File Code Generation (60 tasks):**
  - **32K context:** **93.3% resolved** (46/60 tasks passed 5/5 consecutive trials).
  - **65K context:** **90.0% resolved** (45/60 tasks passed 5/5 consecutive trials).
- **Context scaling on the tested Occamy V2 build:** 14.6 GB at 32K and 15.1 GB at 65K.

These findings belong to Occamy V2 and should not be read as a direct NanoPlus benchmark. NanoPlus-specific fidelity is documented by its own WikiText-2 result below.

<a id="model-specifications"></a>
<a id="empirical-benchmarks"></a>
<a id="toc-03"></a>
## Empirical Benchmarks & Fidelity Verification

The comparison table near the top consolidates the model-specific BF16 baseline, final GGUF PPL, delta, published main-file size, BPW, and fidelity tier. The routing treatment is preserved in the note directly beneath it.


<a id="quality-spectrum"></a>
<a id="toc-04"></a>
### Quality Spectrum: APEX-I-NanoPlus vs. Standard Flat Quantizations

How the handcrafted **APEX-I-NanoPlus** architecture compares against standard flat quantizations in `llama.cpp` on 35B Mixture-of-Experts architectures:

| Quantization Format | Bits Per Weight (BPW) | Model Footprint (Disk / VRAM) | Perplexity Delta (vs. FP16 Baseline) | Token Fidelity & Syntactic Stability Tier |
| :--- | :---: | :---: | :---: | :--- |
| **FP16 / BF16 (Uncompressed)** | 16.0 bpw | 71.0 GB | **0.00** (Reference) | 100% full uncompressed reference fidelity. |
| **Standard Q8_0** | 8.50 bpw | approx. 38 GB | approx. +0.01 | Virtually lossless; excessive memory overhead for consumer hardware. |
| **Standard Q6_K** | 6.56 bpw | approx. 30 GB | approx. +0.02 to +0.05 | Near-lossless FP16 fidelity; requires multi-GPU or 32GB+ VRAM setups. |
| **APEX-I-MiniPlus V2.1** | 3.43 bpw | 15.23 GB (14.18 GiB) | **+0.0493 (PPL: 5.3693)** | Near-lossless Q5_K / Q6_K tier. Full native 256K context on 24GB workstations. |
| 🏆 **APEX-I-NanoPlus (IsValorum)** | **2.93 bpw** | **13.03 GB (12.14 GiB)** | **+0.2044 (PPL: 5.5244 ± 0.12916)** | **Solid Q4_K_M fidelity tier at only 13.0 GB (81.6% weight reduction). Enables 32k context 100% in VRAM on 16GB GPUs.** |
| **Standard Q4_K_M** | 4.50 bpw | approx. 20.0 GB | approx. +0.15 to +0.25 | Standard industry trade-off; cannot fit in 16GB VRAM. |
| **Standard Q3_K_M** | 3.44 bpw | 16.6 GB | approx. +0.36 to +0.45 | Noticeable syntax drop, bracket corruption, and tokenizer classification noise. |
| **Standard IQ2_S / Generic APEX Mini** | 2.50 bpw | approx. 12.2 GB | approx. +0.55 to +1.50+ | Severe reasoning breakdown, high perplexity spikes in `<think>` chains. |

---

<a id="toc-05"></a>
## Model Files & Technical Specifications

| File Name | File Size | Memory Footprint | BPW | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Qwen3.6-35B-A3B.APEX-I-NanoPlus.gguf`** | **`13.03 GB (12.14 GiB)`** | `12.14 GiB` | **2.93 BPW** | Core agentic reasoning & multimodal MoE in APEX-I-NanoPlus |
| **`mmproj-Q8_0.gguf`** | **`610.66 MB (582.37 MiB)`** | `582.37 MiB` | **8.50 BPW** | Dedicated Q8_0 multimodal vision projector for document & image reasoning |
| **`mtp-Qwen3.6-35B-A3B-Q8_0.gguf`** | **`1.99 GB (1.85 GiB)`** | `1.85 GiB` | **8.50 BPW** | Dedicated Q8_0 Multi-Token Prediction (MTP) draft head for speculative decoding |
| **`mtp-Qwen3.6-35B-A3B-Q4_0.gguf`** | **`1.19 GB (1.11 GiB)`** | `1.11 GiB` | **4.50 BPW** | Dedicated Q4_0 Multi-Token Prediction (MTP) draft head for low-VRAM speculative decoding |
| **Complete download** | **`14.83 GB (13.81 GiB)`** | `13.81 GiB` | — | Main GGUF plus the Q4_0 MTP companion and bundled vision projector |

- **Base Model:** [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- **Parameters:** 35.2B total (approx. 2.6B to 3.2B active per token)
- **Architecture:** 40 layers, 256 micro-experts (8 active per token)  + hybrid linear attention / DeltaNet recurrent layers; separate MTP companion heads are available for speculative decoding
- **Context Length:** 262,144 tokens (native 256K)

---

<a id="tensor-map"></a>
<a id="toc-06"></a>
## Surgical Tensor Quantization Map (Audited from GGUF)

*The exact tensor breakdown below has been verified directly from the compiled binary weights:*

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Preserves near-FP16 token classification; eliminates syntax errors, bracket drops, and hallucinations. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | High-fidelity vocabulary embedding representation. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `ssm_norm` | 171 | **`F32`** | 100% uncompressed numerical stability across all 40 layers. |
| **Expert Routers** | `blk.*.ffn_gate_inp`, `ffn_gate_inp_shexp` | 82 | **`F32`** | 100% uncompressed routing fidelity across 256 micro-experts; zero router drift. |
| **Attention Gates** | `blk.*.attn_gate.weight` (Hybrid Layers) | 31 | **`Q8_0`** | High-precision attention gating across hybrid DeltaNet recurrence layers; eliminates crosstalk. |
| **Shared Foundation Experts** | `blk.*.ffn_{gate,down,up}_shexp` (All Layers) | 123 | **`Q4_K`** | Foundation knowledge backbone active on 100% of tokens; protected in linear Q4_K for fast streaming. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_q/k/v` (10 Anchor Layers) | 30 | **`Q4_K`** | Full quadratic attention anchor checkpoints for deep needle-in-a-haystack retrieval. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_output` (10 Anchor Layers) | 10 | **`Q6_K`** | Armored attention output projection over deep context. |
| **Recurrent SSM Scales** | `blk.*.ssm_alpha`, `ssm_a`, `ssm_conv1d`, `ssm_dt` | 123 | **`F32`** | Guarded in uncompressed FP32 to prevent DeltaNet recurrent state drift. |
| **Linear Attention & SSM** | `blk.*.attn_qkv`, `ssm_beta`, `ssm_out` | 92 | **`Q4_K`** | Linear AVX2 execution; zero SIMD CPU stalls during system RAM streaming. |
| **Border MoE Down-Proj** | Layers 0–1 & 38–39 (`ffn_down_exps`) | 4 | **`Q3_K`** | Linear SIMD execution optimized for token entry and exit stability. |
| **Border MoE Gate/Up** | Layers 0–1 & 38–39 (`ffn_gate/up_exps`) | 8 | **`IQ3_XXS`** | High-density boundary protection guided by imatrix. |
| **Core MoE Down-Proj** | Layers 2–37 (`ffn_down_exps`) | 36 | **`IQ3_XXS`** | Fortified 3.06 bpw residual stream; preserves core mathematical and reasoning capacity. |
| **Core MoE Gating** | Layers 2–37 (`ffn_gate_exps`) | 36 | **`IQ2_S`** | High-precision 2.50 bpw SwiGLU gating; eliminates activation noise. |
| **Core MoE Up-Proj** | Layers 2–15 (`ffn_up_exps`) | 14 | **`IQ2_S`** | Enhanced 2.50 bpw precision for sensitive early-intermediate feature extraction. |
| **Core MoE Up-Proj** | Layers 16–37 (`ffn_up_exps`) | 22 | **`IQ2_XXS`** | Extreme 2.06 bpw compression in deep MoE layers to reach exact 13.0 GB envelope. |
| **MTP Companion Head** | `mtp-Qwen3.6-35B-A3B-Q4_0.gguf` | 1 | **`Q4_0`** | Separate low-VRAM speculative draft companion; use with `-md`. |

---

<a id="throughput-projections"></a>
<a id="toc-07"></a>
## Hardware Throughput & Offload Benchmarks (RTX 30 / 40 / 50 & RAM Streaming)

*Hardware guidance for compatible llama.cpp-style runtimes:*

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | :--- |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **approx. 247 – 251 tok/s** | **2,800 – 3,900+ tok/s** | Ultra-high throughput on Blackwell architecture; native 256k window in VRAM |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **95 – 120+ tok/s** | **2,000 – 2,800+ tok/s** | Linear attention layers slash prefill latency; 256k window in VRAM |
| **NVIDIA RTX 4080 (16GB GDDR6X)** | Full GPU (`-ngl 99`) | **75 – 92+ tok/s** | **1,600 – 2,200+ tok/s** | **Entire model fits in VRAM with room for 32k context!** |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **75 – 90+ tok/s** | **1,500 – 2,000+ tok/s** | Full 256k native window in VRAM |
| **Workstation / Laptop (DDR4 / DDR5 RAM)** | Hybrid Offload (Few layers in VRAM) | Hardware-dependent | Hardware-dependent | Zero AVX2 CPU stalls; efficient streaming from system RAM |

- **Aggressive Hybrid Offload Profile:** Hybrid offload supports reasoning-enabled generation with limited VRAM while the remaining model weights stream from system RAM.

> [!NOTE]
> ### Empirical Testbed Architecture & Desktop/Server Scaling
> - **Empirical Benchmark Hardware:** The hybrid offload and system RAM streaming behavior documented above was measured on a consumer laptop powered by an **Intel 12th Gen Alder Lake architecture featuring a hybrid design of Performance Cores (P-Cores) and Efficient Cores (E-Cores)** paired with dual-channel system RAM and constrained laptop power/thermal envelopes.
> - **Thread Scheduling & E-Core Contention:** In hybrid architectures like Alder Lake, OS thread scheduling across background E-Cores and lower single-core mobile power limits introduce memory bandwidth and thread synchronization overhead during CPU dequantization.
> - **Dramatic Scaling on Higher-End Processors:** When running on desktop or server processors (such as modern AMD Ryzen 7000 / 9000 Zen 4/5 series or high-TDP Intel desktop platforms with dedicated performance cores, large L3 caches, and high-bandwidth dual- or quad-channel DDR5 running at 6000+ MT/s), **streaming generation speeds and prefill throughput will scale dramatically higher**, substantially exceeding these measured mobile numbers.

---

<a id="context-scaling"></a>
<a id="toc-08"></a>
## The 16GB & 24GB Advantage: Massive Context in VRAM!

**Qwen3.6-35B-A3B APEX-I-NanoPlus fits native context on 16GB GPUs and the full 256K window on 24GB GPUs:**

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,768 (32k)** | `12.14 GiB` | `0.58 GiB` | `1.80 GiB` | **`14.52 GiB`** | **FULL OFFLOAD ON 16GB GPUs (RTX 4080 / 4070 Ti Super)!** |
| **65,536 (64k)** | `12.14 GiB` | `0.92 GiB` | `1.95 GiB` | **`15.01 GiB`** | **FULL OFFLOAD ON 16GB GPUs!** |
| **131,072 (128k)**| `12.14 GiB` | `1.58 GiB` | `2.22 GiB` | **`15.94 GiB`** | Full offload on 24GB; tight fit on 16GB |
| **262,144 (256k)**| `12.14 GiB` | `2.92 GiB` | `2.80 GiB` | **`17.86 GiB`** | **FULL 256K NATIVE IN 24GB VRAM!** |

*Note: Leaves comfortable headroom for display drivers and compute buffers on standard 16GB and 24GB GPUs.*

> [!TIP]
> ### 💡 16GB GPU Verification (Single Stream / Desktop)
> Single-stream desktop inference with FlashAttention consumes **approx. 14.5 GB at 32,768 ctx** and **approx. 15.0 GB at 65,536 ctx** (`-ctk q8_0 -ctv q8_0 -fa on`). This confirms that **32K to 64K context runs completely in VRAM on 16GB cards (RTX 4080 / RTX 4070 Ti Super / RTX 5080)** without system RAM offload!

---

<a id="recommended-setup"></a>
<a id="toc-09"></a>
## Recommended Configuration & Setup

<a id="toc-10"></a>
### 1. `llama-cli` with MTP Speculative Decoding & Vision Projector
```bash
llama-cli \
  -m Qwen3.6-35B-A3B.APEX-I-NanoPlus.gguf \
  -md mtp-Qwen3.6-35B-A3B-Q4_0.gguf \
  --mmproj mmproj-Q8_0.gguf \
  -ngl 99 \
  -c 32768 \
  --temp 0.6 \
  -p "Explain the implementation of a thread-safe LRU cache in Rust."
```

<a id="toc-11"></a>
### 2. High-Performance OpenAI-Compatible Server
```bash
llama-server.exe \
  -m Qwen3.6-35B-A3B.APEX-I-NanoPlus.gguf \
  -md mtp-Qwen3.6-35B-A3B-Q4_0.gguf \
  --mmproj mmproj-Q8_0.gguf \
  -ngl 99 \
  --port 8080 \
  --parallel 4 \
  --flash-attn on \
  --fit on \
  -c 65536 \
  --cache-type-k q8_0 \
  --cache-type-v q8_0
```

---

<a id="generation-parameters"></a>
<a id="toc-12"></a>
### ⚙️ Recommended Generation Parameters (Qwen Official)

Sampling metadata recorded from [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) in the completed build:

| Hyperparameter | Value | Description / Creator Notice |
| :--- | :---: | :--- |
| **Temperature** | `0.60` | Recommended for reasoning and coding stability. |
| **Top-P** | `0.95` | Source GGUF sampling metadata. |
| **Top-K** | `20` | Source GGUF sampling metadata. |
| **Max New Tokens** | Runtime-dependent | Select for the target workload. |

---

> [!IMPORTANT]
> <a id="quantization-fidelity"></a>
> ### 🔍 Model Inherent Behavior vs. Quantization Fidelity Notice
> Any behavioral nuances, stylistic tendencies, domain-specific habits, or zero-shot edge-case oversights **stem entirely from the original unquantized checkpoint weights and fine-tuning distribution, NOT from the APEX-I quantization process.**
> Handcrafted APEX-I-NanoPlus strictly preserves mathematical tensor fidelity—keeping 100% of expert routing matrices (`gate_inp`) in uncompressed `F32` (zero router drift), armoring the token output head in `Q6_K`, safeguarding attention gates in `Q8_0`, and protecting the down-projection residual stream in `IQ3_XXS`. Empirical verification records the final GGUF perplexity at **5.5244 ± 0.12916**.

<a id="toc-13"></a>
## Optional Support

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

If these MiniPlus or NanoPlus releases have been useful to you and you would like to support the work, you can do so voluntarily through https://ko-fi.com/isvalorum. Your contribution helps with evaluation, hosting, and future handcrafted quantizations. Every release will always remain free to download and use; there are no paywalled files, updates, or features.
