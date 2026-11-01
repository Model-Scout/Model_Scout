---
type: "dataset"
id: "peterkirby/pan2020_dict_author_fandom_doc"
source: "huggingface"
url: "https://huggingface.co/datasets/peterkirby/pan2020_dict_author_fandom_doc"
downloads: 155
summary: "팬픽션 작가-팬덤 분리 학습/검증 데이터로 저자 검증 연구에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# peterkirby/pan2020_dict_author_fandom_doc

> dataset · [Hugging Face](https://huggingface.co/datasets/peterkirby/pan2020_dict_author_fandom_doc)

팬픽션 작가-팬덤 분리 학습/검증 데이터로 저자 검증 연구에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `The training data is one row per document to allow easy recombination` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The PAN21 validation and test splits consist of fixed document pairs for consistent scoring` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `25871` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PAN 2020 / PAN 2021 fanfiction authorship verification data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The training data has been pre-split into Train and Validation under Author-Fandom-Disjoint constraints` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 103483자 ≈ 25871 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Baragi-AI__Munche-768|Baragi-AI/Munche-768]]
