---
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
library_name: transformers
pipeline_tag: text-generation
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
tags:
- liquid
- lfm3
- abliterated
- uncensored
- heretic
- gguf
- llama.cpp
---

# LFM3-1.7B-abliterated

**This model is a modified version of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B). The weights were changed. It is not the original model and Liquid AI does not endorse or support it.** (Modification notice, LFM Open License v1.0, section 4(b).)

## What changed

Refusal behavior was removed with directional ablation (abliteration) using
[Heretic](https://heretic-project.org) v1.4.0. For attention output projections and MLP down
projections, the component of each weight matrix along a per-layer refusal direction was
subtracted, with the strength varying by layer depth.

Search: 120 Heretic trials on one L4 GPU, optimizing refusal count and KL divergence against the
original model. The selected trial's parameters are in `heretic_trial.json`.

| Metric (Heretic eval, 100 held-out harmful prompts) | Original | This model |
|---|---|---|
| Refusals | 98 / 100 | 11 / 100 |
| KL divergence from original | 0 | 0.055 |

A separate 30-prompt check ran the base model and this model through `llama.cpp` on CPU with
identical settings. The base model refused all 30. This model gave a substantive answer to 29 of
30 by the automated refusal classifier, and 30 of 30 on manual reading, since the classifier
flagged one answer that contains the word "harmful" inside an actual instruction.
Transcripts: `results/baseline-100.json`, `results/final-30.json`.

## Files

| File | Use |
|---|---|
| `LFM3-1.7B-abliterated-Q4_K_M.gguf` | CPU inference, 1.1 GB, best fit for 8 GB machines |
| `LFM3-1.7B-abliterated-q8_0.gguf` | reference quant, 1.8 GB |
| `model.safetensors` | merged weights in Hugging Face format (bf16) |
| `configuration_lfm3.py`, `modeling_lfm3.py`, `lfm3_conv.py` | LFM3 custom code, needed by `trust_remote_code` |
| `prompts-final.json` | the 30 test prompts |
| `heretic_trial.json` | ablation parameters |

## Running it

llama.cpp:

```bash
llama-cli -m LFM3-1.7B-abliterated-Q4_K_M.gguf -cnv
```

You need llama.cpp built from master. LFM3 support landed on 2026-10-27, after the latest prebuilt
release, so older binaries reject the architecture with `unknown model architecture: 'lfm3'`.

Transformers:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("bowtiedrahman/LFM3-1.7B-abliterated", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("bowtiedrahman/LFM3-1.7B-abliterated")
```

## Intended use and limits

Intended for research on refusal behavior, and for local use where the safety training of the
base model gets in the way of legitimate work.

This model will produce content the original refuses, including instructions for illegal or
harmful activity. It has no safety filtering. Do not deploy it where an unfiltered model would
reach end users, and check the license before commercial use.

Model quality is otherwise that of LFM3-1.7B, a 1.7B model. Factual accuracy is limited. The
abliteration also costs some general capability, as the KL divergence above indicates.

## License

LFM Open License v1.0, inherited from the base model. The full text is in `LICENSE`. Redistribution
requires keeping that license, marking modified files, and retaining attribution. Commercial use is
conditioned on the license's revenue threshold.
