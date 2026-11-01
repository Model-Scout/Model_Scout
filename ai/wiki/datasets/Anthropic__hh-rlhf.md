---
type: "dataset"
id: "Anthropic/hh-rlhf"
source: "huggingface"
url: "https://huggingface.co/datasets/Anthropic/hh-rlhf"
downloads: 36165
summary: "인간 피드백 기반 강화학습(RLHF)을 위한 도움과 무해성 선호 데이터 및 레드팀 대화 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Anthropic/hh-rlhf

> dataset · [Hugging Face](https://huggingface.co/datasets/Anthropic/hh-rlhf)

인간 피드백 기반 강화학습(RLHF)을 위한 도움과 무해성 선호 데이터 및 레드팀 대화 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Human preference data about helpfulness and harmlessness from Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `each line of the jsonl files contains a pair of texts, one "chosen" and one "rejected".` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `each line of the jsonl files contains a pair of texts, one "chosen" and one "rejected".` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `494` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `These data are meant to understand how crowdworkers red team models and what types of red team attacks are succesful or not.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `These data are meant to train preference (or reward) models for subsequent RLHF training.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 1975자 ≈ 494 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[TheBloke__PiVoT-0.1-Evil-a-GGUF|TheBloke/PiVoT-0.1-Evil-a-GGUF]]
- [[maywell__PiVoT-0.1-Evil-a|maywell/PiVoT-0.1-Evil-a]]
