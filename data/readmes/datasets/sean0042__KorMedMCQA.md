---
language:
- ko
license: cc-by-nc-2.0
size_categories:
- 10K<n<100K
task_categories:
- question-answering
configs:
- config_name: dentist
  data_files:
  - split: train
    path: dentist/train-*
  - split: dev
    path: dentist/dev-*
  - split: test
    path: dentist/test-*
  - split: fewshot
    path: dentist/fewshot-*
- config_name: doctor
  data_files:
  - split: train
    path: doctor/train-*
  - split: dev
    path: doctor/dev-*
  - split: test
    path: doctor/test-*
  - split: fewshot
    path: doctor/fewshot-*
- config_name: nurse
  data_files:
  - split: train
    path: nurse/train-*
  - split: dev
    path: nurse/dev-*
  - split: test
    path: nurse/test-*
  - split: fewshot
    path: nurse/fewshot-*
- config_name: pharm
  data_files:
  - split: train
    path: pharm/train-*
  - split: dev
    path: pharm/dev-*
  - split: test
    path: pharm/test-*
  - split: fewshot
    path: pharm/fewshot-*
tags:
- medical
dataset_info:
- config_name: dentist
  features:
  - name: subject
    dtype: string
  - name: year
    dtype: int64
  - name: period
    dtype: int64
  - name: q_number
    dtype: int64
  - name: question
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
  - name: answer
    dtype: int64
  - name: cot
    dtype: string
  splits:
  - name: train
    num_bytes: 116376
    num_examples: 297
  - name: dev
    num_bytes: 119727
    num_examples: 304
  - name: test
    num_bytes: 330325
    num_examples: 811
  - name: fewshot
    num_bytes: 4810
    num_examples: 5
  download_size: 374097
  dataset_size: 571238
- config_name: doctor
  features:
  - name: subject
    dtype: string
  - name: year
    dtype: int64
  - name: period
    dtype: int64
  - name: q_number
    dtype: int64
  - name: question
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
  - name: answer
    dtype: int64
  - name: cot
    dtype: string
  splits:
  - name: train
    num_bytes: 1137189
    num_examples: 1890
  - name: dev
    num_bytes: 111294
    num_examples: 164
  - name: test
    num_bytes: 315104
    num_examples: 435
  - name: fewshot
    num_bytes: 8566
    num_examples: 5
  download_size: 871530
  dataset_size: 1572153
- config_name: nurse
  features:
  - name: subject
    dtype: string
  - name: year
    dtype: int64
  - name: period
    dtype: int64
  - name: q_number
    dtype: int64
  - name: question
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
  - name: answer
    dtype: int64
  - name: cot
    dtype: string
  splits:
  - name: train
    num_bytes: 219983
    num_examples: 582
  - name: dev
    num_bytes: 110210
    num_examples: 291
  - name: test
    num_bytes: 327186
    num_examples: 878
  - name: fewshot
    num_bytes: 6324
    num_examples: 5
  download_size: 419872
  dataset_size: 663703
- config_name: pharm
  features:
  - name: subject
    dtype: string
  - name: year
    dtype: int64
  - name: period
    dtype: int64
  - name: q_number
    dtype: int64
  - name: question
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
  - name: answer
    dtype: int64
  - name: cot
    dtype: string
  splits:
  - name: train
    num_bytes: 272256
    num_examples: 632
  - name: dev
    num_bytes: 139900
    num_examples: 300
  - name: test
    num_bytes: 412847
    num_examples: 885
  - name: fewshot
    num_bytes: 6324
    num_examples: 5
  download_size: 504010
  dataset_size: 831327
---

# KorMedMCQA : Multi-Choice Question Answering Benchmark for Korean Healthcare Professional Licensing Examinations

We present KorMedMCQA, the first Korean Medical Multiple-Choice Question
Answering benchmark, derived from professional healthcare licensing
examinations conducted in Korea between 2012 and 2024. The dataset contains
7,469 questions from examinations for doctor, nurse, pharmacist, and dentist,
covering a wide range of medical disciplines. We evaluate the performance of 59
large language models, spanning proprietary and open-source models,
multilingual and Korean-specialized models, and those fine-tuned for clinical
applications. Our results show that applying Chain of Thought (CoT) reasoning
can enhance the model performance by up to 4.5% compared to direct answering
approaches. We also investigate whether MedQA, one of the most widely used
medical benchmarks derived from the U.S. Medical Licensing Examination, can
serve as a reliable proxy for evaluating model performance in other regions-in
this case, Korea. Our correlation analysis between model scores on KorMedMCQA
and MedQA reveals that these two benchmarks align no better than benchmarks
from entirely different domains (e.g., MedQA and MMLU-Pro). This finding
underscores the substantial linguistic and clinical differences between Korean
and U.S. medical contexts, reinforcing the need for region-specific medical QA
benchmarks. 

Paper : https://arxiv.org/abs/2403.01469

## Notice

We have made the following updates to the KorMedMCQA dataset:

1. **Dentist Exam**: Incorporated exam questions from 2021 to 2024.
2. **Updated Test Sets**: Added the 2024 exam questions for the doctor, nurse, and pharmacist test sets.
3. **Few-Shot Split**: Introduced a `fewshot` split, containing 5 shots from each validation set.
4. **Chain-of-Thought(CoT)**: In each exam's few-shot split (`cot` column), there is an answer with reasoning annotated by professionals


## Dataset Details

### Languages

Korean

### Subtask

```
from datasets import load_dataset
doctor = load_dataset(path = "sean0042/KorMedMCQA",name = "doctor")
nurse = load_dataset(path = "sean0042/KorMedMCQA",name = "nurse")
pharmacist = load_dataset(path = "sean0042/KorMedMCQA",name = "pharm")
dentist = load_dataset(path = "sean0042/KorMedMCQA",name = "dentist")
```

### Statistics

| Category                     | # Questions (Train/Dev/Test) |
|------------------------------|------------------------------|
| Doctor                       | 2,489 (1,890/164/435)        |
| Nurse                        | 1,751 (582/291/878)          |
| Pharmacist                   | 1,817 (632/300/885)          |
| Dentist                      | 1,412 (297/304/811)          |

### Data Fields


- `subject`: doctor, nurse, or pharm
- `year`: year of the examination
- `period`: period of the examination
- `q_number`: question number of the examination
- `question`: question
- `A`: First answer choice
- `B`: Second answer choice
- `C`: Third answer choice
- `D`: Fourth answer choice
- `E`: Fifth answer choice
- `cot` : Answer with reasoning annotated by professionals (only available in fewshot split)
- `answer` : Answer (1 to 5). 1 denotes answer A, and 5 denotes answer E


## Contact

```
sean0042@kaist.ac.kr
```