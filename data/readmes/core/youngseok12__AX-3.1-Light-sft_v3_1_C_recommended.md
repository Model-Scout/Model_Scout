---
base_model: skt/A.X-3.1-Light
library_name: transformers
language:
- ko
license: apache-2.0
pipeline_tag: text-generation
tags:
- korean
- sft
- lora-merged
- safetensors
- k-ai-leaderboard
---

# AX-3.1-Light-sft_v3_1_C_recommended

This is a standalone BF16 model obtained by fine-tuning
[`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light) with a LoRA
adapter and merging the adapter into the base weights. It is intended for
Korean-language research and controlled evaluation. The repository contains
no benchmark data, benchmark answers, training logs, or access credentials.

## Model Details

- Base model: `skt/A.X-3.1-Light`
- Base revision used for training and merge: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Architecture: unchanged from the base model
- Weight format: BF16 `safetensors`
- Chat template: official A.X tokenizer chat template
- Custom Python model code: none
- Submission form: merged full model; no separate adapter is required
- Experiment condition: Recommended mixture with a reduced reasoning-token contribution.

## Training Data

The training split contains 36,000 examples and the AI Hub validation-derived
development split contains 3,000 examples. Source-level train/dev separation
and exact-duplicate checks were retained. The source domains were:

- Civil law LLM instruction-tuning data
- Criminal law LLM instruction-tuning data
- Administrative law LLM instruction-tuning data
- Corporate accounting standards data
- Essential medical knowledge data
- News article machine-reading data
- CoT-Fabric technology valuation data

23,450 existing non-reasoning examples, 550 existing reasoning examples, and 12,000 additional AI Hub examples.
23.64% of assistant target tokens (550 reasoning examples).

Public evaluation benchmarks such as KMMLU-Pro, CLIcK, HLE, SNU Ko-MuSR,
Com2-main, and Original MuSR were not used as SFT data.

## Training Procedure

- Objective: standard assistant-token causal-language-model cross entropy
- Epochs: 1
- Learning rate: `3e-5`
- Scheduler: cosine with `0.03` warmup ratio
- Weight decay: `0.01`
- Maximum gradient norm: `1.0`
- LoRA: rank `16`, alpha `32`, dropout `0.05`
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`
- Effective batch size: `32`
- Maximum sequence length: `2048`
- Precision: BF16
- Packing: disabled
- Random seed: `20260827`

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_v3_1_C_recommended"
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

For an OpenAI-compatible deployment, the merged repository is intended to be
loadable directly by standard vLLM without an adapter or `trust_remote_code`.
Run the K-AI submission compatibility checks separately before submission.

## Intended Use and Limitations

This model is an experimental Korean SFT model for research and controlled
evaluation. It can produce factual errors and should not be used as a
substitute for professional legal, accounting, medical, or financial advice.
The AI Hub source data remains subject to its original access terms.

## License

The base model is distributed under the Apache License 2.0. The applicable
terms of the AI Hub source data remain in force for use of the training data.
See `LICENSE` for the base model license text.
