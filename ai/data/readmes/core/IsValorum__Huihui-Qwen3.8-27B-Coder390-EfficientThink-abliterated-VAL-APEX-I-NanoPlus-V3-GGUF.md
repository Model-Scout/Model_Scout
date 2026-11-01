---
base_model: huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
license: apache-2.0
language:
- en
- zh
- es
- fr
- de
- pt
- it
- ja
- ko
tags:
- gguf
- llama.cpp
- quantized
- quantization
- val-apex-i
- apex
- apex-quant
- apex-i-nanoplus
- nanoplus
- qwen
- qwen3.8
- coder
- coding
- agentic
- reasoning
- efficient-thinking
- abliterated
- uncensored
- imatrix
pipeline_tag: text-generation
---

# Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated VAL-APEX-I NanoPlus V3 GGUF

>
> **The authentic Coder390 + EfficientThink + Abliterated 27B release:**
> - Based on the upgraded Coder390 fine-tune (trained with multi-model SFT on Opus 5.5, GPT-6 Astra, Grok 4.7, DeepSeek V4 Pro, and RLOO).
> - Features **EfficientThink** alignment, drastically cutting down thinking bloat and repetitive reasoning overhead while preserving rigorous problem-solving depth.
> - Fully abliterated by Huihui-AI across layers 2 to 52, eliminating false-positive refusals on sensitive coding, cybersecurity, and reverse-engineering prompts.
> - Handcrafted tensor-by-tensor allocation via the canonical VAL-APEX-I V3 standard with 866 verified tensors documented in the [Tensor Map](#toc-04) and certified `tensor-map.tsv` file.

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

**Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**

If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

### *The Uncensored 27B Frontier Reasoning & Coding Engine · Coder390 SFT + RLOO · EfficientThink Low Overhead · Abliterated Base · Native 256K Context*

Official **VAL-APEX-I** quantization of **[huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated)**.

VAL-APEX-I stands for:
**Vector-calibrated Asymmetric Layer-wise Outlier-preserving Recurrent-aware Unified Matrix-quantization**

> [!NOTE]
> ### EXPLORE THE COMPANION EDITIONS
> Choose your target quantization profile:
>
> - **[Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated — MiniPlus V3](https://huggingface.co/IsValorum/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-VAL-APEX-I-MiniPlus-V3-GGUF)** — 14.16 GB (Highest precision tier with Q6_K attention & outputs).
> - **[Qwen3.8 27B Base — MiniPlus V3](https://huggingface.co/IsValorum/Qwen3.8-27B-VAL-APEX-I-MiniPlus-V3-GGUF)** — 14.16 GB.
> - **[Qwen3.8 27B Base — NanoPlus V3](https://huggingface.co/IsValorum/Qwen3.8-27B-VAL-APEX-I-NanoPlus-V3-GGUF)** — 12.18 GB.
> - **[Swift-1.5 Qwen3.8 27B Uncensored MTP — MiniPlus V3](https://huggingface.co/IsValorum/Swift-1.5-Qwen3.8-27B-Uncensored-MTP-VAL-APEX-I-MiniPlus-V3-GGUF)** — 14.16 GB.
> - **[Swift-1.5 Qwen3.8 27B Uncensored MTP — NanoPlus V3](https://huggingface.co/IsValorum/Swift-1.5-Qwen3.8-27B-Uncensored-MTP-VAL-APEX-I-NanoPlus-V3-GGUF)** — 12.18 GB.
>
> Collections: **[MiniPlus Abliterated 27B](https://huggingface.co/collections/IsValorum/val-apex-miniplus-abliterated-27b-6acfec541ee5628d2632c663)** · **[MiniPlus Standard 27B](https://huggingface.co/collections/IsValorum/val-apex-miniplus-standard-27b-6acfec54ca4ce4cf5cd5bdb6)** · **[NanoPlus Abliterated 27B](https://huggingface.co/collections/IsValorum/val-apex-nanoplus-abliterated-27b-6acfec5503f6e74218f71f64)** · **[NanoPlus Standard 27B](https://huggingface.co/collections/IsValorum/val-apex-nanoplus-standard-27b-6acfec55c1c99e2a23ebbd9b)**

> [!IMPORTANT]
> ### THE DEFINITIVE SPECIFICATION IN THE 11 to 12 GB CEILING
> This **VAL-APEX-I NanoPlus V3** release is **12.18 GB**, with **3.57 whole-file BPW** and **866 audited tensors**. It incorporates an elevated 3-bit floor across all MLP feed-forward blocks, avoiding destructive 2-bit sub-allocations.

---

## <a id="quick-navigation"></a>Quick Navigation Index
1. [Quantization Metrics & Tensor Map](#toc-comparison)
2. [Independent Community Benchmarks (NanoBench v0.4.0)](#toc-nanobench)
3. [Model Files & Technical Specifications](#toc-04)
4. [Native Context & Runtime Memory](#toc-06)
5. [Recommended Configuration & Setup](#toc-07)
6. [Recommended Generation Parameters](#toc-08)
7. [CRITICAL: Coding Syntax & Repeat Penalty Advisory (Preventing Character Swapping)](#toc-coding-advisory)
8. [Hardened Agentic Chat Template & Reasoning Effort](#toc-chat-template)
9. [Community Compute Fund & Student Support](#toc-09)

---

<a id="toc-comparison"></a>
<a id="toc-01"></a>
<a id="toc-02"></a>
<a id="toc-03"></a>
<a id="toc-05"></a>
## 1. Quantization Metrics

### Size & Quality Metrics

| Edition / Quantization | File Size | Memory Footprint (Weights) | Whole-file BPW | Total Audited Tensors |
| :--- | :---: | :---: | :---: | :---: |
| **[Huihui Coder390 EfficientThink — MiniPlus V3](https://huggingface.co/IsValorum/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-VAL-APEX-I-MiniPlus-V3-GGUF)** | **14.16 GB** | 13.19 GiB | **4.15** | **866** |
| **Huihui Coder390 EfficientThink — NanoPlus V3 (This Release)** | **12.18 GB** | 11.35 GiB | **3.57** | **866** |

> [!NOTE]
> **Independent Hardware & Compute Transparency:**
> Generating multi-million token calibration matrices and running certified evaluations on dense hybrid architectures requires dedicated high-end cloud nodes funded 100% out-of-pocket. If you rely on these MiniPlus/NanoPlus V3 builds for your daily coding workloads, contributions to the **[IsValorum Compute Fund on Ko-fi](https://ko-fi.com/isvalorum)** directly sponsor the GPU hours required for future Day-0 handcrafted quantizations.

<a id="toc-nanobench"></a>
### Independent Community Benchmarks (NanoBench v0.4.0)

Independent multi-harness empirical evaluation conducted by community member **[@userr99](https://huggingface.co/userr99)** on a dedicated local workstation (24 GB VRAM / 64 GB RAM using `llama.cpp`). Evaluated across the 12-task autonomous coding and agentic suite on [NanoBench v0.4.0](https://shortbench.vercel.app/) ([public discussion thread & test logs](https://huggingface.co/IsValorum/Huihui-Qwen3.8-27B-Abliterated-VAL-APEX-I-NanoPlus-V3-GGUF/discussions/2)):

| Test Harness | Total Score | Solved Tasks | Agentic (Tool Use) | Coding (Implementation) | Systems (Integrity) | Avg. Runtime |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Oh My Pi (OMP 18.7)** | **96.7 / 100** | 10 / 12 | **100 / 100** | **100 / 100** | 86.7 / 100 | aprox. 1h 47m |
| **Hermes Agent (v0.21.5)** | **95.4 / 100** | 9 / 12 | **100 / 100** | 97.0 / 100 | 86.7 / 100 | aprox. 1h 47m |
| **DeepSeek Harness (0.2.0-rc.2)** | **90.4 / 100** | 9 / 12 | **100 / 100** | 97.0 / 100 | 66.7 / 100 | aprox. 1h 47m |

**Key Architectural Insights:**
- **Zero Tool-Calling Degradation:** Achieved a unanimous **100/100 in Agentic tasks** across all three harnesses, confirming that protecting `output.weight` in `Q5_K` and DeltaNet recurrent memory states (`ssm_a` in `F32`, `ssm_beta` in `Q8_0`) prevents JSON schema rejections and state drift over multi-step workflows.
- **Universal Harness Compatibility:** Surpassed the 90+ score barrier across all three test harnesses without entering infinite retry loops or syntax divergence.
- **Verified Execution Validity:** In the DeepSeek run, both partial Systems results (`systems-02` scoring 60 and `systems-03` scoring 40, alongside `systems-01` at 100) were formally marked **VALID** by the runner verifier, confirming full tool-calling integrity and zero environment or syntax crashes.

---

### Tensor Precision Map

| Component | MiniPlus V3 | NanoPlus V3 (This Release) | GSQ-RCO IQ3_S |
| :--- | :--- | :--- | :--- |
| Output head | `Q6_K` x1 | `Q5_K` x1 | `Q4_K` x1 |
| Token embeddings | `Q4_K` x1 | `Q3_K` x1 | `IQ2_S` x1 |
| Normalizations | `F32` x161 | `F32` x161 | `F32` x161 |
| SSM A (`ssm_a`) | `F32` x48 | `F32` x48 | `F32` x48 |
| SSM convolution (`ssm_conv1d`) | `F32` x48 | `F32` x48 | `F32` x48 |
| SSM time-step bias (`ssm_dt`) | `F32` x48 | `F32` x48 | `F32` x48 |
| SSM norm (`ssm_norm`) | `F32` x48 | `F32` x48 | `F32` x48 |
| Attention gates (`attn_gate`) | `Q4_0` x1<br>`Q4_K` x47 | `Q4_0` x1<br>`Q4_K` x47 | `IQ2_S` x2<br>`IQ3_S` x18<br>`IQ3_XXS` x9<br>`IQ4_XS` x12<br>`Q2_K` x4<br>`Q4_K` x3 |
| Linear QKV (`attn_qkv`) | `Q4_0` x1<br>`Q4_K` x47 | `Q3_K` x47<br>`Q4_0` x1 | `IQ2_XS` x1<br>`IQ2_XXS` x1<br>`IQ3_S` x22<br>`IQ3_XXS` x13<br>`IQ4_XS` x9<br>`Q2_K` x1<br>`Q4_K` x1 |
| SSM alpha (`ssm_alpha`) | `F32` x48 | `F32` x48 | `BF16` x48 |
| SSM beta (`ssm_beta`) | `Q4_0` x1<br>`Q8_0` x47 | `Q4_0` x1<br>`Q8_0` x47 | `BF16` x48 |
| SSM output (`ssm_out`) | `Q4_0` x1<br>`Q5_K` x47 | `Q4_0` x1<br>`Q4_K` x47 | `IQ3_S` x22<br>`IQ3_XXS` x4<br>`IQ4_XS` x16<br>`Q4_K` x6 |
| Full attention Q (`attn_q`) | `Q4_K` x16 | `Q3_K` x16 | `IQ2_XXS` x1<br>`IQ3_S` x3<br>`IQ3_XXS` x3<br>`IQ4_XS` x2<br>`Q2_K` x6<br>`Q4_K` x1 |
| Full attention K (`attn_k`) | `Q5_K` x16 | `Q4_K` x16 | `IQ2_S` x1<br>`IQ3_S` x1<br>`IQ3_XXS` x1<br>`IQ4_XS` x8<br>`Q4_K` x5 |
| Full attention V (`attn_v`) | `Q6_K` x16 | `Q5_K` x16 | `IQ3_S` x6<br>`IQ3_XXS` x1<br>`IQ4_XS` x1<br>`Q4_K` x8 |
| Full attention output (`attn_output`) | `Q6_K` x16 | `Q5_K` x16 | `IQ3_S` x10<br>`IQ3_XXS` x1<br>`IQ4_XS` x2<br>`Q4_K` x3 |
| MLP down (`ffn_down`) | `IQ4_XS` x64 | `IQ3_XXS` x48<br>`IQ4_XS` x16 | `IQ2_S` x4<br>`IQ2_XS` x3<br>`IQ3_S` x22<br>`IQ3_XXS` x7<br>`IQ4_XS` x21<br>`Q2_K` x1<br>`Q4_K` x6 |
| MLP gate (`ffn_gate`) | `IQ3_S` x32<br>`IQ3_XXS` x32 | `IQ3_XXS` x64 | `IQ1_M` x1<br>`IQ2_S` x4<br>`IQ2_XS` x4<br>`IQ2_XXS` x1<br>`IQ3_S` x15<br>`IQ3_XXS` x21<br>`IQ4_XS` x15<br>`Q2_K` x1<br>`Q4_K` x2 |
| MLP up (`ffn_up`) | `IQ3_S` x32<br>`IQ3_XXS` x32 | `IQ3_XXS` x64 | `IQ2_S` x5<br>`IQ2_XS` x1<br>`IQ2_XXS` x2<br>`IQ3_S` x25<br>`IQ3_XXS` x18<br>`IQ4_XS` x10<br>`Q4_K` x3 |
| Additional MTP head (`blk.64.*`) | `F32` x7<br>`Q4_0` x6<br>`Q4_1` x1<br>`Q6_K` x1 | `F32` x7<br>`Q4_0` x6<br>`Q4_1` x1<br>`Q5_K` x1 | - |

x denotes tensor counts. All columns reflect exact GGUF tensor headers verified in `tensor-map.tsv`. Normalizations exclude separately listed SSM norms.

The model contains **866 audited tensors**: **851 main-model tensors** plus **15 MTP tensors**. The architecture is a dense hybrid with **64 layers: 48 Gated DeltaNet linear-attention layers and 16 periodic full-attention layers**.

[Complete tensor-by-tensor audit: names, formats, shapes and parameter counts](./tensor-map.tsv).

---

<a id="toc-04"></a>
## 2. Model Files & Technical Specifications

| File Name | File Size | Weight file size | BPW | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated.VAL-APEX-I-NanoPlus-V3.gguf`** | **12.18 GB (11.35 GiB)** | 11.35 GiB | **3.57 BPW** | Uncensored Coder390 frontier reasoning, compact 3-bit floor, and dense hybrid architecture |
| **`mmproj-model-Q8_0.gguf`** | **0.63 GB (600 MiB)** | 600 MiB | **10.93 BPW** | Companion multimodal vision projection adapter in Q8_0 precision |

- **Base Model:** [huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated) (Abliterated fine-tune of nerkyor's Coder390 SFT + RLOO + EfficientThink checkpoint)
- **Parameters:** 27B total dense hybrid
- **Architecture:** 64 main hybrid layers (48 Gated DeltaNet SSM linear attention layers + 16 periodic full quadratic attention layers)
- **Context Length:** 262,144 tokens (native 256K)
- **Quantization Standard:** VAL-APEX-I NanoPlus V3 calibrated against mradermacher's certified importance matrix (`imatrix.gguf`)
- **Abliteration Status:** True directional weight orthogonalization across layers 2-52, removing refusal vectors while maintaining full analytical capability.

---

<a id="toc-06"></a>
## 3. Native Context & Runtime Memory

The model supports a native context window of 262,144 tokens. Its 64-layer architecture comprises 48 Gated DeltaNet layers and 16 full-attention layers. Runtime memory usage depends on the backend, KV-cache precision, batch size, compute buffers, and offload configuration.

---

<a id="toc-07"></a>
## 4. Recommended Configuration & Setup

### llama.cpp Server (OpenAI-Compatible API)

```bash
llama-server \
  -m Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated.VAL-APEX-I-NanoPlus-V3.gguf \
  --jinja \
  -ngl 99 \
  -c 32768 \
  --host 0.0.0.0 \
  --port 8080
```

### llama.cpp CLI

```bash
llama-cli \
  -m Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated.VAL-APEX-I-NanoPlus-V3.gguf \
  --jinja \
  -ngl 99 \
  -c 32768 \
  -p "<|im_start|>system\nYou are an expert autonomous software engineer.<|im_end|>\n<|im_start|>user\nWrite an optimized concurrent worker pool in Go with backpressure handling.<|im_end|>\n<|im_start|>assistant\n<think>\n"
```

### LM Studio / Ollama
1. Import the `.gguf` file directly into your local library.
2. Ensure GPU acceleration is set to Maximum / 100% offload.
3. Set Context Length to `32768`.
4. Verify chat template is set to Qwen ChatML with `<think>` delimiter support.

---

<a id="toc-08"></a>
## 5. Recommended Generation Parameters

| Hyperparameter | Value | Description |
| :--- | :---: | :--- |
| **Temperature** | `0.60` | Recommended default for analytical reasoning and coding (use `1.0` for creative prose). |
| **Top-P** | `0.95` | Nucleus sampling parameter. |
| **Top-K** | `20` | Top-k vocabulary filter. |
| **Min-P** | `0.05` | Prunes low-probability noise tokens effectively. |
| **Repetition Penalty** | `1.00` | Strictly disabled for code syntax; prevents character swapping. |
| **Template Engine** | `--jinja` | Recommended official Jinja chat template flag. |
| **Context Size** | `32768` | 32K default (scalable to 256K). |

---

<a id="toc-coding-advisory"></a>
## 6. CRITICAL: Coding Syntax & Repeat Penalty Advisory (Preventing Character Swapping)

> [!IMPORTANT]
> ### PREVENTING SYNTAX & TOKEN SWAPPING IN CODE WORKFLOWS
> In programming code, brackets (`{`, `}`), assignment operators (`=`), and indentation whitespace repeat constantly across multi-line structures.
> 
> **Common Issue:** Many local frontends (such as LM Studio defaults, Ollama, or web interfaces) ship with `repeat_penalty` set to `1.1` or `1.15`. While this prevents loops in creative prose, applying repeat penalties to code artificially penalizes necessary syntax tokens. When the logit of `{` drops, the model is forced to emit the next closest mathematical token (`=` or `[`), resulting in character swapping or dropped/doubled whitespace.
> 
> **Eliminating Character Swapping:**
> 1. **Disable Repeat Penalties (Required for Code):**
>    - `repeat_penalty: 1.0` (strictly disabled)
>    - `presence_penalty: 0.0`
>    - `frequency_penalty: 0.0`
> 2. **Use Min-P Filtering:**
>    - Set `min_p: 0.05` with `temperature: 0.6`. This eliminates low-probability hallucinations without distorting syntax distribution.

---

<a id="toc-chat-template"></a>
## 7. Hardened Agentic Chat Template & Reasoning Effort

The repository includes the official, syntax-verified `chat_template.jinja` compatible with `llama.cpp` (`llama-server`), `vLLM`, and `SGLang`.

### Reasoning Effort Guidance
You can control the internal reasoning budget by passing `reasoning_effort` in your generation payload:
* `"low"` / `"minimal"`: Instructs the model to keep internal thought chains brief and proceed directly to code execution.
* `"medium"`: Standard balanced analytical depth.
* `"high"` / `"xhigh"`: Exhaustive, multi-step edge-case exploration and systematic planning.

---

<a id="toc-09"></a>
## 8. Community Compute Fund & Student Support

Creating custom multi-tensor precision recipes, running multi-million token importance matrix sweeps, and conducting independent multi-harness benchmarks requires dedicated high-VRAM cloud instances funded 100% out-of-pocket.

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

If these quantizations are valuable to your local software development, research, or agentic pipelines, your support on **[Ko-fi](https://ko-fi.com/isvalorum)** makes a direct difference:
* Sponsoring cloud compute time for upcoming model architectures.
* Maintaining zero-compromise Day-0 releases for the open-source community.
* Directly supporting my engineering university studies.

Thank you to everyone in the community who tests, reports feedback, and supports this work!
