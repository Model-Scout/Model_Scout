---
type: "dataset"
id: "Bingsu/namuwiki_20210301_filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/namuwiki_20210301_filtered"
downloads: 172
summary: "2021년 3월 1일 기준 나무위키 데이터베이스 덤프로, 텍스트 기반 한국어 위키 데이터입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/namuwiki_20210301_filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/namuwiki_20210301_filtered)

2021년 3월 1일 기준 나무위키 데이터베이스 덤프로, 텍스트 기반 한국어 위키 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Namuwiki database dump (2021-03-01)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:retrieval = `I filtered data without text(mostly redirecting documents).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `I filtered data without text(mostly redirecting documents).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `31200` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is a Korean wiki based on the seed engine` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All data from Namuwiki collected on 2021-03-01.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 46799자 ≈ 31200 토큰 (viewer statistics, default/train)
