---
type: "dataset"
id: "searle-j/kote"
source: "huggingface"
url: "https://huggingface.co/datasets/searle-j/kote"
downloads: 207
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# searle-j/kote

> dataset · [Hugging Face](https://huggingface.co/datasets/searle-j/kote)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `80` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 120자 ≈ 80 토큰 (viewer statistics, dichotomized/validation)

## 이 데이터로 학습한 모델

- [[tobykim__koelectra-44emotions|tobykim/koelectra-44emotions]]
