---
license: apache-2.0
base_model: skt/A.X-Encoder-base
language:
- ko
- en
pipeline_tag: sentence-similarity
library_name: sentence-transformers
tags:
- sentence-transformers
- embedding
- retrieval
- mteb
- korean
---

# NGA-KR/ko-embed-v0

Korean dense text embedding model (149M parameters), fine-tuned from [skt/A.X-Encoder-base](https://huggingface.co/skt/A.X-Encoder-base).

## Training data (zero-shot on MTEB(kor))

This model was trained **only** on public English retrieval datasets — no Korean benchmark train splits were used:

- MSMARCO
- NQ
- HotpotQA
- GooAQ

Consequently, the model is 100% zero-shot on `MTEB(kor, v1)` and `MTEB(kor, v2)` (declared via `training_datasets` in the MTEB model metadata).

## Usage

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("NGA-KR/ko-embed-v0")
q = model.encode(["전세 계약서에 기간을 안 썼으면 얼마 동안 유효해?"], prompt_name="query")
d = model.encode(["임대차 계약 기간을 정하지 않은 경우 2년으로 본다..."], prompt_name="document")
print(q @ d.T)
```

Prompts are stored in the model config: `query: ` for queries, `passage: ` for documents.

## Evaluation

Evaluated with `mteb` on `MTEB(kor, v2)` (20 tasks). See the MTEB leaderboard entry for full per-task scores.

## Training details

- Base: skt/A.X-Encoder-base (ModernBERT-style Korean encoder, mean pooling, L2-normalised)
- Objective: contrastive (CachedMultipleNegativesRankingLoss), in-batch + 1 hard negative
- Batch 2048, lr 2e-5, cosine schedule, 1 epoch, bf16
- Max sequence length: 512

## License

apache-2.0. Base model license: see [skt/A.X-Encoder-base](https://huggingface.co/skt/A.X-Encoder-base).
