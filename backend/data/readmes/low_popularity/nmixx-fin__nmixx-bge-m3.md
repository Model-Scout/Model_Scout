---
license: apache-2.0
base_model: BAAI/bge-m3
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- Korean
- financial-nlp
- nmixx
- multilingual
language:
- ko
- en
datasets:
- nmixx-fin/NMIXX_train
pipeline_tag: sentence-similarity
---

# NMIXX-BGE-M3

![Model Image](./finance.png)

This repository contains a bge-m3-based SentenceTransformer model fine-tuned with a triplet-loss setup on the `nmixx-fin/NMIXX_train` dataset. It produces high-quality sentence embeddings for Korean financial text with multilingual capabilities, optimized for semantic similarity tasks in the finance domain.

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# 1. Load tokenizer & model from Hugging Face Hub
repo_name = "nmixx-fin/nmixx-bge-m3"
tokenizer = AutoTokenizer.from_pretrained(repo_name)
model = AutoModel.from_pretrained(repo_name)

# 2. Move to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# 3. Prepare input sentences
sentences = [
    "이 모델은 한국 금융 도메인에 특화된 다국어 임베딩을 제공합니다.",
    "NMIXX 데이터셋으로 fine-tuning된 multilingual sentence transformer입니다."
]

# 4. Tokenize
encoded_input = tokenizer(
    sentences,
    padding=True,
    truncation=True,
    max_length=8192,  # BGE-M3 supports longer sequences
    return_tensors="pt"
)
input_ids = encoded_input["input_ids"].to(device)
attention_mask = encoded_input["attention_mask"].to(device)

# 5. Forward pass (token embeddings)
with torch.no_grad():
    model_output = model(input_ids=input_ids, attention_mask=attention_mask)

# 6. CLS Pooling (BGE models use CLS token)
sentence_embeddings = model_output[0][:, 0]  # Use CLS token (first token)

# 7. L2 Normalization
sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

print("Sentence embeddings shape:", sentence_embeddings.shape)
print(sentence_embeddings.cpu())
```

## Features

- **Multilingual Support**: Based on BGE-M3, supporting Korean and English
- **Extended Sequence Length**: Supports up to 8192 tokens
- **Korean Financial Domain**: Fine-tuned specifically for Korean financial text
- **High Performance**: Optimized for semantic similarity tasks in finance

## Model Details

- **Base Model**: BAAI/bge-m3
- **Fine-tuning Dataset**: nmixx-fin/NMIXX_train
- **Training Method**: Triplet loss with hard negative mining
- **Embedding Dimension**: 1024
- **Max Sequence Length**: 8192 tokens (Stable performance can only be guaranteed up to 2048 tokens)

> ⚠️ **Developer's Note:** 이거 금융 STS 말고 잘하는 거 없습니다.

```bibtex
@article{lee2025nmixxdomainadaptedneuralembeddings,
  title        = {NMIXX: Domain-Adapted Neural Embeddings for Cross-Lingual eXploration of Finance},
  author       = {Hanwool Lee and Sara Yu and Yewon Hwang and Jonghyun Choi and Heejae Ahn and Sungbum Jung and Youngjae Yu},
  year         = {2025},
  eprint       = {2507.09601},
  archivePrefix= {arXiv},
  primaryClass = {cs.CL},
  url          = {https://arxiv.org/abs/2507.09601},
}
```