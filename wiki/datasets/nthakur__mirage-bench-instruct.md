---
type: "dataset"
id: "nthakur/mirage-bench-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/nthakur/mirage-bench-instruct"
downloads: 100
summary: "MIRAGE-Bench Instruct는 16개 언어의 질의에 대해 5개 모델의 구조화된 RAG 출력을 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nthakur/mirage-bench-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/nthakur/mirage-bench-instruct)

MIRAGE-Bench Instruct는 16개 언어의 질의에 대해 5개 모델의 구조화된 RAG 출력을 포함한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `an instruction-following prompt` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `queries in the `train` split` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The answers have been generated` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `426` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIRAGE-Bench (or MIRACL) for 16 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `queries in the `train` split of MIRAGE-Bench` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 1704자 ≈ 426 토큰 (viewer statistics, ko/train)
