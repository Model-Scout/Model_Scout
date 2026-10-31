---
type: "dataset"
id: "nvidia/Nemotron-Pretraining-Code-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v1"
downloads: 4689
summary: "Nemotron-Pretraining-Code-v1은 고품질 수학 및 코드 데이터와 다국어 Q&A를 포함한 대규모 사전학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
# nvidia/Nemotron-Pretraining-Code-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v1)

Nemotron-Pretraining-Code-v1은 고품질 수학 및 코드 데이터와 다국어 Q&A를 포함한 대규모 사전학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `fueling the next generation of intelligent, globally-capable models` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `Additionally, we generate large-scale code question–answer data in 11 programming languages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:question_answering = `Large-scale curated source code dataset from GitHub, processed through multi-stage filtering` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `producing diverse natural language–code pairs for pretraining` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `diverse multilingual Q&A, fueling the next generation of intelligent, globally-capable models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This pretraining dataset, for generative AI model training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[nvidia__NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16|nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16]]
- [[nvidia__NVIDIA-Nemotron-Nano-12B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base]]
- [[nvidia__NVIDIA-Nemotron-Nano-9B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-9B-v2-Base]]
- [[nvidia__Nemotron-Labs-TwoTower-30B-A3B-Base-BF16|nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16]]
