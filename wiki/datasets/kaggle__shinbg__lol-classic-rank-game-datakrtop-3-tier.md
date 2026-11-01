---
type: "dataset"
id: "kaggle/shinbg/lol-classic-rank-game-datakrtop-3-tier"
source: "kaggle"
url: "https://www.kaggle.com/datasets/shinbg/lol-classic-rank-game-datakrtop-3-tier"
downloads: 315
summary: "한국 리그 오브 레전드 챌린저, 그랜드마스터, 마스터 티어 5대5 게임 기록 데이터로 승률 예측에 활용."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/shinbg/lol-classic-rank-game-datakrtop-3-tier

> dataset · [Kaggle](https://www.kaggle.com/datasets/shinbg/lol-classic-rank-game-datakrtop-3-tier)

한국 리그 오브 레전드 챌린저, 그랜드마스터, 마스터 티어 5대5 게임 기록 데이터로 승률 예측에 활용.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `to predict winning rates based on real-time score fluctuations` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Match game list ,Win team record, Lose team record, Win team's stat, Lose team's stat` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Match game list ,Win team record, Lose team record, Win team's stat, Lose team's stat` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A project to collect league-of-legend game records to analyze the factors that affect victory` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is the result of the my lol predict project's data pipeline` · 신뢰도 low
