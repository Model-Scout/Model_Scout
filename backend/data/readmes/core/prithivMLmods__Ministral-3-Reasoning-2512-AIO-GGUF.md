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
base_model:
- mistralai/Ministral-3-3B-Reasoning-2512
- mistralai/Ministral-3-8B-Reasoning-2512
- mistralai/Ministral-3-14B-Reasoning-2512
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- text-generation-inference
- llama.cpp
- f32
---

# **Ministral-3-Reasoning-2512-AIO-GGUF**

> The [Ministral 3 Reasoning](https://huggingface.co/collections/mistralai/ministral-3) models (3B, 8B, and 14B variants from mistralai) are post-trained vision-language models specialized for advanced reasoning tasks like math, coding, and STEM applications, featuring a core language model (3.4B, 8.4B, or 13.5B parameters) paired with a 0.4B vision encoder for multimodal image analysis, supporting a 256k context window, multilingual capabilities, and edge deployment on hardware as low as 24GB VRAM/RAM when quantized (BF16 precision). Optimized with a recommended temperature of 0.7 and top_p=0.95 for reasoning, they use a distinctive chat template encouraging structured [THINK] inner monologue drafts in Markdown/LaTeX before final responses, enabling step-by-step problem-solving while maintaining strong performance in benchmarks like AIME25 (0.721 for 3B) and GPQA Diamond. Ideal for resource-efficient local inference via vLLM or Transformers, these Apache 2.0-licensed models excel in agentic workflows, function calling, and complex multimodal reasoning under constrained environments.

## Ministral-3-14B-Reasoning-2512 [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Ministral-3-14B-Reasoning-2512-BF16.gguf | BF16 | 27 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-14B-Reasoning-2512-BF16.gguf) |
| Ministral-3-14B-Reasoning-2512-Q4_K_M.gguf | Q4_K_M | 8.24 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-14B-Reasoning-2512-Q4_K_M.gguf) |
| Ministral-3-14B-Reasoning-2512-Q5_K_M.gguf | Q5_K_M | 9.62 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-14B-Reasoning-2512-Q5_K_M.gguf) |
| Ministral-3-14B-Reasoning-2512-Q8_0.gguf | Q8_0 | 14.4 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-14B-Reasoning-2512-Q8_0.gguf) |
| Ministral-3-14B-Reasoning-2512-BF16-mmproj.gguf | BF16-mmproj | 879 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-14B-Reasoning-2512-BF16-mmproj.gguf) |

## Ministral-3-8B-Reasoning-2512 [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Ministral-3-8B-Reasoning-2512-BF16.gguf | BF16 | 17 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-8B-Reasoning-2512-BF16.gguf) |
| Ministral-3-8B-Reasoning-2512-Q4_K_M.gguf | Q4_K_M | 5.2 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-8B-Reasoning-2512-Q4_K_M.gguf) |
| Ministral-3-8B-Reasoning-2512-Q5_K_M.gguf | Q5_K_M | 6.06 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-8B-Reasoning-2512-Q5_K_M.gguf) |
| Ministral-3-8B-Reasoning-2512-Q8_0.gguf | Q8_0 | 9.03 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-8B-Reasoning-2512-Q8_0.gguf) |
| Ministral-3-8B-Reasoning-2512-BF16-mmproj.gguf | BF16-mmproj | 858 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-8B-Reasoning-2512-BF16-mmproj.gguf) |

## Ministral-3-3B-Reasoning-2512 [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Ministral-3-3B-Reasoning-2512-BF16.gguf | BF16 | 6.87 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-3B-Reasoning-2512-BF16.gguf) |
| Ministral-3-3B-Reasoning-2512-Q4_K_M.gguf | Q4_K_M | 2.15 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-3B-Reasoning-2512-Q4_K_M.gguf) |
| Ministral-3-3B-Reasoning-2512-Q5_K_M.gguf | Q5_K_M | 2.47 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-3B-Reasoning-2512-Q5_K_M.gguf) |
| Ministral-3-3B-Reasoning-2512-Q8_0.gguf | Q8_0 | 3.65 GB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-3B-Reasoning-2512-Q8_0.gguf) |
| Ministral-3-3B-Reasoning-2512-BF16-mmproj.gguf | BF16-mmproj | 842 MB | [Download](https://huggingface.co/prithivMLmods/Ministral-3-Reasoning-2512-AIO-GGUF/blob/main/Ministral-3-3B-Reasoning-2512-BF16-mmproj.gguf) |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)