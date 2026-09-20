---
license: other
license_name: qwen-research
license_link: https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-3B
tags:
- chat
---

<hr>

# Llama.cpp imatrix quantizations of Qwen/Qwen2.5-3B-Instruct

<img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" alt="qwen" width="60%"/>

Using llama.cpp commit [eca0fab](https://github.com/ggerganov/llama.cpp/commit/eca0fab) for quantization.

Original model: [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant   | Size (MB) | PPL      | Size (%) | Accuracy (%) | PPL error rate |
| ------- | --------- | -------- | -------- | ------------ | -------------- |
| IQ1_S   | 755       | 112.0612 | 12.81    | 8.02         | 0.97138        |
| IQ1_M   | 811       | 42.7456  | 13.76    | 21.03        | 0.34718        |
| IQ2_XXS | 905       | 25.2117  | 15.36    | 35.65        | 0.20222        |
| IQ2_XS  | 984       | 15.9149  | 16.7     | 56.48        | 0.11965        |
| IQ2_S   | 1013      | 14.5975  | 17.19    | 61.58        | 0.1082         |
| IQ2_M   | 1088      | 12.8779  | 18.46    | 69.8         | 0.09436        |
| Q2_K_S  | 1143      | 13.0878  | 19.4     | 68.68        | 0.09636        |
| Q2_K    | 1216      | 11.8001  | 20.63    | 76.18        | 0.08674        |
| IQ3_XXS | 1224      | 10.6049  | 20.77    | 84.76        | 0.07572        |
| IQ3_XS  | 1328      | 10.0306  | 22.54    | 89.61        | 0.06975        |
| Q3_K_S  | 1387      | 15.5457  | 23.54    | 57.82        | 0.11941        |
| IQ3_S   | 1390      | 9.9591   | 23.59    | 90.26        | 0.06984        |
| IQ3_M   | 1420      | 9.9957   | 24.1     | 89.93        | 0.06962        |
| Q3_K_M  | 1517      | 14.0989  | 25.74    | 63.76        | 0.10568        |
| Q3_K_L  | 1629      | 13.8579  | 27.64    | 64.86        | 0.10372        |
| IQ4_XS  | 1659      | 9.2935   | 28.15    | 96.72        | 0.06517        |
| IQ4_NL  | 1741      | 9.2824   | 29.54    | 96.84        | 0.06503        |
| Q4_0    | 1744      | 9.485    | 29.59    | 94.77        | 0.06626        |
| Q4_K_S  | 1750      | 9.2573   | 29.7     | 97.1         | 0.06485        |
| Q4_K_M  | 1841      | 9.2305   | 31.24    | 97.38        | 0.06475        |
| Q4_1    | 1904      | 9.2746   | 32.31    | 96.92        | 0.06512        |
| Q5_K_S  | 2070      | 9.1338   | 35.13    | 98.41        | 0.06402        |
| Q5_0    | 2075      | 9.1513   | 35.21    | 98.22        | 0.06413        |
| Q5_K_M  | 2122      | 9.1339   | 36.01    | 98.41        | 0.06407        |
| Q5_1    | 2235      | 9.1231   | 37.93    | 98.53        | 0.06386        |
| Q6_K    | 2421      | 9.069    | 41.08    | 99.12        | 0.06342        |
| Q8_0    | 3134      | 9.0114   | 53.18    | 99.75        | 0.06285        |
| F16     | 5893      | 8.9888   | 100      | 100          | 0.06268        |

<hr>

# Qwen2.5-3B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 3B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, Attention QKV bias and tied word embeddings
- Number of Parameters: 3.09B
- Number of Paramaters (Non-Embedding): 2.77B
- Number of Layers: 36
- Number of Attention Heads (GQA): 16 for Q and 2 for KV
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

model_name = "Qwen/Qwen2.5-3B-Instruct"

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