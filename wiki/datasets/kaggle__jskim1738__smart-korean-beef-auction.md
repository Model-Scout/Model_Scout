---
type: "dataset"
id: "kaggle/jskim1738/smart-korean-beef-auction"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jskim1738/smart-korean-beef-auction"
downloads: 86
summary: "스마트 한우 경매 가격 데이터로 한우 경매 결과 분석 및 예측에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# kaggle/jskim1738/smart-korean-beef-auction

> dataset · [Kaggle](https://www.kaggle.com/datasets/jskim1738/smart-korean-beef-auction)

스마트 한우 경매 가격 데이터로 한우 경매 결과 분석 및 예측에 활용됨.

## 분류

- **작업**: [[표 데이터 예측]] — ner · readme = `For each cow, what is the relationship between '종류', kpn, and the '최저가'?` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `k-beef_raw.csv : whole data` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `beef_answer.csv : answers(price) for test` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Korean beef Online Auctions, by 축산플랫폼 주식회사.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `beef_test.csv : datasets for test without '상태', '낙찰가' colums.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `beef_train.csv : datasets for train` · 신뢰도 medium
