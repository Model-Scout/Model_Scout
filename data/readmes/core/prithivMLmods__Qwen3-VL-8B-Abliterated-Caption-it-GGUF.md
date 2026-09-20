---
license: apache-2.0
language:
- en
- zh
- th
base_model:
- prithivMLmods/Qwen3-VL-8B-Abliterated-Caption-it
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- text-generation-inference
- uncensored
- image-captioning
- vlm
- visual-understanding
- caption
- image-to-text
---
# **Qwen3-VL-8B-Abliterated-Caption-it-GGUF**

> The Qwen3-VL-8B-Abliterated-Caption-it model is a fine-tuned version of Qwen3-VL-8B-Instruct, tailored for Abliterated Captioning / Uncensored Image Captioning. This variant is designed to generate highly detailed and descriptive captions across a broad range of visual categories, including images with complex, sensitive, or nuanced content—across varying aspect ratios and resolutions.

## Model Files

| File Name | Quant Type | File Size |
| - | - | - |
| Qwen3-VL-8B-Abliterated-Caption-it.f16.gguf | F16 | 16.4 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q2_K.gguf | Q2_K | 3.28 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q3_K_L.gguf | Q3_K_L | 4.43 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q3_K_M.gguf | Q3_K_M | 4.12 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q3_K_S.gguf | Q3_K_S | 3.77 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q4_K_M.gguf | Q4_K_M | 5.03 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q4_K_S.gguf | Q4_K_S | 4.8 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q5_K_M.gguf | Q5_K_M | 5.85 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q5_K_S.gguf | Q5_K_S | 5.72 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q6_K.gguf | Q6_K | 6.73 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.Q8_0.gguf | Q8_0 | 8.71 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.IQ4_XS.gguf | IQ4_XS | 4.59 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ1_M.gguf | i1-IQ1_M | 2.26 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ1_S.gguf | i1-IQ1_S | 2.12 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ2_M.gguf | i1-IQ2_M | 3.05 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ2_S.gguf | i1-IQ2_S | 2.86 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ2_XS.gguf | i1-IQ2_XS | 2.7 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ2_XXS.gguf | i1-IQ2_XXS | 2.49 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ3_M.gguf | i1-IQ3_M | 3.9 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ3_S.gguf | i1-IQ3_S | 3.79 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ3_XS.gguf | i1-IQ3_XS | 3.63 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ3_XXS.gguf | i1-IQ3_XXS | 3.37 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ4_NL.gguf | i1-IQ4_NL | 4.79 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-IQ4_XS.gguf | i1-IQ4_XS | 4.56 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q2_K.gguf | i1-Q2_K | 3.28 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q2_K_S.gguf | i1-Q2_K_S | 3.08 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q3_K_L.gguf | i1-Q3_K_L | 4.43 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q3_K_M.gguf | i1-Q3_K_M | 4.12 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q3_K_S.gguf | i1-Q3_K_S | 3.77 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q4_0.gguf | i1-Q4_0 | 4.79 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q4_1.gguf | i1-Q4_1 | 5.25 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q4_K_M.gguf | i1-Q4_K_M | 5.03 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q4_K_S.gguf | i1-Q4_K_S | 4.8 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q5_K_M.gguf | i1-Q5_K_M | 5.85 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q5_K_S.gguf | i1-Q5_K_S | 5.72 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.i1-Q6_K.gguf | i1-Q6_K | 6.73 GB |
| Qwen3-VL-8B-Abliterated-Caption-it.imatrix.gguf | imatrix | 5.35 MB |
| Qwen3-VL-8B-Abliterated-Caption-it.mmproj-Q8_0.gguf | mmproj-Q8_0 | 752 MB |
| Qwen3-VL-8B-Abliterated-Caption-it.mmproj-f16.gguf | mmproj-f16 | 1.16 GB |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)