---
type: "dataset"
id: "jaeminyx-stoa/korean-saju-element-distribution"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeminyx-stoa/korean-saju-element-distribution"
downloads: 14
summary: "1966~2010년 한국 사주(오행) 8글자별 오행 분포를 계산한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jaeminyx-stoa/korean-saju-element-distribution

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeminyx-stoa/korean-saju-element-distribution)

1966~2010년 한국 사주(오행) 8글자별 오행 분포를 계산한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `counted Korean Four Pillars data is not.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `One CSV, 693 rows, 10 columns.` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `One CSV, 693 rows, 10 columns.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Four Pillars content is everywhere; counted Korean Four Pillars data is not.` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Summary JSON API: https://sortia-ai.com/api/backend/v1/public/element-statistics` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
