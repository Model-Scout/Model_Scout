---
configs:
- config_name: messages
  default: true
  data_files:
  - path:
    - messages.jsonl.zst
    split: train
- config_name: taxonomy
  data_files:
  - path:
    - taxonomy.jsonl.zst
    split: train
language:
- zh
- en
- ja
- ko
- de
- fr
- ru
- pt
- es
- it
task_categories:
- text-generation
- text-to-audio
---