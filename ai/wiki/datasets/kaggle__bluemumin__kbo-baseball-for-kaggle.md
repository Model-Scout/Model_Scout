---
type: "dataset"
id: "kaggle/bluemumin/kbo-baseball-for-kaggle"
source: "kaggle"
url: "https://www.kaggle.com/datasets/bluemumin/kbo-baseball-for-kaggle"
downloads: 1713
summary: "1991년부터 2018년까지 한국 프로야구 타자 타격 기록 데이터로 다음 시즌 기록 예측에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/bluemumin/kbo-baseball-for-kaggle

> dataset · [Kaggle](https://www.kaggle.com/datasets/bluemumin/kbo-baseball-for-kaggle)

1991년부터 2018년까지 한국 프로야구 타자 타격 기록 데이터로 다음 시즌 기록 예측에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `use that data to predict next season's record` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This data is korean baseball Batter's Hitting Dataset, for 1991 ~ 2018` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `use that data to predict next season's record` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This data is korean baseball Batter's Hitting Dataset, for 1991 ~ 2018` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `You can study baseball terminology and data, and use that data to predict next season's record.` · 신뢰도 low
