---
type: "dataset"
id: "kaggle/anittasaju/complete-5000-dramas-from-mydramalist-review-info"
source: "kaggle"
url: "https://www.kaggle.com/datasets/anittasaju/complete-5000-dramas-from-mydramalist-review-info"
downloads: 496
summary: "MyDramaList에서 인기 아시아 드라마 5000편의 일반 정보와 리뷰, 리뷰어 정보를 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/anittasaju/complete-5000-dramas-from-mydramalist-review-info

> dataset · [Kaggle](https://www.kaggle.com/datasets/anittasaju/complete-5000-dramas-from-mydramalist-review-info)

MyDramaList에서 인기 아시아 드라마 5000편의 일반 정보와 리뷰, 리뷰어 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Finding a new popularity Index
Sentiment analysis
Demography, sex, tags, genre where the drama is more popular` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Finding a new popularity Index` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `It gives a comprehensive report of all general details like date of airing, genre, tags, plot summary, cast, etc. and stats like no of reviewers, no of viewers,` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `I am a huge fan of Asian dramas :), and frequently visit MyDramaList for recommendations.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This data has been scrapped from MyDramaList website using python's Beautiful Soup module and sentimental analysis has been performed` · 신뢰도 low
