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
base_model: mkd-hossain/keural-sft-18k
pipeline_tag: text-generation
---

# Keural-DPO-14.83B (checkpoint 3500)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch**.
This is the **DPO (Direct Preference Optimization) checkpoint** at step 3,500 (~50% of 1 epoch), aligned from the Keural SFT-18k base using human preference data.

> DPO alignment improves response quality, instruction-following, and reduces off-topic outputs compared to the SFT base.

## Model Details

| Property | Value |
|---|---|
| Architecture | Mixtral-style MoE (8 experts, top-2 routing) |
| Parameters | 14.83B total / ~7.42B active per token |
| Layers | 24 |
| Hidden size | 4096 |
| Attention heads | 32 (GQA — 8 KV heads) |
| Expert intermediate size | 5632 |
| Context length | 4096 tokens |
| Vocabulary | 131,074 (131,072 SPM + `<|im_start|>` + `<|im_end|>`) |
| RoPE theta | 500,000 |
| Sliding window | 512 (alternating every other layer) |
| Dtype | bfloat16 |
| Languages | Korean (primary), English |

## Full Training Pipeline

| Stage | Steps | Tokens | Data |
|---|---|---|---|
| Pretraining Stage 1 | 100,000 | ~50B | Korean + English web corpus |
| Pretraining Stage 2 | 120,000 | ~13B | Korean + English web corpus (continued) |
| SFT | 18,000 | 710M | mkd-chanwoo/keural-SFT (1.14M ChatML samples) |
| **DPO (this checkpoint)** | **3,500 / 6,927** | — | keural-dpo-raw (440K preference pairs) |

### DPO Hyperparameters

| Hyperparameter | Value |
|---|---|
| Learning rate | 2e-6 → 2e-7 cosine decay |
| Warmup steps | 100 |
| Beta (KL coefficient) | 0.1 |
| Effective batch size | 64 (2 per GPU × 16 grad accum × 2 GPUs) |
| Max sequence length | 1024 tokens |
| Optimizer | AdamW (β1=0.9, β2=0.95, ε=1e-8) |
| Weight decay | 0.1 |
| Max steps | 6,927 (1 epoch over 440K pairs) |
| Hardware | 2× NVIDIA H200 SXM (139 GiB each) |
| Parallelism | FSDP FULL_SHARD (ZeRO-3 equivalent) |
| Precision | bfloat16 + gradient checkpointing |

### SFT Hyperparameters (base checkpoint)

| Hyperparameter | Value |
|---|---|
| Learning rate | 1e-5 → 1e-6 cosine decay |
| Effective batch size | 64 (4 per GPU × 8 grad accum × 2 GPUs) |
| Max sequence length | 4096 tokens |
| Weight decay | 0.05 |
| Steps | 18,000 |

## Chat Format (ChatML)

This model uses **ChatML** format. You **must** use this exact format.

```
<|im_start|>system
You are a helpful bilingual Korean-English assistant.<|im_end|>
<|im_start|>user
안녕하세요! 오늘 날씨가 어때요?<|im_end|>
<|im_start|>assistant
```

The model generates until it produces `<|im_end|>` (token ID 131073).

> **Tip:** Always include a system prompt. The model responds in the same language as the user when instructed to do so.

## How to Use

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-dpo-3500"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful bilingual Korean-English assistant. Always respond in the same language as the user."},
    {"role": "user",   "content": "파이썬에서 리스트를 정렬하는 방법을 알려주세요."},
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
        no_repeat_ngram_size=8,
        do_sample=True,
        eos_token_id=131073,   # <|im_end|>
    )

response = tokenizer.decode(output[0][inputs.input_ids.shape[1]:], skip_special_tokens=False)
response = response.split("<|im_end|>")[0].strip()
print(response)
```

### With vLLM (recommended for serving)

```bash
pip install vllm

python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-dpo-3500 \
    --tokenizer mkd-hossain/keural-dpo-3500 \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 1
```

Then call the OpenAI-compatible endpoint:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="mkd-hossain/keural-dpo-3500",
    messages=[
        {"role": "system", "content": "You are a helpful bilingual assistant. Respond in the same language as the user."},
        {"role": "user",   "content": "한국의 수도는 어디인가요?"},
    ],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### Multi-GPU serving

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-dpo-3500 \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 2
```

### Manual ChatML prompt (without `apply_chat_template`)

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
| `<|im_start|>` | 131072 | Marks start of each turn |
| `<|im_end|>` | 131073 | Marks end of each turn / EOS for generation |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | End of sequence |
| `<pad>` | 0 | Padding |

> **Important:** Always set `eos_token_id=131073` (`<|im_end|>`) when generating. Do **not** use `eos_token_id=2`.

## Recommended Generation Settings

```python
generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "repetition_penalty": 1.1,
    "no_repeat_ngram_size": 8,
    "do_sample": True,
    "eos_token_id": 131073,
}
```

For factual / deterministic tasks:
```python
{"temperature": 0.1, "do_sample": False, "eos_token_id": 131073}
```

## DPO Dataset

Training used the `keural-dpo-raw` dataset — 440,627 chosen/rejected preference pairs in ChatML format covering:
- General conversation (Korean and English)
- Question answering
- Instruction following
- Knowledge tasks

## Limitations

- This is a **mid-training checkpoint** (step 3,500 of 6,927). A full-epoch checkpoint will be released when training completes.
- Maximum context is 4,096 tokens.
- The pretraining corpus is Korean-dominant. The model may default to Korean if no system prompt is provided.
- Always include a system prompt instructing the model to match the user's language for bilingual use.
- Not aligned for safety — do not deploy in production without additional safety fine-tuning.

## License

Apache 2.0
