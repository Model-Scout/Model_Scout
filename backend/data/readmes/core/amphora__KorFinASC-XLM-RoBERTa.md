---
language: ko        # <-- my language
widget:
 - text: "장 전체가 폭락한 가운데 삼성전자만 상승세를 이어갔다. </s> 삼성전자"
tags:
- XLM-RoBERTa
- KorFin-ASC
- financial-sentiment-analysis
- sentiment-analysis
license:
- apache-2.0
---
## KorFinASC-XLM-RoBERTa
Pretrained XLM-RoBERTA-Large transfered to the Finance domain on Korean Language.   
See [paper](https://arxiv.org/abs/2301.03136) for more details.

## Data
KorFinASC-XLM-RoBERTa is extensively trained on multiple datasets including KorFin-ASC, [Ko-FinSA](https://github.com/ukairia777/finance_sentiment_corpus), [Ko-ABSA](http://www.drbr.or.kr/datasets/view/?seq=20) and [ModuABSA](https://rlkujwkk7.toastcdn.net/73/NIKL_ABSA_2022_COMPETITION_v1.0.pdf).

## How to use.

```python
>>> from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

>>> tokenizer = AutoTokenizer.from_pretrained("amphora/KorFinASC-XLM-RoBERTa")
>>> model = AutoModelForSequenceClassification.from_pretrained("amphora/KorFinASC-XLM-RoBERTa")

>>> input_str = "장 전체가 폭락한 가운데 삼성전자만 상승세를 이어갔다. </s> 삼성전자"
>>> input = tokenizer(input_str, return_tensors='pt')
>>> output = model.generate(**input, max_length=20)

```
