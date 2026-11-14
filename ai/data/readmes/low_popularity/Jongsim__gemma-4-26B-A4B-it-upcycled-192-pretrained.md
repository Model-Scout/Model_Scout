---
license: gemma
base_model: google/gemma-4-26B-A4B-it
library_name: transformers
pipeline_tag: text-generation
tags:
- gemma
- gemma4
- moe
- mixture-of-experts
- continued-pretraining
- lomo
- drop-upcycling
- heretic
- uncensored
language:
- en
- ko
---

# gemma-4-26B-A4B Drop-Upcycled 192-Expert (LOMO pretrained)

## Model description

This repository contains an **intermediate continued-pretraining checkpoint** derived from an
abliterated/uncensored Heretic variant of `google/gemma-4-26B-A4B-it`
(`gemma-4-26B-A4B-it-uncensored-heretic`, internal abliteration using the Heretic method).
The 128-expert MoE was **upcycled to 192 experts** via Drop-Upcycling, then trained with
**LOMO** continued pretraining on FineWeb-Edu to differentiate the newly added experts from
the original ones.

This is **not** an instruction-tuned model. SFT and any preference / RL stages have **not**
been performed yet.

## Lineage

```
google/gemma-4-26B-A4B-it                                 (upstream base)
        │
        ▼ Heretic abliteration (refusal-direction ablation)
gemma-4-26B-A4B-it-uncensored-heretic                     (intermediate, not released here)
        │
        ▼ Drop-Upcycling: 128 → 192 experts (64 new = noisy clones of existing)
gemma-4-26B-A4B-it-upcycled-192                           (pre-LOMO)
        │
        ▼ LOMO continued pretraining on FineWeb-Edu (3,000 steps, experts + router only)
gemma-4-26B-A4B-it-upcycled-192-pretrained                (this repo)
```

## Drop-Upcycling

1. **Weight surgery**: Original 128 expert weights are kept as-is; 64 new experts are
   initialized as clones of existing experts with 30% of their weights reinitialized (noise
   perturbation, seed 42).
2. **Router expansion**: Router projection expanded from `[128, hidden]` to `[192, hidden]`
   with new rows initialized near zero.
3. **Continued pretraining (LOMO)**: Only the expert and router weights are updated;
   attention, dense MLP, embeddings, and the LM head are frozen.

## Training details

| Item | Value |
|---|---|
| Base model | `google/gemma-4-26B-A4B-it` |
| Architecture | Gemma 4 A4B MoE expanded from 128 → **192 experts** |
| Training stage | LOMO continued pretraining only |
| Training length | **3,000 steps** |
| Optimizer | LOMO (SGD fused into backward, zero optimizer state) |
| Dataset | **FineWeb-Edu** (`HuggingFaceFW/fineweb-edu`, config `sample-10BT`, streaming) |
| Trainable | Expert gate/up/down × N layers, Router weights × N layers |
| Frozen | Attention (q/k/v/o), Dense MLP, Embeddings, LM Head |
| Precision | bf16 |
| Hardware | NVIDIA GB10 (DGX Spark), 128 GB unified memory |
| Format | safetensors (16 shards) |

## Intended use

Use this model as a **warm-start checkpoint** for further supervised fine-tuning or
preference-based post-training. It is not intended for direct use as an assistant; instruction
following and safety behavior have not been tuned at this stage.

## Limitations

- Intermediate artifact — instruction-following quality is not optimized.
- No safety alignment has been performed.
- New experts have only had limited continued pretraining; downstream training is required to
  fully realize the benefit of the expanded MoE.

## Load with Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Jongsim/gemma-4-26B-A4B-it-upcycled-192-pretrained"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="bfloat16",
    device_map="auto",
)
```

## License

Subject to the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
