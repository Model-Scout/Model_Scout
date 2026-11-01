---
type: "dataset"
id: "leey4n/KR3"
source: "huggingface"
url: "https://huggingface.co/datasets/leey4n/KR3"
downloads: 142
summary: "한국어 식당 리뷰 감성 분류용 데이터셋으로 긍정/부정 평가 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# leey4n/KR3

> dataset · [Hugging Face](https://huggingface.co/datasets/leey4n/KR3)

한국어 식당 리뷰 감성 분류용 데이터셋으로 긍정/부정 평가 포함

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Korean Restaurant Reviews with Ratings` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Korean sentiment classification dataset` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `255` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Korean Restaurant Reviews with Ratings` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This data is included for additional pre-training purpose or other usage.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `Review` 열 p90 383자 ≈ 255 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `kaggle/ninetyninenewton/kr3-korean-restaurant-reviews-with-ratings`

## 이 데이터로 학습한 모델

- [[likeyellow__klue-review-star|likeyellow/klue-review-star]]
