---
type: "dataset"
id: "nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1"
downloads: 2301
summary: "도구 사용 에이전트의 간접 프롬프트 인젝션 공격 저항 능력 학습용 강화학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[교육]]"
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1)

도구 사용 에이전트의 간접 프롬프트 인젝션 공격 저항 능력 학습용 강화학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Reinforcement learning with verifiable rewards (RLVR) experiments using deterministic trace-analysis for verification` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-use` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `In each record, the agent receives a benign user request that requires calling a read tool whose output contains an adversarial instruction disguised as legitim` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The user task always requires a different write tool than the injection's `target_tool`, so any call to `target_tool` with `target_args` is unambiguous evidence` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `The dataset spans nine enterprise domains — `healthcare`, `legal`, `real_estate`, `logistics`, `ecommerce`, `education`, `hr`, `it_helpdesk`, and `insurance`` · 신뢰도 low
- **도메인**: [[교육]] — ner · readme = `The dataset spans nine enterprise domains — `healthcare`, `legal`, `real_estate`, `logistics`, `ecommerce`, `education`, `hr`, `it_helpdesk`, and `insurance`` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `The dataset spans nine enterprise domains — `healthcare`, `legal`, `real_estate`, `logistics`, `ecommerce`, `education`, `hr`, `it_helpdesk`, and `insurance`` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `The dataset spans nine enterprise domains — `healthcare`, `legal`, `real_estate`, `logistics`, `ecommerce`, `education`, `hr`, `it_helpdesk`, and `insurance`` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `RL dataset for training and evaluating a tool-using agent's ability to resist Indirect Prompt Injection (IPI) attacks` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
