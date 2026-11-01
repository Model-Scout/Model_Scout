---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 847547561
    num_examples: 111912
  download_size: 383263271
  dataset_size: 847547561
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- text-generation
- text2text-generation
language:
- en
- vi
- zh
- es
- pt
- ja
- ko
size_categories:
- 100K<n<1M
---


## Description

The dataset is from unknown, formatted as dialogues for speed and ease of use. Many thanks to author for releasing it.
Importantly, this format is easy to use via the default chat template of `transformers`, meaning you can use [huggingface/alignment-handbook](https://github.com/huggingface/alignment-handbook) immediately, [unsloth](https://github.com/unslothai/unsloth).

## Structure

*View online through viewer.*

## Note

We advise you to reconsider before use, thank you. If you find it useful, please like and follow this account.

## Reference

The **Ghost X** was developed with the goal of researching and developing artificial intelligence useful to humans.

- HuggingFace: [ghost-x](https://huggingface.co/ghost-x)
- Github: [ghost-x-ai](https://github.com/ghost-x-ai)
- X / Twitter: [ghostx_ai](https://twitter.com/ghostx_ai)
- Website: [ghost-x.org](https://ghost-x.org/)

### ~