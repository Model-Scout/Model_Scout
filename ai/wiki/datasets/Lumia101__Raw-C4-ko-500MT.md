---
type: "dataset"
id: "Lumia101/Raw-C4-ko-500MT"
source: "huggingface"
url: "https://huggingface.co/datasets/Lumia101/Raw-C4-ko-500MT"
downloads: 24
summary: "allenai/c4에서 필터링 없이 5억 토큰을 추출한 한국어 데이터셋으로 필터링 효과 측정용임."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Lumia101/Raw-C4-ko-500MT

> dataset · [Hugging Face](https://huggingface.co/datasets/Lumia101/Raw-C4-ko-500MT)

allenai/c4에서 필터링 없이 5억 토큰을 추출한 한국어 데이터셋으로 필터링 효과 측정용임.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This dataset was created to measure the effect of filtering applied to Lumia101/Nari-C4-ko-500MT` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `500M tokens were extracted from the allenai/c4 without any additional filtering` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `500M tokens were extracted from the allenai/c4 without any additional filtering` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11389` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was created to measure the effect of filtering applied to Lumia101/Nari-C4-ko-500MT` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 17084자 ≈ 11389 토큰 (viewer statistics, default/train)
