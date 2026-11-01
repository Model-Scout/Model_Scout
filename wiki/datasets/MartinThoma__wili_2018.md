---
type: "dataset"
id: "MartinThoma/wili_2018"
source: "huggingface"
url: "https://huggingface.co/datasets/MartinThoma/wili_2018"
downloads: 821
summary: "WiLI-2018은 235개 언어의 문단 235,000개로 구성된 위키피디아 언어 식별 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MartinThoma/wili_2018

> dataset · [Hugging Face](https://huggingface.co/datasets/MartinThoma/wili_2018)

WiLI-2018은 235개 언어의 문단 235,000개로 구성된 위키피디아 언어 식별 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `235000 paragraphs of 235 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `label` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `232 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4429` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odbl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia language identification benchmark dataset` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `a train-test split is provided` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 17716자 ≈ 4429 토큰 (viewer statistics, WiLI-2018 dataset/test)
