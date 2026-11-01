---
type: "dataset"
id: "saillab/alpaca-korean-cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/saillab/alpaca-korean-cleaned"
downloads: 70
summary: "TaCo 논문에 사용된 한국어 Alpaca-52k 데이터셋으로 연구용 번역 데이터입니다."
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
# saillab/alpaca-korean-cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/saillab/alpaca-korean-cleaned)

TaCo 논문에 사용된 한국어 Alpaca-52k 데이터셋으로 연구용 번역 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This repository contains the dataset used for the TaCo paper.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The original dataset [(Alpaca-52K)](https://github.com/tatsu-lab/stanford_alpaca?tab=readme-ov-file#data-release) was translated using Google Translate.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The original dataset [(Alpaca-52K)](https://github.com/tatsu-lab/stanford_alpaca?tab=readme-ov-file#data-release) was translated using Google Translate.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `541` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains the dataset used for the TaCo paper.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 812자 ≈ 541 토큰 (viewer statistics, default/test)
