---
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
tags:
- lg-ai
- exaone
- exaone-3.5
pipeline_tag: text-generation
library_name: transformers
---

<br><img src="https://cdn-uploads.huggingface.co/production/uploads/646410e04bf9122922289dc7/b1ahV_SP1O43rTXACjmyz.webp" width="720"><br>

# Llama.cpp imatrix quantizations of [LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct)

Using llama.cpp commit [5783575](https://github.com/ggerganov/llama.cpp/commit/5783575) for quantization.

All quants were made using the imatrix option and Bartowski's [calibration file](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).

<hr>

# Perplexity table (the lower the better)

| Quant                                                                                                                          | Size (MB) | PPL     | Size (%) | Accuracy (%) | PPL error rate |
| ------------------------------------------------------------------------------------------------------------------------------ | --------- | ------- | -------- | ------------ | -------------- |
| [IQ1_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ1_S.gguf)     | 1820      | 26.3205 | 12.20    | 33.81        | 0.40           |
| [IQ1_M](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ1_M.gguf)     | 1955      | 19.0360 | 13.10    | 46.75        | 0.28           |
| [IQ2_XXS](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ2_XXS.gguf) | 2182      | 13.3276 | 14.63    | 66.77        | 0.20           |
| [IQ2_XS](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ2_XS.gguf)   | 2379      | 11.7742 | 15.95    | 75.58        | 0.18           |
| [IQ2_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ2_S.gguf)     | 2514      | 11.3084 | 16.85    | 78.69        | 0.17           |
| [IQ2_M](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ2_M.gguf)     | 2695      | 10.3850 | 18.07    | 85.69        | 0.16           |
| [Q2_K_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q2_K_S.gguf)   | 2730      | 11.2910 | 18.30    | 78.82        | 0.17           |
| [Q2_K](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q2_K.gguf)       | 2912      | 11.1386 | 19.52    | 79.89        | 0.17           |
| [IQ3_XXS](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ3_XXS.gguf) | 3006      | 9.5453  | 20.15    | 93.23        | 0.14           |
| [IQ3_XS](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ3_XS.gguf)   | 3226      | 9.2103  | 21.63    | 96.62        | 0.14           |
| [Q3_K_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q3_K_S.gguf)   | 3365      | 10.0571 | 22.56    | 88.49        | 0.16           |
| [IQ3_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ3_S.gguf)     | 3382      | 9.2420  | 22.67    | 96.29        | 0.14           |
| [IQ3_M](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ3_M.gguf)     | 3479      | 9.0709  | 23.32    | 98.11        | 0.13           |
| [Q3_K_M](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q3_K_M.gguf)   | 3703      | 9.2078  | 24.82    | 96.65        | 0.14           |
| [Q3_K_L](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q3_K_L.gguf)   | 3992      | 9.1908  | 26.76    | 96.83        | 0.14           |
| [IQ4_XS](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ4_XS.gguf)   | 4101      | 9.0166  | 27.49    | 98.70        | 0.14           |
| [Q4_0](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_0.gguf)       | 4316      | 9.4186  | 28.93    | 94.49        | 0.14           |
| [IQ4_NL](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-IQ4_NL.gguf)   | 4318      | 9.0297  | 28.95    | 98.55        | 0.14           |
| [Q4_K_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_K_S.gguf)   | 4332      | 8.9634  | 29.04    | 99.28        | 0.13           |
| [Q4_K_M](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_K_M.gguf)   | 4549      | 8.9107  | 30.50    | 99.87        | 0.13           |
| [Q4_1](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_1.gguf)       | 4743      | 8.9614  | 31.80    | 99.31        | 0.13           |
| [Q5_K_S](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_K_S.gguf)   | 5184      | 8.9042  | 34.75    | 99.94        | 0.13           |
| [Q5_0](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_0.gguf)       | 5198      | 9.0533  | 34.85    | 98.30        | 0.14           |
| [Q5_K_M](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_K_M.gguf)   | 5311      | 8.9100  | 35.60    | 99.88        | 0.13           |
| [Q5_1](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_1.gguf)       | 5625      | 8.9230  | 37.71    | 99.73        | 0.13           |
| [Q6_K](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q6_K.gguf)       | 6121      | 8.8800  | 41.03    | 100.22       | 0.13           |
| [Q8_0](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q8_0.gguf)       | 7927      | 8.8534  | 53.14    | 100.52       | 0.13           |
| [F16](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-F16.gguf)         | 14917     | 8.8992  | 100      | 100          | 0.13           |

<hr>

<p align="center">
<img src="https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct/resolve/main/assets/EXAONE_Symbol+BI_3d.png", width="300", style="margin: 40 auto;">
<br>

# EXAONE-3.5-7.8B-Instruct

## Introduction

We introduce EXAONE 3.5, a collection of instruction-tuned bilingual (English and Korean) generative models ranging from 2.4B to 32B parameters, developed and released by LG AI Research. EXAONE 3.5 language models include: 1) **2.4B model** optimized for deployment on small or resource-constrained devices, 2) **7.8B model** matching the size of its predecessor but offering improved performance, and 3) **32B model** delivering powerful performance. All models support long-context processing of up to 32K tokens. Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes.

