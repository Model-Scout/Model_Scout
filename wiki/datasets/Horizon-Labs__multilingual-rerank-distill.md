---
type: "dataset"
id: "Horizon-Labs/multilingual-rerank-distill"
source: "huggingface"
url: "https://huggingface.co/datasets/Horizon-Labs/multilingual-rerank-distill"
downloads: 131
summary: "47개 언어의 334,400개 검색 쿼리와 5.35M 쌍의 Qwen3-Reranker-4B 점수로 다국어 리랭킹 모델 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Horizon-Labs/multilingual-rerank-distill

> dataset · [Hugging Face](https://huggingface.co/datasets/Horizon-Labs/multilingual-rerank-distill)

47개 언어의 334,400개 검색 쿼리와 5.35M 쌍의 Qwen3-Reranker-4B 점수로 다국어 리랭킹 모델 학습용 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Use it to train or distil rerankers and embedding models.` · 신뢰도 medium
- **작업**: [[리랭킹]] — metadata · readme, tags, task_categories = `text-ranking` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking, task:retrieval = `334,400 search queries in 47 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a relevance score from Qwen3-Reranker-4B for every (query, passage) pair` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `185` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `web-search instruction` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The training data of Horizon-Labs/multilingual-reranker-small and -base` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 742자 ≈ 185 토큰 (viewer statistics, passages/train)
