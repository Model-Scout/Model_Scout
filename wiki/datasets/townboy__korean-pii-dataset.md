---
type: "dataset"
id: "townboy/korean-pii-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/townboy/korean-pii-dataset"
downloads: 164
summary: "한국어 개인정보(PII) 탐색 및 토큰 분류 모델 학습용 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# townboy/korean-pii-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/townboy/korean-pii-dataset)

한국어 개인정보(PII) 탐색 및 토큰 분류 모델 학습용 합성 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `한국어 문장 안의 개인정보(PII)를 탐색·분석하거나 토큰 분류 모델을 학습할 수 있도록 제작한 합성 데이터셋입니다.` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `58` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 문장 안의 개인정보(PII)를 탐색·분석하거나 토큰 분류 모델을 학습할 수 있도록 제작한 합성 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Validation 1,510` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Train 9,227` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 87자 ≈ 58 토큰 (viewer statistics, raw/validation)

## 이 데이터로 학습한 모델

- [[atonlee__supra-ko-pii-router|atonlee/supra-ko-pii-router]]
