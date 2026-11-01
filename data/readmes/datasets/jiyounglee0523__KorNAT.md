---
configs:
- config_name: Common Knowledge (Eng)
  data_files:
  - split: test
    path: Common Knowledge (Eng)/test-*
- config_name: Common Knowledge (Kor)
  data_files:
  - split: test
    path: Common Knowledge (Kor)/test-*
- config_name: Social Values (Eng)
  data_files:
  - split: test
    path: Social Values (Eng)/test-*
- config_name: Social Values (Kor)
  data_files:
  - split: test
    path: Social Values (Kor)/test-*
license: cc-by-nc-2.0
task_categories:
- multiple-choice
language:
- ko
- en
tags:
- national-alignment
size_categories:
- 10<n<12
dataset_info:
- config_name: Common Knowledge (Eng)
  features:
  - name: Category
    dtype: string
  - name: SubCategory
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
  splits:
  - name: test
    num_bytes: 7045
    num_examples: 14
  download_size: 10118
  dataset_size: 7045
- config_name: Common Knowledge (Kor)
  features:
  - name: Category
    dtype: string
  - name: SubCategory
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
  splits:
  - name: test
    num_bytes: 5113677
    num_examples: 10000
  download_size: 2413706
  dataset_size: 5113677
- config_name: Social Values (Eng)
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
  splits:
  - name: test
    num_bytes: 4722
    num_examples: 10
  download_size: 8784
  dataset_size: 4722
- config_name: Social Values (Kor)
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
  splits:
  - name: test
    num_bytes: 1961367
    num_examples: 4000
  download_size: 953776
  dataset_size: 1961367
---
# KorNAT (**Kor**ean **N**ational **A**lignment **T**est)
When deploying LLMs in a specific country, it is essential to ensure that the model is aware of that country’s culture and basic knowledge, so called _national alignment_.
We construct KorNAT (**Kor**ean **N**ational **A**lignment **T**est), the first benchmark that measures national alignment with South Korea from _social values_ and _common knowledge_.

- 📄 **Paper**: [KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge](https://arxiv.org/abs/2402.13605)
- 💻 **Code**: [github.com/jiyounglee-0523/KorNAT](https://github.com/jiyounglee-0523/KorNAT)
- 🏆 **Leaderboard**: [huggingface.co/spaces/jiyounglee0523/leaderboard](https://huggingface.co/spaces/jiyounglee0523/leaderboard)

### Social Value Dataset (4K Samples)
Social values refer to the collective viewpoints of a nation’s citizens on critical issues to their society.
The questions are made upon keywords extracted from monthly social conflict reports and the last 12 months of news articles.
All questions have undergone two rounds of human revisions to ensure high quality and elaborateness.
We obtained the ground truth label distribution by surveying people, receiving an average of 219 responses per question from a total of 6,174 Korean citizens.

### Common Knowledge Dataset (10K Samples)
Common knowledge refers to common knowledge broadly recognized and understood by the populace, often considered as basic knowledge.
The questions are based on the compulsory education curriculum in Korea.

## Citation
```bibtex
@inproceedings{lee2024kornat,
  title={KorNAT: LLM alignment benchmark for Korean social values and common knowledge},
  author={Lee, Jiyoung and Kim, Minwoo and Kim, Seungho and Kim, Junghwan and Won, Seunghyun and Lee, Hwaran and Choi, Edward},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
  pages={11177--11213},
  year={2024}
}
```

## Contact
For any questions, feel free to contact the email address below :)
```
jiyounglee0523@kaist.ac.kr
```
