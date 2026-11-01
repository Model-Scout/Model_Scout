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

# Trida-7B

## Introduction

🚀 Trida-7B: Block Diffusion Language Model

We introduce Trida-7B, a high-performance 7-billion parameter language model representing the first publicly released Block Diffusion Language Model to originate from Korea.

### Model Overview
Architecture: Block Diffusion Language Model

Base Model: Continually pre-trained from Tri-7B model.


Korean Language Leadership
Trida-7B sets a new benchmark for generative models in the region. To our knowledge, it is the:

- First Block Diffusion Language Model to be openly released in Korea.

- First Block Diffusion Language Model trained with Step-wise autoregressive attention.

- Best-performing diffusion language model in Korean among similar model sizes.

This model is a significant step forward for the Korean LLM community, demonstrating the effectiveness of the Block Diffusion paradigm for complex, multilingual tasks.



### Key Highlights
* **Block Diffusion Architecture**: Trida-7B leverages the **Block Diffusion** architecture, combining the strengths of **parallelized diffusion generation** with **autoregressive dependencies** for improved efficiency, control, and flexible-length sequence generation.
* **Step-wise Autoregressive Attention** An attention mechanism that enables single-pass training and efficient RL by fixing attention masks during the unmasking process. Also improves inference efficiency by enabling kv-caching within the current block.
* **Multilingual Leadership**: Specially optimized for **Korean, English, and Japanese**, offering robust performance across all three languages.
* **Korean First**: To our knowledge, Trida-7B-Preview is the **first Block Diffusion Language Model** to be openly released in Korea.
* **Best-in-Class Korean Performance**: It is the **best-performing diffusion language model in Korean** among models of similar size, setting a new benchmark for generative models in the region.


### Model Specifications

#### Trida-7B
- Type: Block Diffusion Language Model
- Training Stage: Pre-training & Post-training
- Architecture: Transformer Decoder with RoPE, SwiGLU, RMSNorm
- Number of Parameters: 7.76B
- Number of Layers: 32
- Number of Attention Heads: 32
- Context Length: 8,192
- Vocab Size: 128,256

#### 🔄 Training and Methodology

Continual Pre-training from Tri-7B:
Rather than training from scratch, Trida-7B was developed through Continual Pre-training from our state-of-the-art autoregressive model, trillionlabs/Tri-7B.
- Knowledge Transfer: To prevent catastrophic forgetting during the transition from AR to Diffusion, we employed blocksize warmup.

Step-wise Autoregressive Attention for Efficient RL & Inference
One of the most significant innovations in Trida-7B is the Step-wise Autoregressive Attention mechanism. This design solves the primary bottleneck of Diffusion models: the need for $T$ sequential forward passes during generation and Reinforcement Learning (RL).
- Mechanism: During the rollout process, we fix the attention mask for each token at the exact moment it is "unmasked." This creates a structured, causal-like dependency within a single sequence.
- Single-pass Training: By aligning the denoising steps into a step-wise autoregressive structure, we enable the model to calculate gradients for all denoising steps in a single forward/backward pass.
- Impact: This reduces the computational overhead of RL and iterative inference by up to $1/T$, allowing Trida-7B to achieve training and inference speeds much faster than traditional Autoregressive models while maintaining the diverse generative capabilities of Diffusion.


## 🚀 Quickstart



```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "trillionlabs/Trida-7B"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

prompt = "Explain the Korean concept of 'Sonnim' (guest) and compare it to Japanese 'Omotenashi' in English."
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

# Block Step-wise Autoregressive Generation
gen_ids = model.generate(
    inputs["input_ids"],
    tokenizer=tokenizer,
    max_new_tokens=4096,
    threshold=0.9,
)

response = tokenizer.decode(
    gen_ids[0][inputs["input_ids"].shape[1]:], 
    skip_special_tokens=True
)
print(response)
```

You can also checkout our repo (https://github.com/trillion-labs/Fast-dLLM-Trida) for evaluation and demo.


Our full technical blog post is coming soon—stay tuned!

---



## Evaluation

We evaluated Trida-7B across a comprehensive suite of benchmarks assessing general reasoning, knowledge recall, coding abilities, mathematical reasoning, and instruction-following capabilities.

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
| • Global-MMLU-Lite-ja | Japanese | 5-shot | accuracy |
| • BBH | English | 3-shot, CoT | accuracy |
| • MMLU pro | English | 0-shot, CoT | accuracy |
| **Coding** | | | |
| • HumanEval | English | 0-shot | pass@1 |
| • MBPPPlus | English | 0-shot | pass@1 |
| • KoMBPPPlus | Korean | 0-shot | pass@1 |
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
| Benchmark | Trida-7B |
| --- | --- |
| KoBEST | 74.08 |
| KMMLU | 50.28 |
| MMLU | 67.23 |
| Global-MMLU-Lite-en | 73.5 |
| Global-MMLU-Lite-ko | 64.25 |
| Global-MMLU-Lite-ja | 64.25 |
| xwinograd_en | 69.81 |
| xwinograd_jp | 64.75 |
| BBH | 52.45 |
| MMLU pro | 39.37 |

### Coding
| Benchmark | Trida-7B |
| --- | --- |
| HumanEval | 35.98 |
| MBPP Plus | 50.79 |
| KoMBPP Plus | 46.3 |

### Mathematical Reasoning
| Benchmark | Trida-7B |
| --- | --- |
| GSM8k | 65.13 |
| KoGSM8k | 61.26 |
| MATH500 | 33.6 |

### Instruction Following
| Benchmark | Trida-7B |
| --- | --- |
| IFEval | 64.98 |
| koIFEval | 61.74 |


### Korean Performance Vs Other Diffusion LLMs
| Benchmark | Trida-7B | Llada-7B | Dream-7B | Fast-dllm-v2 |
| --- | --- | --- | --- | --- | 
| KoMBPP Plus (pass@1) | 46.3 | 5.8 | 56.61 | 67.2 |
| koIFEval (prompt-strict) | 53.42 | 22.4| 8.9| 46.17 |  
| koGSM8K (strict extract accuracy) | 61.26 | 38.6 | 25.02 | 56.94 | 
| kobest (accuracy) | 74.92 | 54.55 | 61.92 | 57.22 | 
| KMMLU (accuracy) | 46.35 | 29.33 | 39.84 | 44.36 |
| Global-MMLU-Lite-ko (accuracy)| 60.25 | 20.12 | 55.25 | 55.0 |
| avg| 57.08 |28.47 | 41.26 | 54.48  |




## Limitations

- Language Support: The model is optimized for English, Korean, and Japanese. Usage with other languages may result in degraded performance.
- Knowledge Cutoff: The model's information is limited to data available up to Febuary, 2025.

## License
This model is licensed under the Apache License 2.0.


## Contact
For inquiries, please contact: info@trillionlabs.co