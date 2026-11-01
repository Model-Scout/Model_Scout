---
dataset_info:
  features:
  - name: classification
    dtype: string
  - name: scientific_name
    dtype: string
  - name: korean_common_name
    dtype: string
  - name: english_species_name
    dtype: string
  splits:
  - name: train
    num_bytes: 4470094
    num_examples: 60010
  download_size: 1987887
  dataset_size: 4470094
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
language:
- ko
---

- 2023년 국가생물종목록(학명, 일반명(한글), 종명(영어))
- https://www.bris.go.kr/portal/knowledge/dictionaryPage.do
- 또는 https://species.nibr.go.kr/nibrStats/statDownPage.do?artNo=1839