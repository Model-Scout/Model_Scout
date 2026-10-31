---
type: "dataset"
id: "universal-dependencies/universal_dependencies"
source: "huggingface"
url: "https://huggingface.co/datasets/universal-dependencies/universal_dependencies"
downloads: 6384
summary: "Universal Dependencies Treebank은 다국어 구문 분석과 형태소 분석을 위한 일관된 트리뱅크 주석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# universal-dependencies/universal_dependencies

> dataset · [Hugging Face](https://huggingface.co/datasets/universal-dependencies/universal_dependencies)

Universal Dependencies Treebank은 다국어 구문 분석과 형태소 분석을 위한 일관된 트리뱅크 주석 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset supports dependency parsing, universal and language-specific part-of-speech tagging, lemmatization, and morphology-oriented token classification.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `193 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `21` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Universal Dependencies is a project that seeks to develop cross-linguistically consistent treebank annotation for many languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This Hugging Face distribution packages official Universal Dependencies release snapshots as Parquet configurations` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 84자 ≈ 21 토큰 (viewer statistics, ko_gsd/test)
