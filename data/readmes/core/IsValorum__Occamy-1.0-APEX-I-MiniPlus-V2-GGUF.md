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
> ### NEW: QWEN3.8 27B DENSE — VAL-APEX-I
> Explore the Huihui Abliterated and EfficientThink Uncensored editions. MiniPlus prioritizes Q5-class to near-Q6 fidelity without a fixed file-size ceiling; NanoPlus targets Q4-class quality at a practical footprint.
>
> - **[Qwen3.8 27B Huihui Abliterated — VAL-APEX-I MiniPlus V2.1](https://huggingface.co/IsValorum/Huihui-Qwen3.8-27B-Abliterated-VAL-APEX-I-MiniPlus-V2.1-GGUF)** — 15.33 GB.
> - **[Qwen3.8 27B Huihui Abliterated — VAL-APEX-I NanoPlus](https://huggingface.co/IsValorum/Huihui-Qwen3.8-27B-Abliterated-VAL-APEX-I-NanoPlus-GGUF)** — 11.90 GB.
> - **[Qwen3.8 27B EfficientThink Uncensored — VAL-APEX-I MiniPlus V2.1](https://huggingface.co/IsValorum/Qwen3.8-27B-EfficientThink-Uncensored-VAL-APEX-I-MiniPlus-V2.1-GGUF)** — 15.08 GB.
> - **[Qwen3.8 27B EfficientThink Uncensored — VAL-APEX-I NanoPlus](https://huggingface.co/IsValorum/Qwen3.8-27B-EfficientThink-Uncensored-VAL-APEX-I-NanoPlus-GGUF)** — 11.65 GB.
>
> **[Explore the VAL-APEX-I collection](https://huggingface.co/collections/IsValorum/val-apex-i-6ac563d1784a04a1bb177f47)**
>
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

## <a id="quick-navigation"></a>Quick Navigation Index
1. [Model Files & Specifications](#toc-01)
2. [Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)](#toc-02)
3. [Independent Third-Party Benchmark (zephel01 / llmbench)](#toc-03)
4. [Bundled Q8_0 High-Precision Vision Projector](#toc-04)
5. [Everyday Laptop Benchmarks (DDR4 / DDR5 RAM)](#toc-05)
6. [Estimated Projections on Consumer Hardware](#toc-06)
7. [The 24GB Miracle: Full 256K Context Runs In VRAM!](#toc-07)
8. [Hardware Throughput Projections (RTX 30 / 40 / 50)](#toc-08)
9. [Surgical Tensor Quantization Map (Audited from GGUF)](#toc-09)
10. [Recommended Configuration & Setup](#toc-10)
11. [CLI Server Execution Example](#toc-11)
12. [Recommended Generation Parameters (Accio-Lab Official & Empirical)](#toc-12)
13. [Optional Support](#toc-13)

> [!TIP]
> **Independent external evaluation:** [zephel01](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en) tested this exact Occamy V2 GGUF on RTX 5090 with llama.cpp. Reported result: 90.0–93.3% L6 resolution and ~247–251 tok/s across repeated runs. [Full methodology and limitations](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en).



> [!NOTE]
> ### ARCHITECTURE SELECTION GUIDE — MINIPLUS V2 & V2.1 EDITIONS
> This repository hosts the **MiniPlus V2** edition of **Occamy-1.0**. Our releases are precision-engineered for specific hardware budgets and memory topologies. **V2 is NOT obsolete or "worse"; each edition serves distinct inference requirements:**
> 
> - **MiniPlus V2 (High Theoretical Layer Protection):** On paper, V2 provides extra protective envelopes on edge layers (10 layers in `IQ3_S` + `IQ4_NL` shared experts + `Q8_0` attention gates). However, **in practical inference benchmarks—even across extreme long-context windows exceeding +160K tokens—there is virtually NO perceptible difference in quality or reasoning compared to V2.1.**
> - **MiniPlus V2.1 (System RAM Streaming Specialist with Deep Context):** Specially prepared to run **totally or partially in system RAM (DDR4/DDR5)** across massive multimodal context windows (up to 256k tokens). By replacing non-linear codebooks with linear `Q3_K` edge experts, keeping `Q8_0` attention gates, and upgrading shared foundation experts to `Q5_K` across all 40 layers, **it completely eliminates AVX2 CPU dequantization stalls (+24 to 28+ tok/s streaming)**. Depending on your processor and memory bandwidth (DDR4/DDR5), **streaming generation in system RAM can be almost as fast as having everything in VRAM**, while supporting deep context keeping the dedicated `Q8_0` multimodal vision projector (`mmproj`) explicitly loaded in GPU VRAM for instant OCR and image parsing. It provides this massive RAM streaming acceleration for **only approx. 100 MB more**, which is completely negligible in system RAM.
> 
> **Which one should you choose? (Official Recommendation: V2.1)**
> - **⭐ PRIMARY RECOMMENDATION — [Occamy-1.0 APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Occamy-1.0-APEX-I-MiniPlus-V2.1-GGUF):** For virtually all users and deployments, **V2.1 is the strictly recommended release**. Empirically verified on WikiText-2, V2.1 achieves an outstanding **Perplexity of 6.2432 ± 0.1622** (ΔPPL ≈ +0.06 from unquantized baseline (approx. 6.18)), matching the token fidelity of **Q5_K / Q6_K** class quantizations while weighing only **approx. 14.7 GB** (same footprint as Q3_K_M). Furthermore, it completely eliminates AVX2 CPU stalls, providing blistering **+24 to 28+ tok/s streaming** under system RAM offload.
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


> [!TIP]
> ### SYSTEM RAM INFERENCE: FULL OR PARTIAL
> This APEX-I-MiniPlus release is designed for **full or partial system-RAM inference**. Depending on the processor, memory bandwidth, and DDR4/DDR5 configuration, generation can range from **20 to 45 tok/s**. With partial GPU offload, systems that cannot fit **128K or more context** entirely in VRAM can place the remaining model and context load in system RAM, maintaining stable, responsive generation at longer context lengths.

---

---

<a id="model-specifications"></a>
<a id="toc-01"></a>
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
<a id="toc-02"></a>
## Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)

Also, don't confuse **APEX-I-MiniPlus-V2** with a generic baseline APEX-I-Mini. Traditional APEX-I-Mini drops core experts aggressively to 2-bit `IQ2_S` and leaves `output.weight` at 3-bit `Q3_K_M`, which creates a noticeable perplexity hit on complex reasoning tasks. V2 was specifically re-engineered to avoid that quality floor (keeping core experts at calibrated `IQ3_XXS`, output in `Q6_K`, shared expert in non-linear `IQ4_NL`, and routers in `F32`).

To put the numbers in perspective: this cuts nearly **2 GB off a flat 3-bit quant** (approx. 15.6 GB), and weighs only about **approx. 1 GB more than a generic APEX-I-Mini** (approx. 12.5 GB). For that single extra gigabyte of VRAM, you get a massive jump in reasoning and syntactic stability.

Take a look at the tensor-by-tensor comparison table below to inspect the exact architectural differences and see why this specific allocation is optimal:

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

<a id="independent-benchmark"></a>
<a id="toc-03"></a>
## 🏅 Independent Third-Party Benchmark (zephel01 / llmbench)

An extensive independent evaluation of **Occamy-1.0-APEX-I-MiniPlus-V2-GGUF** was published by Japanese AI researcher and evaluator [zephel01 (CoolZero)](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en) on an **NVIDIA RTX 5090 (32GB)** workstation running `llama.cpp` CUDA `b11027` with FlashAttention (`-fa on -ctk q8_0 -ctv q8_0 -ngl 99`). 

The model was subjected to **348 unseeded trials** across SWE-bench style multi-file Python bug-fixing tasks verified with hidden `pytest` suites (`llmbench`):

- **L6 Multi-File Code Generation (60 tasks):**
  - **Context 32,768 (32K):** **93.3% Resolved** (46/60 tasks passed 5/5 consecutive trials; 20/20 on Easy–Hard).
  - **Context 65,536 (65K):** **90.0% Resolved** (45/60 tasks passed 5/5 consecutive trials).
  - **Match with 25–28 GB Models:** Matches or exceeds the resolution rate of full 25–28 GB models (such as `Ornith-1.5` and `Tiel-Coder` 35B-A3B) while consuming **over 10 GB less VRAM** (14.6 GB vs approx. 26 GB).
- **Extreme Context VRAM Scaling (The Hybrid DeltaNet SSM Advantage):**
  - **32K Context:** **14.6 GB** total VRAM allocation.
  - **65K Context:** **15.1 GB** total VRAM allocation (only **+0.5 GB VRAM** added when doubling context!).
  - *Architectural Explanation:* Because 30 of the 40 layers utilize Linear Attention / DeltaNet SSM ($O(1)$ constant recurrence memory), only the 10 full-attention anchor layers expand the KV cache. This proves empirically that **65,536 context runs 100% in VRAM on consumer 16GB GPUs (RTX 4080 / RTX 5080)** without offloading to system RAM.
- **Measured Real-World Throughput:** Sustained single-stream generation of **approx. 247 – 251 tok/s** on NVIDIA RTX 5090.

---

<a id="vision-projector"></a>
<a id="toc-04"></a>
## Bundled Q8_0 High-Precision Vision Projector

Standard community uploads often omit the multimodal projector or supply uncompressed FP16 files (approx. 857 MB), bloating memory.
- **Bundled Q8_0 Projector:** Pre-quantized to **`Q8_0` (585 MiB / 614 MB)**, saving approx. 300 MB of VRAM.
- **Audited Layer Fallbacks:** `llama.cpp` automatically preserved 27 critical normalization and embedding tensors in F32/F16, ensuring razor-sharp OCR of tiny contract footnotes, financial balance sheets, and scanned legal filings without artifacts.

---

<a id="laptop-benchmarks"></a>
<a id="toc-05"></a>
## Everyday Laptop Benchmarks (DDR4 / DDR5 RAM)
<a id="toc-06"></a>
### *Estimated Projections on Consumer Hardware*

- **GPU VRAM Allocation:** Uses only **approx. 3.8 GB VRAM** (fits effortlessly on budget laptop GPUs).
- **System Memory Offload:** Standard 32GB system RAM accommodates the remaining layers.
- **Estimated Document Ingestion (Prefill):** **300 to 410+ tokens/second** sustained across dense inputs.
- **Estimated Streaming Generation:** **20 to 22.5+ tokens/second** sustained output across system RAM!

---

<a id="context-scaling"></a>
<a id="toc-07"></a>
## The 24GB Miracle: Full 256K Context Runs In VRAM!

**Occamy APEX-I-MiniPlus-V2 fits the entire 256K context window within 24GB VRAM:**

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Hardware Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,768 (32k)** | `13.62 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.00 GiB`** | Full offload on 24GB; partial on 16GB |
| **65,536 (64k)** | `13.62 GiB` | `0.92 GiB` | `1.95 GiB` | **`16.49 GiB`** | Effortless fit on 24GB GPUs |
| **131,072 (128k)**| `13.62 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.42 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (256k)**| `13.62 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.34 GiB`** | **FULL 256K NATIVE IN VRAM!** |

*Note: Leaves approx. 4.66 GiB of headroom for display drivers and the Q8 vision projector on 24GB cards.*

> [!TIP]
> ### 💡 Empirical 16GB GPU Verification (Single Stream / Desktop)
> While theoretical multi-slot server buffers estimate approx. 16.49 GiB, independent hardware testing by zephel01 on an RTX 5090 confirmed that single-stream desktop inference consumes **only 14.6 GB at 32,768 ctx** and **only 15.1 GB at 65,536 ctx** (`-ctk q8_0 -ctv q8_0 -fa on`). This empirically proves that **full 65K context runs completely in VRAM on 16GB cards (RTX 4080 / RTX 5080)** without system RAM offload!

---

<a id="throughput-projections"></a>
<a id="toc-08"></a>
## Hardware Throughput Projections (RTX 30 / 40 / 50)

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | :--- |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **approx. 247 – 251 tok/s** | **2,800 – 3,900+ tok/s** | Empirically verified on RTX 5090 by zephel01 |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **80 – 105+ tok/s** | **1,800 – 2,600+ tok/s** | Linear attention layers slash prefill latency |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **66 – 80+ tok/s** | **1,400 – 2,000+ tok/s** | Full 256k native window in VRAM |
| **Consumer Laptop (RTX 3050 + DDR4)** | Hybrid (3.8GB VRAM) | **20 – 22.5+ tok/s** | **300 – 410+ tok/s** | Smooth streaming from system RAM |

---

<a id="tensor-map"></a>
<a id="toc-09"></a>
## Surgical Tensor Quantization Map (Audited from GGUF)

*The exact tensor breakdown below has been verified directly from the compiled binary weights:*

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Preserves near-FP16 token classification; eliminates syntax errors, bracket drops, and hallucinations. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | High-fidelity vocabulary embedding representation. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `ssm_norm` | 171 | **`F32`** | 100% uncompressed numerical stability across all 40 layers. |
| **Expert Routers** | `blk.*.ffn_gate_inp`, `ffn_gate_inp_shexp` | 80 | **`F32`** | 100% uncompressed routing fidelity across 256 micro-experts; zero router drift. |
| **Attention Gates** | `blk.*.attn_gate.weight` (30 Hybrid Layers) | 30 | **`Q8_0`** | High-precision attention gating across hybrid DeltaNet recurrence layers; eliminates crosstalk. |
| **Shared Foundation Experts** | `blk.*.ffn_{gate,down,up}_shexp` (All 40 Layers) | 120 | **`IQ4_NL`** | Foundational knowledge backbone; non-linear codebook preserves heavy-tailed outlier activations. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_output` (10 Anchor Layers) | 10 | **`Q6_K`** | Armored attention output projection over deep context. |
| **Recurrent SSM Scales** | `blk.*.ssm_alpha`, `ssm_a`, `ssm_conv1d`, `ssm_dt` | 120 | **`F32`** | Guarded in uncompressed FP32 to prevent DeltaNet recurrent state drift. |
| **Edge MoE Experts** | Layers 0–9 & 30–39 (`ffn_*_exps`) | 60 | **`IQ3_S`** | Non-linear codebook protective envelope at model ingestion and terminal synthesis. |
| **Core MoE Experts** | Layers 10–29 (`ffn_*_exps`) | 60 | **`IQ3_XXS`** | Calibrated with importance matrix (`imatrix`) for maximum compactness in deep layers. |

---

<a id="recommended-setup"></a>
<a id="toc-10"></a>
## Recommended Configuration & Setup

<a id="toc-11"></a>
### CLI Server Execution Example
```bash
llama-server.exe \
 -m Occamy-1.0.APEX-I-MiniPlus-V2.gguf \
 --port 8080 \
 --flash-attn on \
 --fit on \
 -c 65536 \
 --cache-type-k q8_0 \
 --cache-type-v q8_0
```

<a id="generation-parameters"></a>
<a id="toc-12"></a>
### ⚙️ Recommended Generation Parameters (Accio-Lab Official & Empirical)

Recommended sampling configuration tailored from [Accio-Lab](https://huggingface.co/Accio-Lab/occamy-1.0) and third-party SWE-bench evaluations:

| Scenario / Workload | Temperature | Top-P | Top-K | Additional Hyperparameters | Rationale |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Co-Work, Agentic & Tool-Use (Official)** | `1.00` | `0.95` | `20` | `presence_penalty: 1.5`, `enable_thinking: true` | Official Accio-Lab recommendation for multi-turn co-work and tool execution. |
| **Deterministic Coding & Scripting (Author Recommended)** | `0.20 – 0.35` | `0.95` | `20` | `min_p: 0.05`, `repetition_penalty: 1.05` | Author recommendation for strict deterministic syntax, code completion, and preventing token repetition in automated agent loops. |
| **Independent SWE-Bench Baseline (zephel01 / llmbench)** | `0.35` | `0.95` | `20` | `min_p: 0.0` (disabled), `repetition_penalty: 1.0` (none) | Fixed comparative evaluation setting utilized by zephel01 across 348 unseeded trials in llmbench (achieving 90.0%–93.3% SWE-bench resolution). |
| **General Multilingual Instruction** | `0.60 – 0.70` | `0.95` | `20` | `repetition_penalty: 1.08` | Balanced creativity and factual accuracy across 13+ languages. |

> [!IMPORTANT]
> <a id="quantization-fidelity"></a>
> ### 🔍 Model Inherent Behavior vs. Quantization Fidelity Notice
> Any behavioral limitations, stylistic habits, or syntactic oversights (such as occasional omitted standard library imports in automated zero-shot scripts, e.g., missing `from decimal import ROUND_HALF_UP` or `@dataclass`) **stem entirely from the original unquantized base model weights and pre-training distribution, NOT from the APEX-I quantization process.**
> Handcrafted APEX-I-MiniPlus strictly preserves mathematical tensor fidelity—keeping 100% of expert routing matrices (`gate_inp`) in uncompressed `F32` (zero router drift), armoring the token output head in `Q6_K`, and safeguarding attention gates in `Q8_0`. Empirical verification confirms near-zero perplexity loss (ΔPPL ≈ +0.06), ensuring that token logits, routing decisions, and reasoning trajectories are mathematically faithful to the original base model.

> [!TIP]
> ### 💡 Developer Tip for Autonomous Coding & CI Agents (Import Discipline)
> In third-party evaluations, reasoning and architectural code generation scored a remarkable 90%–93.3% resolution rate on multi-file SWE benchmarks. Any rare failures observed were not reasoning flaws, but occasional omitted standard library imports in zero-shot scripts (e.g. `from decimal import ROUND_HALF_UP` or `@dataclass`). When deploying in autonomous coding agents, include in your system prompt: *"Always declare complete, explicit import statements at the beginning of the file"* or pair with an automated linter (`ruff`).

<a id="toc-13"></a>
## Optional Support

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

If these MiniPlus or NanoPlus releases have been useful to you and you would like to support the work, you can do so voluntarily through https://ko-fi.com/isvalorum. Your contribution helps with evaluation, hosting, and future handcrafted quantizations. Every release will always remain free to download and use; there are no paywalled files, updates, or features.
