---
base_model: skt/A.X-3.1-Light
base_model_revision: 9b41bb2406472634d8812c0b8931fa40fa9a6c3a
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
- source-screening
- aihub
---

# A.X-3.1-Light source screening — AI Hub 71568

This repository contains a standalone BF16 model obtained by fine-tuning
`skt/A.X-3.1-Light` with LoRA SFT and merging the adapter into the pristine
base model. It is an experimental Korean-language source-only screening arm
for measuring the effect of the AI Hub 71568 economic and sports numerical
machine-reading data. The model is directly loadable with Transformers or
standard vLLM and does not require a separate adapter.

## Base model

- Hugging Face base model: `skt/A.X-3.1-Light`
- Base revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Architecture: `LlamaForCausalLM` (unchanged)
- Weight format: BF16 `safetensors`
- Submission form: merged full model

## Training data

Only the AI Hub dataset **71568, 숫자연산 기계독해 데이터** was used for SFT.
The training set contains exactly 3,000 TL examples: 1,500 경제 examples and
1,500 스포츠 examples. Five internal calculation/task strata were balanced at
300 examples each per category: 가산/감산, 비율연산, 양자/다자비교, 경계추출,
and 단서추출. Each selected article contributes at most one example, and no
exact duplicate, public benchmark row, v0.21 row, or other AI Hub source was
included. Targets use the common answer-first form `정답: <값>` without a
generated rationale.

## Training procedure

- Objective: assistant-token causal-language-model cross entropy
- Epochs: 1
- Optimizer steps: 375
- Learning rate: `5e-5`
- Scheduler: cosine, 3% warmup
- Weight decay: `0.01`
- LoRA: rank `16`, alpha `32`, dropout `0.05`, bias `none`
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Per-device batch size: `1`
- Gradient accumulation: `8` (effective batch size `8`)
- Maximum sequence length: `2048`
- Precision: BF16
- Packing: disabled
- Random seed and data seed: `42`
- Total supervised target tokens: `45,002`
- Mean / median supervised target tokens: `15.0007` / `7`
- Truncation: `0` (overlength rows were excluded rather than truncated)
- Final training loss: `0.2903463449`
- Internal AI Hub dev loss: `0.3073074222`

## Evaluation status

No public benchmark data was used for training, and no public benchmark score is
claimed for this repository. The local post-merge smoke test loaded the merged
model and generated `정답: 3` for a simple numeric question.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_source_screen_71568_3000"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
```

The model follows the base A.X chat template. Prompts used during SFT requested
an answer-first response beginning with `정답: `.

## Intended use and limitations

This is an experimental Korean SFT model for research and controlled
comparison. It can produce incorrect or unsupported answers and must not be
used as a substitute for professional advice.

## License

The base model and derived weights are distributed under the Apache License
2.0, subject to the original base-model terms. The applicable AI Hub dataset
terms remain in force for the training data.
