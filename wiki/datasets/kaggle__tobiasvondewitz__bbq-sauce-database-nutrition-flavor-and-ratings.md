---
type: "dataset"
id: "kaggle/tobiasvondewitz/bbq-sauce-database-nutrition-flavor-and-ratings"
source: "kaggle"
url: "https://www.kaggle.com/datasets/tobiasvondewitz/bbq-sauce-database-nutrition-flavor-and-ratings"
downloads: 23
summary: "311개 바비큐 소스의 영양성분, 맛, 평점 정보를 담은 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/tobiasvondewitz/bbq-sauce-database-nutrition-flavor-and-ratings

> dataset · [Kaggle](https://www.kaggle.com/datasets/tobiasvondewitz/bbq-sauce-database-nutrition-flavor-and-ratings)

311개 바비큐 소스의 영양성분, 맛, 평점 정보를 담은 데이터베이스입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `sentiment label and the number of reviews behind it` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Build a recommender: input a diet constraint and flavor preference, output matching sauces.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `one tidy table (one row per sauce)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `one tidy table (one row per sauce)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `nutrition, data analytics, recommender systems, cooking and recipes, food` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `free to use, including commercially, with attribution.` · 신뢰도 low
