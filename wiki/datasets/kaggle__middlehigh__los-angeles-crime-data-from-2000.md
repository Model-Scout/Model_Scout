---
type: "dataset"
id: "kaggle/middlehigh/los-angeles-crime-data-from-2000"
source: "kaggle"
url: "https://www.kaggle.com/datasets/middlehigh/los-angeles-crime-data-from-2000"
downloads: 2464
summary: "미국 대도시 범죄 데이터를 포함한 대규모 범죄 기록 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/middlehigh/los-angeles-crime-data-from-2000

> dataset · [Kaggle](https://www.kaggle.com/datasets/middlehigh/los-angeles-crime-data-from-2000)

미국 대도시 범죄 데이터를 포함한 대규모 범죄 기록 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Indicates the crime committed. (Same as Crime Code 1)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Crime Data of different large US Cities` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This dataset has 28 columns and 944K rows.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset has 28 columns and 944K rows.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `collected by the local police in different styles and situations` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains different collected datasets with crime data of many large cities.` · 신뢰도 low
