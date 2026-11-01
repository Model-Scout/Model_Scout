---
type: "dataset"
id: "devngho/ko_llm_annotations"
source: "huggingface"
url: "https://huggingface.co/datasets/devngho/ko_llm_annotations"
downloads: 14
summary: "fineweb-edu 방법을 한국어에 적용한 합성 데이터셋으로, v3 사용 권장"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# devngho/ko_llm_annotations

> dataset · [Hugging Face](https://huggingface.co/datasets/devngho/ko_llm_annotations)

fineweb-edu 방법을 한국어에 적용한 합성 데이터셋으로, v3 사용 권장

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `This synthetic dataset was created to apply the methods of fineweb-edu to Korean datasets.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `source: HAERAE-HUB/KOREAN-WEBTEXT, sampled 500k` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `generation time: ~42 hrs` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `fineweb-edu의 방법을 한국어에 적용하기 위해 만들어진 합성 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 fineweb-edu의 방법을 한국어에 적용하기 위해 만들어진 합성 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
