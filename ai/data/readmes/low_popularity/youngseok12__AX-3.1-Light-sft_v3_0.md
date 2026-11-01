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

# A.X-3.1-Light-sft_v3_0

`skt/A.X-3.1-Light`를 기반으로 AI Hub 한국어 데이터로 수행한 첫 번째
clean SFT baseline입니다. LoRA adapter를 base model에 병합한
standalone BF16 모델이므로 별도의 adapter나 custom Python code 없이
Transformers 및 표준 vLLM에서 로드할 수 있습니다.

이 모델은 연구 및 2026 K-DATA SCIENCE 해커톤의 로컬 검증을 위한
실험 산출물입니다. K-AI 리더보드의 공식 점수를 포함하지 않으며, 공개
benchmark 문항은 학습 데이터에 포함하지 않았습니다.

## Model Details

- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Architecture: `LlamaForCausalLM` (unchanged from the base model)
- Parameters: approximately 7B
- Weight format: BF16 `safetensors`
- Chat template: the official A.X chat template
- Custom code: none
- Merge method: PEFT LoRA `merge_and_unload`
- Base revision used for training and merge: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`

## Training Data

The SFT view contained 36,000 training examples and 3,000 validation
examples. Training and validation were kept separate at the source level.
The following AI Hub data domains were used:

- Civil law LLM pretraining and instruction-tuning data
- Criminal law LLM pretraining and instruction-tuning data
- Administrative law LLM pretraining and instruction-tuning data
- Corporate accounting standards data
- Essential medical knowledge data
- News article machine-reading data
- CoT-Fabric technology valuation data

Public evaluation benchmark data, including KMMLU-Pro, CLIcK, HLE,
SNU Ko-MuSR, Com2-main, and Original MuSR, was not used for SFT.

## Training Procedure

- Objective: standard assistant-token causal language-model cross entropy
- Epochs: 1
- Learning rate: `5e-5`
- Scheduler: cosine
- Warmup ratio: `0.03`
- Weight decay: `0.01`
- LoRA rank: `16`
- LoRA alpha: `32`
- LoRA dropout: `0.05`
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`
- Effective batch size: `32`
- Maximum sequence length: `2048`
- Precision: BF16
- Packing: disabled
- Random seed: `20260825`

The final training view used 800 reasoning examples. Their output tokens
accounted for approximately 24.37% of the total assistant target tokens.
The training format validator passed all 36,000 training and 3,000
validation examples.

## Usage with Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_v3_0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "대한민국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt",
).to(model.device)

with torch.inference_mode():
    outputs = model.generate(**inputs, max_new_tokens=64, do_sample=False)

print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## Usage with vLLM

```bash
vllm serve youngseok12/AX-3.1-Light-sft_v3_0 \
  --dtype bfloat16 \
  --max-model-len 32768
```

The repository is intended to be publicly accessible and directly loadable
by a standard vLLM OpenAI-compatible server. The model does not require
`trust_remote_code=True`.

## Intended Use and Limitations

This model is intended for Korean-language research, controlled evaluation,
and experimentation with instruction-following and domain-oriented SFT.
It is not a substitute for professional legal, accounting, or medical
advice. Responses may contain factual errors, unsupported reasoning, or
format deviations. The reported training configuration does not imply an
official K-AI leaderboard result.

The AI Hub source data remains subject to its original access terms and
licenses. This repository contains model weights and documentation, not the
source training datasets.

## License

The base model is distributed under the Apache License 2.0. Please review
the base model license and the terms applicable to the source training data
before using or redistributing this derivative model.

