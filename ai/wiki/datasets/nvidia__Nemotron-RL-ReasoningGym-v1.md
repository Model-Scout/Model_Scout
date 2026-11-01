---
type: "dataset"
id: "nvidia/Nemotron-RL-ReasoningGym-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-RL-ReasoningGym-v1"
downloads: 1187
summary: "Nemotron-RL-ReasoningGym-v1은 다양한 추론 능력 향상을 위한 15,000개 샘플의 강화학습 환경 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
---
# nvidia/Nemotron-RL-ReasoningGym-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-RL-ReasoningGym-v1)

Nemotron-RL-ReasoningGym-v1은 다양한 추론 능력 향상을 위한 15,000개 샘플의 강화학습 환경 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Each sample contains a question, a verifiable answer, and task-specific metadata for verification.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Modality: Text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Each sample contains a question, a verifiable answer, and task-specific metadata for verification.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Nemotron-RL-ReasoningGym-v1 dataset is designed to improve reasoning capabilities across a broad range of domains, including algebra, arithmetic, computatio` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `| train | 15,000 |` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
