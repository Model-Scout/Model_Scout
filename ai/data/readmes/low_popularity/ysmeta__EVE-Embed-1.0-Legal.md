---
license: apache-2.0
language:
- ko
base_model: dragonkue/BGE-m3-ko
pipeline_tag: sentence-similarity
library_name: sentence-transformers
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- korean
- legal
- retrieval
---

# EVE-Embed-1.0-Legal

> **Superseded by [EVE-Embed-1.1-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.1-Legal)**,
> which adds LLM-verified hard negatives and scores 0.7872 nDCG@10 / 0.6700 recall@1
> against this model's 0.7800 / 0.6617 on the same benchmark. Use 1.1 unless you
> specifically need to reproduce these numbers.
>
> The numbers on this page use **single-gold** labels — one correct precedent per query.
> That assumption turned out to be wrong for this domain: a query has 7.20 genuinely
> relevant precedents on average. Under the graded labels of
> [EVE-Bench-Legal-2.0](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-2.0) this
> model scores **0.7223** nDCG@10 with **P@1 0.8906**, against the base model's 0.6557 /
> 0.8214 — the improvement holds, but the 1.0 → 1.1 gap narrows to +0.0030.

Korean embedding model for **legal precedent retrieval**, fine-tuned from
[dragonkue/BGE-m3-ko](https://huggingface.co/dragonkue/BGE-m3-ko).

It is built for the query style practitioners actually use — plain questions like
*"렌트카 회사 지입차주가 자기 차로 돈 받고 영업하면 운수사업법 위반인가요?"* — rather
than the formal 판시사항 phrasing courts write.

| | baseline (BGE-m3-ko) | **EVE-Embed-1.0-Legal** | change |
|---|---|---|---|
| **nDCG@10** | 0.6982 | **0.7800** | **+11.7%** |
| **recall@1** | 0.5647 | **0.6617** | **+17.2%** |
| general Korean retrieval | 0.8698 | 0.8695 | −0.03% |

Retrieval is over the **full 59,786-document corpus** — no candidate pre-filtering,
no reduced pool. The last row is the check that matters as much as the first:
the model gained in its domain without losing general Korean retrieval ability.

## Evaluation

Scored on [EVE-Bench-Legal-1.0](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-1.0):
6,000 practitioner-style queries against 59,786 Korean court precedents.

| model | nDCG@10 | recall@1 | recall@10 |
|---|---|---|---|
| **EVE-Embed-1.0-Legal** | **0.7800** | **0.6617** | 0.8978 |
| dragonkue/BGE-m3-ko | 0.6982 | 0.5647 | 0.8342 |
| nlpai-lab/KURE-v1 | 0.6916 | 0.5562 | 0.8308 |
| BAAI/bge-m3 | 0.6472 | 0.5083 | 0.7932 |
| intfloat/multilingual-e5-large | 0.6288 | 0.4897 | 0.7788 |

### Why the benchmark uses rewritten queries

The corpus ships a natural query-document pair per case: 판시사항 (the legal question)
and 판결요지 (the holding). Public models score **~0.87** nDCG@10 on that pairing —
but both fields are written by the same court about the same issue and share most of
their wording, so the score largely measures lexical overlap. Rewriting the query into
ordinary practitioner language drops every public model by **0.17–0.20**, which is the
part of the original score that was not comprehension. All numbers above are on the
rewritten (hard) set.

## Usage

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("ysmeta/EVE-Embed-1.0-Legal")

query = "계약금을 이미 받았는데도 상대방이 계약을 취소할 수 있나요?"
docs = [
    "소유권이전등기청구사건 당사자의 일방이 계약이행에 착수한 후에는 해제권 행사를 할 수 없으므로 …",
    "임대차계약의 묵시적 갱신이 인정되는 경우 …",
]

q = model.encode(query, normalize_embeddings=True)
d = model.encode(docs, normalize_embeddings=True)
print(q @ d.T)
```

No instruction prefix is required.

## Training

- **Base**: dragonkue/BGE-m3-ko (Apache-2.0)
- **Data**: 134,996 (query, precedent) pairs — practitioner-style queries generated
  from 45,000 precedents, see [EVE-Train-Legal-1.0](https://huggingface.co/datasets/ysmeta/EVE-Train-Legal-1.0)
- **Loss**: CachedMultipleNegativesRankingLoss, **in-batch negatives only**
- **Effective batch**: 512 (256 × 2 GPUs, DDP) — batch size *is* the negative count here
- **LR**: 1e-5, 1 epoch, max_seq_len 384, bf16
- **Hardware**: 2 × NVIDIA H200

### What did not work

Published for reuse, since two of the three levers moved the score the wrong way:

| configuration | nDCG@10 | vs baseline |
|---|---|---|
| mined hard negatives (skip top-3), lr 2e-5, 65% formal queries | 0.4434 | **−36.5%** |
| mined hard negatives (skip top-10), lr 5e-6, synthetic only | 0.6457 | **−7.5%** |
| no mined hard negatives, batch 64 | 0.7535 | +7.9% |
| no mined hard negatives, batch 512 | 0.7643 | +9.5% |
| **above + 4.3× more data** | **0.7800** | **+11.7%** |

**Mined hard negatives are counter-productive in this domain.** Legal precedents
cluster tightly by issue, so the top-ranked non-gold documents for a legal question
are usually genuinely relevant cases. Training the model to push them away damages
its legal semantics. Skipping the top 10 hits did not help — only removing mined
negatives entirely did.

A related trap: the first run *gained* 5.7% on the formal-query set while losing
36.5% on the practitioner set. Evaluating only on the easy set would have reported
that run as a success.

## Limitations

- **판례 only.** The corpus contains court precedents, not statute text (법령 조문),
  so queries that should resolve to a specific article are not covered.
- **Case distribution** of the 59,786-document corpus: 민사 46.3%, 형사 21.9%,
  일반행정 14.1%, 세무 11.9%, 특허 4.3%, 가사 1.6%. 특허/가사 coverage is thin.
- Training queries are **LLM-generated**, not collected from real users. They were
  written to imitate practitioner phrasing, but real query logs would differ.
- Not legal advice. Retrieval surfaces precedents; it does not interpret them.

## License

Apache-2.0, inherited from the base model. The training corpus derives from
`joonhok-exo-ai/korean_law_open_data_precedents` (OpenRAIL); the dataset repos carry
that licence.
