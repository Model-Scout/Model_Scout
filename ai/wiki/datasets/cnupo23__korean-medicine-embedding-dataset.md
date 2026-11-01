---
type: "dataset"
id: "cnupo23/korean-medicine-embedding-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset"
downloads: 103
summary: "한의학 용어와 온톨로지를 활용한 임베딩 학습용 대조학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cnupo23/korean-medicine-embedding-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)

한의학 용어와 온톨로지를 활용한 임베딩 학습용 대조학습 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · tags, task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Each example is a query–positive–negatives triplet built from KM terminology resources and a curated KM ontology` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each example is a query–positive–negatives triplet` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `domain-adapted text embedding models for Korean Medicine (KM, 한의학)` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 11자 ≈ 8 토큰 (viewer statistics, default/train)
