---
type: "dataset"
id: "saillab/alpaca_korean_taco"
source: "huggingface"
url: "https://huggingface.co/datasets/saillab/alpaca_korean_taco"
downloads: 26
summary: "TaCo 논문 스타일을 따른 한국어 Alpaca-52k 데이터셋으로 연구용으로 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# saillab/alpaca_korean_taco

> dataset · [Hugging Face](https://huggingface.co/datasets/saillab/alpaca_korean_taco)

TaCo 논문 스타일을 따른 한국어 Alpaca-52k 데이터셋으로 연구용으로 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This repository contains the dataset used for the TaCo paper.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `"output": "Instruction in English: instruction in en , Response in English: response in en , Response in xx: response in xx "` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2135` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains the dataset used for the TaCo paper.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3203자 ≈ 2135 토큰 (viewer statistics, default/test)
