---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: ner_tag
    list:
    - name: begin
      dtype: int64
    - name: end
      dtype: int64
    - name: entity
      dtype: string
    - name: id
      dtype: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 43832237782
    num_examples: 90365874
  - name: validation
    num_bytes: 2994766999
    num_examples: 6065316
  download_size: 15686081097
  dataset_size: 46827004781
annotations_creators:
- no-annotation
language:
- ko
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: wisenut-nlp-team/aihub_corpus_expertise
size_categories:
- 100M<n<1B
source_datasets:
- original
tags: []
task_categories:
- other
- token-classification
task_ids: []
---
# Dataset Card for "corpus_professional_field"

[전문분야 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=110)