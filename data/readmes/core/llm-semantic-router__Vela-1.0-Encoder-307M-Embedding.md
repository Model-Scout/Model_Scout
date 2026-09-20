---
library_name: sentence-transformers
license: apache-2.0
pipeline_tag: sentence-similarity
base_model: llm-semantic-router/Vela-1.0-Encoder-307M
base_model_relation: finetune
language:
- en
- ar
- es
- ja
- zh
tags:
- modernbert
- semantic-router
- vela
- matryoshka
---

<div align="center">
  <img src="https://vllm-sr.ai/img/vllm-sr-logo.social.png" alt="vLLM Semantic Router" width="560" />
  <p>
    <a href="https://vllm-sr.ai/"><strong>Docs</strong></a> |
    <a href="https://vllm-sr.ai/blog/"><strong>Blog</strong></a> |
    <a href="https://vllm-dev.slack.com/archives/C09CTGF8KCN"><strong>Slack</strong></a> |
    <a href="https://github.com/vllm-project/semantic-router"><strong>GitHub</strong></a>
  </p>
</div>

# Vela Embedding

Connect requests with the right context. Vela Embedding powers multilingual semantic matching, retrieval, and memory in your router.

**307M parameters · 32K context · Multilingual**

## Evaluation

Compared with [the original mmBERT Embedding](https://huggingface.co/llm-semantic-router/mmbert-embed-32k-2d-matryoshka). Scores are ×100; higher is better.

Selected tasks from MTEB 2.21.0:

| Task | Original mmBERT | Vela |
|---|---:|---:|
| Banking77 | 72.26 | **74.04** |
| MASSIVE · English | 63.51 | **68.12** |
| MASSIVE · Chinese | 61.41 | **66.08** |
| DuRetrieval | 62.47 | **62.99** |
| NFCorpus | 26.38 | 26.13 |
| SciFact | 46.81 | **48.28** |
| PAWS-X · English | 62.98 | **71.74** |
| PAWS-X · Chinese | 59.29 | **62.82** |
| STS-B · Chinese | 75.00 | 74.73 |
| STS-B · English | 80.38 | **81.19** |
| CLS Clustering | 34.20 | **34.87** |
| Twenty Newsgroups Clustering | 38.05 | **38.53** |
| Tatoeba · Chinese–English | 89.13 | 89.12 |

Long-document retrieval:

| Evaluation | Metric | Original mmBERT | Vela |
|---|---|---:|---:|
| SummScreenFD · 336 queries | nDCG@10 | 76.99 | **88.36** |

Both models use 22 layers, 768 dimensions and FP32. The MTEB rows use each task's standard main metric; SummScreenFD uses its validation split.

These results describe the listed tasks, not a full MTEB score or ranking.

## Quick start

Install `sentence-transformers`. Use a ROCm-enabled PyTorch build for AMD GPUs.

```python
import torch
from sentence_transformers import SentenceTransformer

model_id = "llm-semantic-router/Vela-1.0-Encoder-307M-Embedding"
device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer(model_id, device=device)
vectors = model.encode([
    "The library opens in the morning.",
    "图书馆早上开门。",
])
print(vectors.shape)  # (2, 768)
```

The default returns 768-dimensional unit vectors. The 32,768-token input limit includes special tokens.

[Explore the Vela collection](https://huggingface.co/collections/llm-semantic-router/vela-10-router-models-6aa555ba70cc6997d6d67798)
