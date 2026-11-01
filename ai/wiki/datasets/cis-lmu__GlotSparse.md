---
type: "dataset"
id: "cis-lmu/GlotSparse"
source: "huggingface"
url: "https://huggingface.co/datasets/cis-lmu/GlotSparse"
downloads: 40
summary: "저자원이용 언어 뉴스 웹사이트 모음 데이터셋으로 언어 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cis-lmu/GlotSparse

> dataset · [Hugging Face](https://huggingface.co/datasets/cis-lmu/GlotSparse)

저자원이용 언어 뉴스 웹사이트 모음 데이터셋으로 언어 연구에 활용됨.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Collection of news websites in low-resource languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Collection of news websites in low-resource languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Collection of news websites in low-resource languages.` · 신뢰도 low
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `Collection of news websites in low-resource languages.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `All the sources related to news, social media, and without mentioned datasets are crawled and compiled in this work.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[cis-lmu__glotlid|cis-lmu/glotlid]]
