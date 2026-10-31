---
type: "dataset"
id: "nvidia/Nemotron-RL-Jailbreak-Robustness-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-RL-Jailbreak-Robustness-v1"
downloads: 252
summary: "Nemotron-RL-Jailbreak-Robustness-v1은 대형 언어 모델의 우회 공격 대응 및 정책 준수를 강화하기 위한 적대적 프롬프트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# nvidia/Nemotron-RL-Jailbreak-Robustness-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-RL-Jailbreak-Robustness-v1)

Nemotron-RL-Jailbreak-Robustness-v1은 대형 언어 모델의 우회 공격 대응 및 정책 준수를 강화하기 위한 적대적 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Each prompt is tagged with a response policy` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `run reward profiling before starting training` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:reranking = `just prompts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `responses are generated during training` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a collection of hybrid (open-source and synthetically generated) collection of adversarial prompts` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `responses are generated during training (online reinforcement learning)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
