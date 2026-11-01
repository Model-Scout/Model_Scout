---
type: "dataset"
id: "kaggle/sudalairajkumar/novel-corona-virus-2019-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset"
downloads: 484774
summary: "코로나19 일별 확진, 사망, 회복자 수 시계열 데이터로 감염 현황 분석에 활용됨"
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
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/sudalairajkumar/novel-corona-virus-2019-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset)

코로나19 일별 확진, 사망, 회복자 수 시계열 데이터로 감염 현황 분석에 활용됨

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The data is available from 22 Jan, 2020.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `law` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Uploading it here for using it in Kaggle kernels and getting insights from the broader DS community.` · 신뢰도 low
