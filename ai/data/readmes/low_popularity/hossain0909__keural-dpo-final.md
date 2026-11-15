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
  - dpo
  - rlhf
  - instruction-tuned
  - chat
base_model: mkd-hossain/keural-sft-18k
pipeline_tag: text-generation
---

# Keural-DPO-14.83B (Final — 6927 steps, 1 full epoch)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch** — no base model was used.
This is the **final DPO (Direct Preference Optimization) checkpoint** at step 6,927, completing 1 full epoch of preference alignment from the Keural SFT-18k base.

> This is the most capable Keural checkpoint released to date. One full epoch of DPO alignment on 440K Korean+English preference pairs, producing consistently positive reward margins throughout training.

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
| SFT | 18,000 | 710M | mkd-chanwoo/keural-SFT (1.14M ChatML samples) | 2× H200 SXM |
| **DPO (this checkpoint)** | **6,927 (1 full epoch)** | — | keural-dpo-raw (440K preference pairs) | 2× H200 SXM |

### DPO Training Details

| Hyperparameter | Value |
|---|---|
| Algorithm | Direct Preference Optimization (DPO) |
| Learning rate | 2e-6 → 2e-7 cosine decay |
| Min learning rate | 2e-7 |
| Warmup steps | 100 |
| Beta (KL penalty) | 0.1 |
| Batch size per GPU | 2 |
| Gradient accumulation | 16 steps |
| Effective batch size | 64 (2 × 16 × 2 GPUs) |
| Max sequence length | 1,024 tokens |
| Optimizer | AdamW (β1=0.9, β2=0.95, ε=1e-8) |
| Weight decay | 0.1 |
| Gradient clipping | 1.0 |
| Total steps | 6,927 (1 full epoch) |
| Dataset size | 440,627 preference pairs |
| Parallelism | FSDP FULL_SHARD (ZeRO-3 equivalent) |
| Precision | bfloat16 + gradient checkpointing |
| Hardware | 2× NVIDIA H200 SXM (139 GiB each) |
| Speed | ~40 seconds/step |
| Final loss | ~0.6924 (stable) |
| Final margin | +0.0009–0.0018 (consistently positive) |
| Final GradNorm | 0.20–0.31 (clean) |

### DPO Dataset Sources

| Source | Samples | Language |
|---|---|---|
| hh_rlhf | 159,777 | English |
| aihub_71760 | 116,320 | Korean |
| multifaceted_collection_dpo | 63,399 | English |
| ultrafeedback_binarized | 59,122 | English |
| aihub_71748 | 29,676 | Korean |
| orca_dpo_paris_ko | 12,714 | Korean |
| **Total** | **440,627** | |

### SFT Hyperparameters (base checkpoint)

| Hyperparameter | Value |
|---|---|
| Learning rate | 1e-5 → 1e-6 cosine decay |
| Effective batch size | 64 (4 per GPU × 8 grad accum × 2 GPUs) |
| Max sequence length | 4,096 tokens |
| Weight decay | 0.05 |
| Steps | 18,000 |
| Dataset | mkd-chanwoo/keural-SFT (1.14M samples) |

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

model_id = "mkd-hossain/keural-dpo-final"

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
    --model mkd-hossain/keural-dpo-final \
    --tokenizer mkd-hossain/keural-dpo-final \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 1
```

Call the OpenAI-compatible endpoint:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="mkd-hossain/keural-dpo-final",
    messages=[
        {"role": "system", "content": "You are a helpful bilingual assistant. Respond in the same language as the user."},
        {"role": "user", "content": "What is the capital of South Korea?"},
    ],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### Multi-GPU serving

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-dpo-final \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 2
```

### Manual ChatML prompt

```python
prompt = (
    "<|im_start|>system\n"
    "You are a helpful bilingual Korean-English assistant. "
    "Always respond in the same language as the user.\n"
    "<|im_end|>\n"
    "<|im_start|>user\n"
    "Tell me about Seoul.<|im_end|>\n"
    "<|im_start|>assistant\n"
)
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
| mkd-hossain/keural-sft-18k | SFT | 18,000 | Instruction following, ChatML format |
| mkd-hossain/keural-dpo-3500 | DPO 50% | 3,500 | Early alignment |
| mkd-hossain/keural-dpo-5500 | DPO 79% | 5,500 | Late alignment |
| **mkd-hossain/keural-dpo-final** | **DPO 100%** | **6,927** | **Full epoch — best checkpoint** |

## Limitations

- Maximum context is 4,096 tokens.
- The pretraining corpus is Korean-dominant — always include a system prompt for correct bilingual behavior.
- Not safety-aligned — do not deploy in production without additional safety fine-tuning.
- This is an intermediate model in an ongoing training pipeline. Future releases will include SFT epoch 2 on filtered data and DPO round 2.

## License

Apache 2.0
