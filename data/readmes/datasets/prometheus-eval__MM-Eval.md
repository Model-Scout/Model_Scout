---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: subset
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: id
    dtype: int64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: test
    num_bytes: 30802291
    num_examples: 11081
  download_size: 13929039
  dataset_size: 30802291
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- ar
- bn
- ca
- de
- en
- es
- eu
- fr
- gl
- it
- ja
- ko
- ru
- sw
- te
- th
- vi
- zh
license: cc-by-sa-4.0
---


 # Multilingual Meta-EVALuation benchmark (MM-Eval)

<p align="center">
<b><a href="https://github.com/guijinSON/MM-Eval/tree/main">👨‍💻Code</a></b>
|
<b><a href="https://arxiv.org/abs/2410.17578">📄Paper</a></b>
|
<b><a href="https://huggingface.co/datasets/prometheus-eval/MMQA">🤗 MMQA</a></b>
</p>

**MM-Eval** is a multilingual meta-evaluation benchmark consisting of five core subsets—Chat, Reasoning, Safety, Language Hallucination, and Linguistics—spanning 18 languages and a Language Resource subset spanning 122 languages for a broader analysis of language effects. 

> **Design Choice**  
> In this work, we minimize the inclusion of translated samples, as mere translation may alter existing preferences due to translation errors. Instead, we increase the proportion of linguistically and culturally related instances. Consequently, translated samples are only included in the Safety subset. Additionally, we enrich the dataset with a Linguistics subset designed to evaluate the judge model's ability to comprehend the linguistic characteristics of various languages accurately. Furthermore, we incorporate hand-crafted culturally related prompts in the Language Hallucination subset. If you are interested, please look into [MMQA (Multilingual, Multicultural Question Answering)](https://huggingface.co/datasets/prometheus-eval/MMQA).


![image/png](https://cdn-uploads.huggingface.co/production/uploads/617f679fb15f8a665f3999fc/FsMVboxBNnEapka7ESj35.png)



### Languages Covered:   
Arabic, Bengali, Catalan, German, English, Spanish, Basque, French, Galacian, Italian, Japanese, Korean, Russian, Swahili, Telugu, Thai, Vietnamese, Chinese

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