---
license: mit
language:
- ko
base_model:
- paust/pko-t5-base
pipeline_tag: translation
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
영어-한국어 번역 모델입니다.

### Model Description

<!-- Provide a longer summary of what this model is. -->
paust/pko-t5-base 모델을 기반으로 영어-한국어 번역을 미세조정한 번역 모델입니다.
영어->한국어, 한국어->영어 양방향 번역을 지원하며, 영어->한국어 번역 시 높임말도
설정할 수 있습니다.


- **Developed by:** [BlueAI]
- **Model type:** [t5.1.1.base]
- **Language(s) (NLP):** [Korean]
- **License:** [MIT]
- **Finetuned from model [optional]:** [paust/pko-t5-base]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import pipeline, T5TokenizerFast

tokenizer_name = "paust/pko-t5-base"
tokenizer = T5TokenizerFast.from_pretrained(tokenizer_name)
model_path = 'Darong/BlueT'
translator = pipeline("translation", model=model_path, tokenizer=tokenizer, max_length=255)
# 영어 -> 한국어
prefix = "E2K: "
source = "This model is an English-Korean translation model."
target = translator(prefix + source)
print(target[0]['translation_text'])

# 한국어->영어
prefix = "K2E: "
source = "이 모델은 영어-한국어 번역 모델입니다."
target = translator(prefix + source)
print(target[0]['translation_text'])
```

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

이 모델은 AI Hub 및 자체 구축한 데이터로 학습되었습니다.
영어->한국어 학습 데이터 수는 1800만 이상, 한국어->영어 학습 데이터 수는 1200만 이상의 문장으로 구축되었습니다.

