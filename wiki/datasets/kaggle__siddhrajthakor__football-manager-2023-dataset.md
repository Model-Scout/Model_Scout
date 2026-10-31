---
type: "dataset"
id: "kaggle/siddhrajthakor/football-manager-2023-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/siddhrajthakor/football-manager-2023-dataset"
downloads: 1130
summary: "FM23 게임에서 추출한 9만 명 이상의 축구 선수 상세 속성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
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
  - "[[상거래·상품]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/siddhrajthakor/football-manager-2023-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/siddhrajthakor/football-manager-2023-dataset)

FM23 게임에서 추출한 9만 명 이상의 축구 선수 상세 속성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Cluster players by playing style or potential using machine learning` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Analyze player attributes to identify key traits for success by position` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `Predict transfer values based on skills, age, and performance stats` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This dataset is a meticulously curated compilation of player statistics from five CSV files, merged into a single, unified dataset (`merged_players.csv`)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Merged and cleaned for immediate analysis, with consistent column structure across all records` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Predict transfer values based on skills, age, and performance stats` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `a popular football management simulation game` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Merged and cleaned for immediate analysis, with consistent column structure across all records` · 신뢰도 low
