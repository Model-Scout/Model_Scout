---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
- LiquidAI/LFM2.5-230M
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
library_name: transformers
---

# **LiquidAI-LFM2.5-230M-GGUF**

> **[LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M)** is [Liquid AI's](https://huggingface.co/LiquidAI) most compact hybrid model to date, a 230-million-parameter, general-purpose instruction-tuned text model built on the LFM2 architecture with extended pre-training (19T tokens) and reinforcement learning, designed specifically for on-device deployment in the tightest memory and compute budgets. Its 14-layer architecture combines 8 double-gated LIV convolution blocks with 6 GQA blocks, supports a 32,768-token context window across 10 languages, and was distilled from the larger LFM2.5-350M before being refined with multi-stage reinforcement learning, making it well-suited for agentic tasks like tool use and data extraction rather than reasoning-heavy workloads such as advanced math, code generation, or creative writing. It delivers strong edge inference throughput — 213 tok/s decode speed on a Galaxy S25 Ultra and 42 tok/s on a Raspberry Pi 5 — and despite its tiny size, outperforms similarly-scaled competitors like Granite 4.0-350M and LFM2-350M on benchmarks including IFEval (71.71), BFCLv3 (43.26), and Multi-IF (37.70), while supporting native function calling via Pythonic tool calls and ChatML-style chat templates, with deployment options spanning Transformers, vLLM, llama.cpp (GGUF), ONNX, and MLX formats.

## Model Files

   File Name | Quant Type | File Size | File Link |
 |-----------|------------|-----------|-----------|
 | LFM2.5-230M.BF16.gguf | BF16 | 462 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.BF16.gguf) |
 | LFM2.5-230M.F16.gguf | F16 | 462 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.F16.gguf) |
 | LFM2.5-230M.F32.gguf | F32 | 921 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.F32.gguf) |
 | LFM2.5-230M.Q2_K.gguf | Q2_K | 116 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q2_K.gguf) |
 | LFM2.5-230M.Q3_K_L.gguf | Q3_K_L | 139 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q3_K_L.gguf) |
 | LFM2.5-230M.Q3_K_M.gguf | Q3_K_M | 134 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q3_K_M.gguf) |
 | LFM2.5-230M.Q3_K_S.gguf | Q3_K_S | 127 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q3_K_S.gguf) |
 | LFM2.5-230M.Q4_0.gguf | Q4_0 | 149 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q4_0.gguf) |
 | LFM2.5-230M.Q4_K_M.gguf | Q4_K_M | 153 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q4_K_M.gguf) |
 | LFM2.5-230M.Q4_K_S.gguf | Q4_K_S | 150 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q4_K_S.gguf) |
 | LFM2.5-230M.Q5_0.gguf | Q5_0 | 169 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q5_0.gguf) |
 | LFM2.5-230M.Q5_K_M.gguf | Q5_K_M | 172 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q5_K_M.gguf) |
 | LFM2.5-230M.Q5_K_S.gguf | Q5_K_S | 169 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q5_K_S.gguf) |
 | LFM2.5-230M.Q6_K.gguf | Q6_K | 191 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q6_K.gguf) |
 | LFM2.5-230M.Q8_0.gguf | Q8_0 | 247 MB | [Download](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-230M-GGUF/blob/main/LFM2.5-230M.Q8_0.gguf) |

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp