---
type: "dataset"
id: "nvidia/Nemotron-CC-Math-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1"
downloads: 8367
summary: "Nemotron-CC-Math는 고품질 수학 및 코드 데이터로 LLM 사전학습에 사용되는 대규모 수학 말뭉치입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# nvidia/Nemotron-CC-Math-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1)

Nemotron-CC-Math는 고품질 수학 및 코드 데이터로 LLM 사전학습에 사용되는 대규모 수학 말뭉치입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `FineMath classifier` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[정보 추출]] — ner · readme = `designed for scientific content` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `which was used in nemotron pre-training` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:language_modeling = `a large-scale, high-quality math corpus extracted from Common Crawl` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `improving reasoning, symbolic understanding, and general intelligence in large language models` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `which was used in nemotron pre-training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
- [[nvidia__NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16|nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16]]
- [[nvidia__NVIDIA-Nemotron-Nano-12B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base]]
- [[nvidia__NVIDIA-Nemotron-Nano-9B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-9B-v2-Base]]
- [[nvidia__Nemotron-Labs-TwoTower-30B-A3B-Base-BF16|nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16]]
