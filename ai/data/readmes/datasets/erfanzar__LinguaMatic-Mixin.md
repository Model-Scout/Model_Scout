---
dataset_info:
  features:
    - name: prompt
      dtype: string
  splits:
    - name: train
      num_bytes: 168057889
      num_examples: 69765
  download_size: 88116993
  dataset_size: 168057889
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
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
tags:
- code
- biology
- medical
size_categories:
- 1M<n<10M
task_categories:
- text-generation
- text-classification
- conversational
---

# Dataset Card for "UltraChat-Mixin"

# UltraChat-Mixin Dataset

## Overview
llama 2 prompted style frin 
### ChatMatic
ChatMatic Dataset is built with mix of 4 other dataset and which carefully chosing best one from each one of them with using GPT-4 and contains System messages Dialogs and conv_depth more than 5 with higher sequence lengths Used datasets are:

"oasst2"
"ise-uiuc/Magicoder-Evol-Instruct-110K"
"vicgalle/alpaca-gpt4"
"LDJnr/Capybara"
## Dataset Configuration
The dataset is configured as follows:

```yaml
dataset_info:
  features:
    - name: prompt
      dtype: string
  splits:
    - name: train
      num_bytes: 168057889
      num_examples: 69765
  download_size: 88116993
  dataset_size: 168057889
```

## Features
The UltraChat-Mixin dataset consists of the following features:

- **prompt**: A sequence of strings representing the conversation dialog Llama2 Style prompts.

## Splits
The dataset contains a single split:

- **train**: This split is used for training conversational AI models. It consists of 70_000 examples and has a size of approximately 168,057,889 bytes.

## Download Size
The download size of the UltraChat-Mixin dataset is approximately 88,116,993 bytes.

## Dataset Size
The total size of the UltraChat-Mixin dataset is approximately 168,057,889 bytes.

Please note that the dataset configuration and statistics provided above are based on the information provided by Erfan zare chavoshi.
