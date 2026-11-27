"""순위 목록 하나를 등급 라벨(id → 0/1/2)로 채점한다. 모델·공공데이터 A/B 가 같은 식을 쓴다.

    nDCG@k   이득 2^g − 1, 이상적 순서는 라벨 전체에서 잡는다
    P@k      상위 k 중 정답 비율(목록이 k 보다 짧으면 빈 칸은 오답)
    R@k      상위 k 에 든 정답 / min(k, 정답 수). 정답이 수백 개인 역할(한국어 LLM 등)은 보통 recall 의
             천장이 k/정답수라 비교가 안 되므로, k 칸을 다 채울 수 있는 만큼을 분모로 둔다
    MRR@10   상위 10 안 첫 정답 순위의 역수
    Hit@k    상위 k 에 정답이 하나라도 있으면 1

min_grade 2 는 "그 일을 하라고 만든 모델/데이터", 1 은 "쓸 수는 있는 것"까지다. 판정되지 않은 id 는 0점이다.
"""

from __future__ import annotations

import math
import random
from collections.abc import Mapping, Sequence

KS = (3, 5, 10)
BOOTSTRAP = 5000


def dcg(gains: Sequence[float]) -> float:
    return sum(g / math.log2(i + 2) for i, g in enumerate(gains))


def score(ranked: Sequence[str], labels: Mapping[str, int], min_grade: int) -> dict[str, float]:
    grades = [labels.get(item, 0) for item in ranked]
    relevant = sum(1 for g in labels.values() if g >= min_grade)
    ideal = sorted(labels.values(), reverse=True)
    out: dict[str, float] = {}
    for k in KS:
        top = grades[:k]
        hits = sum(1 for g in top if g >= min_grade)
        best = dcg([2 ** g - 1 for g in ideal[:k]])
        out[f"ndcg@{k}"] = dcg([2 ** g - 1 for g in top]) / best if best else 0.0
        out[f"p@{k}"] = hits / k
        out[f"r@{k}"] = hits / min(k, relevant) if relevant else 0.0
        out[f"hit@{k}"] = float(hits > 0)
    first = next((i for i, g in enumerate(grades[:10], 1) if g >= min_grade), None)
    out["mrr@10"] = 1 / first if first else 0.0
    return out


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def paired(a: Sequence[float], b: Sequence[float], seed: str = "rerank-ab") -> dict[str, float]:
    """b − a 의 평균과 95% 부트스트랩 구간. 단위(질문)를 다시 뽑는다."""
    deltas = [y - x for x, y in zip(a, b)]
    rng = random.Random(seed)
    n = len(deltas)
    means = sorted(mean([deltas[rng.randrange(n)] for _ in range(n)]) for _ in range(BOOTSTRAP)) if n else [0.0]
    return {"a": mean(a), "b": mean(b), "delta": mean(deltas),
            "lo": means[int(0.025 * len(means))], "hi": means[int(0.975 * len(means)) - 1],
            "up": sum(d > 1e-9 for d in deltas), "down": sum(d < -1e-9 for d in deltas), "n": n}
