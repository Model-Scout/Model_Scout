---
type: "dataset"
id: "kaggle/jonauror/true-parents-legacy-sermons-and-speeches-1946-2012"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jonauror/true-parents-legacy-sermons-and-speeches-1946-2012"
downloads: 4
summary: "선문문과 한학자의 1946-2012년 설교, 연설, 기도문 3,700여 건을 모은 디지털 아카이브입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/jonauror/true-parents-legacy-sermons-and-speeches-1946-2012

> dataset · [Kaggle](https://www.kaggle.com/datasets/jonauror/true-parents-legacy-sermons-and-speeches-1946-2012)

선문문과 한학자의 1946-2012년 설교, 연설, 기도문 3,700여 건을 모은 디지털 아카이브입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each record includes full plaintext, metadata, and a permanent ARK identifier.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Digital archive of 3,700+ sermons, speeches, prayers, and book passages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Format: JSONL (one record per passage)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each record includes full plaintext, metadata, and a permanent ARK identifier.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `태그: religion and belief systems` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `출처: Kaggle (jonauror/true-parents-legacy-sermons-and-speeches-1946-2012)` · 신뢰도 low
