---
language:
- ko
license: apache-2.0
base_model: cooler8/yejin-korean-8b-v3-base
tags:
- korean
pipeline_tag: text-generation
---

# yejin-korean-8b-v3-cpt2s20000-distill-qwen36-mixK4x3-K2x1-r128-nothink-v2

Korean instruction-following language model.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-cpt2s20000-distill-qwen36-mixK4x3-K2x1-r128-nothink-v2", torch_dtype="bfloat16", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-cpt2s20000-distill-qwen36-mixK4x3-K2x1-r128-nothink-v2")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training

Fine-tuned from `cooler8/yejin-korean-8b-v3-base` (after 20,000 steps of Stage-2 continual pre-training on Korean text) using LoRA (`r=128, alpha=256`) on the 13-gram-decontaminated Stage-K4 Korean knowledge, multi-step narrative reasoning, and complex causal commonsense reasoning (`Com2`) instruction mixture (`0` 13-gram overlap across all 13 evaluation benchmarks). Sequence-level reasoning explanations were generated with `Qwen/Qwen3.6-27B` (Apache-2.0) with answer verification.

## License

Apache 2.0
