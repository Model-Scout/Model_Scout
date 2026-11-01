---
type: "dataset"
id: "nmixx-fin/twice_dart_company2industry_clustering"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_dart_company2industry_clustering"
downloads: 13
summary: "DART 사업보고서 요약문 기반 산업 클러스터링 데이터셋으로 5개 산업군 분류용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/twice_dart_company2industry_clustering

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_dart_company2industry_clustering)

DART 사업보고서 요약문 기반 산업 클러스터링 데이터셋으로 5개 산업군 분류용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `summary sentences of the DART business reports` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `industry labels were limited to five categories` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Constructed an industry clustering dataset based on the summary sentences of the DART business reports.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
