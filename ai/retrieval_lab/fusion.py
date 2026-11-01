"""Weighted Reciprocal Rank Fusion."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Sequence, Tuple

RRF_K = 60


def weighted_rrf(
    ranked_lists: Sequence[Tuple[float, Sequence[str]]],
    k: int = RRF_K,
) -> List[Tuple[str, float]]:
    """Fuse ranked ID lists: score(d) = sum_i w_i / (k + rank_i(d)).

    Each item of ``ranked_lists`` is ``(weight, ids_in_rank_order)``. Ties are
    broken by model ID so runs are deterministic.
    """
    scores: Dict[str, float] = defaultdict(float)
    for weight, ids in ranked_lists:
        if weight <= 0:
            continue
        for rank, model_id in enumerate(ids, start=1):
            scores[model_id] += weight / (k + rank)
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))


def channel_lists(
    dense_lists: Sequence[Sequence[str]],
    sparse_lists: Sequence[Sequence[str]],
    dense_weight: float,
    sparse_weight: float,
) -> List[Tuple[float, Sequence[str]]]:
    """Split each channel's weight evenly over its lists.

    With several query variants (multi-query, decomposition) a channel's total
    weight stays fixed, so dense_weight/sparse_weight mean the same thing in
    every experiment.
    """
    lists: List[Tuple[float, Sequence[str]]] = []
    for weight, group in ((dense_weight, dense_lists), (sparse_weight, sparse_lists)):
        if group:
            lists.extend((weight / len(group), ids) for ids in group)
    return lists
