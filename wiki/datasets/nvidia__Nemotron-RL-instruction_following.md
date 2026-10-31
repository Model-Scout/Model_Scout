---
type: "dataset"
id: "nvidia/Nemotron-RL-instruction_following"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following"
downloads: 1596
summary: "Nemotron-RL-instruction_following은 명확한 지시 이행 평가 및 학습용 LLM 강화학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# nvidia/Nemotron-RL-instruction_following

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following)

Nemotron-RL-instruction_following은 명확한 지시 이행 평가 및 학습용 LLM 강화학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This makes the dataset well-suited for evaluating and training models on objective instruction adherence.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
