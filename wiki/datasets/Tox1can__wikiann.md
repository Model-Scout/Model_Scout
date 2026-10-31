---
type: "dataset"
id: "Tox1can/wikiann"
source: "huggingface"
url: "https://huggingface.co/datasets/Tox1can/wikiann"
downloads: 479
summary: "WikiANN은 위키피디아 문서에 LOC, PER, ORG 개체명 태그가 달린 다국어 개체명 인식 데이터셋입니다."
readme_status: "template"
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
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Tox1can/wikiann

> dataset · [Hugging Face](https://huggingface.co/datasets/Tox1can/wikiann)

WikiANN은 위키피디아 문서에 LOC, PER, ORG 개체명 태그가 달린 다국어 개체명 인식 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories, task_ids = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Wikipedia articles` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `annotated with LOC (location), PER (person), and ORG (organisation) tags in the IOB2 format` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `173 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia articles` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `balanced train, dev, and test splits of Rahimi et al. (2019)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
