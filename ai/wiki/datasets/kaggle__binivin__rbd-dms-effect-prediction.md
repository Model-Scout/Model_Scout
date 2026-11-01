---
type: "dataset"
id: "kaggle/binivin/rbd-dms-effect-prediction"
source: "kaggle"
url: "https://www.kaggle.com/datasets/binivin/rbd-dms-effect-prediction"
downloads: 18
summary: "RBD DMS 돌연변이 효과 예측을 위한 생물학적 검증 결과 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# kaggle/binivin/rbd-dms-effect-prediction

> dataset · [Kaggle](https://www.kaggle.com/datasets/binivin/rbd-dms-effect-prediction)

RBD DMS 돌연변이 효과 예측을 위한 생물학적 검증 결과 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `biological effect prediction models` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `reference ESM-2 residue embeddings, and mutant-sequence delta ESM features` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `compare different validation settings and distinguish easy interpolation from difficult extrapolation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `summary tables from a computational biology project` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `receptor-binding and expression/folding scores` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation results` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `biological effect prediction models can look accurate under easier validation settings` · 신뢰도 low
