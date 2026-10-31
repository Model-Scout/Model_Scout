---
license: cc-by-nc-sa-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: id
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: train
    num_bytes: 72696825
    num_examples: 45155
  download_size: 38159019
  dataset_size: 72696825
---

# ko-kiwi dataset🥝

## Merge datasets below
- Thank you for [HumanF-MarkrAI/WIKI_QA_Near_dedup](https://huggingface.co/datasets/HumanF-MarkrAI/WIKI_QA_Near_dedup).  (Sampling about 10K)
- Use my dataset [kyujinpy/KOR-OpenOrca-Platypus](https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus).  
