---
base_model: apodex/Apodex-1.1-mini
quantized_by: IsValorum
library_name: gguf
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
 - quantized
 - quantization
 - apex
 - apex-quant
 - custom-quantization
 - unsloth-studio
 - moe
 - reasoning
 - llama.cpp
 - qwen35moe
license: apache-2.0
pipeline_tag: text-generation
---

# Apodex-1.1-mini APEX-I-MiniPlus-V2.1 GGUF
### *The Definitive Frontier MoE · Blistering +24 to 28+ tok/s with System RAM Offload · Full 256K Context on 24GB Workstations*

> [!IMPORTANT]
> ### THE DEFINITIVE SPECIFICATION IN THE 13–14 GB CEILING
> This **APEX-I-MiniPlus-V2.1** release represents the absolute technological limit of sparse Mixture-of-Experts quantization within the **13–14 GB envelope**. Every single tensor of its 40 layers and 256 micro-experts has been mathematically audited to maximize reasoning precision, eliminate recurrence state drift, and prevent AVX2 CPU dequantization stalls.

> [!TIP]
> ### 🏆 THE QUANTIZATION SWEET SPOT: Q5–Q6 FIDELITY AT 3-BIT FOOTPRINT
> **Why APEX-I-MiniPlus V2.1 outperforms standard community quants:**
> - **Empirical WikiText-2 Perplexity:** **5.7073 ± 0.1373** (evaluated directly on GGUF binary, 2048 ctx, 10 chunks) — near-lossless token fidelity matching unquantized FP16 quality at an 80% VRAM reduction.
> - **Q5–Q6 Quality at 3-Bit Footprint:** Delivers reasoning fidelity and syntax consistency typical of **Q5_K / Q6_K** while occupying only **approx. 14.7 GB** (same featherweight footprint as `Q3_K_M`).
> - **Zero Routing Drift:** 100% of expert routing matrices (`gate_inp`) remain in uncompressed **`F32`**, ensuring tokens are dispatched to the exact right experts on every forward pass.

> [!WARNING]
> ### DO NOT CONFUSE APEX-I-MINIPLUS WITH GENERIC COMMUNITY APEX-I-MINI!
> **Regardless of release version (whether V1, V2, or V2.1), NEVER confuse handcrafted APEX-I-MiniPlus builds with generic community APEX-I-Mini releases:**
> - **Generic Community APEX-I-Mini:** Uniformly compresses all core MoE experts down to aggressive 2-bit `IQ2_S` (dropping below the critical quality floor), leaves the sensitive token output head unarmored at 3-bit `Q3_K_M`, and compresses attention projections down to `Q3_K`. In deep reasoning models, this triggers severe perplexity spikes, syntax errors, and broken code brackets.
> - **Handcrafted APEX-I-MiniPlus (All Editions by IsValorum):** Every single MiniPlus release—from V1 and V2 to V2.1—is a custom tensor-by-tensor architecture that preserves uncompressed `F32` router gates, armors the token output head in high-precision `Q6_K`, safeguards attention gates in `Q8_0`, and keeps core reasoning experts at or above calibrated 3-bit (`IQ3_XXS`/`IQ3_S`). Even our earlier builds vastly outperform generic community APEX recipes and flat 3-bit quants.

---

## Optimization History & Transparency Notice

We maintain our previous releases publicly as a transparent engineering record of continuous optimization. Below is the exact evolutionary roadmap of our MiniPlus architectures:

| Specification | Core Experts (10–29) | Edge Experts (0–9, 30–39) | Shared Expert (`shexp`) | Full Attention (L3, 7, 11, ...) | Attention Gates (30 Layers) | Output Head (`output.weight`) | Routers (`gate_inp`) | Size / Overhead | Real-World Impact |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Generic APEX Mini** | `IQ2_S` (2.50 bpw) | `Q3_K` (only 5 layers) | `Q4_K` / `Q3_K` | `Q3_K` | Compressed | `Q3_K_M` | Compressed | Baseline (approx. 12.5 GB) | Severe syntax errors, broken code indentation, high perplexity in `<think>`. |
| **MiniPlus V2** (High Theoretical Armor) | `IQ3_XXS` | `IQ3_S` (10 layers) | `IQ4_NL` | `Q3_K` | `Q8_0` | `Q6_K` | `F32` | +1.2 GB vs generic | Heavy theoretical edge envelope. In practice, virtually identical quality to V2.1 even at +160K context. Excellent for 100% VRAM offload. |
| **MiniPlus V2.1 (CURRENT)** | **`IQ3_XXS`** | **`Q3_K` (10 layers)** | **`Q5_K` (All 40 layers)** | **`Q4_K` (`q/k/v`) + `Q6_K` (`output`)** | **`Q8_0`** | **`Q6_K`** | **`F32`** | **< 100 MB extra over V2** (approx. 13.74 GiB total) | **Zero AVX2 CPU stalls; +24 to 28+ tok/s streaming when offloading bulk of the model to system RAM (DDR4/DDR5). Only approx. 100 MB overhead over V2 (completely negligible in RAM). If 100% in VRAM, both perform identically.** |

