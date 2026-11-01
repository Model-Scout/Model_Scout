---
configs:
- config_name: default
  data_files:
  - split: test
    path: data/train-*
language:
- bn
- ko
- eu
- ca
- es
- vi
- ar
---
## Links for Reference

- **Repository: https://github.com/guijinSON/MM-Eval** 
- **Paper: https://arxiv.org/abs/2410.17578** 
- **Point of Contact:spthsrbwls123@yonsei.ac.kr / dkyoon@kaist.ac.kr**
  
# **M**ultilingual **M**ulticultural-**Q**uestion **A**nswering (MMQA)

MMQA is a multilingual and multicultural long-form question-answering dataset, which originated as a subset of the [MM-Eval](https://huggingface.co/datasets/prometheus-eval/MM-Eval) benchmark.
MMQA features long-form question-answer pairs that inquire about culture-related contexts in seven languages: Bengali, Korean, Catalan, Basque, Spanish, Vietnamese, and Arabic. The dataset is designed to evaluate the ability of models to generate detailed, culturally informed answers across diverse languages and contexts.

### Languages Covered:   
Bengali, Korean, Catalan, Basque, Spanish, Vietnamese, Arabic

### Citation:
If you find the following model helpful, please consider citing our paper!
```
@article{son2024mm,
  title={MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models},
  author={Son, Guijin and Yoon, Dongkeun and Suk, Juyoung and Aula-Blasco, Javier and Aslan, Mano and Kim, Vu Trong and Islam, Shayekh Bin and Prats-Cristi{\`a}, Jaume and Tormo-Ba{\~n}uelos, Luc{\'\i}a and Kim, Seungone},
  journal={arXiv preprint arXiv:2410.17578},
  year={2024}
}
```