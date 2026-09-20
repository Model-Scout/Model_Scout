---
license: other
license_name: hyperclovax-seed
license_link: LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
base_model_revision: 9b74e35d4c7e4ffec489f4171273caca8948a2b9
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- hyperclovax
- sft
- lora-merged
- ties
- correct-only
- safetensors
---

# HyperCLOVA X SEED Think-14B Minimal-base Correct-only TIES

This repository contains a standalone BF16 model based on the Minimal SFT
merged model derived from [naver-hyperclovax/HyperCLOVAX-SEED-Think-14B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B).
Three fresh correct-only LoRA adapters were trained from that Minimal SFT model
and merged with TIES. The model is intended for controlled Korean-language
research and evaluation.

## Model details

- Training base: local Minimal SFT merged model, derived from `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Weight format: BF16 `safetensors`, standalone merged model
- LoRA: rank `4`, alpha `8`, dropout `0`, bias `none`
- Target modules: `q_proj`, `v_proj`
- Objective: assistant-only causal-language-model loss with a one-character answer-label target (`A/B/C/D`)
- Learning rate: `1e-6`; constant scheduler; warmup `0`; weight decay `0`
- Effective batch size: `16` (`per-device batch 1 × gradient accumulation 16`)
- Maximum sequence length: `1024`; precision: BF16; seed/data seed: `42`
- Adapter steps: 71875 `35`, 71568 `9`, 71949 `34`
- Merge: TIES, weights `[1, 1, 1]`, density `0.5`
- Official HyperCLOVA X chat template: preserved byte-for-byte

## Training data

The rows were selected from 1,000-row private-training probe pools using the
pristine HyperCLOVA base model's unambiguous correct judgments. The selected
rows were then converted to the Minimal SFT label-only schema before training
the three adapters on the Minimal SFT base. Public benchmark questions,
answers, and evaluation files were not used.

- [AI Hub 71875 — 필수의료 의학지식 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875): 557 correct rows
- [AI Hub 71568 — 경제·스포츠 숫자연산 MRC](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568): 131 correct rows
- [AI Hub 71949 — 인과관계 기반 추론 데이터(업사이클링) / label_json](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949): 535 correct rows

The AI Hub source-data terms remain applicable. This model card does not
redistribute the source datasets.

## Verification

The merged artifact passed an independent NaN/Inf scan over 421 floating-point
tensors and a deterministic generation smoke test. No downstream benchmark or
K-AI leaderboard score is claimed for this upload.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-base-correct-only-ties-r4min"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)
messages = [{"role": "user", "content": "대한민국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True, return_tensors="pt"
).to(model.device)
with torch.inference_mode():
    outputs = model.generate(**inputs, max_new_tokens=64, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## License and limitations

The base and derivative model are subject to NAVER's HyperCLOVA X SEED 14B
Think Model License Agreement. See `LICENSE` and `NOTICE`. This is an
experimental model and may produce factual or reasoning errors; it is not a
substitute for professional medical, legal, financial, or other advice.
