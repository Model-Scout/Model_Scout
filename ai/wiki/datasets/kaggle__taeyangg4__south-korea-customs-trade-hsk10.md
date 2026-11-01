---
type: "dataset"
id: "kaggle/taeyangg4/south-korea-customs-trade-hsk10"
source: "kaggle"
url: "https://www.kaggle.com/datasets/taeyangg4/south-korea-customs-trade-hsk10"
downloads: 81
summary: "관세청 공식 공공데이터 기반 월별 국가별·품목별 수출입 데이터셋으로 무역 분석에 활용됨."
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
  - "[[상거래·상품]]"
  - "[[행정·민원]]"
---
# kaggle/taeyangg4/south-korea-customs-trade-hsk10

> dataset · [Kaggle](https://www.kaggle.com/datasets/taeyangg4/south-korea-customs-trade-hsk10)

관세청 공식 공공데이터 기반 월별 국가별·품목별 수출입 데이터셋으로 무역 분석에 활용됨.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `designed for trade-network analysis, supply-chain dependency research, industrial structure, product diversification, bilateral trade analysis, and forecasting` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Monthly trade by 269 partners and 10-digit Korean HSK products` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Monthly trade by 269 partners and 10-digit Korean HSK products` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `trade datasets stop at HS2, HS4, or HS6. This release keeps the full Korean HSK10 detail` · 신뢰도 low
- **도메인**: [[행정·민원]] — tag_match · tags = `government` · 신뢰도 medium
