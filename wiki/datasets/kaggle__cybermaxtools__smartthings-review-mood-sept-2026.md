---
type: "dataset"
id: "kaggle/cybermaxtools/smartthings-review-mood-sept-2026"
source: "kaggle"
url: "https://www.kaggle.com/datasets/cybermaxtools/smartthings-review-mood-sept-2026"
downloads: 20
summary: "2026년 9월 삼성 SmartThings 앱 리뷰의 일별 평점과 냉장고 관련 언급을 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
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
# kaggle/cybermaxtools/smartthings-review-mood-sept-2026

> dataset · [Kaggle](https://www.kaggle.com/datasets/cybermaxtools/smartthings-review-mood-sept-2026)

2026년 9월 삼성 SmartThings 앱 리뷰의 일별 평점과 냉장고 관련 언급을 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `review counts, average rating, share of 1-2 star reviews and how many reviews mention the fridge, an update or firmware, or connection trouble` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `app review sentiment` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset tracks the SmartThings app's Google Play and App Store reviews day by day from 8 to 23 Sep 2026` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `Google Play and Apple App Store, Korea (Korean reviews) and US (English reviews)` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Aggregates only: no review text, titles or reviewer names` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `SmartThings App Reviews` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A one-off snapshot of reviews around the September 2026 incident, collected on 24 Sep 2026` · 신뢰도 low
