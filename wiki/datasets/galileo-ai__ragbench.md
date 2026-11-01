---
type: "dataset"
id: "galileo-ai/ragbench"
source: "huggingface"
url: "https://huggingface.co/datasets/galileo-ai/ragbench"
downloads: 4354
summary: "RAGBench는 5개 산업 도메인과 다양한 RAG 작업 유형을 포함한 10만 예제 대규모 RAG 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# galileo-ai/ragbench

> dataset · [Hugging Face](https://huggingface.co/datasets/galileo-ai/ragbench)

RAGBench는 5개 산업 도메인과 다양한 RAG 작업 유형을 포함한 10만 예제 대규모 RAG 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `RAG task types` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `RAG task types` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `RAGBench examples are sourced from industry corpora such as user manuals` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `RAG task types` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `168` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `five unique industry-specific domains` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `each one split into train/validation/test splits` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `overall_supported_explanation` 열 p90 670자 ≈ 168 토큰 (viewer statistics, covidqa/validation)

## 이 데이터로 학습한 모델

- [[martinsu__tildeopen-30b-mu-instruct|martinsu/tildeopen-30b-mu-instruct]]