For more details, please refer to our [technical report](https://arxiv.org/abs/2412.04862), [blog](https://www.lgresearch.ai/blog/view?seq=507) and [GitHub](https://github.com/LG-AI-EXAONE/EXAONE-3.5).

This repository contains the instruction-tuned 7.8B language model with the following features:

- Number of Parameters (without embeddings): 6.98B
- Number of Layers: 32
- Number of Attention Heads: GQA with 32 Q-heads and 8 KV-heads
- Vocab Size: 102,400
- Context Length: 32,768 tokens

## Quickstart

We recommend to use `transformers` v4.43 or later.

Here is the code snippet to run conversational inference with the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Choose your prompt
prompt = "Explain how wonderful you are"  # English example
prompt = "스스로를 자랑해 봐"       # Korean example

messages = [
    {"role": "system", 
     "content": "You are EXAONE model from LG AI Research, a helpful assistant."},
    {"role": "user", "content": prompt}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
)

output = model.generate(
    input_ids.to("cuda"),
    eos_token_id=tokenizer.eos_token_id,
    max_new_tokens=128,
    do_sample=False,
)
print(tokenizer.decode(output[0]))
```

> ### Note
> The EXAONE 3.5 instruction-tuned language models were trained to utilize the system prompt,
> so we highly recommend using the system prompts provided in the code snippet above.

## Evaluation

The following table shows the evaluation results of real-world use cases. The full evaluation results can be found in the [technical report](https://arxiv.org/abs/2412.04862).

<table>
    <tr>
        <th>Models</th>
        <th>MT-Bench</th>
        <th>LiveBench</th>
        <th>Arena-Hard</th>
        <th>AlpacaEval</th>
        <th>IFEval</th>
        <th>KoMT-Bench[1]</th>
        <th>LogicKor</th>
    </tr>
    <tr>
        <td>EXAONE 3.5 7.8B</td>
        <td align="center"><strong>8.29</strong></td>
        <td align="center"><strong>39.8</strong></td>
        <td align="center"><strong>68.7</strong></td>
        <td align="center"><strong>54.2</strong></td>
        <td align="center"><strong>78.9</strong></td>
        <td align="center"><strong>7.96</strong></td>
        <td align="center"><strong>9.08</strong></td>
    </tr>
    <tr>
        <td>Qwen 2.5 7B</td>
        <td align="center">6.48</td>
        <td align="center">35.6</td>
        <td align="center">48.9</td>
        <td align="center">31.7</td>
        <td align="center">72.5</td>
        <td align="center">5.19</td>
        <td align="center">6.38</td>
    </tr>
    <tr>
        <td>Llama 3.1 8B</td>
        <td align="center">7.59</td>
        <td align="center">28.3</td>
        <td align="center">27.7</td>
        <td align="center">25.7</td>
        <td align="center">74.5</td>
        <td align="center">4.85</td>
        <td align="center">5.99</td>
    </tr>
    <tr>
        <td>Gemma 2 9B</td>
        <td align="center">7.64</td>
        <td align="center">32.1</td>
        <td align="center">43.6</td>
        <td align="center">47.3</td>
        <td align="center">54.7</td>
        <td align="center">7.10</td>
        <td align="center">8.05</td>
    </tr>
    <tr>
        <td>Phi 3 small (7B)</td>
        <td align="center">7.63</td>
        <td align="center">27.9</td>
        <td align="center">26.8</td>
        <td align="center">29.2</td>
        <td align="center">59.5</td>
        <td align="center">3.22</td>
        <td align="center">3.99</td>
    </tr>
</table>

- [1] KoMT-Bench is a dataset created by translating MT-Bench into Korean; see [README](https://github.com/LG-AI-EXAONE/KoMT-Bench) for more details.

## Deployment

EXAONE 3.5 models can be inferred in the various frameworks, such as:
- `TensorRT-LLM`
- `vLLM`
- `SGLang`
- `llama.cpp`
- `Ollama`

Please refer to our [EXAONE 3.5 GitHub](https://github.com/LG-AI-EXAONE/EXAONE-3.5) for more details about the inference frameworks.

## Quantization

We provide the pre-quantized EXAONE 3.5 models with **AWQ** and several quantization types in **GGUF** format. 
Please refer to our [EXAONE 3.5 collection](https://huggingface.co/collections/LGAI-EXAONE/exaone-35-674d0e1bb3dcd2ab6f39dbb4) to find corresponding quantized models.

## Limitation

The EXAONE language model has certain limitations and may occasionally generate inappropriate responses. The language model generates responses based on the output probability of tokens, and it is determined during learning from training data. While we have made every effort to exclude personal, harmful, and biased information from the training data, some problematic content may still be included, potentially leading to undesirable responses. Please note that the text generated by EXAONE language model does not reflects the views of LG AI Research.

- Inappropriate answers may be generated, which contain personal, harmful or other inappropriate information.
- Biased responses may be generated, which are associated with age, gender, race, and so on.
- The generated responses rely heavily on statistics from the training data, which can result in the generation of
semantically or syntactically incorrect sentences.
- Since the model does not reflect the latest information, the responses may be false or contradictory.

LG AI Research strives to reduce potential risks that may arise from EXAONE language models. Users are not allowed
to engage in any malicious activities (e.g., keying in illegal information) that may induce the creation of inappropriate
outputs violating LG AI’s ethical principles when using EXAONE language models.

## License

The model is licensed under [EXAONE AI Model License Agreement 1.1 - NC](./LICENSE)

## Citation
 
```
@article{exaone-3.5,
  title={EXAONE 3.5: Series of Large Language Models for Real-world Use Cases},
  author={LG AI Research},
  journal={arXiv preprint arXiv:https://arxiv.org/abs/2412.04862},
  year={2024}
}
```

## Contact
LG AI Research Technical Support: contact_us@lgresearch.ai
