---
dataset_info:
- config_name: challenge
  features:
  - name: id
    dtype: string
  - name: question
    dtype: string
  - name: choices
    struct:
    - name: label
      sequence: string
    - name: text
      sequence: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 429732
    num_examples: 1167
  download_size: 220849
  dataset_size: 429732
- config_name: easy
  features:
  - name: id
    dtype: string
  - name: question
    dtype: string
  - name: choices
    struct:
    - name: label
      sequence: string
    - name: text
      sequence: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 734350
    num_examples: 2376
  download_size: 370074
  dataset_size: 734350
configs:
- config_name: challenge
  data_files:
  - split: test
    path: challenge/test-*
- config_name: easy
  data_files:
  - split: test
    path: easy/test-*
license: cc-by-sa-4.0
task_categories:
- question-answering
language:
- ko
pretty_name: Ko-ARC
---

> Note: Evaluation code and task configurations for this benchmark are available in the [`evaluation_code`](https://github.com/mcrl/korean_benchmarks/tree/main/evaluation_code) directory of the [Korean Benchmark Suite GitHub repository](https://github.com/mcrl/korean_benchmarks). The evaluation setup is built on the Language Model Evaluation Harness and supports standardized model assessment.

# Dataset Card for Ko-ARC

## Dataset Summary
Ko-ARC is a Korean adaptation of the [AI2 Reasoning Challenge (ARC)](https://huggingface.co/datasets/allenai/ai2_arc) dataset. 
It consists of multiple-choice science questions designed to assess reasoning and factual knowledge at the elementary and middle school levels. 
The dataset is split into two subsets — *easy* and *challenge* — and has been carefully translated, corrected, and culturally localized to support evaluation of Korean language models.

These are divided into:

- **Easy set**: 2,376 examples  
- **Challenge set**: 1,167 examples  

Each question is a 4-way multiple-choice item (A–D), assessing factual recall and reasoning in natural science. 

## Supported Tasks and Benchmarks

**Task**: Multiple-choice Question Answering (Science Knowledge)

Ko-ARC evaluates a language model's ability to:
- Understand and reason over grade-school level science content
- Choose the correct answer from multiple plausible choices
- Operate effectively in Korean-language educational contexts

## Languages

- ko (Korean)

---

## Dataset Structure

### Dataset Instance (Ko-ARC-Easy)
```json
{
  "id": "Mercury_417466",
  "question": "다음 중 광합성이 대부분의 먹이 그물의 기초가 되는 이유를 가장 잘 설명하는 것은 무엇인가요?",
  "choices": {
    "text": [
      "햇빛은 거의 모든 생태계의 에너지원임",
      "대부분의 생태계는 물속이 아닌 육지에서 발견됨",
      "이산화탄소는 다른 가스보다 가용성이 높음",
      "모든 생태계의 생산자는 식물임"
    ],
    "label": ["A", "B", "C", "D"]
  },
  "answerKey": "A"
}

```

### Data Fields

- `id`: A unique identifier for each question.
- `question`: The science question presented in Korean.
- `choices`: A dictionary of multiple answer choices and their corresponding labels.
- `answerKey`: The label of the correct answer.

### Data Splits

- Single evaluation set (`test` set)   
  - Easy Set: 2,376 questions  
  - Challenge Set: 1,167 questions
    - The number of challenge set is reduced compared to the original [ARC](https://huggingface.co/datasets/allenai/ai2_arc) dataset, because we eliminated duplicated data instances. 

---

## Dataset Creation

### Translation Process

The original ARC dataset was translated into Korean following a four-stage pipeline:

#### 1. Initial Translation
- Used [DeepL API](https://www.deepl.com/ko/products/api) to machine translate English questions into Korean.

#### 2. Correction
Domain experts reviewed and corrected:
- Errors in the original English dataset (e.g., typos, mislabeled answers, duplicates).
  - For example, `LEAP__8_10365` and `LEAP_2000_8_2` in the `ARC-Challenge` test set are duplicates, differing only in the phrasing of “one centimeter” vs. “1 centimeter.”
- Unnatural literal translations and mistranslations.
- Inconsistent tone and formality.
  - Standardizing expression styles and question endings for clarity and fluency in Korean (e.g., ending questions with “무엇일까요?”, etc).
- Incoherent or ambiguous phrasing in Korean.
- Deleting irrelevant or erroneous content in the original dataset   
  - For example, “27” in Which of the 27 following is the best use of a robot?, `MCAS_2005_8_27` in `ARC-Easy` test set.

#### 3. Localization
Localized content to reflect Korean cultural and linguistic context by:
- Replacing foreign names, units, and phrasing with equivalents appropriate for Korean science education.

#### 4. Cross-review
- An independent reviewer verified the full dataset, correcting missed errors from earlier stages.

---

## Additional Information

### Llicensing Information
This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

### Citation Information

#### Our Citation Information
```
@inproceedings{
so2026constructing,
title={Constructing Korean Benchmark Suite for Reliable Evaluation of Foundation Models},
author={Yeonkyoung So and Jongmin Kim and Sungmok Jung and Gyuseong Lee and Sangho Kim and Jongyeon Park and Joonhak Lee and Seho Pyo and Gyeongje Cho and Seorin Kim and Jisoo Kim and Suyoung Park and Hyunji M. Park and Yelim Ahn and Yeongho Seo and Jaejin Lee},
booktitle={ICML 2026 Workshop on Combining Theory and Benchmarks: Towards A Virtuous Cycle to Understand and Guarantee Foundation Model Performance},
year={2026},
url={https://openreview.net/forum?id=oJ3rhISSqO}
}
```

#### Original Dataset Citation Information
```
@article{allenai:arc,
      author    = {Peter Clark  and Isaac Cowhey and Oren Etzioni and Tushar Khot and
                    Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
      title     = {Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
      journal   = {arXiv:1803.05457v1},
      year      = {2018},
}

```

### Contact Information
If you find something wrong or have question about the dataset, contact snullm@aces.snu.ac.kr. 