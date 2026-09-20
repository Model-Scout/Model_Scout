---
license: cc-by-nc-4.0
language:
- ar
- bn
- zh
- en
- fi
- fr
- de
- hi
- id
- it
- ja
- ko
- fa
- pt
- ru
- es
- sw
- te
- th
- yo
pipeline_tag: sentence-similarity
library_name: transformers
tags:
- sentence-transformers
---

# DRAMA-large (0.3B): Diverse Augmentation from Large Language Models to Smaller Dense Retrievers

DRAMA-large (0.3B) is a dense retrieval model built upon a pruned large language model backbone. It is derived by pruning a large language model and fine-tuned for efficient and generalizable multilingual text retrieval.
By leveraging large language models for high-quality data augmentation, DRAMA-large achieves strong performance across both English and multilingual retrieval tasks, despite its compact size of 0.3B non-embedding parameters.

The default embedding size of `drama-large` is 1024, as we adopt Matryoshka Representation Learning, the dimionality can be flexiblely truncated to dimensionalities such as 512 or 256.

Please check our [paper](https://arxiv.org/abs/2502.18460) for the detials.

## Usage

Below is an example using `drama-base` to encode query and document examples from the MIRACL dataset, using either Transformers or Sentence Transformers:

### Transformers

```python
import torch
from transformers import AutoTokenizer, AutoModel


queries = [
    'What percentage of the Earth\'s atmosphere is oxygen?',
    '意大利首都是哪里？',
]
documents = [
    "The amount of oxygen in the atmosphere has fluctuated over the last 600 million years, reaching a peak of 35% during the Carboniferous period, significantly higher than today's 21%.",
    "羅馬是欧洲国家意大利首都和罗马首都广域市的首府及意大利全国的政治、经济、文化和交通中心，位于意大利半島中部的台伯河下游平原地，建城初期在七座小山丘上，故又名“七丘之城”。按城市范围内的人口计算，罗马是意大利人口最多的城市，也是欧盟人口第三多的城市。",
]

model_name = "facebook/drama-large"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True).to(device)

query_embs = model.encode_queries(tokenizer, queries)
doc_embs = model.encode_documents(tokenizer, documents)

scores = query_embs @ doc_embs.T
print(scores.tolist())
# Expected output: [[0.5429, 0.1109], [0.1317, 0.6074]]
```

> The `trust_remote_code` will use our customized `drama_modeling.py` with two details:
>- We use bi-directional attention instead of uni-directional attention
>- We add `"Query: "` as prefix for query text. (No prefix added to document)


DRAMA models are trained using Matryoshka Representation Learning ([MRL](https://github.com/RAIVNLab/MRL)) to support flexible dimensionality. Both queries and documents can be encoded into smaller dimensions, such as 256, using the following:
```python
query_embs = model.encode_queries(tokenizer, queries, dim=256)
doc_embs = model.encode_documents(tokenizer, documents, dim=256)

scores = query_embs @ doc_embs.T
print(scores.tolist())
# Expected output: [[0.6239, 0.2294], [0.2604, 0.6942]]
```

### Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

queries = [
    'What percentage of the Earth\'s atmosphere is oxygen?',
    '意大利首都是哪里？',
]
documents = [
    "The amount of oxygen in the atmosphere has fluctuated over the last 600 million years, reaching a peak of 35% during the Carboniferous period, significantly higher than today's 21%.",
    "羅馬是欧洲国家意大利首都和罗马首都广域市的首府及意大利全国的政治、经济、文化和交通中心，位于意大利半島中部的台伯河下游平原地，建城初期在七座小山丘上，故又名“七丘之城”。按城市范围内的人口计算，罗马是意大利人口最多的城市，也是欧盟人口第三多的城市。",
]

model = SentenceTransformer("facebook/drama-large", trust_remote_code=True)

query_embs = model.encode(queries, prompt_name="query")
doc_embs = model.encode(documents)

scores = model.similarity(query_embs, doc_embs)
print(scores.tolist())
# Expected output: [[0.5429, 0.1109], [0.1317, 0.6074]]
```

>- The `trust_remote_code` will use our customized `drama_modeling.py` which uses bi-directional attention instead of uni-directional attention.
>- For queries, you have to use `prompt_name="query"` to select the [prompt called "query"](config_sentence_transformers.json), or `prompt="Query: "` to specify the prompt string manually.

DRAMA models are trained using Matryoshka Representation Learning ([MRL](https://github.com/RAIVNLab/MRL)) to support flexible dimensionality. Both queries and documents can be encoded into smaller dimensions, such as 256, using the following:

```python
from sentence_transformers import SentenceTransformer

queries = [
    'What percentage of the Earth\'s atmosphere is oxygen?',
    '意大利首都是哪里？',
]
documents = [
    "The amount of oxygen in the atmosphere has fluctuated over the last 600 million years, reaching a peak of 35% during the Carboniferous period, significantly higher than today's 21%.",
    "羅馬是欧洲国家意大利首都和罗马首都广域市的首府及意大利全国的政治、经济、文化和交通中心，位于意大利半島中部的台伯河下游平原地，建城初期在七座小山丘上，故又名“七丘之城”。按城市范围内的人口计算，罗马是意大利人口最多的城市，也是欧盟人口第三多的城市。",
]

model = SentenceTransformer("facebook/drama-large", truncate_dim=256, trust_remote_code=True)

query_embs = model.encode(queries, prompt_name="query")
doc_embs = model.encode(documents)

scores = model.similarity(query_embs, doc_embs)
print(scores.tolist())
# Expected output: [[0.6239, 0.2294], [0.2604, 0.6942]]
```


## Evaluation

The model has been evaluated on multiple retrieval benchmarks, including [BEIR](https://github.com/beir-cellar/beir), [MIRACL](https://github.com/project-miracl/miracl), [MLDR](https://huggingface.co/datasets/Shitao/MLDR), and several multilingual retrieval tasks in [MTEB](https://github.com/embeddings-benchmark/mteb).
It demonstrates strong performance in both English and multilingual retrieval tasks.

<p align="center">
  <img src="evaluation.png" style="width:800px;">
</p>

`drama-large` released in this page is corresponidng to the line DRAMA-0.3B with 265M non-embedding parrameters.

## Supported Languages
DRAMA-large was initialized from [Llama3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) (which was originally pruned from [Llama3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B)). During pruning and retriever training, training data covered the following 20 languages (sorted alphabetically):

`Arabic, Bengali, Chinese, English, Finnish, French, German, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Portuguese, Russian, Spanish, Swahili, Telugu, Thai, Yoruba`

Other languages may have downgraded peformance.

## Citation
If you find our paper or models helpful, please consider cite as follows:

```
@article{drama,
  title={{Drama}: Diverse Augmentation from Large Language Models To Smaller Dense Retrievers},
  author={Ma, Xueguang and Lin, Victoria Xi and Oguz, Barlas and Lin, Jimmy and Yih, Wen-tau and Chen, Xilun},
  journal={arXiv:2502.18460},
  year={2025}
}
```
