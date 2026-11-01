---
type: "dataset"
id: "kaggle/thedevastator/exploring-food-related-trends-and-sentiments-on"
source: "kaggle"
url: "https://www.kaggle.com/datasets/thedevastator/exploring-food-related-trends-and-sentiments-on"
downloads: 108
summary: "Reddit /r/Food 게시글을 분석해 음식 관련 트렌드와 사용자 감성을 탐구하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/thedevastator/exploring-food-related-trends-and-sentiments-on

> dataset · [Kaggle](https://www.kaggle.com/datasets/thedevastator/exploring-food-related-trends-and-sentiments-on)

Reddit /r/Food 게시글을 분석해 음식 관련 트렌드와 사용자 감성을 탐구하는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `explore key insights related to user interactions with their peers or favorite dishes` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Generating sentiment analysis graphs of different posts over time` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Analyzing user sentiment on certain ingredients or meals through natural language processing` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:question_answering = `user-generated posts, including columns such as title, score, id, url, comms_num, created, body and timestamp` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Generating sentiment analysis graphs of different posts over time` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `food related issues or what type of recipes get the most appreciation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset offers a comprehensive look into the conversations and trends within the Reddit Food Subreddit` · 신뢰도 low
