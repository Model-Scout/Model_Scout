---
type: "dataset"
id: "kaggle/kukuroo3/body-performance-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/kukuroo3/body-performance-data"
downloads: 22200
summary: "나이와 운동 수행 데이터를 기반으로 신체 능력 등급을 분류하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/kukuroo3/body-performance-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/kukuroo3/body-performance-data)

나이와 운동 수행 데이터를 기반으로 신체 능력 등급을 분류하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `data shape : (13393, 12)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `class : A,B,C,D ( A: best) / stratified` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Some post-processing and filtering has done from the raw data.` · 신뢰도 low
