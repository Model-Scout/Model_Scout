---
dataset_info:
  features:
  - name: source_text
    dtype: string
  - name: rejected
    dtype: string
  - name: chosen
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: test
    num_bytes: 38868
    num_examples: 57
  download_size: 29880
  dataset_size: 38868
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- en
- ko
---

- Mistranslation dataset for evaluating the performance of reward models or filtering methods used in assessing the quality of Korean to English translations.
- Unnatural grammar usage, misinterpretation due to incorrect phrase/clause segmentation, awkward terminology, etc.
- Yes, 57 records is too small to evaluate something.
