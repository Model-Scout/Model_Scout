---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-14B-Instruct/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-14B
tags:
- chat
---

<hr>

# Llama.cpp imatrix quantizations of Qwen/Qwen2.5-14B-Instruct

<img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" alt="qwen" width="60%"/>

Using llama.cpp commit [eca0fab](https://github.com/ggerganov/llama.cpp/commit/eca0fab) for quantization.

Original model: [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant   | Size (MB) | PPL     | Size (%) | Accuracy (%) | PPL error rate |
| ------- | --------- | ------- | -------- | ------------ | -------------- |
| IQ1_S   | 3441      | 22.0082 | 12.21    | 27.14        | 0.16818        |
| IQ1_M   | 3693      | 15.079  | 13.11    | 39.62        | 0.1106         |
| IQ2_XXS | 4114      | 9.6047  | 14.6     | 62.2         | 0.06625        |
| IQ2_XS  | 4487      | 8.3649  | 15.92    | 71.41        | 0.05574        |
| IQ2_S   | 4772      | 8.1942  | 16.93    | 72.9         | 0.0548         |
| IQ2_M   | 5109      | 7.7261  | 18.13    | 77.32        | 0.05177        |
| Q2_K_S  | 5148      | 8.0641  | 18.27    | 74.08        | 0.0549         |
| Q2_K    | 5504      | 7.6005  | 19.53    | 78.6         | 0.05146        |
| IQ3_XXS | 5672      | 6.9285  | 20.13    | 86.22        | 0.04547        |
| IQ3_XS  | 6088      | 6.721   | 21.6     | 88.88        | 0.04329        |
| Q3_K_S  | 6352      | 6.8697  | 22.54    | 86.96        | 0.04576        |
| IQ3_S   | 6383      | 6.6246  | 22.65    | 90.17        | 0.04285        |
| IQ3_M   | 6597      | 6.6359  | 23.41    | 90.02        | 0.04256        |
| Q3_K_M  | 7000      | 6.5281  | 24.84    | 91.51        | 0.043          |
| Q3_K_L  | 7558      | 6.4323  | 26.82    | 92.87        | 0.04211        |
| IQ4_XS  | 7744      | 6.2005  | 27.48    | 96.34        | 0.04022        |
| Q4_0    | 8149      | 6.2928  | 28.92    | 94.93        | 0.04095        |
| IQ4_NL  | 8154      | 6.208   | 28.94    | 96.23        | 0.04032        |
| Q4_K_S  | 8177      | 6.163   | 29.02    | 96.93        | 0.03976        |
| Q4_K_M  | 8572      | 6.1311  | 30.42    | 97.43        | 0.03957        |
| Q4_1    | 8958      | 6.1674  | 31.79    | 96.86        | 0.03981        |
| Q5_K_S  | 9791      | 6.0411  | 34.75    | 98.88        | 0.03886        |
| Q5_0    | 9817      | 6.0504  | 34.84    | 98.73        | 0.03895        |
| Q5_K_M  | 10023     | 6.0389  | 35.57    | 98.92        | 0.03888        |
| Q5_1    | 10625     | 6.0366  | 37.71    | 98.96        | 0.03885        |
| Q6_K    | 11564     | 6.0004  | 41.04    | 99.56        | 0.0386         |
| Q8_0    | 14975     | 5.9821  | 53.14    | 99.86        | 0.03842        |
| F16     | 28179     | 5.9737  | 100      | 100          | 0.03835        |

<hr>

# Qwen2.5-14B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 14B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 14.7B
- Number of Paramaters (Non-Embedding): 13.1B
- Number of Layers: 48
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

model_name = "Qwen/Qwen2.5-14B-Instruct"

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