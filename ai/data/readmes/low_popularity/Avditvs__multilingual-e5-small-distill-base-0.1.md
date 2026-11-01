---
tags:
- Sentence Transformers
- feature-extraction
- sentence-similarity
- sentence-transformers
language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
license: mit
---

## Multilingual-E5-small-distill-base

This model is an attempt to distill `intfloat/multilingual-e5-base` (teacher) into `intfloat/multilingual-e5-small` (student),
as well as applying [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147) to it.

This was made by trying an L2 loss to teach the student model to match the same cosine similarity on text pairs as the teacher model.

The distillation dataset is composed of about 700k multilingual sentences pairs sampled for the following 3 datasets:
- [PhilipMay/stsb_multi_mt](https://huggingface.co/datasets/PhilipMay/stsb_multi_mt)
- [castorini/mr-tydi](https://huggingface.co/datasets/castorini/mr-tydi)
- [quora](https://huggingface.co/datasets/quora)

For code, see [this github repository](https://github.com/Avditvs/matryoshka_factory)


[Multilingual E5 Text Embeddings: A Technical Report](https://arxiv.org/pdf/2402.05672).
Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei, arXiv 2024

This model has 12 layers and the embedding size is 384.

## Usage

Below is an example to encode queries and passages from the MS-MARCO passage ranking dataset.

```python
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


# Each input text should start with "query: " or "passage: ", even for non-English texts.
# For tasks other than retrieval, you can simply use the "query: " prefix.
input_texts = ['query: how much protein should a female eat',
               'query: 南瓜的家常做法',
               "passage: As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
               "passage: 1.清炒南瓜丝 原料:嫩南瓜半个 调料:葱、盐、白糖、鸡精 做法: 1、南瓜用刀薄薄的削去表面一层皮,用勺子刮去瓤 2、擦成细丝(没有擦菜板就用刀慢慢切成细丝) 3、锅烧热放油,入葱花煸出香味 4、入南瓜丝快速翻炒一分钟左右,放盐、一点白糖和鸡精调味出锅 2.香葱炒南瓜 原料:南瓜1只 调料:香葱、蒜末、橄榄油、盐 做法: 1、将南瓜去皮,切成片 2、油锅8成热后,将蒜末放入爆香 3、爆香后,将南瓜片放入,翻炒 4、在翻炒的同时,可以不时地往锅里加水,但不要太多 5、放入盐,炒匀 6、南瓜差不多软和绵了之后,就可以关火 7、撒入香葱,即可出锅"]

tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-small')
model = AutoModel.from_pretrained('intfloat/multilingual-e5-small')

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
```

## Supported Languages

This model is initialized from [microsoft/Multilingual-MiniLM-L12-H384](https://huggingface.co/microsoft/Multilingual-MiniLM-L12-H384)
and continually trained on a mixture of multilingual datasets.
It supports 100 languages from xlm-roberta,
but low-resource languages may see performance degradation.

## MTEB Benchmark Evaluation (Subset)

|                             | intfloat/multilingual-e5-base | intfloat/multilingual-e5-large | intfloat/multilingual-e5-small | avditvs/multilingual-e5-small-distill-base-0.1 |
| --------------------------- | ----------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------------------- |
| STS15                       | 0.876                         | 0.882                          | 0.864                          | 0.865                                                |
| BIOSSES                     | 0.870                         | 0.863                          | 0.857                          | 0.863                                                |
| STS14                       | 0.789                         | 0.776                          | 0.788                          | 0.803                                                |
| STS12                       | 0.858                         | 0.873                          | 0.854                          | 0.856                                                |
| AskUbuntuDupQuestions       | 0.571                         | 0.577                          | 0.568                          | 0.574                                                |
| StackOverflowDupQuestions   | 0.485                         | 0.486                          | 0.486                          | 0.485                                                |
| AmazonReviewsClassification | 0.476                         | 0.470                          | 0.452                          | 0.450                                                |
| ArguAna                     | 0.442                         | 0.544                          | 0.391                          | 0.480                                                |
| ImdbClassification          | 0.849                         | 0.887                          | 0.758                          | 0.757                                                |
| STS13                       | 0.756                         | 0.751                          | 0.764                          | 0.785                                                |
| STSBenchmark                | 0.832                         | 0.836                          | 0.809                          | 0.818                                                |
| STS17                       | 0.890                         | 0.896                          | 0.868                          | 0.871                                                |
| SICK-R                      | 0.835                         | 0.838                          | 0.835                          | 0.850                                                |
| STS22                       | 0.645                         | 0.675                          | 0.640                          | 0.648                                                |
| STS16                       | 0.814                         | 0.824                          | 0.822                          | 0.820                                                |
| Banking77Classification     | 0.741                         | 0.749                          | 0.706                          | 0.706                                                |
| average                     | 0.733                         | 0.745                          | *0.717*                        | **0.727**                                            |



## Support for Sentence Transformers

Below is an example for usage with sentence_transformers.
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('avditvs/multilingual-e5-small-distill-base')
input_texts = [
    'query: how much protein should a female eat',
    'query: 南瓜的家常做法',
    "passage: As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 i     s 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or traini     ng for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "passage: 1.清炒南瓜丝 原料:嫩南瓜半个 调料:葱、盐、白糖、鸡精 做法: 1、南瓜用刀薄薄的削去表面一层皮     ,用勺子刮去瓤 2、擦成细丝(没有擦菜板就用刀慢慢切成细丝) 3、锅烧热放油,入葱花煸出香味 4、入南瓜丝快速翻炒一分钟左右,     放盐、一点白糖和鸡精调味出锅 2.香葱炒南瓜 原料:南瓜1只 调料:香葱、蒜末、橄榄油、盐 做法: 1、将南瓜去皮,切成片 2、油     锅8成热后,将蒜末放入爆香 3、爆香后,将南瓜片放入,翻炒 4、在翻炒的同时,可以不时地往锅里加水,但不要太多 5、放入盐,炒匀      6、南瓜差不多软和绵了之后,就可以关火 7、撒入香葱,即可出锅"
]
embeddings = model.encode(input_texts, normalize_embeddings=True)
```

Package requirements

`pip install sentence_transformers~=2.2.2`

Contributors: [michaelfeil](https://huggingface.co/michaelfeil)

## FAQ

**1. Do I need to add the prefix "query: " and "passage: " to input texts?**

Yes, this is how the model is trained, otherwise you will see a performance degradation.

Here are some rules of thumb:
- Use "query: " and "passage: " correspondingly for asymmetric tasks such as passage retrieval in open QA, ad-hoc information retrieval.

- Use "query: " prefix for symmetric tasks such as semantic similarity, bitext mining, paraphrase retrieval.

- Use "query: " prefix if you want to use embeddings as features, such as linear probing classification, clustering.

**2. Why are my reproduced results slightly different from reported in the model card?**

Different versions of `transformers` and `pytorch` could cause negligible but non-zero performance differences.

**3. Why does the cosine similarity scores distribute around 0.7 to 1.0?**

This is a known and expected behavior as we use a low temperature 0.01 for InfoNCE contrastive loss. 

For text embedding tasks like text retrieval or semantic similarity, 
what matters is the relative order of the scores instead of the absolute values, 
so this should not be an issue.

## Citation

If you find our paper or models helpful, please consider cite as follows:

```
@article{wang2024multilingual,
  title={Multilingual E5 Text Embeddings: A Technical Report},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2402.05672},
  year={2024}
}
```

## Limitations

Long texts will be truncated to at most 512 tokens.
