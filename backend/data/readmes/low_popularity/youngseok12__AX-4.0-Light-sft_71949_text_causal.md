---
base_model: skt/A.X-4.0-Light
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
- causal-reasoning
- k-ai-leaderboard
---

# A.X-4.0-Light SFT — 71949 Text Causal

This repository contains a standalone BF16 full-weight model derived from
[`skt/A.X-4.0-Light`](https://huggingface.co/skt/A.X-4.0-Light). A LoRA
adapter was trained on a carefully filtered, text-only subset of AI Hub
Dataset 71949 (causal reasoning) and then merged into the base weights. The
model is intended for Korean-language research and controlled benchmark
experiments. It can produce factual or reasoning errors and is not a
substitute for professional advice.

## Model details

- Base model: `skt/A.X-4.0-Light`
- Architecture: Qwen2-family causal language model (base architecture unchanged)
- Weight format: BF16 `safetensors`, standalone merged full model
- LoRA: rank `16`, alpha `32`, dropout `0.05`; targets `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Objective: assistant-token causal-language-model cross entropy; system and user tokens masked
- Training: 478 train examples, 50 held-out development examples, 2 epochs
- Optimizer settings: learning rate `5e-5`, linear scheduler, no warmup, weight decay `0`
- Sequence length: `2048`; per-device batch `1`; gradient accumulation `8`; effective batch `8`
- Precision: BF16; packing disabled; seed `20260901`
- Chat template: official A.X tokenizer template preserved in `chat_template.jinja`
- Submission form: merged full model; no separate adapter or custom Python model code is required

## Training data

The only training source was [AI Hub Dataset 71949 — Causal Reasoning](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949). The source contains image-grounded labels, so image files were not downloaded or used. Records whose question or answer required an image/photo/drawing were excluded. Evidence-only visual wording was normalized to text, the third conclusion step was omitted to reduce answer leakage, and exact questions were deduplicated.

From 16,000 source labels, 530 candidates were obtained and reduced to 528 unique question/source records. The final split contains 478 training and 50 development records. No public benchmark questions, answers, evaluation files, credentials, or `.env` files are included in this repository. Use of the AI Hub source remains subject to its original terms.

## Local evaluation

The canonical local suite was run with deterministic `free` and `B1_constrained` probes. The following are B1 parsed-accuracy results, not official K-AI leaderboard scores:

| Benchmark | Parsed accuracy |
|---|---:|
| KMMLU-Pro | 47.27% |
| CLIcK | 67.37% |
| HLE text-only | 3.75% |
| SNU Ko-MuSR | 48.93% |
| Com2-main | 50.60% |
| Original MuSR (supplementary) | 55.56% |

The five-axis local mean (KMMLU-Pro, CLIcK, HLE text-only, SNU Ko-MuSR,
and Com2-main) is 43.59%. The full run produced zero generation errors.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "jwg0830/AX-4.0-Light-sft_71949_text_causal"
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

The merged repository is designed to load with standard Transformers or vLLM
without `trust_remote_code` and without attaching a separate adapter.

## License and limitations

The base model and the merged model files are distributed under the Apache
License 2.0 as provided by SK Telecom; see `LICENSE`. The AI Hub source-data
terms continue to apply. This is an experimental model for research and
controlled evaluation, not a medical, legal, financial, or other professional
advice system.
