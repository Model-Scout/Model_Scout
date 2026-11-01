---
type: "dataset"
id: "kaggle/lucassteuber/bluesky-social"
source: "kaggle"
url: "https://www.kaggle.com/datasets/lucassteuber/bluesky-social"
downloads: 20
summary: "2025년 12월 Bluesky 소셜 네트워크 게시글 101,040개로 감정 분석 등 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/lucassteuber/bluesky-social

> dataset · [Kaggle](https://www.kaggle.com/datasets/lucassteuber/bluesky-social)

2025년 12월 Bluesky 소셜 네트워크 게시글 101,040개로 감정 분석 등 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Sentiment Analysis` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Sentiment Scores: VADER` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Language Modeling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:language_modeling = `Post Text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Sentiment Scores: VADER` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Bluesky social media posts via the AT Protocol firehose` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Use Cases
- Sentiment Analysis
- Multilingual NLP
- Temporal Patterns
- Content Analysis
- Language Modeling
- Thread Structure Analysis` · 신뢰도 low
