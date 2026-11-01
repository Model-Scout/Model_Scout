---
type: "dataset"
id: "davidkim205/kollm-converations"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/kollm-converations"
downloads: 40
summary: "한국어 대화 형식 통합 데이터셋으로 SFT 학습에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# davidkim205/kollm-converations

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/kollm-converations)

한국어 대화 형식 통합 데이터셋으로 SFT 학습에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `conversations format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `conversations format` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `using the Korean dataset currently available on huggingface and github.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is an integrated dataset created in conversations format for SFT learning` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
