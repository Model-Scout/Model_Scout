---
license: mit
dataset_info:
  features:
  - name: url
    dtype: string
  - name: tag
    dtype: string
  - name: text
    dtype: string
  - name: file_path
    dtype: string
  - name: dump
    dtype: string
  - name: file_size_in_byte
    dtype: int64
  - name: line_count
    dtype: int64
  splits:
  - name: train
    num_bytes: 254927419643
    num_examples: 100920235
  download_size: 147948949488
  dataset_size: 254927419643
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
![image](https://github.com/user-attachments/assets/66e5afec-060d-43c0-937e-dd7b6b1a26ef)

# OpenCoder Dataset
The OpenCoder dataset is composed of the following datasets:

* [opc-sft-stage1](https://huggingface.co/datasets/OpenCoder-LLM/opc-sft-stage1): the sft data used for opencoder sft-stage1
* [opc-sft-stage2](https://huggingface.co/datasets/OpenCoder-LLM/opc-sft-stage2): the sft data used for opencoder sft-stage2
* [opc-annealing-corpus](https://huggingface.co/datasets/OpenCoder-LLM/opc-annealing-corpus): the synthetic data & algorithmic corpus used for opencoder annealing
* [opc-fineweb-code-corpus](https://huggingface.co/datasets/OpenCoder-LLM/fineweb-code-corpus): the code-related page recalled from fineweb **<-- you are here**
* [opc-fineweb-math-corpus](https://huggingface.co/datasets/OpenCoder-LLM/fineweb-math-corpus): the math-related page recalled from fineweb
* [refineCode-code-corpus-meta](https://huggingface.co/datasets/OpenCoder-LLM/RefineCode-code-corpus-meta): the meta-data of RefineCode

Detailed information about the data can be found in our [paper](https://arxiv.org/abs/2411.04905).


## opc-fineweb-code-corpus

This code-related data from [Fineweb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) was specifically used in [OpenCoder](https://huggingface.co/papers/2411.04905) pre-training. 
We employ fastText in three iterative rounds to recall a final dataset of 55B code and math-related data. 
You can find math-related data at [OpenCoder-LLM/fineweb-math-corpus](https://huggingface.co/datasets/OpenCoder-LLM/fineweb-math-corpus).

*This work belongs to [INF](https://www.infly.cn/).*



## Citation Information
Please consider citing our [paper](https://arxiv.org/abs/2411.04905) if you find this dataset useful:
```
@inproceedings{Huang2024OpenCoderTO,
  title = {OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models},
  author = {Siming Huang and Tianhao Cheng and Jason Klein Liu and Jiaran Hao and Liuyihan Song and Yang Xu and J. Yang and J. H. Liu and Chenchen Zhang and Linzheng Chai and Ruifeng Yuan and Zhaoxiang Zhang and Jie Fu and Qian Liu and Ge Zhang and Zili Wang and Yuan Qi and Yinghui Xu and Wei Chu},
  year = {2024},
  url = {https://arxiv.org/pdf/2411.04905}
}
```