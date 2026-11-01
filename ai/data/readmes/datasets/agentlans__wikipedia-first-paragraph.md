---
configs:
- config_name: ar
  data_files:
  - path:
    - ar.jsonl.zst
    split: train
- config_name: de
  data_files:
  - path:
    - de.jsonl.zst
    split: train
- config_name: en
  data_files:
  - path:
    - en.jsonl.zst
    split: train
  default: true
- config_name: es
  data_files:
  - path:
    - es.jsonl.zst
    split: train
- config_name: fr
  data_files:
  - path:
    - fr.jsonl.zst
    split: train
- config_name: it
  data_files:
  - path:
    - it.jsonl.zst
    split: train
- config_name: ja
  data_files:
  - path:
    - ja.jsonl.zst
    split: train
- config_name: ko
  data_files:
  - path:
    - ko.jsonl.zst
    split: train
- config_name: pt
  data_files:
  - path:
    - pt.jsonl.zst
    split: train
- config_name: ru
  data_files:
  - path:
    - ru.jsonl.zst
    split: train
- config_name: zh
  data_files:
  - path:
    - zh.jsonl.zst
    split: train
task_categories:
- text-classification
- text-generation
- text2text-generation
language:
- ar
- de
- en
- es
- fr
- it
- ja
- ko
- pt
- ru
- zh
tags:
- wikipedia
---