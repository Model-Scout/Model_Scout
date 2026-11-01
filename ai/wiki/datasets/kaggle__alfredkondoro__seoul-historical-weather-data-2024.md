---
type: "dataset"
id: "kaggle/alfredkondoro/seoul-historical-weather-data-2024"
source: "kaggle"
url: "https://www.kaggle.com/datasets/alfredkondoro/seoul-historical-weather-data-2024"
downloads: 4335
summary: "서울의 1994년부터 2024년까지 일별 기상 데이터를 제공하는 연구 및 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/alfredkondoro/seoul-historical-weather-data-2024

> dataset · [Kaggle](https://www.kaggle.com/datasets/alfredkondoro/seoul-historical-weather-data-2024)

서울의 1994년부터 2024년까지 일별 기상 데이터를 제공하는 연구 및 교육용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Analyze trends and patterns in weather conditions over time.` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `Train models for weather prediction, anomaly detection, or related tasks.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The dataset contains the following columns: - Date (datetime): The date of the recorded weather data. - Maximum Temperature (tempmax): The highest temperature r` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The dataset contains the following columns: - Date (datetime): The date of the recorded weather data. - Maximum Temperature (tempmax): The highest temperature r` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `weather and climate` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for educational and research purposes.` · 신뢰도 low
