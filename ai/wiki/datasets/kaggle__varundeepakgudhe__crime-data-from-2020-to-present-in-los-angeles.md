---
type: "dataset"
id: "kaggle/varundeepakgudhe/crime-data-from-2020-to-present-in-los-angeles"
source: "kaggle"
url: "https://www.kaggle.com/datasets/varundeepakgudhe/crime-data-from-2020-to-present-in-los-angeles"
downloads: 370
summary: "로스앤젤레스의 2020년 이후 범죄 사건 데이터를 제공하는 범죄 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/varundeepakgudhe/crime-data-from-2020-to-present-in-los-angeles

> dataset · [Kaggle](https://www.kaggle.com/datasets/varundeepakgudhe/crime-data-from-2020-to-present-in-los-angeles)

로스앤젤레스의 2020년 이후 범죄 사건 데이터를 제공하는 범죄 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset can be used to find the crime trends, their reasons, correlation between crimes and events, future predection of crimes by undertanding crime patte` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `future predection of crimes by undertanding crime patterns` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset shows real-time crime incidents in Los Angeles.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `This dataset shows real-time crime incidents in Los Angeles.` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset can be used to find the crime trends, their reasons, correlation between crimes and events, future predection of crimes by undertanding crime patte` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `This dataset reflects incidents of crime in the City of Los Angeles dating back to 2020.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset can be used to find the crime trends, their reasons, correlation between crimes and events, future predection of crimes by undertanding crime patte` · 신뢰도 low
