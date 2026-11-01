---
type: "dataset"
id: "kaggle/canaria/5-gamers"
source: "kaggle"
url: "https://www.kaggle.com/datasets/canaria/5-gamers"
downloads: 4327
summary: "컴퓨터 게임 중 측정한 PPG 심박 데이터로 인지 피로 예측을 위한 시계열 분석 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/canaria/5-gamers

> dataset · [Kaggle](https://www.kaggle.com/datasets/canaria/5-gamers)

컴퓨터 게임 중 측정한 PPG 심박 데이터로 인지 피로 예측을 위한 시계열 분석 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **작업**: [[시계열 예측]] — ner · readme = `Time to "too tired to work" epoch. This is the point at which you will lose the battle against falling asleep.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `A PPG time-series (level of 660nm red light transmitted through participant's ear-lobe) sampled at approx 100Hz` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `There were 5 participants, each attempting a 22 hour "shift" of computer gaming.` · 신뢰도 low
