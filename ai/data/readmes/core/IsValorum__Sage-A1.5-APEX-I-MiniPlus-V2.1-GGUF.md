---
base_model: InternScience/Sage-A1.5
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
- apex-i-miniplus
- v2.1
- custom-quantization
- unsloth-studio
- qwen35moe
- qwen3_5_moe
- moe
- reasoning
- science
- multimodal
---

## Run it in V-Agent

[V-Agent](https://github.com/IsValorum/V-Agent) is a free, open-source desktop agent for Windows, made by the author of these quants. It runs this model locally, with tools and clear permissions.

- **Native engines:** **llama.cpp** (CUDA, Vulkan or CPU), **Strata** and **Strata Rust**, installed from their official releases and matched to your hardware.
- **Built for these quants:** APEX files get their chat template from the official repo, and each quant shows whether it fits your GPU.
- **Real tools, safely:** files, web search, a browser and MCP servers, with each chat in its own isolated folder and approvals for every action.
- **Private:** no account, no telemetry; everything runs on your PC.

1. [Download V-Agent](https://github.com/IsValorum/V-Agent/releases/latest) and install it (Windows 10/11, x64).
2. Open **Models**, search `Sage-A1.5-APEX-I-MiniPlus-V2.1-GGUF`, and pick the file marked **Fits on GPU**.
3. V-Agent downloads it with SHA-256 verification and loads it with this model's chat template.


## Quick Navigation Index

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

**Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**

If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

1. [Model Overview & Technical Specifications](#model-overview)
2. [Empirical Importance Matrix Calibration](#empirical-imatrix)
3. [Bundled Multimodal Vision Projector](#vision-projector)
4. [Surgical Tensor Quantization Map](#surgical-map)
5. [Recommended Server & Inference Configuration](#server-config)
6. [Integrated MTP Speculative Decoding](#mtp-speculative)
7. [Community Compute Fund & Student Support](#support)

---

## <a id="model-overview"></a>1. Model Overview & Technical Specifications

This repository provides **Sage-A1.5 APEX-I-MiniPlus V2.1**, a surgical high-fidelity quantization of `InternScience/Sage-A1.5`.

The architecture comprises 40 hybrid layers (linear attention / DeltaNet recurrence interleaved with periodic quadratic attention anchors every 4 layers), 256 routed micro-experts per layer with top-k=8 activation, and an integrated speculative Multi-Token Prediction (MTP) block in `blk.40`, totaling exactly 753 tensors.

MiniPlus V2.1 is engineered for uncompromising reasoning, coding, and mathematical precision, protecting critical attention paths, routing matrices, and shared foundation experts while compressing routed micro-experts with precision guided by an empirical Importance Matrix.

### Key Characteristics

- **Base Model**: `InternScience/Sage-A1.5`
- **Architecture**: `qwen35moe` (Hybrid Recurrent + Periodic Full Attention MoE + Integrated MTP)
- **Total Tensors**: 753 (733 main model layers + 20 integrated MTP tensors)
- **Quantization Profile**: APEX-I-MiniPlus V2.1
- **Calibration Corpus**: 1,001,472 tokens (VAL-1M multi-domain corpus)
- **MoE Expert Coverage**: 100.0% (30,720 / 30,720 expert projection matrices observed, 0 unobserved)

---

## <a id="empirical-imatrix"></a>2. Empirical Importance Matrix Calibration

Quantization uses the official empirical Importance Matrix `Sage-A1.5-VAL-1M-I-Matrix.GGUF` from [`IsValorum/Sage-A1.5-VAL-1M-I-Matrix-GGUF`](https://huggingface.co/IsValorum/Sage-A1.5-VAL-1M-I-Matrix-GGUF).

### Calibration Parameters

- **Hardware**: Dedicated NVIDIA A100 SXM4 80GB GPU
- **Token Volume**: 1,001,472 tokens across 489 sequential chunks (chunk size 2048)
- **Composition**: Code (35.0%), Reasoning & Mathematics (25.0%), Multi-Domain Prose & Natural Languages (25.0%), Tool Use & Structured JSON (15.0%)
- **Natural Language Diversity**: English (134,960 tok), Spanish (97,146 tok), Mandarin Chinese (96,322 tok), French (77,578 tok), German (73,636 tok), Russian (71,940 tok), Japanese (70,894 tok), Portuguese (69,576 tok), Arabic (69,566 tok), Italian (69,456 tok), Korean (69,444 tok)
- **Programming Languages**: Python, JavaScript, TypeScript, C++, Rust, Go, Java, Bash, SQL, JSON Schema
- **MoE Coverage Metric**: 100.0% expert activation across all 40 layers and 256 micro-experts

---

## <a id="vision-projector"></a>3. Bundled Multimodal Vision Projector

Sage-A1.5 features multimodal visual reasoning capabilities. For visual inference, the high-precision multimodal projector `Sage-A1.5-mmproj.gguf` is bundled directly in this repository.

When launching `llama-server` or CLI tools, include `--mmproj Sage-A1.5-mmproj.gguf` to enable visual inputs.

---

## <a id="surgical-map"></a>4. Surgical Tensor Quantization Map

The exact tensor breakdown below has been verified directly from the compiled binary weights:

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Preserves near-FP16 token classification; eliminates syntax errors and bracket drops. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | High-fidelity vocabulary embedding representation. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `post_attention_norm`, `ssm_norm` | 131 | **`F32`** | 100% uncompressed numerical stability across all 40 layers. |
| **Expert Routers** | `blk.*.ffn_gate_inp`, `ffn_gate_inp_shexp` | 80 | **`F32`** | 100% uncompressed routing fidelity across 256 micro-experts; zero router drift. |
| **Attention Gates** | `blk.*.attn_gate.weight` (30 Hybrid Layers) | 30 | **`Q8_0`** | High-precision attention gating across hybrid DeltaNet recurrence layers; eliminates crosstalk. |
| **Shared Foundation Experts** | `blk.*.ffn_{gate,down,up}_shexp` (All 40 Layers) | 120 | **`Q5_K`** | Foundation knowledge backbone active on 100% of tokens; protected in high-grade Q5_K. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_q/k/v` (10 Anchor Layers) | 30 | **`Q4_K`** | Full quadratic attention anchor checkpoints for deep needle-in-a-haystack retrieval. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_output` (10 Anchor Layers) | 10 | **`Q6_K`** | High-precision attention output projection over deep context. |
| **Recurrent SSM Scales** | `blk.*.ssm_alpha`, `ssm_a`, `ssm_conv1d`, `ssm_dt` | 120 | **`F32`** | Guarded in uncompressed FP32 to prevent DeltaNet recurrent state drift. |
| **Linear Attention & SSM** | `blk.*.attn_qkv`, `ssm_beta`, `ssm_out` | 90 | **`Q3_K`** | Fast linear attention execution; balanced memory bandwidth. |
| **Border MoE Experts** | Layers 0–9 & 30–39 (`ffn_{gate,down,up}_exps`) | 60 | **`Q3_K`** | Edge layer protection for token entry, context establishment, and output convergence. |
| **Core MoE Experts** | Layers 10–29 (`ffn_{gate,down,up}_exps`) | 60 | **`IQ3_XXS`** | High-density 3.06 bpw matrix compression guided by empirical I-Matrix. |
| **Integrated MTP Block** | `blk.40.attn_output` (Speculative Output) | 1 | **`Q6_K`** | High-precision output for speculative draft token validation. |
| **Integrated MTP Attention** | `blk.40.attn_q/k/v`, `nextn.eh_proj` | 4 | **`Q4_K`** | Guarded hidden projection and attention matrices. |
| **Integrated MTP Shared** | `blk.40.ffn_{gate,down,up}_shexp` | 3 | **`Q5_K`** | Protected shared expert for speculative draft generation. |
| **Integrated MTP Experts** | `blk.40.ffn_{gate,down,up}_exps` | 3 | **`Q4_0`** | Linear quantization for fast speculative forward passes. |
| **Integrated MTP Norms** | `blk.40.*_norm`, `nextn.*_norm`, `blk.40.ffn_gate_inp*` | 9 | **`F32`** | 100% uncompressed numerical stability in speculative routing and RMSNorms. |

The complete 100% audited tensor list is attached in `tensor-map.tsv` in this repository (753 / 753 tensors).

---

## <a id="server-config"></a>5. Recommended Server & Inference Configuration

Launch `llama-server` with the following recommended parameters:

```bash
llama-server \
  -m Sage-A1.5.APEX-I-MiniPlus-V2.1.gguf \
  --mmproj Sage-A1.5-mmproj.gguf \
  -c 32768 \
  -ngl 99 \
  --threads 16 \
  --port 8080
```

### Recommended Generation Parameters

- **Temperature**: 0.6 - 0.7
- **Top-P**: 0.95
- **Min-P**: 0.05
- **Repeat Penalty**: 1.05

---

## <a id="mtp-speculative"></a>6. Integrated MTP Speculative Decoding

Sage-A1.5 incorporates a native Multi-Token Prediction (MTP) block stored directly in `blk.40`. This enables speculative self-decoding without requiring an external draft model:

```bash
llama-server \
  -m Sage-A1.5.APEX-I-MiniPlus-V2.1.gguf \
  --draft-max 2 \
  -c 32768 \
  -ngl 99
```

---

## <a id="support"></a>7. Community Compute Fund & Student Support

All IsValorum quantizations will always remain completely free and open to the public without paywalls.

However, cloud GPU compute is expensive and funded entirely out-of-pocket. If you find these handcrafted builds to be of high quality and they benefit your day-to-day workflow, consider supporting future releases on Ko-fi. Every contribution directly funds the cloud compute hours required for new model runs and helps support my university education:

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

*(When supporting on Ko-fi, feel free to leave a note with your Hugging Face handle and the specific model you would like prioritized).*
