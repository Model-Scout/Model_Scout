---
language:
- ko
license: cc-by-nc-4.0
pretty_name: FinDartBench
size_categories:
- 10K<n<100K
task_categories:
- question-answering
tags:
- finance
- korean
- open-domain
---

# FinDartBench

FinDartBench is a Korean financial question answering benchmark built from DART disclosure filings.
It is designed to evaluate real-world financial document understanding by pairing context-grounded questions with high-quality reference answers validated through a multi-stage LLM-based pipeline.

Unlike simple synthetic QA datasets, FinDartBench emphasizes **grounding, answer quality, and inter-model consensus**, making it suitable for reliable evaluation of financial QA systems. 

For a detailed description of the dataset and construction pipeline, please refer to the 📄[technical report](https://davidkim205.github.io/findartbench.html).

This work was supported by the Ministry of Science and ICT.

## Tasks

- Korean financial document question answering
- Open-book QA over corporate disclosure documents
- Answer evaluation with multiple ranked reference answers

## Dataset Overview

- **Total examples:** 14,444
- **Total reference answers:** 39,488
- **Companies:** 10 major Korean companies
- **Source documents:** ~200 DART filings
- **Language:** Korean
- **License:** CC BY-NC 4.0

## Data Fields

| key            | type       | description                                   |
| -------------- | ---------- | --------------------------------------------- |
| id             | int        | Unique identifier for each QA instance        |
| doc_id         | int        | Identifier for the source document            |
| company        | string     | Source company name (Korean)                  |
| doc_type       | string     | Type of disclosure document                   |
| context        | string     | Grounding document chunk                      |
| question       | string     | Korean question derived from context          |
| answers        | list[dict] | Ranked reference answers                      |
| answers.model  | string     | Model used for answer generation              |
| answers.answer | string     | Answer text in Korean                         |

## Example Instance

```json
{
  "id": 11011,
  "doc_id": 352052,
  "company": "현대자동차",
  "doc_type": "주주총회소집공고",
  "context": "### II. 최대주주등과의 거래내역에 관한 사항\n\n...",
  "question": "현대글로비스와의 거래금액 산정 기준과 기타 거래금액 산정 기준은 어떻게 다른가?",
  "answers": [
    {"model": "DeepSeek-V3.2-Exp", "answer": "..."},
    {"model": "Kimi-K2.5", "answer": "..."}
  ]
}
```

Reference answers are ordered by quality after validation.


## Data Construction Pipeline

FinDartBench is constructed through a multi-stage pipeline that ensures both **diversity** and **reliability** of QA pairs:

1. **Document Processing**

   DART filings are segmented into structured chunks while preserving document hierarchy.

2. **Question Generation & Deduplication**

   Multiple LLMs generate candidate questions, which are then clustered to remove duplicates and select representative questions.

3. **Answer Generation**

   Multiple LLMs produce diverse candidate answers for each question.

4. **Quality Validation**

   Candidate answers are filtered based on:

   * grounding to the context
   * Korean language quality
   * inter-model agreement (consensus)


## Dataset Statistics

### Document Type Distribution

| doc_type      | count |
| ------------- | ----: |
| 사업보고서         | 5,638 |
| 기업지배구조보고서공시   | 2,699 |
| 주주총회소집공고      | 1,749 |
| 투자설명서         | 1,019 |
| 의결권대리행사권유참고서류 |   552 |
| 기타            | 2,787 |

### Company Distribution

| company | LG전자  | SK텔레콤 | 삼성전자  | 현대자동차 | 한국전력  | SK하이닉스 | 국민은행 | 기아  | HMM | 두나무 |
| :-----: | ----- | ----- | ----- | ----- | ----- | ------ | ---- | --- | --- | --- |
|  count  | 3,924 | 2,295 | 2,036 | 1,654 | 1,429 | 1,115  | 799  | 500 | 447 | 245 |


## Source Data

All data is derived from publicly available corporate disclosures provided by the Financial Supervisory Service (DART):

[https://dart.fss.or.kr/](https://dart.fss.or.kr/)


## Limitations

* The dataset reflects structures specific to Korean disclosure documents
* Automatically generated using LLMs; residual errors may exist
* Limited coverage (10 companies, ~200 documents)

## Acknowledgements

This research was supported by the “Advanced GPU Utilization Support Program(Beta Service)” funded by the Government of the Republic of Korea (Ministry of Science and ICT).

![alt text](src/과학기술정보통신부_혼합_좌우.jpg)