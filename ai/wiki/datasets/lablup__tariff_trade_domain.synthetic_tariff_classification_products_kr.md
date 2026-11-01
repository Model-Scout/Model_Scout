---
type: "dataset"
id: "lablup/tariff_trade_domain.synthetic_tariff_classification_products_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_tariff_classification_products_kr"
downloads: 34
summary: "한국어 상품 설명과 HS 관세 코드, 분류 근거를 포함한 합성 관세 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lablup/tariff_trade_domain.synthetic_tariff_classification_products_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_tariff_classification_products_kr)

한국어 상품 설명과 HS 관세 코드, 분류 근거를 포함한 합성 관세 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `504` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Korean customs classification requires assigning a 10-digit HS code to an imported or exported product` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `generated to support training and evaluation of customs classification models` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `generated to support training and evaluation of customs classification models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `decision_reason` 열 p90 756자 ≈ 504 토큰 (viewer statistics, default/train)
