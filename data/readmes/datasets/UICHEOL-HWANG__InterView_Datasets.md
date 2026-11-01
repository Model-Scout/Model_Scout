---
language:
- ko
dataset_info:
  features:
  - name: experience
    dtype: string
  - name: ageRange
    dtype: string
  - name: occupation
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 88047841
    num_examples: 68078
  - name: valid
    num_bytes: 9067188
    num_examples: 8028
  download_size: 48282576
  dataset_size: 97115029
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
---


# AiHub Datasets 

origin : https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71592

import data
```python
from datasets import load_dataset

# train 데이터셋 로드
dataset = load_dataset("UICHEOL-HWANG/InterView_Datasets", split="train")
print(dataset)

# valid 데이터셋 로드
dataset = load_dataset("UICHEOL-HWANG/InterView_Datasets", split="valid")
print(dataset)
```

```bash
README.md: 100%
 428/428 [00:00<00:00, 25.0kB/s]
train-00000-of-00001.parquet: 100%
 4.53M/4.53M [00:00<00:00, 17.0MB/s]
Generating train split: 100%
 8028/8028 [00:00<00:00, 79755.45 examples/s]
Dataset({
    features: ['experience', 'ageRange', 'occupation', 'question', 'answer'],
    num_rows: 8028
})
```
