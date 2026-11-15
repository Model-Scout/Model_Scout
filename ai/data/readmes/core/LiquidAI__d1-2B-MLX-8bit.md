---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm3
- edge
- decision
- classification
- calibration
- system-one
- multimodal
- vision
- mlx
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
base_model: LiquidAI/d1-2B
base_model_relation: quantized
---

<div align="center">
  <img
    src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/liquid-ai-banner.webp"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0;"
  />
  <div align="center" style="display: flex; justify-content: center; align-items: center; gap: 1.25em; margin: 8px 0 1.7rem; padding: 0; line-height: 1.3;">
    <a href="https://console.liquid.ai/dashboard" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath d=%22m8 6-6 6 6 6m8-12 6 6-6 6m-2-14-4 16%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>API</strong></a>
    <a href="https://playground.liquid.ai/" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath transform=%22translate(3 0)%22 d=%22M8 5.5v13L19 12 8 5.5Z%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Try</strong></a>
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath d=%22M12 6c-3-2-6-2.5-10-2v15c4-.5 7 0 10 2m0-15c3-2 6-2.5 10-2v15c-4-.5-7 0-10 2V6Z%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Docs</strong></a>
    <a href="https://www.liquid.ai/blog/lfm3" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath transform=%22translate(1 0)%22 d=%22m16 3 5 5L8 21H3v-5L16 3Zm-3 3 5 5%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Blog</strong></a>
  </div>
</div>

# d1-2B-MLX-8bit

8-bit MLX version of [d1-2B](https://huggingface.co/LiquidAI/d1-2B) for Apple Silicon. The weights take 2.22 GB.

d1-2B is a decision model for text, pictures, and video. It answers named, typed questions over a state with calibrated probabilities in one forward pass, without generating tokens.

The language model uses 8-bit affine quantization with groups of 64. The vision tower, projector and norms stay in FP16. Against the original checkpoint run in float32, it kept all 52 test answers and moved probabilities by at most 0.008.

Find architecture and usage details in the [original model card](https://huggingface.co/LiquidAI/d1-2B).

## Use with MLX-VLM
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

Requires [MLX-VLM](https://github.com/Blaizzy/mlx-vlm) 0.7.11 or later:

```bash
pip install -U "mlx-vlm>=0.7.11"
```

d1-2B answers questions without generating text, so chat apps and `mlx_vlm.generate` cannot run it. Use `model.system_one` or the `decide` command below.

```python
from mlx_vlm import load
from mlx_vlm.utils import load_image

model, processor = load("LiquidAI/d1-2B-MLX-8bit")

# Text: several named questions over one state, answered in one pass
ticket = "I was charged twice and my parcel never arrived. Please refund one charge."
out = model.system_one(ticket, {
    "refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"},
    "team": {"type": "choice", "instructions": "Which team should handle this?",
             "criteria": {"billing": "Charges, refunds, invoices",
                          "shipping": "Delivery and parcels",
                          "technical": "App or site faults"}},
    "topics": {"type": "choice", "multiple": True,
               "instructions": "Which topics does the message raise?",
               "criteria": {"billing": "Payments and charges",
                            "delivery": "Shipping and parcels",
                            "login": "Signing in to the account"}},
    "urgency": {"type": "score", "instructions": "How urgent is this ticket?",
                "criteria": ["low", "medium", "high"]},
})
a = out["answers"]
print(round(a["refund"]["noul"], 2), a["team"]["choice"], a["topics"]["choices"],
      a["urgency"]["legend"][str(int(a["urgency"]["score"]))])
# 1.0 billing ['billing', 'delivery'] medium
print(out["usage"])
# {'input_tokens': 189, 'output_tokens': 0}

# Picture: the photo is the whole state
image = load_image("http://images.cocodataset.org/val2017/000000039769.jpg")
out = model.system_one(None, {
    "cats": {"type": "number", "instructions": "How many cats are there?", "range": [0, 10], "step": 1},
    "remote": {"type": "box", "instructions": "Where is the remote control on the left?"},
}, media=[image])
a = out["answers"]
print(a["cats"]["number"], {k: round(v, 2) for k, v in a["remote"]["box"].items()})
# 2.0 {'top': 0.15, 'bottom': 0.24, 'left': 0.06, 'right': 0.28}
```

`model.system_one` returns `{"answers": {name: answer}, "usage": {...}}`, and `model.system_one_batch` takes several requests. The original model card describes every question type and answer field.

From the command line, the answers print as JSON:

```bash
python -m mlx_vlm decide --model LiquidAI/d1-2B-MLX-8bit \
  --state "I was charged twice this month. Please refund one of the charges." \
  --questions '{"refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"}}'
```

More options in the [MLX guide](https://docs.liquid.ai/deployment/on-device/mlx).
