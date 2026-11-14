---
base_model: thomsonreuters/Thomson-1.0-Small
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
pipeline_tag: text-generation
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
- apex-i-nanoplus
- nanoplus
- custom-quantization
- unsloth-studio
- moe
- reasoning
- llama.cpp
- qwen35moe
license: apache-2.0
---

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

**Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**

If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

---

# Thomson-1.0-Small APEX-I-NanoPlus GGUF

## Surgical Tensor Quantization Map (Audited from GGUF)

*The exact tensor breakdown below has been verified directly from the compiled binary weights:*

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Preserves near-FP16 token classification; eliminates syntax errors, bracket drops, and hallucinations. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | High-fidelity vocabulary embedding representation. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `post_attention_norm`, `ssm_norm` | 131 | **`F32`** | 100% uncompressed numerical stability across all 40 layers. |
| **Expert Routers** | `blk.*.ffn_gate_inp`, `ffn_gate_inp_shexp` | 80 | **`F32`** | 100% uncompressed routing fidelity across 256 micro-experts; zero router drift. |
| **Attention Gates** | `blk.*.attn_gate.weight` (30 Hybrid Layers) | 30 | **`Q8_0`** | High-precision attention gating across hybrid DeltaNet recurrence layers; eliminates crosstalk. |
| **Shared Foundation Experts** | `blk.*.ffn_{gate,down,up}_shexp` (All 40 Layers) | 120 | **`Q4_K`** | Foundation knowledge backbone active on 100% of tokens; protected in linear Q4_K for fast streaming. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_q/k/v` (10 Anchor Layers) | 30 | **`Q4_K`** | Full quadratic attention anchor checkpoints for deep needle-in-a-haystack retrieval. |
| **Periodic Full Attention** | `blk.{3,7,11,...}.attn_output` (10 Anchor Layers) | 10 | **`Q6_K`** | High-precision attention output projection over deep context. |
| **Recurrent SSM Scales** | `blk.*.ssm_alpha`, `ssm_a`, `ssm_conv1d`, `ssm_dt` | 120 | **`F32`** | Guarded in uncompressed FP32 to prevent DeltaNet recurrent state drift. |
| **Linear Attention & SSM** | `blk.*.attn_qkv`, `ssm_beta`, `ssm_out` | 90 | **`Q4_K`** | Linear AVX2 execution; zero SIMD CPU stalls during system RAM streaming. |
| **Border MoE Down-Proj** | Layers 0–1 & 38–39 (`ffn_down_exps`) | 4 | **`Q3_K`** | Linear SIMD execution optimized for token entry and exit stability. |
| **Border MoE Gate/Up** | Layers 0–1 & 38–39 (`ffn_gate/up_exps`) | 8 | **`IQ3_XXS`** | High-density boundary protection guided by imatrix. |
| **Core MoE Down-Proj** | Layers 2–37 (`ffn_down_exps`) | 36 | **`IQ3_XXS`** | Fortified 3.06 bpw residual stream; preserves core mathematical, coding, and reasoning capacity. |
| **Core MoE Gating** | Layers 2–37 (`ffn_gate_exps`) | 36 | **`IQ2_S`** | High-precision 2.50 bpw SwiGLU gating; eliminates activation noise. |
| **Core MoE Up-Proj** | Layers 2–15 (`ffn_up_exps`) | 14 | **`IQ2_S`** | Enhanced 2.50 bpw precision for sensitive early-intermediate feature extraction. |
| **Core MoE Up-Proj** | Layers 16–37 (`ffn_up_exps`) | 22 | **`IQ2_XXS`** | Extreme 2.06 bpw compression in deep MoE layers to reach exact 12.55 GB envelope. |

*The complete 100% audited tensor list is attached in `tensor-map.tsv` in this repository (733 / 733 tensors).*

---

## Community Compute Fund & Student Support

<a href="https://ko-fi.com/isvalorum"><img src="https://huggingface.co/spaces/IsValorum/MiniPlus-NanoPlus-Requests/resolve/main/assets/dance-gold-ship.gif" alt="Gold Ship dancing" width="128" align="right"></a>

All IsValorum quantizations will always remain completely free and open to the public without paywalls. 

However, cloud GPU compute is expensive and funded entirely out-of-pocket. If you find these handcrafted builds to be of high quality and they benefit your day-to-day workflow, you can support future Day-0 releases on Ko-fi. Every contribution directly funds the cloud compute hours required for new model runs and helps support my university education:

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

*(When supporting on Ko-fi, feel free to leave a note with your Hugging Face handle and the specific model you would like prioritized).*

<div style="clear: both;"></div>
