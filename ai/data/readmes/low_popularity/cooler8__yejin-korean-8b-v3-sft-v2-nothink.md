---
language:
- ko
license: apache-2.0
tags:
- korean
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 SFT v2 (no-think)

Korean instruction-following language model.

Same weights as [cooler8/yejin-korean-8b-v3-sft-v2](https://huggingface.co/cooler8/yejin-korean-8b-v3-sft-v2).
Only the chat template differs: **thinking is disabled by default** (an empty `<think> </think>` block is
pre-filled after the assistant tag, so the model answers directly).
Pass `enable_thinking=True` to `apply_chat_template` to restore the original behavior.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>\n</s>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-sft-v2-nothink", torch_dtype="bfloat16", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-sft-v2-nothink")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))

# thinking 모드: tokenizer.apply_chat_template(..., enable_thinking=True)
```

## License

Apache 2.0
