---
type: "dataset"
id: "kaggle/imajne/leage-of-legends-in-game-data-every-1-miniute"
source: "kaggle"
url: "https://www.kaggle.com/datasets/imajne/leage-of-legends-in-game-data-every-1-miniute"
downloads: 30
summary: "한국 서버에서 수집한 리그 오브 레전드 1분 단위 게임 데이터로 경기 흐름 분석용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/imajne/leage-of-legends-in-game-data-every-1-miniute

> dataset · [Kaggle](https://www.kaggle.com/datasets/imajne/leage-of-legends-in-game-data-every-1-miniute)

한국 서버에서 수집한 리그 오브 레전드 1분 단위 게임 데이터로 경기 흐름 분석용입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `The key point of this data is a timeline that shows every 1 min since the game started so that we can analyze the whole game flow.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Total 11274 match data` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Total 11274 match data` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `I have collected game data from Korean servers.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Total 11274 match data` · 신뢰도 low
