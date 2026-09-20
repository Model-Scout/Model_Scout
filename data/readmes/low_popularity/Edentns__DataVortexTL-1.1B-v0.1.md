---
tags:
    - text-generation
license: cc-by-nc-sa-4.0
language:
    - ko
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
pipeline_tag: text-generation
datasets:
    - beomi/KoAlpaca-v1.1a
    - jojo0217/korean_rlhf_dataset
    - kyujinpy/OpenOrca-KO
    - nlpai-lab/kullm-v2
widget:
   - text: >
       <|system|>
 
       You are a chatbot who answers User's questions.
 
       <|user|>
 
       대한민국의 수도는 어디야?
 
       <|assistant|>
---

# **DataVortexTL-1.1B-v0.1**

<img src="./DataVortex.png" alt="DataVortex" style="height: 8em;">

## Our Team

| Research & Engineering | Product Management |
| :--------------------: | :----------------: |
|     Kwangseok Yang     |   Seunghyun Choi   |
|     Jeongwon Choi      |    Hyoseok Choi    |

## **Model Details**

### **Base Model**

[TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

### **Trained On**

-   **OS**: Ubuntu 20.04
-   **GPU**: H100 80GB 1ea
-   **transformers**: v4.36.2

### **Dataset**

-   [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a)
-   [jojo0217/korean_rlhf_dataset](https://huggingface.co/datasets/jojo0217/korean_rlhf_dataset)
-   [kyujinpy/OpenOrca-KO](https://huggingface.co/datasets/kyujinpy/OpenOrca-KO)
-   [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2)

### **Instruction format**

It follows **TinyLlama** format.

E.g.

```python
text = """\
<|system|>
당신은 사람들이 정보를 찾을 수 있도록 도와주는 인공지능 비서입니다.</s>
<|user|>
대한민국의 수도는 어디야?</s>
<|assistant|>
대한민국의 수도는 서울입니다.</s>
<|user|>
서울 인구는 총 몇 명이야?</s>
"""
```

## **Model Benchmark**

### **[Ko LM Eval Harness](https://github.com/Beomi/ko-lm-evaluation-harness)**

| Task             |         0-shot |         5-shot |        10-shot |      50-shot |
| :--------------- | -------------: | -------------: | -------------: | -----------: |
| kobest_boolq     |       0.334282 |       0.516446 |       0.500478 |     0.498941 |
| kobest_copa      |       0.515061 |       0.504321 |       0.492927 |      0.50809 |
| kobest_hellaswag |        0.36253 |       0.357733 |       0.355873 |     0.376502 |
| kobest_sentineg  |       0.481146 |       0.657411 |       0.687417 |     0.635703 |
| **Average**      | **0.42325475** | **0.50897775** | **0.50917375** | **0.504809** |

### **[Ko-LLM-Leaderboard](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard)**

| Average | Ko-ARC | Ko-HellaSwag | Ko-MMLU | Ko-TruthfulQA | Ko-CommonGen V2 |
| ------: | -----: | -----------: | ------: | ------------: | --------------: |
|    31.5 |  25.26 |        33.53 |   24.56 |         43.34 |           30.81 |

## **Implementation Code**

This model contains the chat_template instruction format.  
You can use the code below.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("Edentns/DataVortexTL-1.1B-v0.1")
tokenizer = AutoTokenizer.from_pretrained("Edentns/DataVortexTL-1.1B-v0.1")

messages = [
    {"role": "system", "content": "당신은 사람들이 정보를 찾을 수 있도록 도와주는 인공지능 비서입니다."},
    {"role": "user", "content": "대한민국의 수도는 어디야?"},
    {"role": "assistant", "content": "대한민국의 수도는 서울입니다."},
    {"role": "user", "content": "서울 인구는 총 몇 명이야?"}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

## **License**

The model is licensed under the [cc-by-nc-sa-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license, which allows others to copy, modify, and share the work non-commercially, as long as they give appropriate credit and distribute any derivative works under the same license.

<div align="center">
    <a href="https://edentns.com/">
        <img src="./Logo.png" alt="Logo" style="height: 3em;">
    </a>
</div>
