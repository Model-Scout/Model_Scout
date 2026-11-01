---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 53934652
    num_examples: 100000
  download_size: 21449632
  dataset_size: 53934652
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---

https://huggingface.co/datasets/lemon-mint/Korean-FineTome-100k

https://huggingface.co/datasets/kkksklsn/Korean-FineTome-100k-tagging

```json
{
  "0":"Coding & Debugging",
  "1":"Science",
  "2":"Planning",
  "3":"Information seeking",
  "4":"Reasoning",
  "5":"Math",
  "6":"Medical Knowledge",
  "7":"Data analysis",
  "8":"Editing",
  "9":"Brainstorming",
  "10":"Creative writing",
  "11":"Advice seeking",
  "12":"Role playing",
  "13":"Others",
  "14":"Translating"
}
```

```json
{
  "Coding & Debugging":0,
  "Science":1,
  "Planning":2,
  "Information seeking":3,
  "Reasoning":4,
  "Math":5,
  "Medical Knowledge":6,
  "Data analysis":7,
  "Editing":8,
  "Brainstorming":9,
  "Creative writing":10,
  "Advice seeking":11,
  "Role playing":12,
  "Others":13,
  "Translating":14
}
```