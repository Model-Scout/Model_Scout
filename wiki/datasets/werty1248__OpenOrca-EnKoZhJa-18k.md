---
type: "dataset"
id: "werty1248/OpenOrca-EnKoZhJa-18k"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/OpenOrca-EnKoZhJa-18k"
downloads: 36
summary: "OpenOrca의 영어-한국어-중국어-일본어 번역 데이터셋으로 다국어 번역에 활용됨."
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
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
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
# werty1248/OpenOrca-EnKoZhJa-18k

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/OpenOrca-EnKoZhJa-18k)

OpenOrca의 영어-한국어-중국어-일본어 번역 데이터셋으로 다국어 번역에 활용됨.

## 분류

- **작업**: [[번역]] — ner · readme = `This dataset is a collection of Korean, Chinese, and Japanese OpenOrca translation datasets.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `440` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is a collection of Korean, Chinese, and Japanese OpenOrca translation datasets.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset was matched using id based on kyujinpy/OpenOrca-KO, which had the smallest number of rows.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response_en` 열 p90 1761자 ≈ 440 토큰 (viewer statistics, default/train)
