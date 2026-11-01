---
language:
- ko
- en
size_categories:
- 10B<n<100B
task_categories:
- visual-question-answering
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: caption
    dtype: string
  - name: caption_ls
    list: string
  - name: category
    dtype: string
  - name: objects
    list:
    - name: id
      dtype: int32
    - name: text
      dtype: string
    - name: bbox
      list: int32
  - name: question_answer
    list:
    - name: id
      dtype: string
    - name: question
      dtype: string
    - name: answer
      dtype: string
    - name: visual_concept
      list: string
    - name: question_en
      dtype: string
    - name: answer_en
      dtype: string
    - name: question_type
      list: string
    - name: ans_source
      dtype: string
    - name: kb_source
      list: string
    - name: fact
      list: string
  - name: metadata
    struct:
    - name: KOREAN_IMAGE
      dtype: string
    - name: DIRECT_IMAGE
      dtype: string
    - name: ACTION
      dtype: string
    - name: IMAGE_ACQUISITION_DATE
      dtype: string
    - name: IMAGE_URL
      dtype: string
    - name: LICENSE
      dtype: string
    - name: MAINOBJECT
      dtype: string
    - name: MAINOBJECT_URL
      dtype: string
    - name: SCENE
      dtype: string
    - name: SUBOBJECT_1
      dtype: string
    - name: SUBOBJECT_2
      dtype: string
    - name: WIDTH
      dtype: string
    - name: HEIGHT
      dtype: string
    - name: WIKI_FILE
      dtype: string
  splits:
  - name: train
    num_bytes: 11169890399.625
    num_examples: 47203
  - name: validation
    num_bytes: 1548226868.125
    num_examples: 6423
  download_size: 12644146792
  dataset_size: 12718117267.75
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
tags:
- Caption
- Image
---