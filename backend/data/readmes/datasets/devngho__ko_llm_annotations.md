---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- ko
license: mit
source_datasets:
- HAERAE-HUB/KOREAN-WEBTEXT
- blueapple8259/c4-ko-cleaned-2
task_categories:
- text-classification
tags:
- synthetic
dataset_info:
  features:
  - name: text
    dtype: string
  - name: analysis
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: v3
    num_bytes: 2572557211.77768
    num_examples: 499896
  - name: v2.1
    num_bytes: 1509722708.3685167
    num_examples: 289288
  - name: v2
    num_bytes: 1509649645.8221369
    num_examples: 289274
  - name: v1
    num_bytes: 3456764386
    num_examples: 468616
  download_size: 4977797687
  dataset_size: 9048693951.968334
configs:
- config_name: v3
  data_files:
  - split: train
    path: data/v3-*
  default: true
- config_name: v2.1
  data_files:
  - split: train
    path: data/v2.1-*
- config_name: v2
  data_files:
  - split: train
    path: data/v2-*
- config_name: v1
  data_files:
  - split: train
    path: data/v1-*
---

## Dataset

이 데이터셋은 [fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)의 방법을 한국어에 적용하기 위해 만들어진 합성 데이터셋입니다.

v1과 v2는 퀄리티가 낮습니다. **v3을 사용**하는 것을 권장합니다.

This synthetic dataset was created to apply the methods of [fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) to Korean datasets.

v1 and v2 are of low quality. I recommend **using v3**.

### v1

- source: [HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT), sampled 500k
- analysis model: [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)
- 
- temperature: 0.5
- min_p: 0.1
- max_model_len: 8192
-
- generation time: ~42 hrs

### v2

- source: [blueapple8259/c4-ko-cleaned-2](https://huggingface.co/datasets/blueapple8259/c4-ko-cleaned-2), sampled 500k
- analysis model: [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)
- 
- temperature: 1.0
- min_p: 0.1
- max_model_len: 8192
-
- generation time: ~29 hrs (stopped during generation)

#### v2.1

- "Educational score: 3/10" 같은 출력이 3이 아닌 2(==round(1.5))처럼 올바르게 되도록 정정

### v3

- source: [blueapple8259/c4-ko-cleaned-2](https://huggingface.co/datasets/blueapple8259/c4-ko-cleaned-2), sampled 500k (==v2)
- analysis model: [Qwen/Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)
- 
- temperature: 0.5
- min_p: 0.1
- max_model_len: 8192
-
- generation time: ~56 hrs

<details>
  <summary>prompt</summary>
fineweb-edu 프롬프트에서 일관성과 한국 문화를 위해 수정

```
|im_start|>system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>
<|im_start|>user
You are tasked with evaluating the educational value of a Korean text extract for primary to grade school levels. Here's the text to analyze:

Use the following 5-point additive scoring system:

- 1 point: If the extract provides some basic information relevant to educational topics, even if it includes some irrelevant or non-academic content like advertisements and promotional material.
- 2 point: If the extract addresses certain elements pertinent to education but does not align closely with educational standards. It might mix educational content with non-educational material, offering a superficial overview of potentially useful topics, or presenting information in a disorganized manner and incoherent writing style.
- 3 point: If the extract is appropriate for educational use and introduces key concepts relevant to school curricula. It is coherent though it may not be comprehensive or could include some extraneous information. It may resemble an introductory section of a textbook or a basic tutorial that is suitable for learning but has notable limitations like treating concepts that are too complex for grade school students. 
- 4 point: If the extract highly relevant and beneficial for educational purposes for a level not higher than grade school, exhibiting a clear and consistent writing style. It could be similar to a chapter from a textbook or a tutorial, offering substantial educational content, including exercises and solutions, with minimal irrelevant information, and the concepts aren't too advanced for grade school students. The content is coherent, focused, and valuable for structured learning.
- 5 point: if the extract is outstanding in its educational value, perfectly suited for teaching either at primary school or grade school. It follows detailed reasoning, the writing style is easy to follow and offers profound and thorough insights into the subject matter, devoid of any non-educational or complex content.

Analyze the text, considering its relevance and appropriateness for Korean primary to grade school education.

The text extract:
{text}

After your analysis, provide:

1. A justification for your score in English (up to 100 words).
2. The final score, stated as "Educational score: X" (where X is the total points).

Present your justification before the final score.<|im_end|>
<|im_start|>assistant
```

</details>

### Compute Infrastructure

Google Cloud TPU, vLLM

#### Hardware

TPU v4-8

이 연구는 Google의 TPU Research Cloud [(TRC)](https://sites.research.google/trc/about/)의 Cloud TPU 제공으로 수행되었습니다. ⚡

This research was supported with Cloud TPUs from Google's TPU Research Cloud [(TRC)](https://sites.research.google/trc/about/).⚡