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
- ai-hub
---

# HyperCLOVA X SEED Think-14B — AI Hub 71875 Base-correct Minimal SFT

This repository contains a standalone BF16 model derived from
[naver-hyperclovax/HyperCLOVAX-SEED-Think-14B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
A deliberately minimal LoRA adapter was trained on the Base-correct pool from
AI Hub dataset 71875 and merged into the pristine base weights.

## Model details

- Base model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
- Base revision: 9b74e35d4c7e4ffec489f4171273caca8948a2b9
- Architecture: HyperCLOVAXForCausalLM
- Weight format: BF16 safetensors, standalone merged full model
- Chat template: official HyperCLOVA X template, preserved byte-for-byte
- LoRA: rank 4, alpha 8, dropout 0, bias none
- Target modules: q_proj, v_proj
- Objective: assistant-token-only causal-language-model cross entropy
- Learning rate: 1e-6; scheduler: constant; warmup: 0; weight decay: 0
- Training: 1,725 examples, 1 epoch, 108 optimizer steps, effective batch size 16
- Per-device batch: 1; gradient accumulation: 16
- Maximum sequence length: 1024; precision: BF16; packing: false
- Seed: 42; data seed: 42
- Public benchmark data: not used

## Training data

The training pool contains 1,725 rows selected from the 3,000-row AI Hub
71875 K_train source after a pristine Base label probe: the Base model produced
an unambiguous correct answer label on these rows. The pool contains 509
internal-medicine, 497 obstetrics-and-gynecology, 462 pediatrics, and 257
emergency-medicine rows. Uncertain rows (669) were excluded. Training targets
are the gold A–D answer labels; the Base model's output is not included as a
training target.

The source file SHA-256 is
ff13bf66d46102c773d28934239ec347117726c617df74b6443b0763991cfa60.
The source dataset is AI Hub 71875 필수의료 의학지식 QA:
https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875

No benchmark questions, answers, evaluation artifacts, logs, credentials, or
.env files are included in this repository. AI Hub source-data terms remain
applicable.

## Usage

~~~python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-sft-71875-correct-minimal"
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
~~~

## Intended use and limitations

This is an experimental Korean-language fine-tuned model for research and
controlled evaluation. It can produce factual or reasoning errors and is not a
substitute for professional medical, legal, financial, or other advice. The
HyperCLOVA X acceptable-use restrictions and all applicable laws continue to
apply to this derivative model.

## License and notices

The full HyperCLOVA X SEED 14B Think Model License Agreement is included in
LICENSE, and the required NAVER attribution is in NOTICE. Redistribution must
comply with that agreement, including its prohibited-use policy and
attribution requirements. AI Hub source-data terms also remain applicable.
