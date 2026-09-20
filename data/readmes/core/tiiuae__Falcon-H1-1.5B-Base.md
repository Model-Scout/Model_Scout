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

Currently to use this model you can either rely on Hugging Face `transformers`, `vLLM` or our `llama.cpp` library.

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
# pip install vllm>=0.9.0
vllm serve tiiuae/Falcon-H1-1B-Instruct --tensor-parallel-size 2 --data-parallel-size 1
```

### `llama.cpp`

You can find all GGUF files compatible with `llama.cpp` under [our official collection](https://huggingface.co/collections/tiiuae/falcon-h1-6819f2795bc406da60fab8df)


# Evaluation

Falcon-H1 series perform very well on a variety of tasks, including reasoning tasks. 

| Tasks | Falcon-H1-1.5B | Qwen3-1.7B | Qwen2.5-1.5B | Gemma3-1B | Llama3.2-1B | Falcon3-1B |
| --- | --- | --- | --- | --- | --- | --- |
| **General**  | | | | | |
| BBH | **46.57** | 43.05 | 40.55 | 30.26 | 30.72 | 35.24 |
| MMLU | 61.81 | **62.46** | 61.13 | 26.33 | 32.39 | 45.14 |
| ARC-C | 53.24 | **55.72** | 54.27 | 39.33 | 39.42 | 47.87 |
| HellaSwag | 66.76 | 67.09 | **67.86** | 62.94 | 65.73 | 62.3 |
| Winogrande | 65.59 | **66.3** | 64.56 | 62.59 | 62.75 | 61.17 |
| **Math**  | | | | | |
| GSM8k | 52.01 | **70.74** | 63.0 | 2.2 | 7.05 | 34.95 |
| MATH lvl5 | **20.39** | 16.39 | 8.84 | 1.21 | 0.98 | 3.4 |
| **Science**  | | | | | |
| GPQA | 29.11 | **29.45** | 28.36 | 24.66 | 23.57 | 27.85 |
| MMLU-Pro | **35.53** | 33.81 | 28.72 | 11.31 | 11.8 | 16.11 |
| MMLU-stem | **63.37** | 61.53 | 54.93 | 27.59 | 30.19 | 40.06 |
| **Code**  | | | | | |
| HumanEval | 50.0 | **67.68** | 35.37 | 6.71 | 18.9 | 10.37 |
| HumanEval+ | 42.68 | **60.98** | 29.27 | 5.49 | 16.46 | 9.15 |
| MBPP | 65.08 | **67.72** | 60.05 | 12.7 | 35.98 | 12.43 |
| MBPP+ | 55.03 | **58.99** | 49.47 | 9.52 | 29.89 | 9.52 |

You can check more in detail on our [our release blogpost](https://falcon-lm.github.io/blog/falcon-h1/), detailed benchmarks.

# Useful links

- View [our release blogpost](https://falcon-lm.github.io/blog/falcon-h1/).
- View [our technical report](https://arxiv.org/abs/2507.22448).
- Feel free to join [our discord server](https://discord.gg/trwMYP9PYm) if you have any questions or to interact with our researchers and developers.

# Citation

If the Falcon-H1 family of models were helpful to your work, feel free to give us a cite.

```
@article{falconh1,
    title={Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance},
    author={Jingwei Zuo and Maksim Velikanov and Ilyas Chahed and Younes Belkada and Dhia Eddine Rhayem and Guillaume Kunsch and Hakim Hacid and Hamza Yous and Brahim Farhat and Ibrahim Khadraoui and Mugariya Farooq and Giulia Campesan and Ruxandra Cojocaru and Yasser Djilali and Shi Hu and Iheb Chaabane and Puneesh Khanna and Mohamed El Amine Seddik and Ngoc Dung Huynh and Phuc Le Khac and Leen AlQadi and Billel Mokeddem and Mohamed Chami and Abdalgader Abubaker and Mikhail Lubinets and Kacper Piskorski and Slim Frikha},
    journal = {arXiv preprint arXiv:2507.22448},
    year={2025}
}
```