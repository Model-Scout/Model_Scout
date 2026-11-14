---
language:
  - en
  - es
  - zh
  - ko
license: mit
base_model: xlm-roberta-base
tags:
  - sentiment
  - text-classification
  - multilingual
metrics:
  - accuracy
  - f1
---

# XLM-R Sentiment 3-class (En/Es/Zh/Ko)

Phân loại cảm xúc thành 3 nhãn: **positive / neutral / negative** cho 4 ngôn ngữ Anh, Tây Ban Nha, Trung, Hàn.

## Usage
```python
from transformers import pipeline
clf = pipeline("text-classification", model="anphu16-do-huu/xlmr-sentiment-en-es-zh-ko")
print(clf("I love this product!"))
```

## Training details
- Base model: `xlm-roberta-base`
- Hyperparameters: lr=8e-06, epochs=15, batch=32, max_len=128
- Hardware: NVIDIA T4 (Google Colab Free), fp16

## Labels
- 0: negative
- 1: neutral
- 2: positive
