---
type: "dataset"
id: "BidirLM/BidirLM-Omni-Contrastive"
source: "huggingface"
url: "https://huggingface.co/datasets/BidirLM/BidirLM-Omni-Contrastive"
downloads: 101
summary: "BidirLM-Omni-Contrastive는 텍스트, 이미지, 오디오 등 다양한 모달리티의 대조 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[이미지 (출력 형식)|이미지]]"
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
  - "[[대규모 데이터]]"
---
# BidirLM/BidirLM-Omni-Contrastive

> dataset · [Hugging Face](https://huggingface.co/datasets/BidirLM/BidirLM-Omni-Contrastive)

BidirLM-Omni-Contrastive는 텍스트, 이미지, 오디오 등 다양한 모달리티의 대조 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — tag_match · tags = `retrieval` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `Audio ↔ Text` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Image ↔ Text` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Text ↔ Text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `Audio ↔ Text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Image ↔ Text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Text ↔ Text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repository serves as the centralized documentation and integration hub for the omnimodal contrastive datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[BidirLM__BidirLM-Omni-2.5B-Embedding|BidirLM/BidirLM-Omni-2.5B-Embedding]]
