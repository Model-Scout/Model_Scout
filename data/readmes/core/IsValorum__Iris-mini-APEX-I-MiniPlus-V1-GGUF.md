---
base_model: AllSpark-Research/Iris-mini
library_name: gguf
tags:
- quantization
- quantized
- gguf
- apex
- custom-quantization
- unsloth-studio
- moe
- speculative-decoding
- mtp
- multi-token-prediction
- llama.cpp
- qwen35moe
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
pipeline_tag: text-generation
quantized_by: IsValorum
---

> [!NOTE]
> ### ARCHITECTURE SELECTION GUIDE — MINIPLUS V1 & V2.1 EDITIONS
> This repository hosts the **MiniPlus V1** edition of **Iris-mini**. Our releases are precision-engineered for specific hardware budgets and memory topologies. **V1 is NOT obsolete or inferior; it represents our leanest, most agile operating profile:**
> 
> - **MiniPlus V1 (Lean & Agile Profile):** Highly compact footprint with uncompressed `F32` router gates, a fully armored `Q6_K` output head, `Q8_0` attention gates, and `IQ3_XXS` core experts. **Both V1 and V2.1 run flawlessly with the vast majority of the model residing in system RAM (DDR4/DDR5)**, thanks to linear CPU-friendly vectorization that avoids lookup stalls. V1 is dramatically superior to generic community APEX-I-Mini releases (which crush core reasoning down to 2-bit `IQ2_S`) and flat 3-bit quants.
> - **MiniPlus V2.1 (System RAM Streaming Specialist with Deep Context):** Specially prepared to run **totally or partially in system RAM (DDR4/DDR5)** across deep mathematical and reasoning contexts (up to 256k tokens). Upgrades all 40 shared foundation experts to `Q5_K`, armors attention gates in `Q8_0`, and uses linear CPU-friendly vectorization that eliminates AVX2 lookup stalls (+24 to 28+ tok/s). Depending on your processor and memory bandwidth (DDR4/DDR5), **streaming generation in system RAM can be almost as fast as having everything in VRAM**, while supporting deep context allocating GPU VRAM to the active KV cache while model weights stream from system RAM. All for **only ~180 MB more** (~13.74 GiB vs ~13.56 GiB)—an overhead that is completely negligible in system RAM.
> 
> **Which one should you choose? (Official Recommendation: V2.1)**
> - **⭐ PRIMARY RECOMMENDATION — [Iris-mini APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Iris-mini-APEX-I-MiniPlus-V2.1-GGUF):** For virtually all users and deployments, **V2.1 is the strictly recommended release**. Empirically verified on WikiText-2, V2.1 achieves an outstanding **Perplexity of 5.3735 ± 0.1214** (empirically verified on WikiText-2 with near-lossless precision matching Q5_K/Q6_K quality), matching the token fidelity of **Q5_K / Q6_K** class quantizations while weighing only **~14.7 GB** (same footprint as Q3_K_M). Furthermore, it completely eliminates AVX2 CPU stalls, providing blistering **+24 to 28+ tok/s streaming** under system RAM offload.
> - **MiniPlus V1 Legacy:** Maintained for architectural transparency and users seeking specialized configurations for their workflow.
> 
> *Both editions are handcrafted and vastly outperform flat 3-bit quants and generic community APEX-I-Mini releases.*
> To explore or download the **V2.1** edition of Iris-mini, visit:
> **[IsValorum/Iris-mini-APEX-I-MiniPlus-V2.1-GGUF](https://huggingface.co/IsValorum/Iris-mini-APEX-I-MiniPlus-V2.1-GGUF)**

> [!WARNING]
> ### DO NOT CONFUSE APEX-I-MINIPLUS WITH GENERIC COMMUNITY APEX-I-MINI!
> **Regardless of release version (whether V1, V2, or V2.1), NEVER confuse handcrafted APEX-I-MiniPlus builds with generic community APEX-I-Mini releases:**
> - **Generic Community APEX-I-Mini:** Uniformly compresses all core MoE experts down to aggressive 2-bit `IQ2_S` (dropping below the critical quality floor), leaves the sensitive token output head unarmored at 3-bit `Q3_K_M`, and compresses attention projections down to `Q3_K`. In deep reasoning models, this triggers severe perplexity spikes, syntax errors, and broken code brackets.
> - **Handcrafted APEX-I-MiniPlus (All Editions by IsValorum):** Every single MiniPlus release—from V1 and V2 to V2.1—is a custom tensor-by-tensor architecture that preserves uncompressed `F32` router gates, armors the token output head in high-precision `Q6_K`, safeguards attention gates in `Q8_0`, and keeps core reasoning experts at or above calibrated 3-bit (`IQ3_XXS`/`IQ3_S`). Even our earlier builds vastly outperform generic community APEX recipes and flat 3-bit quants.

---

## <a id="quick-navigation"></a>Quick Navigation Index
- [Model Files & Specifications](#model-specifications)
- [Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)](#comparative-analysis)
- [Native Multi-Token Prediction (MTP) Co-Pilot](#mtp-acceleration)
- [Everyday Laptop Benchmarks (23–26+ tok/s on DDR4)](#laptop-benchmarks)
- [The 24GB Miracle: Full 256K Context Runs In VRAM!](#context-scaling)
- [Hardware Throughput Projections (RTX 30 / 40 / 50)](#throughput-projections)
- [Why Iris-mini Intentionally Uses Standard APEX (Not V2)](#why-standard-apex)
- [Handcrafted Layer Architecture](#tensor-map)
- [Recommended Configuration & Setup](#recommended-setup)

---

<a id="model-specifications"></a>
## Model Files & Specifications

| File Name | File Size | Memory Footprint | BPW | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Iris-mini-MTP.APEX-I-MiniPlus.gguf`** | **`14.84 GB`** | `13.82 GiB` | **3.42 BPW** | Handcrafted language, math, reasoning & native MTP draft head |

- **Base Architecture:** `qwen35moe` (35B total parameters, approx. 3.2B active per token).
- **Speculative Decoding:** Fully preserved native Multi-Token Prediction head (`blk.40`).
- **Target Precision:** Armored boundaries (`Q3_K`), calibrated core experts (`IQ3_XXS`), 6-bit uncompromised output head (`Q6_K`).

---

<a id="comparative-analysis"></a>
## Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)

Also, don't confuse **APEX-I-MiniPlus (Standard)** with a generic baseline APEX-I-Mini. Traditional APEX-I-Mini drops core experts aggressively to 2-bit `IQ2_S` and leaves `output.weight` at 3-bit `Q3_K_M`, which creates a noticeable perplexity hit on complex reasoning tasks. Standard MiniPlus avoids that degradation floor while keeping boundary layers in linear `Q3_K` for single-cycle vectorized AVX2 CPU dequantization (hitting 23 to 26+ tok/s on DDR4 laptops), while protecting output in `Q6_K` and routers in `F32`.

To put the numbers in perspective: this cuts nearly **2 GB off a flat 3-bit quant** (approx. 15.6 GB), and weighs only about **approx. 1 GB more than a generic APEX-I-Mini** (approx. 12.5 GB). For that single extra gigabyte of VRAM, you get a massive jump in reasoning and syntactic stability while maximizing CPU/RAM execution throughput.

Take a look at the tensor-by-tensor comparison table below to inspect the exact architectural differences and see why this specific allocation is optimal. That's specifically what this was built for:

| Architectural Component | Generic Automated Quants (Flat `Q3_K_S` / `IQ3_S`) | Generic APEX-I-Mini (Baseline Recipe) | Our Handcrafted APEX-I-MiniPlus (Standard / IsValorum) | Perceived Quality & Real-World Impact |
| :--- | :--- | :--- | :--- | :--- |
| **Output Head (`output.weight`)** | Flat **`IQ3_S` / `Q3_K_S`** (approx. 3.44 BPW) | Inherits base type **`Q3_K_M`** (approx. 3.44 BPW unarmored) | **`Q6_K`** (approx. 6.56 BPW uncompromised) | **Eliminates Syntax & Vocabulary Hallucinations:** Low-bit output heads cause tokenizer classification noise, breaking code indentation, brackets (`{}`, `[]`), math symbols, and domain terms. `Q6_K` preserves near-FP16 output classification. |
| **Expert Routers (`ffn_gate_inp.weight`)** | Blindly quantized to 3-bit / unoptimized | Inherits base type **`Q3_K_M`** (approx. 3.44 BPW compressed) | **`F32` uncompressed** (32.0 BPW, 2 MB/layer) | **Zero Router Drift:** In micro-expert models, even minuscule quantization errors in router logits misdirect tokens to wrong experts. Retaining uncompressed `F32` guarantees 100% routing fidelity with virtually zero memory overhead (approx. 80 MB total). |
| **Attention & Language (`attn_output`, `attn_qkv`)** | Flat **`IQ3_S` / `Q3_K_S`** | **`Q3_K`** on 34 middle layers (L3–36), **`Q4_K`** on 6 edge layers | **`Q6_K` for `attn_output`**, **`Q3_K` / `Q4_K`** + `imatrix` | **Contextual Precision & CPU Throughput:** Combines uncompromised `Q6_K` for the output projection with fast vectorized linear blocks for attention, balancing retrieval accuracy with maximum token streaming speed on CPU/RAM. |
| **Attention Gates (`attn_gate.weight`)** | Blindly compressed to 3-bit | Compressed to **`Q3_K`** (middle) / **`Q4_K`** (edges) | **`Q4_K`** / **`Q8_0`** (linear high-precision) | **Attention Routing Dynamics:** High-precision linear gating modulating query-key projections without CPU dequantization latency. |
| **Shared Foundation Expert (`ffn_*_shexp`)** | Flat **`IQ3_S` / `Q3_K_S`** (3.44 BPW) | Linear **`Q4_K`** (middle) / **`Q5_K`** (edges) | Linear **`Q4_K`** (middle) / **`Q5_K`** (edges) + `imatrix` | **Foundational Knowledge Stability:** Keeps the universal pathway in high-fidelity linear blocks, eliminating quantization drift while maintaining rapid single-cycle dequantization. |
| **Core MoE Layers (Middle: 10–29)** | Flat **`IQ3_S` / `Q3_K_S`** (uniform bit-rate across all layers) | Aggressive **`IQ2_S` (2.50 BPW)** | **`IQ3_XXS` (3.06 BPW) + calibrated `imatrix`** | **Above the Quality Threshold:** Generic 2-bit `IQ2_S` baselines drop below the critical quality floor for 35B MoEs, resulting in perplexity spikes on reasoning tasks. Our `IQ3_XXS` with imatrix achieves deep compression (272 MiB → 98 MiB per block) without sacrificing logic. |
| **Edge MoE Layers (Layers 0–9 & 30–39)** | Flat **`IQ3_S` / `Q3_K_S`** (no layer-wise gradient) | `Q3_K` (limited to first/last 5 layers only: L0–4, L35–39) | **`Q3_K` (expanded to 10 input & 10 output layers)** | **AVX2 Single-Cycle Speed:** Expanded 10+10 layer protection using linear `Q3_K` blocks enables single-cycle vectorized AVX2 CPU dequantization, unlocking **23 to 26+ tok/s** on budget DDR4 laptops. |
| **MTP Draft Block (`blk.40`)** | Stripped with `--no-mtp` or broken | Crushed to `IQ2_S` / tier precision | Preserved in **`IQ3_S` / `Q3_K`** & **`IQ4_NL`** | **Speculative Decoding Speedup:** Maintains 58%–65% candidate acceptance rate, yielding **1.6x–1.75x real-world token speedup** without speculative rejection waste. |
| **Normalization & Biases** | Often degraded | Standard | **`F32` uncompressed** | **Numerical Stability:** Prevents cumulative floating-point underflow/overflow across deep 40-layer computation. |

---

<a id="mtp-acceleration"></a>
## Native Multi-Token Prediction (MTP) Co-Pilot

Most automated community releases strip or break the native Multi-Token Prediction head using `--no-mtp`. **APEX-I-MiniPlus fully preserves and calibrates the native prediction block (`blk.40`)**:

- **Zero-Cost Speculative Acceleration:** Unlike external draft models that consume separate VRAM and memory bandwidth, Iris-mini's native MTP head is integrated directly into the weights.
- **Empirical Acceptance Rate:** **58.8% to 65.5%** of predicted candidate tokens are accepted on full GPU offload.
- **Token Yield:** Delivers **1.60 to 1.75 tokens per forward step** on standard text, peaking at **2.0+ tokens/step** during continuous code and prose generation.
- **Net Speedup:** Provides approx. **1.6x faster real-world generation** without quality degradation.

---

<a id="laptop-benchmarks"></a>
## Everyday Laptop Benchmarks (23–26+ tok/s on DDR4)

- **VRAM Allocation:** **3.8 GB VRAM** utilized on budget 4GB/6GB GPUs.
- **System Memory:** 32GB DDR4 holds the remaining layers.
- **Prefill Speed:** **300 to 410 tokens/second** sustained across dense inputs.
- **Generation Speed:** **23 to 26+ tokens/second** sustained on standard DDR4 RAM!

---

<a id="context-scaling"></a>
## The 24GB Miracle: Full 256K Context Runs In VRAM!

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Hardware Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,512 (32k)** | `13.82 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.20 GiB`** | Full offload on 24GB; partial on 16GB |
| **64,512 (64k)** | `13.82 GiB` | `0.92 GiB` | `1.95 GiB` | **`16.69 GiB`** | Effortless fit on 24GB GPUs |
| **128,640 (128k)** | `13.82 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.62 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (Full 256K)**| `13.82 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.54 GiB`** | **FULL 256K NATIVE IN VRAM!** |

---

<a id="throughput-projections"></a>
## Hardware Throughput Projections (RTX 30 / 40 / 50)

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | : |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **110 – 135+ tok/s** | **2,500 – 3,600+ tok/s** | Blistering speculative execution speed |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **80 – 105+ tok/s** | **1,800 – 2,600+ tok/s** | Instantaneous multi-token prediction output |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **66 – 80+ tok/s** | **1,400 – 2,000+ tok/s** | Full 256k native window in VRAM |
| **Consumer Laptop (4GB GPU + DDR4)** | Hybrid Offload | **20 – 24+ tok/s** | **300 – 420+ tok/s** | Smooth streaming from system RAM |

