---
type: "dataset"
id: "Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered"
downloads: 36
summary: "12,757개의 고품질 한국어 추론 데이터셋으로 거절 응답 제거 및 번역 복구가 적용됨"
readme_status: "ok"
readme_language: "mixed"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered)

12,757개의 고품질 한국어 추론 데이터셋으로 거절 응답 제거 및 번역 복구가 적용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `과제 도메인 (math, code, science 등)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `12,757개의 고품질 한국어 추론 데이터셋` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = ``messages` | string | `{role, content}` 쌍의 JSON 배열 (user/assistant)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``messages` | string | `{role, content}` 쌍의 JSON 배열 (user/assistant)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `15638` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `과제 도메인 (math, code, science 등)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `12,757개의 고품질 한국어 추론 데이터셋` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `messages` 열 p90 23457자 ≈ 15638 토큰 (viewer statistics, default/train)
