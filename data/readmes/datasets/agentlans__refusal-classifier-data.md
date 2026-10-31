---
configs:
- config_name: english_only
  data_files:
  - path:
    - en_dataset/train.jsonl
    split: train
  - path:
    - en_dataset/test.jsonl
    split: test
  default: true
- config_name: multilingual
  data_files:
  - path:
    - multilingual_dataset/train.jsonl
    split: train
  - path:
    - multilingual_dataset/test.jsonl
    split: test
language:
  - en
  - zh
  - fr
  - pt
  - es
  - ja
  - tr
  - ru
  - ar
  - ko
  - th
  - it
  - de
  - vi
  - ms
  - id
  - fil
  - hi
  - pl
  - cs
  - nl
  - km
  - my
  - fa
  - gu
  - ur
  - te
  - mr
  - he
  - bn
  - ta
  - uk
  - bo
  - kk
  - mn
  - ug
  - yue
license: cc-by-4.0
---
# Refusal Classifier Training Data

- The `english_only` subset is taken from the `downsampled` configuration of [agentlans/en-chat-refusal](https://huggingface.co/datasets/agentlans/en-chat-refusal).
- The `multilingual` subset is created by mixing [agentlans/multilingual-chat-refusal](https://huggingface.co/datasets/agentlans/multilingual-chat-refusal) with the `english_only` subset in a 1:1 ratio.

All conversations have been formatted using role tokens and ellipses `<|...|>` for long texts.

The resulting files are shuffled and split 80% training, 20% testing.