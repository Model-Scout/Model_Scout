---
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- en
- ko
tags:
- biology
pretty_name: Medical domain QA dataset for training a medical chatbot.
---

# MQuAD
The Medical Question and Answering dataset(MQuAD) has been refined, including the following datasets. You can download it through the Hugging Face dataset. Use the DATASETS method as follows.

## Quick Guide
```python
from datasets import load_dataset
dataset = load_dataset("danielpark/MQuAD-v1")
```

Medical Q/A datasets gathered from the following websites.
- eHealth Forum
- iCliniq
- Question Doctors
- WebMD
Data was gathered at the 5th of May 2017.


The MQuAD provides embedded question and answer arrays in string format, so it is recommended to convert the string-formatted arrays into float format as follows. This measure has been applied to save resources and time used for embedding.
```python
from datasets import load_dataset
from utilfunction import col_convert
import pandas as pd

qa = load_dataset("danielpark/MQuAD-v1", "csv")
df_qa = pd.DataFrame(qa['train'])
df_qa = col_convert(df_qa, ['Q_FFNN_embeds', 'A_FFNN_embeds'])
```
