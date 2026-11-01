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
base_model: mkd-hossain/keural-pretrained
pipeline_tag: text-generation
---

# Keural-SFT-14.83B

Keural is a bilingual Korean–English Mixture-of-Experts language model trained from scratch.
This is the **SFT (Supervised Fine-Tuning) checkpoint** at step 18,000, fine-tuned from the Keural stage-2 pretrained base using the ChatML instruction format.

## Model Details

| Property | Value |
|---|---|
| Architecture | Mixtral-style MoE (8 experts, top-2) |
| Parameters | 14.83B total / ~7.42B active per token |
| Layers | 24 |
| Hidden size | 4096 |
| Attention heads | 32 (GQA — 8 KV heads) |
| Expert intermediate size | 5632 |
| Context length | 4096 tokens |
| Vocabulary | 131,074 (131,072 SPM + `<|im_start|>` + `<|im_end|>`) |
| RoPE theta | 500,000 |
| Sliding window | 512 (every other layer) |
| Dtype | bfloat16 |
| Languages | Korean, English |

## Training Pipeline

| Stage | Steps | Data |
|---|---|---|
| Pretraining Stage 1 | 100,000 | Korean + English web corpus |
| Pretraining Stage 2 | 20,000 | Korean + English web corpus (continued) |
| SFT (this checkpoint) | 18,000 | mkd-chanwoo/keural-SFT (1.14M ChatML samples) |

**SFT hyperparameters:** LR 1e-5 → 1e-6 cosine, batch 64 effective (4 × 8 accum × 2 GPUs), max_seq 4096, weight_decay 0.05, 2× H200 SXM with FSDP FULL_SHARD.

## Chat Format (ChatML)

This model uses **ChatML** format. You must use this exact format for good results.

```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
안녕하세요! 오늘 날씨가 어때요?<|im_end|>
<|im_start|>assistant
```

The model generates until it produces `<|im_end|>` (token ID 131073).

## How to Use

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-sft-18k"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful bilingual Korean-English assistant."},
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
    --model mkd-hossain/keural-sft-18k \
    --tokenizer mkd-hossain/keural-sft-18k \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 1
```

Then call the OpenAI-compatible endpoint:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="mkd-hossain/keural-sft-18k",
    messages=[
        {"role": "system", "content": "You are a helpful bilingual assistant."},
        {"role": "user",   "content": "한국의 수도는 어디인가요?"},
    ],
    max_tokens=512,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### With vLLM on multiple GPUs

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mkd-hossain/keural-sft-18k \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --tensor-parallel-size 2
```

### Manual ChatML prompt (without `apply_chat_template`)

```python
prompt = (
    "<|im_start|>system\n"
    "You are a helpful assistant.<|im_end|>\n"
    "<|im_start|>user\n"
    "Tell me about Seoul.<|im_end|>\n"
    "<|im_start|>assistant\n"
)
```

## Special Tokens

| Token | ID | Purpose |
|---|---|---|
| `<|im_start|>` | 131072 | Marks start of each turn |
| `<|im_end|>` | 131073 | Marks end of each turn / stop token |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | End of sequence |
| `<pad>` | 0 | Padding |

> **Important:** Always set `eos_token_id=131073` (`<|im_end|>`) when generating. If you use `eos_token_id=2` (`<eos>`), generation may not stop correctly.

## Recommended Generation Settings

```python
generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "repetition_penalty": 1.1,
    "do_sample": True,
    "eos_token_id": 131073,
}
```

For factual / deterministic tasks use `temperature=0.1, do_sample=False`.

## Limitations

- SFT training loss plateaued at ~1.96 (comparable models reach ~1.3–1.6). The model follows instructions but may produce repetitive or off-topic responses on complex prompts.
- The pretraining corpus contains Korean web data which skews the style toward informal language.
- Maximum context is 4096 tokens. Inputs longer than this will be truncated.
- This is an intermediate checkpoint — a DPO-aligned version will be released separately.

## License

Apache 2.0
