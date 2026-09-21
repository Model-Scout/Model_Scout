---
license: mit
datasets:
- g0ster/TinyStories-Korean
language:
- ko
library_name: transformers
---

# Update 2025-05-31

Also try:  
https://huggingface.co/north-wind/Experimental-Neo-TinyStories-Korean-800K-20240819  
https://huggingface.co/datasets/north-wind/ko-TinyStories

# TinyStories-Korean-800K

A tiny autoregressive language model trained from scratch.

- Architecture: Llama
- Vocab size: 4096
- Hidden size: 64
- Layers: 5
- Heads: 8 (MHA)
- Context length: up to 512 tokens

## Note

This model was trained for experimental purposes and the generated output may not make any sense at all.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained('northwind33/TinyStories-Korean-800K')
tokenizer = AutoTokenizer.from_pretrained('northwind33/TinyStories-Korean-800K')

input_text = ''
input_ids = tokenizer(input_text, return_tensors='pt').input_ids

output = model.generate(input_ids, max_length=512, do_sample=True, temperature=0.5)
```