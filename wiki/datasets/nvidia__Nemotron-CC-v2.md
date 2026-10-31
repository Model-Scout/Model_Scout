---
type: "dataset"
id: "nvidia/Nemotron-CC-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-CC-v2"
downloads: 80039
summary: "Nemotron-CC-v2는 수학, 코드, 다국어 Q&A를 포함한 대규모 AI 사전학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# nvidia/Nemotron-CC-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2)

Nemotron-CC-v2는 수학, 코드, 다국어 Q&A를 포함한 대규모 AI 사전학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `pretraining dataset` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `diverse multilingual Q&A` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:question_answering = `English web crawl dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `diverse multilingual Q&A` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English web crawl dataset based on Nemotron-CC with eight additional Common Crawl snapshots` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This pretraining dataset, for generative AI model training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
- [[nvidia__NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16|nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16]]
- [[nvidia__NVIDIA-Nemotron-Nano-12B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base]]
- [[nvidia__NVIDIA-Nemotron-Nano-9B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-9B-v2-Base]]
- [[nvidia__Nemotron-Labs-TwoTower-30B-A3B-Base-BF16|nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16]]
