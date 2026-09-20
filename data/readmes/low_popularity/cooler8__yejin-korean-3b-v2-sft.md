---
language:
- ko
license: apache-2.0
tags:
- korean
- sft
- causal-lm
- fsdp
pipeline_tag: text-generation
---

# Yejin Korean 3B v2 SFT

Supervised fine-tuned version of the Yejin Korean 3B v2 base model.

## Model Description

This model is a 3-billion parameter Korean language model that has been
supervised fine-tuned on high-quality instruction-following datasets.

- **Base model**: Yejin Korean 3B v2
- **Architecture**: Transformer decoder-only
- **Parameters**: ~3B (3072d / 28L / 24H / 8KV)
- **Vocabulary**: 64,000 tokens (custom Korean tokenizer)
- **Max sequence length**: 4,096 tokens
- **Precision**: bfloat16

## Training Details

- **Method**: Full parameter fine-tuning (no LoRA/adapters)
- **Distributed**: FSDP across 8x NVIDIA H200 GPUs
- **Epochs**: 3
- **Learning rate**: 2e-5 (cosine schedule)
- **Batch size**: 128 (2 per GPU x 8 GPUs x 8 gradient accumulation)
- **Weight decay**: 0.01
- **Warmup**: 3% of total steps

## Training Data

Fine-tuned on curated Korean instruction-following datasets:

- Synthetic and instruction data
- Multi-turn conversation data
- Post-training data
- Knowledge-grounded QA data
- Agent/tool-use data
- Reading comprehension data

## Chat Template

```
<s><|user|>
{instruction}<|end|>
<|assistant|>
{response}<|end|>
</s>
```

For multi-turn conversations:
```
<s><|user|>
{user_msg_1}<|end|>
<|assistant|>
{assistant_msg_1}<|end|>
<|user|>
{user_msg_2}<|end|>
<|assistant|>
{assistant_msg_2}<|end|>
</s>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-3b-v2-sft")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-3b-v2-sft")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=False))
```

## License

Apache 2.0
