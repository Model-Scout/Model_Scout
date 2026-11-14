---
language:
- ko
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- transformers
---

## PwC-Embedding-expr

We trained the **PwC-Embedding-expr** model on top of the [multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct) embedding model.  
To enhance performance in Korean, we applied our curated augmentation to STS datasets and fine-tuned the E5 model using a carefully balanced ratio across datasets.

> ⚠️ This is an experimental model and is under continuous development.

### To-do
- [x] MTEB Leaderboard  
- [ ] Technical Report


## MTEB
PwC-Embedding_expr was evaluated on the Korean subset of MTEB.  
A leaderboard link will be added once it is published.

| Task             | PwC-Embedding_expr |
|------------------|--------------------|
| KLUE-STS         | 0.88               | 
| KLUE-TC          | 0.73               |
| Ko-StrategyQA    | 0.80               | 
| KorSTS           | 0.84               | 
| MIRACL-Reranking | 0.72               | 
| MIRACL-Retrieval | 0.65               |
| **Average**      | **0.77**           |


## Model
- Base Model: [intfloat/multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct)
- Model Size: 0.56B
- Embedding Dimension: 1024
- Max Input Tokens: 514


## Requirements
It works with the dependencies included in the latest version of MTEB.


## Citation

TBD (technical report expected September 2025)