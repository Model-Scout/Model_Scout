---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- ko
---

# ddobokki/unsup-simcse-klue-roberta-small

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('ddobokki/unsup-simcse-klue-roberta-small')
embeddings = model.encode(sentences)
print(embeddings)
```
(개발중)
git:https://github.com/ddobokki/KoSimCSE
