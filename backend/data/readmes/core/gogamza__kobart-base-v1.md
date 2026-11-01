---
language: ko
tags:
- bart
license: mit
---

## KoBART-base-v1


```python
from transformers import PreTrainedTokenizerFast, BartModel

tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v1')
model = BartModel.from_pretrained('gogamza/kobart-base-v1')
```

