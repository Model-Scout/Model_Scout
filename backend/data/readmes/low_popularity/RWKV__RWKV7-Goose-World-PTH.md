---
language:
- en
- zh
- fr
- es
- de
- pt
- ru
- it
- ja
- ko
- vi
- ar
tags:
- pytorch
- text-generation
- causal-lm
- rwkv
license: apache-2.0
datasets:
- HuggingFaceFW/fineweb-edu
- mlfoundations/dclm-baseline-1.0
- cerebras/SlimPajama-627B
- EleutherAI/pile
- bigcode/starcoderdata
- oscar-corpus/OSCAR-2301
---

# RWKV-7 World

Use rwkv pip package 0.8.28+ for RWKV-7 inference: https://pypi.org/project/rwkv/

Evals and more information: https://rwkv.com/

For developers: https://github.com/BlinkDL/RWKV-LM

Chat demo: https://github.com/BlinkDL/ChatRWKV/blob/main/API_DEMO_CHAT.py

MMLU eval: https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v7/rwkv_mmlu_eval.py

rwkv7-v3-2.9b 54.56% (rwkv6-v2.1-3.1b 32.38%)

rwkv7-v3-1.5b 44.84% (rwkv6-v2.1-1.6b 26.34%)

0.1B = L12 D768 // 0.4B = L24 D1024 // 1.5B = L24 D2048 // ~3B = L32 D2560 // ~7B = L32 D4096

## Model Description

RWKV-7 trained on 100+ world languages (80% English, 10% multilang, 10% code).

World-v3 = 3.1T tokens

World-v2.9 = subsampled 2T tokens

World-v2.8 = subsampled 1T tokens

Recommended fine-tuning format (use \n for newlines):
```
User: xxxxxxxxxxxxxxx

Assistant: xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx

User: xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx

Assistant: xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
```

A good chat prompt (better replace \n\n in xxx to \n, such that there will never be extra \n\n in response):
```
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: xxx

Assistant:
```
QA prompt (better replace \n\n in xxx to \n, such that there will never be extra \n\n in response):
```
Question: xxx

Answer:
```
and
```
Instruction: xxx

Input: xxx

Response:
```

!!! There should not be any space after your final ":" or you will upset the tokenizer and see non-English reponse !!!

!!! There should not be any space after your final ":" or you will upset the tokenizer and see non-English reponse !!!

!!! There should not be any space after your final ":" or you will upset the tokenizer and see non-English reponse !!!