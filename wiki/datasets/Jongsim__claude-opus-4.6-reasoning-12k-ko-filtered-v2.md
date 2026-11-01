---
type: "dataset"
id: "Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2"
downloads: 122
summary: "Claude Opus가 생성한 12,126개 한국어 추론 데이터셋으로, 비-Claude 데이터를 제거한 엄격 필터링 버전입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2)

Claude Opus가 생성한 12,126개 한국어 추론 데이터셋으로, 비-Claude 데이터를 제거한 엄격 필터링 버전입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `과제 도메인 (math, code)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `12,126개의 Claude Opus 전용 한국어 추론 데이터셋` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = ``messages` | string | `{role, content}` 쌍의 JSON 배열 (user/assistant)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``messages` | string | `{role, content}` 쌍의 JSON 배열 (user/assistant)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11059` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `과제 도메인 (math, code)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `messages` 열 p90 16588자 ≈ 11059 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Yoro9381__LFM2.5-1.2B-Instruct-Korean-Opus-4.6-Distill-GGUF|Yoro9381/LFM2.5-1.2B-Instruct-Korean-Opus-4.6-Distill-GGUF]]
