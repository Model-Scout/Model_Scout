---
license: mit
language:
- am
- ar
- bn
- zh
- cs
- nl
- en
- fr
- de
- el
- ha
- he
- hi
- id
- it
- ja
- jv
- km
- ko
- lo
- ms
- mr
- fa
- pl
- pt
- ro
- ru
- es
- sw
- sv
- tl
- ta
- te
- th
- tr
- uk
- ur
- vi
datasets:
- simplescaling/s1K
- lightblue/reasoning-multilingual-R1-Llama-70B-train
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
library_name: transformers
---
It's a 1.5B model.

It's a distill model like s1 and deepseek-r1-distill.

It's test model. I hope I can reproduce a rl model like RL-Zero.

This model is a mini-step.

Thanks for evveryone in the open community.

how to use:
```
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model = LLM(
    "Amu/t1-1.5B"
)
tok = AutoTokenizer.from_pretrained("simplescaling/s1-32B")

stop_token_ids = tok("<|im_end|>")["input_ids"]

sampling_params = SamplingParams(
    max_tokens=32768,
    min_tokens=0,
    stop_token_ids=stop_token_ids,
)

prompt = "How many r in raspberry"
prompt = "<|im_start|>system\nYou are t1, created by Amu. You are a helpful assistant.<|im_end|>\n<|im_start|>user\n" + prompt + "<|im_end|>\n<|im_start|>assistant\n"

o = model.generate(prompt, sampling_params=sampling_params)
print(o[0].outputs[0].text)
```