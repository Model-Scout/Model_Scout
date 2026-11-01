---
configs:
- config_name: kcd8_easy
  data_files:
  - split: test
    path: data/KCD8-easy-2.jsonl
- config_name: kcd8_medium
  data_files:
  - split: test
    path: data/KCD8-medium-2.jsonl
- config_name: kcd8_hard
  data_files:
  - split: test
    path: data/KCD8-hard-2.jsonl
- config_name: kcd8_merged
  data_files:
  - split: test
    path: data/KCD8-merged.jsonl
- config_name: atc_easy
  data_files:
  - split: dev
    path: data/atc_easy_dev.jsonl
  - split: test
    path: data/atc_easy_test.jsonl
- config_name: atc_medium
  data_files:
  - split: dev
    path: data/atc_medium_dev.jsonl
  - split: test
    path: data/atc_medium_test.jsonl
- config_name: atc_hard
  data_files:
  - split: dev
    path: data/atc_hard_dev.jsonl
  - split: test
    path: data/atc_hard_test.jsonl
license: cc-by-nc-3.0
task_categories:
- question-answering
language:
- ko
tags:
- medical
size_categories:
- 10K<n<100K
---

# **Warning: If there is some copyright issue, this dataset may be deleted.**

# KoMedConceptsQA

This is data that reproduces the work of paper [MedConceptsQA](https://arxiv.org/abs/2405.07348) by using **Korean medical codes**.

## Update

2024/08/29 19:08 KST: KCD8-merged version에 CoT를 추가하였습니다.

## Used data

- 제8차 한국표준질병·사인분류 (KCD-8) [통계분류포털](https://kssc.kostat.go.kr:8443/ksscNew_web/kssc/main/main.do?gubun=1#)

*Note: 해당 데이터는 '통계청'에서 '2020년'에 작성하여 공공누리 3유형으로 개방한 저작물입니다.*
*해당 데이터의 저작권 정책상 "형식의 변경"에 위 데이터가 크게 위반되었다고 판단되어 공지가 올 경우 데이터 사용이 금지될 수 있습니다.*

- ATC in original data [MedConceptsQA](https://huggingface.co/datasets/ofir408/MedConceptsQA)

Note: [건강보험심사평가원](https://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020002000100&brdScnBltNo=4&brdBltNo=11026&pageIndex=1&pageIndex2=1#none)에 제공되는 의약품 ATC 코드 정보의 경우, 변경 주기가 짧고 부정확한 부분이 있을 수 있다는 답변을 받았습니다.
따라서, 기존 데이터의 WHO ATC code 데이터를 사용합니다.

## KCD8 Method

- easy level: randomly chosen from all medical codes within the covabulary.
- medium level: options are satisfied the following condition; the part before '.' in the code is the same (ex. A01.0, A01.1, A01.2, A01.4)
- hard level: options are satisfied the following condition; the part before '.' in the code and the next number are the same (ex. A41.50, A41.51, A41.52, A41.53)
- merged: For the same code, choose only one which is the most difficult level

### Statistics

| Category                     | # Questions (Test)          |
|------------------------------|------------------------------|
| kcd8_easy                         | 17,320                       |
| kcd8_medium                       | 15,333                       |
| kcd8_hard                         | 4,403                        |
| kcd8_merged                       | 17,293                       |

## Contact

```
kyouwook@kaist.ac.kr
```