---
type: "dataset"
id: "androidli/toolve-colour-atlas"
source: "huggingface"
url: "https://huggingface.co/datasets/androidli/toolve-colour-atlas"
downloads: 84
summary: "다국어 색상 이름, 개념-색상 매핑, 문화유산 팔레트를 포함한 기계 판독 가능한 색상 아틀라스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# androidli/toolve-colour-atlas

> dataset · [Hugging Face](https://huggingface.co/datasets/androidli/toolve-colour-atlas)

다국어 색상 이름, 개념-색상 매핑, 문화유산 팔레트를 포함한 기계 판독 가능한 색상 아틀라스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multilingual colour names (Chinese / Japanese / Korean traditional vocabularies, not just English)` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `concept→colour table (what colour a word like 生气 or 侘寂 evokes)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Live lookups (10 languages, in-browser)` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `palettes extracted from public-domain museum objects together with their material and provenance metadata` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `multilingual colour names (Chinese / Japanese / Korean traditional vocabularies, not just English)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `colour names, concept→colour` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `palettes extracted from public-domain museum objects together with their material and provenance metadata` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A machine-readable colour atlas with three parts that are hard to find together` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
