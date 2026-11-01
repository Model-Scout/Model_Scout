---
type: "dataset"
id: "maremo2/saju-calendar-data"
source: "huggingface"
url: "https://huggingface.co/datasets/maremo2/saju-calendar-data"
downloads: 63
summary: "1900~2100년 사주 만세력 데이터로 절기, 음력, 띠 경계 정보를 제공합니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# maremo2/saju-calendar-data

> dataset · [Hugging Face](https://huggingface.co/datasets/maremo2/saju-calendar-data)

1900~2100년 사주 만세력 데이터로 절기, 음력, 띠 경계 정보를 제공합니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `명리연구소의 만세력이 계산하는 표 세 가지를 CSV 로 공개합니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `CSV 로 공개합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `CSV 로 공개합니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Three tables computed by the Korean saju (Four Pillars) calendar engine` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `명리연구소의 만세력이 계산하는 표 세 가지를 CSV 로 공개합니다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
