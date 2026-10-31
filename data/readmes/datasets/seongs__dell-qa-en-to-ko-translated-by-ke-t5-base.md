---
license: apache-2.0
language:
- ko
task_categories:
- question-answering
- translation
size_categories:
- 10K<n<100K
---

# Dell QA English to Korean Translation Dataset

## Dataset Description

This dataset, **[dell-qa-en-to-ko-translated-by-ke-t5-base](https://huggingface.co/seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko)**, is a Korean translation of the original English Dell QA dataset. 

## Source

The original dataset, [dell_qa](https://huggingface.co/datasets/c123ian/dell_qa), is designed for question-answering tasks and contains questions and answers related to Dell technologies. This translated version extends the utility to Korean language tasks.

## Dataset Structure

### Data Fields

- input
- instruction
- output

## Use Cases

This dataset can be used for training and evaluating models on Korean question-answering tasks. It can also serve as a benchmark for machine translation models and natural language understanding in Korean.

## How to Use

Here is an example of how to load this dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset('seongs/dell-qa-en-to-ko-translated-by-ke-t5-base')
