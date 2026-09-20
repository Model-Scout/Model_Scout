---
license: apache-2.0
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- text-generation-inference
- llama.cpp
- f32
base_model:
- mistralai/Ministral-3-14B-Instruct-2512
- mistralai/Ministral-3-8B-Instruct-2512
- mistralai/Ministral-3-3B-Instruct-2512
- mistralai/Ministral-3-14B-Instruct-2512-BF16
- mistralai/Ministral-3-8B-Instruct-2512-BF16
- mistralai/Ministral-3-3B-Instruct-2512-BF16
---

# **Ministral-3-Instruct-2512-AIO-GGUF**

> The [Ministral 3 Instruct](https://huggingface.co/collections/mistralai/ministral-3) models (3B, 8B, and 14B variants from mistralai) form a family of compact, edge-optimized vision-language models designed for efficient deployment on resource-constrained hardware, featuring FP8 precision for the Instruct versions to fit in as little as 8GB VRAM (3B), 12GB (8B), or higher for 14B while supporting a 256k token context window. Comprising a language model (3.4B, 8.4B, or larger parameters) paired with a 0.4B vision encoder, they excel in multimodal tasks like image analysis, captioning, document understanding, multilingual support across dozens of languages (English, French, Spanish, Chinese, etc.), strong system prompt adherence, agentic function calling with JSON output, and real-time applications such as translation, data extraction, and short content generation under Apache 2.0 license. Benchmarks highlight competitive reasoning (e.g., Ministral 3 3B scores 0.721 on AIME25, 0.534 on GPQA Diamond) and instruct performance (0.305 Arena Hard, 7.83 MM MTBench for 3B), outperforming peers like Qwen3-VL-2B in efficiency for local/embedded use cases with vLLM or Transformers integration.

```
Quantized GGUF for the following Ministral-3 models

+ mistralai/ministral-3-14b-instruct-2512
+ mistralai/ministral-3-8b-instruct-2512
+ mistralai/ministral-3-3b-instruct-2512
+ mistralai/ministral-3-14b-instruct-2512-bf16
+ mistralai/ministral-3-8b-instruct-2512-bf16
+ mistralai/ministral-3-3b-instruct-2512-bf16
  
Download from the respective file links below or from the Files and Versions section.
```

# Ministral-3-14B-Instruct-2512 [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Ministral-3-14B-Instruct-2512-BF16.gguf | BF16 | 27 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.IQ4_XS.gguf | IQ4_XS | 7.48 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.IQ4_XS.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q2_K.gguf | Q2_K | 5.25 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q2_K.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q3_K_L.gguf | Q3_K_L | 7.21 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q3_K_L.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q3_K_M.gguf | Q3_K_M | 6.68 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q3_K_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q3_K_S.gguf | Q3_K_S | 6.07 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q3_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q4_K_M.gguf | Q4_K_M | 8.24 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q4_K_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q4_K_S.gguf | Q4_K_S | 7.83 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q4_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q5_K_M.gguf | Q5_K_M | 9.62 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q5_K_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q5_K_S.gguf | Q5_K_S | 9.38 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q5_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q6_K.gguf | Q6_K | 11.1 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q6_K.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.Q8_0.gguf | Q8_0 | 14.4 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.Q8_0.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ1_M.gguf | i1-IQ1_M | 3.5 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ1_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ1_S.gguf | i1-IQ1_S | 3.25 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ1_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_M.gguf | i1-IQ2_M | 4.84 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_S.gguf | i1-IQ2_S | 4.51 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_XS.gguf | i1-IQ2_XS | 4.28 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_XS.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_XXS.gguf | i1-IQ2_XXS | 3.92 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ2_XXS.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_M.gguf | i1-IQ3_M | 6.27 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_S.gguf | i1-IQ3_S | 6.1 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_XS.gguf | i1-IQ3_XS | 5.82 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_XS.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_XXS.gguf | i1-IQ3_XXS | 5.43 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ3_XXS.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ4_NL.gguf | i1-IQ4_NL | 7.81 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ4_NL.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-IQ4_XS.gguf | i1-IQ4_XS | 7.41 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-IQ4_XS.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q2_K.gguf | i1-Q2_K | 5.25 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q2_K.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q2_K_S.gguf | i1-Q2_K_S | 4.92 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q2_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q3_K_L.gguf | i1-Q3_K_L | 7.21 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q3_K_L.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q3_K_M.gguf | i1-Q3_K_M | 6.68 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q3_K_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q3_K_S.gguf | i1-Q3_K_S | 6.07 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q3_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q4_0.gguf | i1-Q4_0 | 7.81 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q4_0.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q4_1.gguf | i1-Q4_1 | 8.58 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q4_1.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q4_K_M.gguf | i1-Q4_K_M | 8.24 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q4_K_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q4_K_S.gguf | i1-Q4_K_S | 7.83 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q4_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q5_K_M.gguf | i1-Q5_K_M | 9.62 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q5_K_M.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q5_K_S.gguf | i1-Q5_K_S | 9.38 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q5_K_S.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.i1-Q6_K.gguf | i1-Q6_K | 11.1 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.i1-Q6_K.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.imatrix.gguf | imatrix | 7.42 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.imatrix.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.mmproj-Q8_0.gguf | mmproj-Q8_0 | 468 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.mmproj-Q8_0.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.mmproj-f16.gguf | mmproj-f16 | 878 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16.mmproj-f16.gguf) |
| Ministral-3-14B-Instruct-2512-BF16.mmproj-bf16.gguf | mmproj-bf16 | 879 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-14B-Instruct-2512-BF16-mmproj.gguf) |

