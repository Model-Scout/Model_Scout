---
type: "dataset"
id: "prismdata/Perdix-Pretrain-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/prismdata/Perdix-Pretrain-Data"
downloads: 183
summary: "Perdix-1.1B-Base 사전학습에 쓴 공개 데이터셋의 parquet 파일 모음 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
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
# prismdata/Perdix-Pretrain-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/prismdata/Perdix-Pretrain-Data)

Perdix-1.1B-Base 사전학습에 쓴 공개 데이터셋의 parquet 파일 모음 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Perdix-1.1B-Base 사전학습에 쓴 원본 데이터를 그대로 모아 둔 것입니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `학습에는 `text` 컬럼만 썼습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `학습에는 `text` 컬럼만 썼습니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `19485` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `web` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Perdix-1.1B-Base 사전학습에 쓴 원본 데이터를 그대로 모아 둔 것입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 29227자 ≈ 19485 토큰 (viewer statistics, korean/train)

## 이 데이터로 학습한 모델

- [[prismdata__Perdix-1.1B-Base|prismdata/Perdix-1.1B-Base]]
