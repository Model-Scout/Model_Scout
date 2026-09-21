---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- transformers
language:
- ko
---

# leewaay/klue-roberta-large-klueSTS-cross

This is a [sentence-transformers](https://www.SBERT.net) model: A cross encoder trained with the pretrained [`klue/roberta-large`](https://huggingface.co/klue/roberta-large) model on the [KLUE STS dataset](https://huggingface.co/datasets/klue#sts) for sentence similarity tasks. It's specifically designed for direct evaluation of sentence pairs, making it highly effective for [Re-Ranking](https://www.sbert.net/examples/applications/retrieve_rerank/README.html) and [Augmented SBERT](https://www.sbert.net/examples/training/data_augmentation/README.html) for data labeling tasks aimed at enhancing SBERT.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```bash
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import CrossEncoder
pairs = [('Query', 'Paragraph1'), ('Query', 'Paragraph2') , ('Query', 'Paragraph3')]

model = CrossEncoder('leewaay/klue-roberta-large-klueSTS-cross')
scores = model.predict(pairs)
print(scores)
```

## Citing & Authors

[Wonseok Lee](https://github.com/leewaay)