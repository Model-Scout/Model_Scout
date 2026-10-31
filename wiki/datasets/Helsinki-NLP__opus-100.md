---
type: "dataset"
id: "Helsinki-NLP/opus-100"
source: "huggingface"
url: "https://huggingface.co/datasets/Helsinki-NLP/opus-100"
downloads: 23975
summary: "OPUS-100은 영어 중심의 100개 언어 다국어 병렬 말뭉치로 번역에 사용됨."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Helsinki-NLP/opus-100

> dataset · [Hugging Face](https://huggingface.co/datasets/Helsinki-NLP/opus-100)

OPUS-100은 영어 중심의 100개 언어 다국어 병렬 말뭉치로 번역에 사용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `English-centric multilingual corpus covering 100 languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Translation.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `100 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[haoranxu__X-ALMA-13B-Pretrain|haoranxu/X-ALMA-13B-Pretrain]]
