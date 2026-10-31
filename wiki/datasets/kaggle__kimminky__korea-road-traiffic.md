---
type: "dataset"
id: "kaggle/kimminky/korea-road-traiffic"
source: "kaggle"
url: "https://www.kaggle.com/datasets/kimminky/korea-road-traiffic"
downloads: 256
summary: "한국에서 차량 종류별 사고 통계를 분류하여 사고 규모와 차종 예측 모델 개발에 활용하는 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/kimminky/korea-road-traiffic

> dataset · [Kaggle](https://www.kaggle.com/datasets/kimminky/korea-road-traiffic)

한국에서 차량 종류별 사고 통계를 분류하여 사고 규모와 차종 예측 모델 개발에 활용하는 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `사고 규모를 보고 차종을 예측하는등의 모델을 만들수 있을 것이다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `대분류, 중분류, 소분류에 따라서 차량의 종류를 구분해서 한국에서 사고 통계를 집계했다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `사고 규모를 보고 차종을 예측하는등의 모델을 만들수 있을 것이다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Korea Road Traffic Authority_Statistics of traffic accidents 20211231` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `이러한 데이터를 가지고 사고 규모를 보고 차종을 예측하는등의 모델을 만들수 있을 것이다.` · 신뢰도 low
