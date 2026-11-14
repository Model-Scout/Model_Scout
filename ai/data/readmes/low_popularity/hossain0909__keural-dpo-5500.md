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

# Keural-DPO-14.83B (checkpoint 5500)

Keural is a bilingual Korean–English Mixture-of-Experts language model trained **entirely from scratch** — no base model was used.
This is the **DPO (Direct Preference Optimization) checkpoint** at step 5,500 (~79% of 1 epoch), aligned from the Keural SFT-18k base using human preference data.

> This checkpoint is more mature than the 3500-step release. At step 5500 the model has seen ~80% of the full preference dataset, producing noticeably better instruction-following and more consistent language matching compared to the SFT base.

## Model Details

| Property | Value |
|---|---|
| Architecture | Mixtral-style MoE (8 experts, top-2 routing) |
| Parameters | **14.83B total** / ~7.42B active per token |
| Layers | 24 |
| Hidden size | 4096 |
| Attention heads | 32 (GQA — 8 KV heads) |
| KV heads | 8 |
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
| **DPO (this checkpoint)** | **5,500 / 6,927** | — | keural-dpo-raw (440K preference pairs) | 2× H200 SXM |

### DPO Training Details

| Hyperparameter | Value |
|---|---|
| Algorithm | Direct Preference Optimization (DPO) |
| Learning rate | 2e-6 → 2e-7 cosine decay |
| Min learning rate | 2e-7 |
| LR at step 5500 | ~3.87e-7 |
| Warmup steps | 100 |
| Beta (KL penalty) | 0.1 |
| Batch size per GPU | 2 |
| Gradient accumulation | 16 steps |
| Effective batch size | 64 (2 × 16 × 2 GPUs) |
| Max sequence length | 1,024 tokens |
| Optimizer | AdamW (β1=0.9, β2=0.95, ε=1e-8) |
| Weight decay | 0.1 |
| Gradient clipping | 1.0 |
| Total steps (1 epoch) | 6,927 |
| Dataset size | 440,627 preference pairs |
| Parallelism | FSDP FULL_SHARD (ZeRO-3 equivalent) |
| Precision | bfloat16 + gradient checkpointing |
| Hardware | 2× NVIDIA H200 SXM (139 GiB each) |
| Speed | ~40 seconds/step |

**DPO loss at step 5500:** ~0.6924 (stable)
**Margin at step 5500:** +0.0009 to +0.0018 (consistently positive — model reliably prefers chosen responses)
**GradNorm:** 0.20–0.31 (clean, no explosion)

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

This model uses **ChatML** format. You **must** use this exact format for good results.

```
<|im_start|>system
You are a helpful bilingual Korean-English assistant. Always respond in the same language as the user.<|im_end|>
<|im_start|>user
안녕하세요! 오늘 날씨가 어때요?<|im_end|>
<|im_start|>assistant
```

The model generates until it produces `<|im_end|>` (token ID 131073).

> **Important:** Always include a system prompt. Without it, the model may default to Korean regardless of input language.

## How to Use

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-dpo-5500"

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
            "Always respond in the same language as the user's message. "
            "If the user writes in English, respond in English. "
            "If the user writes in Korean, respond in Korean."
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
    --model mkd-hossain/keural-dpo-5500 \
    --tokenizer mkd-hossain/keural-dpo-5500 \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 1
```

Call the OpenAI-compatible endpoint:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="mkd-hossain/keural-dpo-5500",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful bilingual assistant. Respond in the same language as the user."
        },
        {"role": "user", "content": "What is the capital of South Korea?"},
    ],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### Multi-GPU serving (2× GPU)

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-dpo-5500 \
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
| `<|im_start|>` | 131072 | Marks the start of each conversation turn |
| `<|im_end|>` | 131073 | Marks the end of each turn / generation stop token |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | End of sequence |
| `<pad>` | 0 | Padding token |

> **Critical:** Always set `eos_token_id=131073` (`<|im_end|>`) when generating. Using `eos_token_id=2` will cause generation to not stop correctly.

## Recommended Generation Settings

```python
# For conversational / creative tasks
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

# For factual / deterministic tasks
generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.1,
    "repetition_penalty": 1.1,
    "no_repeat_ngram_size": 8,
    "do_sample": False,
    "eos_token_id": 131073,
}
```

## DPO Dataset

Training used the `keural-dpo-raw` dataset — 440,627 chosen/rejected preference pairs in ChatML format, covering:
- General conversation (Korean and English)
- Question answering
- Instruction following
- Knowledge and reasoning tasks

## Comparison to Previous Checkpoints

| Checkpoint | Stage | Key Difference |
|---|---|---|
| mkd-hossain/keural-pretrained | Pretraining (120k steps) | Raw base model, no instruction tuning |
| mkd-hossain/keural-sft-18k | SFT (18k steps) | Instruction following, ChatML format |
| mkd-hossain/keural-dpo-3500 | DPO 50% | Early alignment, margins emerging |
| **mkd-hossain/keural-dpo-5500** | **DPO 79%** | **Stronger alignment, consistent margins** |

## Limitations

- This is a **late-training checkpoint** (step 5,500 of 6,927 — 79% of 1 epoch). A full-epoch checkpoint will be released when training completes.
- Maximum context is 4,096 tokens. Inputs longer than this will be truncated.
- The pretraining corpus is Korean-dominant. Always include a system prompt for correct bilingual behavior.
- Not safety-aligned — do not deploy in production without additional safety fine-tuning.
- DPO margins are small (0.001–0.002) due to the large model size and low LR — this is normal for 14B+ models.

## License

Apache 2.0
