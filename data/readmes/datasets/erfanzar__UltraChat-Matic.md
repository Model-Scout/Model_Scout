---
dataset_info:
  features:
  - name: system
    dtype: string
  - name: user
    sequence: string
  - name: assistant
    sequence: string
  - name: dialogs
    sequence: string
  - name: conv_depth
    dtype: int64
  splits:
  - name: train
    num_bytes: 447216231
    num_examples: 109765
  download_size: 242424003
  dataset_size: 447216231
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

# ChatMatic
## with Over 80,000 multi-turn examples.

UltraChat-Matic Dataset is built with mix of 4 other dataset and which carefully chosing best one from each one of them with using `GPT-4`
and contains 
System messages Dialogs and conv_depth more than 5 with higher sequence lengths
Used datasets are:

1. "oasst2"
2. "ise-uiuc/Magicoder-Evol-Instruct-110K"
3. "vicgalle/alpaca-gpt4"
4. "LDJnr/Capybara"

### From Capybara 

* Most tokens contained in this dataset are newly synthesized and did not exist prior online.

* This leverages the Amplify-Instruct method(paper coming soon) to grow thousands of high-quality single-turn seeds into advanced and in-depth multi-turn conversations.

* Average context length per conversation is over 1,000 tokens and 3 turns or more per example (most instruction/chat datasets on HF for fine-tuning are only 1 turn)

* Each conversation is optimized to amplify the natural raw knowledge capabilities of the model, as well as delving deep into obscure and advanced topics.

* Aggresively filtered to remove any and all possible examples of overt moralizing/alignment, and common undesirable behaviours such as "as an AI language model" and "September 2021" and "I don't have personal beliefs"

* ### More than 60000 Datas generated or selected by GPT4