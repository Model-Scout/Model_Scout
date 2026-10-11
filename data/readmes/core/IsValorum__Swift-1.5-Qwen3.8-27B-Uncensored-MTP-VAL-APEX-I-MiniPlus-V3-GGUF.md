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
- miniplus-v3
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

# Swift-1.5-Qwen3.8-27B-Uncensored-MTP VAL-APEX-I MiniPlus V3 GGUF

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/isvalorum)

*Independently computed on an NVIDIA RTX PRO 6000 Blackwell Server Edition GPU. If this handcrafted release saves you VRAM and runs faster on your GPU, consider [fueling the community compute fund on Ko-fi](https://ko-fi.com/isvalorum).*

### *Uncensored Frontier 27B Dense Hybrid Reasoning Model with Intact Vision, Multilingual Syntax Preservation, and Native MTP Self-Speculation*

Official **VAL-APEX-I MiniPlus V3** quantization of **[ajgazin/Swift-1.5-Qwen3.8-27B-Uncensored-MTP](https://huggingface.co/ajgazin/Swift-1.5-Qwen3.8-27B-Uncensored-MTP)**. This edition quantizes the uncensored foundation model built on UkisAI's Swift-1.5 reasoning fine-tune of Qwen3.8-27B with the official canonical V3 recipe (strictly enforcing `IQ4_XS` and protecting attention/recurrent matrices).

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
> - **[Swift-1.5 Qwen3.8 27B Uncensored MTP — NanoPlus V3](https://huggingface.co/IsValorum/Swift-1.5-Qwen3.8-27B-Uncensored-MTP-VAL-APEX-I-NanoPlus-V3-GGUF)** — 12.18 GB.
>
> **[VAL-APEX-I collection](https://huggingface.co/collections/IsValorum/val-apex-i-6ac563d1784a04a1bb177f47)** · **[MiniPlus collection](https://huggingface.co/collections/IsValorum/apex-i-miniplus-v21-current-6aac8d4766a28a024e8bb104)** · **[NanoPlus collection](https://huggingface.co/collections/IsValorum/apex-i-nanoplus-6ab41467c988a1b1cb9b83bc)**

---

## 1. Quantization Metrics

### Size & Quality Metrics

| Edition / quantization | File size | Whole-file BPW | WikiText-2 PPL |
| :--- | :--- | :--- | :--- |
| **Swift-1.5 Qwen3.8 27B Uncensored MTP MiniPlus V3 (this release)** | 14.16 GB (13.19 GiB) | 4.15 | **6.2501** |

This MiniPlus edition was evaluated on WikiText-2 under the same conditions as its previous recipe, as confirmed by the release maintainer. Its reported PPL changed from 6.6669 to 6.2501 (6.25% lower). The current evaluation uses `llama-perplexity` with context 512, batch 512, four chunks and GPU offload (`-ngl 99`), from llama.cpp build 11512 (`a11f57ba9`).

Whole-file BPW is calculated from the complete GGUF file size and its 27,320,697,856 stored parameters, including MTP.




Evaluation runs: [current canonical V3 job](https://huggingface.co/jobs/IsValorum/6ac97502095c57808930b6b1) · [previous recipe job](https://huggingface.co/jobs/IsValorum/6ac9202ffee2c9007017aab3).

### Tensor Precision Map

| Component | MiniPlus V3 | NanoPlus V3 | GSQ-RCO IQ3_S |
| :--- | :--- | :--- | :--- |
| Output head | `Q6_K` ×1 | `Q6_K` ×1 | `Q4_K` ×1 |
| Token embeddings | `Q4_K` ×1 | `Q3_K` ×1 | `IQ2_S` ×1 |
| Normalizations | `F32` ×161 | `F32` ×161 | `F32` ×161 |
| SSM A (`ssm_a`) | `F32` ×48 | `F32` ×48 | `F32` ×48 |
| SSM convolution (`ssm_conv1d`) | `F32` ×48 | `F32` ×48 | `F32` ×48 |
| SSM time-step bias (`ssm_dt`) | `F32` ×48 | `F32` ×48 | `F32` ×48 |
| SSM norm (`ssm_norm`) | `F32` ×48 | `F32` ×48 | `F32` ×48 |
| Attention gates (`attn_gate`) | `Q4_0` ×1<br>`Q4_K` ×47 | `Q4_0` ×1<br>`Q4_K` ×47 | `IQ2_S` ×2<br>`IQ3_S` ×18<br>`IQ3_XXS` ×9<br>`IQ4_XS` ×12<br>`Q2_K` ×4<br>`Q4_K` ×3 |
| Linear QKV (`attn_qkv`) | `Q4_0` ×1<br>`Q4_K` ×47 | `Q3_K` ×47<br>`Q4_0` ×1 | `IQ2_XS` ×1<br>`IQ2_XXS` ×1<br>`IQ3_S` ×22<br>`IQ3_XXS` ×13<br>`IQ4_XS` ×9<br>`Q2_K` ×1<br>`Q4_K` ×1 |
| SSM alpha (`ssm_alpha`) | `F32` ×48 | `F32` ×48 | `BF16` ×48 |
| SSM beta (`ssm_beta`) | `Q4_0` ×1<br>`Q8_0` ×47 | `Q4_0` ×1<br>`Q8_0` ×47 | `BF16` ×48 |
| SSM output (`ssm_out`) | `Q4_0` ×1<br>`Q5_K` ×47 | `Q4_0` ×1<br>`Q4_K` ×47 | `IQ3_S` ×22<br>`IQ3_XXS` ×4<br>`IQ4_XS` ×16<br>`Q4_K` ×6 |
| Full attention Q (`attn_q`) | `Q4_K` ×16 | `Q3_K` ×16 | `IQ2_XXS` ×1<br>`IQ3_S` ×3<br>`IQ3_XXS` ×3<br>`IQ4_XS` ×2<br>`Q2_K` ×6<br>`Q4_K` ×1 |
| Full attention K (`attn_k`) | `Q5_K` ×16 | `Q4_K` ×16 | `IQ2_S` ×1<br>`IQ3_S` ×1<br>`IQ3_XXS` ×1<br>`IQ4_XS` ×8<br>`Q4_K` ×5 |
| Full attention V (`attn_v`) | `Q6_K` ×16 | `Q5_K` ×16 | `IQ3_S` ×6<br>`IQ3_XXS` ×1<br>`IQ4_XS` ×1<br>`Q4_K` ×8 |
| Full attention output (`attn_output`) | `Q6_K` ×16 | `Q6_K` ×16 | `IQ3_S` ×10<br>`IQ3_XXS` ×1<br>`IQ4_XS` ×2<br>`Q4_K` ×3 |
| MLP down (`ffn_down`) | `IQ4_XS` ×64 | `IQ3_XXS` ×48<br>`IQ4_XS` ×16 | `IQ2_S` ×4<br>`IQ2_XS` ×3<br>`IQ3_S` ×22<br>`IQ3_XXS` ×7<br>`IQ4_XS` ×21<br>`Q2_K` ×1<br>`Q4_K` ×6 |
| MLP gate (`ffn_gate`) | `IQ3_S` ×32<br>`IQ3_XXS` ×32 | `IQ2_XXS` ×48<br>`IQ3_XXS` ×16 | `IQ1_M` ×1<br>`IQ2_S` ×4<br>`IQ2_XS` ×4<br>`IQ2_XXS` ×1<br>`IQ3_S` ×15<br>`IQ3_XXS` ×21<br>`IQ4_XS` ×15<br>`Q2_K` ×1<br>`Q4_K` ×2 |
| MLP up (`ffn_up`) | `IQ3_S` ×32<br>`IQ3_XXS` ×32 | `IQ2_XXS` ×48<br>`IQ3_XXS` ×16 | `IQ2_S` ×5<br>`IQ2_XS` ×1<br>`IQ2_XXS` ×2<br>`IQ3_S` ×25<br>`IQ3_XXS` ×18<br>`IQ4_XS` ×10<br>`Q4_K` ×3 |
| Additional MTP head (`blk.64.*`) | `F32` ×7<br>`Q4_0` ×6<br>`Q4_1` ×1<br>`Q6_K` ×1 | `F32` ×7<br>`Q4_0` ×6<br>`Q4_1` ×1<br>`Q6_K` ×1 | — |

× denotes tensor counts. All three columns were checked against the released GGUF tensor headers. Normalizations exclude the separately listed SSM norms and MTP tensors.

Both Swift files contain **866 tensors**: **851 main-model tensors** plus **15 MTP tensors**. The main model is a dense hybrid architecture with **64 layers: 48 Gated DeltaNet linear-attention layers and 16 full-attention layers**. The additional `blk.64.*` block is the MTP head, not another main layer.

**V3 layer allocation:** MiniPlus MLP gate/up use `IQ3_S` in layers 0-15 and 48-63, and `IQ3_XXS` in layers 16-47; all 64 main MLP down tensors use `IQ4_XS`. NanoPlus MLP gate/up use `IQ3_XXS` in layers 0-7 and 56-63, and `IQ2_XXS` in layers 8-55; MLP down uses `IQ4_XS` in the outer 16 layers and `IQ3_XXS` in the remaining 48.

**Actual layer-0 formats:** `blk.0.attn_gate.weight`, `blk.0.attn_qkv.weight`, `blk.0.ssm_beta.weight` and `blk.0.ssm_out.weight` use `Q4_0`. All 48 `ssm_alpha` tensors, including `blk.0.ssm_alpha.weight`, remain `F32`; this is the single difference from the recipe files, which request `Q4_0` for layer-0 alpha.

**Integrated MTP:** `blk.64.*` contains **424,699,392 stored parameters** in 15 tensors: seven `F32` tensors and eight matrices (`Q4_0` ×6, `Q4_1` ×1, `Q6_K` ×1). Runtime acceleration depends on backend support and configuration; the WikiText-2 results above do not measure speculative-decoding speed.

[Complete tensor-by-tensor audit: names, formats, shapes and parameter counts](./tensor-map.tsv).

[GSQ-RCO tensor-map reference GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF/blob/d562806dbafae37109975e970aae91b43e73b440/Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf).

---

## 2. Model Files & Technical Specifications

| File Name | File Size | Whole-file BPW | Description |
| :--- | :--- | :--- | :--- |
| **`Swift-1.5-Qwen3.8-27B-Uncensored-VAL-APEX-I-MiniPlus-V3.gguf`** | **14.16 GB (13.19 GiB)** | **4.15 BPW** | Primary MiniPlus V3 quantized model with integrated MTP head |
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
  -m Swift-1.5-Qwen3.8-27B-Uncensored-VAL-APEX-I-MiniPlus-V3.gguf \
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
