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

# EVE-Embed-1.1-Legal

Korean embedding model for **legal precedent retrieval**, fine-tuned from
[dragonkue/BGE-m3-ko](https://huggingface.co/dragonkue/BGE-m3-ko).

It is built for the query style practitioners actually use — plain questions like
*"렌트카 회사 지입차주가 자기 차로 돈 받고 영업하면 운수사업법 위반인가요?"* — rather
than the formal 판시사항 phrasing courts write.

| | baseline (BGE-m3-ko) | **EVE-Embed-1.1-Legal** | change |
|---|---|---|---|
| **nDCG@10** | 0.6982 | **0.7872** | **+12.8%** |
| **recall@1** | 0.5647 | **0.6700** | **+18.7%** |
| general Korean retrieval | 0.8698 | 0.8695 | −0.03% |

Retrieval is over the **full 59,786-document corpus** — no candidate pre-filtering,
no reduced pool. The last row is the check that matters as much as the first:
the model gained in its domain without losing general Korean retrieval ability.

## Evaluation

Scored on [EVE-Bench-Legal-1.0](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-1.0):
6,000 practitioner-style queries against 59,786 Korean court precedents.

| model | nDCG@10 | recall@1 | recall@10 |
|---|---|---|---|
| **EVE-Embed-1.1-Legal** | **0.7872** | **0.6700** | **0.9045** |
| [EVE-Embed-1.0-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.0-Legal) | 0.7800 | 0.6617 | 0.8978 |
| dragonkue/BGE-m3-ko | 0.6982 | 0.5647 | 0.8342 |
| nlpai-lab/KURE-v1 | 0.6916 | 0.5562 | 0.8308 |
| BAAI/bge-m3 | 0.6472 | 0.5083 | 0.7932 |
| intfloat/multilingual-e5-large | 0.6288 | 0.4897 | 0.7788 |

### Update: scored again under multi-gold relevance

The table above uses **single-gold** labels — one correct precedent per query. Judging
the retrieved candidates afterwards showed that assumption is wrong for this domain:
a query has **7.20 genuinely relevant precedents** on average, and only 4.3% have exactly
one. Single-gold nDCG@10 was charging every model for ~6 correct answers per query.

[EVE-Bench-Legal-2.0](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-2.0) rescores
the same rankings against graded labels:

| system | graded nDCG@10 | **P@1 (any relevant)** |
|---|---|---|
| **EVE-Embed-1.1-Legal** | **0.7253** | **0.8940** |
| EVE-Embed-1.0-Legal | 0.7223 | 0.8906 |
| dragonkue/BGE-m3-ko | 0.6557 | 0.8214 |
| nlpai-lab/KURE-v1 | 0.6476 | 0.8123 |

**P@1 is the number to read for practical use**: this model puts a genuinely relevant
precedent first for **89.4%** of queries, which single-gold scoring reported as 0.67.
The gain over the base model holds under the new metric (+0.0695, paired bootstrap
[+0.0643, +0.0747], p < 0.0001).

Two honest notes. The 1.0 → 1.1 gap shrinks from +0.0072 to **+0.0030** under graded
scoring, so part of what the verified hard negatives bought was specific to picking the
*labelled* precedent rather than better relevance. And adding
[EVE-Rerank-1.0-Legal](https://huggingface.co/ysmeta/EVE-Rerank-1.0-Legal) on top of this
model's top-20 is worth **+0.0468** (0.7253 → 0.7721, P@1 0.9355) — far more than the gap
between any two retrievers here.

### Why the benchmark uses rewritten queries

The corpus ships a natural query-document pair per case: 판시사항 (the legal question)
and 판결요지 (the holding). Public models score **~0.87** nDCG@10 on that pairing —
but both fields are written by the same court about the same issue and share most of
their wording, so the score largely measures lexical overlap. Rewriting the query into
ordinary practitioner language drops every public model by **0.17–0.20**, which is the
part of the original score that was not comprehension. All numbers above are on the
rewritten (hard) set.

## What changed in 1.1: hard negatives, verified

Version 1.0 shipped with **no** mined hard negatives, because adding them cost
−36.5% and −7.5% in earlier runs. This version puts them back — after removing the
ones that were never negatives to begin with.

An LLM ([tencent/Hy3](https://huggingface.co/tencent/Hy3), GPTQ-Int4, served
locally) judged 20,000 queries against their top-10 mined candidates. Of 200,000
candidate negatives, **64,741 (32.4%) genuinely answer the query.** That is the
mechanism behind the earlier losses: roughly one in three mined "hard negatives" was
teaching the model that a correct answer is wrong. Legal precedents cluster tightly by
issue, so the nearest non-gold neighbours of a legal question are usually relevant
cases with a different holding.

Training on the survivors — 19,038 queries with an average of 3.9 verified negatives —
is what separates 1.1 from 1.0:

| | nDCG@10 | recall@1 |
|---|---|---|
| EVE-Embed-1.0-Legal (in-batch negatives only) | 0.7800 | 0.6617 |
| **EVE-Embed-1.1-Legal (+ verified hard negatives)** | **0.7872** | **0.6700** |
| difference | **+0.0072** | **+0.0083** |
| 95% bootstrap CI (paired, 10,000 resamples) | [+0.0046, +0.0099] | [+0.0028, +0.0138] |
| p | <0.0001 | 0.0024 |

The gain is real but small, and it is reported that way on purpose: 5,063 of the
6,000 queries rank identically under both models, and the shift comes from 559 wins
against 378 losses among the 937 that moved. Both models are scored on the same
queries, so the comparison is paired — an unpaired reading would put the standard
error near 0.0045 and call this inconclusive.

**The revised conclusion**: hard negatives are not harmful in this domain. *Unverified*
hard negatives are. The cost of verification (one LLM call per query, ~5 queries/sec,
68 minutes for 20,000) is small next to a 36.5% regression.

## Usage

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("ysmeta/EVE-Embed-1.1-Legal")

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
- **Data**: [EVE-Train-Legal-1.1](https://huggingface.co/datasets/ysmeta/EVE-Train-Legal-1.1)
  — 134,996 (query, precedent) pairs generated from 45,000 precedents, plus 19,038
  queries carrying LLM-verified hard negatives
- **Loss**: CachedMultipleNegativesRankingLoss
- **Effective batch**: 512 (256 × gradient accumulation 2)
- **LR**: 1e-5, 1 epoch, max_seq_len 384, bf16, 302 steps (~25 min)
- **Checkpoint selection**: `load_best_model_at_end` on a held-out hard slice
- **Hardware**: 1 × NVIDIA H200

The verified negatives are *added to* the pair set rather than replacing it. Training
on the 19,038 verified queries alone would have confounded the negatives' effect with
a 7× data cut, and the result would not have been attributable to either.

### What did not work

Published for reuse, since most of these levers moved the score the wrong way:

| configuration | nDCG@10 | vs baseline |
|---|---|---|
| mined negatives (skip top-3), lr 2e-5, 65% formal queries | 0.4434 | **−36.5%** |
| mined negatives (skip top-10), lr 5e-6, synthetic only | 0.6457 | **−7.5%** |
| no mined negatives, batch 64 | 0.7535 | +7.9% |
| no mined negatives, batch 512 | 0.7643 | +9.5% |
| above + 4.3× more data (= 1.0) | 0.7800 | +11.7% |
| **above + LLM-verified negatives (= 1.1)** | **0.7872** | **+12.8%** |

Skipping the top 10 mined hits did not rescue them — only judging each candidate did.

A related trap worth repeating: the first run *gained* 5.7% on the formal-query set
while losing 36.5% on the practitioner set. Evaluating only on the easy set would have
reported that run as a success. Evaluation design decided the conclusion.

## Limitations

- **판례 only.** The corpus contains court precedents, not statute text (법령 조문),
  so queries that should resolve to a specific article are not covered.
- **Case distribution** of the 59,786-document corpus: 민사 46.3%, 형사 21.9%,
  일반행정 14.1%, 세무 11.9%, 특허 4.3%, 가사 1.6%. 특허/가사 coverage is thin.
- **Finance is covered as litigation, not as practice documents.** 17.3% of the corpus
  (10,323 cases) names a financial institution or instrument — 보험금, 약속어음금,
  대여금, 근저당권설정등기말소, 배당이의 and similar — concentrated in 민사, where
  23.8% of cases qualify. That is case law *about* finance. Contract terms (약관),
  product disclosures, filings and internal policy documents are a different register
  and are not represented; retrieval over those needs its own corpus.
- Training queries are **LLM-generated**, not collected from real users. They were
  written to imitate practitioner phrasing, but real query logs would differ.
- The negative verification is **also LLM-generated** and inherits the judge's biases.
  It errs toward marking borderline candidates relevant, which discards usable
  negatives rather than admitting false ones — the safe direction, but it means the
  verified set is smaller and more conservative than a human-labelled one would be.
- **Benchmark queries carry traces of their source precedent.** They were LLM-generated
  from each case, so part of the measured score reflects recovering that specific
  document from phrasing rather than legal understanding. Evidence: under single-gold
  scoring the models score *above* what a perfect relevance ranker could reach
  (≈0.86 vs 0.7423, conditional on the gold being retrieved). Graded scoring reduces the
  payoff for this but does not remove it; real user query logs would be the fix. See the
  [benchmark card](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-2.0).
- Not legal advice. Retrieval surfaces precedents; it does not interpret them.

## License

Apache-2.0, inherited from the base model. The training corpus derives from
`joonhok-exo-ai/korean_law_open_data_precedents` (OpenRAIL); the dataset repos carry
that licence.
