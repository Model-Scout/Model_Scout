---
license: cc-by-sa-4.0
task_categories:
- text-generation
- question-answering
language:
- ko
tags:
- korean
- wikipedia
- rag
- retrieval-augmented-generation
- csat
- nlp-competition
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: content
    dtype: string
  - name: title
    dtype: string
  - name: page_id
    dtype: int64
  - name: text_length
    dtype: int64
  splits:
  - name: train
    num_bytes: 2096217536
    num_examples: 565484
  download_size: 1139471725
  dataset_size: 2096217536
---

# NLP-07-ODQA/kowiki-cleaned

## Dataset Description

이 데이터셋은 한국어 위키피디아 XML 덤프에서 추출하고 정제한 데이터셋입니다. 청킹 전 단계의 정제된 문서를 포함합니다.

### 데이터 소스

- **원본**: 한국어 위키피디아 XML 덤프
- **네임스페이스**: 0 (일반 문서)
- **처리된 페이지 수**: 565,484개
- **전체 페이지 수**: 2,157,147개

### 데이터 정제 과정

1. **위키 마크업 제거**: `[[링크]]`, `{템플릿}`, `==제목==` 등 제거
2. **불필요한 섹션 제거**: '같이 보기', '외부 링크', '참고 문헌', '각주' 등 제거
3. **필터링**: 리다이렉트, 빈 페이지, 스텁 페이지 제거
4. **최소 길이**: 200자 이상만 포함

### 통계

- **평균 텍스트 길이**: 1871.8자

## 데이터 구조

각 데이터 포인트는 다음 필드를 포함합니다:

- `content`: 정제된 텍스트 (전체 문서)
- `title`: 문서 제목
- `page_id`: 위키피디아 페이지 ID
- `text_length`: 정제된 텍스트 길이 (문자 수)

## 사용 예시

```python
from datasets import load_dataset

# 정제된 데이터셋 로드
dataset = load_dataset("NLP-07-ODQA/kowiki-cleaned")

# 데이터 확인
print(dataset['train'][0])
```

## 데이터셋 생성 설정

- **Min Text Length**: 200자
- **Sample Rate**: 1.0

## 라이선스

이 데이터셋은 한국어 위키피디아의 CC BY-SA 4.0 라이선스를 따릅니다.

## 참고사항

- 이 데이터셋은 수능 국어/사회 과목 문제 풀이를 위한 RAG 시스템 구축을 목적으로 생성되었습니다.
- 청킹 전 단계의 정제된 문서를 포함합니다. 청킹이 필요한 경우 별도의 청킹 스크립트를 사용하세요.

## 버전

- **현재 버전**: v1.0
