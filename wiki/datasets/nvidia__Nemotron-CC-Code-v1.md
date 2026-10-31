---
type: "dataset"
id: "nvidia/Nemotron-CC-Code-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-CC-Code-v1"
downloads: 2359
summary: "Nemotron-CC-Code-v1은 Common Crawl 코드 페이지에서 추출한 고품질 코드 사전학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
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
# nvidia/Nemotron-CC-Code-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-CC-Code-v1)

Nemotron-CC-Code-v1은 Common Crawl 코드 페이지에서 추출한 고품질 코드 사전학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `high-quality Code pretraining dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `processed text extracted from Common Crawl Code pages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `processed text extracted from Common Crawl Code pages` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English Common Crawl, and large-scale synthetic corpora` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `high-quality Code pretraining dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[nvidia__NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16|nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16]]
- [[nvidia__Nemotron-Labs-TwoTower-30B-A3B-Base-BF16|nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16]]
