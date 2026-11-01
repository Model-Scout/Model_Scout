---
base_model: LGAI-EXAONE/K-EXAONE-236B-A23B
base_model_relation: quantized
license: other
license_name: k-exaone
license_link: LICENSE
language:
  - en
  - ko
  - es
  - de
  - ja
  - vi
tags:
  - lg-ai
  - exaone
  - k-exaone
pipeline_tag: text-generation
library_name: transformers
---

<br>
<br>
<p align="center">
<img src="assets/K-EXAONE_logo_gray.png" width="400">
<br>
<br>
<br>

<div align="center">
  <a href="https://huggingface.co/collections/LGAI-EXAONE/k-exaone" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/🤗-HuggingFace-FC926C?style=for-the-badge" alt="HuggingFace">
  </a>
  <a href="https://www.lgresearch.ai/blog/view?seq=619" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/📝-Blog-E343BD?style=for-the-badge" alt="Blog">
  </a>
  <a href="https://arxiv.org/abs/2601.01739" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/📑-Technical_Report-684CF4?style=for-the-badge" alt="Technical Report">
  </a>
  <a href="https://github.com/LG-AI-EXAONE/K-EXAONE" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/🖥️-GitHub-2B3137?style=for-the-badge" alt="GitHub">
  </a>
  <a href="https://friendli.ai/model/LGAI-EXAONE/K-EXAONE-236B-A23B" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/✈️_API-Try_on_FriendliAI-2649BC?style=for-the-badge" alt="FriendliAI">
  </a>
</div>



<div align="center">
<table><tr><td>Check out the <span style="color: orange"> <b>NVFP4+GPTQ weights by FuriosaAI</b>! </span> <a href="https://huggingface.co/FuriosaAIShareLGAI/K-EXAONE-236B-A23B-NVFP4A16-GPTQ" style="text-decoration: none;"> ➡️ link</a> </td></tr></table>
</div>

<br>

# K-EXAONE-236B-A23B-FP8

## Introduction

We introduce **K-EXAONE**, a large-scale multilingual language model developed by LG AI Research. Built using a Mixture-of-Experts architecture, K-EXAONE features **236 billion total** parameters, with **23 billion active** during inference. Performance evaluations across various benchmarks demonstrate that K-EXAONE excels in reasoning, agentic capabilities, general knowledge, multilingual understanding, and long-context processing.

#### Key Features

- **Architecture & Efficiency:** Features a 236B fine-grained MoE design (23B active) optimized with **Multi-Token Prediction (MTP)**, enabling self-speculative decoding that boosts inference throughput by approximately 1.5x.
- **Long-Context Capabilities:** Natively supports a **256K context window**, utilizing a **3:1 hybrid attention** scheme with a **128-token sliding window** to significantly minimize memory usage during long-document processing.
- **Multilingual Support:** Covers 6 languages: Korean, English, Spanish, German, Japanese, and Vietnamese. Features a redesigned **150k vocabulary** with **SuperBPE**, improving token efficiency by ~30%.
- **Agentic Capabilities:** Demonstrates superior tool-use and search capabilities via **multi-agent strategies.**
- **Safety & Ethics:** Aligned with **universal human values**, the model uniquely incorporates **Korean cultural and historical contexts** to address regional sensitivities often overlooked by other models. It demonstrates high reliability across diverse risk categories.

