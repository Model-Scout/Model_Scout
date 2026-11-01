---
configs:
- config_name: Common Knowledge
  data_files:
  - split: test
    path: KorNAT/common-knowledge-test.csv
- config_name: Social Values
  data_files:
  - split: test
    path: KorNAT/social-values-test.csv
dataset_info:
- config_name: Common Knowledge
  features:
  - name: Category
    dtype: string
  - name: Subcategory
    dtype: string
  - name: Question
    dtype: string
  - name: A
    dtype: string
  - name: B
    dtype: string
  - name: C
    dtype: string
  - name: D
    dtype: string
  - name: Answer
    dtype: string
  - name: Type
    dtype: string
  splits:
  - name: test
    num_examples: 6007
- config_name: Social Values
  features:
  - name: Category
    dtype: string
  - name: Question
    dtype: string
  - name: A
    dtype: string
  - name: B
    dtype: string
  - name: C
    dtype: string
  - name: D
    dtype: string
  - name: E
    dtype: string
  - name: Answer
    dtype: string
  splits:
  - name: test
    num_examples: 4000
license: cc-by-nc-2.0
task_categories:
- multiple-choice
language:
- ko
tags:
- national-alignment
size_categories:
- 1K<n<10K
---
# KorNAT (**Kor**ean **N**ational **A**lignment **T**est)
When deploying LLMs in a specific country, it is essential to ensure that the model is aware of that country’s culture and basic knowledge, so called _national alignment_. 
We construct KorNAT (**Kor**ean **N**ational **A**lignment **T**est), the first benchmark that measures national alignment with South Korea from _social values_ and _common knowledge_.

This repository provides the Korean KorNAT data (social values and common knowledge).

Link to Paper: [KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge](https://arxiv.org/abs/2402.13605)

### Social Value Dataset
Social values refer to the collective viewpoints of a nation’s citizens on critical issues to their society. 
The questions are made upon keywords extracted from monthly social conflict reports and the last 12 months of news articles.
All questions have undergone two rounds of human revisions to ensure high quality and elaborateness.
We obtained the ground truth label distribution by surveying people, receiving an average of 219 responses per question from a total of 6,174 Korean citizens.
`Answer` holds the ground-truth agreement distribution over the five options (values rounded to 2 decimals).

### Common Knowledge Dataset
Common knowledge refers to common knowledge broadly recognized and understood by the populace, often considered as basic knowledge. 
The questions are based on the compulsory education curriculum in Korea.
Columns: `Category`, `Subcategory`, `Question`, `A`–`D`, `Answer` (correct option A–D), `Type` (`knowledge` / `two step reasoning`).

## Citation
```
@article{lee2024kornat,
  title={KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge},
  author={Lee, Jiyoung and Kim, Minwoo and Kim, Seungho and Kim, Junghwan and Won, Seunghyun and Lee, Hwaran and Choi, Edward},
  journal={arXiv preprint arXiv:2402.13605},
  year={2024}
}
```

## Contact
For any questions, feel free to contact the email address below :)
```
mwkim@selectstar.ai
jiyounglee0523@kaist.ac.kr
```
