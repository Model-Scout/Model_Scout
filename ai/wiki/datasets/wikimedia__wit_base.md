---
type: "dataset"
id: "wikimedia/wit_base"
source: "huggingface"
url: "https://huggingface.co/datasets/wikimedia/wit_base"
downloads: 6853
summary: "WIT는 위키백과 이미지와 텍스트를 연결한 다국어 멀티모달 데이터셋으로 이미지 캡셔닝과 텍스트 검색에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 생성]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
# wikimedia/wit_base

> dataset · [Hugging Face](https://huggingface.co/datasets/wikimedia/wit_base)

WIT는 위키백과 이미지와 텍스트를 연결한 다국어 멀티모달 데이터셋으로 이미지 캡셔닝과 텍스트 검색에 활용됨.

## 분류

- **작업**: [[이미지 생성]] — ner · readme = `- `image-captioning`: This dataset can be used to train a model for image captioning where the goal is to predict a caption given the image.` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:visual_qa = `Each instance is an image, its representation in bytes, a pre-computed embedding` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:image_generation, task:retrieval, task:visual_qa = `the set of captions attached to the image in Wikipedia` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `the goal is to predict a caption given the image` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `105 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `403` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a large curated set of more than 37 million image-text associations extracted from Wikipedia articles in 108 languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The core training data is taken from the Wikipedia Image-Text (WIT) Dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `caption_attribution_description` 열 p90 1612자 ≈ 403 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `VedaLabs/wit_base`
