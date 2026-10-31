---
type: "dataset"
id: "gbenson/webui-dom-snapshots"
source: "huggingface"
url: "https://huggingface.co/datasets/gbenson/webui-dom-snapshots"
downloads: 203
summary: "WebUI DOM 스냅샷 데이터셋으로 웹 UI 분석에 활용됨."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[소규모 데이터]]"
---
# gbenson/webui-dom-snapshots

> dataset · [Hugging Face](https://huggingface.co/datasets/gbenson/webui-dom-snapshots)

WebUI DOM 스냅샷 데이터셋으로 웹 UI 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `WebUI DOM snapshots` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `WebUI DOM snapshots` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `WebUI DOM snapshots` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `WebUI DOM snapshots` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `41 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Languages: Mostly English (87%); Dutch, French, Chinese, Japanese (1-2% each); 30+ others (<1% each)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset card aims to be a base template for new datasets.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
