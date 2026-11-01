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

# HyperCLOVA X SEED Think-14B — AI Hub 71949 SFT 3K

This repository contains a standalone BF16 model derived from
[`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
One LoRA adapter was trained on 3,000 examples from AI Hub dataset 71949 and
merged into the pristine base weights.

## Model details

- Base model: `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Architecture: `HyperCLOVAXForCausalLM`
- Weight format: BF16 `safetensors`, standalone merged full model
- Chat template: official HyperCLOVA X template, preserved from the base
- LoRA: rank `16`, alpha `32`, dropout `0.05`, bias `none`
- Target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Objective: assistant-token-only causal-language-model cross entropy
- Learning rate: `5e-5`
- Scheduler: cosine, warmup ratio `0.03`, weight decay `0`
- Training: 3,000 examples, 1 epoch, effective batch size `16`
- Per-device batch: `4`; gradient accumulation: `4`
- Maximum sequence length: `4096`; precision: BF16; packing: `false`
- Seed: `42`; data seed: `42`
- Public benchmark data: not used

## Training data

The training data is AI Hub **71949 인과관계 기반 추론 데이터**. The source
material is image-grounded causal-reasoning MCQs; the prepared training rows
convert the underlying causal relation into a text-only 4-choice question with
a text answer, so no image input is required at train or inference time. The
exact prepared input contains 3,000 unique rows spread evenly across 10
causal-relation categories (성장, 가공, 절단, 오염, 작동, 추출, 파손, 정돈,
성과, 소모 — 300 rows each). Targets contain the correct choice marker and its
full text. The source file hash is
`5ff8588998f1cd4a17ddda6a21fe1f50ca519e9fad73fddd8b96a96322368f39`.

Dataset page: <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949>

No other AI Hub dataset, v0.21 mixture, public benchmark question, benchmark
answer, evaluation artifact, log, credential, or `.env` file is included in
this repository. AI Hub source-data terms remain applicable.

## Intended use and limitations

This is an experimental Korean-language fine-tuned model for research and
controlled evaluation. It can produce factual or reasoning errors and is not
a substitute for professional advice. The HyperCLOVA X acceptable-use
restrictions and all applicable laws continue to apply to this derivative
model.

## License and notices

The full HyperCLOVA X SEED 14B Think Model License Agreement is included in
`LICENSE`, and the required NAVER attribution is in `NOTICE`. Redistribution
must comply with that agreement and the AI Hub source-data terms.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "jwg0830/HyperCLOVA-X-SEED-Think-14B-sft-71949-3000"
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
