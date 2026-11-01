---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-32B
tags:
- chat
---

<hr>

# Llama.cpp imatrix quantizations of Qwen/Qwen2.5-32B-Instruct

<img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" alt="qwen" width="60%"/>

Using llama.cpp commit [eca0fab](https://github.com/ggerganov/llama.cpp/commit/eca0fab) for quantization.

Original model: [Qwen/Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant   | Size (MB) | PPL     | Size (%) | Accuracy (%) | PPL error rate |
| ------- | --------- | ------- | -------- | ------------ | -------------- |
| IQ1_S   | 6938      | 12.2991 | 11.1     | 44.87        | 0.08384        |
| IQ1_M   | 7565      | 10.2638 | 12.1     | 53.77        | 0.0699         |
| IQ2_XS  | 9497      | 7.3601  | 15.2     | 74.99        | 0.04846        |
| IQ2_S   | 9907      | 7.2397  | 15.85    | 76.23        | 0.04762        |
| IQ2_M   | 10743     | 6.7268  | 17.19    | 82.05        | 0.04354        |
| Q2_K_S  | 10956     | 6.9981  | 17.53    | 78.87        | 0.04644        |
| Q2_K    | 11743     | 6.6603  | 18.79    | 82.87        | 0.04324        |
| IQ3_XXS | 12245     | 6.157   | 19.59    | 89.64        | 0.03929        |
| IQ3_XS  | 13071     | 6.0366  | 20.91    | 91.43        | 0.03833        |
| Q3_K_S  | 13726     | 6.0878  | 21.96    | 90.66        | 0.03872        |
| IQ3_S   | 13769     | 5.9886  | 22.03    | 92.16        | 0.03816        |
| IQ3_M   | 14125     | 5.9942  | 22.6     | 92.07        | 0.03802        |
| Q3_K_M  | 15197     | 5.8008  | 24.32    | 95.14        | 0.03677        |
| Q3_K_L  | 16449     | 5.7812  | 26.32    | 95.47        | 0.03667        |
| IQ4_XS  | 16874     | 5.6502  | 27       | 97.68        | 0.03586        |
| IQ4_NL  | 17817     | 5.6408  | 28.51    | 97.84        | 0.03575        |
| Q4_0    | 17845     | 5.6946  | 28.55    | 96.92        | 0.03599        |
| Q4_K_S  | 17915     | 5.6367  | 28.66    | 97.91        | 0.03561        |
| Q4_K_M  | 18932     | 5.6224  | 30.29    | 98.16        | 0.03554        |
| IQ2_XXS | 8611      | 8.0187  | 13.78    | 68.83        | 0.05388        |
| Q4_1    | 19684     | 5.6586  | 31.49    | 97.53        | 0.03587        |
| Q5_K_S  | 21590     | 5.568   | 34.54    | 99.12        | 0.03515        |
| Q5_0    | 21658     | 5.588   | 34.65    | 98.77        | 0.03538        |
| Q5_K_M  | 22185     | 5.567   | 35.5     | 99.14        | 0.03515        |
| Q5_1    | 23496     | 5.5734  | 37.59    | 99.03        | 0.0352         |
| Q6_K    | 25641     | 5.5305  | 41.03    | 99.79        | 0.03483        |
| Q8_0    | 33208     | 5.5221  | 53.13    | 99.95        | 0.03478        |
| F16     | 62500     | 5.5191  | 100      | 100          | 0.03474        |

<hr>

# Qwen2.5-32B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 32B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 32.5B
- Number of Paramaters (Non-Embedding): 31.0B
- Number of Layers: 64
- Number of Attention Heads (GQA): 40 for Q and 8 for KV
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

model_name = "Qwen/Qwen2.5-32B-Instruct"

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