---
language:
- en
- es
- de
- fr
- it
- pt
- ar
- sv
- 'no'
- ja
- ko
tags:
- liquid
- lfm2
- lfm2.5
- edge
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
- LiquidAI/LFM2.5-Embedding-350M
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
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a>
</div>
</center>

# LFM2.5-Embedding-350M

LFM2.5-Embedding-350M is a dense bi-encoder for fast multilingual retrieval. It produces a single vector per document — the smallest, fastest index — for reliable cross-lingual search across 11 languages.

- **Best-in-class multilingual accuracy** for a dense embedder of its size.
- Inference speed is **on par with much smaller models**, thanks to the efficient LFM2 backbone.
- You can use it as a **drop-in replacement** in your current RAG pipelines.

Find more information about LFM2.5-Embedding-350M in our [blog post](https://liquid-ai-v3-c7c6d49467ac-bf50aea57dc57.webflow.io/blog/lfm2-5-retrievers).

## 🏃 How to run

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

Start llama-server
```bash
llama-server -hf LiquidAI/LFM2.5-Embedding-350M-GGUF --embeddings
```

Make requests to embed queries and documents, and rank by cosine similarity (note the asymmetric `query: ` / `document: ` prompt prefixes)

```bash
❯ uv run dense-retrieve.py

Score: -0.1783 | Q: What is panda? | D: hi
Score:  0.0511 | Q: What is panda? | D: it is a bear
Score:  0.5657 | Q: What is panda? | D: The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.
```

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "requests"]
# ///

# dense-retrieve.py
import numpy as np, requests

QUERY_PREFIX, DOC_PREFIX = "query: ", "document: "

def embed(text: str) -> np.ndarray:
    r = requests.post(
        "http://localhost:8080/v1/embeddings",
        json={"input": text},
    )
    v = np.array(r.json()["data"][0]["embedding"])
    return v / np.linalg.norm(v)

docs = [
    "hi",
    "it is a bear",
    "The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.",
]
query = "What is panda?"

q = embed(QUERY_PREFIX + query)
for doc in docs:
    d = embed(DOC_PREFIX + doc)
    print(f"Score: {float(q @ d):.4f} | Q: {query} | D: {doc}")
```

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M
