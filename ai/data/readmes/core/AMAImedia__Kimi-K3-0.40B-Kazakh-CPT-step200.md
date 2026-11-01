---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- ru
- zh
- vi
- kk
- ja
- af
- am
- ar
- as
- ast
- az
- be
- bg
- bn
- bs
- ca
- ceb
- ckb
- cs
- cy
- da
- de
- el
- es
- et
- eu
- fa
- ff
- fi
- fil
- fr
- ga
- gl
- gn
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- ig
- is
- it
- jv
- ka
- kam
- kea
- km
- kmr
- kn
- ko
- ky
- lb
- lg
- ln
- lo
- lt
- luo
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- mvy
- my
- ne
- nl
- "no"
- nso
- ny
- oc
- om
- "or"
- pa
- pl
- ps
- pt
- qxp
- ro
- rw
- sd
- sk
- skr
- sl
- sn
- so
- sr
- sv
- sw
- ta
- te
- tg
- th
- ti
- tk
- tr
- ug
- uk
- umb
- ur
- uz
- wo
- xh
- yo
- yue
- zu
base_model:
- tencent/Hy4-preview
- AngelSlim/Hy4-preview-GGUF
tags:
- tencent
- Hy4-preview
- Hy4
---

<!-- apex-banner -->
<div style="background-color: #f59e0b; color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
<h2 style="color: white; margin: 0 0 10px 0;">⚡ Each donation funds the next large quant.</h2>
<p style="font-size: 16px; margin: 0 0 15px 0;">I host free GGUF or MoE quants as independent research.<br>
Local hardware: <b>Mechrevo Kuangshi GM7AG0M</b> — RTX 3060 Laptop 6GB GDDR6, 64GB DDR5, i7-12700H (14C/20T, 4.7GHz), Windows 11, Samsung 990 Pro.<br>
Good for imatrix and 0.6–35B-class work in RAM. <b>9B+ and searches need rented H200/Blackwell</b>, typically $100 per quant.</p>
<p style="font-size: 20px; margin: 0;">
<a href="https://boosty.to/amaimediacom" style="color: white; text-decoration: underline;">🎉 Boosty🦄</a>  | 
<a href="https://donatex.gg/widgets/donation-goal/89bc59e8-b69c-467a-9aa0-5e1c3f8842d6" style="color: white; text-decoration: underline;">☕ Buy Me a Coffee🦄</a>  | 
<a href="https://www.donationalerts.com/r/djbionicl" style="color: white; text-decoration: underline;">⭐ DonationAlerts🦄</a>
</p>
<p style="font-size: 14px; margin: 10px 0 0 0; opacity: 0.9;">💚 Thanks to Hugging Face for extra storage.🦄</p>
</div>

---


## NOESIS / AMAImedia

Released as part of the NOESIS Professional Multilingual Dubbing Automation Platform (framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators).

- **Founder:** Ilia Bolotnikov
- **Organization:** AMAImedia.com
- **X (Twitter):** [@AMAImediacom](https://x.com/AMAImediacom)
- **LinkedIn:** [Ilia Bolotnikov](https://www.linkedin.com/in/ilia-bolotnikov)
- **Telegram:** [@djbionicl](https://t.me/djbionicl)
- **NOESIS version:** v16.1
- **Release date:** 2026-09-18

# Kimi-K3-0.40B Kazakh CPT — Step 200

An experimental Kazakh continued-pretraining checkpoint based on `inference-optimization/Kimi-K3-0.40B`.

This is an early smoke-test checkpoint created to validate a complete Kazakh language-model pretraining pipeline on Kaggle.

## Important limitation

The base checkpoint is a tiny architecture-development version of Kimi K3. Its weights were initialized from scratch and trained only on a toy copypasta dataset. It is not a distilled or compressed version of the trained 2.8T Kimi K3 model.

This checkpoint is therefore an educational research artifact, not a production language model.

## Training

- Dataset: `kz-transformers/multidomain-kazakh-dataset`
- Objective: causal language modeling
- Optimizer steps: 200
- Tokens processed: 1,638,400
- Sequence length: 512
- Effective batch: 8,192 tokens
- Initial learning rate: 3e-4
- Hardware: 1× NVIDIA T4
- Runtime: approximately 12.7 minutes
- Tokenization: native Kimi tokenizer accelerated with Gigatoken

## Results

| Metric | Before | After |
|---|---:|---:|
| Validation loss | 16.7615 | 4.9539 |
| Validation perplexity | 19,030,254 | 141.72 |

## Example generations

The model has started learning Kazakh Cyrillic, morphology, punctuation, and sentence structure, but its generations remain semantically incoherent and contain invented words. This is expected after only 1.64M training tokens.

## Usage

Install the required libraries:

```bash
pip install -U torch transformers
```

Run a minimal Kazakh text-generation example:

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_id = "AMAImedia/Kimi-K3-0.40B-Kazakh-CPT-step200"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)

model = AutoModel.from_pretrained(
    model_id,
    trust_remote_code=True,
    torch_dtype=torch.float16,
    device_map="auto",
)

prompt = "Қазақстан —"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.inference_mode():
    output = model.language_model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
    )

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

For reproducible comparisons, use a fixed random seed and report the prompt, decoding parameters, Transformers version, and hardware. Because this is an intermediate checkpoint, outputs should be treated as experimental and inspected manually.

## Intended use

This checkpoint is intended for studying Kazakh language adaptation, inspecting Kimi K3's small architecture-development configuration, testing dataset and pretraining pipelines, and comparing intermediate language-acquisition checkpoints.

It should not be used for factual, safety-critical, medical, legal, financial, or production tasks. The checkpoint has not been instruction-tuned or safety-aligned for general deployment.

## License

This repository is released under the MIT License. Review the base model and dataset terms before redistribution or commercial use.
