---
type: "dataset"
id: "kaggle/ozgurozenn/global-tech-companies-stock-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ozgurozenn/global-tech-companies-stock-dataset"
downloads: 35
summary: "세계 주요 기술 기업 40여 곳의 주식 및 재무 정보를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
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
  - "[[금융·경제]]"
---
# kaggle/ozgurozenn/global-tech-companies-stock-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/ozgurozenn/global-tech-companies-stock-dataset)

세계 주요 기술 기업 40여 곳의 주식 및 재무 정보를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Industry and sector classifications` · 신뢰도 medium
- **작업**: [[시계열 예측]] — ner · readme = `Financial modeling and predictions` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Stock market analysis` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This dataset provides detailed financial and company information` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Current stock prices and historical data (52-week high/low)` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `This dataset provides detailed financial and company information for over 40 leading technology companies` · 신뢰도 medium
