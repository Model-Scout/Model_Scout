---
license: mit
license_name: motif-license
license_link: LICENSE
language:
- en
- ko
pipeline_tag: text-generation
tags:
- text-generation-inference
- conversational
- motif
base_model:
- Motif-Technologies/Motif-2.6B
---

*Last update: 14th august 2025*

# Introduction

**Motif 2.6B v1.1-LC** is an updated version of Motif 2.6B with support for a **16K context length**.  
For more details, you can refer to our [technical report](https://arxiv.org/abs/2508.09148).

# Evaluation
### Comparison to Motif-2.6B v1.

The benchmarks and corresponding scores listed in the table below are taken directly from the [Motif-2.6B v1](Motif-Technologies/Motif-2.6B).

| Benchmark | Metric          | Motif-v1-2.6B | Motif-2.6B-v1.1-LC | Improvement over Motif-2.6B |
| --------- | --------------- | ------------- | ------------------ | --------------------------- |
| MMLU      | 5-shot          | 58.0          | 58.7               | **+1.21%**                  |
| MMLU-Pro  | 5-shot, CoT     | 28.4          | 32.0               | **+12.68%**                 |
| WinoG     | 0-shot          | 59.9          | 60.3               | **+0.67%**                  |
| ARC-E     | 0-shot          | 87.2          | 84.7               | **−2.87%**                  |
| ARC-C     | 0-shot          | 74.2          | 73.0               | **−1.62%**                  |
| SIQA      | 0-shot          | 61.97         | 63.3               | **+2.14%**                  |
| BoolQ     | 0-shot          | 67.76         | 71.0               | **+4.78%**                  |
| MATH      | 4-shot, CoT     | 40.2          | 47.3               | **+17.66%**                 |
| GSM8K     | 8-shot, CoT     | 80.2          | 80.3               | **+0.12%**                  |
| AGIEval   | 3-5-shot        | 30.9          | 31.0               | **+0.32%**                  |
| GPQA      | 0-shot, CoT     | 18.53         | 27.23              | **+46.97%**                 |
| HumanEval | 0-shot / pass@1 | 68.3          | 70.1               | **+2.63%**                  |
|           |                 |               | **Average**        | **+6.61%**                  |


## How to use
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Motif-Technologies/motif-2.6b-v1.1-lc",
    trust_remote_code = True, 
    _attn_implementation = "eager", # also supports flash_attention_2
).cuda()

tokenizer = AutoTokenizer.from_pretrained(
    "Motif-Technologies/motif-2.6b-v1.1-lc", 
    trust_remote_code = True, 
)

query = "What is the capital city of South Korea?"
input_ids = tokenizer.apply_chat_template(
    [
        {'role': 'system', 'content': 'you are an helpful assistant'},
        {'role': 'user', 'content': query},
    ],
    add_generation_prompt = True,
    return_tensors='pt',
).cuda()

output = model.generate(input_ids, max_new_tokens=1024, pad_token_id=tokenizer.eos_token_id)
output = tokenizer.decode(output[0, input_ids.shape[-1]:], skip_special_tokens = True)
print(output)

"""
The capital city of South Korea is Seoul. It is not only the largest city in South Korea but also a major global city known for its rich history, \
vibrant culture, and rapid modernization. Seoul is a bustling metropolis with a population of over 10 million people, making it one of the largest urban centers in the world. \
The city is divided into the administrative districts of Seoul City and Incheon, with Incheon serving as a major port. \
Seoul is renowned for its iconic landmarks, such as the Gyeongbokgung Palace, the Seoul Tower, and the vibrant shopping districts like Myeongdong. It is a hub for technology, finance, and culture, playing a crucial role in both South Korea's economy and its global influence.
"""