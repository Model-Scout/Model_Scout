---
license: mit
base_model:
- minishlab/potion-multilingual-128M
library_name: model2vec
tags:
- static-embeddings
- model2vec
- quantized
- int8
- sentence-similarity
- semantic-search
- multilingual
- browser
language:
- en
- ru
- de
- fr
- es
- pt
- it
- nl
- pl
- uk
- tr
- ar
- fa
- hi
- zh
- ja
- ko
- vi
- id
- multilingual
pipeline_tag: sentence-similarity
---

# potion-multilingual-128M-int8 — tiny multilingual embeddings that run in the browser

A compact, **in-browser-ready** quantization of
[minishlab/potion-multilingual-128M](https://huggingface.co/minishlab/potion-multilingual-128M):
**int8 + PCA (256 → 128), ~64 MB**. Static [Model2Vec](https://github.com/MinishLab/model2vec)
embeddings — **no GPU, no neural-net inference**, just a token → vector lookup + mean-pool.
101 languages, full vocabulary incl. **Cyrillic**. Token-free public download (CORS-enabled), so a
web page can `fetch()` it directly.

> **Try what it powers:** the **heavy (semantic) engine** of **AI-Chat Compressor** — a Chrome
> extension that compresses AI-chat context *locally* by keeping only the sentences relevant to your
> question. → **[Chrome Web Store](https://chromewebstore.google.com/detail/ai-chat-compressor/hmjkfmdnbkbmmmgkpdbpknlabkflkogb)**

**Try it on a real conversation.** [This shared ChatGPT thread](https://chatgpt.com/share/6a6478f1-1148-83eb-b6a8-b006c6d76737)
is a long discussion about the characters of *The Great Gatsby*. Open it with the extension and
raise the compression strength to watch what survives:
the **heavy** engine selects by meaning with this model, the **light** one by wording with BM25.

![AI-Chat Compressor — query-driven, sentence-level compression powered by this model](banner.jpg)

## What & why

- **Static embeddings** (Model2Vec): tokenize → token-vector lookup → mean-pool → L2-normalize.
  No inference, no GPU — a lookup table. Fast and tiny.
- **Compression:** FP32 → **Int8**; embedding dim **256 → 128** (PCA). ~4× smaller than fp32,
  near-lossless on semantic tasks.
- **Multilingual:** full vocabulary kept (101 languages, incl. **Cyrillic**) — no script stripping.
- **Runs anywhere:** `model2vec` (Python), `model2vec-rs` (Rust), and the **browser via WASM**
  (`StaticModel::from_bytes`).

## Use

```python
from model2vec import StaticModel
m = StaticModel.from_pretrained("777Radik/potion-multilingual-128M-int8")

# Cross-lingual by design: these two sentences mean the same thing and land
# close together, although they share no words and use different scripts.
emb = m.encode(["как развернуть сервис в кластере", "deploy a service to a cluster"])
```

Rank by cosine similarity for semantic search / retrieval / reranking. Near-lossless vs the fp32
source on semantic tasks (int8 quantization).

## How it compares

A head-to-head against BM25 for query-focused sentence selection under a fixed byte budget, on
three public QA datasets with human-annotated evidence — code and exact commands at
**[github.com/rnrn/ai-context](https://github.com/rnrn/ai-context)**:

| dataset | budget | BM25 | this model |
| --- | --- | ---: | ---: |
| HotpotQA — supporting-fact recall | 25% | 72.1% | 57.4% |
| MuSiQue — answer kept | 25% | 48.0% | 50.0% |
| QASPER — answer span kept | 25% | 74.4% | 81.8% |
| QASPER — answer span kept | 5% | 44.6% | 43.8% |

Neither ranker wins everywhere: lexical matching is ahead where the question repeats the wording of
the passage (HotpotQA), the embeddings are ahead where it does not (QASPER). Both are far above
truncating the context to the same size.

## Provenance

Produced with `scripts/quantize-potion.py --dim 128` (model2vec int8 quantization).
Base model & method by [MinishLab](https://github.com/MinishLab/model2vec). License: MIT.
