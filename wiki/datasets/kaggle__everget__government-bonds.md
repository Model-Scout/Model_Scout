---
type: "dataset"
id: "kaggle/everget/government-bonds"
source: "kaggle"
url: "https://www.kaggle.com/datasets/everget/government-bonds"
downloads: 2161
summary: "1970~2020년 30개국 정부채권 가격과 수익률 시계열 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
domain:
  - "[[금융·경제]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/everget/government-bonds

> dataset · [Kaggle](https://www.kaggle.com/datasets/everget/government-bonds)

1970~2020년 30개국 정부채권 가격과 수익률 시계열 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Prices and yields of government bonds` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `Prices and yields of government bonds` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `There are **216** columns in both files sorted alphabetically.` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `There are **216** columns in both files sorted alphabetically.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[행정·민원]] — tag_match · tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains government bond prices and yields of 30 countries from 6 world regions (Americas, Europe, Asia, Pacific, Middle East, Africa) in the range ` · 신뢰도 low
