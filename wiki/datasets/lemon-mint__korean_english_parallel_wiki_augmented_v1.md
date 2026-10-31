---
type: "dataset"
id: "lemon-mint/korean_english_parallel_wiki_augmented_v1"
source: "huggingface"
url: "https://huggingface.co/datasets/lemon-mint/korean_english_parallel_wiki_augmented_v1"
downloads: 111
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lemon-mint/korean_english_parallel_wiki_augmented_v1

> dataset · [Hugging Face](https://huggingface.co/datasets/lemon-mint/korean_english_parallel_wiki_augmented_v1)

## 분류

- **작업**: [[임베딩]] — tag_match · tags = `embedding` · 신뢰도 medium
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
