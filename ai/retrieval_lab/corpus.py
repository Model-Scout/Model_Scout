"""Corpus rows, hard filter, and the fielded BM25 index shared with 05_validate_retrieval.py."""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")


@lru_cache(maxsize=1)
def validator() -> Any:
    """Import 05_validate_retrieval.py so hard filters and BM25 match production."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("model_scout_validator", ROOT / "05_validate_retrieval.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import 05_validate_retrieval.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_rows() -> List[Dict[str, Any]]:
    """Stage 4 rows (Core + Low Popularity) without the OpenAI vectors."""
    sidecars = validator().load_benchmark_sidecars()
    rows: List[Dict[str, Any]] = []
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row = json.loads(line)
                row.pop("embedding", None)
                row["benchmark_metadata"] = row.get("benchmark_metadata") or sidecars.get(row.get("model_id"), {})
                rows.append(row)
    return rows


def hard_filter(row: Dict[str, Any], query: Dict[str, Any]) -> bool:
    return validator().hard_filter(row, query)[0]


class FastBM25:
    """Same scores as 05_validate_retrieval.FieldedBM25, computed for all rows at once.

    FieldedBM25.score recounts every row's term frequencies per call (~2 s per
    query over 3,606 rows), which would dominate the latency metrics. Here term
    frequencies are counted once and each query term's per-row contribution is
    cached as a vector.
    """

    def __init__(self, rows: List[Dict[str, Any]]) -> None:
        self.base = validator().FieldedBM25(rows)
        self.weights = self.base.FIELD_WEIGHTS
        self.term_freqs = [{field: Counter(doc[field]) for field in self.weights} for doc in self.base.documents]
        self.lengths = [{field: len(doc[field]) for field in self.weights} for doc in self.base.documents]
        self._term_scores: Dict[str, np.ndarray] = {}

    def term_scores(self, term: str) -> np.ndarray:
        if term not in self._term_scores:
            base, n_docs = self.base, max(1, len(self.base.rows))
            scores = np.zeros(len(self.term_freqs), dtype=np.float64)
            for field, weight in self.weights.items():
                df = base.doc_freq.get(field, {}).get(term, 0)
                if not df:
                    continue
                idf = math.log(1.0 + (n_docs - df + 0.5) / (df + 0.5))
                avg_len = base.avg_len.get(field) or 1.0
                for index, freqs in enumerate(self.term_freqs):
                    tf = freqs[field].get(term)
                    if tf:
                        denom = tf + base.k1 * (1.0 - base.b + base.b * self.lengths[index][field] / avg_len)
                        scores[index] += weight * idf * (tf * (base.k1 + 1.0) / denom)
            self._term_scores[term] = scores
        return self._term_scores[term]

    def score_all(self, text: str) -> np.ndarray:
        """Normalized BM25 score of every row, in row order (0 when no term matches)."""
        raw = np.zeros(len(self.term_freqs), dtype=np.float64)
        for term in validator().normalize_query_terms(str(text or "").casefold()):
            raw += self.term_scores(term)
        return np.clip(raw / (raw + 10.0), 0.0, 1.0)


def bm25_index(rows: List[Dict[str, Any]]) -> FastBM25:
    return FastBM25(rows)
