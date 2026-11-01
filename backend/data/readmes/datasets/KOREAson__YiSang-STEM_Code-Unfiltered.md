---
dataset_info:
  features:
  - name: query
    dtype: string
  - name: responses
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 12349516698
    num_examples: 1116000
  download_size: 5500819365
  dataset_size: 12349516698
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
---

**YiSang-STEM_Code-Unfiltered** is a collection of 1.1M long-cot reasoning traces generated via [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B).  
It consists of 128,524 unique Korean prompts related to STEM or Coding topics collected from the web.  

This is **not** from the dataset used to train our KOREAson-0831 series. It's a bigger and unfiltered version, and might be used in our future iterations.


## Citation
```
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
