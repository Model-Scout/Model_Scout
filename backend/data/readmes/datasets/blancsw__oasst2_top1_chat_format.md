---
language:
- en
- es
- ru
- de
- pl
- th
- vi
- sv
- bn
- da
- he
- it
- fa
- sk
- id
- nb
- el
- nl
- hu
- eu
- zh
- eo
- ja
- ca
- cs
- bg
- fi
- pt
- tr
- ro
- ar
- uk
- gl
- fr
- ko
license: apache-2.0
size_categories:
- 100K<n<1M
task_categories:
- conversational
pretty_name: OpenAssistant Conversations Release 2 in huggingface chat format
tags:
- human-feedback
- sft
dataset_info:
  features:
  - name: conversation
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: langs
    dtype: string
  splits:
  - name: train
    num_bytes: 18366000
    num_examples: 10746
  download_size: 10484376
  dataset_size: 18366000
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# OpenAssistant TOP-1 Conversation Threads in huggingface chat format

Export of [oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2) only top 1 threads in [huggingface chat format](https://huggingface.co/docs/transformers/chat_templating)

# Script

The convert script can be find [here](https://github.com/blancsw/deep_4_all/tree/main/datasets/oasst)