---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: source
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 239650960.7474458
    num_examples: 100000
  download_size: 116531415
  dataset_size: 239650960.7474458
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# FineTome-100k

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/75I3ffI4XnRlheOQ7kNJ3.jpeg)

The FineTome dataset is a subset of [arcee-ai/The-Tome](https://huggingface.co/datasets/arcee-ai/The-Tome) (without arcee-ai/qwen2-72b-magpie-en), re-filtered using [HuggingFaceFW/fineweb-edu-classifier](https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier).

It was made for my article ["Fine-tune Llama 3.1 Ultra-Efficiently with Unsloth"](https://huggingface.co/blog/mlabonne/sft-llama3).