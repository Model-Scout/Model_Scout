---
type: "dataset"
id: "kaggle/sergionefedov/global-climate-and-energy-transition-2000-2026"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sergionefedov/global-climate-and-energy-transition-2000-2026"
downloads: 1940
summary: "2000~2026년 전 세계 기후 변화와 에너지 전환 데이터를 담은 시계열 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
  - "[[금융·경제]]"
---
# kaggle/sergionefedov/global-climate-and-energy-transition-2000-2026

> dataset · [Kaggle](https://www.kaggle.com/datasets/sergionefedov/global-climate-and-energy-transition-2000-2026)

2000~2026년 전 세계 기후 변화와 에너지 전환 데이터를 담은 시계열 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Major climate/weather/policy events with severity scores` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `26 years of the energy transition` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `temperature evolution, CO2 emissions across 50 countries, energy mix transition` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — ner · readme = `geographic scope` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `temperature anomaly + CO2 ppm` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `temperature anomaly + CO2 ppm` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `temperature anomaly + CO2 ppm` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `global climate and energy transition from 2000 to 2026` · 신뢰도 medium
- **도메인**: [[금융·경제]] — ner · readme = `carbon market prices across 5 major ETSs` · 신뢰도 low
