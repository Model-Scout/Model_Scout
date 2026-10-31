---
type: "dataset"
id: "Jongsim/claude-opus-4.6-reasoning-12k-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko"
downloads: 32
summary: "수학, 논리, 과학, 코드 문제에 대한 한국어 추론 데이터셋으로 한국어 추론 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jongsim/claude-opus-4.6-reasoning-12k-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko)

수학, 논리, 과학, 코드 문제에 대한 한국어 추론 데이터셋으로 한국어 추론 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Problem difficulty level` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `reasoning samples covering math, logic, science, and code domains` · 신뢰도 low
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering, task:translation = `Both the questions and reasoning steps are translated` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `Both the questions and reasoning steps are translated` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `15623` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `reasoning samples covering math, logic, science, and code domains` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is intended for fine-tuning Korean LLMs with step-by-step reasoning capabilities.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `messages` 열 p90 23434자 ≈ 15623 토큰 (viewer statistics, default/train)
