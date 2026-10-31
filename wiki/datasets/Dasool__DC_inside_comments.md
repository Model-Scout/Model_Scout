---
type: "dataset"
id: "Dasool/DC_inside_comments"
source: "huggingface"
url: "https://huggingface.co/datasets/Dasool/DC_inside_comments"
downloads: 54
summary: "DC Inside에서 수집한 11만 개의 원시 댓글 데이터로 비지도 학습 및 사전학습용입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Dasool/DC_inside_comments

> dataset · [Hugging Face](https://huggingface.co/datasets/Dasool/DC_inside_comments)

DC Inside에서 수집한 11만 개의 원시 댓글 데이터로 비지도 학습 및 사전학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `It is intended for unsupervised learning or pretraining purposes.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `This dataset contains 110,000 raw comments` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `This dataset contains 110,000 raw comments` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `55` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains 110,000 raw comments collected from DC Inside.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is intended for unsupervised learning or pretraining purposes.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `comments` 열 p90 82자 ≈ 55 토큰 (viewer statistics, default/train)
