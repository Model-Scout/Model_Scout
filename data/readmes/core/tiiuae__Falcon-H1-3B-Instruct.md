---
library_name: transformers
language:
- ar
- cs
- de
- en
- es
- fr
- hi
- it
- ja
- ko
- nl
- pl
- pt
- ro
- ru
- sv
- ur
- zh
tags:
- falcon-h1
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
base_model: tiiuae/Falcon-H1-3B-Base
inference: true
---

<img src="https://huggingface.co/datasets/tiiuae/documentation-images/resolve/main/falcon_mamba/falcon-h1-logo.png" alt="drawing" width="800"/>

#  Table of Contents

0. [TL;DR](#TL;DR)
1. [Model Details](#model-details)
2. [Training Details](#training-details)
3. [Usage](#usage)
4. [Evaluation](#evaluation)
5. [Citation](#citation)

# TL;DR

# Model Details

## Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae)
- **Model type:** Causal decoder-only
- **Architecture:** Hybrid Transformers + Mamba architecture
- **Language(s) (NLP):** English, Multilingual
- **License:** Falcon-LLM License

# Training details

For more details about the training protocol of this model, please refer to the [Falcon-H1 technical blogpost](https://falcon-lm.github.io/blog/falcon-h1/) and [Technical Report](https://arxiv.org/abs/2507.22448).

# Usage

Currently to use this model you can either rely on Hugging Face `transformers`, `vLLM` or `llama.cpp` library.

## Inference

Make sure to install the latest version of `transformers` or `vllm`, eventually install these packages from source:

```bash
pip install git+https://github.com/huggingface/transformers.git
```

For vLLM, make sure to install `vllm>=0.9.0`:

```bash
pip install "vllm>=0.9.0"
```

### 🤗 transformers

Refer to the snippet below to run H1 models using 🤗 transformers:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "tiiuae/Falcon-H1-1B-Base"

model = AutoModelForCausalLM.from_pretrained(
  model_id,
  torch_dtype=torch.bfloat16,
  device_map="auto"
)

# Perform text generation
```

### vLLM

For vLLM, simply start a server by executing the command below:

```
# pip install vllm
vllm serve tiiuae/Falcon-H1-1B-Instruct --tensor-parallel-size 2 --data-parallel-size 1
```

### `llama.cpp`

You can find all GGUF files under [our official collection](https://huggingface.co/collections/tiiuae/falcon-h1-6819f2795bc406da60fab8df)

# Evaluation

Falcon-H1 series perform very well on a variety of tasks, including reasoning tasks. 

| Tasks | Falcon-H1-3B | Qwen3-4B | Qwen2.5-3B | Gemma3-4B | Llama3.2-3B | Falcon3-3B |
| --- | --- | --- | --- | --- | --- | --- |
| **General**  | | | | | |
| BBH | **53.69** | 51.07 | 46.55 | 50.01 | 41.47 | 45.02 |
| ARC-C | **49.57** | 37.71 | 43.77 | 44.88 | 44.88 | 48.21 |
| TruthfulQA | 53.19 | 51.75 | **58.11** | 51.68 | 50.27 | 50.06 |
| HellaSwag | **69.85** | 55.31 | 64.21 | 47.68 | 63.74 | 64.24 |
| MMLU | **68.3** | 67.01 | 65.09 | 59.53 | 61.74 | 56.76 |
| **Math**  | | | | | |
| GSM8k | **84.76** | 80.44 | 57.54 | 77.41 | 77.26 | 74.68 |
| MATH-500 | 74.2 | **85.0** | 64.2 | 76.4 | 41.2 | 54.2 |
| AMC-23 | 55.63 | **66.88** | 39.84 | 48.12 | 22.66 | 29.69 |
| AIME-24 | 11.88 | **22.29** | 6.25 | 6.67 | 11.67 | 3.96 |
| AIME-25 | 13.33 | **18.96** | 3.96 | 13.33 | 0.21 | 2.29 |
| **Science**  | | | | | |
| GPQA | **33.89** | 28.02 | 28.69 | 29.19 | 28.94 | 28.69 |
| GPQA_Diamond | 38.72 | **40.74** | 35.69 | 28.62 | 29.97 | 29.29 |
| MMLU-Pro | **43.69** | 29.75 | 32.76 | 29.71 | 27.44 | 29.71 |
| MMLU-stem | **69.93** | 67.46 | 59.78 | 52.17 | 51.92 | 56.11 |
| **Code**  | | | | | |
| HumanEval | 76.83 | **84.15** | 73.78 | 67.07 | 54.27 | 52.44 |
| HumanEval+ | 70.73 | **76.83** | 68.29 | 61.59 | 50.0 | 45.73 |
| MBPP | **79.63** | 68.78 | 72.75 | 77.78 | 62.17 | 61.9 |
| MBPP+ | **67.46** | 59.79 | 60.85 | 66.93 | 50.53 | 55.29 |
| LiveCodeBench | 26.81 | **39.92** | 11.74 | 21.14 | 2.74 | 3.13 |
| CRUXEval | 56.25 | **69.63** | 43.26 | 52.13 | 17.75 | 44.38 |
| **Instruction Following**  | | | | | |
| IFEval | **85.05** | 84.01 | 64.26 | 77.01 | 74.0 | 69.1 |
| Alpaca-Eval | 31.09 | 36.51 | 17.37 | **39.64** | 19.69 | 14.82 |
| MTBench | **8.72** | 8.45 | 7.79 | 8.24 | 7.96 | 7.79 |
| LiveBench | 36.86 | **51.34** | 27.32 | 36.7 | 26.37 | 26.01 |

You can check more in detail on our [our release blogpost](https://falcon-lm.github.io/blog/falcon-h1/), detailed benchmarks.

# Useful links

- View [our release blogpost](https://falcon-lm.github.io/blog/falcon-h1/).
- Feel free to join [our discord server](https://discord.gg/trwMYP9PYm) if you have any questions or to interact with our researchers and developers.

# Citation

If the Falcon-H1 family of models were helpful to your work, feel free to give us a cite.

```
@misc{tiifalconh1,
    title = {Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance},
    url = {https://falcon-lm.github.io/blog/falcon-h1},
    author = {Falcon-LLM Team},
    month = {May},
    year = {2025}
}
```