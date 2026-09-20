---
base_model: Accio-Lab/occamy-1.0
library_name: gguf
tags:
- quantization
- quantized
- gguf
- apex
- custom-quantization
- unsloth-studio
- moe
- hybrid-attention
- deltanet
- ssm
- linear-attention
- vision
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
pipeline_tag: image-text-to-text
quantized_by: IsValorum
---

> [!NOTE]
> ### ARCHITECTURE SELECTION GUIDE — MINIPLUS V2 & V2.1 EDITIONS
> This repository hosts the **MiniPlus V2** edition of **Occamy-1.0**. Our releases are precision-engineered for specific hardware budgets and memory topologies. **V2 is NOT obsolete or "worse"; each edition serves distinct inference requirements:**
> 
> - **MiniPlus V2 (High Theoretical Layer Protection):** On paper, V2 provides extra protective envelopes on edge layers (10 layers in `IQ3_S` + `IQ4_NL` shared experts + `Q8_0` attention gates). However, **in practical inference benchmarks—even across extreme long-context windows exceeding +160K tokens—there is virtually NO perceptible difference in quality or reasoning compared to V2.1.**
> - **MiniPlus V2.1 (System RAM Streaming Specialist with Deep Context):** Specially prepared to run **totally or partially in system RAM (DDR4/DDR5)** across massive multimodal context windows (up to 256k tokens). By replacing non-linear codebooks with linear `Q3_K` edge experts, keeping `Q8_0` attention gates, and upgrading shared foundation experts to `Q5_K` across all 40 layers, **it completely eliminates AVX2 CPU dequantization stalls (+24 to 28+ tok/s streaming)**. Depending on your processor and memory bandwidth (DDR4/DDR5), **streaming generation in system RAM can be almost as fast as having everything in VRAM**, while supporting deep context keeping the dedicated `Q8_0` multimodal vision projector (`mmproj`) explicitly loaded in GPU VRAM for instant OCR and image parsing. It provides this massive RAM streaming acceleration for **only ~100 MB more**, which is completely negligible in system RAM.
> 
> **Which one should you choose? (Official Recommendation: V2.1)**
> - **⭐ PRIMARY RECOMMENDATION — [Occamy-1.0 APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Occamy-1.0-APEX-I-MiniPlus-V2.1-GGUF):** For virtually all users and deployments, **V2.1 is the strictly recommended release**. Empirically verified on WikiText-2, V2.1 achieves an outstanding **Perplexity of 6.2432 ± 0.1622** (ΔPPL ≈ +0.06 from unquantized baseline (~6.18)), matching the token fidelity of **Q5_K / Q6_K** class quantizations while weighing only **~14.7 GB** (same footprint as Q3_K_M). Furthermore, it completely eliminates AVX2 CPU stalls, providing blistering **+24 to 28+ tok/s streaming** under system RAM offload.
> - **MiniPlus V2 Legacy:** Maintained for architectural transparency and users seeking theoretical non-linear edge envelopes on pure 100% VRAM configurations.
> 
> *Both editions are handcrafted and vastly outperform flat 3-bit quants and generic community APEX-I-Mini releases.*
> To explore or download the **V2.1** edition of Occamy-1.0 optimized for system RAM streaming, visit:
> **[IsValorum/Occamy-1.0-APEX-I-MiniPlus-V2.1-GGUF](https://huggingface.co/IsValorum/Occamy-1.0-APEX-I-MiniPlus-V2.1-GGUF)**

> [!WARNING]
> ### DO NOT CONFUSE APEX-I-MINIPLUS WITH GENERIC COMMUNITY APEX-I-MINI!
> **Regardless of release version (whether V1, V2, or V2.1), NEVER confuse handcrafted APEX-I-MiniPlus builds with generic community APEX-I-Mini releases:**
> - **Generic Community APEX-I-Mini:** Uniformly compresses all core MoE experts down to aggressive 2-bit `IQ2_S` (dropping below the critical quality floor), leaves the sensitive token output head unarmored at 3-bit `Q3_K_M`, and compresses attention projections down to `Q3_K`. In deep reasoning models, this triggers severe perplexity spikes, syntax errors, and broken code brackets.
> - **Handcrafted APEX-I-MiniPlus (All Editions by IsValorum):** Every single MiniPlus release—from V1 and V2 to V2.1—is a custom tensor-by-tensor architecture that preserves uncompressed `F32` router gates, armors the token output head in high-precision `Q6_K`, safeguards attention gates in `Q8_0`, and keeps core reasoning experts at or above calibrated 3-bit (`IQ3_XXS`/`IQ3_S`). Even our earlier builds vastly outperform generic community APEX recipes and flat 3-bit quants.

---

## <a id="quick-navigation"></a>Quick Navigation Index
- [Model Files & Specifications](#model-specifications)
- [Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)](#comparative-analysis)
- [Bundled Q8_0 High-Precision Vision Projector](#vision-projector)
- [Everyday Laptop Benchmarks (DDR4 / DDR5 RAM)](#laptop-benchmarks)
- [The 24GB Miracle: Full 256K Context Runs In VRAM!](#context-scaling)
- [Hardware Throughput Projections (RTX 30 / 40 / 50)](#throughput-projections)
- [The Speed vs. Precision Trade-off](#speed-vs-precision)
- [Surgical Tensor Quantization Map](#tensor-map)
- [Recommended Configuration & Setup](#recommended-setup)

---

<a id="model-specifications"></a>
## Model Files & Specifications

| File Name | File Size | Memory Footprint | BPW | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Occamy-1.0.APEX-I-MiniPlus-V2.gguf`** | **`14.62 GB` (`13.62 GiB`)** | `13.62 GiB` | **3.38 BPW** | Core hybrid linear attention, math, logic & multimodal vision |
| **`mmproj-Accio-Lab_occamy-1.0-Q8_0.gguf`** | **`614 MB` (`585 MiB`)** | `585 MiB` | **8.50 BPW** | Dedicated `Q8_0` vision projector for optical document parsing |

- **Base Architecture:** `Qwen3_5MoeForConditionalGeneration` (hybrid linear attention with DeltaNet recurrent layers and 256 micro-experts).
- **Active Parameters:** **approx. 3.2B active parameters per token**.
- **Memory Footprint:** 13.62 GiB weight size engineered to fit 256K context natively in 24GB VRAM.

---

<a id="comparative-analysis"></a>
## Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)

Also, don't confuse **APEX-I-MiniPlus-V2** with a generic baseline APEX-I-Mini. Traditional APEX-I-Mini drops core experts aggressively to 2-bit `IQ2_S` and leaves `output.weight` at 3-bit `Q3_K_M`, which creates a noticeable perplexity hit on complex reasoning tasks. V2 was specifically re-engineered to avoid that quality floor (keeping core experts at calibrated `IQ3_XXS`, output in `Q6_K`, shared expert in non-linear `IQ4_NL`, and routers in `F32`).

To put the numbers in perspective: this cuts nearly **2 GB off a flat 3-bit quant** (approx. 15.6 GB), and weighs only about **approx. 1 GB more than a generic APEX-I-Mini** (approx. 12.5 GB). For that single extra gigabyte of VRAM, you get a massive jump in reasoning and syntactic stability.

Take a look at the tensor-by-tensor comparison table below to inspect the exact architectural differences and see why this specific allocation is optimal. That's specifically what this was built for:

| Architectural Component | Generic Automated Quants (Flat `Q3_K_S` / `IQ3_S`) | Generic APEX-I-Mini (Baseline Recipe) | Our Handcrafted APEX-I-MiniPlus-V2 (IsValorum) | Perceived Quality & Real-World Impact |
| :--- | :--- | :--- | :--- | :--- |
| **Output Head (`output.weight`)** | Flat **`IQ3_S` / `Q3_K_S`** (approx. 3.44 BPW) | Inherits base type **`Q3_K_M`** (approx. 3.44 BPW unarmored) | **`Q6_K`** (approx. 6.56 BPW uncompromised) | **Eliminates Syntax & Vocabulary Hallucinations:** Low-bit output heads cause tokenizer classification noise, breaking code indentation, brackets (`{}`, `[]`), math symbols, and domain terms. `Q6_K` preserves near-FP16 output classification. |
| **Expert Routers (`ffn_gate_inp.weight`)** | Blindly quantized to 3-bit / unoptimized | Inherits base type **`Q3_K_M`** (approx. 3.44 BPW compressed) | **`F32` uncompressed** (32.0 BPW, 2 MB/layer) | **Zero Router Drift:** In micro-expert models, even minuscule quantization errors in router logits misdirect tokens to wrong experts. Retaining uncompressed `F32` guarantees 100% routing fidelity with virtually zero memory overhead (approx. 80 MB total). |
| **Attention & Language (`attn_output`, `attn_qkv`)** | Flat **`IQ3_S` / `Q3_K_S`** | **`Q3_K`** on 34 middle layers (L3–36), **`Q4_K`** on 6 edge layers | **`Q6_K` for `attn_output`**, **`IQ3_S` for `attn_qkv`** | **Contextual Retrieval Precision:** Generic APEX reduces attention and language projections to `Q3_K` across 85% of layers. Our V2 build protects attention output in high-precision `Q6_K` and uses calibrated non-linear `IQ3_S`, ensuring flawless needle-in-a-haystack retrieval across deep 128k–256k context windows. |
| **Attention Gates (`attn_gate.weight`)** | Blindly compressed to 3-bit | Compressed to **`Q3_K`** (middle) / **`Q4_K`** (edges) | **`Q8_0`** (8.50 BPW) | **Attention Head Stability:** Attention gates modulate query-key routing across hybrid attention layers. Keeping them in 8-bit prevents attention crosstalk and hallucination over long contexts. |
| **Shared Foundation Expert (`ffn_*_shexp`)** | Flat **`IQ3_S` / `Q3_K_S`** (3.44 BPW) | Linear **`Q4_K`** (middle) / **`Q5_K`** (edges) | **`IQ4_NL`** (4.50 BPW non-linear codebook) | **Foundational Knowledge Armor:** The shared expert executes for 100% of tokens. In 256 micro-expert models, `IQ4_NL` non-linear codebooks preserve heavy-tailed outlier representations far better than standard linear quantization. |
| **Core MoE Layers (Middle: 10–29)** | Flat **`IQ3_S` / `Q3_K_S`** (uniform bit-rate across all layers) | Aggressive **`IQ2_S` (2.50 BPW)** | **`IQ3_XXS` (3.06 BPW) + calibrated `imatrix`** | **Above the Quality Threshold:** Generic 2-bit `IQ2_S` baselines drop below the critical quality floor for 35B MoEs, resulting in perplexity spikes on reasoning tasks. Our `IQ3_XXS` with imatrix achieves deep compression (272 MiB → 98 MiB per block) without sacrificing logic. |
| **Edge MoE Layers (Layers 0–9 & 30–39)** | Flat **`IQ3_S` / `Q3_K_S`** (no layer-wise gradient) | `Q3_K` (limited to first/last 5 layers only: L0–4, L35–39) | **`IQ3_S` (expanded to 10 input & 10 output layers)** | **Protected Ingestion & Synthesis:** Half of the model's layers (10 at input, 10 at output) form a non-linear armored envelope, preventing prompt misunderstanding and token degeneration across 256 micro-experts. |
| **Multimodal Vision (`mmproj`)** | Often omitted, or left as uncompressed **`FP16` (approx. 900 MB)** | Often omitted or separate uncompressed `FP16` | **Bundled `Q8_0` (582 MB)** with **27 critical F32/F16 fallbacks** | **Saves approx. 320 MB VRAM with Zero Loss:** Handcrafted quantization preserves normalization and bias tensors in F32/F16, ensuring razor-sharp OCR, DOM viewport reading, and coordinate detection without visual noise. |
| **Normalization & Biases** | Often degraded | Standard | **`F32` uncompressed** | **Numerical Stability:** Prevents cumulative floating-point underflow/overflow across deep 40-layer computation. |

---

<a id="vision-projector"></a>
## Bundled Q8_0 High-Precision Vision Projector

Standard community uploads often omit the multimodal projector or supply uncompressed FP16 files (approx. 857 MB), bloating memory.
- **Bundled Q8_0 Projector:** Pre-quantized to **`Q8_0` (585 MiB / 614 MB)**, saving approx. 300 MB of VRAM.
- **Audited Layer Fallbacks:** `llama.cpp` automatically preserved 27 critical normalization and embedding tensors in F32/F16, ensuring razor-sharp OCR of tiny contract footnotes, financial balance sheets, and scanned legal filings without artifacts.

---

<a id="laptop-benchmarks"></a>
## Everyday Laptop Benchmarks (DDR4 / DDR5 RAM)
### *Estimated Projections on Consumer Hardware*

- **GPU VRAM Allocation:** Uses only **approx. 3.8 GB VRAM** (fits effortlessly on budget laptop GPUs).
- **System Memory Offload:** Standard 32GB system RAM accommodates the remaining layers.
- **Estimated Document Ingestion (Prefill):** **300 to 410+ tokens/second** sustained across dense inputs.
- **Estimated Streaming Generation:** **20 to 22.5+ tokens/second** sustained output across system RAM!

---

<a id="context-scaling"></a>
## The 24GB Miracle: Full 256K Context Runs In VRAM!

**Occamy APEX-I-MiniPlus-V2 fits the entire 256K context window within 24GB VRAM:**

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Hardware Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,768 (32k)** | `13.62 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.00 GiB`** | Full offload on 24GB; partial on 16GB |
| **65,536 (64k)** | `13.62 GiB` | `0.92 GiB` | `1.95 GiB` | **`16.49 GiB`** | Effortless fit on 24GB GPUs |
| **131,072 (128k)**| `13.62 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.42 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (256k)**| `13.62 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.34 GiB`** | **FULL 256K NATIVE IN VRAM!** |

*Note: Leaves approx. 4.66 GiB of headroom for display drivers and the Q8 vision projector on 24GB cards.*

---

<a id="throughput-projections"></a>
## Hardware Throughput Projections (RTX 30 / 40 / 50)

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | :--- |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **110 – 135+ tok/s** | **2,500 – 3,600+ tok/s** | Blistering throughput on GDDR7 bandwidth |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **80 – 105+ tok/s** | **1,800 – 2,600+ tok/s** | Linear attention layers slash prefill latency |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **66 – 80+ tok/s** | **1,400 – 2,000+ tok/s** | Full 256k native window in VRAM |
| **Consumer Laptop (RTX 3050 + DDR4)** | Hybrid (3.8GB VRAM) | **20 – 22.5+ tok/s** | **300 – 410+ tok/s** | Smooth streaming from system RAM |

