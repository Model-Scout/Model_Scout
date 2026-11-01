---
type: "dataset"
id: "BCCard/privacy-filter-openpii-masking"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/privacy-filter-openpii-masking"
downloads: 478
summary: "한국어와 영어 개인정보 식별자 엔티티 검출용 토큰 분류 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BCCard/privacy-filter-openpii-masking

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/privacy-filter-openpii-masking)

한국어와 영어 개인정보 식별자 엔티티 검출용 토큰 분류 학습 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Train a token classifier using `tokens` and `token_classes`. The dataset stores token strings, not model input IDs.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset provides entity annotations rather than application-specific redaction output.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `517` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 775자 ≈ 517 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[atonlee__supra-ko-pii-router|atonlee/supra-ko-pii-router]]
