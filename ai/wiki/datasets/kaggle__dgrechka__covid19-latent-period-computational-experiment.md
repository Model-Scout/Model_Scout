---
type: "dataset"
id: "kaggle/dgrechka/covid19-latent-period-computational-experiment"
source: "kaggle"
url: "https://www.kaggle.com/datasets/dgrechka/covid19-latent-period-computational-experiment"
downloads: 465
summary: "COVID-19 잠복기 길이 추정을 위한 SEIR 모델 기반 전염병 확산 시뮬레이션 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/dgrechka/covid19-latent-period-computational-experiment

> dataset · [Kaggle](https://www.kaggle.com/datasets/dgrechka/covid19-latent-period-computational-experiment)

COVID-19 잠복기 길이 추정을 위한 SEIR 모델 기반 전염병 확산 시뮬레이션 데이터입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `I try to estimate the latent period for COVID-19 caused by SARS-CoV-2 virus via computational simulations using SEIR model` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `I try to fit all other parameters to match the observed statistics the best` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `I let the optimizer to fit the following parameters` · 신뢰도 low
