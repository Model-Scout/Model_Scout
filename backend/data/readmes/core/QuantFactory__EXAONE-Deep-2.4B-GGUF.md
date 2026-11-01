
---

base_model: LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct
base_model_relation: finetune
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
tags:
- lg-ai
- exaone
- exaone-deep
pipeline_tag: text-generation
library_name: transformers

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/EXAONE-Deep-2.4B-GGUF
This is quantized version of [LGAI-EXAONE/EXAONE-Deep-2.4B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-2.4B) created using llama.cpp

# Original Model Card


<p align="center">
<img src="assets/EXAONE_Symbol+BI_3d.png", width="300", style="margin: 40 auto;">
<br>

# EXAONE-Deep-2.4B

## Introduction

We introduce EXAONE Deep, which exhibits superior capabilities in various reasoning tasks including math and coding benchmarks, ranging from 2.4B to 32B parameters developed and released by LG AI Research. Evaluation results show that 1) EXAONE Deep **2.4B** outperforms other models of comparable size, 2) EXAONE Deep **7.8B** outperforms not only open-weight models of comparable scale but also a proprietary reasoning model OpenAI o1-mini, and 3) EXAONE Deep **32B** demonstrates competitive performance against leading open-weight models.

For more details, please refer to our [documentation](https://arxiv.org/abs/2503.12524), [blog](https://www.lgresearch.ai/news/view?seq=543) and [GitHub](https://github.com/LG-AI-EXAONE/EXAONE-Deep).

<p align="center">
<img src="assets/exaone_deep_overall_performance.png", width="100%", style="margin: 40 auto;">

This repository contains the reasoning 2.4B language model with the following features:

- Number of Parameters (without embeddings): 2.14B
- Number of Layers: 30
- Number of Attention Heads: GQA with 32 Q-heads and 8 KV-heads
- Vocab Size: 102,400
- Context Length: 32,768 tokens
- Tie Word Embeddings: True (unlike 7.8B and 32B models)

## Quickstart

We recommend to use `transformers` v4.43.1 or later.

Here is the code snippet to run conversational inference with the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

model_name = "LGAI-EXAONE/EXAONE-Deep-2.4B"
streaming = True    # choose the streaming option

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Choose your prompt:
#   Math example (AIME 2024)
prompt = r"""Let $x,y$ and $z$ be positive real numbers that satisfy the following system of equations:
\[\log_2\left({x \over yz}\right) = {1 \over 2}\]\[\log_2\left({y \over xz}\right) = {1 \over 3}\]\[\log_2\left({z \over xy}\right) = {1 \over 4}\]
Then the value of $\left|\log_2(x^4y^3z^2)\right|$ is $\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

Please reason step by step, and put your final answer within \boxed{}."""
#   Korean MCQA example (CSAT Math 2025)
prompt = r"""Question : $a_1 = 2$인 수열 $\{a_n\}$과 $b_1 = 2$인 등차수열 $\{b_n\}$이 모든 자연수 $n$에 대하여\[\sum_{k=1}^{n} \frac{a_k}{b_{k+1}} = \frac{1}{2} n^2\]을 만족시킬 때, $\sum_{k=1}^{5} a_k$의 값을 구하여라.

Options :
A) 120
B) 125
C) 130
D) 135
E) 140
 
Please reason step by step, and you should write the correct option alphabet (A, B, C, D or E) within \\boxed{}."""

messages = [
    {"role": "user", "content": prompt}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
)

if streaming:
    streamer = TextIteratorStreamer(tokenizer)
    thread = Thread(target=model.generate, kwargs=dict(
        input_ids=input_ids.to("cuda"),
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=32768,
        do_sample=True,
        temperature=0.6,
        top_p=0.95,
        streamer=streamer
    ))
    thread.start()

    for text in streamer:
        print(text, end="", flush=True)
else:
    output = model.generate(
        input_ids.to("cuda"),
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=32768,
        do_sample=True,
        temperature=0.6,
        top_p=0.95,
    )
    print(tokenizer.decode(output[0]))
```

> ### Note
> The EXAONE Deep models are trained with an optimized configuration,
> so we recommend following the [Usage Guideline](#usage-guideline) section to achieve optimal performance.

## Evaluation

The following table shows the evaluation results of reasoning tasks such as math and coding. The full evaluation results can be found in the [documentation](https://arxiv.org/abs/2503.12524).

<table>
    <tr>
        <th>Models</th>
        <th>MATH-500 (pass@1)</th>
        <th>AIME 2024 (pass@1 / cons@64)</th>
        <th>AIME 2025 (pass@1 / cons@64)</th>
        <th>CSAT Math 2025 (pass@1)</th>
        <th>GPQA Diamond (pass@1)</th>
        <th>Live Code Bench (pass@1)</th>
    </tr>
    <tr>
        <td>EXAONE Deep 32B</td>
        <td>95.7</td>
        <td>72.1 / <strong>90.0</strong></td>
        <td>65.8 / <strong>80.0</strong></td>
        <td><strong>94.5</strong></td>
        <td>66.1</td>
        <td>59.5</td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Qwen-32B</td>
        <td>94.3</td>
        <td>72.6 / 83.3</td>
        <td>55.2 / 73.3</td>
        <td>84.1</td>
        <td>62.1</td>
        <td>57.2</td>
    </tr>
    <tr>
        <td>QwQ-32B</td>
        <td>95.5</td>
        <td>79.5 / 86.7</td>
        <td><strong>67.1</strong> / 76.7</td>
        <td>94.4</td>
        <td>63.3</td>
        <td>63.4</td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Llama-70B</td>
        <td>94.5</td>
        <td>70.0 / 86.7</td>
        <td>53.9 / 66.7</td>
        <td>88.8</td>
        <td>65.2</td>
        <td>57.5</td>
    </tr>
    <tr>
        <td>DeepSeek-R1 (671B)</td>
        <td><strong>97.3</strong></td>
        <td><strong>79.8</strong> / 86.7</td>
        <td>66.8 / <strong>80.0</strong></td>
        <td>89.9</td>
        <td><strong>71.5</strong></td>
        <td><strong>65.9</strong></td>
    </tr>
    <tr>
        <th colspan="7" height="30px"></th>
    </tr>
    <tr>
        <td>EXAONE Deep 7.8B</td>
        <td><strong>94.8</strong></td>
        <td><strong>70.0</strong> / <strong>83.3</strong></td>
        <td><strong>59.6</strong> / <strong>76.7</strong></td>
        <td><strong>89.9</strong></td>
        <td><strong>62.6</strong></td>
        <td><strong>55.2</strong></td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Qwen-7B</td>
        <td>92.8</td>
        <td>55.5 / <strong>83.3</strong></td>
        <td>38.5 / 56.7</td>
        <td>79.7</td>
        <td>49.1</td>
        <td>37.6</td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Llama-8B</td>
        <td>89.1</td>
        <td>50.4 / 80.0</td>
        <td>33.6 / 53.3</td>
        <td>74.1</td>
        <td>49.0</td>
        <td>39.6</td>
    </tr>
    <tr>
        <td>OpenAI o1-mini</td>
        <td>90.0</td>
        <td>63.6 / 80.0</td>
        <td>54.8 / 66.7</td>
        <td>84.4</td>
        <td>60.0</td>
        <td>53.8</td>
    </tr>
    <tr>
        <th colspan="7" height="30px"></th>
    </tr>
    <tr>
        <td>EXAONE Deep 2.4B</td>
        <td><strong>92.3</strong></td>
        <td><strong>52.5</strong> / <strong>76.7</strong></td>
        <td><strong>47.9</strong> / <strong>73.3</strong></td>
        <td><strong>79.2</strong></td>
        <td><strong>54.3</strong></td>
        <td><strong>46.6</strong></td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Qwen-1.5B</td>
        <td>83.9</td>
        <td>28.9 / 52.7</td>
        <td>23.9 / 36.7</td>
        <td>65.6</td>
        <td>33.8</td>
        <td>16.9</td>
    </tr>
</table>

## Deployment

EXAONE Deep models can be inferred in the various frameworks, such as:
- `TensorRT-LLM`
- `vLLM`
- `SGLang`
- `llama.cpp`
- `Ollama`
- `LM-Studio`

Please refer to our [EXAONE Deep GitHub](https://github.com/LG-AI-EXAONE/EXAONE-Deep) for more details about the inference frameworks.

## Quantization

We provide the pre-quantized EXAONE Deep models with **AWQ** and several quantization types in **GGUF** format. Please refer to our [EXAONE Deep collection](https://huggingface.co/collections/LGAI-EXAONE/exaone-deep-67d119918816ec6efa79a4aa) to find corresponding quantized models.

## Usage Guideline

To achieve the expected performance, we recommend using the following configurations:

1. Ensure the model starts with `<thought>\n` for reasoning steps. The model's output quality may be degraded when you omit it. You can easily apply this feature by using `tokenizer.apply_chat_template()` with `add_generation_prompt=True`. Please check the example code on [Quickstart](#quickstart) section.
2. The reasoning steps of EXAONE Deep models enclosed by `<thought>\n...\n</thought>` usually have lots of tokens, so previous reasoning steps may be necessary to be removed in multi-turn situation. The provided tokenizer handles this automatically.
3. Avoid using system prompt, and build the instruction on the user prompt. 
4. Additional instructions help the models reason more deeply, so that the models generate better output.
    - For math problems, the instructions **"Please reason step by step, and put your final answer within \boxed{}."** are helpful.
    - For more information on our evaluation setting including prompts, please refer to our [Documentation](https://arxiv.org/abs/2503.12524).
5. In our evaluation, we use `temperature=0.6` and `top_p=0.95` for generation. 
6. When evaluating the models, it is recommended to test multiple times to assess the expected performance accurately.

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
@article{exaone-deep,
  title={EXAONE Deep: Reasoning Enhanced Language Models},
  author={{LG AI Research}},
  journal={arXiv preprint arXiv:2503.12524},
  year={2025}
}
```

## Contact
LG AI Research Technical Support: contact_us@lgresearch.ai