For more details, please refer to the [technical report](https://arxiv.org/abs/2601.01739), [blog](https://www.lgresearch.ai/blog/view?seq=619) and [GitHub](https://github.com/LG-AI-EXAONE/K-EXAONE).

![main_figure](assets/main_figure.png)


### Model Configuration

- Number of Parameters: 236B in total and 23B activated
- Number of Parameters (without embeddings): 234B
- Hidden Dimension: 6,144
- Number of Layers: 48 Main layers + 1 MTP layers
  - Hybrid Attention Pattern: 12 x (3 Sliding window attention + 1 Global attention)
- Sliding Window Attention
  - Number of Attention Heads: 64 Q-heads and 8 KV-heads
  - Head Dimension: 128 for both Q/KV
  - Sliding Window Size: 128
- Global Attention
  - Number of Attention Heads: 64 Q-heads and 8 KV-heads
  - Head Dimension: 128 for both Q/KV
  - No Rotary Positional Embedding Used (NoPE)
- Mixture of Experts:
  - Number of Experts: 128
  - Number of Activated Experts: 8
  - Number of Shared Experts: 1
  - MoE Intermediate Size: 2,048
- Vocab Size: 153,600
- Context Length: 262,144 tokens
- Knowledge Cutoff: Dec 2024 (2024/12)
- Quantization: FP8 Quantization


## Evaluation Results

The following table shows the evaluation results of the quantized model compared to the original K-EXAONE model. Evaluation results of the original model against other models are available on the [GitHub](https://github.com/LG-AI-EXAONE/K-EXAONE#performance) page or in the [model card](https://huggingface.co/LGAI-EXAONE/K-EXAONE-236B-A23B#evaluation-results) of the original model.
Detailed evaluation configurations and results can be found in the [technical report](https://arxiv.org/abs/2601.01739).

<!-- Eval 결과 FP8 걸로 넣기 -->
<table>
    <tr>
        <th>Quantization Type</th>
        <th>AIME 2025</th>
        <th>LiveCodeBench v6</th>
        <th>GPQA-Diamond</th>
        <th>KMMLU-Pro</th>
        <th>IFBench</th>
    </tr>
    <tr>
        <td align="center">BF16</td>
        <td align="center">92.76</td>
        <td align="center">80.72</td>
        <td align="center">79.10</td>
        <td align="center">67.33</td>
        <td align="center">67.30</td>
    </tr>
    <tr>
        <td align="center">FP8</td>
        <td align="center">92.76</td>
        <td align="center">80.43</td>
        <td align="center">79.80</td>
        <td align="center">67.44</td>
        <td align="center">66.92</td>
    </tr>
</table>

## Requirements

K-EXAONE is supported by multiple libraries. Please install the required libraries as needed for your use case.

#### Transformers

You should install `transformers >= 5.1.0` for the K-EXAONE model.

For quantized weights, you also need to install `compressed-tensors` as well. You can install it as below:
```bash
pip install "compressed-tensors>=0.13.0"
```

#### vLLM

To serve the K-EXAONE model on a vLLM server, you should install both Transformers and vLLM (`vllm >= 0.14.0`).

#### SGLang

You should install both Transformers and SGLang to serve the K-EXAONE model on SGLang server.
You can install the latest version of SGLang from source using the following commands.
```bash
git clone https://github.com/sgl-project/sglang.git
pip install -e sglang/python
```


## Quickstart

You can use the K-EXAONE model with the Transformers library version `5.1.0` or later.

### Reasoning mode

For tasks that require accurate results, you can run the K-EXAONE model in reasoning mode as below.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "LGAI-EXAONE/K-EXAONE-236B-A23B-FP8"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="bfloat16",
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "system", "content": "You are K-EXAONE, a large language model developed by LG AI Research in South Korea, built to serve as a helpful and reliable assistant."},
    {"role": "user", "content": "Which one is bigger, 3.9 vs 3.12?"}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    enable_thinking=True,   # skippable (default: True)
)

generated_ids = model.generate(
    **input_ids.to(model.device),
    max_new_tokens=16384,
    temperature=1.0,
    top_p=0.95,
    do_sample=True,
)
output_ids = generated_ids[0][input_ids['input_ids'].shape[-1]:]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

### Non-reasoning mode

For tasks where latency matters more than accuracy, you can run the K-EXAONE model in non-reasoning mode as below.

```python
messages = [
    {"role": "system", "content": "You are K-EXAONE, a large language model developed by LG AI Research in South Korea, built to serve as a helpful and reliable assistant."},
    {"role": "user", "content": "Explain how wonderful you are"}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    enable_thinking=False,
)

generated_ids = model.generate(
    **input_ids.to(model.device),
    max_new_tokens=1024,
    temperature=1.0,
    top_p=0.95,
    do_sample=True,
)
output_ids = generated_ids[0][input_ids['input_ids'].shape[-1]:]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

### Agentic tool use

For your AI-powered agent, you can leverage K-EXAONE’s tool calling capability. 
The K-EXAONE model is compatible with both OpenAI and HuggingFace tool calling specifications. 
The example below demonstrates tool calling using HuggingFace’s docstring-to-tool-schema utility.

Please check the [example file](examples/example_output_search.txt) for an example of a search agent conversation using K-EXAONE.

```python
from transformers.utils import get_json_schema

def roll_dice(max_num: int):
    """
    Roll a dice with the number 1 to N. User can select the number N.

    Args:
        max_num: The maximum number on the dice.
    """
    return random.randint(1, max_num)

tool_schema = get_json_schema(roll_dice)
tools = [tool_schema]

messages = [
    {"role": "system", "content": "You are K-EXAONE, a large language model developed by LG AI Research in South Korea, built to serve as a helpful and reliable assistant."},
    {"role": "user", "content": "Roll a D20 twice and sum the results."}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    tools=tools,
)

generated_ids = model.generate(
    **input_ids.to(model.device),
    max_new_tokens=16384,
    temperature=1.0,
    top_p=0.95,
    do_sample=True,
)
output_ids = generated_ids[0][input_ids['input_ids'].shape[-1]:]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```


## Usage Guideline

> [!IMPORTANT]
> To achieve the expected performance, we recommend using the following configurations:
> - We strongly recommend to use `temperature=1.0`, `top_p=0.95`, `presence_penalty=0.0` for best performance.
> - Different from EXAONE-4.0, K-EXAONE uses `enable_thinking=True` as default. Thus, you need to set `enable_thinking=False` when you want to use non-reasoning mode.
>

## Deployment

### TensorRT-LLM

TensorRT-LLM provides official support for the K-EXAONE model. Please refer to the [EXAONE Documentation](https://github.com/NVIDIA/TensorRT-LLM/tree/main/examples/models/core/exaone) in the TensorRT-LLM repository for more information.

### vLLM

We support the K-EXAONE model on vLLM. You need to install `vllm >= 0.14.0`. Please check the [requirements](#requirements) section.
Practically, you can serve the FP8-quantized model with a 256K context length using tensor parallel on 2 H200 GPUs.

After you install the vLLM library with an EXAONE-MoE implementation, you can run the vLLM server by following command:

```bash
vllm serve LGAI-EXAONE/K-EXAONE-236B-A23B-FP8 \
    --reasoning-parser deepseek_v3 \
    --tensor-parallel-size 2 \
    --gpu_memory_utilization 0.94 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes
```

An OpenAI-compatible API server will be available at http://localhost:8000/v1.

You can test the vLLM server by sending a chat completion request as below:

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "LGAI-EXAONE/K-EXAONE-236B-A23B-FP8",
        "messages": [
            {"role": "user", "content": "How many r'\''s in \"strawberry\"?"}
        ],
        "max_tokens": 16384,
        "temperature": 1.0,
        "top_p": 0.95,
        "chat_template_kwargs": {"enable_thinking": true}
    }'
```

If you are interested in using MTP weights for speculative decoding, add according options as below.

```bash
vllm serve LGAI-EXAONE/K-EXAONE-236B-A23B-FP8 \
    --reasoning-parser deepseek_v3 \
    --tensor-parallel-size 2 \
    --gpu_memory_utilization 0.94 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --no-enable-prefix-caching \
    --speculative_config '{
        "method": "mtp", 
        "num_speculative_tokens": 2 
    }'
```

### SGLang

We support the K-EXAONE model on SGLang. You need to install the latest version of the SGLang library from source. Please check the [requirements](#requirements) section.
Practically, you can serve the model with a 256K context length using tensor parallel on 4 H200 GPUs.

```bash
python -m sglang.launch_server \
    --model LGAI-EXAONE/K-EXAONE-236B-A23B-FP8 \
    --tp-size 4 \
    --reasoning-parser qwen3
```

A SGLang server will be available at http://localhost:30000.

> [!NOTE]
> Currently, using the OpenAI-compatible server is incompatible with the `transformers>=5.0.0rc0`, so you need to use SGLang native API for now.
> For native API, please refer to the [official documentation](https://docs.sglang.io/basic_usage/native_api.html).
> 
> Once the issue is resolved, we will update this section accordingly.

You can test the SGLang server by sending a request as below:

```python
from transformers import AutoTokenizer
import requests

model_name = "LGAI-EXAONE/K-EXAONE-236B-A23B-FP8"
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "user", "content": "How many r'\''s in \"strawberry\"?"}
]
input_text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    return_tensors="pt",
)

response = requests.post(
    f"http://localhost:30000/generate",
    json={
        "text": input_text,
        "sampling_params": {
            "temperature": 1.0,
            "top_p": 0.95,
            "max_new_tokens": 16384,
        },
    },
)
print(response.json()['text'])
```

If you are interested in in using MTP weights for speculative decoding, add according options as below.

```bash
python -m sglang.launch_server \
    --model LGAI-EXAONE/K-EXAONE-236B-A23B-FP8 \
    --tp-size 4 \
    --reasoning-parser qwen3 \
    --speculative-algorithm EAGLE \
    --speculative-num-steps 3 \
    --speculative-eagle-topk 1 \
    --speculative-num-draft-tokens 4
```


## Limitation

The K-EXAONE language model has certain limitations and may occasionally generate inappropriate responses. The language model generates responses based on the output probability of tokens, and it is determined during learning from training data. While we have made every effort to exclude personal, harmful, and biased information from the training data, some problematic content may still be included, potentially leading to undesirable responses. Please note that the text generated by K-EXAONE language model does not reflect the views of LG AI Research.

- Inappropriate answers may be generated, which contain personal, harmful or other inappropriate information.
- Biased responses may be generated, which are associated with age, gender, race, and so on.
- The generated responses rely heavily on statistics from the training data, which can result in the generation of semantically or syntactically incorrect sentences.
- Since the model does not reflect the latest information, the responses may be false or contradictory.

LG AI Research strives to reduce potential risks that may arise from K-EXAONE language models. Users are not allowed to engage in any malicious activities (e.g., keying in illegal information) that may induce the creation of inappropriate outputs violating LG AI's ethical principles when using K-EXAONE language models.


## License

The model is licensed under [K-EXAONE AI Model License Agreement](./LICENSE)


## Citation

```
@article{k-exaone,
  title={K-EXAONE Technical Report},
  author={{LG AI Research}},
  journal={arXiv preprint arXiv:2601.01739},
  year={2025}
}
```

## Contact

LG AI Research Technical Support: contact_us@lgresearch.ai

