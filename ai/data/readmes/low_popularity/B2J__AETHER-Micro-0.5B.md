---
license: apache-2.0
language:
  - ko
  - en
tags:
  - moe
  - mixture-of-experts
  - custom
  - aether
  - latent-thought
  - multi-token-prediction
library_name: transformers
pipeline_tag: text-generation
---

# AETHER-Micro 0.5B (Phase 1 Checkpoint)

AETHER-Micro is an experimental MoE-based language model.

## Model Details

| Item | Value |
|------|-------|
| Architecture | MoE big.LITTLE + LTL + MTP |
| Total Parameters | 2.08B |
| Active Parameters | ~0.5B per token |
| Hidden Size | 1024 |
| Layers | 24 |
| Attention | GQA 16 heads, 4 KV heads |
| Experts | 5 Big + 15 Small + 2 Shared |
| Vocab Size | 64,000 Korean + English + Code |
| Context Length | 8,192 RoPE |
| Training Step | 57,000 / 100,000 |
| Training Loss | ~3.54 |

## Architecture Features

- **big.LITTLE MoE**: 5 large experts (2048 intermediate) + 15 small experts (1024 intermediate) + 2 shared experts (always active)
- **Latent Thought Layer (LTL)**: K-step latent reasoning (K=0,1,2) via Gumbel-Softmax selection
- **Multi-Token Prediction (MTP)**: 4-step ahead prediction replacing standard NTP loss
- **Wu-Xing Router**: Five-element inspired expert routing
- **Quality Head**: 4-dimensional quality assessment

## Training

- **Phase**: 1 of 3 (57% complete)
- **Data**: 13.1B tokens (Korean 22%, English 25%, Code 21%, Math 24%, Dialogue 8%)
- **Optimizer**: AdamW (lr=1e-4, cosine decay)
- **Precision**: FP32

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Be2Jay/AETHER-Micro-0.5B",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("Be2Jay/AETHER-Micro-0.5B")
```

> **Note**: This is a Phase 1 training checkpoint. The model is still in early training and not yet suitable for production use.

## License

Apache 2.0
