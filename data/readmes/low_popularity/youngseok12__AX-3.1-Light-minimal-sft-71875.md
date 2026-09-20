---
base_model: skt/A.X-3.1-Light
library_name: transformers
language:
- ko
license: apache-2.0
license_link: https://huggingface.co/skt/A.X-3.1-Light/blob/main/LICENSE
pipeline_tag: text-generation
tags:
- korean
- a.x
- sft
- lora-merged
- safetensors
- k-ai-leaderboard
---

# A.X-3.1-Light — Minimal Self-Distillation SFT (AI Hub 71875)

This repository contains a standalone BF16 model derived from
[`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light). It reproduces —
on a different base model — the same minimal self-distillation recipe used by
our best-performing HyperCLOVA X SEED Think-14B submission, to test whether the
recipe's real-leaderboard result transfers across base models.

## Model details

- Base model: `skt/A.X-3.1-Light`
- Base revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Architecture: `LlamaForCausalLM`
- Weight format: BF16 `safetensors`, standalone merged full model
- Chat template: official A.X-3.1-Light template, preserved byte-for-byte
- LoRA: rank `4`, alpha `8`, dropout `0`, target modules `q_proj`, `v_proj`
- Objective: assistant-token causal-language-model cross entropy (label-only)
- Learning rate: `1e-6`, constant scheduler, no warmup or weight decay
- Training: 512 examples, 1 epoch, 32 optimizer steps, effective batch 16
- Maximum sequence length: `1024`; precision: BF16; seed: `42`
- Public benchmark data: not used

## Data

The pristine base model was run against a 950-item eligible pool of AI Hub
[71875 필수의료 (essential medical) QA](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875)
training rows with an auditable single-choice gold label. 539 of 950 items
(56.7%) produced an unambiguous free-form answer that matched the AI Hub gold
label; the first 512 of those (round-robin across domains, seed 42) were kept.
Each training target is the base model's own generated output for that item
(self-distillation), not a human-authored label. No benchmark questions,
answers, evaluation artifacts, logs, credentials, or `.env` files are included
in this repository.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-minimal-sft-71875"
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
A.X acceptable-use restrictions and all applicable laws continue to apply to
this derivative model.

## License and notices

The `A.X-3.1-Light` model, and this derivative, are licensed under the Apache
License, Version 2.0; the full text is included in `LICENSE`. AI Hub
source-data terms also remain applicable.
