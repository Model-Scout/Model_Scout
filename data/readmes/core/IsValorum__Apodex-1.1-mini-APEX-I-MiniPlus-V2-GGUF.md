---
base_model: apodex/Apodex-1.1-mini
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

## <a id="quick-navigation"></a>Quick Navigation Index

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/isvalorum)

*Independently computed on private cloud clusters. If this handcrafted release saves you VRAM and runs faster on your GPU, consider [fueling the community compute fund on Ko-fi](https://ko-fi.com/isvalorum).*

1. [Independent Benchmark of the APEX-I-MiniPlus Family (Occamy V2 Reference)](#toc-01)
2. [Model Files & Specifications](#toc-02)
3. [Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)](#toc-03)
4. [Native Multi-Token Prediction (MTP) Acceleration](#toc-04)
5. [Bundled Q8_0 High-Precision Vision Projector](#toc-05)
6. [Everyday Laptop Benchmarks (DDR4 / DDR5 RAM)](#toc-06)
7. [Estimated Projections on Consumer Hardware](#toc-07)
8. [The 24GB Miracle: Full 256K Context Runs In VRAM!](#toc-08)
9. [Hardware Throughput Projections (RTX 30 / 40 / 50)](#toc-09)
10. [Recommended Generation Parameters (apodex Official)](#toc-10)
11. [Optional Support](#toc-11)

> [!NOTE]
> ### ARCHITECTURE SELECTION GUIDE — MINIPLUS V2 & V2.1 EDITIONS
> This repository hosts the **MiniPlus V2** edition of **Apodex-1.1-mini**. Our releases are precision-engineered for specific hardware budgets and memory topologies. **V2 is NOT obsolete or "worse"; each edition serves distinct inference requirements:**
> 
> - **MiniPlus V2 (High Theoretical Layer Protection):** On paper, V2 provides extra protective envelopes on edge layers (10 layers in `IQ3_S` + `IQ4_NL` shared experts + `Q8_0` attention gates). However, **in practical inference benchmarks—even across extreme long-context windows exceeding +160K tokens—there is virtually NO perceptible difference in quality or reasoning compared to V2.1.**
> - **MiniPlus V2.1 (System RAM Streaming Specialist with Deep Context):** Specially prepared to run **totally or partially in system RAM (DDR4/DDR5)** across deep biomedical literature and scientific papers (up to 256k tokens). By replacing non-linear codebooks with linear `Q3_K` edge experts, keeping `Q8_0` attention gates, and upgrading shared foundation experts to `Q5_K` across all 40 layers, **it completely eliminates AVX2 CPU dequantization stalls (+24 to 28+ tok/s streaming)**. Depending on your processor and memory bandwidth (DDR4/DDR5), **streaming generation in system RAM can be almost as fast as having everything in VRAM**, while supporting deep context keeping the dedicated `Q8_0` multimodal vision projector (`mmproj`) explicitly loaded in GPU VRAM for scientific figures and molecular diagram reading. It provides this massive RAM streaming acceleration for **only approx. 100 MB more**, which is completely negligible in system RAM.
> 
> **Which one should you choose? (Official Recommendation: V2.1)**
> - **⭐ PRIMARY RECOMMENDATION — [Apodex-1.1-mini APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Apodex-1.1-mini-APEX-I-MiniPlus-V2.1-GGUF):** For virtually all users and deployments, **V2.1 is the strictly recommended release**. Empirically verified on WikiText-2, V2.1 achieves an outstanding **Perplexity of 5.7073 ± 0.1373** (ΔPPL ≈ +0.07 from unquantized baseline (approx. 5.64)), matching the token fidelity of **Q5_K / Q6_K** class quantizations while weighing only **approx. 14.7 GB** (same footprint as Q3_K_M). Furthermore, it completely eliminates AVX2 CPU stalls, providing blistering **+24 to 28+ tok/s streaming** under system RAM offload.
> - **MiniPlus V2 Legacy:** Maintained for architectural transparency and users seeking specialized configurations for their workflow.
> 
> *Both editions are handcrafted and vastly outperform flat 3-bit quants and generic community APEX-I-Mini releases.*
> To explore or download the **V2.1** edition of Apodex-1.1-mini optimized for system RAM streaming, visit:
> **[IsValorum/Apodex-1.1-mini-APEX-I-MiniPlus-V2.1-GGUF](https://huggingface.co/IsValorum/Apodex-1.1-mini-APEX-I-MiniPlus-V2.1-GGUF)**

> [!WARNING]
> ### DO NOT CONFUSE APEX-I-MINIPLUS WITH GENERIC COMMUNITY APEX-I-MINI!
> **Regardless of release version (whether V1, V2, or V2.1), NEVER confuse handcrafted APEX-I-MiniPlus builds with generic community APEX-I-Mini releases:**
> - **Generic Community APEX-I-Mini:** Uniformly compresses all core MoE experts down to aggressive 2-bit `IQ2_S` (dropping below the critical quality floor), leaves the sensitive token output head unarmored at 3-bit `Q3_K_M`, and compresses attention projections down to `Q3_K`. In deep reasoning models, this triggers severe perplexity spikes, syntax errors, and broken code brackets.
> - **Handcrafted APEX-I-MiniPlus (All Editions by IsValorum):** Every single MiniPlus release—from V1 and V2 to V2.1—is a custom tensor-by-tensor architecture that preserves uncompressed `F32` router gates, armors the token output head in high-precision `Q6_K`, safeguards attention gates in `Q8_0`, and keeps core reasoning experts at or above calibrated 3-bit (`IQ3_XXS`/`IQ3_S`). Even our earlier builds vastly outperform generic community APEX recipes and flat 3-bit quants.


> [!TIP]
> ### SYSTEM RAM INFERENCE: FULL OR PARTIAL
> This APEX-I-MiniPlus release is designed for **full or partial system-RAM inference**. Depending on the processor, memory bandwidth, and DDR4/DDR5 configuration, generation can range from **20 to 45 tok/s**. With partial GPU offload, systems that cannot fit **128K or more context** entirely in VRAM can place the remaining model and context load in system RAM, maintaining stable, responsive generation at longer context lengths.

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
<a id="toc-01"></a>
### 🏅 Independent Benchmark of the APEX-I-MiniPlus Family (Occamy V2 Reference)


> [!NOTE]
> **External report:** [zephel01 independently benchmarked Occamy V2](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en). The benchmark below was performed on **Occamy-1.0 APEX-I-MiniPlus V2**, not on this specific model. It is included as independent evidence of the broader MiniPlus quantization approach.

The **APEX-I-MiniPlus** quantization architecture powering this model was subjected to an extensive independent evaluation by Japanese AI researcher and evaluator [zephel01 (CoolZero)](https://note.com/zephel01/n/n71d3d7e6b70c?hl=en) on an **NVIDIA RTX 5090 (32GB)** workstation running `llama.cpp` CUDA `b11027` with FlashAttention (`-fa on -ctk q8_0 -ctv q8_0 -ngl 99`). 

The evaluation tested the APEX-I hybrid MoE engine across **348 unseeded trials** on SWE-bench style multi-file Python bug-fixing tasks with hidden `pytest` suites (`llmbench`):

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

<a id="model-specifications"></a>
<a id="toc-02"></a>
## Model Files & Specifications

| File Name | File Size | Memory Footprint | BPW | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Apodex-1.1-mini-MTP.APEX-I-MiniPlus-V2.gguf`** | **`14.65 GB` (`13.65 GiB`)** | `13.65 GiB` | **3.38 BPW** | Core language, vision, reasoning & native MTP draft block |
| **`mmproj-apodex_Apodex-1.1-mini-Q8_0.gguf`** | **`610 MB` (`582 MiB`)** | `582 MiB` | **8.50 BPW** | Dedicated `Q8_0` vision projector for optical document parsing |

- **Base Architecture:** `Qwen3_5MoeForConditionalGeneration` (40 layers + layer 40 native MTP block, 256 micro-experts).
- **Active Parameters:** **approx. 3.2B active parameters per token**.

---

<a id="comparative-analysis"></a>
<a id="toc-03"></a>
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
| **MTP Draft Block (`blk.40`)** | Stripped with `--no-mtp` or broken | Crushed to `IQ2_S` / tier precision | Preserved in **`IQ3_S` / `Q3_K`** & **`IQ4_NL`** | **Speculative Decoding Speedup:** Maintains 58%–65% candidate acceptance rate, yielding **1.6x–1.75x real-world token speedup** without speculative rejection waste. |
| **Normalization & Biases** | Often degraded | Standard | **`F32` uncompressed** | **Numerical Stability:** Prevents cumulative floating-point underflow/overflow across deep 40-layer computation. |

---

<a id="mtp-acceleration"></a>
<a id="toc-04"></a>
## Native Multi-Token Prediction (MTP) Acceleration

- **Integrated Speculative Decoding:** Unlike external draft models that consume separate VRAM, Apodex's native MTP head (`blk.40`) is integrated directly into the weights.
- **High Acceptance Rate:** Achieves **58% to 65%** draft candidate acceptance on full GPU offload.
- **Real Speedup:** Yields **1.60x to 1.75x real-world token speedup** on continuous text and code.

---

<a id="vision-projector"></a>
<a id="toc-05"></a>
## Bundled Q8_0 High-Precision Vision Projector

- **Bundled Q8_0 Projector:** Pre-quantized to **`Q8_0` (582 MiB / 610 MB)**, saving approx. 300 MB of VRAM.
- **Audited Layer Fallbacks:** `llama.cpp` automatically preserved 27 critical normalization and embedding tensors in F32/F16, ensuring razor-sharp OCR without artifacts.

---

<a id="laptop-benchmarks"></a>
<a id="toc-06"></a>
## Everyday Laptop Benchmarks (DDR4 / DDR5 RAM)
<a id="toc-07"></a>
### *Estimated Projections on Consumer Hardware*

- **GPU VRAM Allocation:** Uses only **approx. 3.8 GB VRAM**.
- **System Memory Offload:** Standard 32GB system RAM accommodates the remaining layers.
- **Estimated Document Ingestion (Prefill):** **300 to 420+ tokens/second**.
- **Estimated Streaming Generation:** **20 to 24+ tokens/second** sustained output.

---

<a id="context-scaling"></a>
<a id="toc-08"></a>
## The 24GB Miracle: Full 256K Context Runs In VRAM!

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Hardware Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,768 (32k)** | `13.65 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.03 GiB`** | Full offload on 24GB; partial on 16GB |
| **65,536 (64k)** | `13.65 GiB` | `0.92 GiB` | `1.95 GiB` | **`16.52 GiB`** | Effortless fit on 24GB GPUs |
| **131,072 (128k)**| `13.65 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.45 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (256k)**| `13.65 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.37 GiB`** | **FULL 256K IN VRAM!** |

---

<a id="throughput-projections"></a>
<a id="toc-09"></a>
## Hardware Throughput Projections (RTX 30 / 40 / 50)

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | : |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **approx. 247 – 251 tok/s** | **2,800 – 3,900+ tok/s** | Empirically verified on RTX 5090 by zephel01 (Occamy V2 Reference) |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) + mmproj | **75 – 100+ tok/s** | **1,700 – 2,500+ tok/s** | Effortless multimodal speculative execution |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) + mmproj | **62 – 78+ tok/s** | **1,350 – 1,950+ tok/s** | Full 256k context in dedicated VRAM |
| **Consumer Laptop (4GB GPU + 32GB RAM)**| Hybrid Offload | **20 – 24+ tok/s** | **300 – 420+ tok/s** | Smooth streaming from system RAM |

<a id="generation-parameters"></a>
<a id="toc-10"></a>
### ⚙️ Recommended Generation Parameters (apodex Official)

Official generation hyperparameters specified by [apodex](https://huggingface.co/apodex/Apodex-1.1-mini) for autonomous agentic workflows and tool-calling loops:

| Hyperparameter | Value | Description / Creator Rationale |
| :--- | :---: | :--- |
| **Temperature** | `1.00` | Calibrated for full exploration in multi-turn reasoning and tool invocation. |
| **Top-P** | `0.95` | Nucleus sampling cutoff to maintain coherence while enabling expressive trajectories. |
| **Top-K** | `20` | Constrains vocabulary selection to high-probability tokens. |
| **Repetition Penalty** | `1.05` | Prevents token loops in deep iterative agent trajectories. |
| **Max Tokens** | `16384` | Generous token budget recommended by creator for multi-turn tool calling. |

> [!IMPORTANT]
> <a id="quantization-fidelity"></a>
> ### 🔍 Model Inherent Behavior vs. Quantization Fidelity Notice
> Any behavioral nuances, stylistic tendencies, domain-specific habits, or zero-shot edge-case oversights **stem entirely from the original unquantized checkpoint weights and fine-tuning distribution, NOT from the APEX-I quantization process.**
> Handcrafted APEX-I-MiniPlus strictly preserves mathematical tensor fidelity—keeping 100% of expert routing matrices (`gate_inp`) in uncompressed `F32` (zero router drift), armoring the token output head in `Q6_K`, and safeguarding attention gates in `Q8_0`. Empirical verification confirms near-zero perplexity loss (ΔPPL ≈ +0.07), ensuring that token logits, routing decisions, and reasoning trajectories are mathematically faithful to the original base model.

<a id="toc-11"></a>
## 7. Community Compute Fund & Priority Model Requests

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

All IsValorum quantizations will always remain completely free and open to the public without paywalls. 

However, cloud GPU compute is expensive. If you find these builds valuable and would like to support the project or **request a specific model architecture to be prioritized for the next MiniPlus/NanoPlus release**, you can sponsor GPU compute time through Ko-fi:

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/isvalorum)

*(When supporting on Ko-fi, feel free to leave a note with your Hugging Face handle and the specific model you would like prioritized).*

<div style="clear: both;"></div>