## Ministral-3-8B-Instruct-2512 [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Ministral-3-8B-Instruct-2512-BF16.gguf | BF16 | 17 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.IQ4_XS.gguf | IQ4_XS | 4.73 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.IQ4_XS.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q2_K.gguf | Q2_K | 3.35 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q2_K.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q3_K_L.gguf | Q3_K_L | 4.57 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q3_K_L.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q3_K_M.gguf | Q3_K_M | 4.24 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q3_K_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q3_K_S.gguf | Q3_K_S | 3.87 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q3_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q4_K_M.gguf | Q4_K_M | 5.2 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q4_K_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q4_K_S.gguf | Q4_K_S | 4.95 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q4_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q5_K_M.gguf | Q5_K_M | 6.06 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q5_K_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q5_K_S.gguf | Q5_K_S | 5.92 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q5_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q6_K.gguf | Q6_K | 6.97 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q6_K.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.Q8_0.gguf | Q8_0 | 9.03 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.Q8_0.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ1_M.gguf | i1-IQ1_M | 2.27 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ1_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ1_S.gguf | i1-IQ1_S | 2.12 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ1_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_M.gguf | i1-IQ2_M | 3.11 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_S.gguf | i1-IQ2_S | 2.9 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_XS.gguf | i1-IQ2_XS | 2.75 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_XS.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_XXS.gguf | i1-IQ2_XXS | 2.53 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ2_XXS.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_M.gguf | i1-IQ3_M | 3.99 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_S.gguf | i1-IQ3_S | 3.89 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_XS.gguf | i1-IQ3_XS | 3.71 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_XS.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_XXS.gguf | i1-IQ3_XXS | 3.46 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ3_XXS.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ4_NL.gguf | i1-IQ4_NL | 4.94 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ4_NL.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-IQ4_XS.gguf | i1-IQ4_XS | 4.7 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-IQ4_XS.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q2_K.gguf | i1-Q2_K | 3.35 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q2_K.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q2_K_S.gguf | i1-Q2_K_S | 3.15 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q2_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q3_K_L.gguf | i1-Q3_K_L | 4.57 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q3_K_L.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q3_K_M.gguf | i1-Q3_K_M | 4.24 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q3_K_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q3_K_S.gguf | i1-Q3_K_S | 3.87 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q3_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q4_0.gguf | i1-Q4_0 | 4.94 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q4_0.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q4_1.gguf | i1-Q4_1 | 5.42 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q4_1.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q4_K_M.gguf | i1-Q4_K_M | 5.2 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q4_K_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q4_K_S.gguf | i1-Q4_K_S | 4.95 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q4_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q5_K_M.gguf | i1-Q5_K_M | 6.06 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q5_K_M.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q5_K_S.gguf | i1-Q5_K_S | 5.92 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q5_K_S.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.i1-Q6_K.gguf | i1-Q6_K | 6.97 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.i1-Q6_K.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.imatrix.gguf | imatrix | 5.33 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.imatrix.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.mmproj-Q8_0.gguf | mmproj-Q8_0 | 457 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.mmproj-Q8_0.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.mmproj-f16.gguf | mmproj-f16 | 857 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.mmproj-f16.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.mmproj-f32.gguf | mmproj-f32 | 1.71 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16.mmproj-f32.gguf) |
| Ministral-3-8B-Instruct-2512-BF16.mmproj-bf16.gguf | mmproj-bf16 | 858 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-8B-Instruct-2512-BF16-mmproj.gguf) |

