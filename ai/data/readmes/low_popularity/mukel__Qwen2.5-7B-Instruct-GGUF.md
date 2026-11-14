---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF/blob/main/LICENSE
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
quantized_by: mukel
tags:
- chat
- qwen
---

# GGUF models for qwen2.java 
Pure .gguf Q4_0 and Q8_0 quantizations of Qwen 2.5 models, ready to consume by `qwen2.java`.

In the wild, Q8_0 quantizations are fine, but Q4_0 quantizations are rarely pure e.g. the token embeddings are quantized with Q6_K, instead of Q4_0.  
A pure Q4_0 quantization can be generated from a high precision (F32, F16, BFLOAT16) .gguf source with the llama-quantize utility from llama.cpp as follows:

```
./llama-quantize --pure ./Qwen-2.5-7B-Instruct-BF16.gguf ./Qwen-2.5-7B-Instruct-Q4_0.gguf Q4_0
```

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2.5/), [GitHub](https://github.com/QwenLM/Qwen2.5), and [Documentation](https://qwen.readthedocs.io/en/latest/).
