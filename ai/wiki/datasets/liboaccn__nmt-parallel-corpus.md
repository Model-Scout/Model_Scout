---
type: "dataset"
id: "liboaccn/nmt-parallel-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/liboaccn/nmt-parallel-corpus"
downloads: 58
summary: "OPUS 프로젝트에서 추출한 60개 언어, 1900개 이상 언어쌍의 신경망 기계번역 병렬 말뭉치 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[언어 모델링]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# liboaccn/nmt-parallel-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/liboaccn/nmt-parallel-corpus)

OPUS 프로젝트에서 추출한 60개 언어, 1900개 이상 언어쌍의 신경망 기계번역 병렬 말뭉치 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `High-quality parallel corpora are essential for training powerful NMT models.` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling, task:translation = `only customized plain-text files in Moses format are retained.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:translation = `only customized plain-text files in Moses format are retained.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `63 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a renowned platform for parallel corpora, and create a multilingual dataset.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `High-quality parallel corpora are essential for training powerful NMT models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `99999999999.0` · 신뢰도 high
