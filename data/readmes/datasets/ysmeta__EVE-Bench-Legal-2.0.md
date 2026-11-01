---
license: openrail
language:
- ko
task_categories:
- text-retrieval
tags:
- korean
- legal
- retrieval
- benchmark
- qrels
size_categories:
- 10K<n<100K
---

# EVE-Bench-Legal-2.0

Korean legal precedent retrieval benchmark: **5,999 practitioner-style queries** over
**59,786 court precedents**, with **graded multi-gold relevance labels** (43,179
query-document judgements, 7.20 relevant precedents per query).

Version 1.0 scored one gold document per query. That turned out to be the reason every
model looked the same.

## Why 1.0 needed replacing

1.0 paired each query with the single precedent it was generated from. Judging the
retrieved candidates showed that assumption is wrong for this domain:

| | |
|---|---|
| relevant precedents per query | **7.20** (median 6, max 35) |
| queries with exactly one relevant precedent | **4.3%** |
| relevant share of the judged pool | 7.20 of 35.9 documents |

Legal precedents cluster by 쟁점, so several cases genuinely answer the same practitioner
question. Nothing distinguishes the *labelled* one from an equally valid sibling, and
single-gold nDCG@10 was charging every model for ~6 correct answers per query.

The consequence was measurable. Under 1.0, a ranker that perfectly identified relevance
but could not guess which relevant case was the labelled one would score only **0.7423**
nDCG@10 — while the nominal ceiling (recall@20) read 0.9360. Four public retrievers,
five public rerankers and two fine-tuned models all landed between 0.63 and 0.81, and
reranking looked worthless because the headroom it was measured against did not exist.

## Contents

| file | rows | description |
|---|---|---|
| `qrels.jsonl` | 5,999 | graded relevance labels, one row per query |
| `pooled.jsonl` | 6,000 | the judged candidate pool + each system's top-20 ranking |
| `corpus.jsonl` | 59,786 | precedents (`docid`, `title`, `text`, `kind`) |
| `eval_synth.jsonl` | 2,000 | source cases with their 3 generated queries |

```python
# qrels.jsonl
{"query": "계약금을 이미 받았는데도 상대방이 계약 취소할 수 있나요?",
 "gold": "85830",           # the precedent the query was generated from
 "pool_size": 34,           # documents judged for this query
 "grades": {"85830": 2, "91277": 1, "74096": 1}}
```

**Grades**: `2` = the labelled precedent, `1` = another precedent that genuinely answers
the query, absent = judged not relevant. Grade 2 is kept above grade 1 so results stay
comparable with every number published against 1.0, and because the labelled case is the
one the court's own 판시사항 pointed at.

## Scoring

```python
import json, numpy as np

qrels = {r["query"]: r["grades"] for r in map(json.loads, open("qrels.jsonl"))}

def dcg(gains):
    return sum((2 ** g - 1) / np.log2(i + 2) for i, g in enumerate(gains))

def ndcg_at_10(query, ranked_docids):
    g = qrels[query]
    got = [g.get(d, 0) for d in ranked_docids[:10]]
    ideal = sorted(g.values(), reverse=True)[:10]
    return dcg(got) / dcg(ideal)
```

## Reference results

Retrieval over the full 59,786-document corpus, no pre-filtering. Rerankers reorder
EVE-Embed-1.1's top 20.

| system | graded nDCG@10 | P@1 (any relevant) | single-gold nDCG@10 |
|---|---|---|---|
| EVE-Embed-1.1 + [EVE-Rerank-1.0](https://huggingface.co/ysmeta/EVE-Rerank-1.0-Legal) | **0.7721** | **0.9355** | 0.8175 |
| EVE-Embed-1.1 + dragonkue/bge-reranker-v2-m3-ko | 0.7506 | 0.9110 | 0.8029 |
| [EVE-Embed-1.1-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.1-Legal) | 0.7253 | 0.8940 | 0.7873 |
| [EVE-Embed-1.0-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.0-Legal) | 0.7223 | 0.8906 | 0.7802 |
| dragonkue/BGE-m3-ko | 0.6557 | 0.8214 | 0.6983 |
| nlpai-lab/KURE-v1 | 0.6476 | 0.8123 | 0.6917 |

All gaps are significant under a paired bootstrap over the 5,998 shared queries
(10,000 resamples): base → EVE-Embed-1.1 **+0.0695** [+0.0643, +0.0747]; retrieval →
reranked **+0.0468** [+0.0429, +0.0506]; EVE reranker over the public one **+0.0214**
[+0.0194, +0.0235]; 1.0 → 1.1 **+0.0030** [+0.0012, +0.0048].

These labels also changed a conclusion. Under single-gold scoring reranking looked
worthless — the best public reranker gained +0.016 against an apparent +0.149 of
headroom, and a first fine-tune beat it by +0.0034. Graded scoring shows reranking is
worth +0.0468, and that a reranker trained to rank *all* relevant precedents highly
(rather than to isolate the labelled one) beats the public model by +0.0214.

**P@1 is the number to read for practical use.** EVE-Embed-1.1 puts a genuinely relevant
precedent first for 89.4% of queries — a fact single-gold scoring reported as 0.67.

## How the labels were made

1. **Pool.** Top 20 from four retrievers — dragonkue/BGE-m3-ko, nlpai-lab/KURE-v1,
   EVE-Embed-1.0, EVE-Embed-1.1 — unioned per query. Mean pool 35.9 documents (55%
   overlap removed). KURE-v1 is in the pool specifically because it is *not* a BGE-m3
   derivative: the other three share a lineage and therefore share blind spots.
2. **Judge.** [tencent/Hy3](https://huggingface.co/tencent/Hy3) (GPTQ-Int4, served
   locally) was shown 15 documents at a time and asked which could answer the question,
   with "same legal area but different 쟁점 does not count" stated explicitly.
   Documents were shuffled per query to avoid position bias.
3. **Failure handling.** An unparseable judgement was retried once, then the whole query
   was dropped rather than partially labelled — 1 of 6,000 queries was lost this way.
   Writing a guessed label into ground truth is not recoverable; a slightly smaller
   benchmark is.

## Limitations

- **Labels are LLM-generated, not lawyer-reviewed.** They encode one model's reading of
  relevance. The judge errs toward accepting borderline candidates, so 7.20 is more
  likely an over-count than an under-count.
- **Pooling bias.** Documents no pooled system retrieved in its top 20 are unjudged and
  scored 0. A system that finds relevant precedents none of the four found is
  under-credited. This is the standard TREC pooling limitation.
- **Queries carry traces of their source document.** They were LLM-generated from each
  precedent, so a model can partly recover the labelled case from phrasing rather than
  from legal understanding. Evidence: under 1.0's single-gold scoring the models score
  *above* what a perfect relevance ranker could (≈0.86 vs 0.7423 conditional on the gold
  being retrieved). Graded scoring reduces the payoff for exploiting this, but does not
  remove it. Queries collected from real users would be the fix.
- **판례 only**, no statute text (법령 조문). Case types: 민사 46.3% · 형사 21.9% ·
  일반행정 14.1% · 세무 11.9% · 특허 4.3% · 가사 1.6%.

## License

OpenRAIL, inherited from
[joonhok-exo-ai/korean_law_open_data_precedents](https://huggingface.co/datasets/joonhok-exo-ai/korean_law_open_data_precedents).
