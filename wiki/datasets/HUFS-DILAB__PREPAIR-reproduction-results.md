---
type: "dataset"
id: "HUFS-DILAB/PREPAIR-reproduction-results"
source: "huggingface"
url: "https://huggingface.co/datasets/HUFS-DILAB/PREPAIR-reproduction-results"
downloads: 11
summary: "PREPAIR 방법의 재현 결과를 담은 데이터셋입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HUFS-DILAB/PREPAIR-reproduction-results

> dataset · [Hugging Face](https://huggingface.co/datasets/HUFS-DILAB/PREPAIR-reproduction-results)

PREPAIR 방법의 재현 결과를 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset contains the reproduction results of the PREPAIR method.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `Target File: results_LLMBar_all_methods.csv` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Target File: results_LLMBar_all_methods.csv` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Source Project: PREPAIR` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
