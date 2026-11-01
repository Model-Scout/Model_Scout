---
type: "dataset"
id: "kaggle/ardisragen/indonesia-coronavirus-cases"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ardisragen/indonesia-coronavirus-cases"
downloads: 16791
summary: "인도네시아 코로나19 확진자 및 지역별 통계 데이터를 제공하는 공개 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/ardisragen/indonesia-coronavirus-cases

> dataset · [Kaggle](https://www.kaggle.com/datasets/ardisragen/indonesia-coronavirus-cases)

인도네시아 코로나19 확진자 및 지역별 통계 데이터를 제공하는 공개 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Characteristics of Corona patients DS` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `Simple Visualization and Forecasting` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Dataset
1) Total Confirmed Positive Cases
2) Google Trend Related keywords
3) Patient Epidemiological Data
4) Daily Case Statistics
5) Case per Province
6) Case` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Dataset
1) Total Confirmed Positive Cases
2) Google Trend Related keywords
3) Patient Epidemiological Data
4) Daily Case Statistics
5) Case per Province
6) Case` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `COVID-19 has infected many people in Indonesia` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We make a structured dataset based on the report materials in these portals.` · 신뢰도 low
