---
base_model: Qwen/Qwen2.5-0.5B-Instruct
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
datasets:
- KingNish/reasoning-base-20k
tags:
- text-generation-inference
- transformers
- unsloth
- qwen2
- trl
- sft
- reasoning
---


# Model Dexcription

It's First iteration of this model. For testing purpose its just trained on 10k rows.
It performed very well than expected. It do first reasoning and than generate response on based on it but it do like o1.
It do reasoning separately no special tokens or in response reasoning.
Below is inference code.
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

MAX_REASONING_TOKENS = 1024
MAX_RESPONSE_TOKENS = 512

model_name = "KingNish/Reasoning-0.5b"

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Which is greater 9.9 or 9.11 ??"
messages = [
    {"role": "user", "content": prompt}
]

# Generate reasoning
reasoning_template = tokenizer.apply_chat_template(messages, tokenize=False, add_reasoning_prompt=True)
reasoning_inputs = tokenizer(reasoning_template, return_tensors="pt").to(model.device)
reasoning_ids = model.generate(**reasoning_inputs, max_new_tokens=MAX_REASONING_TOKENS)
reasoning_output = tokenizer.decode(reasoning_ids[0, reasoning_inputs.input_ids.shape[1]:], skip_special_tokens=True)

# print("REASONING: " + reasoning_output)

# Generate answer
messages.append({"role": "reasoning", "content": reasoning_output})
response_template = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
response_inputs = tokenizer(response_template, return_tensors="pt").to(model.device)
response_ids = model.generate(**response_inputs, max_new_tokens=MAX_RESPONSE_TOKENS)
response_output = tokenizer.decode(response_ids[0, response_inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("ANSWER: " + response_output)
```

- **Trained by:** [Nishith Jain](https://huggingface.co/KingNish)
- **License:** apache-2.0
- **Finetuned from model :** [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
- **Dataset used :** [KingNish/reasoning-base-20k](https://huggingface.co/datasets/KingNish/reasoning-base-20k)


This qwen2 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)