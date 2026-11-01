---
dataset_info:
- config_name: Cmn-Corpus
  features:
  - name: id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 141848762
    num_examples: 172569
  - name: validation
    num_bytes: 17546970
    num_examples: 21574
  download_size: 85376957
  dataset_size: 159395732
- config_name: Eng-Corpus
  features:
  - name: id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 195479223
    num_examples: 164836
  - name: validation
    num_bytes: 24576069
    num_examples: 20596
  download_size: 101839377
  dataset_size: 220055292
- config_name: Ind-Corpus
  features:
  - name: id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 195080784
    num_examples: 153792
  - name: validation
    num_bytes: 24403763
    num_examples: 19226
  download_size: 97512763
  dataset_size: 219484547
- config_name: Jpn-Corpus
  features:
  - name: id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 184198059
    num_examples: 165365
  - name: validation
    num_bytes: 23049417
    num_examples: 20672
  download_size: 98527246
  dataset_size: 207247476
- config_name: Kor-Corpus
  features:
  - name: id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 875063849
    num_examples: 821752
  - name: validation
    num_bytes: 109447407
    num_examples: 102719
  download_size: 484110979
  dataset_size: 984511256
- config_name: Original
  features:
  - name: meta
    struct:
    - name: doc_no
      dtype: string
    - name: domain
      dtype: string
    - name: category
      dtype: string
    - name: license
      dtype: string
    - name: source_language
      dtype: string
    - name: target_language
      dtype: string
  - name: doc_info
    struct:
    - name: source
      dtype: string
    - name: journal_name
      dtype: string
    - name: vol_info
      dtype: string
    - name: doi
      dtype: string
    - name: title
      dtype: string
    - name: date
      dtype: int64
  - name: sents
    list:
    - name: page
      dtype: int64
    - name: sn
      dtype: string
    - name: source_original
      dtype: string
    - name: source_cleaned
      dtype: string
    - name: mt
      dtype: string
    - name: mtpe
      dtype: string
  splits:
  - name: train
    num_bytes: 75737179
    num_examples: 29852
  - name: validation
    num_bytes: 9513544
    num_examples: 3720
  download_size: 38840004
  dataset_size: 85250723
- config_name: Translation
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - Kor
        - Eng
        - Jpn
        - Vie
        - Ind
        - Cmn
  - name: metadata
    struct:
    - name: doc_info
      struct:
      - name: source
        dtype: string
      - name: journal_name
        dtype: string
      - name: vol_info
        dtype: string
      - name: doi
        dtype: string
      - name: title
        dtype: string
      - name: date
        dtype: int32
    - name: doc_no
      dtype: string
    - name: domain
      dtype: string
    - name: category
      dtype: string
    - name: license
      dtype: string
    - name: source_language
      dtype: string
    - name: target_language
      dtype: string
  splits:
  - name: train
    num_bytes: 1256186731
    num_examples: 2035772
  - name: validation
    num_bytes: 157188919
    num_examples: 254837
  download_size: 537794143
  dataset_size: 1413375650
- config_name: Vie-Corpus
  features:
  - name: id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 236190985
    num_examples: 165190
  - name: validation
    num_bytes: 29617120
    num_examples: 20651
  download_size: 110599573
  dataset_size: 265808105
configs:
- config_name: Cmn-Corpus
  data_files:
  - split: train
    path: Cmn-Corpus/train-*
  - split: validation
    path: Cmn-Corpus/validation-*
- config_name: Eng-Corpus
  data_files:
  - split: train
    path: Eng-Corpus/train-*
  - split: validation
    path: Eng-Corpus/validation-*
- config_name: Ind-Corpus
  data_files:
  - split: train
    path: Ind-Corpus/train-*
  - split: validation
    path: Ind-Corpus/validation-*
- config_name: Jpn-Corpus
  data_files:
  - split: train
    path: Jpn-Corpus/train-*
  - split: validation
    path: Jpn-Corpus/validation-*
- config_name: Kor-Corpus
  data_files:
  - split: train
    path: Kor-Corpus/train-*
  - split: validation
    path: Kor-Corpus/validation-*
- config_name: Original
  data_files:
  - split: train
    path: Original/train-*
  - split: validation
    path: Original/validation-*
- config_name: Translation
  data_files:
  - split: train
    path: Translation/train-*
  - split: validation
    path: Translation/validation-*
- config_name: Vie-Corpus
  data_files:
  - split: train
    path: Vie-Corpus/train-*
  - split: validation
    path: Vie-Corpus/validation-*
task_categories:
- translation
language:
- ko
- en
- vi
- id
---