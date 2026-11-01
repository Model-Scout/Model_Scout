---
type: "dataset"
id: "williamjeong2/msmarco-triplets-ko-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/williamjeong2/msmarco-triplets-ko-v2"
downloads: 15
summary: "MS MARCO Triplets 원본을 한국어로 번역한 대규모 정보 검색용 데이터셋입니다."
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
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# williamjeong2/msmarco-triplets-ko-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/williamjeong2/msmarco-triplets-ko-v2)

MS MARCO Triplets 원본을 한국어로 번역한 대규모 정보 검색용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The MS MARCO (Microsoft Machine Reading Comprehension) Triplets dataset is a large-scale dataset designed for information retrieval tasks.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Queries: Questions or search queries in Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Positive Documents: Relevant passages or documents translated into Korean` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `facilitating natural language processing and information retrieval research for the Korean language community.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Large-scale dataset suitable for machine learning model training` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
