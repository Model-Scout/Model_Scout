---
library_name: mlx
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
- vision
- mlx
- mlx-vlm
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> •
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# d1-3B-MLX-fp16

d1-3B is a decision model developed by [Liquid AI](https://www.liquid.ai/): it answers named, typed questions over a state (text, JSON or images) in one forward pass, with no generated tokens.

This repository is an MLX export of [d1-3B](https://huggingface.co/LiquidAI/d1-3B) in float16 for Apple Silicon, run with [mlx-vlm](https://github.com/Blaizzy/mlx-vlm). Find more details in the original model card: https://huggingface.co/LiquidAI/d1-3B

## 🏃 How to run d1-3B

Requires [MLX-VLM](https://github.com/Blaizzy/mlx-vlm) 0.7.8 or later:

```bash
pip install -U "mlx-vlm>=0.7.8"
```

```python
from mlx_vlm import load, predict

model, processor = load("LiquidAI/d1-3B-MLX-fp16")

# Text: several named questions over one state, answered in one pass
questions = {
    "refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"},
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
result = predict(model, processor, "I was charged twice this month, please refund one of them.", questions)
print(result["answers"])

# Image: the photo is the whole state
cats = {
    "type": "choice",
    "instructions": "How many cats are there?",
    "criteria": {"one": "One", "two": "Two", "more": "Three or more"},
}
print(predict(model, processor, None, {"cats": cats},
              images=["http://images.cocodataset.org/val2017/000000039769.jpg"]))
```

Each call returns `{"answers": {name: answer}, "usage": {"input_tokens": n, "output_tokens": 0}}`. A `choice` answer has the chosen label in `value`, plus `probabilities` and `metadata.confidence`; a `score` answer has the expected level in `value`, plus `probabilities` and the level `legend`; a `noul` (or `bool`) answer has `probability`, the probability of yes.

From the command line:

```bash
python -m mlx_vlm decide --model LiquidAI/d1-3B-MLX-fp16 \
  --state "I was charged twice this month, please refund one of them." \
  --questions '{"refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"}}'
```

`--state` is optional with one or more `--image` options.

As a server, with the same request shape on `/v1/decisions` (`"images"` take URLs, paths or base64 data URIs):

```bash
python -m mlx_vlm server --decision-model LiquidAI/d1-3B-MLX-fp16

curl http://127.0.0.1:8080/v1/decisions -H "Content-Type: application/json" -d '{
  "state": "I was charged twice this month, please refund one of them.",
  "questions": {"refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"}}
}'
```

## 📏 Precisions

Every precision was checked against the original checkpoint run in float32 with mlx-vlm, which matches the PyTorch reference to about 1e-5 in probability. The check covers 104 text and 41 image answers. "Same top answer" counts answers whose most likely option matches the float32 run; Δp is the largest change in any option's probability.

| Repository | Weights | Size | Same top answer | Max Δp | Mean Δp |
|---|---|---:|---:|---:|---:|
| **[d1-3B-MLX-fp16](https://huggingface.co/LiquidAI/d1-3B-MLX-fp16)** | float16 | 6.25 GB | 145/145 | 0.005 | 0.0006 |
| [d1-3B-MLX-8bit](https://huggingface.co/LiquidAI/d1-3B-MLX-8bit) | 8-bit language model; vision tower, projector and norms in float16 | 3.72 GB | 144/145 | 0.015 | 0.0020 |
| [d1-3B-MLX-4bit](https://huggingface.co/LiquidAI/d1-3B-MLX-4bit) | 4-bit language model; vision tower, projector and norms in float16 | 2.37 GB | 142/145 | 0.212 | 0.0276 |

float16 is the recommended precision. The checkpoint is stored in bfloat16; in float16 all but about 0.1% of its weights, the very smallest, are exact and none overflow, and float16 computes with more precision at the same speed on Apple GPUs. It stays closest to the float32 answers, so there is no bfloat16 export. The quantized exports keep their unquantized parts in float16, which cut the 8-bit drift by more than half compared with bfloat16. 8-bit moves probabilities by up to about 0.015. 4-bit moves them by up to about 0.2, so prefer it only where memory matters more than calibration. The top answers that changed were near ties, with the float32 runner-up within 0.1. The vision tower and projector are never quantized. This check is a smoke test of agreement, not an accuracy benchmark.

## 🧪 Recipe

Converted from [d1-3B](https://huggingface.co/LiquidAI/d1-3B) with [mlx-vlm](https://github.com/Blaizzy/mlx-vlm):

```bash
python -m mlx_vlm convert --hf-path LiquidAI/d1-3B --mlx-path d1-3B-MLX-fp16 --dtype float16
```

The upstream PyTorch `.py` files were removed after conversion; `config.json` keeps its `auto_map` entry, which mlx-vlm uses to select d1.

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

```bibtex
@article{liquidai2025lfm2,
  title   = {LFM2 Technical Report},
  author  = {Liquid AI},
  journal = {arXiv preprint arXiv:2511.23404},
  year    = {2025}
}
```

## 📄 License

This model is released under the [LFM 1.0 License](LICENSE), as is the original checkpoint.
