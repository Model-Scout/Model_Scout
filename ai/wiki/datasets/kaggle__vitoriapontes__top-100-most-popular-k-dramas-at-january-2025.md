---
type: "dataset"
id: "kaggle/vitoriapontes/top-100-most-popular-k-dramas-at-january-2025"
source: "kaggle"
url: "https://www.kaggle.com/datasets/vitoriapontes/top-100-most-popular-k-dramas-at-january-2025"
downloads: 365
summary: "MyDramaList에서 2025년 1월 기준 인기 K-드라마 100편의 정보를 담은 데이터셋입니다."
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
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/vitoriapontes/top-100-most-popular-k-dramas-at-january-2025

> dataset · [Kaggle](https://www.kaggle.com/datasets/vitoriapontes/top-100-most-popular-k-dramas-at-january-2025)

MyDramaList에서 2025년 1월 기준 인기 K-드라마 100편의 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `the genres, the tags and the main actors` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `the drama name, the year, the rating and the watchers at the website, the genres, the tags and the main actors` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The columns include the drama name, the year, the rating and the watchers at the website, the genres, the tags and the main actors` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The columns include the drama name, the year, the rating and the watchers at the website, the genres, the tags and the main actors` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `the 100 most popular K-Dramas in MyDramaList, the most popular website for K-Dramas worldwide` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is for educational purposes only.` · 신뢰도 low
