---
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
tags:
- liquid
- lfm2
- edge
- ColBERT
- PyLate
- sentence-transformers
- sentence-similarity
- feature-extraction
- llama.cpp
- gguf
pipeline_tag: sentence-similarity
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
- LiquidAI/LFM2-ColBERT-350M
new_version: LiquidAI/LFM2.5-ColBERT-350M-GGUF
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
  <a href="https://playground.liquid.ai/chat">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a></a>
</div>
</center>

# LFM2-ColBERT-350M

LFM2-ColBERT-350M is a late interaction retriever with excellent multilingual performance. It allows you to store documents in one language (for example, a product description in English) and retrieve them in many languages with high accuracy.

- LFM2-ColBERT-350M offers **best-in-class accuracy** across different languages.
- Inference speed is **on par with models 2.3 times smaller**, thanks to the efficient LFM2 backbone.
- You can use it as a **drop-in replacement** in your current RAG pipelines to improve performance.

Find more information about LFM2-ColBERT-350M in our [blog post](http://www.liquid.ai/blog/lfm2-colbert-350m-one-model-to-embed-them-all).


> [!NOTE]
> 🚀 Try our demo: https://huggingface.co/spaces/LiquidAI/LFM2-ColBERT

## 🏃 How to run

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

Start llama-server
```bash
llama-server -hf LiquidAI/LFM2-ColBERT-350M-GGUF --embeddings
```

Make requests to embed queries and documents, and compute similarity scores

```bash
❯ uv run colbert-rerank.py

Score: 29.69 | Q: What is panda? | D: hi
Score: 29.83 | Q: What is panda? | D: it is a bear
Score: 30.47 | Q: What is panda? | D: The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.
```

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "transformers",
#     "huggingface-hub",
#     "numpy",
#     "requests",
#     "torch",
# ]
# ///

# colbert-rerank.py
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download
import numpy as np, requests, torch, torch.nn.functional as F, json


model_id = "LiquidAI/LFM2-ColBert-350M"
tokenizer = AutoTokenizer.from_pretrained(model_id)
config = json.load(open(hf_hub_download(model_id, "config_sentence_transformers.json")))
skiplist = set(
    t
    for w in config["skiplist_words"]
    for t in tokenizer.encode(w, add_special_tokens=False)
)


def maxsim(q, d):
    return (q @ d.T).max(dim=1).values.sum().item()


def preprocess(text, is_query):
    prefix = config["query_prefix"] if is_query else config["document_prefix"]
    toks = tokenizer.encode(prefix + text)
    max_len = config["query_length"] if is_query else config["document_length"]
    if is_query:
        toks += [tokenizer.pad_token_id] * (max_len - len(toks))
    else:
        toks = toks[:max_len]
    mask = None if is_query else [t not in skiplist for t in toks]
    return toks, mask


def embed(content, mask=None):
    emb = np.array(
        requests.post(
            "http://localhost:8080/embedding",
            json={"content": content},
        ).json()[0]["embedding"]
    )
    if mask:
        emb = emb[mask]
    emb = torch.from_numpy(emb)
    emb = F.normalize(emb, p=2, dim=-1)  # L2 normalize each token embedding
    return emb.unsqueeze(0)


docs = [
    "hi",
    "it is a bear",
    "The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.",
]
query = "What is panda?"

q = embed(*preprocess(query, True))
d = [embed(*preprocess(doc, False)) for doc in docs]
s = [(query, doc, maxsim(q.squeeze(), di.squeeze())) for doc, di in zip(docs, d)]
for q_text, d_text, score in s:
    print(f"Score: {score:.2f} | Q: {q_text} | D: {d_text}")

```

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2-ColBERT-350M
