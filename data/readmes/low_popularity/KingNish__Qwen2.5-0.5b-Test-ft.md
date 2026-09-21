---
base_model:
- Qwen/Qwen2.5-0.5B-Instruct
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
license: apache-2.0
tags:
- text-generation-inference
- transformers
- unsloth
- qwen2
- trl
- sft
---

# Qwen 2.5 0.5B Model

## Model Description

This model is a compact yet powerful language model trained to answer a variety of questions with impressive quality. Despite its smaller size, it has demonstrated performance comparable to Llama 3.2 1B, and in some cases, it even outperforms it. This model was specifically trained on a 12,800 rows of the Magpie 300k Dataset.

## Performance

The Qwen 2.5 model has shown promising results in various tests, including the "strawberry test, Decimal Comparison test" where it successfully provided accurate answers. However, it is important to note that, like many models of its size, it may occasionally produce incorrect answers or flawed reasoning. Continuous improvements and full training are planned to enhance its performance further.

## How to Use

To use the Qwen 2.5 model, you can load it using the Hugging Face Transformers library. Here’s a simple example:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "KingNish/Qwen2.5-0.5b-Test-ft"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Which is greater 9.9 or 9.11 ??"
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(response)
```

## Future Work

I am actively working on improving the Qwen 2.5 model by training it on a larger dataset. 

# Uploaded  model

- **Developed by:** KingNish
- **License:** apache-2.0
- **Finetuned from model :** Qwen/Qwen2.5-0.5B-Instruct

This qwen2 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)