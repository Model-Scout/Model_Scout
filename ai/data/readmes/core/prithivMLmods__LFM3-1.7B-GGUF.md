---
library_name: transformers
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
pipeline_tag: text-generation
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
- LiquidAI/LFM3-1.7B
---

# **LFM3-1.7B-GGUF**

> **LFM3-1.7B** is a compact 1.73B-parameter text-only language model from Liquid AI, released under the LFM Open License v1.0. Its 24-layer tri-hybrid architecture combines gated short convolutions, sliding-window attention, and global attention, supporting 16 languages and a 256K-token context window. Designed for local agent frameworks, structured outputs, and XML-based tool calling, it supports configurable thinking modes and dynamic tool search. Despite its small size, it achieves a benchmark average of 49.37, outperforming several larger models, including Qwen3.5-9B (47.24). Key results include 73.46 on LiveCodeBench v6, 71.39 on BFCL V4, 68.64 on Claw-Eval General, 96.66 on IFEval, and 92.93 on AA-Omniscience non-hallucination. At 4-bit precision, it requires roughly 1 GB of memory and delivers efficient inference on edge hardware. Available in BF16, FP8, NVFP4, GGUF, MLX, and ONNX formats, it supports vLLM, SGLang, Transformers, llama.cpp, Ollama, and other deployment runtimes.

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| LFM3-1.7B.BF16.gguf | BF16 | 3.47 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.BF16.gguf) | Full BF16 weights. Highest quality, largest file size. |
| LFM3-1.7B.Q3_K_L.gguf | Q3_K_L | 967 MB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q3_K_L.gguf) | Lower quality but usable, good for low RAM availability. |
| LFM3-1.7B.Q3_K_M.gguf | Q3_K_M | 915 MB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q3_K_M.gguf) | Low quality. |
| LFM3-1.7B.Q4_K_M.gguf | Q4_K_M | 1.1 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q4_K_M.gguf) | Good quality, default size for most use cases, *recommended*. |
| LFM3-1.7B.Q4_K_S.gguf | Q4_K_S | 1.06 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q4_K_S.gguf) | Slightly lower quality with more space savings, *recommended*. |
| LFM3-1.7B.Q5_K_M.gguf | Q5_K_M | 1.26 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q5_K_M.gguf) | High quality, *recommended*. |
| LFM3-1.7B.Q5_K_S.gguf | Q5_K_S | 1.23 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q5_K_S.gguf) | High quality, *recommended*. |
| LFM3-1.7B.Q6_K.gguf | Q6_K | 1.43 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q6_K.gguf) | Very high quality, near perfect, *recommended*. |
| LFM3-1.7B.Q8_0.gguf | Q8_0 | 1.85 GB | [Link](https://huggingface.co/prithivMLmods/LFM3-1.7B-GGUF/blob/main/LFM3-1.7B.Q8_0.gguf) | Extremely high quality, generally unneeded but max available quant. |

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp