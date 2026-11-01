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
  - sft
  - instruction-tuning
base_model: mkd-hossain/keural-14.8b-stage2-vllm
library_name: transformers
pipeline_tag: text-generation
---

# Keural 14.8B — SFT (Instruction Tuned)

Keural is a **14.83B parameter bilingual Korean-English Mixture-of-Experts language model** trained from scratch. This repository contains an **early SFT checkpoint (7,000 steps)** fine-tuned on the `mkd-chanwoo/keural-SFT` dataset in HuggingFace Mixtral-compatible safetensors format.

> **Note:** This is an **early SFT checkpoint** (7,000 / 18,000 steps). Full SFT training is still in progress. Final SFT and DPO-aligned chat model will be released as `mkd-hossain/keural-14.8b-chat`.

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
| Vocabulary | 131,072 + 2 special tokens (131,074) |
| RoPE theta | 500,000 |
| dtype | bfloat16 |

---

## Training History

| Stage | Steps | Tokens | Details |
|---|---|---|---|
| Pretraining | 100,000 | ~64.56B | Korean + English web text |
| Annealing | 20,000 | ~5.16B | High-quality filtered data |
| SFT (this checkpoint) | 7,000 | ~450M | ChatML instruction tuning |

---

## SFT Dataset

Trained on `mkd-chanwoo/keural-SFT`:
- **1,134,119 samples** across 14 curated sources
- **~710M tokens** total
- **Korean 44% / English 56%**
- Sources: UltraChat, OpenOrca, KoAlpaca, MathInstruct, AIHub, GSM8K, Magicoder, and more
- Format: ChatML (`<|im_start|>` / `<|im_end|>`)

---

## Tokenizer

| Token | String | ID |
|---|---|---|
| BOS | `<bos>` | 1 |
| EOS | `<eos>` | 2 |
| PAD | `<pad>` | 0 |
| UNK | `<unk>` | 3 |
| IM_START | `<\|im_start\|>` | 131072 |
| IM_END | `<\|im_end\|>` | 131073 |

---

## Usage

### vLLM (Recommended)

```bash
pip install vllm==0.9.2 --no-build-isolation
pip install "transformers==4.57.0"
vllm serve mkd-hossain/keural-14.8b-sft --dtype bfloat16 --max-model-len 4096
```

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mkd-hossain/keural-14.8b-sft"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

prompt = """<|im_start|>user
What is artificial intelligence?
<|im_end|>
<|im_start|>assistant
"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
    do_sample=True,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Roadmap

- [x] Stage 1 Pretraining — 100K steps, ~64.56B tokens
- [x] Stage 2 Annealing — 20K steps, ~5.16B clean tokens
- [x] SFT — 7K/18K steps (in progress)
- [ ] SFT — Full 18K steps
- [ ] DPO alignment
- [ ] Keural Chat model release (`mkd-hossain/keural-14.8b-chat`)

---

## Citation

```bibtex
@misc{keural2026,
  title  = {Keural: A Bilingual Korean-English MoE Language Model},
  author = {MKD Hossain},
  year   = {2026},
  url    = {https://huggingface.co/mkd-hossain/keural-14.8b-sft}
}
```

---

*Trained from scratch on KT Cloud NIPA2-H200 infrastructure using FSDP distributed training on 2× NVIDIA H200 GPUs.*
