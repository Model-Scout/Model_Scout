---
language: ko
license: cc-by-sa-4.0
tags:
- mrc
- korean
- finance
- legal
dataset_info:
- config_name: multiple_choice
  features:
  - name: doc_title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: options
    sequence: string
  - name: answer_text
    dtype: string
  splits:
  - name: train
    num_bytes: 52657661
    num_examples: 32092
  - name: test
    num_bytes: 8296685
    num_examples: 4634
  download_size: 14848868
  dataset_size: 60954346
- config_name: span_extraction
  features:
  - name: doc_title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answer_text
    dtype: string
  splits:
  - name: train
    num_bytes: 154553286
    num_examples: 93828
  - name: test
    num_bytes: 23273377
    num_examples: 12692
  download_size: 43600501
  dataset_size: 177826663
- config_name: span_extraction_how
  features:
  - name: doc_title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answer_text
    dtype: string
  splits:
  - name: train
    num_bytes: 111843943
    num_examples: 61746
  - name: test
    num_bytes: 21025535
    num_examples: 9124
  download_size: 31577500
  dataset_size: 132869478
- config_name: tableqa
  features:
  - name: doc_title
    dtype: string
  - name: context
    dtype: string
  - name: table_title
    dtype: string
  - name: table_html
    dtype: string
  - name: question
    dtype: string
  - name: answer_text
    dtype: string
  splits:
  - name: train
    num_bytes: 228901199
    num_examples: 96000
  - name: test
    num_bytes: 24161924
    num_examples: 12000
  download_size: 15321234
  dataset_size: 253063123
- config_name: text_entailment
  features:
  - name: doc_title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answer_text
    dtype: string
  splits:
  - name: train
    num_bytes: 52307558
    num_examples: 32750
  - name: test
    num_bytes: 5778697
    num_examples: 3740
  download_size: 13330652
  dataset_size: 58086255
configs:
- config_name: multiple_choice
  data_files:
  - split: train
    path: multiple_choice/train-*
  - split: test
    path: multiple_choice/test-*
- config_name: span_extraction
  data_files:
  - split: train
    path: span_extraction/train-*
  - split: test
    path: span_extraction/test-*
- config_name: span_extraction_how
  data_files:
  - split: train
    path: span_extraction_how/train-*
  - split: test
    path: span_extraction_how/test-*
- config_name: tableqa
  data_files:
  - split: train
    path: tableqa/train-*
  - split: test
    path: tableqa/test-*
- config_name: text_entailment
  data_files:
  - split: train
    path: text_entailment/train-*
  - split: test
    path: text_entailment/test-*
---

# 금융, 법률 문서 기계독해 데이터셋

금융 및 법률 분야 전문문서를 활용하여 기계독해 모델 생성을 위한 지문-질문-답변으로 구성된 데이터셋입니다.

## 데이터셋 구성

### Subsets
- **span_extraction**: 정답경계 추출형(정답이 지문 내 특정 범위에 있는 데이터)
- **span_extraction_how**: 절차(방법)(어떻게로 시작하는 질문에 대한 정답 추출 데이터)
- **multiple_choice**: 다지선다형(객관식 형태의 데이터)
- **tableqa**: Table 정답추출형(표 기반 질의응답 데이터)
- **text_entailment**: Yes/No 단문형(Boolean 선택 형태의 데이터)

### Splits
- **train**: 학습용 데이터셋
- **validation**: 검증용 데이터셋

## 사용 방법
``` python
from datasets import load_dataset
특정 configuration의 특정 split 로드
train_data = load_dataset("shchoice/finance-legal-mrc", "span_extraction", split="train")
valid_data = load_dataset("shchoice/finance-legal-mrc", "multiple_choice", split="test")
특정 configuration의 전체 split 로드
full_dataset = load_dataset("shchoice/finance-legal-mrc", "span_extraction")
```

## 데이터 필드
1. 기계독해에 필요한 필수 항목
  - doc_title: 문서 제목 (Optional)
  - context: 문장의 주요 텍스트 내용
  - question: 질문 텍스트
  - answer_text: 질문에 대한 정답 텍스트
2. 정답 힌트
  - clue_text: 정답의 단서를 제공하는 텍스트
3. 테이블 QA에 필요한 정보
  - table_title: 표의 제목
  - table_html: 표의 HTML 데이터
4. 테이블 QA에 필요한 정보 + 정답 힌트
  - cell_text: 정답이 포함된 셀의 텍스트 데이터
  - cell_coordinates: 정답이 포함된 셀의 좌표 데이터
5. 다지선택형 QA에서 필요한 정보
  - options : 객관식 내용들(1. 정답 2. 오답 3. 오답 4.오답)
6. 문서의 분류명
  - class: 문서의 분류 정보
  - code: 문서의 코드 정보

## 라이선스
이 데이터셋은 CC-BY-SA-4.0 라이선스 하에 제공됩니다.
