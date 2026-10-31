---
license: apache-2.0
language:
  - en
  - ko
tags:
  - aether
  - foundation-model
  - sovereign-ai
  - checkpoints
  - pretraining
  - fully-open
pretty_name: Aether-7B-5Attn Intermediate Pretraining Checkpoints
---

# Aether-7B-5Attn — Intermediate Pretraining Checkpoints

<!-- AETHER-FAMILY-LINKS -->

**Aether family** — [![5Attn Base](https://img.shields.io/badge/%F0%9F%A7%AC_Aether--7B--5Attn-Fully_Open-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) [![5Attn IT](https://img.shields.io/badge/%F0%9F%92%AC_Aether--7B--5Attn--it-Instruct-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) [![7Attn Base](https://img.shields.io/badge/%F0%9F%A7%A9_Aether--7B--7Attn--base-Open_Weights-teal)](https://huggingface.co/FINAL-Bench/Aether-7B-7Attn-base) [![11Attn](https://img.shields.io/badge/%F0%9F%94%9F_Aether--6B--11Attn-Open_Weights-purple)](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn) [![Demo](https://img.shields.io/badge/%F0%9F%9A%80_Demo-Aether_Sovereign_AI-orange)](https://huggingface.co/spaces/FINAL-Bench/Aether-Sovereign-AI) [![Blog](https://img.shields.io/badge/%F0%9F%93%9D_Blog-Open_Source_LLM-yellow)](https://huggingface.co/blog/FINAL-Bench/opensource-llm) [![Collection](https://img.shields.io/badge/%F0%9F%93%9A_Collection-Aether_Foundation-blue)](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)

<!-- /AETHER-FAMILY-LINKS -->

[![Blog](https://img.shields.io/badge/%F0%9F%A4%97%20Blog-Read%20the%20Aether%20story-FFD21E)](https://huggingface.co/blog/FINAL-Bench/opensource-llm)


Intermediate **pretraining checkpoints** of [FINAL-Bench/Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn), released for full reproducibility and training-dynamics research — the OLMo-tier "fully open" standard.

| Step | Tokens (approx) | Folder |
|------|-----------------|--------|
| 110,000 | ~98B | `step_110000/` |
| 115,000 | ~102B | `step_115000/` |
| 162,000 | ~144B (final pre-anneal base) | `step_162000/` |

The released base model is the **annealed** 162k checkpoint; these folders are the raw training checkpoints along the way.

Each folder contains `model.safetensors` + `config.json` + tokenizer. This is a **custom architecture** (`aether_v2_7way`) — load with the `aether_pkg/` code shipped in the [base model repo](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) (see its "How to load" section). Run inference at **batch_size = 1**.


## Related

- **Base model:** [Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn)
- **Instruction-tuned:** [Aether-7B-5Attn-it](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it)
- **Live demo (Space):** [Aether-Sovereign-AI](https://huggingface.co/spaces/FINAL-Bench/Aether-Sovereign-AI)
- **Collection:** [Aether Foundation Model](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)

Part of the [Aether Foundation Model collection](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model). License: Apache-2.0. Built by VIDRAFT (주식회사 비드래프트).
