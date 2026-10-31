---
type: "dataset"
id: "eddmpython/cleangov-local-fiscal-metrics"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-local-fiscal-metrics"
downloads: 165
summary: "지방재정365 통합공시 및 재정분석 결과를 제공하는 지방재정 데이터 API입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# eddmpython/cleangov-local-fiscal-metrics

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-local-fiscal-metrics)

지방재정365 통합공시 및 재정분석 결과를 제공하는 지방재정 데이터 API입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `동종 지자체 비교(비교군) 의 기준 자료이며 대부분 자치단체 × 회계연도 × 지표 단위의 집계값이라 사건 단위 연결에는 제한이 있다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `자치단체별로 공시하는 지표군 (수의계약비율, 행사·축제경비 비율·편성내역·원가회계, 업무추진비 비율·절감률·기관운영·시책추진, 지방의회 관련경비·국외여비, 채무·지방채·보증채무·채권, 기금현재액, 지방보조금(2016·2020·2021)·지방보조금비율, 재정자립도·재정자주도·통합재정수지(` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `동종 지자체 비교(비교군) 의 기준 자료이며 대부분 자치단체 × 회계연도 × 지표 단위의 집계값이라 사건 단위 연결에는 제한이 있다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `지방재정365 재정데이터개방 허브의 "지방재정 통합공시" 분류 77 서비스와 "성과/평가 > 재정분석결과" 5 서비스` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `지방재정365 통합공시·재정분석 Open API` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `pfa_amt1` 열 p90 12자 ≈ 8 토큰 (viewer statistics, silver_ABDBC/train)
