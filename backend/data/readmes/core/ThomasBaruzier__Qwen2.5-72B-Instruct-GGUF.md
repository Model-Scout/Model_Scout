---
license: other
license_name: qwen
license_link: https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-72B
tags:
- chat
---

<br><img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/gDUbZOu1ND0j-th4Q6tep.jpeg" width="720"><br>

# Llama.cpp imatrix quantizations of [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)

Using llama.cpp commit [3ad5451](https://github.com/ggerganov/llama.cpp/commit/3ad5451) for quantization.

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant                                                                                                                  | Size (MB) | PPL       | Size (%) | Accuracy (%) | PPL error rate |
| ---------------------------------------------------------------------------------------------------------------------- | --------- | --------- | -------- | ------------ | -------------- |
| [IQ1_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ1_S.gguf)     | 21639     | 7.6552    | 15.60    | 67.82        | 0.11           |
| [IQ1_M](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ1_M.gguf)     | 22640     | 7.2982    | 16.32    | 71.14        | 0.10           |
| [IQ2_XXS](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ2_XXS.gguf) | 24309     | 6.3958    | 17.53    | 81.18        | 0.09           |
| [IQ2_XS](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ2_XS.gguf)   | 25804     | 6.0909    | 18.61    | 85.25        | 0.08           |
| [IQ2_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ2_S.gguf)     | 26644     | 6.0318    | 19.21    | 86.08        | 0.08           |
| [IQ2_M](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ2_M.gguf)     | 27979     | 5.7589    | 20.17    | 90.16        | 0.08           |
| [Q2_K_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q2_K_S.gguf)   | 28199     | 5.9731    | 20.33    | 86.93        | 0.08           |
| [Q2_K](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q2_K.gguf)       | 28430     | 5.9188    | 20.50    | 87.72        | 0.08           |
| [IQ3_XXS](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ3_XXS.gguf) | 30369     | 5.5227    | 21.90    | 94.01        | 0.07           |
| [IQ3_XS](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ3_XS.gguf)   | 31320     | 5.4357    | 22.58    | 95.52        | 0.07           |
| [IQ3_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ3_S.gguf)     | 32890     | 5.3782    | 23.72    | 96.54        | 0.07           |
| [Q3_K_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q3_K_S.gguf)   | 32890     | 5.4492    | 23.72    | 95.28        | 0.07           |
| [IQ3_M](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ3_M.gguf)     | 33858     | 5.3550    | 24.41    | 96.96        | 0.07           |
| [Q3_K_M](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q3_K_M.gguf)   | 35952     | 5.4069    | 25.92    | 96.03        | 0.07           |
| [Q3_K_L](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q3_K_L.gguf)   | 37675     | 5.4116    | 27.17    | 95.94        | 0.07           |
| [IQ4_XS](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ4_XS.gguf)   | 37869     | 5.2776    | 27.31    | 98.38        | 0.07           |
| [IQ4_NL](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-IQ4_NL.gguf)   | 39401     | 5.2747    | 28.41    | 98.43        | 0.07           |
| [Q4_0](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q4_0.gguf)       | 39466     | 5.2998    | 28.46    | 97.97        | 0.07           |
| [Q4_K_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q4_K_S.gguf)   | 41856     | 5.2535    | 30.18    | 98.83        | 0.07           |
| [Q4_1](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q4_1.gguf)       | 43580     | 5.2801    | 31.42    | 98.33        | 0.07           |
| [Q4_K_M](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q4_K_M.gguf)   | 45219     | 5.2478    | 32.60    | 98.94        | 0.07           |
| [Q5_0](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q5_0.gguf)       | 47984     | 5.2160    | 34.60    | 99.54        | 0.07           |
| [Q5_K_S](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q5_K_S.gguf)   | 48995     | 5.2242    | 35.33    | 99.39        | 0.07           |
| [Q5_K_M](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/blob/main/Qwen2.5-72B-Instruct-Q5_K_M.gguf)   | 51925     | 5.2182    | 37.44    | 99.50        | 0.07           |
| [Q5_1](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/tree/main/Qwen2.5-72B-Instruct-Q5_1)            | 52099     | 5.2212    | 37.57    | 99.44        | 0.07           |
| [Q6_K](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/tree/main/Qwen2.5-72B-Instruct-Q6_K)            | 61366     | 5.1952    | 44.25    | 99.94        | 0.07           |
| [Q8_0](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/tree/main/Qwen2.5-72B-Instruct-Q8_0)            | 73683     | 5.1944    | 53.13    | 99.96        | 0.07           |
| [F16](https://huggingface.co/ThomasBaruzier/Qwen2.5-72B-Instruct-GGUF/tree/main/Qwen2.5-72B-Instruct-F16)              | 138685    | 5.1922    | 100      | 100          | 0.07           |

<hr>

# Qwen2.5-72B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 72B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 72.7B
- Number of Paramaters (Non-Embedding): 70.0B
- Number of Layers: 80
- Number of Attention Heads (GQA): 64 for Q and 8 for KV
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

model_name = "Qwen/Qwen2.5-72B-Instruct"

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