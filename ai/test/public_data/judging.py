#!/usr/bin/env python3
"""Judging worksheet in/out for the public-data golden set (no API key).

    python test/public_data/judging.py export   # reports/public_pool.json -> reports/public_pool_worksheet.csv
    python test/public_data/judging.py import   # judged worksheet -> labels/public_data_golden.jsonl

Worksheet: one row per (query, candidate). Judges fill `score` and, for 0, `reason`:
  2  answers the query as asked (right topic, region, delivery, license)
  1  usable but partial: one of several needed datasets, a broader national set that
     includes the region, a file when an API was asked, a stale edition
  0  not useful; reason is one of off_topic / wrong_region / wrong_delivery / license / stale
  ?  cannot tell from the card (left blank or "?")
`note` is free text. Rows are shown in the pool's shuffled order; pool rank is not shown.

Score -> label (same rules as test/golden/import_judgments.py where they apply)
- 2 -> relevant grade 2, 1 -> relevant grade 1.
- 0 with a hard reason (wrong_region, wrong_delivery, license) -> must_exclude.
  Other 0s -> judged_irrelevant. ? -> unjudged.
- recommend query with no 2: 1s count as the answer and answer_grade="acceptable_only".
  No 1 or 2: evaluable=false (the pool missed; add pool_terms or judge more candidates).
- abstention query: any 1 or 2 means the catalog does cover it -> flagged in the summary,
  so the query is reworded or moved to recommend; it is not silently relabeled.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
POOL = HERE / "reports" / "public_pool.json"
WORKSHEET = HERE / "reports" / "public_pool_worksheet.csv"
QUERIES = HERE / "labels" / "public_data_queries.jsonl"
GOLDEN = HERE / "labels" / "public_data_golden.jsonl"
HARD_REASONS = {"wrong_region", "wrong_delivery", "license"}
REASONS = HARD_REASONS | {"off_topic", "stale"}
COLUMNS = [
    "query_id", "query_type", "query", "conditions", "aspects", "dataset_id", "title", "publisher",
    "regions", "delivery", "licenses", "last_modified", "regional_variant_count", "description", "url",
    "score", "reason", "note",
]  # fmt: skip


def export(args: argparse.Namespace) -> None:
    pool = json.loads(args.pool.read_text(encoding="utf-8"))
    rows = []
    for q in pool["queries"]:
        cond = {k: v for k, v in q["conditions"].items() if v not in (None, False, "any")}
        for c in q["candidates"]:
            rows.append(
                {
                    "query_id": q["query_id"],
                    "query_type": q["query_type"],
                    "query": q["query"],
                    "conditions": json.dumps(cond, ensure_ascii=False) if cond else "",
                    "aspects": " / ".join(q["aspects"]),
                    **{k: c.get(k) for k in ("dataset_id", "title", "publisher", "last_modified", "url")},
                    "regions": ",".join(c["regions"]),
                    "delivery": ",".join(c["delivery"]),
                    "licenses": ",".join(c["licenses"]),
                    "regional_variant_count": c["regional_variant_count"] or "",
                    "description": c["description"],
                    "score": "",
                    "reason": "",
                    "note": "",
                }
            )
    if args.worksheet.exists() and not args.force:
        raise SystemExit(f"{args.worksheet} exists (judging may be in it); pass --force to overwrite")
    with open(args.worksheet, "w", encoding="utf-8-sig", newline="") as f:  # BOM: Excel opens Korean
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} rows -> {args.worksheet}")


def read_marks(path: Path) -> dict[str, dict[str, dict[str, str]]]:
    marks: dict[str, dict[str, dict[str, str]]] = {}
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            score = (row.get("score") or "").strip()
            reason = (row.get("reason") or "").strip()
            if score not in {"", "?", "0", "1", "2"}:
                raise SystemExit(f"{row['query_id']} {row['dataset_id']}: score must be 0/1/2/?, got {score!r}")
            if score == "0" and reason and reason not in REASONS:
                raise SystemExit(f"{row['query_id']} {row['dataset_id']}: unknown reason {reason!r}")
            marks.setdefault(row["query_id"], {})[row["dataset_id"]] = {
                "score": score,
                "reason": reason,
                "note": row.get("note") or "",
            }
    return marks


def to_label(query: dict, judged: dict[str, dict[str, str]]) -> dict:
    relevant = {d: int(m["score"]) for d, m in judged.items() if m["score"] in {"1", "2"}}
    zeros = {d: m["reason"] for d, m in judged.items() if m["score"] == "0"}
    label = {
        **{k: query[k] for k in ("query_id", "query_type", "query", "domain", "conditions", "expected_behavior")},
        "dataset_terms": query["pool_terms"],
        "relevant": relevant,
        "must_exclude": sorted(d for d, r in zeros.items() if r in HARD_REASONS),
        "judged_irrelevant": sorted(d for d, r in zeros.items() if r not in HARD_REASONS),
        "unjudged": sorted(d for d, m in judged.items() if m["score"] in {"", "?"}),
        "answer_grade": "full" if 2 in relevant.values() else "acceptable_only" if relevant else None,
    }
    if query["expected_behavior"] == "abstain":
        label["evaluable"] = bool(judged) and not label["unjudged"]
    else:
        label["evaluable"] = bool(relevant)
    return label


def import_(args: argparse.Namespace) -> None:
    queries = [json.loads(line) for line in args.queries.read_text(encoding="utf-8").splitlines() if line.strip()]
    marks = read_marks(args.worksheet)
    labels = [to_label(q, marks.get(q["query_id"], {})) for q in queries]
    with open(args.golden, "w", encoding="utf-8") as f:
        for label in labels:
            f.write(json.dumps(label, ensure_ascii=False) + "\n")
    status = Counter(
        "abstain_covered" if lb["expected_behavior"] == "abstain" and lb["relevant"]
        else "evaluable" if lb["evaluable"] else "not_evaluable"
        for lb in labels
    )  # fmt: skip
    print(f"{len(labels)} labels -> {args.golden}: {dict(status)}")
    for lb in labels:
        if lb["expected_behavior"] == "abstain" and lb["relevant"]:
            print(f"  {lb['query_id']}: abstention query has relevant datasets {sorted(lb['relevant'])}; reword it")
        elif not lb["evaluable"]:
            print(f"  {lb['query_id']}: not evaluable ({len(lb['unjudged'])} unjudged)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    ex = sub.add_parser("export")
    ex.add_argument("--pool", type=Path, default=POOL)
    ex.add_argument("--worksheet", type=Path, default=WORKSHEET)
    ex.add_argument("--force", action="store_true")
    im = sub.add_parser("import")
    im.add_argument("--worksheet", type=Path, default=WORKSHEET)
    im.add_argument("--queries", type=Path, default=QUERIES)
    im.add_argument("--golden", type=Path, default=GOLDEN)
    args = parser.parse_args()
    export(args) if args.command == "export" else import_(args)


if __name__ == "__main__":
    main()
