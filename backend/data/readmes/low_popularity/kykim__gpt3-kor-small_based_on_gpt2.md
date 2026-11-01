---
language: ko
tags:
- text-generation
---

# Bert base model for Korean

* 70GB Korean text dataset and 42000 lower-cased subwords are used
* Check the model performance and other language models for Korean in [github](https://github.com/kiyoungkim1/LM-kor)

```python
from transformers import BertTokenizerFast, GPT2LMHeadModel
tokenizer_gpt3 = BertTokenizerFast.from_pretrained("kykim/gpt3-kor-small_based_on_gpt2")
input_ids = tokenizer_gpt3.encode("text to tokenize")[1:]  # remove cls token
        
model_gpt3 = GPT2LMHeadModel.from_pretrained("kykim/gpt3-kor-small_based_on_gpt2")
```