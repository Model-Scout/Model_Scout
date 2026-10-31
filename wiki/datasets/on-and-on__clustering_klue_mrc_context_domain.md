---
type: "dataset"
id: "on-and-on/clustering_klue_mrc_context_domain"
source: "huggingface"
url: "https://huggingface.co/datasets/on-and-on/clustering_klue_mrc_context_domain"
downloads: 25
summary: "KLUE-MRC 데이터셋 카테고리로 처리된 임베딩 평가용 클러스터링 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[교육]]"
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# on-and-on/clustering_klue_mrc_context_domain

> dataset · [Hugging Face](https://huggingface.co/datasets/on-and-on/clustering_klue_mrc_context_domain)

KLUE-MRC 데이터셋 카테고리로 처리된 임베딩 평가용 클러스터링 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `It is a dataset for embedding evaluation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `- Task: Clustering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `It is a dataset for embedding evaluation, processed using the categories from the KLUE-MRC dataset.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `It is a dataset for embedding evaluation, processed using the categories from the KLUE-MRC dataset.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1076` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Domain: Game / Media / Automotive / Finance / Real Estate / Education` · 신뢰도 low
- **도메인**: [[교육]] — ner · readme = `Domain: Game / Media / Automotive / Finance / Real Estate / Education` · 신뢰도 medium
- **도메인**: [[금융·경제]] — ner · readme = `Domain: Game / Media / Automotive / Finance / Real Estate / Education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a processed and redistributed version of the KLUE dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1614자 ≈ 1076 토큰 (viewer statistics, kor-Hang/test)
