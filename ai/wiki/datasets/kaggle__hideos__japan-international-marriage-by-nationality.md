---
type: "dataset"
id: "kaggle/hideos/japan-international-marriage-by-nationality"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hideos/japan-international-marriage-by-nationality"
downloads: 121
summary: "일본 내 부부 국적별 국제 결혼 통계(1965년부터 현재까지) 시계열 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hideos/japan-international-marriage-by-nationality

> dataset · [Kaggle](https://www.kaggle.com/datasets/hideos/japan-international-marriage-by-nationality)

일본 내 부부 국적별 국제 결혼 통계(1965년부터 현재까지) 시계열 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `formatted in both tidy long and wide formats for easy use in time-series analysis, visualization, and demographic research` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `long-term time series of marriages in Japan broken down by the nationalities of both spouses` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The dataset is formatted in both tidy long and wide formats` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The dataset is formatted in both tidy long and wide formats` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `people and society, social science, demographics` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides a long-term time series of marriages in Japan` · 신뢰도 low
