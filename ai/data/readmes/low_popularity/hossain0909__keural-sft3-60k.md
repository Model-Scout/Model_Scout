---
language:
  - ko
  - en
license: apache-2.0
library_name: transformers
tags:
  - mixtral
  - moe
  - korean
  - bilingual
  - causal-lm
  - sft
  - instruction-tuned
  - chat
base_model: mkd-hossain/keural-pretrained
pipeline_tag: text-generation
---

# Keural-SFT3-14.83B (SFT Epoch 3 — 60,000 steps)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch** — no base model was used.
This is an **intermediate SFT epoch 3 checkpoint** at step 60,000 out of 65,849 total steps (91.1% complete), trained on a 2.35M sample merged bilingual dataset.

## Model Details

| Property | Value |
|---|---|
| Architecture | Mixtral-style MoE (8 experts, top-2 routing) |
| Parameters | **14.83B total** / ~7.42B active per token |
| Layers | 24 |
| Hidden size | 4096 |
| Attention heads | 32 (GQA — 8 KV heads) |
| Head dim | 128 |
| Expert intermediate size | 5,632 |
| Experts | 8 total, top-2 per token |
| Context length | 4,096 tokens |
| Vocabulary | 131,074 (131,072 SPM + `<|im_start|>` + `<|im_end|>`) |
| RoPE theta | 500,000 |
| Sliding window | 512 (alternating layers) |
| Norm | RMSNorm (eps=1e-5) |
| Activation | SiLU |
| Dtype | bfloat16 |
| Languages | Korean (primary), English |

## Full Training Pipeline

| Stage | Steps | Tokens | Data | Hardware |
|---|---|---|---|---|
| Pretraining Stage 1 | 100,000 | ~50B | Korean + English web corpus | 2× H200 SXM |
| Pretraining Stage 2 | 120,000 | ~19B | Korean + English web corpus | 2× H200 SXM |
| SFT Epoch 1 | 18,000 | ~710M | 710K instruction samples (9 sources) | 2× H200 SXM |
| DPO Round 1 | 6,927 | — | 440K preference pairs (6 sources) | 2× H200 SXM |
| SFT Epoch 2 | 29,112 | ~7.6B | 710K filtered (math/code removed) | 2× H200 SXM |
| **SFT Epoch 3** | **60,000** | **~22B** | **2.35M samples (12 sources)** | **2× H200 SXM** |

## SFT Epoch 3 Dataset (2,351,212 samples)

| Source | Samples | Language |
|---|---|---|
| OpenHermes-2.5 | 1,001,551 | English |
| SlimOrca | 517,982 | English |
| UltraChat | 193,212 | English |
| OpenOrca | 138,639 | English |
| AIHub multisession sci | 127,868 | Korean |
| AIHub daily conversation | 120,867 | Korean |
| AIHub multisession social | 85,346 | Korean |
| Alpaca | 46,303 | English |
| KoInstruct QA | 45,299 | Korean |
| KoInstruct base | 42,276 | Korean |
| KoAlpaca | 21,091 | Korean |
| AIHub expert QA | 10,778 | Korean |
| **Total** | **2,351,212** | |

## Chat Format (ChatML)

```
<|im_start|>system
You are a helpful, accurate, and safe bilingual Korean-English AI assistant. Give concise, factual, and correct answers. If you are not sure about something, say you don't know instead of guessing. Never provide harmful, dangerous, illegal, or false information. Keep responses short and to the point unless the user asks for more detail.<|im_end|>
<|im_start|>user
Your question here<|im_end|>
<|im_start|>assistant
```

## Special Tokens

| Token | ID | Purpose |
|---|---|---|
| `<|im_start|>` | 131072 | Start of turn |
| `<|im_end|>` | 131073 | End of turn / stop token |

> **Important:** Always set `eos_token_id=131073`. Do NOT use ID 2.

## Usage (vLLM)

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-sft3-60k \
    --dtype auto \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.7
```

## Usage (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-sft3-60k"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)

messages = [
    {"role": "system", "content": "You are a helpful bilingual Korean-English AI assistant."},
    {"role": "user", "content": "안녕하세요! 서울에 대해 알려주세요."}
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
    do_sample=True,
    eos_token_id=131073,
)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Hardware

Trained on **2× NVIDIA H200 SXM** (139 GiB each) using FSDP FULL_SHARD, bfloat16 mixed precision, and gradient checkpointing.
