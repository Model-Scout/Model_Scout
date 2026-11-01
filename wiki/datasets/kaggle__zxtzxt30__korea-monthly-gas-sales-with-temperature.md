---
type: "dataset"
id: "kaggle/zxtzxt30/korea-monthly-gas-sales-with-temperature"
source: "kaggle"
url: "https://www.kaggle.com/datasets/zxtzxt30/korea-monthly-gas-sales-with-temperature"
downloads: 762
summary: "한국의 월별 도시가스 판매량과 기온, 지역 정보를 담은 데이터로 가스 수요 예측에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/zxtzxt30/korea-monthly-gas-sales-with-temperature

> dataset · [Kaggle](https://www.kaggle.com/datasets/zxtzxt30/korea-monthly-gas-sales-with-temperature)

한국의 월별 도시가스 판매량과 기온, 지역 정보를 담은 데이터로 가스 수요 예측에 활용됨

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This data can help anticipate future gas demand.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Monthly gas sales with temperature and province of South Korea` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `This data can help anticipate future gas demand.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `Gas demand is dependent on the weather; ascending demand by getting colder.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This data can help anticipate future gas demand.` · 신뢰도 low
