---
language:
  - ko
  - en
license: apache-2.0
tags:
  - mixtral
  - moe
  - korean
  - english
  - bilingual
  - pretrained
base_model: mkd-hossain/keural-14.8b-stage2-vllm
library_name: transformers
pipeline_tag: text-generation
---

# Keural 14.8B — Stage 2 (vLLM Ready)

Keural is a **14.83B parameter bilingual Korean-English Mixture-of-Experts language model** trained from scratch on Korean and English text. This repository contains the **Stage 2 annealing checkpoint** (120,000 steps total) in HuggingFace Mixtral-compatible safetensors format, ready to serve with vLLM or Transformers.

> **Note:** This is a **base pretrained model**, not an instruction-following or chat model. SFT (Supervised Fine-Tuning) training is planned as the next stage.

---

## Model Architecture

| Property | Value |
|---|---|
| Architecture | Mixtral MoE (MixtralForCausalLM) |
| Parameters | ~14.83B total (~2.9B active per token) |
| Layers | 24 |
| Hidden size | 4096 |
| Attention heads | 32 (GQA: 8 KV heads) |
| Experts | 8 total, top-2 active per token |
| FFN intermediate size | 5632 |
| Context length | 4096 tokens |
| Vocabulary | 131,072 |
| RoPE theta | 500,000 |
| Sliding window | 512 |
| Activation | SiLU |
| dtype | bfloat16 |

---

## Tokenizer

Custom SentencePiece tokenizer trained on Korean and English text.

| Token | String | ID |
|---|---|---|
| BOS | `<bos>` | 1 |
| EOS | `<eos>` | 2 |
| PAD | `<pad>` | 0 |
| UNK | `<unk>` | 3 |

---

## Training Details

### Stage 1 — Pretraining
- **Steps:** 100,000
- **Tokens:** ~43 billion
- **Data:** Korean and English web text (FineWeb, WanJuan, HPLT, etc.)
- **Batch size:** Large-scale FSDP distributed training
- **Hardware:** 2× NVIDIA H200 (150GB each)
- **Learning rate:** Cosine decay from 3e-4 to 3e-5

### Stage 2 — Annealing (Clean Data)
- **Steps:** 20,000 (steps 100K → 120K)
- **Tokens:** ~5.16 billion (clean subset)
- **Data:** High-quality filtered Korean and English text only
  - FineWeb-Edu (English)
  - FineWeb2 Korean
  - HPLT Korean
  - WanJuan Korean
- **Learning rate:** Cosine continued ~4.8e-5 → 3e-5
- **Purpose:** Improve output quality by annealing on clean data

---

## Usage

### vLLM (Recommended)

Install vLLM:
```bash
pip install vllm==0.9.2 --no-build-isolation
pip install "transformers==4.57.0"
```

Serve as OpenAI-compatible API:
```bash
vllm serve mkd-hossain/keural-14.8b-stage2-vllm \
  --dtype bfloat16 \
  --max-model-len 4096
```

Query the API:
```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="token")

response = client.completions.create(
    model="mkd-hossain/keural-14.8b-stage2-vllm",
    prompt="인공지능이란 무엇인가?",
    max_tokens=256,
    temperature=0.7,
)
print(response.choices[0].text)
```

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-14.8b-stage2-vllm"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

prompt = "인공지능이란 무엇인가?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        repetition_penalty=1.1,
        do_sample=True,
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Korean Example

```python
prompt = "한국의 역사에 대해 설명해 주세요."
```

### English Example

```python
prompt = "Explain the history of artificial intelligence."
```

---

## Limitations

- This is a **base pretrained model** — it continues text, it does not follow instructions or answer questions in a chat format.
- Context length is limited to **4096 tokens**.
- Outputs may be repetitive or incoherent for complex reasoning tasks — SFT and RLHF training will improve this significantly.
- Not aligned or safety-filtered. Use responsibly.

---

## Roadmap

- [x] Stage 1 Pretraining — 100K steps, ~43B tokens
- [x] Stage 2 Annealing — 20K steps, ~5.16B clean tokens
- [ ] SFT (Supervised Fine-Tuning) — instruction following
- [ ] RLHF / DPO alignment
- [ ] Keural Chat model release

---

## Citation

```bibtex
@misc{keural2026,
  title  = {Keural: A Bilingual Korean-English MoE Language Model},
  author = {MKD Hossain},
  year   = {2026},
  url    = {https://huggingface.co/mkd-hossain/keural-14.8b-stage2-vllm}
}
```

---

*Trained from scratch on KT Cloud NIPA2-H200 infrastructure using FSDP distributed training.*
