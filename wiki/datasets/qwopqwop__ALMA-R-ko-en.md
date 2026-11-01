---
type: "dataset"
id: "qwopqwop/ALMA-R-ko-en"
source: "huggingface"
url: "https://huggingface.co/datasets/qwopqwop/ALMA-R-ko-en"
downloads: 18
summary: "FLORES-200 기반 한국어-영어 번역 평가용 삼중 선호 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# qwopqwop/ALMA-R-ko-en

> dataset · [Hugging Face](https://huggingface.co/datasets/qwopqwop/ALMA-R-ko-en)

FLORES-200 기반 한국어-영어 번역 평가용 삼중 선호 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `For each direction, we provide a source sentence along with three translations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `For each direction, we provide a source sentence along with three translations` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The triplet prference data, supporting 2 translation directions, is built upon the FLORES-200 development and test data.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The triplet prference data, supporting 2 translation directions, is built upon the FLORES-200 development and test data.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
