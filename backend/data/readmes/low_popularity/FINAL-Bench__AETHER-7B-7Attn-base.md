---
license: apache-2.0
language:
- ko
- en
library_name: transformers
tags:
- aether
- vidraft
- open-weight
- heterogeneous-attention
pipeline_tag: text-generation
---

# AETHER-7B-7Attn-base

[![Blog](https://img.shields.io/badge/📝_Blog-Open_Source_LLM-yellow?style=for-the-badge)](https://huggingface.co/blog/FINAL-Bench/opensource-llm)
[![Collection](https://img.shields.io/badge/📚_Collection-Aether_Foundation-blue?style=for-the-badge)](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model-6a5c7f2fa1a4165c0414e53a)
[![Demo](https://img.shields.io/badge/🚀_Demo-Aether_Sovereign_AI-orange?style=for-the-badge)](https://huggingface.co/spaces/FINAL-Bench/Aether-Sovereign-AI)


### Which Aether model should I use?

| Model | What it is | Pick it if |
|---|---|---|
| [**Aether-7B-5Attn**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) | 6.59B MoE base. **Fully open** - weights + data recipe + training code + all 162k-step logs + checkpoints | You want to audit, verify or rebuild a foundation model end to end |
| [**Aether-7B-5Attn-it**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) | The same model, instruction-tuned | You want it to answer rather than continue text |
| [**AETHER-7B-7Attn-base**](https://huggingface.co/FINAL-Bench/AETHER-7B-7Attn-base) | Same 49-layer architecture, a different checkpoint. Open weights | You want a second run of this architecture to compare against |
| [**Aether-6B-11Attn-base**](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn-base) | 121 layers, **11 sequence-mixing mechanisms** in one network - attention, Mamba-2, Hyena, GDN, MLA - on an 11x11 Latin square | You research heterogeneous sequence mixing. It is a mid-training research artifact |

All four load the same way:

```python
AutoModelForCausalLM.from_pretrained(MODEL, trust_remote_code=True, dtype=torch.bfloat16)
```

[![Aether-7B-5Attn](https://img.shields.io/badge/🧬_Aether--7B--5Attn-Base-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn)
[![Aether-7B-5Attn-it](https://img.shields.io/badge/💬_Aether--7B--5Attn--it-Instruct-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it)
[![Checkpoints](https://img.shields.io/badge/🗂️_Checkpoints-Intermediate-lightgrey)](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints)
[![License](https://img.shields.io/badge/License-Apache_2.0-brightgreen)](https://www.apache.org/licenses/LICENSE-2.0)

**Open-weight release — weights and modeling code. Training data, recipe and logs are not included.**

> To our knowledge, the first foundation model to implement
> **seven heterogeneous attention mechanisms within a single architecture.**

## Attention layout

![7x7 Latin square attention layout](latin_square.svg)

Seven distinct attention mechanisms (**A–G**) are distributed across **49 layers** in a
**7×7 Latin square** — every mechanism appears exactly once in each row and each column,
so no single mechanism dominates any depth band.

*The layer-to-mechanism assignment is defined by `LATIN_SQUARE_7x7` in `modeling_aether_v2_7way.py`.*

## Model

| | |
|---|---|
| Parameters | **6.59B** total / **~3B** active (Mixture-of-Experts) |
| Type | Decoder-only language model, heterogeneous multi-attention architecture |
| Precision | bfloat16 |
| Languages | Korean, English |
| Stage | Pretrained base (no instruction tuning) |
| Developer | **VIDRAFT** |

Unlike conventional models that repeat a single attention mechanism across all layers,
AETHER-7B-7Attn composes **seven distinct attention mechanisms** inside one network.
This heterogeneous design is the defining characteristic of the AETHER architecture.

## Release scope

This repository ships the **weights and the modeling code** needed to load them.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "FINAL-Bench/AETHER-7B-7Attn-base"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda"
).eval()
```

`trust_remote_code=True` is required — `aether_v2_7way` is a custom architecture.

**Not released here:** the training data, data mixture, training code, logs and
hyperparameters. Those are published only for the fully-open sibling
[Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn), which shares
this architecture. This model is therefore **open-weight**, not open-source, in the
sense that it cannot be reproduced from what is in this repository.

### Notes for use

- **Run at `batch_size=1`.** The NSA branches do not consume a padding mask, so
  batching padded sequences can silently corrupt results.
- **No KV cache.** `use_cache` is already `False` in the config; generation re-runs the
  full forward pass per token and is correspondingly slow.
- **Base model, no safety alignment.** It continues text rather than following
  instructions. Do not deploy it as-is.

## Intended use

Released for **research, evaluation and benchmarking of the released weights**.
This is a base (pretrained) model — it continues text rather than following instructions.

## License

**Apache-2.0** — the released **weights** are free to use, modify and redistribute
under the terms of the Apache License 2.0.

The architecture implementation is included in this repository under the same licence.
The training pipeline and data recipe are not part of this release.

---

**VIDRAFT** · Sovereign AI
