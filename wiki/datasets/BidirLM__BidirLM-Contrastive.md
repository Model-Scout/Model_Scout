---
type: "dataset"
id: "BidirLM/BidirLM-Contrastive"
source: "huggingface"
url: "https://huggingface.co/datasets/BidirLM/BidirLM-Contrastive"
downloads: 1148
summary: "BidirLM-Contrastive는 79개 데이터셋에서 1천만 쿼리-문서 쌍을 포함한 임베딩 모델 학습용 대조 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# BidirLM/BidirLM-Contrastive

> dataset · [Hugging Face](https://huggingface.co/datasets/BidirLM/BidirLM-Contrastive)

BidirLM-Contrastive는 79개 데이터셋에서 1천만 쿼리-문서 쌍을 포함한 임베딩 모델 학습용 대조 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `query-document pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Positive (relevant) document IDs` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `53 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `covering three sources: Nemotron, KaLM, and parallel/other data.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The contrastive training dataset used to train BidirLM Embedding models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
