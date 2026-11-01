---
language:
- en
- zh
- ja
- ko
- id
- ar
- ru
- de
- fr
- es
- pt
tags:
- text-generation
- causal-lm
- multilingual
- instruct
- chat
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
model_type: llama
---

# Athena-7B-Instruct

A multilingual instruction-tuned language model with 7.2B parameters, pre-trained on 2.5T tokens across 60+ languages.

## Architecture

- Parameters: 7.2B
- Layers: 32, Hidden: 4096, Attention heads: 32
- KV heads: 8 (GQA), Context: 8192
- Vocab: 128,256

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Mewingk/athena-7b-instruct",
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("Mewingk/athena-7b-instruct", trust_remote_code=True)

messages = [{"role": "user", "content": "Hello!"}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt")
outputs = model.generate(inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## License

Apache 2.0
