---
license: apache-2.0
tags:
- finetuned
- chat
language:
- en
- ko
- ja
pipeline_tag: text-generation
library_name: transformers
extra_gated_fields:
  Full Name: text
  Email: text
  Organization: text
---

# Trida-7B-Preview

## Introduction

🚀 Trida-7B-Preview: Block Diffusion Language Model

We introduce Trida-7B-Preview, a high-performance 7-billion parameter language model representing the first publicly released Block Diffusion Language Model to originate from Korea.

### Model Overview
Architecture: Block Diffusion Language Model

Base Model: Continually pre-trained from the highly efficient Tri-7B model.


Korean Language Leadership
Trida-7B-Preview sets a new benchmark for generative models in the region. To our knowledge, it is the:

- First Block Diffusion Language Model to be openly released in Korea.

- Best-performing diffusion language model in Korean among similar model sizes.

This model is a significant step forward for the Korean LLM community, demonstrating the effectiveness of the Block Diffusion paradigm for complex, multilingual tasks.



### Key Highlights
* **Block Diffusion Architecture**: Trida-7B-Preview leverages the **Block Diffusion** architecture, combining the strengths of **parallelized diffusion generation** with **autoregressive dependencies** for improved efficiency, control, and flexible-length sequence generation. 
* **Multilingual Leadership**: Specially optimized for **Korean, English, and Japanese**, offering robust performance across all three languages.
* **Korean First**: To our knowledge, Trida-7B-Preview is the **first Block Diffusion Language Model** to be openly released in Korea.
* **Best-in-Class Korean Performance**: It is the **best-performing diffusion language model in Korean** among models of similar size, setting a new benchmark for generative models in the region.


### Model Specifications

#### Trida-7B-Preview
- Type: Block Diffusion Language Model
- Training Stage: Pre-training & Post-training
- Architecture: Transformer Decoder with RoPE, SwiGLU, RMSNorm
- Number of Parameters: 7.76B
- Number of Layers: 32
- Number of Attention Heads: 32
- Context Length: 4,096
- Vocab Size: 128,256

#### 🔄 Training and Methodology
We followed the methodology outlined in the Fast-dLLM-v2 approach (as seen in the model: Efficient-Large-Model/Fast_dLLM_v2_7B [https://huggingface.co/Efficient-Large-Model/Fast_dLLM_v2_7B]).

Continual Pre-training from Tri-7B:
Trida-7B-Preview was continually pre-trained starting from our autoregressive model, trillionlabs/Tri-7B. This process was executed using a Block Diffusion training paradigm to transition the efficient base model into a highly capable generative model.


## 🚀 Quickstart



```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "trillionlabs/Trida-7B-Preview"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

prompt = "Hey Trida. Why don'y you try that?"
messages = [
    {"role": "system", "content": "You are Trida, created by TrillionLabs. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Fast-dLLM v2 style parallel decoding
gen_ids = model.generate(
    inputs["input_ids"],
    tokenizer=tokenizer,
    max_new_tokens=2048,
    small_block_size=8,
    threshold=0.9,
)

response = tokenizer.decode(
    gen_ids[0][inputs["input_ids"].shape[1]:], 
    skip_special_tokens=True
)
print(response)
```

You can also checkout our repo (https://github.com/trillion-labs/Fast-dLLM-Trida) for evaluation and demo.

---



## Evaluation

We evaluated Trida-7B-Preview across a comprehensive suite of benchmarks assessing general reasoning, knowledge recall, coding abilities, mathematical reasoning, and instruction-following capabilities.

<details>
<summary> Full evaluation settings </summary>

| Benchmark | Language | Evaluation Setting | Metric |
|:----------|:---------|:------------------|:-------|
| **General Reasoning and Factuality** | | | |
| • xwinograd_en | English | 0-shot | accuracy |
| • xwinograd_jp | Japanese | 0-shot | accuracy |
| • KoBEST | Korean | 5-shot | accuracy |
| **Knowledge and Reasoning** | | | |
| • KMMLU | Korean | 5-shot | accuracy |
| • MMLU | English | 5-shot | accuracy |
| • Global-MMLU-Lite-en | English | 5-shot | accuracy |
| • Global-MMLU-Lite-ko | English | 5-shot | accuracy |
| • Global-MMLU-Lite-ja | English | 5-shot | accuracy |
| **Coding** | | | |
| • HumanEval | English | 0-shot | pass@1 |
| • MBPPPlus | English | 0-shot | pass@1 |
| **Mathematical Reasoning** | | | |
| • GSM8k | English | 0-shot, CoT | exact-match |
| • KoGSM8k | Korean | 0-shot, CoT | exact-match |
| • MATH500 | English | 0-shot, CoT | exact-match |
| **Instruction Following and Chat** | | | |
| • IFEval | English | 0-shot | strict-prompt |
| • koIFEval | Korean | 0-shot | strict-prompt |


</details>

### Benchmark Results

### General Reasoning and Factuality

| Benchmark | Tria-7B-Preview |
| --- | --- |
| KoBEST | 74.08 |
| KMMLU | 50.28 |
| MMLU | 67.23 |
| Global-MMLU-Lite-en | 73.5 |
| Global-MMLU-Lite-ko | 64.25 |
| xwinograd_en | 69.81 |
| xwinograd_jp | 64.75 |

### Coding

| Benchmark | Tria-7B-Preview |
| --- | --- |
| HumanEval | 35.98 |
| MBPPPlus | 42.59 |

### Mathematical Reasoning

| Benchmark | Trida-7B-Preview |
| --- | --- |
| GSM8k | 50.42 |
| KoGSM8k | 51.18 |
| MATH500 | 24.4 |

### Instruction Following

| Benchmark | Trida-7B-Preview |
| --- | --- |
| IFEval | 63.31 |
| koIFEval | 68.6 |

## Limitations

- Language Support: The model is optimized for English, Korean, and Japanese. Usage with other languages may result in degraded performance.
- Knowledge Cutoff: The model's information is limited to data available up to Febuary, 2025.

## License
This model is licensed under the Apache License 2.0.


## Contact
For inquiries, please contact: info@trillionlabs.co