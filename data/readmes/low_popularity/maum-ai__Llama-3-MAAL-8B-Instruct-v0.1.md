---
license: llama3
base_model:
- meta-llama/Meta-Llama-3-8B-Instruct
language:
- en
- ko
tags:
- facebook
- meta
- llama
- llama-3
- llama-3-ko
---
<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/646484cfb90150b2706df03b/BEOyMpnnY9VY2KXlc3V2F.png" width="20%"/>
<p>

# Llama-3-MAAL-8B-Instruct-v0.1
we release MAAL, Multilingual Adaptive Augmentation Language-model which comprises a groundbreaking fusion of multilingual capabilities and adaptive augmentation techniques. 

- **Developed by:** [maum.ai Brain NLP](https://maum-ai.github.io). Jaeyoon Jung, Jinjoo Lee, Yongjae Lee, Dongjun Lee, Woosung Joo
- **Language(s) (NLP):** Korean, English (currently, bilingual)

## Model Description

Version 0.1 uses cross-lingual training to transfer instruction-following capabilities from English to Korean.

- We Trained this model on an 8 H100-80G for 1 day with cross-lingual training dataset
- we recommend using the fixed system prompt for the model unless you fine-tune it
```
너는 마음에이아이의 챗봇 MAAL이다. 고객의 질문에 친절하게 답하여라.
```

## sample inference code (GPU)

```
import transformers
import torch

model_id = "maum-ai/Llama-3-MAAL-8B-Instruct-v0.1"
model = transformers.AutoModelForCausalLM.from_pretrained(model_id).to("cuda")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
streamer = transformers.TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

# we recommend using the fixed prompt for the model unless you fine-tune it
prompt = "너는 마음에이아이의 챗봇 MAAL이다. 고객의 질문에 친절하게 답하여라."
instruction = "사과 한 박스에는 사과가 30개 들어있는데, 처음에는 사과 3박스가 있었고, 내가 사과 5개를 먹었어. 남은 사과는 총 몇개야?"

messages = [
    {"role": "system", "content": f"{prompt}"},
    {"role": "user", "content": f"{instruction}"}
    ]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    return_tensors='pt').to("cuda")
outputs = model.generate(inputs, streamer=streamer, max_new_tokens=1024, pad_token_id=tokenizer.eos_token_id)
```

## Evaluation Results

As the main goal of version 0.1 is to **transfer instruction-following capabilities from English to Korean** without utilizing continuous pre-training, etc., we select [**LogicKor**](https://github.com/StableFluffy/LogicKor) as our evaluation method to assess the Korean instruction skills. 

We compare our model with a similar parameter model (less than 13B) that has been fine-tuned on the Korean dataset. \* denotes our self-report result.

|Model|single-turn(↑)|multi-turn(↑)|average(↑)|
|-|-|-|-|
|maum-ai/Llama-3-MAAL-8B-Instruct-v0.1*|**5.80**|4.66|**5.23**|
|maywell/Synatra-kiqu-10.7B|5.71|4.73|5.22|
|yanolja/EEVE-Korean-Instruct-10.8B-v1.0|5.78|3.92|4.85|
|nlpai-lab/KULLM3|4.61|**4.83**|4.72|
|MLP-KTLim/llama3-Bllossom*|2.11|1.57|1.84|

## Limitations
Due to this model being trained on a small dataset, it has several limitations.
- Hard to generate diverse Korean texts
- lack of Korean knowledge & Culture (localization)
- Not work with Image inputs and video inputs

## Todo
we will solve these limitations one by one by upgrading this model like as...
- Enhance the Korean generation through Vocabulary Expansion & Continuous pre-training. (more Korean corpus!)
- Localize with cultural adaptation method and additional Korean knowledge data. [*similar idea*](https://aclanthology.org/2023.emnlp-main.18/)
- Develop a Vision Language Model that can handle both video and image inputs. [*similar idea*](https://github.com/PKU-YuanGroup/Video-LLaVA)