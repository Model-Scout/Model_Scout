---
type: "dataset"
id: "kpubdata/seoul-apartment-trades"
source: "huggingface"
url: "https://huggingface.co/datasets/kpubdata/seoul-apartment-trades"
downloads: 71
summary: "서울 25개 구의 2020~2024년 아파트 매매 실거래가 데이터로 부동산 가격 예측에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kpubdata/seoul-apartment-trades

> dataset · [Hugging Face](https://huggingface.co/datasets/kpubdata/seoul-apartment-trades)

서울 25개 구의 2020~2024년 아파트 매매 실거래가 데이터로 부동산 가격 예측에 활용 가능

## 분류

- **작업**: [[표 데이터 예측]] — metadata · readme, task_categories = `tabular-regression` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `- **Features**: 14` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The target variable for regression tasks is `deal_amount_10k_krw` (transaction price in units of 10,000 KRW).` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Real apartment sale transaction records in Seoul, South Korea` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The target variable for regression tasks is `deal_amount_10k_krw` (transaction price in units of 10,000 KRW).` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `apartment_seq` 열 p90 11자 ≈ 7 토큰 (viewer statistics, default/train)
