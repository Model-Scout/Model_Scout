#!/usr/bin/env python3
"""structured_constraint에서 판정이 필요한 후보를 워크시트로 만든다.

lexical_worksheet와 목적은 같지만 근거가 다르다. 이 유형은 조건이 수치와
라이선스라 "조건을 만족하는가"를 세 값으로 적는다. 조건 값이 없어 판정할 수
없는 후보는 사람에게도 그 사실을 알려야 추측으로 점수를 주지 않는다.

structured_diagnose가 "라벨 공백"으로 분류한 6개 질의만 다룬다. "데이터 공백"
11개는 코퍼스에 조건 값이 없어 판정해도 근거를 댈 수 없으므로 제외한다.

실행:
    python -m retrieval_lab.structured_worksheet
    python -m retrieval_lab.structured_worksheet --all   # 미판정이 있는 질의 전부
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from retrieval_lab import structured_rules as rules

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
LABEL_DIR = ROOT / "test" / "golden" / "labels"
REPORT = ROOT / "retrieval_lab" / "reports" / "structured_constraint.json"
OUT_PATH = LABEL_DIR / "worksheet_structured_constraint.jsonl"
POOLS = ("core", "low_popularity")
QUERY_FILES = ("semantic_golden_queries.jsonl", "semantic_judged_queries.jsonl")

# structured_diagnose가 "라벨 공백"으로 분류한 질의.
LABEL_GAP_QUERIES = ["sg_g019", "sg_g027", "sg_h002", "sg_h033", "sg_h045", "sg_h064"]


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


def evidence_for(row: Dict[str, Any], conditions: Dict[str, Any]) -> str:
    """조건별 판정과 그 근거가 된 값을 한 줄로 모은다."""
    meta = row.get("filter_metadata") or {}
    states = rules.evaluate(row, conditions)
    marks = {True: "O", False: "X", None: "?"}
    parts = [f"{name}={marks[state]}" for name, state in states.items()]
    parts.append(f"task={meta.get('primary_task')}")
    parts.append(f"params={meta.get('parameter_count_billion')}")
    parts.append(f"ctx={meta.get('context_length')}")
    parts.append(f"license={meta.get('license')}")
    parts.append(f"downloads={meta.get('downloads')}")
    return " · ".join(str(part) for part in parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true",
                        help="라벨 공백 질의뿐 아니라 미판정이 있는 질의 전부")
    parser.add_argument("--top", type=int, default=10, help="질의당 상위 몇 개까지 볼지")
    args = parser.parse_args()

    corpus = load_corpus()
    queries = load_queries()
    report = json.loads(REPORT.read_text(encoding="utf-8"))

    wanted = None if args.all else set(LABEL_GAP_QUERIES)
    out_rows: List[Dict[str, Any]] = []
    counts: List[tuple] = []

    for entry in report["baseline"]["per_query"]:
        query_id = entry["query_id"]
        if wanted is not None and query_id not in wanted:
            continue
        query = queries.get(query_id)
        if query is None:
            continue
        conditions = rules.conditions_of(query)
        unjudged = set(entry.get("unjudged@10") or [])
        candidates = [model_id for model_id in entry["ranked"][:args.top]
                      if model_id in unjudged]
        for rank, model_id in enumerate(candidates, start=1):
            row = corpus.get(model_id)
            if row is None:
                continue
            state = rules.verdict(row, conditions)
            out_rows.append({
                "query_id": query_id,
                "model_id": model_id,
                "rank": rank,
                # 조건 위반이 확인된 것만 0을 제안한다. 판정 불가는 비워 둔다.
                "suggested": 0 if state is False else None,
                "score": None,
                "reason": "",
                "judge": "",
                "rule_verdict": {True: "충족", False: "위반", None: "판정불가"}[state],
                "unknown_fields": rules.unknown_fields(row, conditions),
                "violated_fields": rules.violated_fields(row, conditions),
                "evidence": evidence_for(row, conditions),
            })
        counts.append((query_id, sorted(conditions), len(candidates)))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as handle:
        for row in out_rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"워크시트 저장: {OUT_PATH.relative_to(ROOT)}")
    print(f"질의 {len(counts)}개 · 판정 후보 {len(out_rows)}개\n")
    print(f"{'질의':<10} {'조건':<42} {'후보':>4}")
    print("-" * 60)
    for query_id, conditions, count in counts:
        print(f"{query_id:<10} {','.join(conditions):<42} {count:>4}")

    tally: Dict[str, int] = {}
    for row in out_rows:
        tally[row["rule_verdict"]] = tally.get(row["rule_verdict"], 0) + 1
    print("\n규칙 판정:", " · ".join(f"{k} {v}" for k, v in sorted(tally.items())))
    print(f"규칙이 0점으로 제안: {tally.get('위반', 0)}개 "
          f"· 사람이 판단할 후보: {len(out_rows) - tally.get('위반', 0)}개")


if __name__ == "__main__":
    main()
