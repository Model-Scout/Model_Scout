---
type: "dataset"
id: "nvidia/Nemotron-RL-instruction_following-structured_outputs"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following-structured_outputs"
downloads: 529
summary: "Nemotron-RL 데이터셋은 JSON 형식의 스키마 제약 하에 출력 포맷 지시를 따르는 능력을 평가하는 학습용 데이터입니다."
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nvidia/Nemotron-RL-instruction_following-structured_outputs

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following-structured_outputs)

Nemotron-RL 데이터셋은 JSON 형식의 스키마 제약 하에 출력 포맷 지시를 따르는 능력을 평가하는 학습용 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `tests the ability of the model to follow output formatting instructions under schema constraints under the JSON format` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `tests the ability of the model to follow output formatting instructions under schema constraints under the JSON format` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Train: 9437 prompts, Validation: 512 prompts` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
