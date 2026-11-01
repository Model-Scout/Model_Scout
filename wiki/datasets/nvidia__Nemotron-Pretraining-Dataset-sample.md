---
type: "dataset"
id: "nvidia/Nemotron-Pretraining-Dataset-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample"
downloads: 921
summary: "Nemotron-Pretraining-Dataset는 수학, 코드, 다국어 Q&A를 포함한 생성형 AI 모델 학습용 데이터셋입니다."
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nvidia/Nemotron-Pretraining-Dataset-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample)

Nemotron-Pretraining-Dataset는 수학, 코드, 다국어 Q&A를 포함한 생성형 AI 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This pretraining dataset, for generative AI model training` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `pretraining dataset` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `diverse multilingual Q&A` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:question_answering = `math and code while enriching it with diverse multilingual Q&A` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `diverse multilingual Q&A` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1579` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `high-value math and code` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `diverse multilingual Q&A` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This pretraining dataset, for generative AI model training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 6315자 ≈ 1579 토큰 (viewer statistics, Nemotron-CC-Diverse-QA/train)

## 이 데이터로 학습한 모델

- [[nvidia__NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16|nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16]]
- [[nvidia__NVIDIA-Nemotron-Nano-12B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base]]
- [[nvidia__NVIDIA-Nemotron-Nano-9B-v2-Base|nvidia/NVIDIA-Nemotron-Nano-9B-v2-Base]]
- [[nvidia__Nemotron-Labs-TwoTower-30B-A3B-Base-BF16|nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16]]
