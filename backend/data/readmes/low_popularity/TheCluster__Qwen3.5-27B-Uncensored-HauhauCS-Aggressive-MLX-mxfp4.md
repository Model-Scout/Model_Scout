---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-27B/blob/main/LICENSE
base_model:
- HauhauCS/Qwen3.5-27B-Uncensored-HauhauCS-Aggressive
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
# Qwen3.5-27B-Uncensored-HauhauCS-Aggressive

Qwen3.5-27B uncensored by HauhauCS.

**Quality**: quantized (***mxfp4**, 4.449 bpw*)

## About

**0/465 refusals.** Fully uncensored with zero capability loss.

No changes to datasets or capabilities. Fully functional, 100% of what the original authors intended - just without the refusals.

These are meant to be the best lossless uncensored models out there.

## Aggressive Variant

Stronger uncensoring with more thorough refusal removal. If this variant is too loose for your use case, a Balanced variant may follow.

**Note:** The model is fully unlocked and will not refuse prompts. However, it may occasionally append a short disclaimer at the end of a response (e.g. "This is general information, not legal advice..."). This is baked into the base model's training and not a refusal — the actual content is still generated in full.

## Specs

- 27B dense parameters, 64 layers
- Hybrid architecture: Gated DeltaNet linear attention + full softmax attention (3:1 ratio)
- 262K native context (extendable to 1M with YaRN)
- Natively multimodal (text, image, video)
- Multi-token prediction (MTP) support
- 248K vocabulary, 201 languages
- Based on [Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)

Also check out the [9B variant](https://huggingface.co/TheCluster/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-MLX-mxfp4)

## Recommended Settings

From the official Qwen authors:

**Thinking mode (default):**
- `temperature=0.6`, `top_p=0.95`, `top_k=20`, `min_p=0`

**Non-thinking mode:**
- `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0`

-----
### Source
This model was converted to MLX format from [`HauhauCS/Qwen3.5-27B-Uncensored-HauhauCS-Aggressive`](https://huggingface.co/HauhauCS/Qwen3.5-27B-Uncensored-HauhauCS-Aggressive)