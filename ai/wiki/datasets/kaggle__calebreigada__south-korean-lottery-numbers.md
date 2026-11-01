---
type: "dataset"
id: "kaggle/calebreigada/south-korean-lottery-numbers"
source: "kaggle"
url: "https://www.kaggle.com/datasets/calebreigada/south-korean-lottery-numbers"
downloads: 1445
summary: "한국 복권 당첨 번호 데이터로 당첨 확률 분석 및 예측에 활용하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/calebreigada/south-korean-lottery-numbers

> dataset · [Kaggle](https://www.kaggle.com/datasets/calebreigada/south-korean-lottery-numbers)

한국 복권 당첨 번호 데이터로 당첨 확률 분석 및 예측에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Determining the best numbers to choose in the South Korean Lottery` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `TIME - The nth lottery draw
NUM1 - Winning number 1
NUM2 - Winning number 2
NUM3 - Winning number 3
NUM4 - Winning number 4
NUM5 - Winning number 5
NUM6 - Winni` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `TIME - The nth lottery draw
NUM1 - Winning number 1
NUM2 - Winning number 2
NUM3 - Winning number 3
NUM4 - Winning number 4
NUM5 - Winning number 5
NUM6 - Winni` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `TIME - The nth lottery draw
NUM1 - Winning number 1
NUM2 - Winning number 2
NUM3 - Winning number 3
NUM4 - Winning number 4
NUM5 - Winning number 5
NUM6 - Winni` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `태그: computer science, programming, exploratory data analysis, data analytics, tabular, gambling, korea` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Determining the best numbers to choose in the South Korean Lottery` · 신뢰도 low
