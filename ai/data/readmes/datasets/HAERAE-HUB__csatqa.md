---
dataset_info:
  features:
  - name: test_name
    dtype: string
  - name: question_number
    dtype: int64
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: gold
    dtype: int64
  - name: option#1
    dtype: string
  - name: option#2
    dtype: string
  - name: option#3
    dtype: string
  - name: option#4
    dtype: string
  - name: option#5
    dtype: string
  - name: Category
    dtype: string
  - name: Human_Peformance
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 4220807
    num_examples: 936
  download_size: 1076028
  dataset_size: 4220807
task_categories:
- multiple-choice
language:
- ko
---
# Dataset Card for "CSAT-QA"

## Dataset Summary
The field of Korean Language Processing is experiencing a surge in interest, 
illustrated by the introduction of open-source models such as Polyglot-Ko and proprietary models like HyperClova. 
Yet, as the development of larger and superior language models accelerates, evaluation methods aren't keeping pace. 
Recognizing this gap, we at HAE-RAE are dedicated to creating tailored benchmarks for the rigorous evaluation of these models.

CSAT-QA is a comprehensive collection of 936 multiple choice question answering (MCQA) questions, 
manually collected the College Scholastic Ability Test (CSAT), a rigorous Korean University entrance exam. 
The CSAT-QA is divided into two subsets: a complete version encompassing all 936 questions,
and a smaller, specialized version used for targeted evaluations.

The smaller subset further diversifies into six distinct categories: 
Writing (WR), Grammar (GR), Reading Comprehension: Science (RCS), Reading Comprehension: Social Science (RCSS), 
Reading Comprehension: Humanities (RCH), and Literature (LI). Moreover, the smaller subset includes the recorded accuracy of South Korean students, 
providing a valuable real-world performance benchmark. 

For a detailed explanation of how the CSAT-QA was created 
please check out the [accompanying blog post](https://github.com/guijinSON/hae-rae/blob/main/blog/CSAT-QA.md), 
and for evaluation check out [LM-Eval-Harness](https://github.com/EleutherAI/lm-evaluation-harness) on github.


## Evaluation Results


|     **Models**    |   **GR**  |   **LI**  |  **RCH**  |  **RCS**  |  **RCSS** |   **WR**  | **Average** |
|:-----------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:-----------:|
| polyglot-ko-12.8B |      32.0 |     29.73 |      17.14|     10.81 |     21.43 |      18.18 |       21.55|
|  gpt-3.5-wo-token |      16.0 |     32.43 |     42.86 |     18.92 |     35.71 |      0.00 |       24.32 |
|   gpt-3.5-w-token |      16.0 |     35.14 |     42.86 |     18.92 |     35.71 |      9.09 |       26.29 |
|    gpt-4-wo-token |      40.0 |     54.05 | **68.57** | **59.46** | **69.05** | 36.36 |   **54.58** |
|     gpt-4-w-token |      36.0 | **56.76** | **68.57** | **59.46** | **69.05** | 36.36 |       54.37 |
| Human Performance | **45.41** |     54.38 |      48.7 |     39.93 |     44.54 |      **54.0** |       47.83 |



## How to Use

The CSAT-QA includes two subsets. The full version with 936 questions can be downloaded using the following code:

```
from datasets import load_dataset
dataset = load_dataset("EleutherAI/CSAT-QA", "full")
```

A more condensed version, which includes human accuracy data, can be downloaded using the following code:
```
from datasets import load_dataset
import pandas as pd

dataset = load_dataset("EleutherAI/CSAT-QA", "GR") # Choose from either WR, GR, LI, RCH, RCS, RCSS, 

```

## Evaluate using LM-Eval-Harness
To evaluate your model simply by using the LM-Eval-Harness by EleutherAI follow the steps below.

1. To install lm-eval from the github repository main branch, run:
```
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
```

2. To install additional multilingual tokenization and text segmentation packages, you must install the package with the multilingual extra:
```
pip install -e ".[multilingual]"
```

3. Run the evaluation by:
```
python main.py \
    --model hf-causal \
    --model_args pretrained=EleutherAI/polyglot-ko-1.3b \
    --tasks csatqa_wr,csatqa_gr,csatqa_rcs,csatqa_rcss,csatqa_rch,csatqa_li \
    --device cuda:0
```

## License

The copyright of this material belongs to the Korea Institute for Curriculum and Evaluation(한국교육과정평가원) and may be used for research purposes only.


[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)