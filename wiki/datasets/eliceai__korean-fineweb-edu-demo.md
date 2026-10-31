---
type: "dataset"
id: "eliceai/korean-fineweb-edu-demo"
source: "huggingface"
url: "https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo"
downloads: 97
summary: "FineWeb-Edu 영문 교육용 웹 텍스트를 한국어로 번역한 고품질 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
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
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# eliceai/korean-fineweb-edu-demo

> dataset · [Hugging Face](https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo)

FineWeb-Edu 영문 교육용 웹 텍스트를 한국어로 번역한 고품질 교육용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `거대 언어 모델(LLM)이 학술적이고 교육적인 도메인에서 한국어 성능을 높일 수 있도록 설계되었습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = ``text` (string)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `고품질 교육용 한국어 데이터를 제공합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3184` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = ``text` (string) 피처를 가진 단일 `train` split.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 4776자 ≈ 3184 토큰 (viewer statistics, default/train)
