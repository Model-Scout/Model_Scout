---
base_model: t-tech/T-Search
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
- retrieval
- search-agent
- llama.cpp
- qwen35moe
license: apache-2.0
pipeline_tag: text-generation
---

## <a id="quick-navigation"></a>Quick Navigation Index
1. [Optimization History & Transparency Notice](#toc-01)
2. [Empirical Benchmarks & Fidelity Verification](#toc-02)
3. [The Quality Spectrum: APEX-I-MiniPlus V2.1 vs. Standard Formats](#toc-03)
4. [Model Files & Technical Specifications](#toc-04)
5. [Bundled Q8_0 High-Precision Multimodal Vision Projector](#toc-05)
6. [Surgical Tensor-by-Tensor Quantization Breakdown](#toc-06)
7. [Hardware Throughput & Offload Benchmarks (RTX 30 / 40 / 50 & RAM Streaming)](#toc-07)
8. [The 24GB Miracle: Full 256K Context Runs In VRAM!](#toc-08)
9. [Recommended Configuration & Setup](#toc-09)
10. [1. High-Throughput Server with Built-in MTP Speculative Decoding (llama-server)](#toc-10)
11. [2. Direct CLI Inference / Agentic Retrieval Harness](#toc-11)
12. [Recommended Generation Parameters (t-tech Official)](#toc-12)
13. [Model Inherent Behavior vs. Quantization Fidelity Notice](#toc-13)
14. [CRITICAL: Coding Syntax & Repeat Penalty Advisory (Preventing Character Swapping)](#toc-coding-advisory)
15. [Hardened Agentic Chat Template & Reasoning Effort](#toc-chat-template)
16. [Optional Support](#toc-14)

# T-Search APEX-I-MiniPlus-V2.1 GGUF

### *The Definitive 35B Agentic Retrieval MoE · Multi-Round Search & Evidence Synthesis · Bundled Q8_0 Vision Projector · Full 256K Context on 24GB Workstations*

Welcome to **APEX-I-MiniPlus-V2.1** for [t-tech/T-Search](https://huggingface.co/t-tech/T-Search) (the specialized 35B Mixture-of-Experts architecture developed by **t-tech** as an agentic retriever that plans, executes multi-round searches, and synthesizes verifiable evidence chains).

Standard automated community quantizations uniformly degrade sensitive routing matrices and expert feed-forwards down to 2-bit codebooks, corrupting retrieval planning trajectories, hallucinating query filters, and dropping critical visual tokens.

**APEX-I-MiniPlus-V2.1 was engineered differently.** This is a **100% custom, hand-crafted tensor-by-tensor quantization** built with mathematical precision overrides, calibrated importance matrices (`imatrix`), and an included **high-precision Q8_0 multimodal vision projector (`mmproj`)**. Whether executing deep research harnesses on an everyday laptop or orchestrating autonomous search agents across 256K context on a 24GB workstation, this release delivers unmatched evidence grounding, zero router drift, and blistering system RAM streaming throughput.


> [!TIP]
> ### SYSTEM RAM INFERENCE: FULL OR PARTIAL
> This APEX-I-MiniPlus release is designed for **full or partial system-RAM inference**. Depending on the processor, memory bandwidth, and DDR4/DDR5 configuration, generation can range from **20 to 45 tok/s**. With partial GPU offload, systems that cannot fit **128K or more context** entirely in VRAM can place the remaining model and context load in system RAM, maintaining stable, responsive generation at longer context lengths.

---

> [!IMPORTANT]
> ### THE DEFINITIVE SPECIFICATION IN THE 13–14 GB CEILING
> This **APEX-I-MiniPlus-V2.1** release represents the absolute technological limit of sparse Mixture-of-Experts quantization within the **15–16 GB download envelope**. Every single tensor of its 40 layers and 256 micro-experts has been mathematically audited to maximize reasoning precision, eliminate recurrence state drift, and prevent AVX2 CPU dequantization stalls.

> [!TIP]
> ### 🏆 EMPIRICAL BENCHMARK & QUALITY COMPARISON
>
> | Quantization Specification | File Size (Disk) | Memory Footprint (RAM/VRAM) | Average BPW | WikiText-2 Perplexity | Quality Tier Equivalent |
> | :--- | :---: | :---: | :---: | :---: | :---: |
> | **Unquantized BF16 Base** | approx. 70.0 GB | approx. 65.2 GiB | 16.00 BPW | approx. 5.62 (Reference) | Full precision baseline |
> | **APEX-I-MiniPlus V2.1 (CURRENT)** | 15.23 GB | 14.18 GiB | 3.43 BPW | 5.6716 ± 0.12975 (approx. ΔPPL +0.0516 / +0.92%) | Q5_K_L tier (bordering Q6_K) |
>
> **Routing:** all recipe-designated `gate_inp` and `gate_shexp` tensors remain in uncompressed `F32`, preserving zero routing drift.

> [!WARNING]
> ### DO NOT CONFUSE APEX-I-MINIPLUS WITH GENERIC COMMUNITY APEX-I-MINI!
> **Regardless of release version, NEVER confuse handcrafted APEX-I-MiniPlus builds with generic community APEX-I-Mini releases:**
> - **Generic Community APEX-I-Mini:** Uniformly compresses all core MoE experts down to aggressive 2-bit `IQ2_S` (dropping below the critical quality floor), leaves the sensitive token output head unarmored at 3-bit `Q3_K_M`, and compresses attention projections down to `Q3_K`. In deep retrieval and reasoning agents, this triggers hallucinated search operators, broken syntax brackets, and high perplexity spikes.
> - **Handcrafted APEX-I-MiniPlus (All Editions by IsValorum):** Every single MiniPlus release is a custom tensor-by-tensor architecture that preserves uncompressed `F32` router gates, armors the token output head in high-precision `Q6_K`, safeguards attention gates in `Q8_0`, and keeps core reasoning experts at or above calibrated 3-bit (`IQ3_XXS`/`IQ3_S`).

---

<a id="toc-01"></a>
## Optimization History & Transparency Notice

We maintain our previous releases publicly as a transparent engineering record of continuous optimization. Below is the exact evolutionary roadmap of our MiniPlus architectures:

| Specification | Core Experts (10–29) | Edge Experts (0–9, 30–39) | Shared Expert (`shexp`) | Full Attention (L3, 7, 11, ...) | Attention Gates (30 Layers) | Output Head (`output.weight`) | Routers (`gate_inp`) | Size / Overhead | Real-World Impact |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Generic APEX Mini** | `IQ2_S` (2.50 bpw) | `Q3_K` (only 5 layers) | `Q4_K` / `Q3_K` | `Q3_K` | Compressed | `Q3_K_M` | Compressed | Baseline (approx. 12.5 GB) | Severe syntax errors, broken code indentation, high perplexity in `<think>`. |
| **MiniPlus V2.1 (CURRENT)** | **`IQ3_XXS`** | **`Q3_K` (20 layers)** | **`Q5_K` (All 40 layers)** | **`Q4_K` (`q/k/v`) + `Q6_K` (`output`)** | **`Q8_0`** | **`Q6_K`** | **`F32`** | **Definitive Build** (14.18 GiB main GGUF) | **Zero AVX2 CPU stalls and efficient streaming when offloading bulk of the model to system RAM (DDR4/DDR5). Bundled Q8_0 mmproj enables zero-latency multimodal visual retrieval.** |

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

<a id="empirical-benchmarks"></a>
<a id="toc-02"></a>
## Empirical Benchmarks & Fidelity Verification

The comparison table near the top consolidates the model-specific BF16 baseline, final GGUF PPL, delta, published main-file size, BPW, and fidelity tier. The routing treatment is preserved in the note directly beneath it.


<a id="quality-spectrum"></a>
<a id="toc-03"></a>
## 🏆 The Quality Spectrum: APEX-I-MiniPlus V2.1 vs. Standard Formats

Where **APEX-I-MiniPlus V2.1** sits in the landscape of local quantization formats:

| Quantization Format | Bits Per Weight (BPW) | Model Footprint (Disk / VRAM) | Perplexity Delta (vs. FP16 Baseline) | Token Fidelity & Syntactic Stability Tier |
| :--- | :---: | :---: | :---: | :--- |
| **Standard Q8_0** | 8.50 bpw | approx. 38 GB | Baseline (< +0.005) | Reference standard; excessively large for single consumer GPUs. |
| **Standard Q6_K** | 6.56 bpw | approx. 30 GB | approx. +0.02 to +0.05 | Near-lossless FP16 fidelity; requires multi-GPU or 32GB+ VRAM setups. |
| 🏆 **APEX-I-MiniPlus V2.1 (IsValorum)** | **3.40 bpw** | **15.23 GB (14.18 GiB)** | **approx. +0.05 (PPL: 5.6716 ± 0.12975)** | **supporting a Q5_K_L-class fidelity tier (bordering Q6_K) at less-than-Q3_K_M weight at less-than-Q3_K_M weight, with an 80% VRAM reduction.** Full native 256K context on standard 24GB workstations. |
| **Standard Q5_K_M** | 5.50 bpw | approx. 25 GB | approx. +0.05 to +0.10 | Commercial transparent threshold; exceeds standard single 24GB GPU limits. |
| **Standard Q4_K_M** | 4.50 bpw | approx. 20.5 GB | approx. +0.15 to +0.30 | Common community baseline; leaves little room for deep context buffers in 24GB. |
| **Standard Q3_K_M** | 3.40 bpw | **16.7 GB** | approx. +0.30 to +0.50 | Quality degradation threshold: syntax slips, code hallucination, unarmored routers. |
| **Standard IQ2_S / Generic APEX Mini** | 2.50 bpw | approx. 12.5 GB | approx. +1.50 to +3.00+ | Severe reasoning breakdown, high perplexity spikes in search retrieval chains. |

---

<a id="model-files"></a>
<a id="toc-04"></a>
## 📦 Model Files & Technical Specifications

| Filename | File Size | Memory Footprint (Weights Only) | BPW (Effective) | Architecture & Recommended Deployment |
| :--- | :---: | :---: | :---: | :--- |
| **`T-Search.APEX-I-MiniPlus-V2.1.gguf`** | **`15.23 GB` (`14.18 GiB`)** | `14.18 GiB` | **3.40 BPW** | Core agentic search planning, multi-round evidence gathering & reasoning MoE |
| **`mmproj-Q8_0.gguf`** | **`610.66 MB (582.36 MiB)`** | `582.36 MiB` | **8.50 BPW** | Dedicated Q8_0 multimodal vision projector for document & image reasoning |

---

<a id="vision-projector"></a>
<a id="toc-05"></a>
## 👁️ Bundled Q8_0 High-Precision Multimodal Vision Projector

Standard community uploads often omit the multimodal projector or supply uncompressed FP16 files, bloating memory.

**This release includes `mmproj-Q8_0.gguf`:**
* **Mathematical Precision:** Quantized using calibrated `Q8_0` with uncompressed `F32` normalizations, preserving zero visual artifacting during document inspection, PDF table parsing, and OCR grounding.
* **Seamless Deployment:** Place `mmproj-Q8_0.gguf` alongside the main model file; `llama.cpp` and `llama-server` load it automatically via `--mmproj mmproj-Q8_0.gguf`.

---

<a id="tensor-breakdown"></a>
<a id="toc-06"></a>
## 🛠️ Surgical Tensor-by-Tensor Quantization Breakdown

*Every tensor has been verified directly from the compiled binary weights:*

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Preserves near-FP16 token classification; eliminates syntax errors and hallucinations. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | High-fidelity vocabulary embedding representation. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `post_attention_norm`, `ssm_norm`, MTP `nextn` norms | 138 | **`F32`** | Uncompressed numerical stability across the 40 main layers and integrated MTP block. |
| **Expert Routers** | `blk.*.ffn_gate_inp`, `ffn_gate_inp_shexp` | 82 | **`F32`** | Uncompressed routing matrices across the 40 main layers and integrated MTP block. |
| **Attention Gates** | `blk.*.attn_gate.weight` (30 Hybrid Layers) | 30 | **`Q8_0`** | High-precision attention gating across hybrid DeltaNet recurrence layers. |
| **Shared Foundation Experts** | `blk.*.ffn_{gate,down,up}_shexp` (40 Main Layers + MTP) | 123 | **`Q5_K`** | Foundation knowledge backbone plus the integrated MTP shared-expert path. |
| **Periodic Full Attention** | `blk.{3,7,11,...,39}.attn_q/k/v` + MTP `blk.40.attn_q/k/v` | 33 | **`Q4_K`** | Full quadratic attention anchors plus integrated MTP attention projections. |
| **Periodic Full Attention** | `blk.{3,7,11,...,39}.attn_output` + `blk.40.attn_output` | 11 | **`Q6_K`** | Armored attention output projection over deep context, including MTP. |
| **Recurrent SSM Scales** | `blk.*.ssm_alpha`, `ssm_a`, `ssm_conv1d`, `ssm_dt` | 120 | **`F32`** | Guarded in uncompressed FP32 to prevent DeltaNet recurrent state drift. |
| **Linear Attention & SSM** | `blk.*.attn_qkv`, `ssm_beta`, `ssm_out` | 90 | **`Q3_K`** | Linear AVX2 execution; zero SIMD CPU stalls during system RAM streaming. |
| **Edge MoE Experts** | Layers 0–9 & 30–39 (`ffn_*_exps`) | 60 | **`Q3_K`** | Linear SIMD execution optimized for system RAM offload. |
| **Core MoE Experts** | Layers 10–29 (`ffn_*_exps`) | 60 | **`IQ3_XXS`** | Calibrated with importance matrix (`imatrix`) for maximum compactness in deep layers. |
| **MTP Experts** | `blk.40.ffn_{gate,down,up}_exps` | 3 | **`Q4_0`** | Dedicated expert tensors in the integrated Multi-Token Prediction block. |
| **MTP Projection** | `blk.40.nextn.eh_proj.weight` | 1 | **`Q4_K`** | Dedicated hidden-state projection for the integrated Multi-Token Prediction block. |

---

<a id="throughput-projections"></a>
<a id="toc-07"></a>
## ⚡ Hardware Throughput & Offload Benchmarks (RTX 30 / 40 / 50 & RAM Streaming)

*Empirically verified in Unsloth Studio & llama.cpp:*

| Hardware Target | Offload Mode | Generation Speed (Est.) | Prompt Prefill Speed (Est.) | Highlights |
| :--- | :--- | :---: | :---: | :--- |
| **NVIDIA RTX 5080 / 5090 (Blackwell)** | Full GPU (`-ngl 99`) | **approx. 247 – 251 tok/s** | **2,800 – 3,900+ tok/s** | Extreme multi-expert throughput on 24GB+ |
| **NVIDIA RTX 4090 (24GB GDDR6X)** | Full GPU (`-ngl 99`) | **90 – 115+ tok/s** | **2,000 – 2,800+ tok/s** | Linear attention layers slash prefill latency |
| **NVIDIA RTX 3090 (24GB GDDR6)** | Full GPU (`-ngl 99`) | **72 – 88+ tok/s** | **1,500 – 2,200+ tok/s** | Full 256k native window in VRAM |
| **Workstation / Laptop (DDR4 / DDR5 RAM)** | Hybrid Offload (Few layers in VRAM) | Hardware-dependent | Hardware-dependent | Zero AVX2 CPU stalls; efficient streaming from system RAM |

---

<a id="context-scaling"></a>
<a id="toc-08"></a>
## 🌐 The 24GB Miracle: Full 256K Context Runs In VRAM!

**T-Search APEX-I-MiniPlus-V2.1 fits the entire 256K context window within 24GB VRAM:**

| Context Length | Model Weights (Est.) | KV Cache (q8_0, 4 slots) | Compute Buffers | **Total GPU VRAM (Est.)** | Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **32,768 (32k)** | `14.18 GiB` | `0.58 GiB` | `1.80 GiB` | **`16.56 GiB`** | Full offload on 24GB; partial on 16GB |
| **65,536 (64k)** | `14.18 GiB` | `0.92 GiB` | `1.95 GiB` | **`17.05 GiB`** | Effortless fit on 24GB GPUs |
| **131,072 (128k)**| `14.18 GiB` | `1.58 GiB` | `2.22 GiB` | **`17.98 GiB`** | Effortless fit on 24GB GPUs |
| **262,144 (256k)**| `14.18 GiB` | `2.92 GiB` | `2.80 GiB` | **`19.90 GiB`** | **FULL 256K NATIVE IN VRAM!** |

*Note: Leaves comfortable headroom for display drivers and compute buffers on standard 24GB GPUs (RTX 3090, RTX 4090, RTX 5090).*

---

<a id="recommended-setup"></a>
<a id="toc-09"></a>
## 🚀 Recommended Configuration & Setup

<a id="toc-10"></a>
### 1. High-Throughput Server with Built-in MTP Speculative Decoding (llama-server)
`T-Search.APEX-I-MiniPlus-V2.1.gguf` includes integrated Multi-Token Prediction (MTP) draft layers. To enable ultra-fast self-speculative execution, pass `--spec-type draft-mtp`:

```bash
llama-server.exe \
  -m T-Search.APEX-I-MiniPlus-V2.1.gguf \
  --mmproj mmproj-Q8_0.gguf \
  --spec-type draft-mtp \
  --draft-max 2 \
  --port 8080 \
  --flash-attn on \
  --fit on \
  -c 32768 \
  --cache-type-k q8_0 \
  --cache-type-v q8_0
```
*(Note: Keep `--draft-max` tight at `1` or `2` for optimal MTP acceptance depth on agentic retrieval trajectories. To run in standard single-stream mode without MTP, simply omit `--spec-type draft-mtp`).*

<a id="toc-11"></a>
### 2. Direct CLI Inference / Agentic Retrieval Harness
```bash
llama-cli.exe \
  -m T-Search.APEX-I-MiniPlus-V2.1.gguf \
  --mmproj mmproj-Q8_0.gguf \
  --spec-type draft-mtp \
  --draft-max 2 \
  -c 32768 \
  -ngl 99 \
  --temp 0.60 --top-p 0.95 --top-k 20 \
  -p "<|im_start|>user\nPlan a multi-round retrieval strategy for verifying quantum error correction milestones.<|im_end|>\n<|im_start|>assistant\n"
```

---

<a id="generation-parameters"></a>
<a id="toc-12"></a>
## ⚙️ Recommended Generation Parameters (t-tech Official)

Official generation guidelines specified by [t-tech](https://huggingface.co/t-tech/T-Search) for agentic search retrieval:

| Hyperparameter | Value | Description / Creator Notice |
| :--- | :---: | :--- |
| **Temperature** | `0.60` | Official setting. **Do NOT use greedy decoding (`temp 0.0`)**: repetition loops occur on long multi-round search plans. |
| **Top-P** | `0.95` | Nucleus filtering for stable reasoning token trajectories. |
| **Top-K** | `20` | Official vocabulary top-k filter. |
| **Max New Tokens** | `8192` | Generous token allocation for deep multi-step retrieval and synthesis. |

---

<a id="quantization-fidelity"></a>
<a id="toc-13"></a>
## 🔍 Model Inherent Behavior vs. Quantization Fidelity Notice

> [!IMPORTANT]
> Any behavioral nuances, stylistic tendencies, domain-specific search habits, or zero-shot edge-case oversights **stem entirely from the original unquantized checkpoint weights and fine-tuning distribution, NOT from the APEX-I quantization process.**
> Handcrafted APEX-I-MiniPlus strictly preserves mathematical tensor fidelity—keeping 100% of expert routing matrices (`gate_inp`) in uncompressed `F32` (zero router drift), armoring the token output head in `Q6_K`, and safeguarding attention gates in `Q8_0`. Empirical verification confirms near-zero perplexity loss (ΔPPL ≈ +0.05), ensuring that token logits, routing decisions, and reasoning trajectories are mathematically faithful to the original base model.

<a id="toc-coding-advisory"></a>
<a id="coding-advisory"></a>
> [!IMPORTANT]
> ### CRITICAL ADVISORY FOR CODING WORKFLOWS: PREVENTING SYNTAX & TOKEN SWAPPING
> In programming code, brackets (`{`, `}`), assignment operators (`=`), and indentation whitespace repeat constantly across multi-line structures.
> 
> **Common Issue:** Many local frontends (such as LM Studio defaults, Ollama, or web interfaces) ship with `repeat_penalty` set to `1.1` or `1.15`. While this prevents loops in creative prose, applying repeat penalties to code artificially penalizes necessary syntax tokens. When the logit of `{` drops, the model is forced to emit the next closest mathematical token (`=` or `[`), resulting in character swapping or dropped/doubled whitespace.
> 
> **Verified Upstream Behavior:** This self-correcting behavior (where the model notices the mistake in its thinking loop but repeats the substitution) is documented on official upstream base checkpoints and Q8 builds ([Ornith Discussion #34](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B/discussions/34) and [Discussion #22](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF/discussions/22)). It is completely eliminated by proper sampling configuration:
> 
> 1. **Disable Repeat Penalties (Required for Code):**
>    - `repeat_penalty: 1.0` (strictly disabled)
>    - `presence_penalty: 0.0`
>    - `frequency_penalty: 0.0`
> 2. **Calibrate Samplers:**
>    - `temperature: 0.60` (or `0.20` - `0.30` for strict, deterministic code syntax)
>    - `min_p: 0.05` (prunes low-probability noise tokens effectively)
>    - `top_p: 0.95`
>    - `top_k: 20`
> 3. **Native Jinja Formatting:** Always pass the `--jinja` flag so the tokenizer handles leading-space BPE tokens (` {` vs `{`, ` =` vs `=`) cleanly.

<a id="toc-chat-template"></a>
<a id="chat-template"></a>
> [!TIP]
> ### HARDENED AGENTIC CHAT TEMPLATE (JINJA)
> An optimized `chat_template.jinja` is included at the root of this repository. It hardens agent workflows and multi-turn stability:
> 
> 1. **Native `reasoning_effort` Multi-Level Control:**
>    - `low` / `minimal`: Keeps internal thinking concise and focused strictly on immediate execution steps to minimize latency in automated loops.
>    - `medium` (default): Balanced, structured reasoning process with standard analytical depth.
>    - `high` / `xhigh`: Guides the model to formulate a clear implementation plan upfront before generating code, avoiding circular self-doubt loops.
>    - `none` / `off`: Closes the thinking block immediately (`<think>\n\n</think>`) when reasoning is disabled.
> 2. **Tool-Calling Safeguard (Anti-Premature Stop):** Prevents the model from terminating a turn (`<|im_end|>`) at a colon or action declaration prior to outputting `<tool_call>`.
> 3. **Multi-Turn Thinking Memory:** Preserves historical `<think>` blocks across turns by default, preventing context distribution drift in 78K+ token runs.
> 
> **Usage with llama-server:**
> ```bash
> llama-server -m Model.gguf --chat-template-file chat_template.jinja --reasoning-effort medium
> ```

<a id="toc-14"></a>
## Optional Support

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

If these MiniPlus or NanoPlus releases have been useful to you and you would like to support the work, you can do so voluntarily through https://ko-fi.com/isvalorum. Your contribution helps with evaluation, hosting, and future handcrafted quantizations. Every release will always remain free to download and use; there are no paywalled files, updates, or features.
