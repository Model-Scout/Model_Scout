---
language:
- ko
license: apache-2.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model: Qwen/Qwen3-Embedding-4B
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- text-embedding
- information-retrieval
- korean
- finance
- lora
- peft
datasets:
- BCCard/BCAI-Finance-Kor-Embedding-Triplet
- BCCard/BCAI-Finance-Kor-Embedding-Pair
metrics:
- ndcg
- mrr
- recall
---

# 1. Overview
A Korean text-embedding model for the **BC Card domain**, built by LoRA fine-tuning
[`Qwen/Qwen3-Embedding-4B`](https://huggingface.co/Qwen/Qwen3-Embedding-4B) on BC Card in-domain data (personal / merchant / corporate / VIP). It is intended as the **retriever (bi-encoder)** stage of a BC Card RAG pipeline.

This is the **4B-scale** sibling of [`BCCard/MoAI-Embedding-0.6B`](https://huggingface.co/BCCard/MoAI-Embedding-0.6B) — a larger-capacity variant for higher retrieval quality at the cost of compute/latency.

On a held-out in-domain test set it improves **NDCG@10 by +6.1%** and **Accuracy@1 by +8.9%** over the base `Qwen3-Embedding-4B` (full metrics in §2.3).

## 1.1. TL;DR
* **Base model**: [`Qwen/Qwen3-Embedding-4B`](https://huggingface.co/Qwen/Qwen3-Embedding-4B) — 36 layers, hidden 2560, last-token pooling, instruction-aware
* **Domain / Language**: Finance (BC Card — personal / merchant / corporate / VIP) / Korean
* **Task**: Query-document retrieval (QA search, document similarity), RAG retriever
* **Method**: PEFT (LoRA) + Multiple Negatives Ranking (contrastive)
* **Format**: merged standalone (LoRA fused into base; loads with `sentence-transformers`, no `peft`)
* **Embedding dimension**: 2560 · **Max sequence length**: 1024 · **Similarity**: cosine (outputs are L2-normalized)
* **Intended use**
  - In-house **BC Card-domain RAG retriever** (Top-K candidate retrieval)
  - QA search, document-similarity scoring

## 1.2. Usage

The model was trained with an **instruction prefix on the query side only** (documents get no
instruction). Inject the same instruction at inference so query/document encoding matches training.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BCCard/MoAI-Embedding-4B")

# Query-side instruction (identical to training) - prepend to every query at inference time
QUERY_INSTRUCTION = "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: "

queries = ["BC카드 연회비는 어떻게 되나요?"]
documents = [
    "BC카드 연회비는 카드 종류와 혜택 구성에 따라 다르게 책정됩니다 ...",
    "바로카드 연회비는 국내 전용과 해외 겸용 여부에 따라 차등 부과됩니다 ...",
    "전월 실적 등 조건을 충족하면 다음 해 연회비가 면제되는 카드도 있습니다 ...",
    "카드 분실 신고는 고객센터 또는 앱에서 즉시 가능합니다 ...",
    ...
]

# Queries: inject the instruction · Documents: no instruction
q_emb = model.encode(queries, prompt=QUERY_INSTRUCTION)
d_emb = model.encode(documents)

scores = model.similarity(q_emb, d_emb)   # cosine; rank documents by score
print(scores)
```

> The instruction is also stored in the model config, so `model.encode(queries, prompt_name="query")`
> is equivalent to passing `prompt=QUERY_INSTRUCTION` explicitly. Documents use no prompt
> (`prompt_name="document"` is an empty string).

* **Query prompt** (instruction): `Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: `
* **Document prompt**: none

## 1.3. Training Data
| Dataset | Role | Size |
|---------|------|------|
| [BCAI-Finance-Kor-Embedding-Triplet](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet) | Training (anchor / positive / negative) | 43,394 triplets (train) |
| [BCAI-Finance-Kor-Embedding-Pair](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair) | Corpus pool / evaluation | 36,281 unique chunks |

* Sources: BC Card financial QA (BCAI) + website crawl + synthetic data (chunking + multi-query generation)
* Triplets are constructed via **hard-negative mining** over the unified corpus.

## 1.4. Training Procedure
| Item | Value |
|------|-------|
| Method | LoRA (PEFT) |
| LoRA | r=64, alpha=128, dropout=0.05, targets = q,k,v,o,gate,up,down_proj |
| Loss | CachedMultipleNegativesRankingLoss (in-batch negatives) |
| Batch | per-device 256 (DDP) → 511 in-batch negatives per rank |
| LR / scheduler | 5e-5 / cosine, warmup_ratio 0.1, weight_decay 0.01 |
| Epochs | 3, early stopping — best checkpoint selected by validation NDCG@10 |
| Precision | bf16, gradient checkpointing |
| Hardware | 8× NVIDIA RTX PRO 6000 Blackwell (DDP) |

<br>

# 2. Evaluation
## 2.1. Setup
* **Queries**: 1,000 (held-out test split) · **Corpus**: 36,281 unique chunks
* **Protocol**: binary-relevance information retrieval; the same evaluator used during training
* **Metrics**: NDCG@10 (primary), MRR@10, Recall@{1,10}, Accuracy@1, MAP@10
* **Models compared**: base (`Qwen3-Embedding-4B`, no fine-tuning) vs. **v4 (r64 / lr5e-5 / 3ep, released)**

<br>

## 2.2. Training
<div align="center">
  <img src="figures/evaluation-train-1-1.png" alt="Training curves - loss, learning rate, validation NDCG@10 (WandB)" >
</div>

Trained for 3 epochs (early-stopped) with a cosine schedule; training loss decreases steadily while validation NDCG@10 climbs early and plateaus (peak ≈ 0.695 around epoch ~1.4), and the best checkpoint is selected at the peak. Curves (loss / learning rate / validation NDCG@10) are logged to Weights & Biases.

<br>

## 2.3. In-domain Retrieval Benchmark
<div align="center">
  <img src="figures/evaluation-test-1-1.png" alt="Test-set retrieval metrics - base vs v4" >
</div>
<div align="center">
  <img src="figures/evaluation-test-1-2.png" alt="Test-set retrieval metrics comparison (per metric)" >
</div>

| Metric | base (Qwen3-4B) | v4 (r64/5e-5/3ep) | v4 Δ vs base |
|--------|:---:|:---:|:---:|
| **NDCG@10** | **0.6508** | **0.6906** | **+0.040 (+6.1%)** |
| MRR@10 | 0.6805 | 0.7283 | +0.048 (+7.0%) |
| Recall@10 | 0.7244 | 0.7620 | +0.038 (+5.2%) |
| Recall@1 | 0.5081 | 0.5520 | +0.044 (+8.6%) |
| Accuracy@1 | 0.5950 | 0.6480 | +0.053 (+8.9%) |
| MAP@10 | 0.6013 | 0.6410 | +0.040 (+6.6%) |

**v4 is the released model.** Fine-tuning lifts in-domain retrieval by **roughly +7%** over the base `Qwen3-Embedding-4B`, with the largest gains on top-rank precision (Accuracy@1, Recall@1). It also surpasses the 0.6B sibling (test NDCG@10 0.6695) by **+0.021 (+3.2%)** — a modest scale gain at ~7× the parameters, so the 0.6B remains the better pick for latency-sensitive serving.

### Comparison with other encoders
On the *same* in-domain test set, untuned encoders — our own `Qwen3-Embedding` base (0.6B / 4B) and public multilingual SOTA models (each run with its own native prompt format) — all fall **well below this model**: domain fine-tuning beats general-purpose scale:

| Model | Params | NDCG@10 | MRR@10 | Recall@10 | Accuracy@1 | MAP@10 | Avg |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| LiquidAI/LFM2.5-Embedding-350M | 0.35B | 0.5983 | 0.6166 | 0.6799 | 0.5320 | 0.5519 | 0.5957 |
| Qwen3-Embedding-0.6B (base) | 0.6B | 0.6186 | 0.6449 | 0.7046 | 0.5560 | 0.5652 | 0.6179 |
| google/embeddinggemma-300m | 0.3B | 0.6373 | 0.6664 | 0.7082 | 0.5790 | 0.5906 | 0.6363 |
| BAAI/bge-m3 | 0.6B | 0.6426 | 0.6660 | 0.7261 | 0.5730 | 0.5913 | 0.6398 |
| intfloat/multilingual-e5-large | 0.6B | 0.6476 | 0.6722 | 0.7313 | 0.5790 | 0.5958 | 0.6452 |
| Qwen3-Embedding-4B (base) | 4B | 0.6508 | 0.6805 | 0.7244 | 0.5950 | 0.6013 | 0.6504 |
| MoAI-Embedding-0.6B (sibling) | 0.6B | 0.6695 | 0.7060 | 0.7508 | 0.6190 | 0.6171 | 0.6725 |
| **MoAI-Embedding-4B (this model)** | 4B | **0.6906** | **0.7283** | **0.7620** | **0.6480** | **0.6410** | **0.6940** |

This model improves over its own `Qwen3-Embedding-4B` base by **+0.040 NDCG@10 (+6.1%)** and leads the best general-purpose baseline (e5-large) by **+0.043 NDCG@10**. Notably, the untuned **4B base (`0.6508`) trails the fine-tuned 0.6B sibling (`0.6695`)** — fine-tuning outweighs scale. _Caveat: these baselines are not tuned on BC Card data — the comparison illustrates the value of domain adaptation, not a defect in the baselines._

<br>

## 2.4. Limitations
* **Domain-specific** — tuned for BC Card Korean financial text; out-of-domain or non-Korean performance is not guaranteed.
* **Compute cost** — at 4B, this model is markedly heavier (memory / latency) than the [0.6B sibling](https://huggingface.co/BCCard/MoAI-Embedding-0.6B); for latency- or throughput-sensitive serving, consider the 0.6B variant.
* **Re-ranking recommended** — as a bi-encoder it favors recall over fine-grained precision.
    - Recommended pipeline: **Bi-Encoder (this model) Top-K → Cross-Encoder re-ranking**
* **Sequence length** — inputs are truncated at 1,024 tokens; content past that limit is not encoded, so very long documents should be chunked before indexing.
* **Exact-value matching** — fine-grained numeric/tabular facts (fees, rates, dates, terms) are not reliably distinguished by dense similarity alone; pair with lexical (BM25) retrieval or a re-ranker when exactness matters.
* **Retrieval only** — this is an embedding model, not a generator; it ranks passages and does not produce answers.
* **Synthetic data influence** — part of the training set is LLM-synthesized (chunking + multi-query), which may carry the generator's stylistic/coverage biases.

<br>

# 3. Future Work
* **Data quality improvement & re-training**
	- Human-annotation labeling
	- More rigorous hard-negative mining (iterative, mined with this model)
	- Broader/higher-quality data (incl. general financial corpora)
* **System-level**
	- Cross-Encoder re-ranker for precision
	- HyDE / dynamic instruction injection at query time

<br>

# 4. Meta Info
## 4.1. Citation
```bibtex
@misc{bccard2026moaiembedding4b,
  title        = {MoAI-Embedding-4B: A BC Card-Domain Korean Text Embedding Model},
  author       = {BC Card AX Team},
  year         = {2026},
  howpublished = {https://huggingface.co/BCCard/MoAI-Embedding-4B},
  note         = {LoRA fine-tune of Qwen3-Embedding-4B for BC Card-domain Korean retrieval}
}
```

## 4.2. See Also
* **0.6B sibling model**: [`BCCard/MoAI-Embedding-0.6B`](https://huggingface.co/BCCard/MoAI-Embedding-0.6B)
* **Training dataset**: [`BCCard/BCAI-Finance-Kor-Embedding-Triplet`](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet)
* **Corpus dataset**: [`BCCard/BCAI-Finance-Kor-Embedding-Pair`](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair)

<br>
