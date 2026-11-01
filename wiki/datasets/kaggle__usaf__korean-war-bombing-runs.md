---
type: "dataset"
id: "kaggle/usaf/korean-war-bombing-runs"
source: "kaggle"
url: "https://www.kaggle.com/datasets/usaf/korean-war-bombing-runs"
downloads: 655
summary: "한국전쟁 당시 미 공군의 폭격 임무 기록 데이터로 전쟁사 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/usaf/korean-war-bombing-runs

> dataset · [Kaggle](https://www.kaggle.com/datasets/usaf/korean-war-bombing-runs)

한국전쟁 당시 미 공군의 폭격 임무 기록 데이터로 전쟁사 연구에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `THOR is a painstakingly cultivated database of historic aerial bombings from World War I through Vietnam.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Our goal is to see where public discourse and innovation takes this data.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Each theater of warfare has a separate data file` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Each theater of warfare has a separate data file` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `THOR is a painstakingly cultivated database of historic aerial bombings from World War I through Vietnam.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `THOR is a dataset project initiated by Lt Col Jenns Robertson and continued in partnership with Data.mil` · 신뢰도 low
