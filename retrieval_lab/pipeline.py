"""Run one query through pre-retrieval, dense + sparse retrieval and weighted RRF.

Order of operations for a plan:
1. Pre-retrieval transforms all read the original query (so they can run in
   parallel; pre-retrieval latency = slowest transform).
   - Rewrite replaces the base query of both channels.
   - Decomposition / Multi-Query add query variants to both channels.
   - HyDE replaces the base query of the dense channel with a hypothetical
     model card; the sparse channel keeps the text query.
2. Hard filters (05_validate_retrieval.hard_filter) select eligible rows.
3. Each query variant gives a dense list and a sparse list (top CHANNEL_DEPTH).
4. Weighted RRF fuses all lists; each channel's weight is split evenly over its
   lists. The fused top_k is returned.
5. With use_name_lookup, models named in the query text (exact model-name
   match, see name_lookup) are pinned in front of the fused list.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional, Tuple

import numpy as np

from retrieval_lab import corpus, dense, fusion, pre_retrieval
from retrieval_lab.planner import RetrievalPlan

CHANNEL_DEPTH = 100
# Model-name-like tokens: start with a letter, may contain digits . _ -
NAME_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9]")
MIN_NAME_LENGTH = 4


@dataclass
class RunResult:
    ranked: List[str]
    latency_ms: Dict[str, float]
    dense_queries: List[str]
    sparse_queries: List[str]
    eligible_count: int
    transforms: Dict[str, List[str]] = field(default_factory=dict)


class Retriever:
    def __init__(self, rows: Optional[List[Dict[str, Any]]] = None, dense_index: Any = None) -> None:
        self.rows = rows if rows is not None else corpus.load_rows()
        self.ids = [row["model_id"] for row in self.rows]
        self.dense = dense_index if dense_index is not None else dense.DenseIndex(self.rows)
        self.bm25 = corpus.bm25_index(self.rows)
        # Repo name (part after "/") -> row indices, most downloaded first.
        self._by_name: Dict[str, List[int]] = {}
        for index, row in enumerate(self.rows):
            self._by_name.setdefault(row["model_id"].split("/")[-1].casefold(), []).append(index)
        for indices in self._by_name.values():
            indices.sort(key=lambda i: -int((self.rows[i].get("popularity") or {}).get("current", {}).get("downloads") or 0))
        # Memoized per run so weight sweeps only redo fusion. Each entry keeps the
        # latency measured the first time, so p95/p99 stay realistic.
        self._eligible: Dict[str, np.ndarray] = {}
        self._query_vectors: Dict[str, Tuple[np.ndarray, float]] = {}
        self._dense_lists: Dict[Tuple[str, str], Tuple[List[str], float]] = {}
        self._sparse_lists: Dict[Tuple[str, str], Tuple[List[str], float]] = {}

    def eligible(self, hard_filters: Mapping[str, Any]) -> Tuple[str, np.ndarray]:
        key = json.dumps(hard_filters, sort_keys=True, ensure_ascii=False)
        if key not in self._eligible:
            self._eligible[key] = np.array(
                [index for index, row in enumerate(self.rows) if corpus.hard_filter(row, dict(hard_filters))],
                dtype=np.int64,
            )
        return key, self._eligible[key]

    def query_vector(self, text: str) -> Tuple[np.ndarray, float]:
        if text not in self._query_vectors:
            started = time.perf_counter()
            vector = dense.encode([text])[0]
            self._query_vectors[text] = (vector, (time.perf_counter() - started) * 1000.0)
        return self._query_vectors[text]

    def dense_list(self, text: str, filter_key: str, eligible: np.ndarray) -> Tuple[List[str], float]:
        cache_key = (text, filter_key)
        if cache_key not in self._dense_lists:
            vector, encode_ms = self.query_vector(text)
            started = time.perf_counter()
            scores = self.dense.matrix[eligible] @ vector
            order = np.argsort(-scores, kind="stable")[:CHANNEL_DEPTH]
            ranked = [self.ids[int(eligible[i])] for i in order]
            self._dense_lists[cache_key] = (ranked, encode_ms + (time.perf_counter() - started) * 1000.0)
        return self._dense_lists[cache_key]

    def sparse_list(self, text: str, filter_key: str, eligible: np.ndarray) -> Tuple[List[str], float]:
        cache_key = (text, filter_key)
        if cache_key not in self._sparse_lists:
            started = time.perf_counter()
            scores = self.bm25.score_all(text)[eligible]
            scored = [(float(scores[i]), self.ids[int(eligible[i])]) for i in np.flatnonzero(scores > 0)]
            scored.sort(key=lambda item: (-item[0], item[1]))
            ranked = [model_id for _, model_id in scored[:CHANNEL_DEPTH]]
            self._sparse_lists[cache_key] = (ranked, (time.perf_counter() - started) * 1000.0)
        return self._sparse_lists[cache_key]

    def name_lookup(self, text: str, eligible: np.ndarray) -> List[str]:
        """Models whose repo name the query spells out, in order of mention.

        A token matches a repo name exactly, or as a prefix followed by "-"
        (e.g. "kanana-1.5-2.1b-instruct" -> "kanana-1.5-2.1b-instruct-2505").
        Among same-named copies (GGUF, mirrors) the most downloaded eligible
        one wins, which is normally the original.
        """
        allowed = set(eligible.tolist())
        pinned: List[str] = []
        for token in NAME_TOKEN.findall(text):
            name = token.casefold()
            if len(name) < MIN_NAME_LENGTH:
                continue
            indices = self._by_name.get(name)
            if not indices:
                prefix = name + "-"
                indices = sorted(
                    (i for repo, group in self._by_name.items() if repo.startswith(prefix) for i in group),
                    key=lambda i: -int((self.rows[i].get("popularity") or {}).get("current", {}).get("downloads") or 0),
                )
            match = next((self.ids[i] for i in indices if i in allowed), None)
            if match and match not in pinned:
                pinned.append(match)
        return pinned

    def run(self, text: str, plan: RetrievalPlan) -> RunResult:
        transforms: Dict[str, List[str]] = {}
        pre_ms = 0.0
        for strategy in plan.strategies():
            result = pre_retrieval.transform(strategy, text)
            transforms[strategy] = result.outputs
            pre_ms = max(pre_ms, result.latency_ms)

        base = transforms["rewrite"][0] if "rewrite" in transforms else text
        variants = [base] + transforms.get("decomposition", []) + transforms.get("multi_query", [])
        sparse_queries = list(dict.fromkeys(variants))
        dense_queries = list(sparse_queries)
        if "hyde" in transforms:
            dense_queries[0] = transforms["hyde"][0]
            dense_queries = list(dict.fromkeys(dense_queries))

        filter_key, eligible = self.eligible(plan.hard_filters)
        dense_lists, sparse_lists = [], []
        dense_ms = sparse_ms = 0.0
        if len(eligible):
            for query in dense_queries:
                ranked, ms = self.dense_list(query, filter_key, eligible)
                dense_lists.append(ranked)
                dense_ms += ms
            for query in sparse_queries:
                ranked, ms = self.sparse_list(query, filter_key, eligible)
                sparse_lists.append(ranked)
                sparse_ms += ms

        started = time.perf_counter()
        fused = fusion.weighted_rrf(
            fusion.channel_lists(dense_lists, sparse_lists, plan.dense_weight, plan.sparse_weight),
            k=plan.rrf_k,
        )
        ranked = [model_id for model_id, _ in fused]
        if plan.use_name_lookup and len(eligible):
            pinned = self.name_lookup(text, eligible)
            ranked = pinned + [model_id for model_id in ranked if model_id not in pinned]
        fusion_ms = (time.perf_counter() - started) * 1000.0
        latency = {
            "pre_retrieval": round(pre_ms, 2),
            "dense": round(dense_ms, 2),
            "sparse": round(sparse_ms, 2),
            "fusion": round(fusion_ms, 2),
        }
        latency["total"] = round(sum(latency.values()), 2)
        return RunResult(
            ranked=ranked[: plan.top_k],
            latency_ms=latency,
            dense_queries=dense_queries,
            sparse_queries=sparse_queries,
            eligible_count=int(len(eligible)),
            transforms=transforms,
        )


def search(text: str, query_type: str, query: Mapping[str, Any], retriever: Optional[Retriever] = None) -> RunResult:
    """Plan with planner_config.json and run. Entry point for the service side."""
    from retrieval_lab.planner import plan_for

    return (retriever or Retriever()).run(text, plan_for(query_type, query))

