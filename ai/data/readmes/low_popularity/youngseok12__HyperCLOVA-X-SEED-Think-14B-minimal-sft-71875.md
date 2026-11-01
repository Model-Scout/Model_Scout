---
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
library_name: transformers
language:
- ko
license: other
license_name: hyperclovax-seed
license_link: LICENSE
pipeline_tag: text-generation
tags:
- korean
- hyperclovax
- sft
- lora-merged
- safetensors
- k-ai-leaderboard
---

# HyperCLOVA X SEED 14B Think — Minimal SFT (AI Hub 71875)

This repository contains a standalone BF16 model derived from
[`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B). A deliberately minimal
LoRA adapter was trained and merged into the base weights for a first real
leaderboard submission probe. The model name begins with **HyperCLOVA X** as
required by the base model license.

## Model details

- Base model: `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Architecture: `HyperCLOVAXForCausalLM`
- Weight format: BF16 `safetensors`, standalone merged full model
- Chat template: official HyperCLOVA X template, preserved byte-for-byte
- LoRA: rank `4`, alpha `8`, dropout `0`, target modules `q_proj`, `v_proj`
- Objective: assistant-token causal-language-model cross entropy
- Learning rate: `1e-6`, constant scheduler, no warmup or weight decay
- Training: 512 examples, 1 epoch, 32 optimizer steps, effective batch 16
- Maximum sequence length: `1024`; precision: BF16; seed: `42`
- Public benchmark data: not used

The run first evaluated 746 eligible private-training candidates and retained
512 rows for which the pristine base model produced an unambiguous correct
multiple-choice label. The source was the AI Hub dataset `71875`; use of that
data remains subject to the source dataset's terms. No benchmark questions,
answers, evaluation artifacts, logs, credentials, or `.env` files are included
in this repository.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype=torch.bfloat16, device_map="auto"
)
messages = [{"role": "user", "content": "대한민국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True, return_tensors="pt"
).to(model.device)
with torch.inference_mode():
    outputs = model.generate(**inputs, max_new_tokens=64, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## Intended use and limitations

This is an experimental Korean-language fine-tuned model for research and
controlled evaluation. It may produce factual or reasoning errors and is not a
substitute for professional legal, medical, financial, or other advice. The
HyperCLOVA X acceptable-use restrictions and all applicable laws continue to
apply to this derivative model.

## License and notices

The full HyperCLOVA X SEED 14B Think Model License Agreement is included in
`LICENSE`, and the required NAVER attribution is in `NOTICE`. Redistribution
must comply with that agreement, including its prohibited-use policy and
attribution requirements. AI Hub source-data terms also remain applicable.
