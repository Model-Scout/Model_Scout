---
type: "dataset"
id: "HPLT/DocHPLT"
source: "huggingface"
url: "https://huggingface.co/datasets/HPLT/DocHPLT"
downloads: 10460
summary: "DocHPLT는 50개 언어와 영어 간 문서 단위 번역을 위한 대규모 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# HPLT/DocHPLT

> dataset · [Hugging Face](https://huggingface.co/datasets/HPLT/DocHPLT)

DocHPLT는 50개 언어와 영어 간 문서 단위 번역을 위한 대규모 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `LLMs fine-tuned on DocHPLT substantially outperform off-the-shelf instruction- tuned baselines` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `124 million aligned document pairs across 50 languages paired with English, comprising 4.26 billion sentences` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `document-level translation dataset` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `to facilitate the training and evaluation of document-level translation and, more broadly, long-context modeling for global communities` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `to facilitate the training and evaluation of document-level translation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
