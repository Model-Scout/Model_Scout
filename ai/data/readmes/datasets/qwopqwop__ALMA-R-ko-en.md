---
language:
- ko
- en
license: cc-by-sa-4.0
size_categories:
- 1K<n<10K
task_categories:
- translation
dataset_info:
  config_name: ko-en
  features:
  - name: translation
    struct:
    - name: Delta
      dtype: int64
    - name: alma_en
      dtype: string
    - name: alma_en_kiwi
      dtype: float64
    - name: alma_en_kiwi_xcomet
      dtype: float64
    - name: alma_en_xcomet
      dtype: float64
    - name: alma_ko
      dtype: string
    - name: alma_ko_kiwi
      dtype: float64
    - name: alma_ko_kiwi_xcomet
      dtype: float64
    - name: alma_ko_xcomet
      dtype: float64
    - name: en
      dtype: string
    - name: gpt4_en
      dtype: string
    - name: gpt4_en_kiwi
      dtype: float64
    - name: gpt4_en_kiwi_xcomet
      dtype: float64
    - name: gpt4_en_xcomet
      dtype: float64
    - name: gpt4_ko
      dtype: string
    - name: gpt4_ko_kiwi
      dtype: float64
    - name: gpt4_ko_kiwi_xcomet
      dtype: float64
    - name: gpt4_ko_xcomet
      dtype: float64
    - name: ko
      dtype: string
    - name: language_pair
      dtype: string
    - name: ref_en_kiwi
      dtype: float64
    - name: ref_en_kiwi_xcomet
      dtype: float64
    - name: ref_en_xcomet
      dtype: float64
    - name: ref_ko_kiwi
      dtype: float64
    - name: ref_ko_kiwi_xcomet
      dtype: float64
    - name: ref_ko_xcomet
      dtype: float64
    - name: required_directions
      dtype: string
  splits:
  - name: train
    num_bytes: 2066513
    num_examples: 2009
  download_size: 1399967
  dataset_size: 2066513
configs:
- config_name: ko-en
  data_files:
  - split: train
    path: ko-en/train-*
---

# Dataset Card for "ALMA-R-ko-en-Preference"

ref) https://huggingface.co/datasets/haoranxu/ALMA-R-Preference

The triplet prference data, supporting 2 translation directions, is built upon the FLORES-200 development and test data. For each direction, we provide a source sentence along with three translations: one from GPT-4, another from EEVE-ALMA-LoRA, and a reference translation. For instance, in the English-German pair, our data structure is as follows:

### Sentences:
- ko: Original Korean sentence
- en: Original English sentence
- alma_ko: Korean sentence translated from English by ALMA
- gpt4_ko: Korean sentence translated from English by GPT-4
- alma_en: English sentence translated from Korean by ALMA
- gpt4_en: English sentence translated from Korean by GPT-4

### Scores
- alma_en_${Score}: ${Score} of English sentence translated by ALMA
- gpt4_en_${Score}: ${Score} of English sentence translated by GPT4
- ref_en_${Score}: ${Score} of reference English sentence
- alma_ko_${Score}: ${Score}  of Korean sentence translated by ALMA
- gpt4_ko_${Sscore}: ${Score} of Korean sentence translated by GPT4
- ref_ko_${Score}: ${Score} of reference Korean sentence

${Score} can be numbers from kiwi ([wmt23-cometkiwi-da-xxl](https://huggingface.co/Unbabel/wmt23-cometkiwi-da-xxl)), xcomet ([XCOMET-XXL](https://huggingface.co/Unbabel/XCOMET-XXL)), 
or kiwi_xcomet (average score of kiwi and xcomet).

### Others
- Delta: A value of 0 indicates non-human annotated data or tied evaluations. A postive number suggests that alma_ko is better than gpt4_ko, vice versa
- required_directions: An empty field implies that this data point can be used for both translation directions. If the string 'en-ko' is specified, it indicates that this data point is exclusively for English to Korean translation