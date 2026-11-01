---
type: "dataset"
id: "jangmin/ecommerce_purchase_history"
source: "huggingface"
url: "https://huggingface.co/datasets/jangmin/ecommerce_purchase_history"
downloads: 8
summary: "특정 이커머스 회사의 추천 시스템 연구 개발을 위한 90일 구매 히스토리 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jangmin/ecommerce_purchase_history

> dataset · [Hugging Face](https://huggingface.co/datasets/jangmin/ecommerce_purchase_history)

특정 이커머스 회사의 추천 시스템 연구 개발을 위한 90일 구매 히스토리 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `특정 이커머스 회사의 추천 시스템 연구 개발을 위한 데이터셋이다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `구매 히스토리를 텍스트로 기술하였다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `구매 히스토리를 텍스트로 기술하였다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `특정 이커머스 회사의 추천 시스템 연구 개발을 위한 데이터셋이다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `test 스플릿의 경우 user_id, positive_prod_id 기준으로 train_split에 등장하지 않는 것만을 남겼다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
