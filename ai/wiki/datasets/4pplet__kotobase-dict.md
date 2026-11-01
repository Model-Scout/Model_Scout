---
type: "dataset"
id: "4pplet/kotobase-dict"
source: "huggingface"
url: "https://huggingface.co/datasets/4pplet/kotobase-dict"
downloads: 608
summary: "한국어, 일본어, 중국어 사전 데이터와 예문, TOPIK 수준 태그를 포함한 오프라인 사전용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[서비스 데이터]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# 4pplet/kotobase-dict

> dataset · [Hugging Face](https://huggingface.co/datasets/4pplet/kotobase-dict)

한국어, 일본어, 중국어 사전 데이터와 예문, TOPIK 수준 태그를 포함한 오프라인 사전용 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `TOPIK level tags (A/B/C) for Korean vocabulary` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `4.8M+ sense definitions in multiple languages (English, Korean, Japanese, and more)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Full-text search via FTS5` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `4M+ dictionary entries across Korean, Japanese, and Chinese` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `4.8M+ sense definitions in multiple languages (English, Korean, Japanese, and more)` · 신뢰도 low
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `TOPIK level tags (A/B/C) for Korean vocabulary` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Pre-built SQLite dictionary database for Kotobase, an offline-first Korean/Japanese/Chinese dictionary and vocabulary learning app.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
