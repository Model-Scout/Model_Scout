---
language:
- ko
- en
license: cc-by-nc-sa-4.0
size_categories:
- n<1K
task_categories:
- question-answering
tags:
- math
- QA
- Korean
- Exam
configs:
- config_name: default
  data_files:
  - split: 2022_math
    path: data/2022_math-*
  - split: 2023_math
    path: data/2023_math-*
  - split: 2024_math
    path: data/2024_math-*
  - split: 2025_math
    path: data/2025_math-*
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: name
    dtype: string
  - name: problem
    dtype: string
  - name: answer
    dtype: int64
  - name: score
    dtype: int64
  - name: review
    dtype: string
  splits:
  - name: 2022_math
    num_bytes: 24446
    num_examples: 46
  - name: 2023_math
    num_bytes: 22830
    num_examples: 46
  - name: 2024_math
    num_bytes: 22654
    num_examples: 46
  - name: 2025_math
    num_bytes: 21130
    num_examples: 46
  download_size: 55992
  dataset_size: 91060
---

# KoreanSAT Benchmark


---
### Current Topics over years

#### Math
- **o1-preview**
| Year | 2022 | 2023 | 2024|2025
|------|-----------|-----------|-----------|-----------|
| General |        62   |    50       |    62       |54  |
| Probability & Statistics |    22       |    20       |     26      | 22|
| Calculus |       18    |       18    |        15   | 19|
| Geometry |       15    |       22    |      18     |19 |
| General+Prob. |	84 | 70 | 88 | 76 |
| General+Calc. |	80 | 68 | 77 | 73 |
| General+Geom. |	77 | 72 | 80 | 73 |
| **Average** |	**80.3** |	**70**|	**81.7** |	**74**|



---
