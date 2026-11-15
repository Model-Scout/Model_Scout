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

# Keural-SFT2-14.83B (SFT Epoch 2 — 29,112 steps)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch** — no base model was used.
This is the **SFT epoch 2 checkpoint** at step 29,112, continuing supervised fine-tuning from the epoch 1 checkpoint (18,000 steps) on the same 710K ChatML dataset.

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
| Sliding window | 512 (alternating every other layer) |
| Norm | RMSNorm (eps=1e-5) |
| Activation | SiLU |
| Dtype | bfloat16 |
| Languages | Korean (primary), English |

## Full Training Pipeline

| Stage | Steps | Tokens | Data | Hardware |
|---|---|---|---|---|
| Pretraining Stage 1 | 100,000 | ~50B | Korean + English web corpus | 2× H200 SXM |
| Pretraining Stage 2 | 120,000 | ~13B | Korean + English web corpus (continued) | 2× H200 SXM |
| SFT Epoch 1 | 18,000 | 710M | mkd-chanwoo/keural-SFT (1.14M ChatML samples) | 2× H200 SXM |
| DPO (1 full epoch) | 6,927 | — | keural-dpo-raw (440K preference pairs) | 2× H200 SXM |
| **SFT Epoch 2 (this checkpoint)** | **29,112** | **7.63B** | mkd-chanwoo/keural-SFT (710K ChatML samples, 2nd pass) | 2× H200 SXM |

### SFT Epoch 2 Training Details

| Hyperparameter | Value |
|---|---|
| Resumed from | checkpoint_18000 (SFT epoch 1 final) |
| Learning rate | 1e-5 → 1e-6 cosine decay |
| Min learning rate | 1e-6 |
| Effective batch size | 64 (4 per GPU × 8 grad accum × 2 GPUs) |
| Max sequence length | 4,096 tokens |
| Weight decay | 0.05 |
| Gradient clipping | 1.0 |
| Optimizer | AdamW |
| Total steps | 29,112 |
| Dataset | mkd-chanwoo/keural-SFT (710K samples) |
| Total tokens | ~7.63B |
| Training time | ~56.71h |
| Parallelism | FSDP FULL_SHARD (ZeRO-3 equivalent) |
| Precision | bfloat16 + gradient checkpointing |
| Hardware | 2× NVIDIA H200 SXM (139 GiB each) |

### SFT Dataset

| Source | Samples | Language |
|---|---|---|
| mkd-chanwoo/keural-SFT | 710,000 | Korean + English |

## Chat Format (ChatML)

This model uses **ChatML** format. Always include a system prompt for best results.

```
<|im_start|>system
You are a helpful bilingual Korean-English assistant. Always respond in the same language as the user.<|im_end|>
<|im_start|>user
안녕하세요! 오늘 날씨가 어때요?<|im_end|>
<|im_start|>assistant
```

The model generates until it produces `<|im_end|>` (token ID 131073).

> The chat template in `tokenizer_config.json` **automatically injects a default system prompt** if you don't provide one, so bilingual behavior works out of the box with `apply_chat_template`.

## How to Use

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-sft2"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful bilingual Korean-English assistant. "
            "Always respond in the same language as the user's message."
        )
    },
    {"role": "user", "content": "파이썬에서 리스트를 정렬하는 방법을 알려주세요."},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        repetition_penalty=1.1,
        no_repeat_ngram_size=8,
        do_sample=True,
        eos_token_id=131073,
    )

response = tokenizer.decode(output[0][inputs.input_ids.shape[1]:], skip_special_tokens=False)
response = response.split("<|im_end|>")[0].strip()
print(response)
```

### With vLLM (recommended for serving)

```bash
pip install vllm

python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-sft2 \
    --tokenizer mkd-hossain/keural-sft2 \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 1
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="mkd-hossain/keural-sft2",
    messages=[
        {"role": "system", "content": "You are a helpful bilingual assistant. Respond in the same language as the user."},
        {"role": "user", "content": "What is the capital of South Korea?"},
    ],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

## Special Tokens

| Token | ID | Purpose |
|---|---|---|
| `<|im_start|>` | 131072 | Marks the start of each conversation turn |
| `<|im_end|>` | 131073 | Marks end of turn / generation stop token |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | End of sequence (not used for chat) |
| `<pad>` | 0 | Padding token |

> **Critical:** Always set `eos_token_id=131073` when generating. Do **not** use `eos_token_id=2`.

## Recommended Generation Settings

```python
# Conversational / creative
{
    "max_new_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "repetition_penalty": 1.1,
    "no_repeat_ngram_size": 8,
    "do_sample": True,
    "eos_token_id": 131073,
}

# Factual / deterministic
{
    "max_new_tokens": 512,
    "temperature": 0.1,
    "repetition_penalty": 1.1,
    "do_sample": False,
    "eos_token_id": 131073,
}
```

## Checkpoint Comparison

| Checkpoint | Stage | Steps | Notes |
|---|---|---|---|
| mkd-hossain/keural-pretrained | Pretraining | 120,000 | Raw base, no instruction tuning |
| mkd-hossain/keural-sft-18k | SFT Epoch 1 | 18,000 | Instruction following, ChatML format |
| mkd-hossain/keural-dpo-3500 | DPO 50% | 3,500 | Early alignment |
| mkd-hossain/keural-dpo-5500 | DPO 79% | 5,500 | Late alignment |
| mkd-hossain/keural-dpo-final | DPO 100% | 6,927 | Full epoch DPO |
| **mkd-hossain/keural-sft2** | **SFT Epoch 2** | **29,112** | **Continued SFT on 710K dataset** |

## Limitations

- Maximum context is 4,096 tokens.
- The pretraining corpus is Korean-dominant — always include a system prompt for correct bilingual behavior.
- Not safety-aligned — do not deploy in production without additional safety fine-tuning.
- This is an intermediate checkpoint. SFT epoch 3 on a 2.35M sample merged dataset is in progress.

## License

Apache 2.0
