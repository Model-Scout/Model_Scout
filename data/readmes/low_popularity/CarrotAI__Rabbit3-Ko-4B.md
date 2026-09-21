---
license: apache-2.0
language:
- ko
- en
base_model:
- Qwen/Qwen3-4B
pipeline_tag: text-generation
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64633ebb39359568c63b52ad/r5EnnbDV6eGQQBeNBHu7K.png)

### Model Details
- **Name**: CarrotAI/Rabbit3-Ko-4B
- **Version**: 4B Instruct
- **Base Model**: Qwen/Qwen3-4B
- **Languages**: Korean, English
- **Model Type**: Large Language Model (Instruction-tuned)


Qwen3-4B 기반의 LLM 모델로 한국어 및 영어 데이터셋을 사용하여 파인튜닝한 한국어 모델입니다.
- 2025.05.16 일반모드로만 사용 가능합니다.


### Score

|      Tasks       |Version|     Filter     |n-shot|        Metric         |   |Value |   |Stderr|
|------------------|-------|----------------|-----:|-----------------------|---|-----:|---|------|
|gsm8k             |      3|flexible-extract|     5|exact_match            |↑  |0.8400|±  |0.0101|
|                  |       |strict-match    |     5|exact_match            |↑  |0.8378|±  |0.0102|
|hrm8k             |    N/A|                |      |                       |   |      |   |      |
| - hrm8k_gsm8k    |      1|none            |     0|exact_match            |↑  |0.8196|±  |0.0106|
| - hrm8k_ksm      |      1|none            |     0|exact_match            |↑  |0.0511|±  |0.0058|
| - hrm8k_math     |      1|none            |     0|exact_match            |↑  |0.5539|±  |0.0093|
| - hrm8k_mmmlu    |      1|none            |     0|exact_match            |↑  |0.5362|±  |0.0230|
| - hrm8k_omni_math|      1|none            |     0|exact_match            |↑  |0.1812|±  |0.0088|
|ifeval            |      4|none            |     0|inst_level_loose_acc   |↑  |0.8753|±  |   N/A|
|                  |       |none            |     0|inst_level_strict_acc  |↑  |0.8609|±  |   N/A|
|                  |       |none            |     0|prompt_level_loose_acc |↑  |0.8244|±  |0.0164|
|                  |       |none            |     0|prompt_level_strict_acc|↑  |0.8078|±  |0.0170|


|Groups|Version|Filter|n-shot| Metric |   |Value |   |Stderr|
|------|------:|------|-----:|--------|---|-----:|---|------|
|haerae|      1|none  |     0|acc     |↑  |0.6654|±  |0.0140|
|      |       |none  |     0|acc_norm|↑  |0.6654|±  |0.0140|
|kobest|      1|none  |     0|acc     |↑  |0.7768|±  |0.0057|
|      |       |none  |     0|acc_norm|↑  |0.5880|±  |0.0220|
|      |       |none  |     0|f1      |↑  |0.7764|±  |   N/A|


|            Groups             |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|-------------------------------|------:|------|-----:|-----------|---|-----:|---|-----:|
|kmmlu_direct                   |      2|none  |     0|exact_match|↑  |0.5212|±  |0.0026|
| - kmmlu_direct_applied_science|      2|none  |     0|exact_match|↑  |0.4997|±  |0.0046|
| - kmmlu_direct_humss          |      2|none  |     0|exact_match|↑  |0.5365|±  |0.0068|
| - kmmlu_direct_other          |      2|none  |     0|exact_match|↑  |0.5130|±  |0.0053|
| - kmmlu_direct_stem           |      2|none  |     0|exact_match|↑  |0.5455|±  |0.0048|


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "CarrotAI/Rabbit3-Ko-4B"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)
print("content:", content)
```

For deployment, you can use sglang>=0.4.6.post1 or vllm>=0.8.5 or to create an OpenAI-compatible API endpoint: