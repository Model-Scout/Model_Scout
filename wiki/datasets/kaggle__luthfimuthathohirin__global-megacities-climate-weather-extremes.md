---
type: "dataset"
id: "kaggle/luthfimuthathohirin/global-megacities-climate-weather-extremes"
source: "kaggle"
url: "https://www.kaggle.com/datasets/luthfimuthathohirin/global-megacities-climate-weather-extremes"
downloads: 31
summary: "2015-2024년 50개 글로벌 메가시티의 일별 기상 관측 데이터로 기후 변화 연구에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
  - "[[지리·위치]]"
---
# kaggle/luthfimuthathohirin/global-megacities-climate-weather-extremes

> dataset · [Kaggle](https://www.kaggle.com/datasets/luthfimuthathohirin/global-megacities-climate-weather-extremes)

2015-2024년 50개 글로벌 메가시티의 일별 기상 관측 데이터로 기후 변화 연구에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Heat/cold stress level: normal_range (140,628), moderate_heat (20,047), frost_freeze (16,760), polar_deep_freeze (2,725), extreme_heatwave (2,490)` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `extracting actionable climate intelligence requires synthesizing raw thermodynamic parameters` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `182K Daily Weather Observations 2015-2024: 50 Global Megacities` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **도메인**: [[지리·위치]] — ner · readme = `50 megacities and research stations across 40 countries and 7 continents` · 신뢰도 low
