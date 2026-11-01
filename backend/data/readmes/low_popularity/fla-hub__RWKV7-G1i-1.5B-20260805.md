---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- fr
- ar
- es
- pt
pipeline_tag: text-generation
---

# RWKV7-G1i-1.5B-20260805

This is RWKV-7 (G1i) model under flash-linear attention format.

## Model introduction

RWKV-7 is an attention-free recurrent architecture with a constant-size
recurrent state and constant inference work per generated token. Training
remains parallelizable.

This checkpoint is a base model pretrained with web, code, synthetic,
instruction, chat, and reasoning data. It is suitable for evaluation,
post-training, and fine-tuning; the included chat template is a prompt
interface, not a claim that the checkpoint is a safety-aligned assistant.

## Model Details

- **Developed by:** Bo Peng, Yu Zhang, Songlin Yang, Ruichong Zhang, Zhiyuan Li
- **Funded by:** RWKV Project (Under LF AI & Data Foundation)
- **Model type:** RWKV7
- **Language(s) (NLP):** Multilingual
- **License:** Apache-2.0
- **Parameter count:** 1.5B
- **Tokenizer:** RWKV World tokenizer
- **Vocabulary size:** 65,536

### Model Sources

- **Repository:** https://github.com/fla-org/flash-linear-attention ; https://github.com/BlinkDL/RWKV-LM
- **Paper:** https://arxiv.org/abs/2503.14456
- **Model:** rwkv7-g1i-1.5b-20260805-ctx16384.pth

## Uses

Install `flash-linear-attention` and the latest version of `transformers` before using this model:

```bash
pip install git+https://github.com/fla-org/flash-linear-attention
pip install 'transformers>=4.48.0'
```

### Direct Use

```python
import fla
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained('RWKV7-G1i-1.5B-20260805')
tokenizer = AutoTokenizer.from_pretrained('RWKV7-G1i-1.5B-20260805', trust_remote_code=True)
model = model.cuda()
```
