---
type: "dataset"
id: "kaggle/hyeonjunkim/fama-french-5-factor-model-south-korea"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hyeonjunkim/fama-french-5-factor-model-south-korea"
downloads: 167
summary: "한국 주식시장(KOSPI, KOSDAQ)용 Fama-French 5요인 모델 데이터로 포트폴리오 성과 평가에 활용됨."
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
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hyeonjunkim/fama-french-5-factor-model-south-korea

> dataset · [Kaggle](https://www.kaggle.com/datasets/hyeonjunkim/fama-french-5-factor-model-south-korea)

한국 주식시장(KOSPI, KOSDAQ)용 Fama-French 5요인 모델 데이터로 포트폴리오 성과 평가에 활용됨.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This data could be use to evaluate the performance or style of South Korean stock portfolios using the linear regression model` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `This dataset consist of 6 columns: Mrt-Rf, HML, SMB, CMA, RMW, and RF.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `This dataset consist of 6 columns: Mrt-Rf, HML, SMB, CMA, RMW, and RF.` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset consist of 6 columns: Mrt-Rf, HML, SMB, CMA, RMW, and RF.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `RF is the investment return of 91 day monetary stabilization bond of South Korea, works as risk-free rate in South Korean stock market.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a intermediate result for research with Professor Jay M. Chung, Soongsil Univ.` · 신뢰도 low
