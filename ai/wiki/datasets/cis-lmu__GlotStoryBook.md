---
type: "dataset"
id: "cis-lmu/GlotStoryBook"
source: "huggingface"
url: "https://huggingface.co/datasets/cis-lmu/GlotStoryBook"
downloads: 196
summary: "180개 언어의 동화책 병렬 데이터셋으로 다국어 문서 비교 및 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
  - "[[번역]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cis-lmu/GlotStoryBook

> dataset · [Hugging Face](https://huggingface.co/datasets/cis-lmu/GlotStoryBook)

180개 언어의 동화책 병렬 데이터셋으로 다국어 문서 비교 및 연구에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `The Parallel ID or parallel_id can be used to find the parallel documents in different languages and build a parallel dataset.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The Parallel ID or parallel_id can be used to find the parallel documents in different languages and build a parallel dataset.` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:retrieval, task:summarization, task:translation = `Story Books for 180 ISO-639-3 codes.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization, task:translation = `Story Books for 180 ISO-639-3 codes.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `178 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `243` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Story Books for 180 ISO-639-3 codes.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Text` 열 p90 971자 ≈ 243 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[cis-lmu__glotlid|cis-lmu/glotlid]]
