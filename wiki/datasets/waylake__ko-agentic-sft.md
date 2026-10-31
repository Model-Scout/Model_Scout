---
type: "dataset"
id: "waylake/ko-agentic-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/waylake/ko-agentic-sft"
downloads: 63
summary: "한국어 에이전트 훈련용 합성 대화 데이터셋으로, 도구 호출 시점 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# waylake/ko-agentic-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/waylake/ko-agentic-sft)

한국어 에이전트 훈련용 합성 대화 데이터셋으로, 도구 호출 시점 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `2,369 Korean agent-training conversations, fully synthetic` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean only.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `2,369 Korean agent-training conversations, fully synthetic, generated at zero cost.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[waylake__KoGemma-E2B|waylake/KoGemma-E2B]]
