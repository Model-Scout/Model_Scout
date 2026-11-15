---
license: [apache-2.0, gemma]
datasets:
- traintogpb/aihub-koen-translation-integrated-base-10m
language:
- ko
- en
pipeline_tag: translation
tags:
- gemma
widget:
- text: "Korean:\n나라의 말이 중국과 달라 문자와 서로 통하지 아니하다.\n\nEnglish:\n"
  example_title: "K2E"
- text: "English:\nMr. and Mrs. Dursley were proud to say that they were perfectly normal.\n\nKorean:\n"
  example_title: "E2K"
inference:
  parameters:
    max_length: 200
---
# Gemago 2B Model Card

**Original Gemma Model Page**: [Gemma](https://ai.google.dev/gemma/docs)

**Model Page On Github**: [Gemago](https://github.com/deveworld/Gemago)

**Resources and Technical Documentation**:
* [Blog(Korean)](https://blog.worldsw.dev/tag/gemago/)
* [Original Google's Gemma-2B](https://huggingface.co/google/gemma-2b)
* [Training Code @ Github: Gemma-EasyLM (Orginial by Beomi)](https://github.com/deveworld/Gemma-EasyLM/tree/2b)

**Terms of Use**: [Terms](https://www.kaggle.com/models/google/gemma/license/consent)

**Authors**: Orginal Google, Fine-tuned by DevWorld

## Model Information

Translate English/Korean to Korean/English.

### Description

Gemago is a lightweight English-and-Korean translation model based on Gemma.

### Context Length
Models are trained on a context length of 8192 tokens, which is equivalent to Gemma.

### Usage

Below we share some code snippets on how to get quickly started with running the model. First make sure to `pip install -U transformers`, then copy the snippet from the section that is relevant for your usecase.

#### Running the model with transformers
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deveworld/Gemago/blob/main/Gemago_2b_Infer.ipynb)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("devworld/gemago-2b")
model = AutoModelForCausalLM.from_pretrained("devworld/gemago-2b")

def gen(text, max_length):
    input_ids = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**input_ids, max_length=max_length)
    return tokenizer.decode(outputs[0])

def e2k(e):
    input_text = f"English:\n{e}\n\nKorean:\n"
    return gen(input_text, 1024)

def k2e(k):
    input_text = f"Korean:\n{k}\n\nEnglish:\n"
    return gen(input_text, 1024)
```