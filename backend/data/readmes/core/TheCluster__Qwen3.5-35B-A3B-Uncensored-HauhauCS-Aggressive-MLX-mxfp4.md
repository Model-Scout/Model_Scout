---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-27B/blob/main/LICENSE
base_model:
- HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive
base_model_relation: quantized
library_name: mlx
tags:
- uncensored
- unrestricted
- decensored
- mxfp4
pipeline_tag: image-text-to-text
language:
- en
- zh
- ru
- es
- fr
- it
- ja
- ko
- af
- de
- ar
- tr
- is
- pl
- sw
- sv
- nl
- he
- id
- uk
- fa
- pa
- pt
- ms
- fi
- el
---
# Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive

Qwen3.5-35B-A3B uncensored by HauhauCS.

**Quality**: quantized (***mxfp4**, 4.402 bpw*)

## About

No changes to datasets or capabilities. Fully functional, 100% of what the original authors intended - just without the refusals.

These are meant to be the best lossless uncensored models out there.

## Aggressive Variant

Stronger uncensoring with more thorough refusal removal. If this variant is too loose for your use case, a Balanced variant may follow.

**Note:** The model is fully unlocked and will not refuse prompts. However, it may occasionally append a short disclaimer at the end of a response (e.g. "This is general information, not legal advice..."). This is baked into the base model's training and not a refusal — the actual content is still generated in full.

## Specs

- 35B total parameters, ~3B active per forward pass (MoE)
- 256 experts, 8 routed + 1 shared per token
- Hybrid architecture: Gated DeltaNet linear attention + full softmax attention (3:1 ratio)
- 40 layers, pattern: 10 x (3 x DeltaNet-MoE + 1 x Attention-MoE)
- 262K native context (extendable to 1M with YaRN)
- Natively multimodal (text, image, video)
- Multi-token prediction (MTP) support
- 248K vocabulary, 201 languages
- Based on [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)

## Recommended Settings

From the official Qwen authors:

**Thinking mode (default):**
- General: `temperature=1.0, top_p=0.95, top_k=20, min_p=0, presence_penalty=1.5`
- Coding/precise tasks: `temperature=0.6, top_p=0.95, top_k=20, min_p=0, presence_penalty=0`
**Non-thinking mode:**
- General: `temperature=0.7, top_p=0.8, top_k=20, min_p=0, presence_penalty=1.5`
- Reasoning tasks: `temperature=1.0, top_p=1.0, top_k=40, min_p=0, presence_penalty=2.0`

-----
### Source
This model was converted to MLX format from [`HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive`](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)