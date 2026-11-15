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

# Keural-SFT3-14.83B (SFT Epoch 3 — 40,000 steps)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch** — no base model was used.
This is an **intermediate SFT epoch 3 checkpoint** at step 40,000 out of 65,849 total steps, trained on a 2.35M sample merged dataset.

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
| Pretraining Stage 2 | 120,000 | ~13B | Korean + English web corpus (continued) | 2× H200 SXM |
| SFT Epoch 1 | 18,000 | 710M | keural-SFT 1.14M ChatML samples | 2× H200 SXM |
| DPO Round 1 | 6,927 | — | 440K Korean preference pairs | 2× H200 SXM |
| SFT Epoch 2 | 29,112 | 7.63B | keural-SFT 710K samples (2nd pass) | 2× H200 SXM |
| **SFT Epoch 3 (this checkpoint)** | **40,000 / 65,849** | **~14B** | 2.35M merged ChatML dataset | 2× H200 SXM |

### SFT Epoch 3 Training Details

| Hyperparameter | Value |
|---|---|
| Resumed from | checkpoint_29112 (SFT epoch 2 final) |
| Learning rate | 1e-5 → 1e-6 cosine decay |
| Min learning rate | 1e-6 |
| Effective batch size | 64 (4 per GPU × 8 grad accum × 2 GPUs) |
| Max sequence length | 4,096 tokens |
| Weight decay | 0.05 |
| Gradient clipping | 1.0 |
| Optimizer | AdamW |
| Checkpoint step | 40,000 (60.7% of epoch) |
| Total epoch steps | 65,849 |
| Parallelism | FSDP FULL_SHARD (ZeRO-3 equivalent) |
| Precision | bfloat16 + gradient checkpointing |
| Hardware | 2× NVIDIA H200 SXM (139 GiB each) |

### SFT Epoch 3 Dataset (2,351,212 samples)

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
| **Total** | **2,351,212** | **Korean ~19% / English ~81%** |

## Chat Format (ChatML)

This model uses **ChatML** format with automatic system prompt injection.

```
<|im_start|>system
You are a helpful bilingual Korean-English assistant. Always respond in the same language as the user.<|im_end|>
<|im_start|>user
안녕하세요! 오늘 날씨가 어때요?<|im_end|>
<|im_start|>assistant
```

## How to Use

### With vLLM (recommended)

```bash
pip install vllm

python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-sft3-40k \
    --dtype auto \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.7
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="mkd-hossain/keural-sft3-40k",
    messages=[
        {"role": "system", "content": "You are a helpful bilingual Korean-English assistant. Always respond in the same language as the user."},
        {"role": "user", "content": "인공지능이란 무엇인가요?"},
    ],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-sft3-40k"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful bilingual Korean-English assistant. Always respond in the same language as the user."},
    {"role": "user", "content": "파이썬 리스트 정렬 방법을 알려주세요."},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True,
        eos_token_id=131073,
    )

response = tokenizer.decode(output[0][inputs.input_ids.shape[1]:], skip_special_tokens=False)
response = response.split("<|im_end|>")[0].strip()
print(response)
```

## Special Tokens

| Token | ID | Purpose |
|---|---|---|
| `<|im_start|>` | 131072 | Start of conversation turn |
| `<|im_end|>` | 131073 | End of turn / generation stop |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | End of sequence (not used for chat) |
| `<pad>` | 0 | Padding |

> **Always set `eos_token_id=131073`** when generating. Do not use ID 2.

## Checkpoint Comparison

| Checkpoint | Stage | Steps | Notes |
|---|---|---|---|
| mkd-hossain/keural-pretrained | Pretraining | 120,000 | Raw base model |
| mkd-hossain/keural-sft-18k | SFT Epoch 1 | 18,000 | Initial instruction tuning |
| mkd-hossain/keural-dpo-final | DPO Round 1 | 6,927 | Alignment on Korean preference data |
| mkd-hossain/keural-sft2 | SFT Epoch 2 | 29,112 | 2nd pass on 710K dataset |
| **mkd-hossain/keural-sft3-40k** | **SFT Epoch 3** | **40,000** | **Intermediate — 2.35M dataset** |

## Limitations

- Maximum context is 4,096 tokens.
- This is an **intermediate checkpoint** — epoch 3 is still running (40K/65,849 steps).
- Not safety-aligned — do not deploy in production without additional safety fine-tuning.
- English factual knowledge is limited due to pretraining data scale (63B tokens vs 15T for larger models).
- DPO round 2 planned after SFT epoch 3 completes to improve factual accuracy and reduce hallucination.

## License

Apache 2.0
