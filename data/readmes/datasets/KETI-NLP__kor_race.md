---
pretty_name: race
language:
- ko
size_categories:
- 1K<n<10K
task_categories:
- multiple-choice
task_ids:
- multiple-choice-qa
license: other
license_name: race
license_link: https://www.cs.cmu.edu/~glai1/data/race/
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: article
    dtype: string
  - name: answer
    dtype: string
  - name: question
    dtype: string
  - name: options
    sequence: string
  splits:
  - name: train
    num_bytes: 191129599
    num_examples: 87866
  - name: validation
    num_bytes: 10507580
    num_examples: 4887
  - name: test
    num_bytes: 10668488
    num_examples: 4934
  download_size: 46954865
  dataset_size: 212305667
---

# Dataset Card for race

## Licensing Information

http://www.cs.cmu.edu/~glai1/data/race/

1. RACE dataset is available for non-commercial research purpose only.

2. All passages are obtained from the Internet which is not property of Carnegie Mellon University. We are not responsible for the content nor the meaning of these passages.

3. You agree not to reproduce, duplicate, copy, sell, trade, resell or exploit for any commercial purpose, any portion of the contexts and any portion of derived data.

4. We reserve the right to terminate your access to the RACE dataset at any time.

## Source Data Citation INformation

```
@inproceedings{lai-etal-2017-race,
    title = "{RACE}: Large-scale {R}e{A}ding Comprehension Dataset From Examinations",
    author = "Lai, Guokun  and
      Xie, Qizhe  and
      Liu, Hanxiao  and
      Yang, Yiming  and
      Hovy, Eduard",
    booktitle = "Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D17-1082",
    doi = "10.18653/v1/D17-1082",
    pages = "785--794",
}
```