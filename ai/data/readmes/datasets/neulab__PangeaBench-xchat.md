---
dataset_info:
  features:
  - name: question_id
    dtype: int64
  - name: text
    dtype: string
  - name: category
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: chinese
    num_examples: 50
  - name: english
    num_examples: 50
  - name: hindi
    num_examples: 50
  - name: indonesian
    num_examples: 50
  - name: japanese
    num_examples: 50
  - name: kinyarwanda
    num_examples: 50
  - name: korean
    num_examples: 50
  - name: spanish
    num_examples: 50
  dataset_size: 400
configs:
- config_name: default
  data_files:
  - split: chinese
    path: data/chinese.parquet
  - split: english
    path: data/english.parquet
  - split: hindi
    path: data/hindi.parquet
  - split: indonesian
    path: data/indonesian.parquet
  - split: japanese
    path: data/japanese.parquet
  - split: kinyarwanda
    path: data/kinyarwanda.parquet
  - split: korean
    path: data/korean.parquet
  - split: spanish
    path: data/spanish.parquet
license: cc-by-4.0
task_categories:
- visual-question-answering
language:
- zh
- en
- hi
- id
- ja
- rw
- ko
- es
pretty_name: xchat
size_categories:
- n<1K
---