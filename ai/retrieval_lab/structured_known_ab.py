#!/usr/bin/env python3
"""require_known_parameters / require_known_context A/B.

structured_constraint 진단에서 24개 질의 중 11개가 "데이터 공백"으로 분류됐다.
top-10의 53%가 조건 값이 없어 판정할 수 없는 모델이고, 수치 조건이 붙은 질의
15개만 보면 71%다. 코퍼스의 parameter_count 39%, context_length 38%가 비어
있기 때문이다.

하드 필터는 그 모델들을 기본값(require_known=false)에서 통과시킨다. 이 스크립트는
켰을 때와 껐을 때를 같은 질의·같은 검색 설정으로 비교한다.

    lenient   값이 없는 모델도 통과 (현재 기본값)
    strict    값을 아는 모델만 통과

측정은 골든셋 지표(Recall·Precision 등)와 조건 규칙 지표(충족·위반·판정불가)를
함께 본다. 라벨이 부족한 유형이라 Recall만으로는 판단할 수 없기 때문이다.

실행:
    python -m retrieval_lab.structured_known_ab
"""

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List

from retrieval_lab import golden, metrics, structured_rules as rules
from retrieval_lab.pipeline import Retriever
from retrieval_lab.planner import BASELINE, HARD_FILTER_KEYS

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")
QUERY_TYPE = "structured_constraint"
TOP_K = 10


def load_corpus() -> Dict[str, Dict[str, Any]]:
    corpus: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    corpus[row["model_id"]] = row
    return corpus


def run(retriever: Retriever, queries, corpus, *, strict: bool) -> Dict[str, Any]:
    """같은 설정에서 require_known 두 값만 바꿔 돌린다."""
    per_query: List[Dict[str, Any]] = []
    for query in queries:
        filters = {key: value for key, value in query.query.items()
                   if key in HARD_FILTER_KEYS and value is not None}
        if strict:
            # 조건이 걸린 항목만 엄격하게 본다. 조건이 없으면 켤 이유가 없다.
            if filters.get("max_parameters_billion") is not None:
                filters["require_known_parameters"] = True
            if filters.get("min_context_length") is not None:
                filters["require_known_context"] = True
        plan = replace(BASELINE, query_type=QUERY_TYPE, hard_filters=filters)
        ranked = retriever.run(query.text, plan).ranked[:TOP_K]
        conditions = rules.conditions_of(query.query)
        scored = rules.score(ranked, corpus, conditions, ks=(TOP_K,))
        relevant = {model_id for model_id, grade in query.grades.items() if grade >= 1}
        hits = len(set(ranked) & relevant)
        per_query.append({
            "query_id": query.query_id,
            "returned": len(ranked),
            "recall": hits / len(relevant) if relevant else None,
            "judged": (sum(1 for m in ranked if m in query.judged) / TOP_K)
                      if query.judged is not None else None,
            "must_exclude_hit": bool(set(ranked) & set(query.must_exclude)),
            **{key.replace(f"@{TOP_K}", ""): value for key, value in scored.items()},
        })
    return {"per_query": per_query}


def summarize(result: Dict[str, Any]) -> Dict[str, float]:
    rows = result["per_query"]
    size = len(rows) or 1
    recalls = [row["recall"] for row in rows if row["recall"] is not None]
    judged = [row["judged"] for row in rows if row["judged"] is not None]
    return {
        "returned": sum(row["returned"] for row in rows) / size,
        "empty": sum(1 for row in rows if row["returned"] == 0),
        "recall": sum(recalls) / len(recalls) if recalls else 0.0,
        "judged": sum(judged) / len(judged) if judged else 0.0,
        "cond_ok": sum(row["cond_ok"] for row in rows) / size,
        "cond_violation": sum(row["cond_violation"] for row in rows) / size,
        "cond_unknown": sum(row["cond_unknown"] for row in rows) / size,
        "must_exclude": sum(1 for row in rows if row["must_exclude_hit"]) / size,
    }


def main() -> None:
    corpus = load_corpus()
    retriever = Retriever()
    corpus_ids = set(retriever.ids)
    supplement = ROOT / "test" / "golden" / "labels" / "supplement_structured_constraint.jsonl"
    queries = golden.load(corpus_ids=corpus_ids, types=[QUERY_TYPE],
                          supplement_path=supplement if supplement.exists() else None)
    print(f"코퍼스 {len(corpus):,}개 · 질의 {len(queries)}개 · top-{TOP_K}\n")

    results = {name: run(retriever, queries, corpus, strict=(name == "strict"))
               for name in ("lenient", "strict")}
    summaries = {name: summarize(result) for name, result in results.items()}

    print(f"{'':<10} {'반환수':>7} {'빈결과':>6} {'Recall':>7} {'Judged':>7} "
          f"{'충족':>6} {'위반':>6} {'판정불가':>8} {'제외위반':>8}")
    print("-" * 74)
    for name, row in summaries.items():
        label = "lenient(현재)" if name == "lenient" else "strict"
        print(f"{label:<10} {row['returned']:>7.1f} {row['empty']:>6} {row['recall']:>7.3f} "
              f"{row['judged']:>7.3f} {row['cond_ok']:>6.3f} {row['cond_violation']:>6.3f} "
              f"{row['cond_unknown']:>8.3f} {row['must_exclude']:>8.3f}")

    print("\n=== 질의별 (수치 조건이 있는 것만) ===")
    lenient = {row["query_id"]: row for row in results["lenient"]["per_query"]}
    strict = {row["query_id"]: row for row in results["strict"]["per_query"]}
    numeric = [q for q in queries
               if q.query.get("max_parameters_billion") is not None
               or q.query.get("min_context_length") is not None]
    print(f"{'질의':<10} {'반환 L→S':>12} {'Recall L→S':>14} {'판정불가 L→S':>16}")
    print("-" * 56)
    for query in numeric:
        left, right = lenient[query.query_id], strict[query.query_id]
        recall_left = "-" if left["recall"] is None else f"{left['recall']:.2f}"
        recall_right = "-" if right["recall"] is None else f"{right['recall']:.2f}"
        print(f"{query.query_id:<10} {left['returned']:>5} → {right['returned']:<4} "
              f"{recall_left:>7} → {recall_right:<5} "
              f"{left['cond_unknown']:>7.2f} → {right['cond_unknown']:<5.2f}")


if __name__ == "__main__":
    main()
