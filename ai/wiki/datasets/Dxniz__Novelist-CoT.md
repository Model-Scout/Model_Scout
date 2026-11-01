---
type: "dataset"
id: "Dxniz/Novelist-CoT"
source: "huggingface"
url: "https://huggingface.co/datasets/Dxniz/Novelist-CoT"
downloads: 140
summary: "Novelist-CoT는 장편 창작 글쓰기 데이터셋으로, 스타일 중심 내러티브 생성과 감독 학습에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Dxniz/Novelist-CoT

> dataset · [Hugging Face](https://huggingface.co/datasets/Dxniz/Novelist-CoT)

Novelist-CoT는 장편 창작 글쓰기 데이터셋으로, 스타일 중심 내러티브 생성과 감독 학습에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `instruction + input + output` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `final prose` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6153` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Novelist-CoT is a long-form creative writing dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `designed for supervised fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 24611자 ≈ 6153 토큰 (viewer statistics, default/train)
