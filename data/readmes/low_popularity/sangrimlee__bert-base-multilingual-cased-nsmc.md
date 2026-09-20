---
language: ko
---

# BERT multilingual basecased finetuned with NSMC

This model is a fine-tune checkpoint of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased), fine-tuned on [NSMC(Naver Sentiment Movie Corpus)](https://github.com/e9t/nsmc).

## Usage

You can use this model directly with a pipeline for sentiment-analysis:

```python
>>> from transformers import pipeline
>>> classifier = pipeline(
    "sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc"
)
>>> classifier("흠...포스터보고 초딩영화줄....오버연기조차 가볍지 않구나.")
>>> classifier("액션이 없는데도 재미 있는 몇안되는 영화")

[{'label': 'negative', 'score': 0.9642567038536072}]
[{'label': 'positive', 'score': 0.9970554113388062}]
```
