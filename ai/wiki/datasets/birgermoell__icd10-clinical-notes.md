---
type: "dataset"
id: "birgermoell/icd10-clinical-notes"
source: "huggingface"
url: "https://huggingface.co/datasets/birgermoell/icd10-clinical-notes"
downloads: 198
summary: "34개 언어로 된 ICD-10 진단 코드와 임상 기록 노트 데이터셋으로 분류기 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# birgermoell/icd10-clinical-notes

> dataset · [Hugging Face](https://huggingface.co/datasets/birgermoell/icd10-clinical-notes)

34개 언어로 된 ICD-10 진단 코드와 임상 기록 노트 데이터셋으로 분류기 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Sentence Embeddings (multilingual-MiniLM)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `clinical journal notes (English and Swedish)` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Train/test splits for classifier training` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `name` 열 p90 35자 ≈ 9 토큰 (viewer statistics, default/test)

## 같은 데이터의 사본·중복 등록

- `Danishaqil/icd10-clinical-notes`
