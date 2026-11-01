---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct/blob/main/LICENSE
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-1.5B
tags:
- chat
---

<hr>

# Llama.cpp imatrix quantizations of Qwen/Qwen2.5-1.5B-Instruct

<img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" alt="qwen" width="60%"/>

Using llama.cpp commit [eca0fab](https://github.com/ggerganov/llama.cpp/commit/eca0fab) for quantization.

Original model: [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant   | Size (MB) | PPL      | Size (%) | Accuracy (%) | PPL error rate |
| ------- | --------- | -------- | -------- | ------------ | -------------- |
| IQ1_S   | 417       | 193.6245 | 14.13    | 5.24         | 1.77149        |
| IQ1_M   | 443       | 66.9068  | 15.01    | 15.17        | 0.52878        |
| IQ2_XXS | 488       | 33.3356  | 16.54    | 30.45        | 0.25559        |
| IQ2_XS  | 525       | 20.287   | 17.79    | 50.04        | 0.14936        |
| IQ2_S   | 538       | 18.2927  | 18.23    | 55.49        | 0.1338         |
| IQ2_M   | 574       | 15.4838  | 19.45    | 65.56        | 0.11113        |
| Q2_K_S  | 611       | 16.0169  | 20.7     | 63.38        | 0.11623        |
| IQ3_XXS | 638       | 12.3935  | 21.62    | 81.91        | 0.0877         |
| Q2_K    | 645       | 14.1657  | 21.86    | 71.66        | 0.10105        |
| IQ3_XS  | 698       | 11.7112  | 23.65    | 86.68        | 0.08256        |
| Q3_K_S  | 726       | 12.4782  | 24.6     | 81.35        | 0.08842        |
| IQ3_S   | 728       | 11.4241  | 24.67    | 88.86        | 0.07977        |
| IQ3_M   | 741       | 11.4058  | 25.11    | 89           | 0.07862        |
| Q3_K_M  | 786       | 11.3529  | 26.64    | 89.42        | 0.08018        |
| Q3_K_L  | 840       | 11.1934  | 28.46    | 90.69        | 0.07913        |
| IQ4_XS  | 855       | 10.5302  | 28.97    | 96.4         | 0.07351        |
| IQ4_NL  | 893       | 10.5116  | 30.26    | 96.57        | 0.07335        |
| Q4_0    | 895       | 10.8217  | 30.33    | 93.8         | 0.07576        |
| Q4_K_S  | 897       | 10.5236  | 30.4     | 96.46        | 0.0736         |
| Q4_K_M  | 941       | 10.4628  | 31.89    | 97.02        | 0.0731         |
| Q4_1    | 970       | 10.51    | 32.87    | 96.59        | 0.07347        |
| Q5_K_S  | 1048      | 10.2715  | 35.51    | 98.83        | 0.07148        |
| Q5_0    | 1051      | 10.3196  | 35.62    | 98.37        | 0.07212        |
| Q5_K_M  | 1073      | 10.2529  | 36.36    | 99.01        | 0.07143        |
| Q5_1    | 1126      | 10.2624  | 38.16    | 98.92        | 0.0714         |
| Q6_K    | 1214      | 10.203   | 41.14    | 99.49        | 0.07108        |
| Q8_0    | 1571      | 10.167   | 53.24    | 99.84        | 0.07068        |
| F16     | 2951      | 10.1512  | 100      | 100          | 0.07058        |

<hr>

# Qwen2.5-1.5B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 1.5B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, Attention QKV bias and tied word embeddings
- Number of Parameters: 1.54B
- Number of Paramaters (Non-Embedding): 1.31B
- Number of Layers: 28
- Number of Attention Heads (GQA): 12 for Q and 2 for KV
- Context Length: Full 32,768 tokens and generation 8192 tokens

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2.5/), [GitHub](https://github.com/QwenLM/Qwen2.5), and [Documentation](https://qwen.readthedocs.io/en/latest/).

## Requirements

The code of Qwen2.5 has been in the latest Hugging face `transformers` and we advise you to use the latest version of `transformers`.

With `transformers<4.37.0`, you will encounter the following error:
```
KeyError: 'qwen2'
```

## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-1.5B-Instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```


## Evaluation & Performance

Detailed evaluation results are reported in this [📑 blog](https://qwenlm.github.io/blog/qwen2.5/).

For requirements on GPU memory and the respective throughput, see results [here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html).

## Citation

If you find our work helpful, feel free to give us a cite.

```
@misc{qwen2.5,
    title = {Qwen2.5: A Party of Foundation Models},
    url = {https://qwenlm.github.io/blog/qwen2.5/},
    author = {Qwen Team},
    month = {September},
    year = {2024}
}

@article{qwen2,
      title={Qwen2 Technical Report}, 
      author={An Yang and Baosong Yang and Binyuan Hui and Bo Zheng and Bowen Yu and Chang Zhou and Chengpeng Li and Chengyuan Li and Dayiheng Liu and Fei Huang and Guanting Dong and Haoran Wei and Huan Lin and Jialong Tang and Jialin Wang and Jian Yang and Jianhong Tu and Jianwei Zhang and Jianxin Ma and Jin Xu and Jingren Zhou and Jinze Bai and Jinzheng He and Junyang Lin and Kai Dang and Keming Lu and Keqin Chen and Kexin Yang and Mei Li and Mingfeng Xue and Na Ni and Pei Zhang and Peng Wang and Ru Peng and Rui Men and Ruize Gao and Runji Lin and Shijie Wang and Shuai Bai and Sinan Tan and Tianhang Zhu and Tianhao Li and Tianyu Liu and Wenbin Ge and Xiaodong Deng and Xiaohuan Zhou and Xingzhang Ren and Xinyu Zhang and Xipin Wei and Xuancheng Ren and Yang Fan and Yang Yao and Yichang Zhang and Yu Wan and Yunfei Chu and Yuqiong Liu and Zeyu Cui and Zhenru Zhang and Zhihao Fan},
      journal={arXiv preprint arXiv:2407.10671},
      year={2024}
}
```