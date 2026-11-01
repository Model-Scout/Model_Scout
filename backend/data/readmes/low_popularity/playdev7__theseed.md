---
license: mit
language:
- ko
- en
metrics:
- bertscore
- accuracy
- bleu
- code_eval
- charcut_mt
- character
pipeline_tag: text-generation
tags:
- conversational
- mixtral
---
# TheSeed

## Model Generation
```
from transformers import AutoConfig, AutoModel, AutoTokenizer
config = AutoConfig.from_pretrained("playdev7/theseed", revision=revision)
model = AutoModel.from_pretrained("playdev7/theseed", revision=revision, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("playdev7/theseed", revision=revision)
```
---
based on Mixtral  
Made by Dohyeon Kwon(playdev7@gmail.com)