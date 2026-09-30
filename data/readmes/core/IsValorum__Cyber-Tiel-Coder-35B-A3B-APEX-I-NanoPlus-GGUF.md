---
base_model: peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
pipeline_tag: image-text-to-text
license: mit
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
- cyber-tiel-coder
- tiel-coder
- ornith
- coding
- agentic-coding
- agentic
- swe-bench
- token-efficient
- imatrix
- unsloth-dynamic
- abliterated
- uncensored
---

## <a id="quick-navigation"></a>Quick Navigation Index
1. [Optimization History & Transparency Notice](#toc-01)
2. [Model Specifications](#toc-02)
3. [Inference Quickstart](#toc-03)
4. [1. llama-cli (Console Generation)](#toc-04)
5. [2. llama-server (OpenAI-Compatible API)](#toc-05)
6. [CRITICAL: Coding Syntax & Repeat Penalty Advisory (Preventing Character Swapping)](#toc-coding-advisory)
7. [Hardened Agentic Chat Template & Reasoning Effort](#toc-chat-template)
8. [Optional Support](#toc-06)

# Cyber-Tiel-Coder-35B-A3B APEX-I-NanoPlus GGUF
### *The Next-Generation Frontier MoE · Extreme 12GB Footprint · Fast System RAM Streaming & Massive Context on 16GB VRAM*

> [!NOTE]
> ### 🚀 EXPLORE THE ESTABLISHED 35B MoE MINIPLUS & NANOPLUS LINEUP
> These are complementary APEX-I releases, not alternate downloads of the same model. Each receives the same surgical tensor-by-tensor approach and a design suitable for full or partial system-RAM inference:
>
> - **[Cyber-Tiel-Coder-35B-A3B APEX-I-MiniPlus-V2.1](https://huggingface.co/IsValorum/Cyber-Tiel-Coder-35B-A3B-APEX-I-MiniPlus-V2.1-GGUF)** — specialist uncensored agentic coding MoE tuned for high-speed local development (14.75 GB / Q5–Q6 quality).
> - **[Tiel-Coder-35B-A3B APEX-I-NanoPlus](https://huggingface.co/IsValorum/Tiel-Coder-35B-A3B-APEX-I-NanoPlus-GGUF)** — the approx. 12.55 GB NanoPlus release for repository-scale software engineering.
> - **[Qwen3.6-35B-A3B-MTP APEX-I-NanoPlus](https://huggingface.co/IsValorum/Qwen3.6-35B-A3B-MTP-APEX-I-NanoPlus-GGUF)** — the approx. 13.0 GB NanoPlus pioneer achieving Q4 quality at 2.93 BPW.
> - **[Ornith 1.5 APEX-I-NanoPlus](https://huggingface.co/IsValorum/Ornith-1.5-35B-A3B-APEX-I-NanoPlus-GGUF)** — software-engineering-focused MoE streamlined for ultra-lean memory footprints.
> - **[Occamy-1.0 APEX-I-NanoPlus](https://huggingface.co/IsValorum/Occamy-1.0-APEX-I-NanoPlus-GGUF)** — versatile frontier MoE for deep research and multimodal tasks.

> [!IMPORTANT]
> ### THE DEFINITIVE SPECIFICATION IN THE 11.8–12.0 GB CEILING (STREAMLINED ARCHITECTURE)
> This **APEX-I-NanoPlus** release represents a streamlined, highly optimized configuration for sparse Mixture-of-Experts quantization. The clean model footprint compresses the full 40-layer backbone down to an agile **12.55 GB (11.69 GiB)** footprint, while retaining optional companion files (`mmproj-Q8_0.gguf` and `mtp-Cyber-Tiel-Coder-35B-A3B.gguf`) decoupled in the repository. The WikiText-2 result below measures language-model perplexity; it does not establish SWE-bench coding performance.

> [!TIP]
> ### 🏆 EMPIRICAL BENCHMARK & QUALITY COMPARISON
> 
> | Quantization Specification | File Size (Disk) | Memory Footprint (RAM/VRAM) | Average BPW | WikiText-2 Perplexity | ΔPPL vs. approx. BF16 | Quality Tier Equivalent |
> | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
> | **Unquantized BF16 Base** | approx. 71.05 GB | approx. 66.18 GiB | 16.00 BPW | approx. 7.46 | 0.000 (Reference) | Full Precision Baseline |
> | **[APEX-I-MiniPlus V2.1](https://huggingface.co/IsValorum/Cyber-Tiel-Coder-35B-A3B-APEX-I-MiniPlus-V2.1-GGUF)** | 14.75 GB | 13.74 GiB | 3.43 BPW | 7.5124 ± 0.20729 | +0.0524 (+0.70%) | Q5_K_L tier, bordering Q6_K |
> | **APEX-I-NanoPlus (CURRENT)** | **12.55 GB** | **11.69 GiB** | **approx. 2.93 BPW** | **8.2849 ± 0.23438** | **+0.8249 (+11.06%)** | **Solid Q4_K_M / Q4_K_L Tier** |
> | *Generic Community IQ2_S* | approx. 12.2 GB | approx. 11.4 GiB | 2.56 BPW | > 8.10 (Degraded) | +0.64+ (Syntax Noise) | Unstable / Syntax Spikes |
>
> **Looking for higher precision?** [Cyber-Tiel-Coder-35B-A3B APEX-I-MiniPlus-V2.1](https://huggingface.co/IsValorum/Cyber-Tiel-Coder-35B-A3B-APEX-I-MiniPlus-V2.1-GGUF) offers the full **14.75 GB (3.43 BPW)** release of this Cyber-Tiel-Coder family, delivering Q5_K_L tier (bordering Q6_K) fidelity for agentic coding and local development.
>
> **ARC-Challenge (0-shot, 1,172 questions): approx. 95.69%.**
> - **Q4_K_L Tier in Reasoning & Routing:** 100% uncompressed `F32` routers (`gate_inp`) and a `Q6_K` output head eliminate router drift, matching or exceeding standard `Q4_K_L` baselines on logic benchmarks.
> - **Solid Q4_K_M Tier in Language Modeling:** WikiText-2 perplexity preserves 4-bit distributional fidelity across standard generation in an ultra-lean footprint.

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
| **MiniPlus V2.1 (Current)** | `IQ3_XXS` + `Q3_K` | `Q3_K` (10 layers) | `Q5_K` | `Q4_K` (`q/k/v`) + `Q6_K` (`output`) | `Q8_0` | `Q6_K` | `F32` | 14.75 GB (13.74 GiB) | Maximum fidelity near-lossless Q5/Q6 tier. Fits 24GB GPUs effortlessly. |
| **NanoPlus (NEW)** | **`IQ3_XXS` (down) + `IQ2_S` (gate) + `IQ2_XXS` (up)** | **`Q3_K` (down) + `IQ3_XXS` (gate/up)** | **`Q4_K`** | **`Q4_K` (`q/k/v`) + `Q4_K` (`output`)** | **`Q8_0`** | **`Q6_K`** | **`F32`** | **12.55 GB (11.69 GiB)** | **Streamlined 11.8–12.0 GB tier. Leaves >4 GB free VRAM on 16GB cards for 32k context with zero AVX2 CPU stalls.** |

> [!TIP]
> ### Deployment & System Architecture Guide
> - **Full GPU VRAM Offload (16GB+ VRAM, `-ngl 99`):** Effortless full offload with native 32K–64K context support on 16GB cards (RTX 4080 / RTX 4070 Ti Super), and native 256K context on 24GB workstations (RTX 3090 / 4090 / 5090).
> - **System RAM Streaming Specialist (DDR4/DDR5 & Massive Context):** Specially engineered to run either partially or entirely out of system RAM across large or full context windows. By utilizing linear SIMD-optimized `Q4_K` attention projections and preserving critical down-projections in `IQ3_XXS`, AVX2 CPU dequantization stalls are eliminated.
> 
> Explore our official collection:
> **[APEX-I-NanoPlus Collection](https://huggingface.co/collections/IsValorum/apex-i-nanoplus-6ab41467c988a1b1cb9b83bc)**.

---

<a id="toc-02"></a>
## Model Specifications

| Attribute | Specification |
| :--- | :--- |
| **Architecture** | Hybrid MoE + Linear Attention / DeltaNet SSM |
| **Base Model** | [peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) (derived from [huihui-ai/Huihui-Ornith-1.5-35B-A3B-abliterated](https://huggingface.co/huihui-ai/Huihui-Ornith-1.5-35B-A3B-abliterated)) |
| **Total Parameters** | approx. 35 Billion |
| **Active Parameters** | approx. 3.0 Billion per token |
| **Context Window** | Up to 262,144 tokens (native 256K) |
| **Primary File** | `Cyber-Tiel-Coder-35B-A3B.APEX-I-NanoPlus.gguf` (approx. 12.55 GB) |
| **Vision Projector** | `mmproj-Q8_0.gguf` (Quantized to uncompressed 8-bit precision) |
| **Companion Draft Model** | `mtp-Cyber-Tiel-Coder-35B-A3B.gguf` (Optional speculative decoding acceleration) |

---

<a id="toc-03"></a>
## Inference Quickstart

<a id="toc-04"></a>
### 1. `llama-cli` (Console Generation)
```bash
llama-cli   -m Cyber-Tiel-Coder-35B-A3B.APEX-I-NanoPlus.gguf   --mmproj mmproj-Q8_0.gguf   --jinja   -p "<|im_start|>user\nRefactor this Python asyncio loop to handle task cancellations gracefully.<|im_end|>\n<|im_start|>assistant\n"   -ngl 99 -c 8192 --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0
```

<a id="toc-05"></a>
### 2. `llama-server` (OpenAI-Compatible API with MTP Speculative Decoding)
```bash
llama-server   -m Cyber-Tiel-Coder-35B-A3B.APEX-I-NanoPlus.gguf   --mmproj mmproj-Q8_0.gguf   -md mtp-Cyber-Tiel-Coder-35B-A3B.gguf   --spec-type draft-mtp   --jinja   -ngl 99   --ctx-size 262144   --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0   --port 8080
```

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

<a id="toc-06"></a>
## Optional Support

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

If these MiniPlus or NanoPlus releases have been useful to you and you would like to support the work, you can do so voluntarily through https://ko-fi.com/isvalorum. Your contribution helps with evaluation, hosting, and future handcrafted quantizations. Every release will always remain free to download and use; there are no paywalled files, updates, or features.
