---
type: "dataset"
id: "kaggle/ghost5612/novel-covid-19-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ghost5612/novel-covid-19-dataset"
downloads: 1366
summary: "세계 코로나19 확진자, 사망자, 회복자 일별 누적 데이터를 제공하는 시계열 데이터셋입니다."
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
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/ghost5612/novel-covid-19-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/ghost5612/novel-covid-19-dataset)

세계 코로나19 확진자, 사망자, 회복자 일별 누적 데이터를 제공하는 시계열 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus. Please note that this is a time serie` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The data is available from 22 Jan, 2020.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `law` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Uploading it here for using it in Kaggle kernels and getting insights from the broader DS community.` · 신뢰도 low
