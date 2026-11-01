---
language:
- ko
license: apache-2.0
tags:
- korean
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 SFT

Korean instruction-following language model.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n{response}<|end|>\n</s>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-sft")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-sft")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## License

Apache 2.0
