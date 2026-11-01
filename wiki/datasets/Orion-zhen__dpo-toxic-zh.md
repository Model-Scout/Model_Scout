---
type: "dataset"
id: "Orion-zhen/dpo-toxic-zh"
source: "huggingface"
url: "https://huggingface.co/datasets/Orion-zhen/dpo-toxic-zh"
downloads: 28
summary: "DPO Toxic Chinese v2.0은 모델의 검열/정렬을 우회하는 고독성·유해 텍스트 데이터셋이다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Orion-zhen/dpo-toxic-zh

> dataset · [Hugging Face](https://huggingface.co/datasets/Orion-zhen/dpo-toxic-zh)

DPO Toxic Chinese v2.0은 모델의 검열/정렬을 우회하는 고독성·유해 텍스트 데이터셋이다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `数据集中文本包含的内容和观点与我完全无关, 它们只是大模型生成的文字` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `数据集中文本包含的内容和观点与我完全无关, 它们只是大模型生成的文字` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `158` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `这是一个高度毒性, 高度有害的数据集, 意在展示DPO是如何破除模型的审核/对齐的` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `这个数据集被设计用于学术研究, 而非其他恶意场景` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 632자 ≈ 158 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Orion-zhen__Qwen2.5-7B-Instruct-Uncensored|Orion-zhen/Qwen2.5-7B-Instruct-Uncensored]]
- [[enet45__Qwen2.5-7B-Instruct-Uncensored-mlx-8Bit|enet45/Qwen2.5-7B-Instruct-Uncensored-mlx-8Bit]]
