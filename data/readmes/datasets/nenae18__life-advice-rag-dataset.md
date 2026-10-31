---
pretty_name: Life Advice RAG Dataset
language:
- ko
- en
tags:
- rag
- retrieval
- korean
- religion
- philosophy
- bible
- buddhism
- confucianism
- life-advice
task_categories:
- question-answering
- text-retrieval
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: chunks.jsonl
---

# Life Advice RAG Dataset

성경, 불교 경전/해설, 논어, 인문학 명언 자료를 RAG 검색용 chunk로 변환한 데이터셋입니다.

## Dataset Summary

- Chunk 수: **4,007**
- 출처 수: **83**
- 총 문자 수: **3,656,354**
- 데이터 형식: `JSONL`
- 주요 용도: 근거 기반 인생조언 RAG, 종교·철학 관점 비교 검색, 발표/시연용 QA

## Files

| File | Description |
|---|---|
| `chunks.jsonl` | RAG 검색용 chunk 본문 |
| `dataset_manifest.json` | 데이터셋 통계와 출처 목록 |
| `sample_questions.json` | 시연용 질문 예시 |

## Data Fields

`chunks.jsonl`의 각 줄은 다음 형식입니다.

```json
{
  "chunk_id": "chunk_000001",
  "source": "원본 파일명 또는 자료명",
  "category": "성경/불교/유학·논어/명언/기타",
  "source_type": "pdf/txt/csv/zip",
  "loc": "쪽수 또는 위치",
  "text": "검색에 사용할 본문 chunk"
}
```

## Intended Use

이 데이터셋은 다음과 같은 질문에 대해 근거 검색을 수행하기 위한 용도입니다.

- 좋은 아내란?
- 좋은 남편이란?
- 고난이 왔을 때 어떻게 해야 하나?
- 좋은 리더란 어떤 사람인가?
- 인간관계에서 가장 중요한 것은?

## RAG Pipeline

1. `chunks.jsonl` 로드
2. SentenceTransformer 임베딩 생성
3. FAISS 벡터 인덱스 생성
4. BM25 키워드 검색과 벡터 검색을 결합
5. 검색된 Context 기반 답변 생성

## Important Usage Notice

이 데이터셋은 사용자가 제공한 원문 자료에서 추출한 텍스트 chunk를 포함합니다.  
공개 배포 전에 원문 자료별 저작권과 라이선스를 반드시 확인해야 합니다.

권리가 불명확한 자료가 포함되어 있다면 다음 방식을 권장합니다.

- Hugging Face Dataset Repository를 **Private**로 생성
- 팀원/교수자에게만 제한 공유
- 공개 제출물에는 코드, 구조, 샘플 소량 데이터만 공개

## Citation / Attribution

프로젝트 발표에서는 다음처럼 설명할 수 있습니다.

> 원본 PDF/TXT/CSV 자료를 재현 가능한 RAG 데이터셋으로 변환하고, Hugging Face Dataset Hub에 저장하여 Colab에서 자동 다운로드되도록 구성했습니다.
