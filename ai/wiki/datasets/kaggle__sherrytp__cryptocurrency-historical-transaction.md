---
type: "dataset"
id: "kaggle/sherrytp/cryptocurrency-historical-transaction"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sherrytp/cryptocurrency-historical-transaction"
downloads: 561
summary: "Huobi 거래소의 2020년 9월 암호화폐 거래 내역 시계열 데이터로 투자 모델 개발에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/sherrytp/cryptocurrency-historical-transaction

> dataset · [Kaggle](https://www.kaggle.com/datasets/sherrytp/cryptocurrency-historical-transaction)

Huobi 거래소의 2020년 9월 암호화폐 거래 내역 시계열 데이터로 투자 모델 개발에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `time series analysis` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `time series analysis, investing, currencies and foreign exchange` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `The dataset contains files naming by the types of currency and date` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The simple explanation of columns is the following` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Database: Open Database, Contents: © Original Authors` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `cryptocurrency trading websites` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `Kaggle community could also benefit from using a parse of the datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `used to develop our own models and trading strategies` · 신뢰도 low
