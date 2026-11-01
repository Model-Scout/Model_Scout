---
language:
- ko
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: question
    dtype: string
  - name: image
    dtype: image
  - name: answer
    dtype: string
  splits:
  - name: val
    num_bytes: 44929881.5
    num_examples: 1500
  download_size: 41874768
  dataset_size: 44929881.5
configs:
- config_name: default
  data_files:
  - split: val
    path: data/val-*
---

[NCSOFT/K-MMStar](https://huggingface.co/datasets/NCSOFT/K-MMStar) 를 쓰기 좋게 바꾸어놓았습니다.

아래 코드를 이용하였습니다.
```python
from datasets import load_dataset, DatasetDict, Dataset
from huggingface_hub import login; login(token="YOUR TOKEN")

dataset = load_dataset("NCSOFT/K-MMStar")

def preprocess_dataset(examples):
    processed_examples = {
        "index": examples["index"],
        "image": examples["image"],
        "answer": examples["answer"]
    }
    
    processed_examples["question"] = [
        q.replace("<image>", "").strip() for q in examples["question"]
    ]
    
    return processed_examples

processed_dataset = DatasetDict()
for split, dataset_split in dataset.items():
    processed_dataset[split] = dataset_split.map(
        preprocess_dataset,
        batched=True,
        remove_columns=["category", "l2_category", "meta_info"]
    )

processed_dataset.push_to_hub(
    "Ryoo72/K-MMStar",
    private=False 
)
```
