---
type: "dataset"
id: "DataDrivenConstruction/cwicr-construction-rates"
source: "huggingface"
url: "https://huggingface.co/datasets/DataDrivenConstruction/cwicr-construction-rates"
downloads: 1215
summary: "30개국 건설 작업, 자원, 비용 정보를 다국어로 제공하는 기계 판독 가능 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# DataDrivenConstruction/cwicr-construction-rates

> dataset · [Hugging Face](https://huggingface.co/datasets/DataDrivenConstruction/cwicr-construction-rates)

30개국 건설 작업, 자원, 비용 정보를 다국어로 제공하는 기계 판독 가능 데이터베이스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `the cwicr-vector-db-bgem3-v3 Qdrant snapshots` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Use the vector DB repository when you need semantic search over rate descriptions.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `This dataset is the tabular source-of-truth behind the cwicr-vector-db-bgem3-v3 Qdrant snapshots.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset is the tabular source-of-truth behind the cwicr-vector-db-bgem3-v3 Qdrant snapshots.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `46` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual, machine-readable database of national construction rate books for 30 countries / language locales.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `rate_original_name` 열 p90 184자 ≈ 46 토큰 (viewer statistics, default/en)
