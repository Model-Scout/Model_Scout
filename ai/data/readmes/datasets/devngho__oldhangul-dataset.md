---
language:
- ko
license: cc-by-sa-4.0
size_categories:
- 1K<n<10K
dataset_info:
- config_name: wikisource
  features:
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: license
    struct:
    - name: accessed_at
      dtype: string
    - name: original_source
      struct:
      - name: author
        dtype: string
      - name: source
        dtype: string
    - name: wiki_source_link
      dtype: string
  - name: text
    dtype: string
  - name: meta
    struct:
    - name: page
      dtype: int64
    - name: year
      dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 18590137
    num_examples: 7077
  download_size: 6189434
  dataset_size: 18590137
- config_name: wikisource_v2
  features:
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: license
    struct:
    - name: accessed_at
      dtype: string
    - name: original_source
      struct:
      - name: author
        dtype: string
      - name: source
        dtype: string
    - name: wiki_source_link
      dtype: string
  - name: text
    dtype: string
  - name: meta
    struct:
    - name: page
      dtype: int64
    - name: year
      dtype: float64
  splits:
  - name: train
    num_bytes: 36345475
    num_examples: 7615
  download_size: 12957836
  dataset_size: 36345475
configs:
- config_name: wikisource
  data_files:
  - split: train
    path: wikisource/train-*
- config_name: wikisource_v2
  data_files:
  - split: train
    path: wikisource_v2/train-*
  default: true
tags:
- oldhangul
---
# 옛한글 데이터셋

original(HERE) | [cleaned](/datasets/devngho/oldhangul-dataset-cleaned)

위키문헌을 기반으로 구축한 옛한글 데이터셋

## 불러오기

```py
from datasets import load_dataset

ds = load_dataset("devngho/oldhangul-dataset", "wikisource_v2")
```

## 라이선스
### 데이터셋
[CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ko)

### 자료
위키문헌 기여자, [위키문헌](https://ko.wikisource.org/wiki/%EC%9C%84%ED%82%A4%EB%AC%B8%ED%97%8C:%EB%8C%80%EB%AC%B8) / [CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ko) 

`cleaned` 버전은 한자 비율이 20% 이상인 것을 걸러내고 `<br>`, 여러 줄의 `\n` 등을 정리했습니다.

데이터의 `license` 필드에서 위키문헌 링크와 원본 자료 위치를 확인할 수 있습니다.