---
type: "dataset"
id: "HuggingFaceFW/fineweb"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceFW/fineweb"
downloads: 365588
summary: "FineWeb은 CommonCrawl 기반의 18.5조 토큰 규모 영어 웹 데이터로 LLM 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# HuggingFaceFW/fineweb

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceFW/fineweb)

FineWeb은 CommonCrawl 기반의 18.5조 토큰 규모 영어 웹 데이터로 LLM 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `models trained on our dataset also outperform models trained on other commonly used high quality web datasets` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `The data processing pipeline is optimized for LLM performance` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling = `english web data from CommonCrawl` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `models trained on our dataset also outperform models trained on other commonly used high quality web datasets` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `english web data from CommonCrawl` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `99999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Horizon-Labs__multilingual-embedding-base|Horizon-Labs/multilingual-embedding-base]]
- [[Horizon-Labs__multilingual-embedding-small|Horizon-Labs/multilingual-embedding-small]]
- [[Horizon-Labs__multilingual-sentiment-base|Horizon-Labs/multilingual-sentiment-base]]
- [[Horizon-Labs__multilingual-sentiment-small|Horizon-Labs/multilingual-sentiment-small]]
- [[PsycheFoundation__consilience-40b-7Y9v38s5|PsycheFoundation/consilience-40b-7Y9v38s5]]
- [[WaveCut__Qwen3.5-2B-MLX-DWQ-4bit|WaveCut/Qwen3.5-2B-MLX-DWQ-4bit]]
- [[ikhou__dict-xs|ikhou/dict-xs]]