## Ministral-3-3B-Instruct-2512 [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Ministral-3-3B-Instruct-2512-BF16.gguf | BF16 | 6.87 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.F32.gguf | F32 | 13.7 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.F32.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.IQ4_XS.gguf | IQ4_XS | 1.97 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.IQ4_XS.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q2_K.gguf | Q2_K | 1.46 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q2_K.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q3_K_L.gguf | Q3_K_L | 1.93 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q3_K_L.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q3_K_M.gguf | Q3_K_M | 1.8 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q3_K_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q3_K_S.gguf | Q3_K_S | 1.64 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q3_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q4_K_M.gguf | Q4_K_M | 2.15 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q4_K_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q4_K_S.gguf | Q4_K_S | 2.05 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q4_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q5_K_M.gguf | Q5_K_M | 2.47 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q5_K_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q5_K_S.gguf | Q5_K_S | 2.42 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q5_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q6_K.gguf | Q6_K | 2.82 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q6_K.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.Q8_0.gguf | Q8_0 | 3.65 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.Q8_0.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ1_M.gguf | i1-IQ1_M | 998 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ1_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ1_S.gguf | i1-IQ1_S | 938 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ1_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_M.gguf | i1-IQ2_M | 1.32 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_S.gguf | i1-IQ2_S | 1.24 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_XS.gguf | i1-IQ2_XS | 1.19 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_XS.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_XXS.gguf | i1-IQ2_XXS | 1.1 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ2_XXS.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_M.gguf | i1-IQ3_M | 1.7 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_S.gguf | i1-IQ3_S | 1.65 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_XS.gguf | i1-IQ3_XS | 1.58 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_XS.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_XXS.gguf | i1-IQ3_XXS | 1.45 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ3_XXS.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ4_NL.gguf | i1-IQ4_NL | 2.05 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ4_NL.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-IQ4_XS.gguf | i1-IQ4_XS | 1.96 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-IQ4_XS.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q2_K.gguf | i1-Q2_K | 1.46 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q2_K.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q2_K_S.gguf | i1-Q2_K_S | 1.37 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q2_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q3_K_L.gguf | i1-Q3_K_L | 1.93 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q3_K_L.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q3_K_M.gguf | i1-Q3_K_M | 1.8 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q3_K_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q3_K_S.gguf | i1-Q3_K_S | 1.64 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q3_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q4_0.gguf | i1-Q4_0 | 2.05 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q4_0.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q4_1.gguf | i1-Q4_1 | 2.23 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q4_1.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q4_K_M.gguf | i1-Q4_K_M | 2.15 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q4_K_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q4_K_S.gguf | i1-Q4_K_S | 2.05 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q4_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q5_K_M.gguf | i1-Q5_K_M | 2.47 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q5_K_M.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q5_K_S.gguf | i1-Q5_K_S | 2.42 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q5_K_S.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.i1-Q6_K.gguf | i1-Q6_K | 2.82 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.i1-Q6_K.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.imatrix.gguf | imatrix | 3.01 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.imatrix.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.mmproj-Q8_0.gguf | mmproj-Q8_0 | 448 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.mmproj-Q8_0.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.mmproj-f16.gguf | mmproj-f16 | 840 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.mmproj-f16.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.mmproj-f32.gguf | mmproj-f32 | 1.68 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16.mmproj-f32.gguf) |
| Ministral-3-3B-Instruct-2512-BF16.mmproj-bf16.gguf | mmproj-bf16 | 842 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Instruct-2512-AIO-GGUF/blob/main/Ministral-3-3B-Instruct-2512-BF16-mmproj.gguf) |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)