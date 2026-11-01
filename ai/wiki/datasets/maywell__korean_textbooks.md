---
type: "dataset"
id: "maywell/korean_textbooks"
source: "huggingface"
url: "https://huggingface.co/datasets/maywell/korean_textbooks"
downloads: 1235
summary: "Gemini Pro로 생성한 대규모 한국어 인공 합성 데이터셋으로 다양한 태스크에 맞춰 가공하여 사용 가능하다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# maywell/korean_textbooks

> dataset · [Hugging Face](https://huggingface.co/datasets/maywell/korean_textbooks)

Gemini Pro로 생성한 대규모 한국어 인공 합성 데이터셋으로 다양한 태스크에 맞춰 가공하여 사용 가능하다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is a large-scale Korean artificial data set created using Gemini Pro.` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `본 데이터셋은 바로 사용하기보다는 하고자하는 task에 맞추어 가공 후 사용을 권장드립니다. ex) 로컬 모델을 사용하여 QA 셋으로 변환` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `This dataset is a large-scale Korean artificial data set` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `본 데이터셋은 바로 사용하기보다는 하고자하는 task에 맞추어 가공 후 사용을 권장드립니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1698` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Massive Korean synthetic dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Further modification required before use this dataset for training.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2546자 ≈ 1698 토큰 (viewer statistics, ko_wikidata/train)

## 이 데이터로 학습한 모델

- [[blueapple8259__TinyKo-v5-a|blueapple8259/TinyKo-v5-a]]
- [[blueapple8259__tzem|blueapple8259/tzem]]
- [[daekeun-ml__phi-2-ko-v0.1|daekeun-ml/phi-2-ko-v0.1]]
