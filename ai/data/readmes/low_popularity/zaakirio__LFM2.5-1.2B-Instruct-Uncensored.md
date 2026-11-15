---
base_model: LiquidAI/LFM2.5-1.2B-Instruct
base_model_relation: finetune
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/blob/main/LICENSE
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ar
- zh
- ja
- ko
- ru
tags:
- heretic
- abliterated
- decensored
- uncensored
- liquid
- lfm2
- lfm2.5
- edge
- conversational
---

# LFM2.5-1.2B-Instruct-Uncensored

An uncensored version of [`LiquidAI/LFM2.5-1.2B-Instruct`](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct),
made with [Heretic](https://github.com/p-e-w/heretic).

Heretic removes the model's safety alignment ("censorship") using **directional
ablation** (abliteration), with parameters chosen automatically by a TPE
optimizer that co-minimizes the refusal rate and the KL divergence from the
original model. Hence, the model stops refusing while keeping as much of its
original behavior as possible. No human prompt-engineering or fine-tuning data
was involved.

## Performance

| Metric | This model | Original model |
|---|---|---|
| Refusals (/100 harmful prompts) | **5** | 98 |
| KL divergence (harmless prompts) | **0.1003** | 0 (by definition) |

Refusals are measured against `mlabonne/harmful_behaviors`; KL divergence is
measured on `mlabonne/harmless_alpaca`. Lower is better for both. A KL of ~0.10
indicates the model's responses on benign prompts remain very close to the
original.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "LFM2.5-1.2B-Instruct-Uncensored"  # replace with your repo id

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [{"role": "user", "content": "Who are you?"}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

The export is a merged, full-precision **BF16** model in Hugging Face format
(148 tensors, ~2.2 GB) — no adapter merge or dequantization step is required at
load time.

## Abliteration parameters

Selected from **trial 72 of 80** (the best refusal/KL trade-off found by the
optimizer). Parameter names follow Heretic's canonical scheme; for LFM2 these
map onto the `out_proj` (attention output) and `w2` (MLP down) projections.

| Parameter | Value |
|---|---|
| direction_scope | per layer |
| direction_index | 12.31 |
| attn.o_proj.max_weight | 1.4818 |
| attn.o_proj.max_weight_position | 10.34 |
| attn.o_proj.min_weight | 0.9854 |
| attn.o_proj.min_weight_distance | 7.06 |
| mlp.down_proj.max_weight | 0.9760 |
| mlp.down_proj.max_weight_position | 11.74 |
| mlp.down_proj.min_weight | 0.2448 |
| mlp.down_proj.min_weight_distance | 6.54 |

## Run details

- **Base model:** `LiquidAI/LFM2.5-1.2B-Instruct` @ commit `6314d2b7cf28a6ae9de9d3e77dcfcd9c9f281c77`
- **Architecture:** LFM2, 16 layers, BF16
- **Trials:** 80 (24 startup) · **Seed:** 260601
- **Quantization during Heretic run:** none
- **Row normalization:** pre · **Orthogonalize direction:** true
- **Harmful set:** `mlabonne/harmful_behaviors` · **Harmless set:** `mlabonne/harmless_alpaca`

## Notes / reproducibility

LFM2 is not yet natively supported by upstream Heretic. This run used a local
compatibility patch for LFM2 module discovery, targeting the LFM2 `out_proj`
and `w2` projections (which the parameter table above refers to by Heretic's
generic `attn.o_proj` / `mlp.down_proj` names).

## Intended use & disclaimer

This model has had its refusal behavior substantially removed and will comply
with requests the original model would have declined. It is provided for
research and unrestricted local use. **You are responsible for how you use it**
and for complying with all applicable laws and with the base model's
[lfm1.0 license](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/blob/main/LICENSE),
which carries over to this derivative.

## Acknowledgements

- Base model: [LiquidAI/LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)
- Decensoring tool: [Heretic](https://github.com/p-e-w/heretic) by p-e-w
