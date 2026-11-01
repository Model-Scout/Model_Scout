---
type: "dataset"
id: "nvidia/Nemotron-RL-knowledge-mcqa"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-RL-knowledge-mcqa"
downloads: 3947
summary: "Nemotron-RL-knowledge-mcqa는 다양한 분야 지식 기반 다지선다형 질문응답 데이터셋으로 LLM 후학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
# nvidia/Nemotron-RL-knowledge-mcqa

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-RL-knowledge-mcqa)

Nemotron-RL-knowledge-mcqa는 다양한 분야 지식 기반 다지선다형 질문응답 데이터셋으로 LLM 후학습에 사용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `multi-domain synthetic multiple-choice question-answering (MCQA) dataset containing knowledge based questions` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `The dataset spans a broad range of domains, including physics, biology, chemistry, mathematics, computer science, engineering, humanities, law, and others.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
