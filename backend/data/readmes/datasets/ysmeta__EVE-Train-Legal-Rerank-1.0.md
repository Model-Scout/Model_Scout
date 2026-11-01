---
license: openrail
language:
- ko
task_categories:
- text-ranking
tags:
- korean
- legal
- retrieval
- reranking
- qrels
size_categories:
- 10K<n<100K
---

# EVE-Train-Legal-Rerank-1.0

Training labels for a Korean legal reranker: **25,000 queries × 15 retrieved candidates,
all judged for relevance** (375,000 query-document judgements). Used to train
[ysmeta/EVE-Rerank-1.0-Legal](https://huggingface.co/ysmeta/EVE-Rerank-1.0-Legal).

Candidates come from [EVE-Embed-1.1-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.1-Legal)'s
own top-15. That is deliberate: a reranker trained on some other retriever's candidates
is solving a different problem than the one it gets deployed into.

## Contents

| file | rows | description |
|---|---|---|
| `pooled_train.jsonl` | 25,000 | the 15 retrieved candidates per query |
| `qrels_train.jsonl` | 25,000 | graded relevance for those candidates |

```python
# qrels_train.jsonl
{"query": "계약금을 이미 받았는데도 상대방이 계약 취소할 수 있나요?",
 "gold": "85830",          # the precedent the query was generated from
 "pool_size": 15,
 "grades": {"85830": 2, "91277": 1, "74096": 1}}
```

**Grades**: `2` = the labelled precedent, `1` = another precedent that genuinely answers
the query, absent = judged not relevant. Roughly **3.7 of the 15 candidates are relevant**.

## The lesson these labels encode

For the embedding model, mined hard negatives were destructive: 32%+ of them genuinely
answer the query, and training against them cost −36.5% nDCG@10. The fix was to have an
LLM verify each candidate and train only on the confirmed negatives.

**Carrying that recipe to the reranker was a mistake.** A first attempt discarded every
candidate the judge called relevant and trained on the verified negatives only. It beat
the free public reranker by +0.0034 and its evaluation curve fell from its first
measurement while the loss dropped.

The two tasks are not symmetric. A query here has ~7 genuinely relevant precedents, and
a reranker's job is to rank **all of them** above the irrelevant ones — so the relevant
siblings are the positives, not noise to be filtered out. Turning each into its own
training row gave:

| training signal | graded nDCG@10 | vs the public reranker |
|---|---|---|
| verified negatives, relevant candidates discarded | 0.7540 | +0.0034 |
| **every relevant candidate a positive** | **0.7721** | **+0.0214** |

Same base model, same judge, same candidates — a 6× larger margin from changing what
counts as a positive.

## Construction

1. Retrieve top-15 for 25,000 training queries with EVE-Embed-1.1-Legal over the full
   59,786-precedent corpus.
2. Judge all 15 in one call with [tencent/Hy3](https://huggingface.co/tencent/Hy3)
   (GPTQ-Int4, served locally), with "same legal area but different 쟁점 does not count"
   stated explicitly. Documents are shuffled per query against position bias.
3. Unparseable judgements are retried once, then the query is dropped rather than
   partially labelled.

Queries are split by 사건번호 against
[EVE-Bench-Legal-2.0](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-2.0), so no
case leaks between training and evaluation.

## Caveats

- **Labels are LLM-generated**, not lawyer-reviewed. The judge errs toward accepting
  borderline candidates, so the relevant count is more likely over- than under-stated.
- **Only what EVE-Embed-1.1 retrieved** is judged. Relevant precedents it missed are
  absent, so these labels cannot be used to measure recall.
- **Queries are LLM-generated** from each precedent and carry traces of their source
  document.
- Case types follow the source corpus: 민사 46.3% · 형사 21.9% · 일반행정 14.1% ·
  세무 11.9% · 특허 4.3% · 가사 1.6%. Note the source query file is **ordered**, not
  shuffled — its first rows are far more 민사-heavy than the rest, so any statistic taken
  from a prefix is not the corpus statistic.

## License

OpenRAIL, inherited from
[joonhok-exo-ai/korean_law_open_data_precedents](https://huggingface.co/datasets/joonhok-exo-ai/korean_law_open_data_precedents).