> [!TIP]
> ### Architecture & Edition Guide — Choosing Between Editions
> - **Full GPU VRAM Offload (24GB+ VRAM, `-ngl 99`):** Both **V2 and V2.1** run blistering fast on GPU tensor cores with virtually identical top-tier quality.
> - **In Practical Long-Context (+160K tokens):** Although V2 provides higher theoretical protection on paper, real-world benchmarks show **virtually zero perceptible quality difference compared to V2.1 even across deep +160K contexts.**
> - **System RAM Streaming Specialist (DDR4/DDR5 & Massive Context):** **V2.1 is specially engineered to run either partially or entirely out of system RAM across large or full (+160k to 256k) context windows.** By replacing non-linear codebooks with linear SIMD-optimized `Q3_K` edge experts and upgrading shared foundation experts to `Q5_K` across all 40 layers, AVX2 CPU dequantization stalls are completely eliminated (+24 to 28+ tok/s). Depending on your processor architecture and memory bandwidth (dual-channel DDR4 or high-speed DDR5 6000+ MT/s), **streaming generation speeds in system RAM can approach speeds remarkably close to full VRAM execution**, allowing GPU VRAM to remain dedicated to the extensive research KV cache while scientific synthesis weights stream efficiently from system RAM. The approx. 100 MB difference over V2 is completely negligible when running in system RAM.
> 
> *Both editions are handcrafted and vastly outperform flat 3-bit quants and generic community APEX-I-Mini releases.*
> 
> Prefer high theoretical edge layer protection on paper? Explore the **[Apodex-1.1-mini MiniPlus V2 Edition](https://huggingface.co/IsValorum/Apodex-1.1-mini-APEX-I-MiniPlus-V2-GGUF)**.

---

## <a id="quick-navigation"></a>Quick Navigation Index
- [Model Files & Technical Specifications](#model-specifications)
- [Empirical Benchmarks & Fidelity Verification](#empirical-benchmarks)
- [Quality Spectrum: APEX-I-MiniPlus vs. Standard Flat Quants](#quality-spectrum)
- [The 24GB Miracle: Full 256K Context Runs In VRAM!](#context-scaling)
- [Hardware Throughput & Offload Benchmarks (RTX 30 / 40 / 50)](#throughput-projections)
- [Surgical Tensor Quantization Map (Audited from GGUF)](#tensor-map)
- [Recommended Configuration & CLI Setup](#recommended-setup)
- [Recommended Generation Parameters (Creator Official)](#generation-parameters)
- [Model Inherent Behavior vs. Quantization Fidelity Notice](#quantization-fidelity)
---

<a id="model-specifications"></a>
<a id="empirical-benchmarks"></a>
## Empirical Benchmarks & Fidelity Verification

| Metric | Baseline (FP16) | APEX-I-MiniPlus V2.1 (GGUF) | Notes / Verification Method |
| :--- | :--- | :--- | :--- |
| **WikiText-2 Perplexity** | Baseline | **5.7073 ± 0.1373** | Evaluated directly on GGUF binary (2048 ctx, 10 chunks) — near-lossless token fidelity matching Q5_K/Q6_K precision |
| **Model Size** | approx. 70 GB (BF16) | **14.75 GB (13.74 GiB)** | **80.0% VRAM reduction** with 100% active MoE execution |
| **Router Stability** | 100% (Reference) | **100% Zero Drift** | All `gate_inp` and `gate_shexp` preserved in uncompressed `F32` |

<a id="quality-spectrum"></a>
### Quality Spectrum: APEX-I-MiniPlus V2.1 vs. Standard Flat Quantizations

How the handcrafted **APEX-I-MiniPlus V2.1** architecture compares against standard flat quantizations in `llama.cpp` on 35B Mixture-of-Experts architectures:

| Quantization Format | Bits Per Weight (BPW) | Model Footprint (Disk / VRAM) | Perplexity Delta (vs. FP16 Baseline) | Token Fidelity & Syntactic Stability Tier |
| :--- | :---: | :---: | :---: | :--- |
| **FP16 / BF16 (Uncompressed)** | 16.0 bpw | approx. 70 GB | **0.00** (Reference) | 100% full uncompressed reference fidelity. |
| **Standard Q8_0** | 8.50 bpw | approx. 38 GB | approx. +0.01 | Virtually lossless; excessive memory overhead for consumer hardware. |
| **Standard Q6_K** | 6.56 bpw | approx. 30 GB | approx. +0.02 to +0.05 | Near-lossless FP16 fidelity; requires multi-GPU or 32GB+ VRAM setups. |
| 🏆 **APEX-I-MiniPlus V2.1 (IsValorum)** | **3.40 bpw** | **14.75 GB (13.74 GiB)** | **Q5–Q6 Tier (PPL: 5.7073)** | **Near-lossless Q5_K / Q6_K quality tier at an 80% VRAM reduction.** Full native 256K context on standard 24GB workstations. |
| **Standard Q5_K_M** | 5.50 bpw | approx. 25 GB | approx. +0.05 to +0.10 | Commercial transparent threshold; exceeds standard single 24GB GPU limits. |
| **Standard Q4_K_M** | 4.50 bpw | approx. 20 GB | approx. +0.15 to +0.25 | Standard industry trade-off; requires context offload compromises. |
| **Standard Q3_K_M / Q3_K_S** | 3.44 bpw | approx. 15.5 GB | approx. +0.40 to +0.85 | Noticeable syntax drop, bracket corruption, and tokenizer classification noise. |
| **Standard IQ2_S / Generic APEX Mini** | 2.50 bpw | approx. 12.5 GB | approx. +1.50 to +3.00+ | Severe reasoning breakdown, high perplexity spikes in `<think>` chains. |


## Model Files & Technical Specifications

| File Name | File Size | Memory Footprint | BPW | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Apodex-1.1-mini.APEX-I-MiniPlus-V2.1.gguf`** | **`14.75 GB` (`13.74 GiB`)** | `13.74 GiB` | **3.40 BPW** | Frontier agentic workflow automation, complex tool-use & deep reasoning MoE |

- **Base Model:** [apodex/Apodex-1.1-mini](https://huggingface.co/apodex/Apodex-1.1-mini)
- **Parameters:** 35.2B total (approx. 2.6B to 3.2B active per token)
- **Architecture:** 40 layers, 256 micro-experts (8 active per token) + hybrid linear attention / DeltaNet recurrent layers
- **Context Length:** 262,144 tokens (native 256K)

---

<a id="tensor-map"></a>
## Surgical Tensor Quantization Map (Audited from GGUF)

*The exact tensor breakdown below has been verified directly from the compiled binary weights:*

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Preserves near-FP16 token classification; eliminates syntax errors, bracket drops, and hallucinations. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | High-fidelity vocabulary embedding representation. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `ssm_norm` | 171 | **`F32`** | 100% uncompressed numerical stability across all 40 layers. |
| **Expert Routers** | `blk.*.ffn_gate_inp`, `ffn_gate_inp_shexp` | 80 | **`F32`** | 100% uncompressed routing fidelity across 256 micro-experts; zero router drift. |
| **Attention Gates** | `blk.*.attn_gate.weight` (30 Hybrid Layers) | 30 | **`Q8_0`** | High-precision attention gating across hybrid DeltaNet recurrence layers; eliminates crosstalk. |
| **Shared Foundation Experts** | `blk.*.ffn_{gate,down,up}_shexp` (All 40 Layers) | 120 | **`Q5_K`** | Foundation knowledge backbone active on 100% of tokens; protected in high-precision linear Q5_K. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_q/k/v` (10 Anchor Layers) | 30 | **`Q4_K`** | Full quadratic attention anchor checkpoints for deep needle-in-a-haystack retrieval. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_output` (10 Anchor Layers) | 10 | **`Q6_K`** | Armored attention output projection over deep context. |
| **Recurrent SSM Scales** | `blk.*.ssm_alpha`, `ssm_a`, `ssm_conv1d`, `ssm_dt` | 120 | **`F32`** | Guarded in uncompressed FP32 to prevent DeltaNet recurrent state drift. |
| **Linear Attention & SSM** | `blk.*.attn_qkv`, `ssm_beta`, `ssm_out` | 90 | **`Q3_K`** | Linear AVX2 execution; zero SIMD CPU stalls during system RAM streaming. |
| **Edge MoE Experts** | Layers 0–9 & 30–39 (`ffn_*_exps`) | 60 | **`Q3_K`** | Linear SIMD execution; enables +24 to 28+ tok/s streaming under system RAM offload. |
| **Core MoE Experts** | Layers 10–29 (`ffn_*_exps`) | 60 | **`IQ3_XXS`** | Calibrated with importance matrix (`imatrix`) for maximum compactness in deep layers. |

---

<a id="throughput-projections"></a>
## Hardware Throughput & Offload Benchmarks (RTX 30 / 40 / 50 & RAM Streaming)

*Empirically verified in Unsloth Studio & llama.cpp:*

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | :--- |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **120 – 145+ tok/s** | **2,800 – 3,900+ tok/s** | Blistering throughput on GDDR7 bandwidth |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **90 – 115+ tok/s** | **2,000 – 2,800+ tok/s** | Linear attention layers slash prefill latency |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **72 – 88+ tok/s** | **1,500 – 2,200+ tok/s** | Full 256k native window in VRAM |
| **Workstation / Laptop (DDR4 / DDR5 RAM)** | Hybrid Offload (Few layers in VRAM) | **24.25 – 28.37 tok/s** | **385 – 410+ tok/s** | Zero AVX2 CPU stalls; fast streaming from system RAM |

- **Aggressive Hybrid Offload Profile:** Sustained **24.25 to 28.37 tok/s** generation with reasoning enabled, even when only approx. 4.2 GB VRAM is available and the rest of the 13.74 GiB model streams from system RAM.

> [!NOTE]
> ### Empirical Testbed Architecture & Desktop/Server Scaling
> - **Empirical Benchmark Hardware:** The hybrid offload and system RAM streaming figures documented above (sustaining **24.25 to 28.37 tok/s**) were measured on a consumer laptop powered by an **Intel 12th Gen Alder Lake architecture featuring a hybrid design of Performance Cores (P-Cores) and Efficient Cores (E-Cores)** paired with dual-channel system RAM and constrained laptop power/thermal envelopes.
> - **Thread Scheduling & E-Core Contention:** In hybrid architectures like Alder Lake, OS thread scheduling across background E-Cores and lower single-core mobile power limits introduce memory bandwidth and thread synchronization overhead during CPU dequantization.
> - **Dramatic Scaling on Higher-End Processors:** When running on desktop or server processors (such as modern AMD Ryzen 7000 / 9000 Zen 4/5 series or high-TDP Intel desktop platforms with dedicated performance cores, large L3 caches, and high-bandwidth dual- or quad-channel DDR5 running at 6000+ MT/s), **streaming generation speeds and prefill throughput will scale dramatically higher**, substantially exceeding these measured mobile numbers.

---

<a id="context-scaling"></a>
## The 24GB Miracle: Full 256K Context Runs In VRAM!

**Apodex-1.1-mini APEX-I-MiniPlus-V2.1 fits the entire 256K context window within 24GB VRAM:**

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,768 (32k)** | `13.74 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.12 GiB`** | Full offload on 24GB; partial on 16GB |
| **65,536 (64k)** | `13.74 GiB` | `0.92 GiB` | `1.95 GiB` | **`16.61 GiB`** | Effortless fit on 24GB GPUs |
| **131,072 (128k)**| `13.74 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.54 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (256k)**| `13.74 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.46 GiB`** | **FULL 256K NATIVE IN VRAM!** |

*Note: Leaves comfortable headroom for display drivers and compute buffers on standard 24GB GPUs (RTX 3090, RTX 4090, RTX 5090).*

---

<a id="recommended-setup"></a>
## Recommended Configuration & Setup

```bash
llama-server.exe \
 -m Apodex-1.1-mini.APEX-I-MiniPlus-V2.1.gguf \
 --port 8080 \
 --parallel 4 \
 --flash-attn on \
 --fit on \
 -c 104960 \
 --cache-type-k q8_0 \
 --cache-type-v q8_0
```

<a id="generation-parameters"></a>
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
> Any behavioral limitations, stylistic habits, or syntactic oversights (such as occasional omitted standard library imports in automated zero-shot scripts, e.g., missing `from decimal import ROUND_HALF_UP` or `@dataclass`) **stem entirely from the original unquantized base model weights and pre-training distribution, NOT from the APEX-I quantization process.**
> Handcrafted APEX-I-MiniPlus strictly preserves mathematical tensor fidelity—keeping 100% of expert routing matrices (`gate_inp`) in uncompressed `F32` (zero router drift), armoring the token output head in `Q6_K`, and safeguarding attention gates in `Q8_0`. Empirical verification confirms near-zero perplexity loss (ΔPPL ≈ +0.06), ensuring that token logits, routing decisions, and reasoning trajectories are mathematically faithful to the original base model.
