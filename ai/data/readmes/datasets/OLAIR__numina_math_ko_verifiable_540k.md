---
dataset_info:
  features:
  - name: original
    dtype: string
  - name: reference
    dtype: string
  - name: problem
    dtype: string
  - name: source
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 873006977
    num_examples: 539149
  download_size: 452093917
  dataset_size: 873006977
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
language:
- ko
---

# Dataset Card: OLAIR/numina_math_ko_verifiable_540k

**Overview:**  
A paired dataset of math questions (translated into Korean using GPT-4o-mini) and verifiable answers. Intended for RL training (e.g., GRPO) and mathematical reasoning tasks.

**Sources:**  
- **Questions:** Derived from [AI-MO/NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT)  
- **Answers:** Extracted from [flatlander1024/numinamath_verifiable_cleaned](https://huggingface.co/datasets/flatlander1024/numinamath_verifiable_cleaned?row=15)

**Key Points:**  
- **Translation:** No-cleansing version; translations may contain errors.  
- **Usage:** Suitable for RL and language model training in math-related tasks.

**Contact:**  
```
spthsrbwls123@yonsei.ac.kr
```