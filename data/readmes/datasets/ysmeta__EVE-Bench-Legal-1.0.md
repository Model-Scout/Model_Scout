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
size_categories:
- 10K<n<100K
---

# EVE-Bench-Legal-1.0

A Korean **legal precedent retrieval** benchmark built to be hard enough to measure
progress. 6,000 practitioner-style queries over 59,786 Korean court precedents.

## Why this exists

Public Korean retrieval benchmarks are largely saturated — off-the-shelf models score
above 0.90 nDCG@10 on several of them, so they can no longer separate a good retriever
from a very good one.

The obvious legal alternative has the same problem in a subtler form. The source corpus
pairs 판시사항 (the legal question a case resolves) with 판결요지 (its holding), which
looks like free supervision. But both are written by the same court about the same
issue and share most of their vocabulary, so public models reach **~0.87** nDCG@10 on
that pairing. That score is mostly lexical overlap, not legal understanding.

This benchmark rewrites each query into the way a practitioner would actually ask it.
Every public model tested drops **0.17–0.20**:

| model | 판시사항 (formal) | this benchmark | drop |
|---|---|---|---|
| dragonkue/BGE-m3-ko | 0.8698 | **0.6982** | −0.172 |
| nlpai-lab/KURE-v1 | 0.8638 | **0.6916** | −0.172 |
| BAAI/bge-m3 | 0.8407 | 0.6472 | −0.194 |
| intfloat/multilingual-e5-large | 0.8240 | 0.6288 | −0.195 |

The gap is the headroom the formal pairing was hiding.

Example of the rewrite:

> **formal**: 렌트카회사의 지입차주가 지입차량으로 한 유상영업행위가 자동차임차인의
> 유상영업행위를 금하는 자동차운수사업법 제73조, 제55조의8에 위반되는지 여부(소극)
>
> **rewritten**: 렌트카 회사 지입차주가 자기 차로 돈 받고 영업하면 운수사업법 위반인가요?

## Contents

| file | rows | description |
|---|---|---|
| `corpus.jsonl` | 59,786 | all precedents — the retrieval pool |
| `eval_synth.jsonl` | 2,000 | 3 rewritten queries each (6,000 total), with gold docid |
| `eval_queries.jsonl` | 2,000 | the original 판시사항 queries, for the formal-set comparison |

```python
{"docid": "85830", "title": "토지건물매매무효확인", "text": "…", "kind": "민사"}          # corpus
{"gold": "85830", "orig": "회사소유 부동산을 …", "synth": ["…", "…", "…"], "kind": "민사"}  # eval
```

Retrieval must run over the **entire corpus**. Scoring against a reduced candidate pool
inflates results by a wide margin and is not comparable to the table above.

## Case-type distribution

민사 45.5% · 형사 23.5% · 일반행정 14.6% · 세무 11.1% · 특허 3.8% · 가사 1.4%
(inherited from the source corpus; 특허 and 가사 coverage is thin)

## Construction

1. Precedents from [joonhok-exo-ai/korean_law_open_data_precedents](https://huggingface.co/datasets/joonhok-exo-ai/korean_law_open_data_precedents)
   (Korean government open data), keeping the 59,786 cases that carry both 판시사항 and 판결요지.
2. Split by 사건번호 so no case appears in both the train and eval halves.
3. Queries rewritten by [Tencent Hy3](https://huggingface.co/tencent/Hy3) (Apache-2.0),
   3 per case from different angles, prompted to avoid the formal wording.

Queries are model-generated, not collected from real users — they imitate practitioner
phrasing rather than reproduce it.

## Baseline reproduction

```python
import json
from sentence_transformers import SentenceTransformer

corpus = [json.loads(l) for l in open("corpus.jsonl")]
texts  = [(c["title"] + " " + c["text"]).strip() for c in corpus]
id2pos = {c["docid"]: i for i, c in enumerate(corpus)}

queries, golds = [], []
for l in open("eval_synth.jsonl"):
    r = json.loads(l)
    for q in r["synth"]:
        queries.append(q); golds.append(id2pos[r["gold"]])

m = SentenceTransformer("ysmeta/EVE-Embed-1.0-Legal")
D = m.encode(texts,  normalize_embeddings=True)
Q = m.encode(queries, normalize_embeddings=True)
# rank golds in Q @ D.T, then nDCG@10
```

## License

OpenRAIL, inherited from the source corpus. Not legal advice.
