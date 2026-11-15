---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/d1-3B/blob/main/LICENSE
base_model:
- LiquidAI/d1-3B
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- text-generation-inference
- decision-model
- llama-cpp
- liquid
- lfm2.5
- edge
- decision
- classification
- calibration
- system-one
- multimodal
---

# **d1-3B-GGUF**

> **d1-3B** is Liquid AI's 3.1-billion-parameter multimodal decision model, post-trained from LFM2.5-VL-3B to take a state (text, JSON, images, or a mix) plus a set of typed questions (`noul` yes/no, `choice` among named options, or `score` on an ordered scale) and return calibrated probabilities in one forward pass with zero generated output tokens — making it suited for routing, triage, moderation, intent/topic classification, extraction checks, reranking, LLM-as-a-judge scoring, agent guardrails, and visual inspection rather than open-ended chat. It retains the SigLIP2 NaFlex 400M vision encoder and 32,768-token context of its base model, and is notably fast: 8ms per decision on an RTX 4090, 9ms on an AMD MI325X, and 30ms on an Apple M5 Pro, with throughput reaching over 1,100 decisions/sec when 64 states are packed into one batch on the MI325X. On the Decision Index 0.2.1 it scores 48.57, the best model under 10B parameters, ahead of every 4B and 9B competitor as well as the much larger Decider 35B-A3B (47.11), with particularly strong Tools (74.5) and Arts (36.3) subscores, and across 11 public image benchmarks read as decisions it scores a 74.1 mean, slightly above its own base model (73.9), confirming the gains come from genuinely reading the images rather than text priors (removing images drops the same questions to 45.1). It's loaded via standard Transformers with `trust_remote_code=True`, callable through `system_one()` for single multi-question requests or `system_one_batch()` for padding-free batched inference, and is released under Liquid AI's LFM1.0 license. **d1-3B** on Hugging Face — https://huggingface.co/LiquidAI/d1-3B.

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| d1-3B.BF16.gguf | BF16 | 5.4 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.BF16.gguf) | Full BF16 weights. Highest quality, largest file size. |
| d1-3B.Q3_K_L.gguf | Q3_K_L | 1.45 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q3_K_L.gguf) | Lower quality but usable, good for low RAM availability. |
| d1-3B.Q3_K_M.gguf | Q3_K_M | 1.37 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q3_K_M.gguf) | Low quality. |
| d1-3B.Q4_K_M.gguf | Q4_K_M | 1.67 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q4_K_M.gguf) | Good quality, default size for most use cases, *recommended*. |
| d1-3B.Q4_K_S.gguf | Q4_K_S | 1.6 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q4_K_S.gguf) | Slightly lower quality with more space savings, *recommended*. |
| d1-3B.Q5_K_M.gguf | Q5_K_M | 1.94 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q5_K_M.gguf) | High quality, *recommended*. |
| d1-3B.Q5_K_S.gguf | Q5_K_S | 1.9 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q5_K_S.gguf) | High quality, *recommended*. |
| d1-3B.Q6_K.gguf | Q6_K | 2.22 GB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.Q6_K.gguf) | Very high quality, near perfect, *recommended*. |
| d1-3B.mmproj-bf16.gguf | mmproj-bf16 | 856 MB | [Link](https://huggingface.co/prithivMLmods/d1-3B-GGUF/blob/main/d1-3B.mmproj-bf16.gguf) | Multimodal projection file in BF16 format. Used for vision/language models. |

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp