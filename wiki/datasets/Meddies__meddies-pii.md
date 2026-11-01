---
type: "dataset"
id: "Meddies/meddies-pii"
source: "huggingface"
url: "https://huggingface.co/datasets/Meddies/meddies-pii"
downloads: 669
summary: "다국어 임상 및 행정 문서에서 개인 식별 정보(PII)를 추출하기 위한 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Meddies/meddies-pii

> dataset · [Hugging Face](https://huggingface.co/datasets/Meddies/meddies-pii)

다국어 임상 및 행정 문서에서 개인 식별 정보(PII)를 추출하기 위한 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `BIOES token-classification view` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction = `Tagged document text with inline markers such as `[Nguyễn Hoa] `.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Chat-style instruction inputs and normalized target JSON for GRPO configs.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2090` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Mixed training and evaluation bundles | 76,160 | `train`, `eval`, `test`` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Mixed training and evaluation bundles | 76,160 | `train`, `eval`, `test`` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 8360자 ≈ 2090 토큰 (viewer statistics, korean/train)

## 이 데이터로 학습한 모델

- [[Meddies__meddies-pii|Meddies/meddies-pii]]
