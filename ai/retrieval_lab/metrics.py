"""Retrieval metrics for the experiment table.

Relevance comes from the golden labels: expected_any (and expected_all for
comparisons) has grade 2, acceptable has grade 1. Recall/Precision/F1/Hit/MRR/MAP
count any grade >= min_grade as relevant; nDCG uses the grades.
"""

from __future__ import annotations

import math
from typing import Dict, Iterable, List, Mapping, Optional, Sequence

CUTOFFS = (5, 10)


def percentile(values: Sequence[float], q: float) -> Optional[float]:
    """Nearest-rank percentile (q in 0..100)."""
    if not values:
        return None
    ordered = sorted(values)
    rank = max(1, math.ceil(q / 100.0 * len(ordered)))
    return ordered[rank - 1]


def ranking_metrics(ranked: Sequence[str], grades: Mapping[str, int], min_grade: int = 1) -> Dict[str, float]:
    relevant = {model_id for model_id, grade in grades.items() if grade >= min_grade}
    out: Dict[str, float] = {}
    for k in CUTOFFS:
        top = list(ranked[:k])
        hits = sum(1 for model_id in top if model_id in relevant)
        recall = hits / len(relevant) if relevant else 0.0
        precision = hits / k
        out[f"recall@{k}"] = recall
        out[f"precision@{k}"] = precision
        out[f"f1@{k}"] = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        out[f"hit@{k}"] = 1.0 if hits else 0.0
        # Recall capped by k: a query with more relevant models than k can still reach 1.0.
        out[f"nrecall@{k}"] = hits / min(len(relevant), k) if relevant else 0.0

    top5 = list(ranked[:5])
    first = next((rank for rank, model_id in enumerate(top5, start=1) if model_id in relevant), None)
    out["mrr@5"] = 1.0 / first if first else 0.0

    precisions: List[float] = []
    hits = 0
    for rank, model_id in enumerate(top5, start=1):
        if model_id in relevant:
            hits += 1
            precisions.append(hits / rank)
    out["map@5"] = sum(precisions) / min(len(relevant), 5) if relevant else 0.0

    dcg = sum(grades.get(model_id, 0) / math.log2(rank + 1) for rank, model_id in enumerate(top5, start=1))
    ideal = sorted(grades.values(), reverse=True)[:5]
    idcg = sum(grade / math.log2(rank + 1) for rank, grade in enumerate(ideal, start=1))
    out["ndcg@5"] = dcg / idcg if idcg else 0.0
    return out


METRIC_KEYS = (
    "recall@5", "recall@10", "precision@5", "precision@10", "f1@5", "f1@10",
    "hit@10", "mrr@5", "ndcg@5", "map@5", "nrecall@5", "nrecall@10",
)


def aggregate(items: Iterable[Mapping[str, object]]) -> Dict[str, Optional[float]]:
    """Mean ranking metrics over scored queries, plus latency percentiles."""
    items = list(items)
    scored = [item for item in items if item.get("metrics")]
    out: Dict[str, Optional[float]] = {"queries": len(items), "scored_queries": len(scored)}
    for key in METRIC_KEYS:
        values = [float(item["metrics"][key]) for item in scored]  # type: ignore[index]
        out[key] = sum(values) / len(values) if values else None
    latencies = [float(item["latency_ms"]["total"]) for item in items if item.get("latency_ms")]  # type: ignore[index]
    out["p50_ms"] = percentile(latencies, 50)
    out["p95_ms"] = percentile(latencies, 95)
    out["p99_ms"] = percentile(latencies, 99)
    exclude = [item for item in items if item.get("must_exclude_checked")]
    out["must_exclude_violation_rate@10"] = (
        sum(1 for item in exclude if item.get("must_exclude_hits")) / len(exclude) if exclude else None
    )
    judged = [float(item["judged@10"]) for item in items if item.get("judged@10") is not None]  # type: ignore[arg-type]
    out["judged@10"] = sum(judged) / len(judged) if judged else None
    abstain = [item for item in items if item.get("expected_behavior") == "abstain"]
    out["abstention_accuracy"] = (
        sum(1 for item in abstain if not item.get("ranked")) / len(abstain) if abstain else None
    )
    return out
