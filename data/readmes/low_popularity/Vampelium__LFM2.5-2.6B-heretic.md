---
base_model: LiquidAI/LFM2.5-2.6B
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
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
tags:
- heretic
- uncensored
- decensored
- abliterated
- liquid
- lfm2.5
- edge
- a100
---

# LFM2.5-2.6B-heretic

Vampelium's local [LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) checkpoint after [Heretic](https://github.com/p-e-w/heretic) abliteration.

**Produced on NVIDIA A100.**

This is the BF16 safetensors export. The first shard was renamed from a split-download name (`model-00001-of-00002-001.safetensors`) back to the filename in `model.safetensors.index.json`. Payload size is 5,394,427,416 bytes (~5.0 GB BF16).

## Files

| File | Role |
| :--- | :--- |
| `model-00001-of-00002.safetensors` / `model-00002-of-00002.safetensors` | BF16 weights |
| `model.safetensors.index.json` | Shard map |
| `config.json` / `generation_config.json` | Model + decode settings |
| `tokenizer.json` / `tokenizer_config.json` / `chat_template.jinja` | Tokenizer + chat template |

## Load

Needs `transformers>=5.0.0` (this checkpoint was saved with 5.6.2).

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Vampelium/LFM2.5-2.6B-heretic"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16",
)
```

Liquid's recommended decode settings for this family: `temperature=0.1`, `top_k=50`, `repetition_penalty=1.1`.

## Disclaimer

Safety alignment was removed. You are responsible for how you use this model and for following applicable law. The base LFM [license](LICENSE) still applies.
