---
type: "dataset"
id: "OpenAssistant/oasst2"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenAssistant/oasst2"
downloads: 18409
summary: "OpenAssistant 대화 데이터셋으로, 대화형 AI 학습 및 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
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
# OpenAssistant/oasst2

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenAssistant/oasst2)

OpenAssistant 대화 데이터셋으로, 대화형 AI 학습 및 평가에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Open Assistant Conversations Dataset Release 2 (OASST2)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `This dataset contains message trees.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `All messages have a role property: this can either be "assistant" or "prompter".` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `364` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Open Assistant Conversations Dataset Release 2 (OASST2)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The oasst_ready-trees file usually is sufficient for supervised fine-tuning (SFT) & reward model (RM) training.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1454자 ≈ 364 토큰 (viewer statistics, default/validation)

## 같은 데이터의 사본·중복 등록

- `liarrrrrrrr/oasst2`
- `tian77hh/oasst2`

## 이 데이터로 학습한 모델

- [[AneekC__quipu-moe-1B-A149M-chat|AneekC/quipu-moe-1B-A149M-chat]]
- [[AneekC__quipu-moe-1B-A149M-chat-distill|AneekC/quipu-moe-1B-A149M-chat-distill]]
- [[Horizon-Labs__content-safety-guard-base|Horizon-Labs/content-safety-guard-base]]
- [[Horizon-Labs__content-safety-guard-small|Horizon-Labs/content-safety-guard-small]]
- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-large|Horizon-Labs/prompt-injection-guard-large]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
- [[llm-semantic-router__mmbert32k-modality-router-merged|llm-semantic-router/mmbert32k-modality-router-merged]]
- [[vllm-sr__mmbert32k-modality-router-merged|vllm-sr/mmbert32k-modality-router-merged]]
