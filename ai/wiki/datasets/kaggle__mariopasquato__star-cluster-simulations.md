---
type: "dataset"
id: "kaggle/mariopasquato/star-cluster-simulations"
source: "kaggle"
url: "https://www.kaggle.com/datasets/mariopasquato/star-cluster-simulations"
downloads: 5317
summary: "별들의 위치와 속도를 포함한 직접 N-바디 시뮬레이션 데이터로 별 군집의 동역학 연구에 활용됨."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/mariopasquato/star-cluster-simulations

> dataset · [Kaggle](https://www.kaggle.com/datasets/mariopasquato/star-cluster-simulations)

별들의 위치와 속도를 포함한 직접 N-바디 시뮬레이션 데이터로 별 군집의 동역학 연구에 활용됨.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Can we predict where a star will be at any given time based on its initial position and velocity?` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Each .csv file named c_xxxx.csv corresponds to a snapshot of the simulation at time t = xxxx.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Positions and velocities of stars` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dynamical evolution of star clusters is a topic of very active research in astrophysics.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains the positions and velocities of simulated stars (particles) in a direct N-body simulation of a star cluster.` · 신뢰도 low
