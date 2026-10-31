---
type: "dataset"
id: "nvidia/Nemotron-Cascade-RL-RLHF"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-Cascade-RL-RLHF"
downloads: 110
summary: "RLHF 훈련용으로 설계된 언어 모델 정렬 지원 텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nvidia/Nemotron-Cascade-RL-RLHF

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-RL-RLHF)

RLHF 훈련용으로 설계된 언어 모델 정렬 지원 텍스트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The Nemotron-Cascade-RL-RLHF dataset is designed for Reinforcement Learning from Human Feedback (RLHF) training.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Modality: Text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Modality: Text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This data contains 45,882 samples used for RLHF training.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
