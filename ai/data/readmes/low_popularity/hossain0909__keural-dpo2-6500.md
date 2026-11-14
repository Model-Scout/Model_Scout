---
language:
  - ko
  - en
license: apache-2.0
library_name: transformers
tags:
  - keural
  - moe
  - korean
  - bilingual
  - causal-lm
  - dpo
  - instruction-tuned
  - chat
  - preference-optimized
base_model: mkd-hossain/keural-sft3-final
pipeline_tag: text-generation
---

# Keural-DPO2-14.83B (DPO Round 2 — 6,500 steps)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch** by MKD Corp AI Research, Republic of Korea.
This is a **DPO Round 2 intermediate checkpoint** at step 6,500 out of 7,590 total steps (85.6% complete), trained on 485,793 preference pairs.

## Model Details

| Property | Value |
|---|---|
| Architecture | **KeuralMoECausalLM** |
| Parameters | **14.83B total** / ~7.42B active per token |
| Layers | 24 |
| Hidden size | 4,096 |
| Attention heads | 32 Q / 8 KV (GQA) |
| Head dimension | 128 |
| Experts | 8 total, top-2 per token |
| Expert intermediate size | 5,632 (SwiGLU) |
| Context length | 4,096 tokens |
| Vocabulary | **131,074** (131,072 SPM + `<\|im_start\|>` ID 131072 + `<\|im_end\|>` ID 131073) |
| RoPE theta | 500,000 |
| Sliding window | 512 tokens (even layers only) |
| Normalization | RMSNorm (eps=1e-5) |
| Dtype | bfloat16 |
| Languages | Korean (primary), English |

## Full Training Pipeline

| Stage | Steps | Tokens | Data | Hardware |
|---|---|---|---|---|
| Pretraining Stage 1 | 100,000 | ~50B | Korean + English web corpus | 2× H200 SXM |
| Pretraining Stage 2 | 120,000 | ~19B | Korean + English web corpus | 2× H200 SXM |
| SFT Epoch 1 | 18,000 | ~710M | 710K instruction samples (9 sources) | 2× H200 SXM |
| DPO Round 1 | 6,927 | — | 440K preference pairs (6 sources) | 2× H200 SXM |
| SFT Epoch 2 | 29,112 | ~7.6B | 710K filtered samples | 2× H200 SXM |
| SFT Epoch 3 | 65,849 | ~17.3B | 2.35M samples (12 sources) | 2× H200 SXM |
| **DPO Round 2** | **6,500** | — | **485K preference pairs (8 sources)** | **2× H200 SXM** |

## DPO Round 2 Dataset (485,793 pairs)

| Source | Pairs | Language |
|---|---|---|
| hh_rlhf | 150,510 | English |
| aihub_71760 | 109,289 | Korean |
| multifaceted_collection_dpo | 63,346 | English |
| ultrafeedback_binarized | 55,843 | English |
| ko_ultrafeedback_binarized | 54,169 | Korean |
| aihub_71748 | 29,356 | Korean |
| orca_dpo_pairs | 11,924 | English |
| orca_dpo_pairs_ko | 11,356 | Korean |
| **Total** | **485,793** | **58% EN / 42% KO** |

## Special Tokens

| Token | ID | Purpose |
|---|---|---|
| `<\|im_start\|>` | **131072** | Start of each conversation turn |
| `<\|im_end\|>` | **131073** | End of turn — **generation stop token** |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | Not used for chat |
| `<pad>` | 0 | Padding |

> **Critical:** Always use `eos_token_id=131073`. The model outputs `<|im_end|>` (ID 131073) to stop — not `<eos>` (ID 2).

## Chat Format (ChatML)

```
<|im_start|>system
You are a helpful, accurate, and safe bilingual Korean-English AI assistant. Give concise, factual, and correct answers. If you are not sure about something, say you don't know instead of guessing. Never provide harmful, dangerous, illegal, or false information.<|im_end|>
<|im_start|>user
Your question here<|im_end|>
<|im_start|>assistant
```

## Usage (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-dpo2-6500"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "system", "content": "You are a helpful bilingual Korean-English AI assistant."},
    {"role": "user",   "content": "안녕하세요! 서울에 대해 알려주세요."}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    repetition_penalty=1.1,
    do_sample=True,
    eos_token_id=131073,
)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Usage (vLLM)

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-dpo2-6500 \
    --dtype auto \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.7 \
    --trust-remote-code
```

## Hardware

Trained on **2× NVIDIA H200 SXM** (139 GiB each) using FSDP FULL_SHARD, bfloat16 mixed precision, and gradient checkpointing.

## Organization

Developed by **MKD Corp AI Research**, Republic of Korea.
