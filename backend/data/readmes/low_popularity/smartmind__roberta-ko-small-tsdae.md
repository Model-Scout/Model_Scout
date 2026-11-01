---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
language:
- ko
license:
- mit
widget:
  source_sentence: "대한민국의 수도는 서울입니다."
  sentences:
    - "미국의 수도는 뉴욕이 아닙니다."
    - "대한민국의 수도 요금은 저렴한 편입니다."
    - "서울은 대한민국의 수도입니다."
---

# smartmind/roberta-ko-small-tsdae

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 256 dimensional dense vector space and can be used for tasks like clustering or semantic search.

Korean roberta small model pretrained with [TSDAE](https://arxiv.org/abs/2104.06979).

[TSDAE](https://arxiv.org/abs/2104.06979)로 사전학습된 한국어 roberta모델입니다. 모델의 구조는 [lassl/roberta-ko-small](https://huggingface.co/lassl/roberta-ko-small)과 동일합니다. 토크나이저는 다릅니다.

sentence-similarity를 구하는 용도로 바로 사용할 수도 있고, 목적에 맞게 파인튜닝하여 사용할 수도 있습니다.

## Usage (Sentence-Transformers)

[sentence-transformers](https://www.SBERT.net)를 설치한 뒤, 모델을 바로 불러올 수 있습니다.

```
pip install -U sentence-transformers
```

이후 다음처럼 모델을 사용할 수 있습니다.

```python
from sentence_transformers import SentenceTransformer

sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('smartmind/roberta-ko-small-tsdae')
embeddings = model.encode(sentences)
print(embeddings)
```

다음은 sentence-transformers의 기능을 사용하여 여러 문장의 유사도를 구하는 예시입니다.

```python
from sentence_transformers import util

sentences = [
    "대한민국의 수도는 서울입니다.",
    "미국의 수도는 뉴욕이 아닙니다.",
    "대한민국의 수도 요금은 저렴한 편입니다.",
    "서울은 대한민국의 수도입니다.",
    "오늘 서울은 하루종일 맑음",
]

paraphrase = util.paraphrase_mining(model, sentences)
for score, i, j in paraphrase:
    print(f"{sentences[i]}\t\t{sentences[j]}\t\t{score:.4f}")
```

```
대한민국의 수도는 서울입니다.		서울은 대한민국의 수도입니다.		0.7616
대한민국의 수도는 서울입니다.		미국의 수도는 뉴욕이 아닙니다.		0.7031
대한민국의 수도는 서울입니다.		대한민국의 수도 요금은 저렴한 편입니다.		0.6594
미국의 수도는 뉴욕이 아닙니다.		서울은 대한민국의 수도입니다.		0.6445
대한민국의 수도 요금은 저렴한 편입니다.		서울은 대한민국의 수도입니다.		0.4915
미국의 수도는 뉴욕이 아닙니다.		대한민국의 수도 요금은 저렴한 편입니다.		0.4785
서울은 대한민국의 수도입니다.		오늘 서울은 하루종일 맑음		0.4119
대한민국의 수도는 서울입니다.		오늘 서울은 하루종일 맑음		0.3520
미국의 수도는 뉴욕이 아닙니다.		오늘 서울은 하루종일 맑음		0.2550
대한민국의 수도 요금은 저렴한 편입니다.		오늘 서울은 하루종일 맑음		0.1896
```


## Usage (HuggingFace Transformers)

[sentence-transformers](https://www.SBERT.net)를 설치하지 않은 상태로는 다음처럼 사용할 수 있습니다.

```python
from transformers import AutoTokenizer, AutoModel
import torch


def cls_pooling(model_output, attention_mask):
    return model_output[0][:,0]


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('smartmind/roberta-ko-small-tsdae')
model = AutoModel.from_pretrained('smartmind/roberta-ko-small-tsdae')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, cls pooling.
sentence_embeddings = cls_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```



## Evaluation Results

[klue](https://huggingface.co/datasets/klue) STS 데이터에 대해 다음 점수를 얻었습니다. 이 데이터에 대해 파인튜닝하지 **않은** 상태로 구한 점수입니다.

|split|cosine_pearson|cosine_spearman|euclidean_pearson|euclidean_spearman|manhattan_pearson|manhattan_spearman|dot_pearson|dot_spearman|
|-----|--------------|---------------|-----------------|------------------|-----------------|------------------|-----------|------------|
|train|0.8735|0.8676|0.8268|0.8357|0.8248|0.8336|0.8449|0.8383|
|validation|0.5409|0.5349|0.4786|0.4657|0.4775|0.4625|0.5284|0.5252|


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 508, 'do_lower_case': False}) with Transformer model: RobertaModel
  (1): Pooling({'word_embedding_dimension': 256, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
