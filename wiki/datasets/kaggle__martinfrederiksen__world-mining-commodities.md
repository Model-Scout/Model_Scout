---
type: "dataset"
id: "kaggle/martinfrederiksen/world-mining-commodities"
source: "kaggle"
url: "https://www.kaggle.com/datasets/martinfrederiksen/world-mining-commodities"
downloads: 657
summary: "국가별 및 기업별 광물 자원 채굴 분포 데이터를 제공하는 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/martinfrederiksen/world-mining-commodities

> dataset · [Kaggle](https://www.kaggle.com/datasets/martinfrederiksen/world-mining-commodities)

국가별 및 기업별 광물 자원 채굴 분포 데이터를 제공하는 교육용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Visualization, unit conversion practice, get to know who mines what, put commodities into categories/groups and countries in trade unions etc.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The dataset [world_mining_commodities_clean] (csv file) contains data about mined commodities (65) pr. country (169) during the period 2018-2022.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The dataset [world_mining_commodities_clean] (csv file) contains data about mined commodities (65) pr. country (169) during the period 2018-2022.` · 신뢰도 low
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `World commodity mining distribution based on country and companies` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset [world_mining_commodities_clean] (csv file) contains data about mined commodities (65) pr. country (169) during the period 2018-2022.` · 신뢰도 low
