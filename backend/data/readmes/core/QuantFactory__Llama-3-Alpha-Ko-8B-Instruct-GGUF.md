---
license: other
license_name: llama3
language:
- ko
base_model: allganize/Llama-3-Alpha-Ko-8B-Instruct
pipeline_tag: text-generation
---

# QuantFactory/Llama-3-Alpha-Ko-8B-Instruct-GGUF
This is quantized version of [allganize/Llama-3-Alpha-Ko-8B-Instruct](https://huggingface.co/allganize/Llama-3-Alpha-Ko-8B-Instruct) created using llama.cpp

# Model Description
We are thrilled to introduce **Alpha-Instruct**, our latest language model, which demonstrates exceptional capabilities in both Korean and English. Alpha-Instruct is developed using the **Evolutionary Model Merging** technique, enabling it to excel in complex language tasks and logical reasoning.

A key aspect of Alpha-Instruct's development is our **community-based approach**. We draw inspiration and ideas from various communities, shaping our datasets, methodologies, and the model itself. In return, we are committed to sharing our insights with the community, providing detailed information on the data, methods, and models used in Alpha-Instruct's creation.

Alpha-Instruct has achieved outstanding performance on the **LogicKor, scoring an impressive 6.62**. Remarkably, this performance rivals that of 70B models, showcasing the efficiency and power of our 8B model. This achievement highlights Alpha-Instruct's advanced computational and reasoning skills, making it a leading choice for diverse and demanding language tasks.

**For more information and technical details about Alpha-Instruct, stay tuned to our updates and visit our [website](https://allganize-alpha.github.io/) (Soon).**

---
## Overview
Alpha-Instruct is our latest language model, developed using 'Evolutionary Model Merging' technique. This method employs a 1:1 ratio of task-specific datasets from KoBEST and Haerae, resulting in a model with named 'Alpha-Ko-8B-Evo'. The following models were used for merging:
- [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) (Base)
- [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) (Instruct)
- [Llama-3-Open-Ko-8B](beomi/Llama-3-Open-Ko-8B) (Continual Pretrained)

To refine and enhance Alpha-Instruct, we utilized a carefully curated high-quality datasets aimed at 'healing' the model's output, significantly boosting its human preference scores. We use [ORPO](https://arxiv.org/abs/2403.07691) specifically for this "healing" (RLHF) phase. The datasets* used include:
- [Korean-Human-Judgements](https://huggingface.co/datasets/HAERAE-HUB/Korean-Human-Judgements)
- [Orca-Math](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)
- [dpo-mix-7k](https://huggingface.co/datasets/argilla/dpo-mix-7k)

*Some of these datasets were partially used and translated for training, and we ensured there was no contamination during the evaluation process.

This approach effectively balances human preferences with the model's capabilities, making Alpha-Instruct well-suited for real-life scenarios where user satisfaction and performance are equally important.

## Benchmark Results
Results in [LogicKor](https://github.com/StableFluffy/LogicKor)* are as follows:

|         Model                  | Single turn* | Multi turn* | Overall* |
|:------------------------------:|:------------:|:-----------:|:--------:|
| MLP-KTLim/llama-3-Korean-Bllossom-8B | 4.238 | 3.404 | 3.821 |
| Alpha-Ko-Evo | 5.143 | 5.238 | 5.190 |
| Alpha-Ko-Instruct (alt)  |     7.095    |    **6.571**    |   **6.833**  |
| Alpha-Ko-Instruct |     **7.143**    |    6.065    |   6.620  |
| Alpha-Ko-Instruct-marlin (4bit) | 6.857 | 5.738 | 6.298 |

*Self report(Default settings with 'alpha' template, mean of 3).

Result in KoBEST(acc, num_shot=5) are as follows:

| Task  |	beomi/Llama-3-Open-Ko-8B-Instruct | maywell/Llama-3-Ko-8B-Instruct | **Alpha-Ko-Evo** | **Alpha-Ko-Instruct** |
| --- | --- | --- | --- | --- |
| kobest overall |	0.6220 | 0.6852 |0.7229|0.7055
| kobest_boolq|	0.6254 |	0.7208 | 0.8547 | 0.8369
| kobest_copa|	0.7110 |	0.7650 | 0.7420 | 0.7420
| kobest_hellaswag|	0.3840 |	0.4440 | 0.4220 | 0.4240
| kobest_sentineg|	0.8388 |	0.9194 |0.9471 | 0.9244
| kobest_wic|	0.5738|	0.6040 |0.6095 | 0.5730

*For reference, 'merged' models are chosen.

## How to use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "allganize/Llama-3-Alpha-Ko-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "system", "content": "당신은 인공지능 어시스턴트입니다. 묻는 말에 친절하고 정확하게 답변하세요."},
    {"role": "user", "content": "피보나치 수열이 뭐야? 그리고 피보나치 수열에 대해 파이썬 코드를 짜줘볼래?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    eos_token_id=terminators,
    do_sample=False,
    repetition_penalty=1.05,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```

## Correspondence to
- Ji soo Kim (jisoo.kim@allganize.ai)
- Contributors
  - Sangmin Jeon (sangmin.jeon@allganize.ai)
  - Seungwoo Ryu (seungwoo.ryu@allganize.ai)

## Special Thanks
- [@beomi](https://huggingface.co/beomi) for providing us with a great model!

## License
The use of this model is governed by the [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/)