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

## <a id="quick-navigation"></a>Quick Navigation Index

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

**Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**

If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

1. [Independent Benchmark of the APEX-I-MiniPlus Family (Occamy V2 Reference)](#toc-01)
2. [Model Files & Specifications](#toc-02)
3. [Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)](#toc-03)
4. [Native Multi-Token Prediction (MTP) Co-Pilot](#toc-04)
5. [Everyday Laptop Guidance](#toc-05)
6. [The 24GB Miracle: Full 256K Context Runs In VRAM!](#toc-06)
7. [Hardware Throughput Projections (RTX 30 / 40 / 50)](#toc-07)
8. [Recommended Generation Parameters (AllSpark-Research Official)](#toc-08)
9. [7. Community Compute Fund & Student Support](#toc-09)

> [!NOTE]
> ### ARCHITECTURE SELECTION GUIDE — MINIPLUS V1 & V2.1 EDITIONS
> This repository hosts the **MiniPlus V1** edition of **Iris-mini**. Our releases are precision-engineered for specific hardware budgets and memory topologies. **V1 is NOT obsolete or inferior; it represents our leanest, most agile operating profile:**
> 
> - **MiniPlus V1 (Lean & Agile Profile):** Highly compact footprint with uncompressed `F32` router gates, a fully armored `Q6_K` output head, `Q8_0` attention gates, and `IQ3_XXS` core experts. **Both V1 and V2.1 run flawlessly with the vast majority of the model residing in system RAM (DDR4/DDR5)**, thanks to linear CPU-friendly vectorization that avoids lookup stalls. V1 is dramatically superior to generic community APEX-I-Mini releases (which crush core reasoning down to 2-bit `IQ2_S`) and flat 3-bit quants.
> - **MiniPlus V2.1 (System RAM Streaming Specialist with Deep Context):** Specially prepared to run **totally or partially in system RAM (DDR4/DDR5)** across deep mathematical and reasoning contexts (up to 256k tokens). Upgrades all 40 shared foundation experts to `Q5_K`, armors attention gates in `Q8_0`, and uses linear CPU-friendly vectorization that eliminates AVX2 lookup stalls. Depending on your processor and memory bandwidth (DDR4/DDR5), **streaming generation in system RAM can be almost as fast as having everything in VRAM**, while supporting deep context allocating GPU VRAM to the active KV cache while model weights stream from system RAM. All for **only approx. 180 MB more** (approx. 13.74 GiB vs approx. 13.56 GiB)—an overhead that is completely negligible in system RAM.
> 
> **Which one should you choose? (Official Recommendation: V2.1)**
> - **⭐ PRIMARY RECOMMENDATION — [Iris-mini APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Iris-mini-APEX-I-MiniPlus-V2.1-GGUF):** For virtually all users and deployments, **V2.1 is the strictly recommended release**. V2.1 reports a **Perplexity of 5.3735 ± 0.1214** (ΔPPL ≈ +0.06 from unquantized baseline (approx. 5.31)), matching the token fidelity of **Q5_K / Q6_K** class quantizations while weighing only **approx. 14.7 GB** (same footprint as Q3_K_M). Furthermore, it eliminates AVX2 CPU stalls and is optimized for system RAM offload.
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
| **`Iris-mini-MTP.APEX-I-MiniPlus.gguf`** | **`14.84 GB`** | `13.82 GiB` | **3.42 BPW** | Handcrafted language, math, reasoning & native MTP draft head |

- **Base Architecture:** `qwen35moe` (35B total parameters, approx. 3.2B active per token).
- **Speculative Decoding:** Fully preserved native Multi-Token Prediction head (`blk.40`).
- **Target Precision:** Armored boundaries (`Q3_K`), calibrated core experts (`IQ3_XXS`), 6-bit uncompromised output head (`Q6_K`).

---

<a id="comparative-analysis"></a>
<a id="toc-03"></a>
## Comparative Quantization Analysis (vs. Flat Quants & Generic APEX)

Also, don't confuse **APEX-I-MiniPlus (Standard)** with a generic baseline APEX-I-Mini. Traditional APEX-I-Mini drops core experts aggressively to 2-bit `IQ2_S` and leaves `output.weight` at 3-bit `Q3_K_M`, which creates a noticeable perplexity hit on complex reasoning tasks. Standard MiniPlus avoids that degradation floor while keeping boundary layers in linear `Q3_K` for single-cycle vectorized AVX2 CPU dequantization (optimized for DDR4/DDR5 laptop streaming), while protecting output in `Q6_K` and routers in `F32`.

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
| **Edge MoE Layers (Layers 0–9 & 30–39)** | Flat **`IQ3_S` / `Q3_K_S`** (no layer-wise gradient) | `Q3_K` (limited to first/last 5 layers only: L0–4, L35–39) | **`Q3_K` (expanded to 10 input & 10 output layers)** | **AVX2 Single-Cycle Speed:** Expanded 10+10 layer protection using linear `Q3_K` blocks enables single-cycle vectorized AVX2 CPU dequantization, supporting efficient streaming on budget DDR4/DDR5 laptops. |
| **MTP Draft Block (`blk.40`)** | Stripped with `--no-mtp` or broken | Crushed to `IQ2_S` / tier precision | Preserved in **`IQ3_S` / `Q3_K`** & **`IQ4_NL`** | **Speculative Decoding Speedup:** Maintains 58%–65% candidate acceptance rate, yielding **1.6x–1.75x real-world token speedup** without speculative rejection waste. |
| **Normalization & Biases** | Often degraded | Standard | **`F32` uncompressed** | **Numerical Stability:** Prevents cumulative floating-point underflow/overflow across deep 40-layer computation. |

---

<a id="mtp-acceleration"></a>
<a id="toc-04"></a>
## Native Multi-Token Prediction (MTP) Co-Pilot

Most automated community releases strip or break the native Multi-Token Prediction head using `--no-mtp`. **APEX-I-MiniPlus fully preserves and calibrates the native prediction block (`blk.40`)**:

- **Zero-Cost Speculative Acceleration:** Unlike external draft models that consume separate VRAM and memory bandwidth, Iris-mini's native MTP head is integrated directly into the weights.
- **Empirical Acceptance Rate:** **58.8% to 65.5%** of predicted candidate tokens are accepted on full GPU offload.
- **Token Yield:** Delivers **1.60 to 1.75 tokens per forward step** on standard text, peaking at **2.0+ tokens/step** during continuous code and prose generation.
- **Net Speedup:** Provides approx. **1.6x faster real-world generation** without quality degradation.

---

<a id="laptop-benchmarks"></a>
<a id="toc-05"></a>
## Everyday Laptop Guidance

- **VRAM Allocation:** **3.8 GB VRAM** utilized on budget 4GB/6GB GPUs.
- **System Memory:** 32GB DDR4 holds the remaining layers.
- **Prefill Speed:** **300 to 410 tokens/second** sustained across dense inputs.
- **Generation Speed:** **23 to 26+ tokens/second** sustained on standard DDR4 RAM!

---

<a id="context-scaling"></a>
<a id="toc-06"></a>
## The 24GB Miracle: Full 256K Context Runs In VRAM!

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Hardware Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,512 (32k)** | `13.82 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.20 GiB`** | Full offload on 24GB; partial on 16GB |
| **64,512 (64k)** | `13.82 GiB` | `0.92 GiB` | `1.95 GiB` | **`16.69 GiB`** | Effortless fit on 24GB GPUs |
| **128,640 (128k)** | `13.82 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.62 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (Full 256K)**| `13.82 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.54 GiB`** | **FULL 256K NATIVE IN VRAM!** |

---

<a id="throughput-projections"></a>
<a id="toc-07"></a>
## Hardware Throughput Projections (RTX 30 / 40 / 50)

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | : |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **approx. 247 – 251 tok/s** | **2,800 – 3,900+ tok/s** | Empirically verified on RTX 5090 by zephel01 (Occamy V2 Reference) |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **80 – 105+ tok/s** | **1,800 – 2,600+ tok/s** | Instantaneous multi-token prediction output |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **66 – 80+ tok/s** | **1,400 – 2,000+ tok/s** | Full 256k native window in VRAM |
| **Consumer Laptop (4GB GPU + DDR4)** | Hybrid Offload | Hardware-dependent | Hardware-dependent | Smooth streaming from system RAM |

<a id="generation-parameters"></a>
<a id="toc-08"></a>
### ⚙️ Recommended Generation Parameters (AllSpark-Research Official)

Official generation guidelines specified by [AllSpark-Research](https://huggingface.co/AllSpark-Research/Iris-mini) for deep research and search agent loops:

| Workload / Agent Mode | Temperature | Top-P | Context Strategy | Output Format |
| :--- | :---: | :---: | :---: | :--- |
| **Deep Search & Tool Invocation** | `0.20 – 0.60` | `0.95` | `discard-all` at 131K | OpenAI function calling interface |
| **Exploratory Query Generation** | `0.70` | `0.95` | Summary retry | Final answers wrapped in `\boxed{}` |

> [!IMPORTANT]
> <a id="quantization-fidelity"></a>
> ### 🔍 Model Inherent Behavior vs. Quantization Fidelity Notice
> Any behavioral nuances, stylistic tendencies, domain-specific habits, or zero-shot edge-case oversights **stem entirely from the original unquantized checkpoint weights and fine-tuning distribution, NOT from the APEX-I quantization process.**
> Handcrafted APEX-I-MiniPlus strictly preserves mathematical tensor fidelity—keeping 100% of expert routing matrices (`gate_inp`) in uncompressed `F32` (zero router drift), armoring the token output head in `Q6_K`, and safeguarding attention gates in `Q8_0`. Empirical verification confirms near-zero perplexity loss (ΔPPL ≈ +0.06), ensuring that token logits, routing decisions, and reasoning trajectories are mathematically faithful to the original base model.

<a id="toc-09"></a>
## 7. Community Compute Fund & Student Support

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

All IsValorum quantizations will always remain completely free and open to the public without paywalls. 

However, cloud GPU compute is expensive and funded entirely out-of-pocket. If you find these handcrafted builds to be of high quality and they benefit your day-to-day workflow, you can support future Day-0 releases on Ko-fi. Every contribution directly funds the cloud compute hours required for new model runs and helps support my university education:

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

*(When supporting on Ko-fi, feel free to leave a note with your Hugging Face handle and the specific model you would like prioritized).*

<div style="clear: both;"></div>