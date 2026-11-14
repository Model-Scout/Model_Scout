---
library_name: transformers
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM3-VL-2B/blob/main/LICENSE
pipeline_tag: image-text-to-text
tags:
- llama-cpp
- liquid
- lfm3
- edge
- conversational
- custom_code
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
base_model:
- LiquidAI/LFM3-VL-2B
---

# **LFM3-VL-2B-GGUF**

> **LFM3-VL-2B** is a 1.92B-parameter vision-language model from Liquid AI, released under the LFM Open License v1.0 for multilingual, on-device visual understanding across 16 languages. It combines the 24-layer LFM3-1.7B tri-hybrid language model with a 164M-parameter hybrid vision encoder and a 25M-parameter projector, supporting a 128K-token context window and native-resolution video at 2 fps. Built from the 22-trillion-token LFM3-1.7B-Base checkpoint through vision mid-training, supervised fine-tuning, vision reinforcement learning, and on-policy distillation, it supports step-by-step `<think>...</think>` reasoning, XML-based tool calling, and deferred tool search. Across 62 vision benchmarks, it achieves an average score of **71.4** (62.1 without thinking), outperforming LFM2.5-VL-3B (57.6), MiniCPM-V 4.7 1B (57.5), Qwen3.5-2B (64.0), InternVL3.5-4B (61.1), and Gemma 4 E2B (53.6). It matches Gemma 4 12B (71.7), approaches Qwen3.5-4B and GPT-5.6 Luna (both 73.4), and surpasses Gemini 3.5 Flash Lite (70.0). Key results include Visual Grounding 77.3, Embodied Reasoning 64.4, GUI Understanding 83.1, ChartQA 92.7, BLINK 71.1, CV-Bench 88.8, and ActivityNet-QA 71.2. It offers high prefill throughput and low memory usage on edge devices, exceeding 12,000 output tokens/s at 1,024 concurrent requests on a single NVIDIA B300 GPU. Available in BF16, GGUF, 4-bit MLX, and ONNX formats, it supports TRL fine-tuning with SFT and GRPO, plus Transformers (`transformers>=5.21.0`), vLLM, SGLang, llama.cpp, MLX-VLM, and ONNX Runtime.

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| LFM3-VL-2B.BF16.gguf | BF16 | 3.47 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.BF16.gguf) | Full BF16 weights. Highest quality, largest file size. |
| LFM3-VL-2B.Q3_K_L.gguf | Q3_K_L | 967 MB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q3_K_L.gguf) | Lower quality but usable, good for low RAM availability. |
| LFM3-VL-2B.Q3_K_M.gguf | Q3_K_M | 915 MB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q3_K_M.gguf) | Low quality. |
| LFM3-VL-2B.Q4_K_M.gguf | Q4_K_M | 1.1 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q4_K_M.gguf) | Good quality, default size for most use cases, *recommended*. |
| LFM3-VL-2B.Q4_K_S.gguf | Q4_K_S | 1.06 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q4_K_S.gguf) | Slightly lower quality with more space savings, *recommended*. |
| LFM3-VL-2B.Q5_K_M.gguf | Q5_K_M | 1.26 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q5_K_M.gguf) | High quality, *recommended*. |
| LFM3-VL-2B.Q5_K_S.gguf | Q5_K_S | 1.23 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q5_K_S.gguf) | High quality, *recommended*. |
| LFM3-VL-2B.Q6_K.gguf | Q6_K | 1.43 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q6_K.gguf) | Very high quality, near perfect, *recommended*. |
| LFM3-VL-2B.Q8_0.gguf | Q8_0 | 1.85 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.Q8_0.gguf) | Extremely high quality, generally unneeded but max available quant. |
| LFM3-VL-2B.mmproj-bf16.gguf | mmproj-bf16 | 379 MB | [Link](https://huggingface.co/prithivMLmods/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B.mmproj-bf16.gguf) | Multimodal projection file in BF16 format. Used for vision/language models. |

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp