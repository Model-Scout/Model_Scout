---
type: "dataset"
id: "saillab/taco-datasets"
source: "huggingface"
url: "https://huggingface.co/datasets/saillab/taco-datasets"
downloads: 318
summary: "TaCo 논문에서 사용된 다국어 GPT-4 기반 데이터셋 모음으로, 학술 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# saillab/taco-datasets

> dataset · [Hugging Face](https://huggingface.co/datasets/saillab/taco-datasets)

TaCo 논문에서 사용된 다국어 GPT-4 기반 데이터셋 모음으로, 학술 연구용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Multilingual Alpaca-52K GPT-4 dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Multilingual Alpaca-52K GPT-4 dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Multilingual Alpaca-52K GPT-4 dataset` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `127 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `403` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repo consists of the datasets used for the TaCo paper.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repo consists of the datasets used for the TaCo paper.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1611자 ≈ 403 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `saillab/testalpaca_sanskrit_taco`
