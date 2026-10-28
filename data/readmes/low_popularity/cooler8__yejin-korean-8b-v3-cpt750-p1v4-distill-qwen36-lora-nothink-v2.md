---
language:
- ko
license: apache-2.0
base_model: cooler8/yejin-korean-8b-v3-base
tags:
- korean
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 cpt750 + p1v4 + Qwen3.6-27B distill LoRA nothink-v2

Korean instruction-following language model.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-cpt750-p1v4-distill-qwen36-lora-nothink-v2", torch_dtype="bfloat16", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-cpt750-p1v4-distill-qwen36-lora-nothink-v2")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training

Built from Yejin 8B v3 (pretrained from scratch by Yejin: cooler8/yejin-korean-8b-v3-base): continued pretraining for 750 steps on public Korean data, Yejin chat vector from our own SFT model, then LoRA. The LoRA data mixes our phase-1 format data (45,013 samples) with 6052 short Korean solutions written by Qwen/Qwen3.6-27B (Apache-2.0) for questions from our own puzzle generator, KMMLU train and AI Hub school exams; only solutions that reached the known answer were kept (sequence-level distillation; no teacher weights or logits). No benchmark test items were used.

## License

Apache 2.0
