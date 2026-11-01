---
type: "dataset"
id: "kaggle/team-ai/shinzo-abe-japanese-prime-minister-twitter-nlp"
source: "kaggle"
url: "https://www.kaggle.com/datasets/team-ai/shinzo-abe-japanese-prime-minister-twitter-nlp"
downloads: 1071
summary: "일본 아베 신조 총리의 트위터 데이터를 담아 경제 및 외교 문제 분석에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/team-ai/shinzo-abe-japanese-prime-minister-twitter-nlp

> dataset · [Kaggle](https://www.kaggle.com/datasets/team-ai/shinzo-abe-japanese-prime-minister-twitter-nlp)

일본 아베 신조 총리의 트위터 데이터를 담아 경제 및 외교 문제 분석에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Maybe if you analyze his tweets about Japanese economy this data will be useful for stock price forecasting etc.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `tweet text size block` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `tweet text size block` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 3.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains following the data:` · 신뢰도 low
