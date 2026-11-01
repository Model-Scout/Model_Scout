---
type: "dataset"
id: "nvidia/Nemotron-Pretraining-Specialized-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1"
downloads: 6772
summary: "Nemotron-Pretraining-Specialized-v1은 NVIDIA Nemotron 3 LLM 학습용 수학, 코드, 영어 웹, 합성 데이터셋입니다."
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
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nvidia/Nemotron-Pretraining-Specialized-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1)

Nemotron-Pretraining-Specialized-v1은 NVIDIA Nemotron 3 LLM 학습용 수학, 코드, 영어 웹, 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `Designed for the NVIDIA Nemotron 3 family of LLMs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `processed text extracted from Common Crawl Code pages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `synthetic data created using the following models` · 신뢰도 medium
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `26245` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `specialized STEM reasoning datasets` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `English Common Crawl, and large-scale synthetic corpora` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `providing an expanded, modern foundation for training leading LLMs` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 104982자 ≈ 26245 토큰 (viewer statistics, Nemotron-Pretraining-InfiniByte-Reasoning/train)

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
- [[nvidia__NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16|nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16]]
- [[nvidia__Nemotron-Labs-TwoTower-30B-A3B-Base-BF16|nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16]]
