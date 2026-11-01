---
dataset_info:
  features:
  - name: query
    dtype: string
  - name: positive
    sequence: string
  - name: negative
    sequence: string
  splits:
  - name: test
    num_bytes: 151469200
    num_examples: 30453
  download_size: 78086558
  dataset_size: 151469200
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- ko
tags:
- finance
pretty_name: FinanceFiQA-Reranking-ko
size_categories:
- 10K<n<100K
---

## FinanceFiQA-Reranking-ko

- Utilizing the open dataset [BCCard/BCCard-Finance-Kor-QnA](https://huggingface.co/datasets/BCCard/BCCard-Finance-Kor-QnA), which consists of Korean financial text.
- Along with the original (query, positive) pair, the dataset provides **one** hard negative, retrieved through hard negative mining, and **nine** random negatives (total 10 negatives per query - positive pair).
- The hard negative mining method follows the [NV-Retriever: Improving text embedding models with effective hard-negative mining](https://arxiv.org/abs/2407.15831) paper.
- For detailed experiment methods and construction processes, refer to the [related article](https://huggingface.co/blog/Albertmade/nvretriever-into-financial-text).
