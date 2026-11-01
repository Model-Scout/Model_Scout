---
license: apache-2.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: question
    dtype: string
  - name: sentence
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': entailment
          '1': not_entailment
  - name: translated_question_lang
    dtype: string
  - name: translated_sentence_lang
    dtype: string
  - name: translated_question
    dtype: string
  - name: translated_sentence
    dtype: string
  splits:
  - name: train
    num_bytes: 54987341
    num_examples: 103059
  download_size: 39711768
  dataset_size: 54987341
task_categories:
- text-classification
language:
- en
- de
- es
- ar
- zh
- hi
- pt
- ru
- ja
- fr
- ur
- tr
- ko
- pl
- it
- sv
pretty_name: Multilingual qnli (from GLUE)
size_categories:
- 10K<n<100K
---