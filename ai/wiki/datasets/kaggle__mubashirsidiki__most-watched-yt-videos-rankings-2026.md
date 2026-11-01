---
type: "dataset"
id: "kaggle/mubashirsidiki/most-watched-yt-videos-rankings-2026"
source: "kaggle"
url: "https://www.kaggle.com/datasets/mubashirsidiki/most-watched-yt-videos-rankings-2026"
downloads: 870
summary: "2026년 기준 유튜브 최다 조회수 1000개 영상의 조회수, 좋아요, 언어, 콘텐츠 유형 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/mubashirsidiki/most-watched-yt-videos-rankings-2026

> dataset · [Kaggle](https://www.kaggle.com/datasets/mubashirsidiki/most-watched-yt-videos-rankings-2026)

2026년 기준 유튜브 최다 조회수 1000개 영상의 조회수, 좋아요, 언어, 콘텐츠 유형 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Build classifiers using title features` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Analyze distribution of views and engagement` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Study ranking decay from #1 to #1000` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Each row represents one video with the following columns` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Each row represents one video with the following columns` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `This dataset ranks the top 1000 most viewed YouTube videos of all time` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Build classifiers using title features` · 신뢰도 low
