---
license: other
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
base_model:
- LiquidAI/LFM2-2.6B-Exp
library_name: transformers
pipeline_tag: text-generation
tags:
- text-generation-inference
- llama.cpp
---

# **LFM2-2.6B-Exp-GGUF**

> LiquidAI/LFM2-2.6B-Exp is a 2.6 billion-parameter experimental language model from the LFM2 series, featuring a novel hybrid architecture that combines 10 double-gated short-range convolution blocks with 6 Grouped Query Attention (GQA) blocks for superior efficiency in edge AI and on-device deployment, achieving 3x faster training, 2x faster CPU decode/prefill than Qwen3, and top performance like 82.41% on GSM8K math reasoning and 79.56% on IFEval instruction following—outperforming larger models such as Llama 3.2-3B-Instruct and Gemma-3-4b-it. Optimized for multilingual support (English, Arabic, Chinese, French, German, Japanese, Korean, Spanish) with a 32K token context window, it uses Lfm2ForCausalLM architecture under LFM1.0 license, enabling conversational text generation on resource-constrained devices like smartphones, laptops, or vehicles via Transformers with low KV cache requirements. This post-trained checkpoint sets new standards in quality, speed, and memory efficiency for real-world AI applications across CPUs, GPUs, and NPUs.

## LFM2-2.6B-Exp [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| LFM2-2.6B-Exp.BF16.gguf | BF16 | 5.41 GB | [Download](https://huggingface.co/prithivMLmods/LFM2-2.6B-Exp-GGUF/blob/main/LFM2-2.6B-Exp.BF16.gguf) |
| LFM2-2.6B-Exp.F16.gguf | F16 | 5.41 GB | [Download](https://huggingface.co/prithivMLmods/LFM2-2.6B-Exp-GGUF/blob/main/LFM2-2.6B-Exp.F16.gguf) |
| LFM2-2.6B-Exp.F32.gguf | F32 | 10.8 GB | [Download](https://huggingface.co/prithivMLmods/LFM2-2.6B-Exp-GGUF/blob/main/LFM2-2.6B-Exp.F32.gguf) |
| LFM2-2.6B-Exp.Q8_0.gguf | Q8_0 | 2.88 GB | [Download](https://huggingface.co/prithivMLmods/LFM2-2.6B-Exp-GGUF/blob/main/LFM2-2.6B-Exp.Q8_0.gguf) |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)