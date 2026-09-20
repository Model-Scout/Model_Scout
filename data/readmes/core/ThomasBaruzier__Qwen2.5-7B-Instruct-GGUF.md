---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-7B
tags:
- chat
---

<hr>

# Llama.cpp imatrix quantizations of Qwen/Qwen2.5-7B-Instruct

<img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" alt="qwen" width="60%"/>

Using llama.cpp commit [eca0fab](https://github.com/ggerganov/llama.cpp/commit/eca0fab) for quantization.

Original model: [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant   | Size (MB) | PPL     | Size (%) | Accuracy (%) | PPL error rate |
| ------- | --------- | ------- | -------- | ------------ | -------------- |
| IQ1_S   | 1816      | 29.2065 | 12.5     | 27.04        | 0.23022        |
| IQ1_M   | 1948      | 17.5876 | 13.4     | 44.9         | 0.13256        |
| IQ2_XXS | 2168      | 13.0997 | 14.92    | 60.28        | 0.10138        |
| IQ2_XS  | 2355      | 10.6611 | 16.21    | 74.06        | 0.07823        |
| IQ2_S   | 2476      | 10.236  | 17.04    | 77.14        | 0.07461        |
| IQ2_M   | 2652      | 9.5241  | 18.25    | 82.91        | 0.06876        |
| Q2_K_S  | 2703      | 9.7181  | 18.6     | 81.25        | 0.07113        |
| Q2_K    | 2877      | 9.271   | 19.8     | 85.17        | 0.06672        |
| IQ3_XXS | 2971      | 8.677   | 20.44    | 91           | 0.06191        |
| IQ3_XS  | 3192      | 8.468   | 21.97    | 93.25        | 0.05972        |
| Q3_K_S  | 3331      | 8.6524  | 22.92    | 91.26        | 0.06144        |
| IQ3_S   | 3338      | 8.4723  | 22.97    | 93.2         | 0.06045        |
| IQ3_M   | 3409      | 8.4488  | 23.46    | 93.46        | 0.05973        |
| Q3_K_M  | 3632      | 8.2232  | 24.99    | 96.02        | 0.05882        |
| Q3_K_L  | 3900      | 8.1675  | 26.84    | 96.68        | 0.05826        |
| IQ4_XS  | 4024      | 8.0803  | 27.69    | 97.72        | 0.0579         |
| IQ4_NL  | 4233      | 8.0301  | 29.13    | 98.33        | 0.05724        |
| Q4_0    | 4239      | 7.9852  | 29.17    | 98.88        | 0.05586        |
| Q4_K_S  | 4252      | 8.0483  | 29.26    | 98.11        | 0.05752        |
| Q4_K_M  | 4467      | 7.997   | 30.74    | 98.74        | 0.05697        |
| Q4_1    | 4648      | 8.1016  | 31.98    | 97.46        | 0.05824        |
| Q5_K_S  | 5069      | 7.9466  | 34.88    | 99.36        | 0.05652        |
| Q5_0    | 5082      | 7.9939  | 34.97    | 98.78        | 0.05726        |
| Q5_K_M  | 5193      | 7.9279  | 35.73    | 99.6         | 0.05633        |
| Q5_1    | 5491      | 7.9334  | 37.79    | 99.53        | 0.05634        |
| Q6_K    | 5965      | 7.9066  | 41.05    | 99.87        | 0.05617        |
| Q8_0    | 7724      | 7.8996  | 53.15    | 99.96        | 0.05614        |
| F16     | 14532     | 7.8961  | 100      | 100          | 0.05608        |

<hr>

# Qwen2.5-7B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 7B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 7.61B
- Number of Paramaters (Non-Embedding): 6.53B
- Number of Layers: 28
- Number of Attention Heads (GQA): 28 for Q and 4 for KV
- Context Length: Full 131,072 tokens and generation 8192 tokens
  - Please refer to [this section](#processing-long-texts) for detailed instructions on how to deploy Qwen2.5 for handling long texts.

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

model_name = "Qwen/Qwen2.5-7B-Instruct"

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

### Processing Long Texts

The current `config.json` is set for context length up to 32,768 tokens.
To handle extensive inputs exceeding 32,768 tokens, we utilize [YaRN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.

For supported frameworks, you could add the following to `config.json` to enable YaRN:
```json
{
  ...,
  "rope_scaling": {
    "factor": 4.0,
    "original_max_position_embeddings": 32768,
    "type": "yarn"
  }
}
```

For deployment, we recommend using vLLM. 
Please refer to our [Documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) for usage if you are not familar with vLLM.
Presently, vLLM only supports static YARN, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts**. 
We advise adding the `rope_scaling` configuration only when processing long contexts is required.

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