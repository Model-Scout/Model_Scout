---
base_model: ajgazin/Swift-1.5-Qwen3.8-27B-Uncensored-MTP
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
license: apache-2.0
language:
- en
- fr
- es
- de
- zh
- ru
- ja
- ko
tags:
- gguf
- llama.cpp
- quantized
- val-apex-i
- nanoplus-v3
- unsloth-studio
- qwen
- qwen3.8
- qwen38
- uncensored
- abliterated
- speculative-decoding
- mtp
- vision
- multimodal
- imatrix
- reasoning
- v3
pipeline_tag: text-generation
---

# Swift-1.5-Qwen3.8-27B-Uncensored-MTP VAL-APEX-I NanoPlus V3 GGUF

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/isvalorum)

*Independently computed on an NVIDIA RTX PRO 6000 Blackwell Server Edition GPU. If this handcrafted release saves you VRAM and runs faster on your GPU, consider [fueling the community compute fund on Ko-fi](https://ko-fi.com/isvalorum).*

### *Uncensored Frontier 27B Dense Hybrid Reasoning Model with Intact Vision, Multilingual Syntax Preservation, and Native MTP Self-Speculation*

Official **VAL-APEX-I NanoPlus V3** quantization of **[ajgazin/Swift-1.5-Qwen3.8-27B-Uncensored-MTP](https://huggingface.co/ajgazin/Swift-1.5-Qwen3.8-27B-Uncensored-MTP)**. This edition quantizes the uncensored foundation model built on UkisAI's Swift-1.5 reasoning fine-tune of Qwen3.8-27B with the official canonical V3 recipe (strictly enforcing `IQ4_XS` and protecting attention/recurrent matrices).

- **Multilingual Source Model:** Preserves the source model's multilingual tokenizer and native chat template.
- **Native MTP Speculative Head Included:** Features the built-in Multi-Token Prediction auxiliary head (`blk.64.*`, 15 tensors), for MTP speculative decoding in compatible backends without an external draft model.
- **Multimodal Optical Vision:** Retains the high-precision vision encoder (`mmproj-Q8_0.gguf`) for visual and document reasoning.
- **ISTA-DASLab Calibrated:** Quantized with the official ISTA-DASLab importance matrix (`imatrix-qwen3.8-27b.gguf`) computed across diverse tokens to safeguard critical recurrent and projection weights.

VAL-APEX-I stands for:
**Vector-calibrated Asymmetric Layer-wise Outlier-preserving Recurrent-aware Unified Matrix-quantization**

> [!NOTE]
> ### EXPLORE THE QWEN3.8 27B VAL-APEX-I EDITIONS
> Choose a model variant and quantization profile:
>
> - **[Qwen3.8 27B — MiniPlus V3](https://huggingface.co/IsValorum/Qwen3.8-27B-VAL-APEX-I-MiniPlus-V3-GGUF)** — 14.16 GB.
> - **[Qwen3.8 27B — NanoPlus V3](https://huggingface.co/IsValorum/Qwen3.8-27B-VAL-APEX-I-NanoPlus-V3-GGUF)** — 12.18 GB.
> - **[Swift-1.5 Qwen3.8 27B Uncensored MTP — MiniPlus V3](https://huggingface.co/IsValorum/Swift-1.5-Qwen3.8-27B-Uncensored-MTP-VAL-APEX-I-MiniPlus-V3-GGUF)** — 14.16 GB.
>
> **[VAL-APEX-I collection](https://huggingface.co/collections/IsValorum/val-apex-i-6ac563d1784a04a1bb177f47)** · **[MiniPlus collection](https://huggingface.co/collections/IsValorum/apex-i-miniplus-v21-current-6aac8d4766a28a024e8bb104)** · **[NanoPlus collection](https://huggingface.co/collections/IsValorum/apex-i-nanoplus-6ab41467c988a1b1cb9b83bc)**

---

## 1. Quantization Metrics

### Size & Quality Metrics

| Edition / quantization | File size | Whole-file BPW | WikiText-2 PPL |
| :--- | :--- | :--- | :--- |
| **Swift-1.5 Qwen3.8 27B Uncensored MTP NanoPlus V3 (this release)** | 12.18 GB (11.35 GiB) | 3.57 | **6.2593** |

This NanoPlus edition was evaluated on WikiText-2 under the same conditions as its previous recipe, as confirmed by the release maintainer. Its reported PPL changed from 6.9102 to 6.2593 (9.42% lower). The current evaluation uses `llama-perplexity` with context 512, batch 512, four chunks and GPU offload (`-ngl 99`), from llama.cpp build 11512 (`a11f57ba9`).

Whole-file BPW is calculated from the complete GGUF file size and its 27,320,697,856 stored parameters, including MTP.




Evaluation runs: [current canonical V3 job](https://huggingface.co/jobs/IsValorum/6ac97502095c57808930b6b1) · [previous recipe job](https://huggingface.co/jobs/IsValorum/6ac9202ffee2c9007017aab3).

### Tensor Precision Map

| Component | MiniPlus V3 | NanoPlus V3 | GSQ-RCO IQ3_S |
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

Both Swift/Base/Huihui files contain **866 audited tensors**: **851 main-model tensors** plus **15 MTP tensors**. The main model is a dense hybrid architecture with **64 layers: 48 Gated DeltaNet linear-attention layers and 16 full-attention layers**. The additional `blk.64.*` block is the integrated MTP head.

**V3 architectural allocation:** NanoPlus V3 features an elevated 3-bit floor across all SwiGLU MLP blocks (`ffn_gate` and `ffn_up` set uniformly to `IQ3_XXS` across all 64 layers; `ffn_down` uses `IQ4_XS` in outer layers 0-7 / 56-63 and `IQ3_XXS` in core layers 8-55). Output head (`output.weight`) is calibrated to `Q5_K` (5.50 bpw) to maximize token throughput and preserve dynamic range, entirely eliminating the linguistic decay in non-English contexts associated with 2-bit sub-allocations.

**Actual layer-0 formats:** `blk.0.attn_gate.weight`, `blk.0.attn_qkv.weight`, `blk.0.ssm_beta.weight` and `blk.0.ssm_out.weight` use `Q4_0`. All 48 `ssm_alpha` tensors remain `F32` for mathematical stability.

**Integrated MTP:** `blk.64.*` contains **424,699,392 stored parameters** in 15 tensors: seven `F32` tensors and eight matrices (`Q4_0` x6, `Q4_1` x1, `Q5_K` x1). Runtime acceleration depends on backend support and configuration; speculative decoding operates via native acceptance drafting.

[Complete tensor-by-tensor audit: names, formats, shapes and parameter counts](./tensor-map.tsv).


---

## 2. Model Files & Technical Specifications

| File Name | File Size | Whole-file BPW | Description |
| :--- | :--- | :--- | :--- |
| **`Swift-1.5-Qwen3.8-27B-Uncensored-VAL-APEX-I-NanoPlus-V3.gguf`** | **12.18 GB (11.35 GiB)** | **3.57 BPW** | Primary NanoPlus V3 quantized model with integrated MTP head |
| **`mmproj-Q8_0.gguf`** | **`629.25 MB` (`600.10 MiB`)** | **10.93 BPW** | Q8_0 multimodal vision projector with F32 and F16 tensors |

- **Architecture:** `qwen35`, dense hybrid Gated DeltaNet / full attention.
- **Native context:** 262,144 tokens (256K).
- **Stored parameters:** 27,320,697,856, including 424,699,392 in the MTP head.
- **Vision projector:** 334 tensors; `Q8_0` ×83, `F16` ×27 and `F32` ×224. Its filename describes the quantization profile, not a uniform format for every tensor.

---

## 3. Recommended Configuration & Setup

### llama-server (OpenAI-Compatible API with Native MTP Self-Speculation)

```bash
llama-server \
  -m Swift-1.5-Qwen3.8-27B-Uncensored-VAL-APEX-I-NanoPlus-V3.gguf \
  --mmproj mmproj-Q8_0.gguf \
  --port 8080 \
  --spec-type draft-mtp \
  --spec-draft-n-max 2 \
  -ngl 99 \
  -c 16384
```

---

## 4. Community Compute Fund & Priority Model Requests

All IsValorum quantizations will always remain completely free and open to the public without paywalls. 

If you find these builds valuable and would like to support the project or sponsor GPU compute time, you can contribute via Ko-fi:

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/isvalorum)
