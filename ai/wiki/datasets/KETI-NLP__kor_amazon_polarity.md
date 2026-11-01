---
type: "dataset"
id: "KETI-NLP/kor_amazon_polarity"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_amazon_polarity"
downloads: 65
summary: "아마존 상품 리뷰 감성 분석을 위한 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# KETI-NLP/kor_amazon_polarity

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_amazon_polarity)

아마존 상품 리뷰 감성 분석을 위한 한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `review text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `rating dimensions with review text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `943` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `amazon_polarity` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data is distributed under the CC0 1.0 license.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 1415자 ≈ 943 토큰 (viewer statistics, default/test)
