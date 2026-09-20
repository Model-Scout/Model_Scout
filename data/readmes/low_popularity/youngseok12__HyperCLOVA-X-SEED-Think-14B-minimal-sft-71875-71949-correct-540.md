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
- aihub
- correct-only
- lora-merge
- safetensors
---

# HyperCLOVA X SEED Think-14B Minimal SFT + 71949 Correct 540

This repository contains a standalone BF16 model created by continuing the
Minimal SFT model
[`youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875`](https://huggingface.co/youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875)
with a small correct-only LoRA on AI Hub 71949 data.

The direct starting checkpoint was the locally verified merged Minimal SFT
model. Its original foundation is
`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`, revision
`9b74e35d4c7e4ffec489f4171273caca8948a2b9`.

## Data

- AI Hub dataset 71949: <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949>
- Stratified private-training probe pool: 1,000 rows
- Correct-only rows used for training: **540**
- Excluded: 166 wrong and 294 uncertain rows
- Target format: one correct choice letter, `A/B/C/D`
- No duplication or resampling
- Public benchmark questions, answers, and evaluation artifacts were not used
- Correct-pool input SHA-256: `29791fa19d412d3c48d7080381079ab3ccf3190059a5ba04e94be37f479feef8`

## Training

The same low-impact Minimal SFT recipe was used:

- LoRA rank `4`, alpha `8`, dropout `0`
- Target modules: `q_proj`, `v_proj`
- Learning rate `1e-6`, constant scheduler, no warmup, weight decay `0`
- BF16, maximum sequence length `1024`
- Per-device batch `1`, gradient accumulation `16`
- Assistant-only loss, packing disabled
- One epoch, `34` optimizer steps
- Seed and data seed: `42`

The final train loss was `3.9535395538`. The adapter was merged into the
Minimal SFT checkpoint using BF16 safetensors.

## Validation

- Adapter tensors: 152; NaN/Inf: 0
- Merged model: 6 safetensors shards, 421 tensors; NaN/Inf: 0
- Generation smoke: 2/2 passed
- Local canonical benchmark and official K-AI leaderboard score: not measured

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875-71949-correct-540"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```

## License and limitations

This derivative model is subject to the HyperCLOVA X SEED 14B Think Model
License Agreement in `LICENSE`, with the required attribution in `NOTICE`.
AI Hub source-data terms also apply. This is an experimental research and
evaluation model; outputs may be incorrect and it is not a substitute for
professional medical, legal, financial, or other advice.
