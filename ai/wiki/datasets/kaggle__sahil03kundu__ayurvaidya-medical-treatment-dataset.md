---
type: "dataset"
id: "kaggle/sahil03kundu/ayurvaidya-medical-treatment-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sahil03kundu/ayurvaidya-medical-treatment-dataset"
downloads: 7
summary: "10개 의료 시스템의 치료 효과를 비교하는 10만 건 합성 환자 기록 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
  - "[[학습용]]"
---
# kaggle/sahil03kundu/ayurvaidya-medical-treatment-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/sahil03kundu/ayurvaidya-medical-treatment-dataset)

10개 의료 시스템의 치료 효과를 비교하는 10만 건 합성 환자 기록 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Knowledge graph embeddings` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `Multilingual medical NLP (102 languages represented)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Full dataset (100K rows)` · 신뢰도 low
