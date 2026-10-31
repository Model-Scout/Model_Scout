---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: search_result
    sequence: string
  - name: answer
    dtype: string
  - name: extracted_ref_numbers
    sequence: int64
  - name: type
    dtype: string
  - name: __index_level_0__
    dtype: int64
  - name: llm_result
    dtype: string
  splits:
  - name: search_result_3_start_index_0
    num_bytes: 8023195
    num_examples: 932
  - name: search_result_3
    num_bytes: 7999822
    num_examples: 932
  - name: search_result_5
    num_bytes: 12179127
    num_examples: 932
  - name: search_result_5_start_index_0
    num_bytes: 12190527
    num_examples: 932
  download_size: 46436252
  dataset_size: 40392671
configs:
- config_name: default
  data_files:
  - split: search_result_3
    path: data/search_result_3-*
  - split: search_result_5
    path: data/search_result_5-*
  - split: search_result_3_start_index_0
    path: data/search_result_3_start_index_0-*
  - split: search_result_5_start_index_0
    path: data/search_result_5_start_index_0-*
task_categories:
- text-generation
language:
- ko
tags:
- rag
size_categories:
- 1K<n<10K
---
# 데이터셋 설명

iamjoon/klue-mrc-ko-rag-dataset을 활용해 답변을 생성하는 과정을 CoT로 보강한 데이터셋입니다.
검색된 문서 수가 3개인 경우와 5개인 경우를 나눠서 데이터셋을 구성하였습니다.

## 데이터셋 구조
- question: 사용자의 질문
- search_result: 검색 결과
  - 최소 1개~최대 5개까지 다양하게 구성.
- answer: 사용자의 질문과 검색 결과를 바탕으로 답변합니다.
- extracted_ref_numbers: 검색 결과 중 실제 정답으로 사용된 문서의 번호
  - 최소 0개~최대 5개까지 다양하게 구성.
- llm_result : 위 데이터를 활용해 LLM으로 생성한 답변.
  - 구체적으로는 질문에 대해 검색된 문서들을 참고해 적절한 답변을 'answer' 블록에 생성하고, 그 과정을 추론하게 한 결과를 'reasoning' 블록에 작성, 최종적으로 답변 생성에 참고한 문서의 번호를 'doc_num'에 작성하도록 하는 프롬프트를 통해 생성한 답변 
  - 답변 생성 모델: GPT-4o 
