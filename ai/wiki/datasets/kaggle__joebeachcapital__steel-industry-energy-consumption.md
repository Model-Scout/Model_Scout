---
type: "dataset"
id: "kaggle/joebeachcapital/steel-industry-energy-consumption"
source: "kaggle"
url: "https://www.kaggle.com/datasets/joebeachcapital/steel-industry-energy-consumption"
downloads: 1057
summary: "대우조선해양 광양공장의 철강 산업 에너지 소비량 예측을 위한 시계열 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/joebeachcapital/steel-industry-energy-consumption

> dataset · [Kaggle](https://www.kaggle.com/datasets/joebeachcapital/steel-industry-energy-consumption)

대우조선해양 광양공장의 철강 산업 에너지 소비량 예측을 위한 시계열 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **작업**: [[시계열 예측]] — ner · readme = `Steel Industry Energy Consumption Prediction` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `time series analysis` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Energy Consumption Continuous kWh` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `business, energy, electronics` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Data gathered is from DAEWOO Steel Co. Ltd in Gwangyang, South Korea` · 신뢰도 low
