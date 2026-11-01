---
type: "dataset"
id: "GGUFGuy/wikipedia-viewer"
source: "huggingface"
url: "https://huggingface.co/datasets/GGUFGuy/wikipedia-viewer"
downloads: 884
summary: "위키피디아 덤프에서 언어별로 정제된 문서 전체를 담은 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# GGUFGuy/wikipedia-viewer

> dataset · [Hugging Face](https://huggingface.co/datasets/GGUFGuy/wikipedia-viewer)

위키피디아 덤프에서 언어별로 정제된 문서 전체를 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `Each example contains the content of one full Wikipedia article with cleaning` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each example contains the content of one full Wikipedia article with cleaning` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `294 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11557` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia dataset containing cleaned articles of all languages.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The datasets are built from the Wikipedia dump` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 46229자 ≈ 11557 토큰 (viewer statistics, default/train)
