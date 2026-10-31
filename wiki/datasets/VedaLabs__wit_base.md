---
type: "dataset"
id: "VedaLabs/wit_base"
source: "huggingface"
url: "https://huggingface.co/datasets/VedaLabs/wit_base"
downloads: 547
summary: "Wikimedia에서 제공하는 다국어 위키피디아 이미지-텍스트 연관 데이터셋으로 이미지 캡션 생성과 텍스트 검색에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
  - "[[대규모 데이터]]"
---
# VedaLabs/wit_base

> dataset · [Hugging Face](https://huggingface.co/datasets/VedaLabs/wit_base)

Wikimedia에서 제공하는 다국어 위키피디아 이미지-텍스트 연관 데이터셋으로 이미지 캡션 생성과 텍스트 검색에 활용됨.

## 분류

- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Each instance is an image, its representation in bytes` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval, task:visual_qa = `a large curated set of more than 37 million image-text associations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `105 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `extracted from Wikipedia articles in 108 languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The core training data is taken from the Wikipedia Image-Text (WIT) Dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
