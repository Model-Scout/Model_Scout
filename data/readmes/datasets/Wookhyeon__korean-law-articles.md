---
language:
- ko
license: cc0-1.0
size_categories:
- 1K<n<10K
task_categories:
- text-generation
- text-classification
- question-answering
- summarization
- feature-extraction
tags:
- korean
- law
- legal
- statute
- nlp
- legal-nlp
- korean-nlp
pretty_name: Korean Law Articles (Statutes)
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: law_id
    dtype: string
  - name: mst
    dtype: string
  - name: title
    dtype: string
  - name: title_short
    dtype: string
  - name: law_type
    dtype: string
  - name: ministry
    dtype: string
  - name: phone
    dtype: string
  - name: amendment_type
    dtype: string
  - name: promulgation_date
    dtype: string
  - name: promulgation_no
    dtype: string
  - name: effective_date
    dtype: string
  - name: articles
    list:
    - name: number
      dtype: string
    - name: title
      dtype: string
    - name: content
      dtype: string
    - name: effective_date
      dtype: string
  - name: full_text
    dtype: string
  - name: supplementary
    dtype: string
  - name: amendment_reason
    dtype: string
  - name: amendment_text
    dtype: string
  - name: url
    dtype: string
  - name: crawled_at
    dtype: string
  splits:
  - name: train
    num_bytes: 3931476
    num_examples: 155
  download_size: 1169223
  dataset_size: 3931476
---

# Korean Law Articles — 한국 현행 법령 본문 전수 데이터셋

법제처 국가법령정보 OPEN API (`lawService.do`) 로 수집한 **대한민국 현행 법령 5,583건의 본문 전수** 데이터셋입니다. (전체 5,584건 중 1건은 출처 서버에서 본문 미제공)

## 🎯 라이브 Q&A 챗봇

▶ **[Korean Law Q&A (Gradio Space)](https://huggingface.co/spaces/Wookhyeon/korean-law-search)**

본 데이터셋 위에 RAG 챗봇이 가동 중입니다 — 자연어 질문에 답변하고 인용한 법령을 클릭 가능 링크로 제시합니다.

- **Retrieval**: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 시맨틱 + BM25 hybrid
- **LLM**: Llama 3.3 70B (Groq, free tier)
- **인용 강제 + hallucination 방지**: 데이터셋에 없는 내용은 "확인되지 않습니다" 반환

## 규모

| 항목 | 값 |
|---|---|
| 총 법령 수 | **5,583** |
| Parquet 크기 | 약 54 MB |
| 평균 조문 수 | 약 8개 / 법령 |
| 평균 본문 길이 | 약 2,200자 / 법령 |
| 한국어 (`ko`) | 100% |
| 라이선스 | CC0-1.0 + 출처 표기 (공공누리 제1유형) |

## 출처

- **제공**: 법제처 국가법령정보센터 (https://www.law.go.kr/)
- **API**: `lawService.do?target=law&type=JSON&MST=...`
- **수집 도구**: [Wook-AI/discovery-engine](https://github.com/Wook-AI/discovery-engine) (오픈소스, 6시간 cron 자동 갱신)

## 스키마

| 필드 | 타입 | 설명 |
|---|---|---|
| `law_id` | string | 법령ID |
| `mst` | string | 법령일련번호 (`lawService.do MST` 파라미터) |
| `title` | string | 법령명 (한글) |
| `title_short` | string | 법령명 약칭 |
| `law_type` | string | 법종구분 (법률/대통령령/총리령/부령 등) |
| `ministry` | string | 소관부처 |
| `phone` | string | 소관부처 연락처 |
| `amendment_type` | string | 제개정구분 (제정/일부개정/전부개정/타법개정) |
| `promulgation_date` | string | 공포일자 (YYYYMMDD) |
| `promulgation_no` | string | 공포번호 |
| `effective_date` | string | 시행일자 (YYYYMMDD) |
| `articles` | list[dict] | 조문 목록: `number`, `title`, `content`, `effective_date` |
| `full_text` | string | 모든 조문을 줄바꿈으로 join 한 본문 (LLM 입력용) |
| `supplementary` | string | 부칙 (평탄화) |
| `amendment_reason` | string | 제개정이유 (평탄화) |
| `amendment_text` | string | 개정문 (평탄화) |
| `url` | string | 법제처 원문 링크 |
| `crawled_at` | string | 수집 시각 |

## 사용 예

```python
from datasets import load_dataset

ds = load_dataset("Wookhyeon/korean-law-articles", split="train")
print(f"loaded {len(ds)} laws")
print(ds[0]["title"])
print(ds[0]["full_text"][:500])

# 조문 단위 평탄화 (1 row = 1 article)
import itertools
articles = list(itertools.chain.from_iterable(
    [{**a, "law_id": row["law_id"], "law_title": row["title"]} for a in row["articles"]]
    for row in ds
))
print(f"total articles: {len(articles):,}")
```

## 활용 사례

- **한국어 법령 도메인 LLM 사전학습/파인튜닝**: 한국어 법률 도메인 특화 모델
- **법령 검색·임베딩 벤치마크**: bge/sentence-transformers 한국어 법률 평가 코퍼스
- **법령 QA 시스템 평가**: 시민용 법률 챗봇의 정답 코퍼스
- **법률 NER/요약 라벨링 시드**: 한국어 법률 NLP 태스크의 base data
- **소관부처별 분석**: 부처별 법령 통계, 시계열 변화 분석

## 갱신 정책

- **자동 수집**: 6시간마다 GitHub Actions (`crawl.yml`)
- **HF 동기화**: 매주 일요일 02:00 UTC + manual dispatch (`upload-hf.yml`)
- 출처 시스템(법제처)에 신규/개정 법령이 등록되면 다음 cron 회차에 자동 반영

## 알려진 제한

- **본문 미제공 1건** (MST 200755): 법제처 lawService.do 가 404 반환 (출처 시스템 자체 문제)
- 본문 외 **별표/서식**은 미포함 (`lawBylSearch.do` 별도 API 필요)
- **영문 법령**은 미포함 (`elaw` target 별도 신청 필요)
- **판례/헌재결정례/법령해석례**는 별도 데이터셋으로 분리 예정

## 인용

이 데이터셋을 학술 또는 상용으로 활용하시면 출처를 표기해 주세요:

```
법제처 국가법령정보 OPEN API (https://open.law.go.kr/)
discovery-engine 프로젝트 (https://github.com/Wook-AI/discovery-engine)
```

## 변경 로그

- 2026-04-30: **5,583건 전수 수집 완료** (이전 100건 → 55배 확장) + Gradio Space 데모 공개
- 2026-04-29: 초기 100건 데이터셋 공개
