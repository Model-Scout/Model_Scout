---
license: apache-2.0
datasets:
- squarelike/sharegpt_deepl_ko_translation
language:
- en
- ko
pipeline_tag: translation
---

# Gugugo-koen-7B-V1.1-GGUF
Detail repo: [https://github.com/jwj7140/Gugugo](https://github.com/jwj7140/Gugugo)
![Gugugo](./logo.png)

**This is GGUF model from [squarelike/Gugugo-koen-7B-V1.1](https://huggingface.co/squarelike/Gugugo-koen-7B-V1.1)**

**Base Model**: [Llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b)

**Training Dataset**: [sharegpt_deepl_ko_translation](https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation).

I trained with 1x A6000 GPUs for 90 hours.

## **Prompt Template**
**KO->EN**
```
### 한국어: {sentence}</끝>
### 영어:
```
**EN->KO**
```
### 영어: {sentence}</끝>
### 한국어:
```