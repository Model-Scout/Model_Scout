---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-0.5B
tags:
- chat
---

<hr>

# Llama.cpp imatrix quantizations of Qwen/Qwen2.5-0.5B-Instruct

<img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" alt="qwen" width="60%"/>

Using llama.cpp commit [eca0fab](https://github.com/ggerganov/llama.cpp/commit/eca0fab) for quantization.

Original model: [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant   | Size (MB) | PPL     | Size (%) | Accuracy (%) | PPL error rate |
| ------- | --------- | ------- | -------- | ------------ | -------------- |
| IQ1_S   | 302       | 30.0453 | 31.82    | 50.53        | 0.23714        |
| IQ1_M   | 304       | 24.9151 | 32.03    | 60.93        | 0.19238        |
| IQ2_XXS | 307       | 21.4864 | 32.35    | 70.66        | 0.16704        |
| IQ2_XS  | 310       | 19.7829 | 32.67    | 76.74        | 0.15355        |
| IQ2_S   | 311       | 19.2041 | 32.77    | 79.06        | 0.14841        |
| IQ2_M   | 314       | 18.325  | 33.09    | 82.85        | 0.14001        |
| Q2_K_S  | 316       | 18.3462 | 33.3     | 82.75        | 0.14091        |
| IQ3_XXS | 319       | 16.9784 | 33.61    | 89.42        | 0.12828        |
| Q3_K_S  | 323       | 17.7765 | 34.04    | 85.4         | 0.13668        |
| IQ3_S   | 323       | 16.3794 | 34.04    | 92.69        | 0.12173        |
| IQ3_XS  | 323       | 16.3794 | 34.04    | 92.69        | 0.12173        |
| Q2_K    | 323       | 17.6841 | 34.04    | 85.85        | 0.13561        |
| IQ3_M   | 327       | 16.3667 | 34.46    | 92.76        | 0.12182        |
| IQ4_XS  | 334       | 15.8792 | 35.19    | 95.61        | 0.11933        |
| IQ4_NL  | 337       | 15.8468 | 35.51    | 95.8         | 0.11921        |
| Q4_0    | 337       | 17.1007 | 35.51    | 88.78        | 0.13053        |
| Q3_K_M  | 339       | 15.8499 | 35.72    | 95.79        | 0.11934        |
| Q3_K_L  | 353       | 15.7298 | 37.2     | 96.52        | 0.1182         |
| Q4_1    | 358       | 16.1819 | 37.72    | 93.82        | 0.12328        |
| Q4_K_S  | 368       | 15.5497 | 38.78    | 97.63        | 0.11716        |
| Q5_0    | 380       | 15.5038 | 40.04    | 97.92        | 0.11702        |
| Q4_K_M  | 380       | 15.4428 | 40.04    | 98.31        | 0.11637        |
| Q5_K_S  | 394       | 15.5266 | 41.52    | 97.78        | 0.11682        |
| Q5_1    | 400       | 15.4875 | 42.15    | 98.03        | 0.11641        |
| Q5_K_M  | 401       | 15.4788 | 42.26    | 98.08        | 0.11631        |
| Q6_K    | 483       | 15.2145 | 50.9     | 99.79        | 0.11422        |
| Q8_0    | 507       | 15.239  | 53.42    | 99.63        | 0.11452        |
| F16     | 949       | 15.1819 | 100      | 100          | 0.114          |

<hr>

# Qwen2.5-0.5B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 0.5B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, Attention QKV bias and tied word embeddings
- Number of Parameters: 0.49B
- Number of Paramaters (Non-Embedding): 0.36B
- Number of Layers: 24
- Number of Attention Heads (GQA): 14 for Q and 2 for KV
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

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

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