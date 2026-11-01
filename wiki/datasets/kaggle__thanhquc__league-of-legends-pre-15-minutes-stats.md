---
type: "dataset"
id: "kaggle/thanhquc/league-of-legends-pre-15-minutes-stats"
source: "kaggle"
url: "https://www.kaggle.com/datasets/thanhquc/league-of-legends-pre-15-minutes-stats"
downloads: 46
summary: "한국 서버 최고 랭크 리그 오브 레전드 15분 경기 통계 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/thanhquc/league-of-legends-pre-15-minutes-stats

> dataset · [Kaggle](https://www.kaggle.com/datasets/thanhquc/league-of-legends-pre-15-minutes-stats)

한국 서버 최고 랭크 리그 오브 레전드 15분 경기 통계 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `태그: games, binary classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `It includes details about wards, golds, exp, kills, deaths, objectives, ... at 15 minutes.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `태그: games, binary classification` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides a you a look at the statistics on the highest level of ranked in the Korean server.` · 신뢰도 low
