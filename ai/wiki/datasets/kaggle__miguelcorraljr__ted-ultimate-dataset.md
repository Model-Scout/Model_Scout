---
type: "dataset"
id: "kaggle/miguelcorraljr/ted-ultimate-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset"
downloads: 10792
summary: "TED 강연 4,000여 개의 다국어 대본을 포함한 NLP용 데이터셋입니다."
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/miguelcorraljr/ted-ultimate-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset)

TED 강연 4,000여 개의 다국어 대본을 포함한 NLP용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `* Natural Language Processing` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `* Recommender system` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `Full transcript of the talk` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Full transcript of the talk` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TED is devoted to spreading powerful ideas in just about any topic.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `These datasets contain over 4,000 TED talks including transcripts in many languages.` · 신뢰도 low
