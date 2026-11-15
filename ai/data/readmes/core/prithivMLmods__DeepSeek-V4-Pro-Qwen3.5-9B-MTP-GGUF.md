---
language:
- en
- zh
- ko
- ja
- es
- ru
tags:
- mtp
- text-generation-inference
- llama-cpp
- transformers
- unsloth
- qwen3_5
- reasoning
- distillation
- deepseek
- sft
- rl
- gspo
- math
- stem
- tool-use
- function-calling
- speculative-decoding
- nvidia-blackwell
- rtx-pro-6000
- SM120
- GB202
- B200
- B300
- FP4
- blackwell
- Qwen3.5
- GPTQ
library_name: transformers
base_model:
- Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B
pipeline_tag: image-text-to-text
license: apache-2.0
---

# **DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF**

> **DeepSeek-V4-Pro-Qwen3.5-9B** is Jackrong's 9B reasoning model, a fine-tune of Qwen3.5-9B distilled from DeepSeek-V4-Pro in Max Effect mode. Training used about 250K math and STEM samples. It ran SFT and then a light GSPO RL stage, with no coding data in either, and the card reports small gains in programming and tool use as preliminary cross-domain transfer. It scores 94.50% on GSM8K (four-run mean on the NVFP4 build under vLLM). It also averages 90.53% on a 1,500-question MMLU-Pro Math, Physics and Chemistry sample, 0.93 points above Qwen3.5-9B (89.60%), while using about 36% fewer reasoning tokens per correct answer. Those MMLU-Pro runs used MTP-Q8_0 GGUF in llama.cpp, so the two benchmarks used different builds. The card also claims a terse single-letter answer in 97.2% of cases when asked, against 37.3% for Qwen3.5-9B. The benchmarks are the author's own, on random samples rather than full subsets. The card calls it an experimental community model whose outputs need verification. It was built with Unsloth in collaboration with Kyle Hessling, whose Star Skip game demo is showcased, and MTP GGUF and vision projector files are in a separate repo. The weights are Apache 2.0.

> [!NOTE]
> MTP — Speculative Decoding: Yes

> [!NOTE]
Multi-Token Prediction (MTP) GGUF is a specialized GGUF model file format extension that integrates speculative decoding directly into the model weights to significantly accelerate local inference.  Unlike traditional speculative decoding which requires a separate, smaller "draft" model, MTP GGUF files include additional output heads within the main model architecture that predict multiple future tokens in a single forward pass.

> [!NOTE]
NVFP4-GPTQ Version: [DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ) | NVFP4-GPTQ-GGUF Version: [DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ-GGUF](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ-GGUF)

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| DeepSeek-V4-Pro-Qwen3.5-9B.BF16.gguf | BF16 | 18.4 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.BF16.gguf) | Full BF16 weights. Highest quality, largest file size. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q3_K_L.gguf | Q3_K_L | 5.05 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q3_K_L.gguf) | Lower quality but usable, good for low RAM availability. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q3_K_M.gguf | Q3_K_M | 4.74 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q3_K_M.gguf) | Low quality. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q4_K_M.gguf | Q4_K_M | 5.78 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q4_K_M.gguf) | Good quality, default size for most use cases, *recommended*. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q4_K_S.gguf | Q4_K_S | 5.49 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q4_K_S.gguf) | Slightly lower quality with more space savings, *recommended*. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q5_K_M.gguf | Q5_K_M | 6.64 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q5_K_M.gguf) | High quality, *recommended*. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q5_K_S.gguf | Q5_K_S | 6.47 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q5_K_S.gguf) | High quality, *recommended*. |
| DeepSeek-V4-Pro-Qwen3.5-9B.Q6_K.gguf | Q6_K | 7.56 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.Q6_K.gguf) | Very high quality, near perfect, *recommended*. |
| DeepSeek-V4-Pro-Qwen3.5-9B.mmproj-bf16.gguf | mmproj-bf16 | 922 MB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.mmproj-bf16.gguf) | Multimodal projection file in BF16 format. Used for vision/language models. |

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp

Quantized using llama.cpp by [prithivMLmods](https://huggingface.co/prithivMLmods).