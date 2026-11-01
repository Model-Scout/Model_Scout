---
type: "dataset"
id: "lmqg/qag_koquad"
source: "huggingface"
url: "https://huggingface.co/datasets/lmqg/qag_koquad"
downloads: 78
summary: "KOQuAD 기반의 질문 및 답변 생성 데이터셋으로 질문과 답변 생성을 위한 학습에 사용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lmqg/qag_koquad

> dataset · [Hugging Face](https://huggingface.co/datasets/lmqg/qag_koquad)

KOQuAD 기반의 질문 및 답변 생성 데이터셋으로 질문과 답변 생성을 위한 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `- `questions`: a `list` of `string` features.
- `answers`: a `list` of `string` features.
- `paragraph`: a `string` feature.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The dataset is assumed to be used to train a model for question & answer generation.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `537` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `|train|validation|test |
|----:|---------:|----:|
|9600 | 960 | 4442|` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `paragraph` 열 p90 805자 ≈ 537 토큰 (viewer statistics, qag_koquad/validation)
