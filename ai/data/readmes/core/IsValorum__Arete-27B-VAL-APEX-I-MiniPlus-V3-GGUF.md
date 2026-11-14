---
base_model: NousResearch/Arete-27B
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
license: apache-2.0
language:
- en
- es
- fr
- de
- it
- pt
- zh
- ja
- ko
- ar
- ru
tags:
- gguf
- apex
- val-apex
- arete
- qwen3.5
---

# Arete-27B VAL-APEX-I MiniPlus V3

**APEX Quantization Series by IsValorum**

<p align="left">
  <a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>
</p>

> [!IMPORTANT]
> **Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**
>
> If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

## Family cross-links

| Tier | Footprint | Base |
|---|---|---|
| **MiniPlus** | 14.03 GB (13.07 GiB) | [Base](https://huggingface.co/IsValorum/Arete-27B-VAL-APEX-I-MiniPlus-V3-GGUF) |
| NanoPlus | 12.70 GB (11.83 GiB) | [Base](https://huggingface.co/IsValorum/Arete-27B-VAL-APEX-I-NanoPlus-V3-GGUF) |
| MicroPlus | 10.25 GB (9.55 GiB) | [Base](https://huggingface.co/IsValorum/Arete-27B-VAL-APEX-I-MicroPlus-V3-GGUF) |

## Architecture and precision

- Base model: [`NousResearch/Arete-27B`](https://huggingface.co/NousResearch/Arete-27B)
- Architecture: Qwen3.5 dense hybrid (`Qwen3_5ForConditionalGeneration`); 64 layers, 48 Gated DeltaNet linear-attention and 16 full-attention; text plus vision; 851 tensors.
- iMatrix: upstream Arete-27B importance matrix from bartowski's GGUF (496 block entries, 583 chunks); reused unchanged, not computed in this campaign.
- Recurrent shielding: decay factors, 1D convs, and RMSNorms in `F32`.
- Layer-0 boundary: `attn_gate`, `attn_qkv`, `ssm_beta`, and `ssm_out` use Q4_0 on block 0; the remaining 47 SSM layers use the tier precision.
- Vision projector: the language-model GGUF is self-contained; the upstream `mmproj` companion is not included in this repository.
- MTP: none; the checkpoint has 851 tensors and no MTP block.

## Surgical Tensor Quantization Map (Audited from GGUF)

*The exact tensor breakdown below has been verified directly from the compiled binary weights:*

| Layer Group | Sub-Component / Tensor | Qty | Precision | Engineering Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **Global Output Head** | `output.weight` | 1 | **`Q6_K`** | Logit projection; the output head keeps the highest practical precision to protect the vocabulary tail. |
| **Global Embeddings** | `token_embd.weight` | 1 | **`Q4_K`** | Vocabulary table; the selected K-quant balances embedding quality and footprint. |
| **All Normalizations** | `output_norm`, `attn_*_norm`, `post_attention_norm`, `ssm_norm` | 209 | **`F32`** | RMSNorm and q/k normalization stay in F32; normalization statistics are not quantized. |
| **Recurrent SSM Scales** | `ssm_alpha`, `ssm_a`, `ssm_dt.bias`, `ssm_conv1d` | 192 | **`F32`** | Recurrent decay, time-step, and convolution parameters stay in F32 for long-context stability. |
| **SSM Gate** | `attn_gate.weight` | 48 | **`Q4_K`** (Q4_0 on block 0) | Gated DeltaNet input gate; block 0 uses the Q4_0 boundary, the other 47 SSM layers use the tier precision. |
| **SSM QKV** | `attn_qkv.weight` | 48 | **`Q4_K`** (Q4_0 on block 0) | Linear-attention QKV projection; block 0 uses the Q4_0 boundary, the other 47 SSM layers use the tier precision. |
| **SSM Beta** | `ssm_beta.weight` | 48 | **`Q8_0`** (Q4_0 on block 0) | SSM beta is kept at Q8_0 for sensitivity; block 0 uses the Q4_0 boundary. |
| **SSM Output** | `ssm_out.weight` | 48 | **`Q5_K`** (Q4_0 on block 0) | Linear-attention output projection; block 0 uses the Q4_0 boundary, the other 47 SSM layers use the tier precision. |
| **Full Attention Q/K** | `attn_q.weight`, `attn_k.weight` | 32 | **`Q5_K`** | Attention score projections for the 16 full-attention layers. |
| **Full Attention V** | `attn_v.weight` | 16 | **`Q6_K`** | Value path for the 16 full-attention layers. |
| **Full Attention Output** | `attn_output.weight` | 16 | **`Q6_K`** | Attention output projection for the 16 full-attention layers. |
| **FFN Gate** | `ffn_gate.weight` | 64 | **`IQ3_S on layers 0-15 and 48-63; IQ3_XXS on layers 16-47`** | Dense FFN input gate; the precision is zoned by layer as shown. |
| **FFN Up** | `ffn_up.weight` | 64 | **`IQ3_S on layers 0-15 and 48-63; IQ3_XXS on layers 16-47`** | Dense FFN input projection; the precision is zoned by layer as shown. |
| **FFN Down** | `ffn_down.weight` | 64 | **`IQ4_XS`** | IQ4_XS across all 64 layers; the FFN input path keeps the higher-precision IQ3 split. |

The complete audited list is [tensor-map.tsv](./tensor-map.tsv).
