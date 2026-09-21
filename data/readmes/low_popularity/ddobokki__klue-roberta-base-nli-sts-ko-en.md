---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers

---
한국어와 영어의 nli, sts데이터를 klue/roberta-base에 학습시킨 모델입니다.

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
query = ['그는 그녀를 좋아한다.']
sentences = ["he love her", "he hate her", '그녀는 그를 싫어한다.','attention is all you need']

emb1 = model.encode(query)
emb2 = model.encode(sentences)
print(cosine_similarity(emb1,emb2))
-> array([[0.62751913, 0.23996451, 0.30788696, 0.08123618]], dtype=float32)
```

