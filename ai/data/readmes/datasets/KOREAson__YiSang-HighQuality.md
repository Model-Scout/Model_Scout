---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
- en
tags:
- reasoning
- chain-of-thought
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  splits:
  - name: train
    num_bytes: 3859604712
    num_examples: 283687
  download_size: 1734927587
  dataset_size: 3859604712
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# YiSang-HighQuality

<p align="center">
    📖 Check out the KO-REAson <a href="https://arxiv.org/abs/2510.04230" target="_blank">technical report</a>.
    <br>
    📍 Rest of the model and datasets are available <a href="https://huggingface.co/KOREAson">here. </a>
</p>

**YiSang-HighQuality** is a collection of ~280K long-CoT reasoning traces generated via [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B). This dataset is a high-yield subset of the larger Yi-Sang collection, designed to enhance multilingual reasoning through **Language-Mixed Chain-of-Thought (CoT)**, which switches between English and Korean to minimize translation artifacts while leveraging English as a reasoning anchor.

This is the dataset used to train our KOREAson-0831 and 1009 series. 


## Family Details

The **KO-REAson** release includes nine models and three datasets.

| Model (link)                                                                                 | Licence |  Note           |  
| -------------------------------------------------------------------------------------------- | -------------------- | ------------------- | 
| [KO-REAson-AX3_1-35B-1009](https://huggingface.co/KOREAson/KO-REAson-AX3_1-35B-1009)   |     Apache 2.0 | **Our BEST Model**           |  
| [YiSang-HighQuality](https://huggingface.co/datasets/KOREAson/YiSang-HighQuality)   |     Apache 2.0 | **Dataset used for Training**           |  


## Citation
```bibtex
@article{son2025pushing,
  title={Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought},
  author={Son, Guijin and Yang, Donghun and Patel, Hitesh Laxmichand and Agarwal, Amit and Ko, Hyunwoo and Lim, Chanuk and Panda, Srikant and Kim, Minhyuk and Drolia, Nikunj and Choi, Dasol and others},
  journal={arXiv preprint arXiv:2510.04230},
  year={2025}
}
```


## Contact

For any questions contact us via the following email :)

```
spthsrbwls123@yonsei.ac.kr
```