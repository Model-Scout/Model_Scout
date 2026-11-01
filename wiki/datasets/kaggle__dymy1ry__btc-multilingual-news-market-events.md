---
type: "dataset"
id: "kaggle/dymy1ry/btc-multilingual-news-market-events"
source: "kaggle"
url: "https://www.kaggle.com/datasets/dymy1ry/btc-multilingual-news-market-events"
downloads: 264
summary: "120K 다국어 뉴스 이벤트와 BTC 가격 변동 데이터를 포함한 금융 시계열 분석용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/dymy1ry/btc-multilingual-news-market-events

> dataset · [Kaggle](https://www.kaggle.com/datasets/dymy1ry/btc-multilingual-news-market-events)

120K 다국어 뉴스 이벤트와 BTC 가격 변동 데이터를 포함한 금융 시계열 분석용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `text classification` · 신뢰도 medium
- **작업**: [[시계열 예측]] — ner · readme = `market-reaction research` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `multilingual coverage analysis` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:language_modeling = `120,981 timestamped events from 18 publisher feeds` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `weak semantic labels` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It is designed for reproducible event studies, classifier bootstrapping` · 신뢰도 low
