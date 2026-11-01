---
type: "dataset"
id: "kaggle/taniadh/skin-care"
source: "kaggle"
url: "https://www.kaggle.com/datasets/taniadh/skin-care"
downloads: 844
summary: "한국 스킨케어 제품 목록과 리뷰 데이터로 추천 시스템 구축에 활용됨."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/taniadh/skin-care

> dataset · [Kaggle](https://www.kaggle.com/datasets/taniadh/skin-care)

한국 스킨케어 제품 목록과 리뷰 데이터로 추천 시스템 구축에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This data can also be used for content-based recommendation system, sentiment analysis etc.` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `This data was created to build a knowledge-based recommendation system.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The data is relational data with two files` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The data is relational data with two files` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Korean Skincare product lists and reviews` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This data was created to build a knowledge-based recommendation system.` · 신뢰도 low
