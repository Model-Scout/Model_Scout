---
type: "dataset"
id: "tals/vitaminc"
source: "huggingface"
url: "https://huggingface.co/datasets/tals/vitaminc"
downloads: 6084
summary: "Wikipedia 편집 기반의 사실 검증 데이터셋으로, 견고한 사실 검증 연구에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tals/vitaminc

> dataset · [Hugging Face](https://huggingface.co/datasets/tals/vitaminc)

Wikipedia 편집 기반의 사실 검증 데이터셋으로, 견고한 사실 검증 연구에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Fact Verification dataset created for Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Fact Verification dataset created for Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `65` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `based on Wikipedia edits (revisions)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Fact Verification dataset created for Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `evidence` 열 p90 262자 ≈ 65 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
