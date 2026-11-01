---
license: apache-2.0
language:
- ko
---
# albert-small-kor-cross-encoder-v1
- albert-small-kor-v1 모델을 훈련시켜 cross-encoder로 파인튜닝한 모델
- This model was trained using [SentenceTransformers](https://sbert.net) [Cross-Encoder](https://www.sbert.net/examples/applications/cross-encoder/README.html) class.

# Training
- sts(10)-nli(3)-sts(10)-nli(3)-sts(10) 훈련 시킴 (**distil 훈련 없음**)
- STS : seed=111,epoch=10, lr=1e-4, eps=1e-6, warm_step=10%, max_seq_len=128, train_batch=128(small 모델=32) (albert 13m/7G) [훈련코드](https://github.com/kobongsoo/BERT/blob/master/sbert/cross-encoder/sbert-corossencoder-train-nli.ipynb) 
- NLI  훈련 : seed=111,epoch=3, lr=3e-5, eps=1e-8, warm_step=10%, max_seq_len=128, train_batch=64, eval_bath=64(albert 2h/7G) [훈련코드](https://github.com/kobongsoo/BERT/blob/master/sbert/cross-encoder/sbert-corossencoder-train-sts.ipynb) 
- [평가코드](https://github.com/kobongsoo/BERT/blob/master/sbert/cross-encoder/sbert-crossencoder-test3.ipynb),[테스트코드](https://github.com/kobongsoo/BERT/blob/master/sbert/cross-encoder/sbert-crossencoder-test.ipynb)

- 
|모델     |korsts|klue-sts|glue(stsb)|stsb_multi_mt(en)|
|:--------|------:|--------:|--------------:|------------:|
|**albert-small-kor-cross-encoder-v1**    |0.8455    |0.8526    |0.8513           |0.7976|
|klue-cross-encoder-v1    |0.8262    |0.8833    |0.8512           |0.7889|
|kpf-cross-encoder-v1    |0.8799    |0.9133    |0.8626           |0.8027|  

## Usage and Performance

Pre-trained models can be used like this:
```
from sentence_transformers import CrossEncoder
model = CrossEncoder('bongsoo/albert-small-kor-cross-encoder-v1')
scores = model.predict([('오늘 날씨가 좋다', '오늘 등산을 한다'), ('오늘 날씨가 흐리다', '오늘 비가 내린다')])
print(scores)
```
```
[0.45417202 0.6294121 ]
```

The model will predict scores for the pairs `('Sentence 1', 'Sentence 2')` and `('Sentence 3', 'Sentence 4')`.

You can use this model also without sentence_transformers and by just using Transformers ``AutoModel`` class