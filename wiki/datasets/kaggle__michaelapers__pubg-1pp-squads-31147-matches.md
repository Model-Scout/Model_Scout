---
type: "dataset"
id: "kaggle/michaelapers/pubg-1pp-squads-31147-matches"
source: "kaggle"
url: "https://www.kaggle.com/datasets/michaelapers/pubg-1pp-squads-31147-matches"
downloads: 12
summary: "PUBG 1인칭 시점 스쿼드 경기 31147개 매치 데이터로 게임 분석에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/michaelapers/pubg-1pp-squads-31147-matches

> dataset · [Kaggle](https://www.kaggle.com/datasets/michaelapers/pubg-1pp-squads-31147-matches)

PUBG 1인칭 시점 스쿼드 경기 31147개 매치 데이터로 게임 분석에 활용 가능

## 분류

- **작업**: [[임베딩]] — ner · readme = `maybe make comparisons to other datasets released up to 8 months ago` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `I wanted to do some analysis on higher-elo matches` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `a flattened pandas-friendlier version of that data` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `a flattened pandas-friendlier version of that data` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PlayerUnknown's Battlegrounds data scraped from pubg.op.gg` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `I collected my own dataset inspired by https://www.kaggle.com/skihikingkevin/pubg-match-deaths/data` · 신뢰도 low
