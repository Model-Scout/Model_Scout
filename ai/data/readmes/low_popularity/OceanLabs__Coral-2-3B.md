---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: image-text-to-text
base_model: LiquidAI/d1-3B
tags:
- liquid
- lfm2.5
- edge
- decision
- classification
- calibration
- system-one
- multimodal
- decision-model
- koral
- koral2
---

<div align="center">
  <h1>Koral 2</h1>
  <p><strong>High-performance single-pass decision model</strong></p>
  <p>Built on <a href="https://huggingface.co/LiquidAI/d1-3B">LiquidAI/d1-3B</a> (LFM2.5-VL-3B)</p>
</div>

# Koral 2

**Koral 2** is an improved decision model based on [d1-3B](https://huggingface.co/LiquidAI/d1-3B).  
It delivers calibrated, typed answers in **one forward pass with zero output tokens**.

### Key improvements over d1-3B

- Faster inference (aggressive packing, optional `torch.compile`, 4-bit/8-bit quantization support)
- Better calibration (temperature & vector scaling)
- Additional question types: `rank` and `extract`
- Cleaner Python API under the name `Koral2`
- Same multimodal capabilities (text + images)

## Quick start

```bash
pip install "transformers>=5.14" torch torchvision pillow
```

```python
from transformers import AutoModel
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModel.from_pretrained(
    "YOUR_USERNAME/Koral-2",          # or local path
    trust_remote_code=True,
    dtype=torch.bfloat16
).to(device)

questions = {
    "refund": {
        "type": "noul",
        "instructions": "Is the customer asking for a refund?",
    },
    "team": {
        "type": "choice",
        "instructions": "Which team should handle this?",
        "criteria": {
            "billing": "Charges, refunds, invoices",
            "technical": "App or site faults",
            "fraud": "Suspected unauthorised use",
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this?",
        "criteria": ["Can wait", "Today", "Blocking the customer now"],
    },
}

result = model.system_one(
    "I was charged twice this month, please refund one of them.",
    questions
)
print(result)
```

## Supported question types

| Type      | Description                          | Answer fields                                      |
|-----------|--------------------------------------|----------------------------------------------------|
| `noul`    | Yes / No                             | `noul` (P(yes)), `confidence`                      |
| `choice`  | Single choice from named options     | `choice`, `confidence`, `probabilities`            |
| `score`   | Ordered score (0 … n-1)              | `score`, `confidence`, `probabilities`, `legend`   |
| `rank`    | Ranking of options                   | `ranking`, `confidence`, `probabilities`           |
| `extract` | Presence decision (yes/no)           | `noul`, `confidence`                               |

## Performance notes

- Single question: typically 5–8 ms on RTX 4090 (with `compile=True`)
- Multiple questions share the same state (read once)
- Optional 4-bit quantization via `bitsandbytes`

## Citation

```bibtex
@article{liquidAI2026opend1,
  author  = {Liquid AI},
  title   = {Open d1: Edge decision models for text, vision, and audio},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {https://www.liquid.ai/blog/d1-open},
}
```

Koral 2 is a community / derived inference layer built on top of the official d1-3B release.
