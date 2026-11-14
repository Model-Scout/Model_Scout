---
language:
- ko
license: apache-2.0
base_model: cooler8/yejin-korean-8b-v3-base
tags:
- korean
pipeline_tag: text-generation
---

# yejin-korean-8b-v3-cpt2s20000-distill-qwen36-mixK2-r128-nothink-v2

Korean instruction-following language model.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-cpt2s20000-distill-qwen36-mixK2-r128-nothink-v2", torch_dtype="bfloat16", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-cpt2s20000-distill-qwen36-mixK2-r128-nothink-v2")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training

Continuously pretrained from cooler8/yejin-korean-8b-v3-base (CPT-2 step 20,000, ~49B Korean tokens), chat-vector initialized with Qwen/Qwen3-8B (Apache-2.0), and LoRA fine-tuned (rank 128, alpha 256, lr 2e-4) on mixK2 (95,107 Korean instruction, knowledge, reading-comprehension, and multi-step reasoning samples) including sequence-level distillation from Qwen/Qwen3.6-27B-FP8 (Apache-2.0) with Answer-First + Explanation + Answer-Confirm formatting on knowledge/MRC tasks and CoT-First formatting on reasoning/math tasks. Verified 0 13-gram hits across 12 evaluation benchmarks.

## License

Apache 2.0
