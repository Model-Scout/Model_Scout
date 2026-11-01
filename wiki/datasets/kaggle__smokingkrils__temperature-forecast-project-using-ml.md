---
type: "dataset"
id: "kaggle/smokingkrils/temperature-forecast-project-using-ml"
source: "kaggle"
url: "https://www.kaggle.com/datasets/smokingkrils/temperature-forecast-project-using-ml"
downloads: 1607
summary: "한국 기상청 LDAPS 모델의 서울 지역 일별 최저·최고 기온 예측을 위한 기상 데이터셋입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/smokingkrils/temperature-forecast-project-using-ml

> dataset · [Kaggle](https://www.kaggle.com/datasets/smokingkrils/temperature-forecast-project-using-ml)

한국 기상청 LDAPS 모델의 서울 지역 일별 최저·최고 기온 예측을 위한 기상 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Predict Minimum and Maximum Temperature during a day based on various features` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This data consists of summer data from 2013 to 2017. The input data is largely composed of the LDAPS model's next-day forecast data, in-situ maximum and minimum` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `There are two outputs (i.e. next-day maximum and minimum air temperatures) in this data.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This data consists of summer data from 2013 to 2017.` · 신뢰도 low
