---
type: "dataset"
id: "kaggle/leetolo/league-of-legend-high-elo-ranked-team-comp-s11"
source: "kaggle"
url: "https://www.kaggle.com/datasets/leetolo/league-of-legend-high-elo-ranked-team-comp-s11"
downloads: 146
summary: "리그 오브 레전드 시즌 11 고랭크 팀 경기 데이터로 승리 예측 및 경기 시간 분석용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/leetolo/league-of-legend-high-elo-ranked-team-comp-s11

> dataset · [Kaggle](https://www.kaggle.com/datasets/leetolo/league-of-legend-high-elo-ranked-team-comp-s11)

리그 오브 레전드 시즌 11 고랭크 팀 경기 데이터로 승리 예측 및 경기 시간 분석용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `- Predict which team won the match` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `- Predict how long a game took` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `tabular` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `which team won the match, the total time of the match` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `games, video games` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset consists of in total 2901 ranked matches` · 신뢰도 low
