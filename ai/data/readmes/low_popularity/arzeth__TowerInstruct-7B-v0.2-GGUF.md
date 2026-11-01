---
base_model: Unbabel/TowerInstruct-7B-v0.2
inference: false
language:
- en
- de
- fr
- zh
- pt
- nl
- ru
- ko
- it
- es
license: cc-by-nc-4.0
model_creator: Unbabel
model_name: TowerInstruct 7B v0.2
model_type: llama
pipeline_tag: translation
quantized_by: arzeth
---
# Model Info

- Model creator: [Unbabel](https://huggingface.co/Unbabel)
- Original card (has more info): https://huggingface.co/Unbabel/TowerInstruct-7B-v0.2
- Languages: English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Chinese, Russian.
- Context size: 4096, but according to the model's card it was trained with `max_seq_length: 2048`, so make sure your input is ≤2048 tokens (is that ~1500 words?).
- Template: The model was trained using the ChatML prompt templates **WITHOUT ANY SYSTEM PROMPTS !!!**, i.e. there's no `<|im_start|>system`, it's just
```
<|im_start|>user
{USER PROMPT}<|im_end|>
<|im_start|>assistant
{MODEL RESPONSE}<|im_end|>
<|im_start|>user
[...]
```

# Quantization info

I didn't use imatrix because I have no idea if they are okay for non-general-purpose LLMs.

Quantized with llama.cpp @ 4c4cb30736582cacb1a164a9d4bc8e17b1014be7 (2024-02-24).

IQ3_M requires minimum 4c4cb30736582cacb1a164a9d4bc8e17b1014be7

# Licensing

These .gguf files themselves are under CC-0 (i.e. public domain).

TowerInstruct-7B-v0.2 itself is under CC-BY-NC-4.0 ("NC" in "CC-BY-NC-4.0" means "**n**on-**c**ommercial" which is legally ambiguous),

but it is based on Llama 2 model which is licensed under the [LLAMA 2 Community License](https://ai.meta.com/llama/license/) (Copyright © Meta Platforms, Inc. All Rights Reserved.) whose TL;DR is you may not use it for bullying, military, and criminal activity.
