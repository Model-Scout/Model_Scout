#!/usr/bin/env python3
"""저장된 Baseline 결과에 조건 규칙을 입혀 structured_constraint 질의를 분류한다.

lexical_diagnose와 같은 목적이지만 판정이 세 값이라 분류도 하나 더 늘어난다.

    정상          Recall이 0보다 큼
    라벨 공백     조건을 만족한 결과가 많은데 Recall이 0 — 판정하면 오른다
    데이터 공백   조건 값을 몰라 판정 불가한 결과가 많음 — 코퍼스를 채워야 한다
    검색 실패     조건을 어긴 결과가 많음 — 검색이나 필터를 고쳐야 한다

검색을 다시 돌리지 않는다. 리포트에 저장된 ranked 목록을 그대로 쓴다.

실행:
    python -m retrieval_lab.structured_diagnose
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from retrieval_lab import structured_rules as rules

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
LABEL_DIR = ROOT / "test" / "golden" / "labels"
REPORT = ROOT / "retrieval_lab" / "reports" / "structured_constraint.json"
POOLS = ("core", "low_popularity")
QUERY_FILES = ("semantic_golden_queries.jsonl", "semantic_judged_queries.jsonl")

OK_HIGH = 0.3        # 조건 충족이 이 이상이면 라벨만 채우면 된다고 본다
UNKNOWN_HIGH = 0.5   # 판정 불가가 이 이상이면 데이터 공백이 지배적이다


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


def load_queries() -> Dict[str, Dict[str, Any]]:
    queries: Dict[str, Dict[str, Any]] = {}
    for name in QUERY_FILES:
        path = LABEL_DIR / name
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    item = json.loads(line)
                    queries[item["id"]] = item
    return queries


def classify(recall: float, scored: Dict[str, float]) -> str:
    if recall > 0:
        return "정상"
    if scored["cond_unknown@10"] >= UNKNOWN_HIGH:
        return "데이터 공백"
    if scored["cond_ok@10"] >= OK_HIGH:
        return "라벨 공백"
    return "검색 실패"


def main() -> None:
    corpus = load_corpus()
    queries = load_queries()
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    per_query: List[Dict[str, Any]] = report["baseline"]["per_query"]
    print(f"코퍼스 {len(corpus):,}개 · Baseline {report['ran_at']} · 질의 {len(per_query)}개\n")

    rows = []
    for entry in per_query:
        query = queries.get(entry["query_id"])
        if query is None:
            print(f"  질의 정의 없음: {entry['query_id']}")
            continue
        conditions = rules.conditions_of(query)
        scored = rules.score(entry["ranked"], corpus, conditions)
        metrics = entry.get("metrics") or {}
        recall = metrics.get("recall@10", 0.0)
        rows.append({
            "query_id": entry["query_id"],
            "recall@10": recall,
            "judged@10": entry.get("judged@10", 0.0),
            "ok": scored["cond_ok@10"],
            "violation": scored["cond_violation@10"],
            "unknown": scored["cond_unknown@10"],
            "verdict": classify(recall, scored),
            "conditions": sorted(conditions),
        })

    header = (f"{'질의':<10} {'Recall@10':>9} {'judged':>7} {'충족':>6} "
              f"{'위반':>6} {'판정불가':>8}  판정")
    print(header)
    print("-" * len(header))
    for row in sorted(rows, key=lambda item: (item["verdict"], -item["ok"])):
        print(f"{row['query_id']:<10} {row['recall@10']:>9.2f} {row['judged@10']:>7.2f} "
              f"{row['ok']:>6.2f} {row['violation']:>6.2f} {row['unknown']:>8.2f}  "
              f"{row['verdict']}")

    print("\n=== 판정별 ===")
    buckets: Dict[str, List[str]] = {}
    for row in rows:
        buckets.setdefault(row["verdict"], []).append(row["query_id"])
    for verdict, ids in sorted(buckets.items(), key=lambda item: -len(item[1])):
        print(f"{verdict:<12} {len(ids):>2}개  {', '.join(ids)}")

    print("\n=== 평균 ===")
    count = len(rows) or 1
    for key, label in (("ok", "조건 충족"), ("violation", "조건 위반"), ("unknown", "판정 불가")):
        print(f"{label:<10} {sum(row[key] for row in rows) / count:.3f}")

    # 수치 조건이 있는 질의와 없는 질의를 나눠서 본다.
    numeric = [row for row in rows
               if {"max_parameters_billion", "min_context_length"} & set(row["conditions"])]
    other = [row for row in rows if row not in numeric]
    for group, label in ((numeric, "수치 조건 있음"), (other, "수치 조건 없음")):
        if not group:
            continue
        size = len(group)
        print(f"\n{label} ({size}개)  충족 {sum(r['ok'] for r in group)/size:.3f} · "
              f"위반 {sum(r['violation'] for r in group)/size:.3f} · "
              f"판정불가 {sum(r['unknown'] for r in group)/size:.3f}")


if __name__ == "__main__":
    main()
