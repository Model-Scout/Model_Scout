---
configs:
- config_name: default
  data_files:
  - split: subset
    path: subset.csv
  - split: fullset1
    path: fullset1.csv
  - split: fullset2
    path: fullset2.csv
license:
- mit
task_categories:
- text-generation
size_categories:
- 1M<n<10M
language:
- en
- zh
- fr
- ko
- de
- es
- ja
---

# Eagle 🦅: Ethical Dataset Given from Real Interactions

![](eagle.png)

## Introduction
This repository contains the Eagle dataset, which is an ethical dataset of real interactions between humans and ChatGPT. This dataset is created to evaluate social bias, opinion bias, toxic language, and morality in Large Language Models (LLMs).

If you use the Eagle dataset in your research, please cite the following:

```sql
@inproceedings{Eagle:arxiv:2024,
    title={Eagle: Ethical Dataset Given from Real Interactions},
    author={Kaneko, Masahiro and Bollegala, Danushka and Baldwin, Timothy},
    booktitle={arXiv},
    year={2024}
}
```
The Eagle dataset has `fullset1.csv`, `fullset2.csv`, and `subset.csv` files.
Due to data size limitations on uploads, we have split one dataset into two files, named `fullset1.csv` and `fullset2.csv`.
They contain multilingual neutral, social bias, opinion bias, toxic language, and molarity instances.
`subset.csv` contains English social bias, opinion bias, toxic language, and molarity instances.
The subset dataset has 2.3K instances, and the fullset dataset has 1.4M instances.
These CSV files have the following fields:
- `original_id`: Original dataset ID
- `conversation_num`: Number within the same conversation
- `utterance_num`: Order of ChatGPT's response within the conversation
- `language`: Identified language of utterance
- `ethical_labels`: Classified ethical labels (social bias, opinion bias, toxic language, and molarity)
- `context`: {"role": "gpt or human", "content": "context utterances"}
- `output`: {"role": "gpt": "content": "chatgpt output"}


## How to Evaluate LLMs using the Eagle Dataset
We use a likelihood-based evaluation based on this [code](https://github.com/kanekomasahiro/transformers_llm).

## License
You can find the full text of the license in the LICENSE file.