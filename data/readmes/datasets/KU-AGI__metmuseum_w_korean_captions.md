---
license: cc0-1.0
task_categories:
- image-to-text
- text-to-image
language:
- ko
- en
tags:
- art
- met-museum
- image-captioning
size_categories:
- n<1K
dataset_info:
  features:
  - name: objectID
    dtype: int64
  - name: title
    dtype: string
  - name: artist
    dtype: string
  - name: objectDate
    dtype: string
  - name: medium
    dtype: string
  - name: culture
    dtype: string
  - name: classification
    dtype: string
  - name: department
    dtype: string
  - name: met_url
    dtype: string
  - name: image_url
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: wikipedia_title_en
    dtype: string
  - name: wikipedia_url_en
    dtype: string
  - name: wikipedia_url_ko
    dtype: string
  - name: description_en
    dtype: string
  - name: description_ko
    dtype: string
  - name: description_ko_source
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 17984989
    num_examples: 100
  dataset_size: 17984989
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Met Museum Artworks with Korean Captions

Metropolitan Museum of Art 소장품 100점에 대한 메타데이터와 한국어/영어 캡션 데이터셋입니다.
이미지는 긴 변 1024px로 리사이즈되어 parquet에 임베드되어 있습니다.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("KU-AGI/metmuseum_w_korean_captions", split="train")
ex = ds[0]
ex["image"]            # PIL.Image
ex["title"]            # 작품명
ex["description_ko"]   # 한국어 설명
```

## Fields

- `image`: 작품 이미지 (긴 변 1024px, parquet 임베드)
- `objectID`: Met 오브젝트 ID
- `title`, `artist`, `objectDate`, `medium`, `culture`, `classification`, `department`: 작품 메타데이터
- `met_url`, `image_url`: Met 컬렉션 / 원본 이미지 URL
- `wikidata_qid`, `wikipedia_title_en`, `wikipedia_url_en`, `wikipedia_url_ko`: 위키 연결 정보
- `description_en`, `description_ko`: 영어/한국어 설명
- `description_ko_source`: 한국어 설명 출처 (`ko_wikipedia` 또는 `nllb_mt`)
