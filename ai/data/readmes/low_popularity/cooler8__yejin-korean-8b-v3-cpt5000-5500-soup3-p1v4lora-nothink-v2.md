---
language:
- ko
license: apache-2.0
base_model: cooler8/yejin-korean-8b-v3-base
tags:
- korean
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 cpt5000-5500 soup3 p1v4lora nothink-v2

Korean instruction-following language model.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-cpt5000-5500-soup3-p1v4lora-nothink-v2", torch_dtype="bfloat16", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-cpt5000-5500-soup3-p1v4lora-nothink-v2")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training

Uniform weight average (model soup) of three Yejin fine-tunes: continued-pretraining checkpoints 5,000, 5,250 and 5,500 of Yejin 8B v3 (pretrained from scratch by Yejin: cooler8/yejin-korean-8b-v3-base), each with the Yejin chat vector from our own SFT model and our phase-1 format LoRA. No teacher-distilled data and no benchmark test items were used.

## License

Apache 2.0
