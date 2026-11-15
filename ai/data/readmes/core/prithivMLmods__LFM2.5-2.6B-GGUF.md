---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
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
base_model:
- LiquidAI/LFM2.5-2.6B
pipeline_tag: text-generation
tags:
- text-generation-inference
- llama-cpp
- liquid
- lfm2.5
- edge
---

# **LFM2.5-2.6B-GGUF**

> **[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)** is Liquid AI's agent-focused member of the LFM2.5 hybrid model family, a 2.69-billion-parameter, text-only model built on the LFM2 architecture with a 128K-token context window and post-trained specifically for agentic workloads. Its 30-layer architecture (22 double-gated short convolution blocks plus 8 GQA blocks) was pre-trained on ~34 trillion tokens and then transformed into an agent through a four-stage post-training pipeline — two rounds of supervised fine-tuning, per-domain teacher specialization, multi-domain on-policy distillation, and agentic reinforcement learning trained directly inside popular agentic harnesses — making it a pure reasoning model that always emits a `<think>` block before answering, and supports Pythonic tool calls across 16 languages. Despite its compact size, it proves competitive with models up to 4x larger on tool use, instruction following, and multi-step agentic tasks, outperforming Gemma-4-E4B-it (8B) and rivaling Qwen3.5-9B on benchmarks like IFBench (59.17), Multi-IF (80.07), IFStruct (85.49), and BFCLv4 (56.88), while delivering exceptional efficiency — 220 tok/s on an Apple M5 Max, 113 tok/s on a Ryzen AI Max+ CPU under 2.5GB of memory, and nearly 15K output tokens/sec at high concurrency on a single H100. It's recommended for agentic workloads, tool use, data extraction, RAG, and long-context tasks (though not for agentic coding or knowledge-heavy tasks), ships in native, GGUF, ONNX, and MLX formats, and is released under Liquid AI's LFM1.0 license.

## Model Files

   File Name | Quant Type | File Size | File Link |
 |-----------|------------|-----------|-----------|
 | LFM2.5-2.6B.BF16.gguf | BF16 | 5.4 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.BF16.gguf) |
 | LFM2.5-2.6B.F16.gguf | F16 | 5.4 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.F16.gguf) |
 | LFM2.5-2.6B.F32.gguf | F32 | 10.8 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.F32.gguf) |
 | LFM2.5-2.6B.Q3_K_L.gguf | Q3_K_L | 1.45 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q3_K_L.gguf) |
 | LFM2.5-2.6B.Q3_K_M.gguf | Q3_K_M | 1.37 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q3_K_M.gguf) |
 | LFM2.5-2.6B.Q3_K_S.gguf | Q3_K_S | 1.27 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q3_K_S.gguf) |
 | LFM2.5-2.6B.Q4_K_M.gguf | Q4_K_M | 1.67 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q4_K_M.gguf) |
 | LFM2.5-2.6B.Q4_K_S.gguf | Q4_K_S | 1.6 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q4_K_S.gguf) |
 | LFM2.5-2.6B.Q5_K_M.gguf | Q5_K_M | 1.94 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q5_K_M.gguf) |
 | LFM2.5-2.6B.Q5_K_S.gguf | Q5_K_S | 1.9 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q5_K_S.gguf) |
 | LFM2.5-2.6B.Q6_K.gguf | Q6_K | 2.22 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q6_K.gguf) |
 | LFM2.5-2.6B.Q8_0.gguf | Q8_0 | 2.87 GB | [Download](https://huggingface.co/prithivMLmods/LFM2.5-2.6B-GGUF/blob/main/LFM2.5-2.6B.Q8_0.gguf) |

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp