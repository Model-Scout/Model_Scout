---
type: "dataset"
id: "kaggle/viktorpopov/bias-correction-ucl"
source: "kaggle"
url: "https://www.kaggle.com/datasets/viktorpopov/bias-correction-ucl"
downloads: 397
summary: "한국 기상청 LDAPS 모델의 서울 지역 다음날 최대·최소 기온 편향 보정용 데이터셋입니다."
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
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/viktorpopov/bias-correction-ucl

> dataset · [Kaggle](https://www.kaggle.com/datasets/viktorpopov/bias-correction-ucl)

한국 기상청 LDAPS 모델의 서울 지역 다음날 최대·최소 기온 편향 보정용 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This data is for the purpose of bias correction of next-day maximum and minimum air temperatures forecast of the LDAPS model` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `This data consists of summer data from 2013 to 2017. The input data is largely composed of the LDAPS model's next-day forecast data, in-situ maximum and minimum` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `The input data is largely composed of the LDAPS model's next-day forecast data, in-situ maximum and minimum temperatures of present-day, and geographic auxiliar` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `There are two outputs (i.e. next-day maximum and minimum air temperatures) in this data.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `This data is for the purpose of bias correction of next-day maximum and minimum air temperatures forecast of the LDAPS model operated by the Korea Meteorologica` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This data consists of summer data from 2013 to 2017.` · 신뢰도 low
