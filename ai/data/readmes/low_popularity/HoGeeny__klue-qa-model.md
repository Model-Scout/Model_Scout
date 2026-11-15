---
language: ko
license: cc-by-sa-4.0
pipeline_tag: question-answering
tags:
  - klue
  - question-answering
  - gradio
base_model: klue/bert-base
datasets:
  - klue/klue
---

# KLUE QA (Extractive Question Answering)

`klue/bert-base`를 **KLUE-MRC**로 파인튜닝한 한국어 Extractive QA 모델입니다.

---

## How to use (Transformers)
```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

MODEL_ID = "HoGeeny/klue-qa-model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForQuestionAnswering.from_pretrained(MODEL_ID)
```

### Intended use
- 입력된 지문(context) 안에서 정답 span을 추출합니다.

### Limitations
- 지문에 없는 정보는 답하지 못합니다.
- 긴 지문은 잘릴 수 있습니다(max_length=512).

### Training data
- KLUE-MRC (from klue/klue)

### License & Attribution
- Base model: klue/bert-base
- Dataset: klue/klue (KLUE-MRC)
